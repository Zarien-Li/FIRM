# Reviewer Routing Protocol

This reference routes artifact reviews. Scientific co-PI roles are selected by
`research-review` and must not be replaced by this generic routing table.

## Modes

| Mode | Use |
|---|---|
| `fresh` | Independent judgment of the current primary artifact |
| `reply` | Same reviewer checks resolution of its own prior findings |
| `local` | Mechanical check or explicit fallback without independence |
| `cross_compare` | High-stakes disagreement among independent reviews |

Use `fresh` for paper readiness, claim/citation/headline audits, experiment-integrity
review, rebuttal stress tests, and proof audits. Follow `reviewer-independence.md`.

Use `reply` only for the same bounded issue after corrected artifacts or facts. Do not
persuade the reviewer with executor arguments or selective excerpts.

Use `local` for compilation, page limits, schemas, deterministic checks, or when no
independent tool exists. Label it local and do not promote it to independent evidence.

Use `cross_compare` only when a near-submission central issue remains genuinely
disputed. Record agreements, disagreements, the highest-risk unresolved issue, and
the artifact change most likely to resolve it; do not average judgments into a score.

## Role Selection

Choose a precise artifact role such as `experiment_reviewer`, `theory_reviewer`,
`systems_reviewer`, `citation_auditor`, `area_chair`, or
`rebuttal_stress_tester`.

Do not route early field choice, explanation comparison, or method construction here.
Those require Field/Prize, Interpret, or Method Challenge and the evidence-maturity
rules in `research-review`.

## Tool Failure

Preserve the intended mode when possible. If no independent reviewer is available,
perform a bounded local check and lower confidence explicitly. Tool failure never
becomes `PASS`, `FAIL`, or a research pause.

## Compact Route Record

```markdown
review_type:
reviewer_role:
mode: fresh | reply | local | cross_compare
tool/thread:
artifact_paths:
trace_path:
```
