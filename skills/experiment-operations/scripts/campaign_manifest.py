#!/usr/bin/env python3
"""Atomic mechanical bookkeeping for multi-run research campaigns."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import sys
import tempfile
import uuid


STATUSES = {"planned", "claimed", "running", "completed", "failed", "invalidated", "cancelled"}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    if not data.get("campaignId"):
        errors.append("campaignId is required")
    if not isinstance(data.get("protocol"), dict):
        errors.append("protocol must be an object")
    cells = data.get("cells")
    if not isinstance(cells, list) or not cells:
        errors.append("cells must be a non-empty array")
        return errors

    ids: set[str] = set()
    fingerprints: dict[str, str] = {}
    for index, cell in enumerate(cells):
        prefix = f"cells[{index}]"
        cell_id = cell.get("cellId")
        fingerprint = cell.get("fingerprint")
        if not cell_id:
            errors.append(f"{prefix}.cellId is required")
        elif cell_id in ids:
            errors.append(f"duplicate cellId: {cell_id}")
        else:
            ids.add(cell_id)
        if not fingerprint:
            errors.append(f"{prefix}.fingerprint is required")
        elif fingerprint in fingerprints:
            errors.append(
                f"duplicate fingerprint: {fingerprint} in {fingerprints[fingerprint]} and {cell_id}"
            )
        else:
            fingerprints[fingerprint] = cell_id or prefix
        if cell.get("status") not in STATUSES:
            errors.append(f"{prefix}.status must be one of {sorted(STATUSES)}")
        if not isinstance(cell.get("dependencies", []), list):
            errors.append(f"{prefix}.dependencies must be an array")
        if not isinstance(cell.get("attempts", []), list):
            errors.append(f"{prefix}.attempts must be an array")

    for cell in cells:
        for dependency in cell.get("dependencies", []):
            if dependency not in ids:
                errors.append(f"{cell.get('cellId')} has unknown dependency {dependency}")
    return errors


def atomic_write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        with contextlib.suppress(FileNotFoundError):
            os.unlink(temp_name)


@contextlib.contextmanager
def locked(path: Path):
    lock_path = Path(f"{path}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        data = load(path)
        errors = validate(data)
        if errors:
            raise ValueError("; ".join(errors))
        yield data


def find_cell(data: dict, cell_id: str) -> dict:
    for cell in data["cells"]:
        if cell["cellId"] == cell_id:
            return cell
    raise ValueError(f"unknown cellId: {cell_id}")


def dependencies_complete(data: dict, cell: dict) -> bool:
    by_id = {item["cellId"]: item for item in data["cells"]}
    return all(by_id[dep]["status"] == "completed" for dep in cell.get("dependencies", []))


def cmd_validate(args: argparse.Namespace) -> dict:
    data = load(args.manifest)
    errors = validate(data)
    if errors:
        raise ValueError("; ".join(errors))
    return {"valid": True, "cells": len(data["cells"])}


def cmd_summary(args: argparse.Namespace) -> dict:
    data = load(args.manifest)
    errors = validate(data)
    if errors:
        raise ValueError("; ".join(errors))
    counts = {status: 0 for status in sorted(STATUSES)}
    for cell in data["cells"]:
        counts[cell["status"]] += 1
    return {"campaignId": data["campaignId"], "total": len(data["cells"]), "counts": counts}


def cmd_claim(args: argparse.Namespace) -> dict:
    with locked(args.manifest) as data:
        candidates = [find_cell(data, args.cell)] if args.cell else data["cells"]
        cell = next(
            (item for item in candidates if item["status"] == "planned" and dependencies_complete(data, item)),
            None,
        )
        if cell is None:
            raise ValueError("no dependency-ready planned cell")
        token = uuid.uuid4().hex
        cell["status"] = "claimed"
        cell["claim"] = {"worker": args.worker, "token": token, "claimedAt": now()}
        atomic_write(args.manifest, data)
        return {"cell": cell, "leaseToken": token}


def require_claim(cell: dict, token: str) -> None:
    if cell.get("claim", {}).get("token") != token:
        raise ValueError("lease token does not own this cell")


def cmd_start(args: argparse.Namespace) -> dict:
    with locked(args.manifest) as data:
        cell = find_cell(data, args.cell)
        require_claim(cell, args.token)
        if cell["status"] != "claimed":
            raise ValueError(f"cell is {cell['status']}, expected claimed")
        attempt_path = Path(args.attempt_path)
        attempt_path.mkdir(parents=True, exist_ok=False)
        attempt = len(cell.setdefault("attempts", [])) + 1
        record = {
            "attempt": attempt,
            "runId": args.run_id,
            "worker": cell["claim"]["worker"],
            "attemptPath": str(attempt_path),
            "startedAt": now(),
            "status": "running",
        }
        cell["attempts"].append(record)
        cell["status"] = "running"
        atomic_write(args.manifest, data)
        return {"cellId": cell["cellId"], "attempt": record}


def current_attempt(cell: dict) -> dict:
    attempts = cell.get("attempts", [])
    if not attempts:
        raise ValueError("cell has no started attempt")
    return attempts[-1]


def parse_artifacts(values: list[str]) -> dict[str, str]:
    artifacts: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"artifact must be NAME=PATH: {value}")
        name, path = value.split("=", 1)
        if not name or not path:
            raise ValueError(f"artifact must be NAME=PATH: {value}")
        if not Path(path).exists():
            raise ValueError(f"artifact does not exist: {path}")
        artifacts[name] = path
    return artifacts


def require_within_attempt(path: Path, attempt: dict, label: str) -> None:
    attempt_root = Path(attempt["attemptPath"]).resolve()
    resolved = path.resolve()
    try:
        resolved.relative_to(attempt_root)
    except ValueError as error:
        raise ValueError(f"{label} must be inside active attempt path: {resolved}") from error


def cmd_complete(args: argparse.Namespace) -> dict:
    if not args.marker.exists():
        raise ValueError(f"completion marker does not exist: {args.marker}")
    artifacts = parse_artifacts(args.artifact)
    with locked(args.manifest) as data:
        cell = find_cell(data, args.cell)
        require_claim(cell, args.token)
        attempt = current_attempt(cell)
        if cell["status"] != "running" or attempt["runId"] != args.run_id:
            raise ValueError("run identity does not match the active attempt")
        require_within_attempt(args.marker, attempt, "completion marker")
        for name, artifact in artifacts.items():
            require_within_attempt(Path(artifact), attempt, f"artifact {name}")
        attempt.update(
            status="completed",
            completedAt=now(),
            completionMarker=str(args.marker),
            artifacts=artifacts,
        )
        cell["status"] = "completed"
        cell.pop("claim", None)
        atomic_write(args.manifest, data)
        return {"cellId": cell["cellId"], "attempt": attempt}


def cmd_fail(args: argparse.Namespace) -> dict:
    with locked(args.manifest) as data:
        cell = find_cell(data, args.cell)
        require_claim(cell, args.token)
        attempt = current_attempt(cell)
        if attempt["runId"] != args.run_id:
            raise ValueError("run identity does not match the active attempt")
        attempt.update(status="failed", finishedAt=now(), failure=args.reason)
        cell["status"] = "failed"
        cell.pop("claim", None)
        atomic_write(args.manifest, data)
        return {"cellId": cell["cellId"], "attempt": attempt}


def cmd_requeue(args: argparse.Namespace) -> dict:
    with locked(args.manifest) as data:
        cell = find_cell(data, args.cell)
        if cell["status"] not in {"claimed", "running", "failed"}:
            raise ValueError(f"cannot requeue cell in status {cell['status']}")
        if cell["status"] == "running":
            attempt = current_attempt(cell)
            attempt.update(status="interrupted", finishedAt=now(), interruption=args.reason)
        cell["status"] = "planned"
        cell.pop("claim", None)
        cell["requeueReason"] = args.reason
        cell["requeuedAt"] = now()
        atomic_write(args.manifest, data)
        return {"cellId": cell["cellId"], "status": "planned"}


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser()
    sub = root.add_subparsers(dest="command", required=True)
    for name in ("validate", "summary"):
        command = sub.add_parser(name)
        command.add_argument("manifest", type=Path)
    claim = sub.add_parser("claim")
    claim.add_argument("manifest", type=Path)
    claim.add_argument("--worker", required=True)
    claim.add_argument("--cell")
    start = sub.add_parser("start")
    start.add_argument("manifest", type=Path)
    start.add_argument("--cell", required=True)
    start.add_argument("--token", required=True)
    start.add_argument("--run-id", required=True)
    start.add_argument("--attempt-path", required=True, type=Path)
    complete = sub.add_parser("complete")
    complete.add_argument("manifest", type=Path)
    complete.add_argument("--cell", required=True)
    complete.add_argument("--token", required=True)
    complete.add_argument("--run-id", required=True)
    complete.add_argument("--marker", required=True, type=Path)
    complete.add_argument("--artifact", action="append", default=[])
    fail = sub.add_parser("fail")
    fail.add_argument("manifest", type=Path)
    fail.add_argument("--cell", required=True)
    fail.add_argument("--token", required=True)
    fail.add_argument("--run-id", required=True)
    fail.add_argument("--reason", required=True)
    requeue = sub.add_parser("requeue")
    requeue.add_argument("manifest", type=Path)
    requeue.add_argument("--cell", required=True)
    requeue.add_argument("--reason", required=True)
    return root


def main() -> int:
    args = parser().parse_args()
    commands = {
        "validate": cmd_validate,
        "summary": cmd_summary,
        "claim": cmd_claim,
        "start": cmd_start,
        "complete": cmd_complete,
        "fail": cmd_fail,
        "requeue": cmd_requeue,
    }
    try:
        result = commands[args.command](args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
