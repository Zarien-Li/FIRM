#!/usr/bin/env python3
"""Validate the installed research-process contract and migration invariants."""

from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve()
PACKAGE_ROOT = HERE.parents[3]
PACKAGED = (PACKAGE_ROOT / "managed-skills.txt").is_file()

if PACKAGED:
    ROOT = PACKAGE_ROOT
    SKILLS = ROOT / "skills"
    SHARED = ROOT / "shared-references"
    RUNTIME_ADDENDUM = ROOT / "CLAUDE-RESEARCH.md"
    SKILL_MANIFEST = ROOT / "managed-skills.txt"
    SHARED_MANIFEST = ROOT / "managed-shared-references.txt"
else:
    SKILLS = HERE.parents[2]
    ROOT = SKILLS.parent
    SHARED = SKILLS / "shared-references"
    RUNTIME_ADDENDUM = ROOT / "CLAUDE-RESEARCH.md"
    SKILL_MANIFEST = SKILLS / ".research-skills-managed"
    SHARED_MANIFEST = SKILLS / ".research-shared-references-managed"

REQUIRED = {
    SKILLS / "research-pipeline/SKILL.md": [
        "## Keep A Program Compass",
        "## Work In Research Episodes",
        "## Expand Positive Science",
        "## Form And Harvest A Paper",
        "construction arc",
    ],
    SKILLS / "baseline/SKILL.md": [
        "## Resolve The Nearest Rival Early",
        "## Verify Substrate Competence",
        "`claim-bearing`",
        "`training`",
        "`diagnostic`",
    ],
    SKILLS / "signal-analysis/SKILL.md": [
        "## Observation Is The Default Update",
        "## Read A Construction Arc Constructively",
        "## Separate Predictive Signal From Editable Cause",
    ],
    SKILLS / "method-primitive-synthesis/SKILL.md": [
        "candidate",
        "realization",
        "## Cultivate One Construction Arc",
        "80% deletion test",
    ],
    SKILLS / "experiment-plan/SKILL.md": [
        "## Use Two Resource Postures",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
    ],
    SKILLS / "research-review/SKILL.md": [
        "## Sparse Codex Policy",
        "Default to **zero Codex calls**",
        "reviewer preference",
        "## Creative Invention",
        "## Program Expansion",
    ],
    SKILLS / "paper-writing/SKILL.md": [
        "Do not create a Paper Spine",
        "Learn Writing From Excellent Papers Without Polluting The Main Context",
        "One identity means one governing scientific principle",
    ],
    SHARED / "research-principles.md": ["P01", "P26", "P51"],
    RUNTIME_ADDENDUM: [
        "act as an autonomous PI",
        "Default to zero calls before a credible",
        "FIRM and registries report process",
    ],
}

FORBIDDEN = {
    RUNTIME_ADDENDUM: [
        "sealed project identity",
        "identity guard",
        "[FIRM CONSTRUCTION_LEASE",
        "Project Claude",
    ],
    SKILLS / "paper-writing/references/submission.md": [
        "Required Independent Checks",
        "obtain user approval plus a new paper-entry review",
        "artifact review for final scientific prize",
    ],
    SKILLS / "run-experiment/references/operations.md": [
        "git add -A",
        "wandb login <",
        "run_in_background",
        "artifact-sync",
        "Never overlap screens",
        "queue_manager.py",
        "install_aris.sh",
    ],
    SKILLS / "research-review/SKILL.md": [
        "Interpret -> Invent -> Attack",
        "Codex decides whether the project must stop",
        "Codex is the critical co-PI",
        "Codex may choose `PARK`",
    ],
    SKILLS / "paper-writing/SKILL.md": [
        "from a fresh `/research-review` artifact review",
    ],
}

EXPECTED_LINKS = {
    SKILLS / "baseline/SKILL.md": [
        "../shared-references/experiment-integrity.md",
        "../shared-references/evidence-lineage.md",
    ],
    SKILLS / "research-audit/SKILL.md": [
        "../shared-references/assurance-contract.md",
    ],
    SKILLS / "research-review/SKILL.md": [
        "../shared-references/assurance-contract.md",
    ],
}


def manifest_entries(path: Path) -> set[str]:
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    failures: list[str] = []

    for path, needles in REQUIRED.items():
        if not path.is_file():
            failures.append(f"missing required file: {label(path)}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(
                    f"missing {needle!r} in {label(path)}"
                )

    for path, needles in FORBIDDEN.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(
                    f"forbidden {needle!r} in {label(path)}"
                )

    for owner, links in EXPECTED_LINKS.items():
        text = owner.read_text(encoding="utf-8")
        for rel in links:
            if rel not in text:
                failures.append(f"missing link {rel!r} in {label(owner)}")
                continue
            if rel.startswith("../shared-references/"):
                target = SHARED / Path(rel).name
            else:
                target = (owner.parent / rel).resolve()
            if not target.is_file():
                failures.append(
                    f"broken link {rel!r} in {label(owner)}"
                )

    manifest = manifest_entries(SKILL_MANIFEST)
    actual = {
        path.name
        for path in SKILLS.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if not manifest.issubset(actual):
        failures.append(
            "managed skills missing: " f"{sorted(manifest - actual)}"
        )
    if PACKAGED and actual != manifest:
        failures.append(f"unmanaged packaged skills present: {sorted(actual - manifest)}")

    shared_manifest = manifest_entries(SHARED_MANIFEST)
    actual_shared = {path.name for path in SHARED.iterdir() if path.is_file()}
    if shared_manifest != actual_shared:
        failures.append(
            "managed-shared-references.txt mismatch: "
            f"missing={sorted(actual_shared - shared_manifest)}, "
            f"extra={sorted(shared_manifest - actual_shared)}"
        )

    if PACKAGED and (SKILLS / "shared-references").exists():
        failures.append("duplicate skills/shared-references directory must not exist")
    if (SKILLS / "research-pipeline/scripts/identity_guard.py").exists():
        failures.append("retired identity_guard.py remains active")

    residue_roots = [SHARED] + [SKILLS / name for name in manifest]
    residue = [
        label(path)
        for base in residue_roots
        for path in base.rglob("*")
        if path.name == "__pycache__" or (path.is_file() and path.suffix == ".pyc")
    ]
    if residue:
        failures.append(f"generated Python residue present: {residue}")

    if failures:
        print("Research semantic contract failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Research semantic contract passed "
        f"({len(manifest)} managed skills, canonical shared references)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
