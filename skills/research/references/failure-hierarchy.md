# Failure hierarchy

Use the narrowest diagnosis supported by the evidence.

## 1. Run or implementation failure

Examples: crash, data leak, wrong metric, dead code, mismatched config, failed
convergence, corrupted output. Repair and rerun; no scientific conclusion yet.

## 2. Optimization or statistical uncertainty

The implementation is plausible but the estimate is too noisy, undertrained, or
sensitive to a known stochastic factor. Add only the seeds or optimization checks
needed to resolve the uncertainty.

## 3. Realization failure

A competent implementation of the current design loses or fails to affect the
target behavior. Treat the run as design evidence. Do not infer that every method
sharing the broad motivation must fail.

## 4. Primitive failure

A controlled comparison shows that the load-bearing component does not mediate the
claimed effect, or a simpler mechanism dominates it. Redesign at the causal level
rather than decorating the same mechanism.

## 5. Family or program failure

Only broad, fair, repeated evidence across serious realizations and alternatives
can support this conclusion. State the covered family and population precisely;
“we tried several versions” is not enough.

## Constructive lineage record

For every failed method version, preserve:

- the causal bet;
- the exact change from its predecessor;
- the competent result;
- the localized failed assumption;
- what remains valid;
- what the next design must inherit or replace.
