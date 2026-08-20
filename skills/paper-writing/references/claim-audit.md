# Manuscript Claim Audit

Use for paper-to-evidence fidelity: do manuscript numbers, configurations, populations,
and semantic qualifiers match completed raw artifacts? This is distinct from
experiment validity (`/research-audit mode: experiment`) and citation support
(`/research-audit mode: citation`).

## Independence

Use a fresh reviewer/context with only:

- the compiled manuscript and source files;
- exact raw result/config artifacts declared for the audit;
- metric definitions needed to reconstruct values.

Do not provide narrative reports, prior audits, desired verdicts, fix summaries, or
author explanations. The executor declares the complete input set; the reviewer cannot
silently narrow it.

## Extract Claims

Inventory consequential claims from title, abstract, contributions, body, captions,
tables, appendix, limitations, and conclusion:

- numbers, percentages, deltas, ranges, counts, sample sizes, seeds, costs;
- model/data/config/evaluator statements;
- best/worst/tie/rank and consistency claims;
- natural, general, robust, causal, deployable, efficient, SOTA, and similar qualifiers;
- population and scope statements;
- claims that diagnostic/oracle/proxy evidence is a method or end-to-end result.

## Reconstruct From Raw Evidence

For each claim:

1. locate the raw artifact and exact records;
2. reproduce filtering, grouping, aggregation, uncertainty, and rounding;
3. verify configuration, seed, sample, model, dataset, and evaluator;
4. check that development/selected evidence is not presented as independent
   confirmation;
5. check semantic status: induced vs natural, diagnostic vs deployed, one cell vs
   population, association vs cause, scale sensitivity vs generality;
6. inspect every repeated occurrence for consistent wording.

Standard rounding to displayed precision is allowed. Direction-changing, threshold-
crossing, or materially scope-changing rounding is not.

## Verdicts

Per claim:

- `PASS`: value and semantics match;
- `WARN`: defensible only with a named qualifier or minor rounding repair;
- `FAIL`: wrong value/config/direction/population or unsupported semantic promotion;
- `BLOCKED`: numeric/semantic claim exists but raw evidence is absent;
- `NOT_APPLICABLE`: no consequential empirical claim;
- `ERROR`: audit failed.

A numerically correct sentence can still fail when it promotes synthetic evidence to
natural prevalence, a proxy to a method result, or an association to a mechanism.

## Output

Write `PAPER_CLAIM_AUDIT.md`:

```markdown
# Paper Claim Audit
- verdict / reviewer / time:
- manuscript files and raw inputs:

| ID | Location | Manuscript claim | Reconstructed evidence | Verdict | Repair |
|---|---|---|---|---|---|

## Cross-location inconsistencies
## Missing raw evidence
## Required repairs
## Claims verified unchanged
```

At submission assurance always write `PAPER_CLAIM_AUDIT.json`, including:

- `audit_skill: paper-claim-audit`;
- verdict, reason code, summary, reviewer/thread/time, trace path;
- hashes for every declared manuscript and raw input;
- per-claim evidence path, reconstructed value/semantics, verdict, and repair.

Use paper-relative paths for in-paper files and absolute paths for external raw
artifacts. Recompute hashes during submission validation; any mismatch makes the audit
stale.

The audit emits findings. Apply repairs through `paper-writing mode: write`, then rerun
only affected claims. It cannot modify raw evidence or strengthen a claim beyond it.
