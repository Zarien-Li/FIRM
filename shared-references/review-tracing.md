# Review Tracing Protocol

## Core Principle

**A review is useful only if its findings can be traced to artifacts, decisions, fixes, and remaining risks.**

This protocol defines how to record reviewer calls and how to connect review feedback to subsequent edits.

## When To Use

Use this protocol for:

- Paper reviews
- Claim audits
- Citation audits
- Headline and scope adversarial reviews
- Experiment audits
- Slide, poster, or talk reviews
- Rebuttal stress tests
- Meta-review or skill-system reviews

Lightweight informal comments do not need full tracing. Any review that can block readiness does.

## Trace Location

Save traces near the artifact being reviewed.

Preferred locations:

| Artifact | Trace Location |
|---|---|
| Paper | `reviews/` or `paper/reviews/` |
| Slides | `slides/reviews/` |
| Poster | `poster/reviews/` |
| Experiment | `experiments/reviews/` or run directory |
| Skill system | `reviews/skills/` |

If no project structure exists, use:

`reviews/YYYY-MM-DD_<review-type>.md`

## Required Trace Header

Every traced review must begin with:

```markdown
# Review Trace

Review ID:
Review type:
Reviewer role:
Reviewer tool/model:
Thread policy: fresh | reply | local
Date:
Artifact paths:
Input prompt path or summary:
Output path:
Decision: PASS | WARN | FAIL | BLOCKED | NOT_APPLICABLE | ERROR
```

`Input prompt path or summary` should identify what was asked without reprinting large prompts.

## Thread Policy

Use one of:

| Policy | Meaning |
|---|---|
| `fresh` | Reviewer received primary artifacts without prior feedback or executor interpretation. |
| `reply` | Reviewer continued a prior thread to check resolution or iterate. |
| `local` | No external reviewer was called; executor performed a local checklist pass. |

Fresh reviews are required for independent acceptance, claim, and citation checks.

Reply reviews are allowed for checking whether the same reviewer considers its own prior concerns resolved.

## Finding Format

Record findings as stable IDs:

```markdown
## Findings

| ID | Severity | Status | Finding | Evidence | Required Fix |
|---|---|---|---|---|---|
| R1 | blocking | open | ... | path:line or artifact section | ... |
```

Severity values:

- `blocking`
- `major`
- `minor`
- `note`

Status values:

- `open`
- `fixed`
- `wont_fix`
- `deferred`
- `invalid`

Do not delete old findings. Change status instead.

## Resolution Log

When a finding is addressed, append:

```markdown
## Resolution Log

| Finding ID | Action Taken | Changed Files | Verification |
|---|---|---|---|
```

Verification must point to evidence:

- File path
- Section name
- Test output path
- Re-review ID
- Compilation result

## Cross-Review Trace

When multiple reviewers are used, add:

```markdown
## Cross-Review Summary

| Reviewer | Decision | Blocking Count | Main Concern |
|---|---|---:|---|
```

If reviewers disagree, record the disagreement. Do not average it away.

## Independence Guard

For fresh reviews, record:

```markdown
Independence check:
- Primary artifacts were passed directly: yes/no
- Executor summaries were excluded: yes/no
- Prior review feedback was excluded: yes/no
```

If any answer is `no`, the review cannot be treated as independent.

## Minimal Trace

For quick reviews, the minimum acceptable trace is:

```markdown
# Review Trace

Review ID:
Review type:
Reviewer role:
Reviewer tool/model:
Thread policy:
Artifact paths:
Decision:

## Blocking Issues

## Actions Taken

## Remaining Risk
```

## Final Rule

No blocking review may be considered resolved unless its trace records what changed and how the fix was verified.
