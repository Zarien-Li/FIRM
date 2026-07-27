# Assurance Contract

## Core Principle

**A research artifact is not assured because it sounds convincing. It is assured only when its claims, evidence, citations, and limitations trace to primary artifacts.**

This contract defines the final gate before treating a paper, talk, poster, rebuttal, or research report as ready for external use.

## Applies To

- Paper drafts
- Rebuttals and resubmissions
- Talks, posters, and slide decks
- Result summaries
- Claim tables
- Camera-ready or public-facing research artifacts

## Required Inputs

Before assurance, the executor must provide paths to primary artifacts:

- Main artifact: paper, slides, poster, rebuttal, or report
- Claim source: claim table, result-to-claim report, or marked claims in the artifact
- Evidence source: experiment logs, metrics files, tables, figures, or analysis reports
- Citation source: bibliography, citation audit, or cited papers
- Limitation source: limitations section or scope notes

Do not ask a reviewer to judge from a summary when primary artifacts exist.

## Assurance Checks

### 1. Claim Support

Every central claim must be classified as one of:

| Class | Meaning |
|---|---|
| `supported` | Direct evidence exists and the wording matches the evidence. |
| `overstated` | Evidence exists, but the wording is too strong. |
| `unsupported` | No adequate evidence was found. |
| `ambiguous` | Evidence may exist, but traceability is unclear. |

`unsupported` central claims are blocking. `overstated` central claims are blocking until softened.

### 2. Evidence Traceability

Every reported number, figure trend, or experimental conclusion must trace to a file, table, script output, or explicitly named source.

Blocking failures:

- Claimed results from missing files
- Claimed comparisons with no baseline result
- Final tables that disagree with result logs
- Pilot results described as full evaluation
- Synthetic or proxy evaluation presented as real ground truth

### 3. Citation Support

Citations must support the sentence they are attached to.

Blocking failures:

- Citation does not make the claimed point
- Citation is used for a stronger claim than the paper supports
- Missing citation for a factual prior-work claim
- Related work omits an obvious close baseline or competing method

### 4. Limitation Honesty

Limitations must be specific enough to constrain reader interpretation.

Blocking failures:

- Scope limitations are absent
- Known negative results are hidden
- Dataset, seed, scale, or evaluation limits are omitted
- Limitations contradict the strength of the abstract or conclusion

### 5. Narrative Integrity

Writing quality cannot compensate for weak evidence.

Blocking failures:

- The artifact uses strong narrative language to hide small or mixed results
- The contribution is framed as broader than the experiments justify
- Failure cases are moved out of sight without explanation
- The abstract promises more than the body demonstrates

## Decision Levels

| Decision | Meaning |
|---|---|
| `PASS` | No blocking issues remain. |
| `PASS_WITH_NOTES` | Only non-blocking improvements remain. |
| `BLOCKED` | One or more blocking issues must be fixed. |
| `INSUFFICIENT_INPUTS` | Primary artifacts are missing or unreadable. |

Do not return `PASS` if primary evidence was unavailable.

## Blocking Vs Advisory

Blocking issues affect correctness, honesty, traceability, or external readiness.

Advisory issues improve clarity, polish, organization, or emphasis but do not change whether the artifact is truthful.

When in doubt, mark as blocking if a reviewer could reject the artifact for the issue.

## Reviewer Independence

Assurance review must follow `reviewer-independence.md`.

The executor may provide:

- Role
- Objective
- File paths
- Venue or format constraints

The executor must not provide:

- Its own summary of the artifact
- Its interpretation of results
- Its preferred conclusion
- A list of expected strengths

## Required Output

Every assurance pass must produce:

```markdown
# Assurance Report

Decision: PASS | PASS_WITH_NOTES | BLOCKED | INSUFFICIENT_INPUTS
Artifact:
Reviewer role:
Date:

## Blocking Issues

| ID | Issue | Evidence | Required Fix |
|---|---|---|---|

## Advisory Issues

| ID | Issue | Suggested Fix |
|---|---|---|

## Claim Trace

| Claim | Status | Evidence Path | Notes |
|---|---|---|---|

## Citation Trace

| Claim/Sentence | Citation | Status | Notes |
|---|---|---|---|

## Final Notes
```

If no blocking issues exist, explicitly write `No blocking issues found.`

## Final Rule

An artifact may only be called ready when all blocking issues are either fixed or explicitly removed from scope.

