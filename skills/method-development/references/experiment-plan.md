---
name: experiment-plan
description: Plan empirical-contact, explanatory, construction, expansion, and claim campaigns whose plausible outcomes change a scientific decision. Use to choose comparisons, ablations, seeds, ordering, utility checks, and compute after the live question is known.
---

# Experiment Planning

Plan evidence that can change understanding or construction. Do not maximize run count,
fill a generic paper table, or replace a real method with cheap probes.

## Plan From The Live Scientific Question

Read the program origin, current scientific state, strongest and inconvenient evidence,
published frontier, current problem model or construction arc, active work, utility
risks, and operational constraints. Write one campaign-level question and the decisions
that materially different outcomes would change.

The appropriate evidence depends on the episode:

- **contact:** establish competent behavior on the accepted task and expose natural
  successes, failures, and disagreements;
- **explanation:** distinguish problem models at the earliest link where they imply
  different designs;
- **construction:** activate, remove, replace, or reorganize a component while preserving
  the named utility;
- **expansion:** test a contrast predicted by a credible primitive;
- **stabilization or claim:** establish the bounded comparison, reliability, tradeoff,
  and scope required by the intended paper.

These labels describe the question; they are not gates. Before substantial compute,
state the best scientific consequence of success. If perfect success only fixes a
private cell with no accepted-task or community consequence, revise the question before
scaling.

## Select Evidence For Decision Value

Prioritize a run when plausible outcomes would:

- establish or challenge a natural premise;
- distinguish explanations that imply different constructions;
- reveal whether the intended computation engages;
- teach which component or interaction the next realization needs;
- expose a substrate, implementation, or evaluator defect that blocks interpretation;
- change the decisive published comparison or accepted-task consequence;
- resolve uncertainty large enough to reverse the current decision;
- test a principle-predicted transfer after a positive object exists.

Defer work whose outcomes merely add a favorable cell, another caveat, or descriptive
detail without changing the arc. A possible reviewer question is not by itself a
scientific reason.

Before evidence first chooses or reshapes a method, map partition use, selection
variables, temporal availability, mutable state, caches, targets, external signals, and
the evaluator path. The complete validity requirements live in
`research-foundation/references/experiment-integrity.md`; do not recreate them in the
campaign plan.

## Match The Design To The Question

An explanatory experiment should contrast alternatives at their earliest meaningful
divergence. Prefer matched successes and failures, controlled substitutions, trace
alignment, code-path interventions, and incumbent component comparisons. Stop when the
remaining accounts imply the same first construction; do not instrument the whole model
for completeness.

A construction campaign follows one central design question. For each successor
realization, state one inheritance sentence:

`Because the previous run contradicted X while preserving Y, change component Z; the
new realization uniquely predicts W.`

Without that sentence, the run is tuning, an unrelated candidate, or a new episode.
Use paired or compact factorial comparisons when components compensate or gate one
another. Check utility when it can change the design, and always before the method is
treated as positive and scalable.

Support or feasibility conditions describe what one frozen run is competent to test.
If treatment formation fails, record that implementation fact; do not report method
transfer. During formation, evidence-directed repair is legitimate. Freeze exact
treatments only when confirming a claim.

## Use Baselines At The Needed Resolution

A prototype may test plumbing, engagement, or one component job. A claim-bearing
comparison uses the healthy accepted surface and role-appropriate published methods
established by `research-foundation`, plus matched attribution and the utility or cost
implicated by the claim. Before paper-sized confirmation, freeze the bounded decisive
comparison set and whether success means primary-metric superiority or a meaningful
Pareto gain. A partial table win, post-hoc metric switch, or unmatched substrate remains
development evidence.

## Allocate Seeds For Uncertainty, Not Rescue

During formation, normally run and read one healthy paired development seed. A clear,
meaningful loss calls for diagnosis or redesign. Repeat only when variance,
nondeterminism, or optimizer instability makes the sign genuinely unresolved. Once a
coherent positive realization exists, use enough independent repetitions for the
reliability implied by the claim.

Do not prelaunch repetitions whose relevance depends on the first result. Preserve
failed and non-converged runs. A verified implementation or evaluator correction earns a
clean matched rerun; it does not erase the original execution record.

## Separate Core Evidence From Optional Scale

Use research compute to establish competent contact, distinguish explanations, and
learn component jobs. Use paper-sized compute only after direct artifacts support a
credible candidate and its scientific return is clear.

The active campaign must close every paper-critical link: natural premise, competent
realization, decisive comparisons, end-to-end utility, load-bearing attribution, honest
tradeoffs, and the accepted-surface evidence required by the intended claim. Once that
chain is sufficient, large grids that only enlarge the table belong on the designated
high-compute machine or remain optional. This is a placement rule, not permission to
stop at a pilot.

Parallelize only runs whose relevance does not depend on unread results. While compute
runs, advance result-independent code, baseline preparation, analysis tooling,
literature, and recovery paths.

## Plan Principle-Predicted Expansion

After a credible primitive exists, choose one contrastive surface whose model family,
task condition, data geometry, temporal structure, scale, or operating regime makes the
principle predict a meaningfully different outcome. Use the smallest faithful comparison
that can separate a reusable primitive from a friendly-setting trick. A negative result
may narrow or repair the principle; it does not justify serial dataset search.

Creative collaboration for a concrete gap follows
`research-pipeline/references/collaboration.md`; the experiment plan records only the
selected implementation and discriminating comparison, never an untested proposal as
evidence.

## Register And Execute At The Right Resolution

An ordinary formative run records its question, unique prediction, implementation,
matched comparator, data, evaluator, metric, seed, stopping condition, competence,
artifacts, and recovery paths. Expensive or claim-defining work also freezes population,
treatment, statistical unit, utility, forecast, artifact risks, and compute.

Use `experiment-operations` for registration, launch, monitoring, and mechanical
campaign manifests. Registration freezes the run, not the evolving research program.
Verify a known case end to end, identities, metric direction, component engagement,
durable outputs, and real-step memory/runtime before scaling.

## Durable Plan

Create `EXPERIMENT_PLAN.md` only when several dependent runs need coordination:

```markdown
# Experiment Plan
## Program Question And Current Episode
## Evidence Or Construction Bundle
- central question and distinct predictions:
- implementation, comparisons, utility, population, and evidence roles:
- outcomes that materially change the decision:
## Run Order And Dependencies
- config, command, log, result, checkpoint, resume path, and compute:
## Deferred Work
- work made dependent, redundant, or unsupported and why:
```

Planning does not grant method or paper maturity.
