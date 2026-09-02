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
    SKILLS / "frontier-direction-discovery/SKILL.md": [
        "## Generate Projects From A Sparse Portfolio Brief",
        "PROJECT_GENERATION.md",
        "no new benchmark construction",
        "no new human annotation",
    ],
    SKILLS / "research-pipeline/SKILL.md": [
        "## Keep A Program Compass",
        "## Work In Research Episodes",
        "## Expand Positive Science",
        "## Form And Harvest A Paper",
        "construction arc",
        "PI is its only scientific author",
        "`MIGRATION PENDING`, `STALE STATE`, and `UNVERIFIED CLAIM`",
        "Do not maintain a second current-state",
        "Never clear it merely to",
        "identity transition",
        "strongest functional rival",
        "Artifact volume never substitutes",
        "one active positive object and one governing",
        "The file's authority is typed",
        "Maintain exactly one **active research episode**",
        "substrate fidelity contract",
        "Call a change `v2` or `v3` only when",
        "The state must also be internally coherent",
    ],
    SKILLS / "baseline/SKILL.md": [
        "## Resolve The Nearest Rival Early",
        "## Verify Substrate Competence",
        "`claim-bearing`",
        "`training`",
        "`diagnostic`",
        "same operational job",
        "functional rival and nearest mechanistic rival",
        "## Preserve Seed-Regime Fidelity",
    ],
    SKILLS / "research-lit/SKILL.md": [
        "## Reset Search When The Scientific Identity Changes",
        "same operational job",
        "keep novelty and\n"
        "paper maturity provisional",
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
        "Each successor realization must make its inheritance explicit",
        "Distinguish **design uncertainty** from **statistical uncertainty**",
    ],
    SKILLS / "experiment-plan/SKILL.md": [
        "## Use Two Resource Postures",
        "## Use Gates To Interpret Runs, Not Authorize Research",
        "## Plan Explanatory Evidence As A Model Test",
        "## Plan A Construction Arc",
        "one healthy paired development seed",
        "## Turn A Pre-Target Gemini Proposal Into Evidence",
        "put one inheritance sentence in the plan",
        "Match the substrate as well as the metric",
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
        "Prize / Fidelity / Trajectory",
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
        "prior paper maturity does not transfer",
        "Claim narrowing cannot delete a stronger",
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
    SKILLS / "run-experiment/SKILL.md": [
        "Size accelerator admission from the real-path canary",
        "GPU wait is an operational fact, not a scientific pause",
    ],
    SHARED / "research-control-protocol.md": [
        "Only explicit user instructions, safety constraints, and live operational limits are\n"
        "binding.",
        "A live `locked`, `forbidden`, `no re-entry`, or equivalent statement must\n"
        "cite the exact user or safety source",
        "changes to explicitly locked project, venue,\n"
        "deliverable, or portfolio scope",
        "Writing an interpretation into the authoritative state does not promote it into a\n"
        "constraint",
    ],
    SKILLS / "research-pipeline/tests/regression-scenarios.md": [
        "## P. High-Stakes Writing Compresses Exemplars Before Authorship",
        "## AA. Independent Verification Manufactures Defensive Work",
        "## AB. A Correlated Failure Slice Jumps Straight To A Method",
        "## AC. A Decisive Baseline Loss Is Read Without The Value Contract",
        "## AD. Gemini Suggestion Is Mistaken For Experimental Progress",
        "## AE. Laptop Power Loss Creates A Duplicate Remote Run",
        "## AF. Portfolio Monitor Rewrites A Stale Scientific State",
        "## AG. A Foundation Checkpoint Is Mistaken For The Field Baseline",
        "## AH. A Diagnostic Surface Does Not Instantiate The Canonical Object",
        "## AI. A Weak Local Reproduction Is Frozen As The Incumbent",
        "## AJ. A Sparse Portfolio Brief Produces Generic Or Tiny Projects",
        "## AK. A Detailed Project Prompt Becomes A Research Script",
        "## AL. A Useful Side Result Inherits A Failed Program's Paper Maturity",
        "## AM. Claim Narrowing Removes The Method That Solves The Same Job",
        "## AN. Selective Routing Makes Zero Regression Tautological",
        "## AO. Evaluator Repair Leaves A Smaller Positive And The Same Paper",
        "## AP. A Self-Authored Gate Becomes Project Law",
        "## AQ. A Positive Method Starts A Serial Dataset Search",
        "## AR. Claim-Confirmation Freezing Is Applied During Method Formation",
        "## AS. Two Positive Objects Compete As The Current Paper",
        "## AT. New Acronyms Replace Construction Inheritance",
        "## AU. A Small Proxy Creates The Problem It Claims To Solve",
        "## AV. Project Methods Precede The Published Field Baseline",
        "## AW. GPU Waiting Produces An Audit Factory",
        "## AX. The Sole State Contradicts Itself",
    ],
    SHARED / "research-principles.md": [
        "P01",
        "PROJECT_STATE.md",
        "P26",
        "P51",
        "P52",
        "P53",
        "P54",
        "P55",
        "P56",
        "P57",
        "P58",
        "P59",
        "P60",
        "P61",
        "P62",
        "P63",
        "P64",
        "P65",
        "P66",
        "P67",
        "P68",
        "P69",
        "P70",
        "meaningful claim-dependent advantage",
        "one isolated author subagent",
        "claims-evidence mapping begins after narrative drafting",
    ],
    RUNTIME_ADDENDUM: [
        "act as an autonomous PI",
        "Default to zero calls before a credible",
        "FIRM and registries report process",
        "do not create a new benchmark",
        "do not collect new human annotations",
        "Freedom to evolve does not let a convenient side result inherit",
        "zero-regression property guaranteed by routing",
        "The current episode is not a stage label",
        "Keep claim-bearing work faithful to the seed's task",
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
