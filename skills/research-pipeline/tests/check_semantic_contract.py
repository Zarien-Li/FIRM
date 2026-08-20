#!/usr/bin/env python3
"""Fail fast when maintenance removes the research-process contract."""

from pathlib import Path


SKILLS = Path(__file__).resolve().parents[2]

REQUIRED = {
    "research-pipeline/SKILL.md": [
        "## Keep A Program Compass",
        "## Work In Research Episodes",
        "## Expand Positive Science",
        "## Form And Harvest A Paper",
        "construction arc",
    ],
    "baseline/SKILL.md": [
        "## Resolve The Nearest Rival Early",
        "## Verify Substrate Competence",
        "`claim-bearing`",
        "`training`",
        "`diagnostic`",
    ],
    "signal-analysis/SKILL.md": [
        "## Observation Is The Default Update",
        "## Read A Construction Arc Constructively",
        "## Separate Predictive Signal From Editable Cause",
    ],
    "method-primitive-synthesis/SKILL.md": [
        "candidate",
        "realization",
        "## Cultivate One Construction Arc",
        "80% deletion test",
    ],
    "experiment-plan/SKILL.md": [
        "## Use Two Resource Postures",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
    ],
    "research-review/SKILL.md": [
        "## Sparse Codex Policy",
        "Default to **zero Codex calls**",
        "reviewer preference",
        "## Field And Prize",
        "## Interpret",
        "## Method Challenge",
        "## Program Expansion",
    ],
    "paper-writing/SKILL.md": [
        "Do not create a Paper Spine",
        "Learn Writing From Excellent Papers Without Polluting The Main Context",
        "One identity means one governing scientific principle",
    ],
    "shared-references/research-principles.md": ["P01", "P26", "P51"],
    "research-pipeline/tests/regression-scenarios.md": [
        "## A.",
        "## M.",
        "## Z.",
    ],
}

FORBIDDEN = {
    "research-pipeline/SKILL.md": [
        "Every construction episode targets a named paper asset",
        "After two failures",
        "Every result must produce",
    ],
    "signal-analysis/SKILL.md": ["paper_asset_delta", "benchmark_movement"],
    "method-primitive-synthesis/SKILL.md": [
        "continuation burden",
        "exit_to_reground:",
    ],
    "research-review/SKILL.md": [
        "Interpret -> Invent -> Attack",
        "Codex decides whether the project must stop",
        "Codex is the critical co-PI",
        "Codex may choose `PARK`",
    ],
    "paper-writing/SKILL.md": ["from a fresh `/research-review` artifact review"],
}


def resolve(rel: str) -> Path:
    installed = SKILLS / rel
    if installed.exists():
        return installed
    packaged = SKILLS.parent / rel
    if packaged.exists():
        return packaged
    return installed


def main() -> int:
    failures: list[str] = []
    for rel, needles in REQUIRED.items():
        text = resolve(rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"missing {needle!r} in {rel}")
    for rel, needles in FORBIDDEN.items():
        text = resolve(rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(f"forbidden {needle!r} in {rel}")

    if failures:
        print("Research semantic contract failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Research semantic contract passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
