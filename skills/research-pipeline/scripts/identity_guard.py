#!/usr/bin/env python3
"""Validate or initialize sealed research-project identity metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


FIELDS = (
    "research_object",
    "input_artifact",
    "intervention_locus",
    "load_bearing_primitive",
    "value_metric",
    "benchmark_family",
    "baseline_community",
    "target_audience",
)
APPROVED_TRANSITIONS = {"same_project", "user_approved", "approved_new_project"}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def transition_is_approved(data: dict) -> bool:
    authority = data.get("transition_authority", {})
    return (
        isinstance(authority, dict)
        and authority.get("status") in APPROVED_TRANSITIONS
        and bool(authority.get("source") or authority.get("context_source"))
        and bool(authority.get("user_quote"))
    )


def boundary_changes(origin: dict, current: dict) -> tuple[list[str], bool]:
    changed = [field for field in FIELDS if origin.get(field) != current.get(field)]
    changed_set = set(changed)
    boundary = (
        "research_object" in changed_set
        or "target_audience" in changed_set
        or len(changed) >= 3
        or {"load_bearing_primitive", "benchmark_family"} <= changed_set
        or {"input_artifact", "intervention_locus", "value_metric"} <= changed_set
    )
    return changed, boundary


def check(project: Path) -> int:
    origin_path = project / "PROGRAM_ORIGIN.md"
    identity_path = project / "PROJECT_IDENTITY.json"
    if not origin_path.exists():
        print(json.dumps({"status": "BLOCK", "reason": "PROGRAM_ORIGIN.md missing"}))
        return 2
    origin_text = origin_path.read_text(encoding="utf-8", errors="replace")
    if not identity_path.exists():
        if "PROVISIONAL" in origin_text.upper():
            print(json.dumps({"status": "PROVISIONAL", "reason": "identity awaits user confirmation"}))
            return 0
        print(json.dumps({"status": "BLOCK", "reason": "PROJECT_IDENTITY.json missing"}))
        return 2

    try:
        data = load_json(identity_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCK", "reason": str(exc)}))
        return 2

    origin = data.get("origin")
    current = data.get("current")
    if not isinstance(origin, dict) or not isinstance(current, dict):
        print(json.dumps({"status": "BLOCK", "reason": "origin/current objects required"}))
        return 2
    missing = [f"origin.{field}" for field in FIELDS if not origin.get(field)]
    missing += [f"current.{field}" for field in FIELDS if not current.get(field)]
    if missing:
        print(json.dumps({"status": "BLOCK", "reason": "missing identity fields", "fields": missing}))
        return 2

    seals = data.get("seals", {})
    seal_errors: list[str] = []
    if isinstance(seals, dict) and seals:
        expected_origin_file = seals.get("program_origin_sha256")
        expected_origin_object = seals.get("origin_object_sha256")
        if expected_origin_file and expected_origin_file != sha256_bytes(origin_path.read_bytes()):
            seal_errors.append("PROGRAM_ORIGIN.md changed after sealing")
        if expected_origin_object and expected_origin_object != canonical_hash(origin):
            seal_errors.append("PROJECT_IDENTITY.json origin changed after sealing")
    if seal_errors:
        print(json.dumps({"status": "BLOCK", "reason": "seal mismatch", "errors": seal_errors}))
        return 2

    changed, boundary = boundary_changes(origin, current)
    approved = transition_is_approved(data)
    if boundary and not approved:
        print(
            json.dumps(
                {
                    "status": "BLOCK",
                    "reason": "unapproved project-boundary change",
                    "changed_fields": changed,
                },
                ensure_ascii=False,
            )
        )
        return 2

    status = "PASS" if seals else "PASS_UNSEALED"
    print(
        json.dumps(
            {
                "status": status,
                "changed_fields": changed,
                "transition_approved": approved,
                "project": str(project),
            },
            ensure_ascii=False,
        )
    )
    return 0


def init_project(project: Path) -> int:
    project.mkdir(parents=True, exist_ok=True)
    origin_path = project / "PROGRAM_ORIGIN.md"
    identity_path = project / "PROJECT_IDENTITY.json"
    existing = [str(path) for path in (origin_path, identity_path) if path.exists()]
    if existing:
        print(json.dumps({"status": "NO_CHANGE", "existing": existing}))
        return 0

    origin_path.write_text(
        "# PROGRAM_ORIGIN - PROVISIONAL\n\n"
        "Status: PROVISIONAL / UNSEALED / pending user confirmation.\n\n"
        "## Exact User Wording\n\n"
        "> TODO: insert the recoverable user-authored origin with source and timestamp.\n",
        encoding="utf-8",
    )
    empty = {field: "" for field in FIELDS}
    identity_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "origin": empty,
                "current": dict(empty),
                "transition_authority": {"status": "pending_user_confirmation"},
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "INITIALIZED_PROVISIONAL", "project": str(project)}))
    return 0


def seal_origin(project: Path) -> int:
    origin_path = project / "PROGRAM_ORIGIN.md"
    identity_path = project / "PROJECT_IDENTITY.json"
    if not origin_path.exists() or not identity_path.exists():
        print(json.dumps({"status": "BLOCK", "reason": "identity files missing"}))
        return 2
    origin_text = origin_path.read_text(encoding="utf-8", errors="replace")
    if "PROVISIONAL" in origin_text.upper():
        print(json.dumps({"status": "BLOCK", "reason": "provisional origin cannot be sealed"}))
        return 2
    data = load_json(identity_path)
    origin = data.get("origin")
    if not isinstance(origin, dict) or any(not origin.get(field) for field in FIELDS):
        print(json.dumps({"status": "BLOCK", "reason": "complete origin object required"}))
        return 2
    data["seals"] = {
        "program_origin_sha256": sha256_bytes(origin_path.read_bytes()),
        "origin_object_sha256": canonical_hash(origin),
    }
    identity_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "SEALED", "project": str(project)}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "init-project", "seal-origin"):
        command = subparsers.add_parser(name)
        command.add_argument("--project", type=Path, default=Path.cwd())
    args = parser.parse_args()
    project = args.project.expanduser().resolve()
    if args.command == "check":
        return check(project)
    if args.command == "init-project":
        return init_project(project)
    return seal_origin(project)


if __name__ == "__main__":
    sys.exit(main())
