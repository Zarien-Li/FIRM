#!/usr/bin/env python3
"""Validate claim-bearing evidence lineage and compute invalidation impact."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path


ALLOWED_STATUSES = {"provisional", "valid", "invalidated", "superseded"}


def load_registry(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("schema_version") != 1 or not isinstance(data.get("evidence"), dict):
        raise ValueError("registry must have schema_version=1 and an evidence object")
    return data


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    evidence = data["evidence"]
    for evidence_id, item in evidence.items():
        if not isinstance(item, dict):
            errors.append(f"{evidence_id}: entry is not an object")
            continue
        if item.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{evidence_id}: invalid status {item.get('status')!r}")
        for field in ("depends_on", "artifacts", "supports"):
            if not isinstance(item.get(field, []), list):
                errors.append(f"{evidence_id}: {field} must be a list")
        for dependency in item.get("depends_on", []):
            if dependency not in evidence:
                errors.append(f"{evidence_id}: unknown dependency {dependency!r}")
    return errors


def descendants(data: dict, roots: set[str]) -> set[str]:
    reverse: dict[str, set[str]] = defaultdict(set)
    for evidence_id, item in data["evidence"].items():
        for dependency in item.get("depends_on", []):
            reverse[dependency].add(evidence_id)

    impacted = set(roots)
    queue = deque(roots)
    while queue:
        current = queue.popleft()
        for child in reverse.get(current, set()):
            if child not in impacted:
                impacted.add(child)
                queue.append(child)
    return impacted


def scan_assets(
    data: dict, paths: list[Path], pending_invalidations: set[str] | None = None
) -> list[dict]:
    invalidated = {
        evidence_id
        for evidence_id, item in data["evidence"].items()
        if item.get("status") == "invalidated"
    }
    invalidated.update(pending_invalidations or set())

    needles: dict[str, str] = {}
    for evidence_id, item in data["evidence"].items():
        if evidence_id not in invalidated:
            continue
        needles[evidence_id] = evidence_id
        for artifact in item.get("artifacts", []):
            needles[artifact] = evidence_id

    findings: list[dict] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for needle, evidence_id in needles.items():
                if needle and needle in line:
                    findings.append(
                        {
                            "file": str(path),
                            "line": lineno,
                            "evidence_id": evidence_id,
                            "matched": needle,
                        }
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    parser.add_argument("--invalidate", action="append", default=[])
    parser.add_argument("--reason", default="material validity failure")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--scan", action="append", default=[], type=Path)
    args = parser.parse_args()

    try:
        data = load_registry(args.registry)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, indent=2))
        return 2

    errors = validate_registry(data)
    missing_roots = sorted(set(args.invalidate) - set(data["evidence"]))
    errors.extend(f"unknown invalidation root {root!r}" for root in missing_roots)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 2

    impacted = descendants(data, set(args.invalidate)) if args.invalidate else set()
    if args.write and impacted:
        for evidence_id in impacted:
            item = data["evidence"][evidence_id]
            item["status"] = "invalidated"
            item["reason"] = args.reason
        args.registry.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    # Dry-run scans must use the computed invalidation closure. Otherwise the tool
    # reports a false green until --write mutates the registry.
    findings = scan_assets(data, args.scan, impacted)
    result = {
        "ok": not findings,
        "registry": str(args.registry),
        "invalidation_roots": sorted(args.invalidate),
        "impacted_evidence": sorted(impacted),
        "impacted_claims": sorted(
            {
                claim
                for evidence_id in impacted
                for claim in data["evidence"][evidence_id].get("supports", [])
            }
        ),
        "stale_references": findings,
        "written": bool(args.write and impacted),
    }
    print(json.dumps(result, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
