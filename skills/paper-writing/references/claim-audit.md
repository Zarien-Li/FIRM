# Manuscript Claim Audit

Use after a narrative draft exists to check whether manuscript numbers,
configurations, populations, and qualifiers match raw artifacts. Experiment validity
and citation support belong to `research-review`.

## Audit Independently

Give a fresh context the compiled manuscript, source files, exact raw result/config
artifacts, and metric definitions. Do not provide author explanations, prior verdicts,
desired outcomes, or fix summaries. The executor declares the complete input set.

Inventory consequential claims in the title, abstract, contributions, body, captions,
tables, appendix, limitations, and conclusion, including:

- values, deltas, ranges, counts, samples, seeds, and costs;
- model, data, configuration, evaluator, rank, and consistency statements;
- causal, natural, general, robust, deployable, efficient, or SOTA qualifiers;
- population and scope claims;
- any promotion of diagnostic, oracle, proxy, or selected evidence.

For each claim, locate exact records; reconstruct filtering, aggregation, uncertainty,
and rounding; verify the model, data, seed, sample, configuration, and evaluator; and
check every repeated occurrence. Distinguish induced from natural, association from
cause, diagnostic from deployed, selected from independent confirmation, and a cell
from its claimed population.

Use `PASS`, `WARN`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, or `ERROR`. A numerically
correct claim still fails when its semantics exceed the evidence.

## Record And Repair

Write `PAPER_CLAIM_AUDIT.md` with inputs and reviewer identity, then one row per claim:

```markdown
| ID | Location | Manuscript claim | Reconstructed evidence | Verdict | Repair |
|---|---|---|---|---|---|
```

Include cross-location inconsistencies, missing raw evidence, and required repairs. At
submission assurance also write `PAPER_CLAIM_AUDIT.json` with the audit skill, verdict,
reason, reviewer/thread/time, trace path, hashes for every input, and per-claim evidence,
semantics, verdict, and repair. Recompute hashes at final validation; changed inputs
make the corresponding result stale.

Apply repairs through `paper-writing mode: write`, then rerun only affected claims. The
audit may correct or qualify prose; it cannot modify evidence or strengthen a claim.
