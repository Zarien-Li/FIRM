# Mode: Experiment Integrity

Independently determine what the existing experiment artifacts can support. Invoke at
a consequential claim boundary or when evaluator, ground truth, execution, provenance,
selection, or fairness is genuinely uncertain. Do not run after every pilot or seed.

## Evidence Packet

Collect the declared claim and, when available:

- exact command, resolved configuration, seeds, code revision/diff, environment;
- dataset/source, split, preprocessing, candidate pool, labels/targets;
- evaluator, parser, metric definition/direction, aggregation script;
- raw predictions, per-example outputs, logs, checkpoints, result files;
- evidence that the advertised component and intended code path executed;
- baseline configuration, information/supervision/tool budget, tuning effort;
- retries, exclusions, failed/interrupted/unread runs, and post-hoc changes;
- pre-result registration or forecast;
- discovery/selection data versus confirmation data;
- manuscript/table/summary claims depending on the result.

Missing evidence is not misconduct. Mark the affected quantity `UNVERIFIED` and state
the claim consequence.

## Checks

### 1. Artifact and code-path integrity

- cited artifacts exist, are non-placeholder, parseable, and mutually consistent;
- run identifiers, timestamps, configs, logs, checkpoints, and results agree;
- intended method branch, feature flags, checkpoint, and evaluator executed;
- no dead code, silent fallback, stale output, copied result, or duplicate job;
- optimization/training was competent enough for the intended conclusion.

### 2. Target and evaluator semantics

- distinguish gold truth, synthetic target, model judgment, proxy, and heuristic label;
- verify target construction, leakage, circularity, truncation, filtering, and missing
  values;
- reconstruct score direction, normalization, denominator, units, and aggregation;
- check that the metric identifies the construct named by the claim;
- separate diagnostic/oracle evidence from deployed end-to-end evidence.

### 3. Comparison and substrate competence

- match data, preprocessing, information, labels, supervision, tools, candidate pool,
  optimization budget, stopping, and evaluator;
- verify the decisive incumbent and strongest simple/direct alternative are correctly
  configured or explicitly unresolved;
- confirm the underlying substrate competently performs the standard task;
- do not attribute a joint change in backbone, data, and mechanism to the mechanism;
- distinguish prototype readiness from a primitive-level comparison.

### 4. Statistical and selection integrity

- seeds/repetitions answer an explicit stochastic question and are consistently
  aggregated;
- failed or inconvenient runs and post-hoc exclusions remain visible;
- experimental unit, dependence, uncertainty, confidence interval, and test match the
  claim;
- thresholds, slices, variables, metrics, and stopping were not selected and confirmed
  on the same evidence without disclosure;
- held-out or independent confirmation is appropriate to the claim.

### 5. Scope, provenance, and traceability

- claimed population matches tested models, tasks, datasets, regimes, and naturality;
- public/private/synthetic/transformed data and reused checkpoints are attributed;
- every consequential claim maps to an exact artifact and reproducible transformation;
- manual edits, exclusions, and external values are traceable;
- selection or artifact repair is propagated to all dependent claims.

## Verdict

- `PASS`: no material integrity issue for the stated bounded claim;
- `WARN`: usable evidence with a required qualifier, missing artifact, or narrower
  scope;
- `FAIL`: the affected claim depends on broken/mismatched evidence or reverses meaning;
- `BLOCKED`: required evidence is absent or inaccessible, so the claim cannot yet be
  assessed;
- `NOT_APPLICABLE`: no claim-bearing experiment is present;
- `ERROR`: audit execution failed.

A negative verdict invalidates or qualifies the affected evidence and dependents. It
does not close a method family or program.

## Evidence Lineage

For each audited item record:

- stable evidence ID and artifact path;
- validity status and exact reason;
- claims/tables/figures/state entries that depend on it;
- superseding clean evidence when available.

Use `scripts/evidence_lineage.py` to validate a registry or compute an invalidation
impact set when the project maintains one. The script reports impact; it does not edit
paper prose or promote repaired evidence automatically.

## Output

Write `EXPERIMENT_AUDIT.md`:

```markdown
# Experiment Integrity Audit
- audited claim and scope:
- verdict and reason:
- reviewer/thread/time:

## Evidence inspected
| Artifact | Path/ID | Status | Notes |
|---|---|---|---|

## Findings
| Check | Verdict | Raw evidence | Claim impact | Required repair |
|---|---|---|---|---|

## Claim traceability
| Claim | Artifact | Transformation | Status |
|---|---|---|---|

## Evidence-lineage impact
## What remains scientifically usable
## What must not be claimed yet
```

At submission assurance also write `EXPERIMENT_AUDIT.json` using the shared assurance
schema, including declared input hashes and per-check details. Do not edit raw results,
completed registrations, or manuscript claims inside the audit itself.
