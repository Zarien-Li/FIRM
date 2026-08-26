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
        "## Build A Problem Model Before A Method",
        "the earliest meaningful divergence between matched successes and failures",
        "## Read A Construction Arc Constructively",
        "## Separate Predictive Signal From Editable Cause",
    ],
    SKILLS / "method-primitive-synthesis/SKILL.md": [
        "candidate",
        "realization",
        "## Require A Design-Giving Problem Account",
        "## Cultivate One Construction Arc",
        "80% deletion test",
        "meaningful advantage on the",
        "claim-relevant value surface",
    ],
    SKILLS / "experiment-plan/SKILL.md": [
        "## Use Two Resource Postures",
        "## Plan Explanatory Evidence As A Model Test",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
        "## Turn A Pre-Target Gemini Proposal Into Evidence",
    ],
    SKILLS / "research-review/SKILL.md": [
        "## Sparse Codex Policy",
        "Default to **zero Codex calls**",
        "Every Codex recommendation bears an action burden",
        "`no material change`",
        "reviewer preference",
        "## Creative Invention",
        "### Effective But Still Behind A Decisive Rival",
        "## Decision-Focused Construction Check",
        "## Program Expansion",
    ],
    SKILLS / "paper-writing/SKILL.md": [
        "## Establish The Author Argument Before The Outline",
        "one-page `AUTHOR_ARGUMENT.md` in continuous prose",
        "## Use Claims-Evidence As A Post-Draft Verification Tool",
        "Let A Dedicated Author Learn Directly From Excellent Papers",
        "Do not create a synthesis of recurring patterns",
        "Use one fresh author subagent for a coherent section or draft",
        "## Draft The Problem Story Early, Then Rewrite It From Stable Evidence",
        "meaningful pre-specified advantage",
        "One identity means one governing scientific principle",
    ],
    SKILLS / "auto-paper-improvement-loop/SKILL.md": [
        "## One Improvement Round",
        "### 1. Fresh human-reader edit",
        "After a normal ten-minute read",
        "authorial voice",
        "Scientific taste is part of successful communication",
    ],
    SKILLS / "research-state-audit/SKILL.md": [
        "claim-sufficient comparison set",
        "meaningful pre-specified advantage",
    ],
    SKILLS / "monitor-experiment/SKILL.md": [
        "## Recover After Host Power Loss Or Session Restart",
        "Never duplicate a run merely because the laptop rebooted",
    ],
    SKILLS / "run-experiment/references/operations.md": [
        "If FIRM is unavailable or not configured",
        "must not block an otherwise\n"
        "authorized ordinary experiment",
        "existing project-owned local process, direct\n"
        "SSH launcher, or managed scheduler path",
    ],
    SHARED / "research-control-protocol.md": [
        "Only explicit user instructions, safety constraints, and live operational limits are\n"
        "binding.",
        "A live `locked`, `forbidden`, `no re-entry`, or equivalent statement must\n"
        "cite the exact user or safety source",
        "changes to explicitly locked project, venue,\n"
        "deliverable, or portfolio scope",
    ],
    SKILLS / "research-pipeline/tests/regression-scenarios.md": [
        "## P. High-Stakes Writing Compresses Exemplars Before Authorship",
        "## AA. Independent Verification Manufactures Defensive Work",
        "## AB. A Correlated Failure Slice Jumps Straight To A Method",
        "## AC. A Decisive Baseline Loss Is Read Without The Value Contract",
        "## AD. Gemini Suggestion Is Mistaken For Experimental Progress",
        "## AE. Laptop Power Loss Creates A Duplicate Remote Run",
    ],
    SHARED / "research-principles.md": [
        "P01",
        "P26",
        "P51",
        "meaningful claim-dependent advantage",
        "one isolated author subagent",
        "claims-evidence mapping begins after narrative drafting",
    ],
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
        "FIRM is required to launch experiments",
    ],
    SKILLS / "research-review/SKILL.md": [
        "Interpret -> Invent -> Attack",
        "Codex decides whether the project must stop",
        "Codex is the critical co-PI",
        "Codex may choose `PARK`",
        "red-team verifier",
        "## Method Challenge",
        "fatal flaw",
        "Classify criticism before acting",
    ],
    SKILLS / "paper-writing/SKILL.md": [
        "from a fresh `/research-review` artifact review",
        "A separate synthesis subagent consumes",
        "main writer reads only that synthesis",
        "## Build One Claims-Evidence Spine",
        "## Draft Evidence First",
        "MANUSCRIPT_FORBIDDEN",
        "beats every such baseline",
        "hard SOTA gate",
    ],
    SKILLS / "auto-paper-improvement-loop/SKILL.md": [
        "another round would optimize taste",
        "### 1. Fresh artifact review",
    ],
    SKILLS / "research-pipeline/tests/regression-scenarios.md": [
        "use a separate synthesis subagent",
        "expose only the compact synthesis",
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
