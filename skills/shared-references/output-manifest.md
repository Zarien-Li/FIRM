# Output Manifest Protocol

## Core Principle

**Every non-trivial skill run should leave a small, structured record of what it read, what it changed, what it produced, and what remains unresolved.**

The manifest is not a diary. It is a handoff artifact for future sessions, reviewers, and downstream skills.

## When Required

Create or update an output manifest when a skill:

- Produces research decisions
- Creates or edits paper artifacts
- Launches or analyzes experiments
- Runs a review or audit
- Changes claims, citations, figures, slides, or rebuttal text
- Produces files that downstream skills will consume

Small one-off checks can omit a manifest if no artifact or decision is produced.

## Location

Preferred names:

- `MANIFEST.md`
- `OUTPUT_MANIFEST.md`
- `reviews/MANIFEST.md`
- `experiments/<run>/MANIFEST.md`
- `paper/MANIFEST.md`

Use the location closest to the produced artifact.

## Required Fields

```markdown
# Output Manifest

Skill:
Run date:
Executor:
Status: complete | partial | blocked

## Inputs

| Path | Role | Notes |
|---|---|---|

## Outputs

| Path | Type | Notes |
|---|---|---|

## Decisions

| Decision | Rationale | Evidence |
|---|---|---|

## Open Issues

| Issue | Severity | Owner/Next Step |
|---|---|---|

## Verification

| Check | Result | Evidence |
|---|---|---|

## Downstream Handoff

Next recommended skill/action:
Files downstream skills should read:
Files downstream skills should ignore:
```

## Status Values

| Status | Meaning |
|---|---|
| `complete` | Requested work finished and verification passed or was not needed. |
| `partial` | Useful outputs exist, but some intended work remains. |
| `blocked` | Work cannot continue without missing input, tool, approval, or decision. |

## Evidence Rules

Evidence should be a path, command result path, review trace ID, or artifact section.

Avoid vague evidence like:

- "looks good"
- "reviewed manually"
- "probably fixed"

Prefer:

- `paper/main.tex:Section 4`
- `experiments/run_017/metrics.json`
- `reviews/2026-05-25_claim-audit.md#R3`
- `build/main.pdf`

## Open Issue Severity

Use:

- `blocking`
- `major`
- `minor`
- `note`

Blocking issues must name a concrete next step.

## Downstream Handoff Rules

The handoff should be compact. Include only the files the next skill needs.

Do not include raw logs unless the next skill explicitly needs them.

If raw logs exist, point to their path and summarize only the relevant line or metric.

## Append Vs Replace

For iterative work:

- Append new decisions and verification entries.
- Update status when work moves from `blocked` to `partial` or `complete`.
- Do not erase old decisions unless they were recorded in error.

## Minimal Manifest

When time is short, use:

```markdown
# Output Manifest

Skill:
Status:

Inputs:
Outputs:
Decisions:
Open issues:
Next action:
```

## Final Rule

If another skill would need to ask "what happened last time?", the manifest is incomplete.

