# Independent claim audit

Read the compiled manuscript in a fresh context, then inspect the raw artifacts
listed in `CLAIMS_EVIDENCE.md`.

For every consequential sentence or table value, classify:

- `VERIFIED`: exact support at the stated scope;
- `OVERSTATED`: evidence supports a narrower statement;
- `MISMATCHED`: number, condition, baseline, or population differs;
- `UNSUPPORTED`: no adequate artifact;
- `INTERPRETIVE`: acceptable only if clearly marked as interpretation;
- `UNVERIFIABLE`: required artifact is unavailable.

Audit especially:

- abstract and contribution bullets;
- best-result and improvement claims;
- averages, relative gains, and compression/speed ratios;
- ablation conclusions;
- generalization and robustness language;
- causal verbs;
- “first,” “only,” “consistent,” and “across all” statements;
- limitations that materially bound the contribution.

Output a table with claim, manuscript location, evidence path, recomputation or
inspection, verdict, and exact repair. Do not rely on the manuscript's own table as
the raw source when a result file exists.
