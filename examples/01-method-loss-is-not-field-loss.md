# Case 1: A Method Loses Once

## Situation

A new routing primitive is trained on one competent paired development seed.
It loses to a strong simple baseline by a large margin. The implementation
converged, budgets match, and the difference is directional rather than noise.

## Common Agent Failure

Agents often choose one of two bad reactions:

1. declare the method family or field exhausted;
2. run five more seeds and hope one becomes positive.

Both confuse design uncertainty with statistical uncertainty.

## ResearcherOS Response

The first seed has already answered the statistical question needed at this
stage: the current realization is not competitive. The next action is to find
where the intended mechanism failed to activate.

The researcher:

- verifies implementation, optimization, and evaluator parity;
- checks whether the intervention actually changes its intended internal or
  behavioral quantity;
- retains the working component and replaces the implicated component;
- compares the repaired version on one paired seed before expanding seeds;
- asks the second PI whether the revised primitive still serves the original
  program and has a meaningful best-case prize.

## Starting Prompt

```text
Use research-pipeline as the persistent first author. Read RESULT.md and the
training artifacts. The new method loses clearly to the matched baseline on
one competent development seed. Do not close the field and do not launch more
seeds to search for a win. Diagnose implementation, optimization, actuation,
and task-value failure; preserve what worked; propose and implement the next
evidence-directed method version; then run one paired test.
```

## Expected Artifacts

- `PIPELINE_STATE.md` separates program, candidate method, and paper maturity.
- `METHOD_LINEAGE.md` records what v1 predicted, what failed, and what v2
  changes.
- `EXPERIMENT_PLAN.md` contains one discriminating paired test.
- A later multi-seed run happens only after a coherent positive result or
  genuine stochastic ambiguity.

## Why It Matters

This prevents both premature abandonment and expensive seed theater. A failed
method becomes information for construction rather than a stopping ritual.
