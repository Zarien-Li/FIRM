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
- strong recent published incumbent, nearest-rival threat, and substrate health;
- relevant utility risks and operational constraints;
- active and completed-unread work whose result may change the plan.

Plan at the resolution of the episode. Early empirical contact may legitimately learn
about natural behavior without naming a paper contribution. A construction arc should
have one central design question across versions. Paper-oriented campaigns are useful
when the PI's artifact-grounded candidate argument makes their scientific return clear.

Before substantial compute, state the best scientific consequence if the episode
succeeds. If perfect success only fixes a private cell with no independent value or
accepted-surface return, revise the question before scaling.

Before the first result is allowed to choose or reshape a method, read
`../shared-references/experiment-integrity.md` and put the information-boundary map in
the run record: partition use, selection variables, temporal availability, mutable
state, caches, targets, external signals, and evaluator path. This is part of defining
the experiment, not a late paper audit.

## Use Two Resource Postures

Use a **research/probe budget** to obtain competent contact, distinguish explanations,
activate a construction, and learn component jobs. Cheapness is not the goal; enough
contact to make a sound design decision is.

Use a **paper/expansion budget** when direct artifact reading supports focused
maturation and the principle appears important, not absorbed by the nearest rival, and
plausibly reusable or consequential. Spend it on dimensions that strengthen the central contribution:
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
A project without an artifact-grounded candidate argument and submission-sufficient paper
cannot justify optional post-sufficiency scale by its own label. Failure of one construction family may close that family, but
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

## Use Gates To Interpret Runs, Not Authorize Research

A support, eligibility, quality, convergence, or feasibility gate states what one
frozen run is competent to test. If it fails before the primary outcome, record the
implementation or treatment-formation failure honestly; do not report a method
transfer result that never occurred. The gate expires with that run and cannot become
a project-wide ban on redesign.

During method formation, adapt the method-owned construction when the failure reveals
what must change. This may mean repairing generation, replacing a brittle evaluator,
using a matched feasible treatment budget, or changing component interaction while
preserving the accepted task and value contract. Such evidence-directed adaptation is
research, not result shopping. Freeze exact treatments only for claim-confirmation.

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
4. the decisive published-incumbent and nearest-rival comparisons needed before a
   paper claim.

Early versions need not run every final comparison. They must be competent for the
question they are asked. State what each outcome would add, remove, replace, separate,
or retain in the next implementation. Use paired or compact factorial comparisons
when components compensate or gate one another.

For every successor realization, put one inheritance sentence in the plan: `because
the previous run falsified prediction X while preserving Y, change component Z; the new
realization uniquely predicts W`. If no such sentence is supported, do not spend the
run as `v2`; return to explanation or open a new episode without inherited maturity.

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
- strongest relevant published incumbent and claim-threatening rival;
- explicit unique prediction;
- relevant capability, coverage, latency, memory, compute, or cost evidence.

Match the substrate as well as the metric. State the seed-authorized model scale,
training treatment, task population, information boundary, and actual run regime. A
proxy run may answer an implementation question, but it cannot carry the main method
claim when the incumbent effect or rival ordering has not been reproduced there.

For method-paper entry, freeze the claim-sufficient decisive comparison set and value
contract before reading the result. Include the bounded set of field-recognized and
directly claim-threatening healthy baselines known at freeze time. Define in advance
whether success means primary-metric
superiority or a meaningful Pareto gain in capability, quality, robustness, coverage,
latency, memory, compute, supervision, or adoption cost. The realized method must earn
that advantage under matched treatment and pass paired utility. A partial table win,
post-hoc metric switch, or gain bought only by an unmatched budget remains pre-paper
evidence; a baseline loss blocks entry only when it defeats the actual intended claim.

Do not infer superiority or primitive failure from a weak reader, untrained bridge,
compound backbone/data/mechanism change, sampled-only baseline, or semantically
mismatched protocol.

## Turn A Pre-Target Gemini Proposal Into Evidence

When a realization is credibly effective but still misses its pre-specified value
target against a decisive baseline, Gemini may help propose one load-bearing
improvement. Planning resumes with the PI:

- name the exact baseline gap, raw contrary cases, and utility that must be preserved;
- select at most one evidence-licensed proposal after literature collision checking;
- implement it in the project rather than treating the proposal as a result;
- freeze the smallest matched comparison that can adjudicate the gap and utility;
- update maturity only from completed raw artifacts.

Do not batch a Gemini idea menu, alter the comparison protocol to favor the suggestion,
or mistake the proposal for experimental progress.

## Plan Expansion After A Positive Object

When a candidate merits focused maturation, let the lead PI and optionally Gemini
form the Program Expansion view. Before a large campaign, one sparse Codex pass may
test a named fatal validity or ownership risk; it is not a mandatory gate. Select only
axes predicted by the same principle:

- simplification or a lower-friction realization;
- reusable supervision, data generation, curriculum, or system machinery;
- accepted tasks, modalities, natural systems, model families, generations, or scale;
- mechanism evidence separating the principle from the nearest rival;
- utility and adoption.

Before writing the full submission matrix, choose one accepted **contrastive surface**
whose mechanism, data geometry, temporal structure, model family, or operating regime
makes the governing principle predict a meaningfully different outcome. Run the
smallest faithful comparison that can distinguish a reusable primitive from a
single-substrate trick. Select it for information, not friendliness. A negative result
may narrow, repair, or replace the principle before large breadth; it does not demand a
serial dataset search. When the intended claim is inherently single-surface or no
faithful contrast exists, state that scope instead of manufacturing a second dataset.

Commit to one campaign-level prediction and read its failure into the construction.
Do not replace a failed precondition or transfer with a succession of datasets chosen
because they are more likely to satisfy the same frozen protocol. Another surface is
justified only when it distinguishes a new principle-level prediction unavailable on
the accepted evidence already in hand.

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
