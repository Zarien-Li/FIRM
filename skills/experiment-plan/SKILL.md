---
name: experiment-plan
description: Plan coherent empirical-contact, explanatory, construction, expansion, and claim campaigns. Use to choose evidence bundles, matched comparisons, ablations, utility checks, seeds, run order, and compute at the resolution of the current research episode rather than turning every run into a paper gate.
---

# Experiment Planning

Plan experiments that change a scientific or design decision. Do not maximize run
count, fill a generic paper table, or replace a real construction with cheap probes.

## Plan From The Current Episode

Read the Program Compass and identify:

- the important question and accepted task or natural system;
- the current episode: contact, explanation, construction, expansion, stabilization,
  or harvest;
- strongest evidence and inconvenient evidence;
- current problem model, competing explanations, or construction arc;
- serious incumbent, simple alternative, nearest-rival threat, and substrate health;
- relevant utility risks and operational constraints;
- active and completed-unread work whose result may change the plan.

Plan at the resolution of the episode. Early empirical contact may legitimately learn
about natural behavior without naming a paper contribution. A construction arc should
have one central design question across versions. Paper-oriented campaigns begin only
after a credible positive object exists.

Before substantial compute, state the best scientific consequence if the episode
succeeds. If perfect success only fixes a private cell with no independent value or
accepted-surface return, revise the question before scaling.

## Use Two Resource Postures

Use a **research/probe budget** to obtain competent contact, distinguish explanations,
activate a construction, and learn component jobs. Cheapness is not the goal; enough
contact to make a sound design decision is.

Use a **paper/expansion budget** only after a credible positive object exists and the
principle is important, not absorbed by the nearest rival, and plausibly reusable or
consequential. Spend it on dimensions that strengthen the central contribution:
accepted-task value, principle-predicted transfer, scale/model behavior, reusable data
or supervision, mechanism, reliability, and adoption cost.

Separate **submission sufficiency** from **large-scale expansion**. The active machine
must still close every paper-critical link: the natural premise, competent realization,
strong and nearest-rival comparisons, end-to-end utility, decisive components, honest
tradeoffs, and enough accepted-surface/generalization evidence for the intended claim.
Once that chain already establishes a credible SOTA-level paper, do not spend thousands
of GPU-hours locally on exhaustive model, dataset, seed, or scale grids that only enlarge
the table. Package those optional expansions for the designated high-compute machine.
Run them locally only when their outcome can still change correctness, novelty, the
central claim, or submission viability. This is not permission to stop at a pilot or omit
owed evidence; it is a placement rule for work beyond the submission-sufficient core.
A project with no credible positive object and no submission-sufficient paper is never
`post_sufficiency_scale`. Failure of one construction family may close that family, but
cannot use this compute policy to terminate or transfer the broad program; re-ground
the program and separate substrate, problem, incumbent, and construction failures first.

Do not distribute paper budgets evenly, rescue low-leverage cells with large matrices,
or confuse experiment volume with idea size. There is no fixed run or failure quota;
compare marginal scientific value and opportunity cost.

## Choose Worthwhile Evidence

Prioritize an experiment when plausible outcomes would:

- establish or challenge a natural premise;
- distinguish live explanations that imply different designs;
- activate, remove, replace, or reorganize a construction component;
- expose an implementation or substrate failure that blocks interpretation;
- change the decisive comparison or accepted-task consequence;
- resolve uncertainty large enough to reverse a decision;
- test a principle-predicted expansion after a positive object exists.

Defer a run when every outcome merely adds detail, another favorable cell, a reviewer
caveat, or a richer explanation without changing the research arc. A possible reviewer
question alone is not a scientific reason.

## Plan Explanatory Evidence As A Model Test

When the problem is not yet understood deeply enough to design, experiment against the
problem model rather than collecting more descriptors. Choose the smallest natural or
controlled contrast that separates alternative accounts at their earliest divergent
link. State how each plausible outcome changes the represented information, state
transition, interaction, credit path, execution, or preserved capability in the
proposed account.

Prefer matched success/failure cases, controlled substitutions, trace alignment, code-
path interventions, and incumbent component comparisons when they answer that question.
Do not demand every modality at once or instrument the whole model for completeness.
The explanatory episode ends when the remaining alternatives imply the same first
construction or when one account has enough support to make component jobs and
preservation constraints non-arbitrary.

## Plan A Construction Arc

Plan the arc around one central design question, not one isolated version. Across its
iterations it should establish:

1. a trainable or executable implementation on the accepted task;
2. component substitutions or interactions that teach what the method should become;
3. a paired utility check at the point where that cost matters for design;
4. the strong simple and nearest-rival comparisons needed before a paper claim.

Early versions need not run every final comparison. They must be competent for the
question they are asked. State what each outcome would add, remove, replace, separate,
or retain in the next implementation. Use paired or compact factorial comparisons
when components compensate or gate one another.

Smoke tests, CPU checks, oracle probes, and activation audits may precede a real run.
They prove plumbing or engagement, not a method, and should not create new method names
or review cycles.

## Allocate Seeds For Their Real Job

Random seeds estimate stochastic uncertainty; they do not explain or repair a method.

- During formation, normally run and read one healthy paired development seed.
- A clear meaningful loss calls for diagnosis or redesign, not a seed sweep.
- Repeat when the result is near the stochastic resolution boundary, conflicts with
  known variance, or may be an execution outlier.
- After a coherent positive realization, use enough independent repetitions for the
  reliability implied by the claim.

Do not prelaunch repetitions whose relevance depends on the first result. Preserve
failed and non-converged runs. A verified implementation or evaluator defect normally
earns one clean matched rerun; a continuing directional loss requires a changed design
question, not a new seed or coefficient.

## Match The Comparison To The Question

A prototype may test engagement, optimization, or one component job. Label what it can
and cannot adjudicate.

A claim-bearing comparison requires:

- credible evaluator and intended natural population;
- competent substrate and direct incumbent;
- fair information, supervision, capacity, optimization, and evaluation treatment;
- strongest simple alternative and claim-threatening rival;
- explicit unique prediction;
- relevant capability, coverage, latency, memory, compute, or cost evidence.

Do not infer superiority or primitive failure from a weak reader, untrained bridge,
compound backbone/data/mechanism change, sampled-only baseline, or semantically
mismatched protocol.

## Plan Expansion After A Positive Object

After the first credible positive construction, let the lead PI and optionally Gemini
form the Program Expansion view. Before a large campaign, one sparse Codex pass may
test a named fatal validity or ownership risk; it is not a mandatory gate. Select only
axes predicted by the same principle:

- simplification or a lower-friction realization;
- reusable supervision, data generation, curriculum, or system machinery;
- accepted tasks, modalities, natural systems, model families, generations, or scale;
- mechanism evidence separating the principle from the nearest rival;
- utility and adoption.

Write one campaign-level question. Another benchmark with no new prediction and a
larger version of the same table are breadth, not scientific expansion.

## Register At The Right Resolution

An ordinary formative run needs a compact record:

- question and unique prediction;
- implementation and matched comparator;
- data, evaluator, metric, development seed, and stopping;
- what the run is competent to test;
- config, log, result, checkpoint, and resume paths.

An expensive, hard-to-repeat, or claim-defining run additionally freezes population,
treatment, metrics, statistical unit, utility, forecast, artifact risks, compute, and
outcome interpretation. Use `research-contract` when separate registration improves
provenance. Registration freezes that run, not the evolving research program.

## Order And Adapt

Before scale, verify one known case end to end, data/checkpoint/evaluator identity,
metric direction, intended component engagement, durable outputs, and memory/runtime
from a real step. These checks establish execution, not scientific equivalence.

Order work by dependency. Parallelize only runs whose relevance does not depend on
unread results. While compute runs, advance result-independent code, baseline
preparation, analysis tooling, literature, and resume paths.

After a result, update the observation. Change the plan immediately only when it
invalidates evidence, answers the arc's design question, makes dependent work
redundant, or materially changes the program. Read a completed construction arc as a
bundle before opening a new one.

Use `signal-analysis` and lead-PI synthesis for scientific interpretation. Use Gemini
selectively for invention and `research-review` Codex only under its sparse late-stage
policy.

## Durable Plan

Create `EXPERIMENT_PLAN.md` when several dependent runs need coordination:

```markdown
# Experiment Plan
## Program Question And Current Episode
## Evidence Or Construction Bundle
- central question and distinct predictions:
- implementation, component comparisons, utility, and rivals as currently needed:
- population, treatment, metrics, statistics, and evidence roles:
- what material outcomes change:
## Run Order And Dependencies
- config/log/result/checkpoint/resume paths and compute:
## Deferred Work
- work made dependent, redundant, or unsupported and why:
```

Planning does not grant method or paper maturity. Execute through `run-experiment` and
monitor through `monitor-experiment`.
