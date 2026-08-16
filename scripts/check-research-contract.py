#!/usr/bin/env python3
"""Protect FIRM's research-episode contract from workflow regression."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "skills/research/SKILL.md": (
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
    "skills/diagnose-result/SKILL.md": (
        "## Observation Is The Default Update",
        "## Read A Construction Arc Constructively",
        "## Separate Predictive Signal From Editable Cause",
    ),
    "skills/design-method/SKILL.md": (
        "candidate",
        "realization",
        "## Cultivate One Construction Arc",
        "80% deletion test",
    ),
    "skills/plan-experiments/SKILL.md": (
        "## Use Two Resource Postures",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
    ),
    "skills/second-pi/SKILL.md": (
        "## Field And Prize",
        "## Interpret",
        "## Method Challenge",
        "## Program Expansion",
    ),
    "shared-references/research-principles.md": ("P01", "P26", "P51"),
    "skills/research/references/regression-scenarios.md": (
        "## A.",
        "## M.",
        "## Z.",
    ),
}

FORBIDDEN = {
    "skills/research/SKILL.md": (
        "Every construction episode targets a named paper asset",
        "After two failures",
        "Every result must produce",
    ),
    "skills/diagnose-result/SKILL.md": (
        "paper_asset_delta",
        "benchmark_movement",
    ),
    "skills/design-method/SKILL.md": (
        "continuation burden",
        "exit_to_reground:",
    ),
    "skills/second-pi/SKILL.md": (
        "Interpret -> Invent -> Attack",
        "Codex decides whether the project must stop",
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
