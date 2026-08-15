#!/usr/bin/env python3
"""Protect FIRM's research-yield contract from accidental workflow regression."""

from __future__ import annotations

import sys
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "skills/research/SKILL.md": (
        "benchmark anchor",
        "claim-bearing",
        "consolidate or re-ground",
        "paper asset target",
        "Do not impose a fixed number",
    ),
    "skills/diagnose-result/SKILL.md": (
        "artifact's role",
        "consolidate or re-ground",
        "Research-yield consequence",
    ),
    "skills/design-method/SKILL.md": (
        "paper asset it can create",
        "There is no fixed episode limit",
    ),
    "skills/plan-experiments/SKILL.md": (
        "Every construction-scale run",
        "accepted benchmark anchor",
        "must not become the evaluation destination",
    ),
    "skills/second-pi/SKILL.md": (
        "do not require a fixed candidate count",
        "must not automatically invent the next method",
    ),
    "skills/baseline/SKILL.md": (
        "accepted benchmark or natural workflow",
        "silently replace the anchor",
    ),
}

FORBIDDEN = (
    "Every result must produce a new method",
    "Interpret -> Invent -> Attack",
    "Codex decides the project must stop",
)


def main() -> int:
    errors: list[str] = []
    corpus: list[str] = []

    for relative, phrases in REQUIRED.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        normalized = re.sub(r"\s+", " ", text).lower()
        corpus.append(normalized)
        for phrase in phrases:
            if phrase.lower() not in normalized:
                errors.append(f"{relative}: missing contract phrase {phrase!r}")

    joined = "\n".join(corpus)
    for phrase in FORBIDDEN:
        if phrase.lower() in joined:
            errors.append(f"obsolete research rule restored: {phrase!r}")

    if errors:
        print("Research contract check failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Research contract check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
