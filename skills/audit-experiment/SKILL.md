---
name: audit-experiment
description: Performs an independent integrity audit of experiment artifacts, provenance, evaluator semantics, configuration consistency, and claim scope.
when_to_use: Invoke explicitly before consequential claims, paper writing, or submission, or when fake ground truth, score normalization, phantom results, dead code, or config mismatch is genuinely suspected.
argument-hint: "[experiment directory or claim]"
disable-model-invocation: true
context: fork
background: false
---

# Experiment Integrity Audit

Audit the experiment as an independent reviewer. The purpose is to determine which
claims the existing artifacts can honestly support, not to search for reasons to
block ordinary research.

## Scope

Use this audit at a consequential boundary or when integrity is genuinely unclear.
Do not require it after every pilot, small ablation, or routine monitoring update.

Inspect the experiment directory or paths supplied in `$ARGUMENTS`. Prefer raw and
machine-generated artifacts over prose summaries.

## Required evidence packet

Collect, when available:

- exact command or scheduler script;
- resolved configuration and random seeds;
- code commit or diff;
- dataset and split identifiers;
- evaluator implementation and metric definition;
- raw predictions, labels, and per-example outputs;
- logs showing the intended code path ran;
- result files and aggregation scripts;
- baseline configuration and budget;
- exclusions, retries, failed runs, and post-hoc changes;
- the precise claim the result is intended to support.

Missing evidence is not automatically fraud. Mark it as missing and explain the
claim consequence.

## Checks

### A. Artifact existence and consistency

- Do cited files exist and contain non-placeholder data?
- Do logs, result files, and reported numbers agree?
- Are timestamps and run identifiers coherent?
- Is the result derived from the declared run rather than copied from another
  configuration?

### B. Code-path integrity

- Did the advertised method component execute?
- Are feature flags, checkpoints, and branches resolved as claimed?
- Is there dead code, a silent fallback, or a baseline path used accidentally?
- Does the evaluation consume the intended outputs?

### C. Ground truth and evaluator semantics

- Is the target real ground truth, a synthetic proxy, model-generated judgment, or
  heuristic label?
- Is that distinction visible in the claim?
- Are score direction, normalization, denominator, units, and missing values handled
  correctly?
- Does the metric measure the claimed construct?

### D. Comparison fairness

- Are data, preprocessing, search budget, training budget, prompts, hardware-relevant
  settings, and evaluation conditions matched?
- Is the strongest relevant baseline included or explicitly deferred?
- Are baseline failures or tuning effort treated symmetrically?

### E. Statistical and selection integrity

- Are seeds and repeated runs complete and consistently aggregated?
- Were failed or inconvenient runs selectively excluded?
- Were primary metrics, slices, or stopping rules changed after seeing results?
- Is uncertainty sufficient for the claimed difference?

### F. Scope and provenance

- Does the result support the claimed population, or only a selected slice?
- Are public, private, synthetic, and transformed data sources distinguishable?
- Are external results, reused checkpoints, and manually edited values attributed?
- Does the manuscript imply stronger natural validity than the evidence provides?

### G. Claim traceability

For each consequential claim, identify the exact supporting artifact and the
transformation from raw data to reported number. If the chain cannot be reproduced,
mark the claim `UNVERIFIED` rather than guessing.

## Verdict policy

Use three levels:

- `PASS`: no material integrity issue for the stated bounded claim;
- `WARN`: evidence is usable, but a limitation, missing artifact, or narrower scope
  must be disclosed or repaired;
- `FAIL`: the affected claim depends on a broken evaluator, nonexistent or mismatched
  result, unexecuted method, invalid ground truth, selective reporting, or another
  issue that reverses its meaning.

A `FAIL` applies to the affected evidence and claim. Do not declare the entire
research program invalid unless the audited issue genuinely reaches that scope.

## Output

Write `EXPERIMENT_AUDIT.md` beside the audited project artifacts when edits are
permitted; otherwise return the same structure in the response.

```markdown
# Experiment Integrity Audit

## Overall verdict
PASS | WARN | FAIL

## Audited claim

## Evidence inspected
| Artifact | Path or identifier | Status | Notes |
|---|---|---|---|

## Checks
### A. Artifact consistency
Verdict:
Evidence:
Claim impact:

### B. Code-path integrity
Verdict:
Evidence:
Claim impact:

### C. Ground truth and evaluator
Verdict:
Evidence:
Claim impact:

### D. Comparison fairness
Verdict:
Evidence:
Claim impact:

### E. Statistical and selection integrity
Verdict:
Evidence:
Claim impact:

### F. Scope and provenance
Verdict:
Evidence:
Claim impact:

## Claim traceability
| Claim | Supporting artifact | Transformation | Status |
|---|---|---|---|

## Required repairs
1.

## What remains scientifically usable

## What must not be claimed yet
```

Do not edit raw results, rewrite a completed registration, or silently repair the
evidence during the audit. Recommend fixes separately and preserve the original
artifacts.
