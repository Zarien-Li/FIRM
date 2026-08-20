#!/usr/bin/env python3
"""Protect FIRM's research-episode contract from workflow regression."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "skills/research-pipeline/SKILL.md": (
        "## Keep A Program Compass",
        "## Work In Research Episodes",
        "## Expand Positive Science",
        "## Form And Harvest A Paper",
        "construction arc",
    ),
    "skills/baseline/SKILL.md": (
        "## Resolve The Nearest Rival Early",
        "## Verify Substrate Competence",
        "`claim-bearing`",
        "`training`",
        "`diagnostic`",
    ),
    "skills/signal-analysis/SKILL.md": (
        "## Observation Is The Default Update",
        "## Read A Construction Arc Constructively",
        "## Separate Predictive Signal From Editable Cause",
    ),
    "skills/method-primitive-synthesis/SKILL.md": (
        "candidate",
        "realization",
        "## Cultivate One Construction Arc",
        "80% deletion test",
    ),
    "skills/experiment-plan/SKILL.md": (
        "## Use Two Resource Postures",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
    ),
    "skills/research-review/SKILL.md": (
        "## Sparse Codex Policy",
        "Default to **zero Codex calls**",
        "reviewer preference",
        "## Field And Prize",
        "## Interpret",
        "## Method Challenge",
        "## Program Expansion",
    ),
    "shared-references/research-principles.md": ("P01", "P26", "P51"),
    "skills/research-pipeline/tests/regression-scenarios.md": (
        "## A.",
        "## M.",
        "## Z.",
    ),
}

FORBIDDEN = {
    "skills/research-pipeline/SKILL.md": (
        "Every construction episode targets a named paper asset",
        "After two failures",
        "Every result must produce",
    ),
    "skills/signal-analysis/SKILL.md": (
        "paper_asset_delta",
        "benchmark_movement",
    ),
    "skills/method-primitive-synthesis/SKILL.md": (
        "continuation burden",
        "exit_to_reground:",
    ),
    "skills/research-review/SKILL.md": (
        "Interpret -> Invent -> Attack",
        "Codex decides whether the project must stop",
        "Codex is the critical co-PI",
        "Codex may choose `PARK`",
    ),
    "skills/paper-writing/SKILL.md": (
        "from a fresh `/research-review` artifact review",
    ),
}


def main() -> int:
    failures: list[str] = []
    for relative, needles in REQUIRED.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"missing {needle!r} in {relative}")

    for relative, needles in FORBIDDEN.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(f"forbidden {needle!r} in {relative}")

    if failures:
        print("Research semantic contract failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Research semantic contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
