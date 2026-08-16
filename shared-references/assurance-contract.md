# Assurance Contract

Use this contract for external-facing papers, rebuttals, talks, posters, and reports.
Assurance checks whether the artifact is traceable and honest; it cannot create a
scientific contribution or close a research program.

## Inputs

Review primary artifacts whenever available:

- the external-facing artifact;
- claim source or claim map;
- raw results, proofs, tables, figures, and analysis;
- bibliography and cited sources;
- scope and limitations;
- current paper fingerprint and entry status when applicable.

Do not substitute an executor summary for readable primary evidence.

## Checks

### Claim And Evidence

- Every central claim maps to direct evidence and matches its scope.
- Numbers and trends trace to raw or reproducible artifacts.
- Pilot, synthetic, proxy, sampled, or induced evidence is labeled.
- Tables and figures agree with results.
- Unsupported claims are removed; overstated claims are narrowed.

### Citation

- Cited works exist with verified metadata.
- Each citation supports its attached statement.
- Obvious close work and decisive baselines are represented faithfully.

### Scope And Narrative

- Abstract, title, conclusion, and limitations describe the same supported object.
- Known negative results and material costs are not hidden.
- Writing does not use a broad field name to disguise a private supported scope.
- The contribution is not manufactured from polished failure history.

## Verdicts

Use the common audit vocabulary:

- `PASS`: no blocking correctness or traceability issue;
- `WARN`: artifact remains usable with an exact qualifier or non-blocking repair;
- `FAIL`: a verified issue invalidates or overstates a central claim;
- `BLOCKED`: required primary artifacts are missing or unreadable;
- `NOT_APPLICABLE`: the selected audit does not apply;
- `ERROR`: tooling or reviewer execution failed.

Do not convert uncertainty automatically into `FAIL`. Classify the issue by what it
can actually change: `EVIDENCE_INVALIDATING`, `METHOD_DESIGN_CHANGING`,
`CLAIM_NARROWING`, or `DEFERRABLE`. Missing evidence for a stronger claim may require
narrowing rather than new experiments.

At submission assurance, emit the required JSON artifact even for `BLOCKED`,
`NOT_APPLICABLE`, or `ERROR`. Never treat unavailable review as `PASS`.

## Reviewer Independence

Independent artifact review follows `reviewer-independence.md`: pass primary files,
role, objective, and venue constraints without executor interpretation or desired
verdict. This restriction concerns audits and readiness review, not co-PI Interpret or
Method Challenge defined in `research-review`.

## Compact Report

```markdown
# Assurance Report
verdict: PASS | WARN | FAIL | BLOCKED | NOT_APPLICABLE | ERROR
artifact:
reviewer role and thread policy:
date:

## Findings
| ID | Class | Severity | Finding | Evidence | Required action |

## Claim Trace
| Claim | Status | Evidence path | Scope/qualifier |

## Citation Trace
| Sentence/claim | Citation | Status | Evidence |

## Remaining Risk
```

If `FAIL` rests on invalid evidence, propagate through `evidence-lineage.md`. A claim
may be called externally ready only after blocking issues are fixed or removed from
scope and any required paper-entry condition remains valid.
