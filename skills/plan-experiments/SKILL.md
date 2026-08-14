---
name: plan-experiments
description: Designs a claim-aware, compute-efficient experiment plan with decisive comparisons, ablations, seed allocation, run order, and adaptive decision points.
when_to_use: Use before a serious experiment campaign or when deciding which experiment can most change the method or paper conclusion.
argument-hint: "[method, claim, and compute budget]"
---

# Experiment Plan

Design experiments to change beliefs and support claims, not to fill a conventional paper table.

The plan should connect each experiment to a research question, a competing explanation, and a design consequence. Keep the main story compact; combine measurements when one run can answer several compatible questions.

## Start From The Current Bet

Read the current research state and any existing run registration. Identify:

- original research program and the current paper's explicit bridge to it;
- natural problem class and value metric;
- discovery slice versus the natural population the method or paper intends to cover;
- accumulated scope debt and the evidence intended to repay it;
- natural support, severity, affected systems, and the decision expected to change;
- central thesis and strongest contrary evidence;
- method primitive and unique prediction;
- current realization maturity: what has only been prototyped, what has been shown to activate, and what is ready for a claim-level comparison;
- strongest incumbent and simple alternative;
- claims the paper hopes to earn;
- the bounded current paper claim and which unresolved issues could actually change it;
- important capability, coverage, latency, or cost risks;
- resource and user constraints.

If the method is still only a diagnostic signal or surface knob, improve the causal/design question before scheduling a large matrix.

Before substantial method compute, make sure the plan is not resting on an avoidable semantic error: verify metric and aggregation, labels and data construction, evaluator behavior, information and supervision parity, the strongest direct or deterministic alternative, and enough natural support for the proposed opportunity. Also state the strongest honest paper-level contribution if the plan succeeds perfectly. If even perfect success would remain a private-cell result without field-level consequence or reintegration, revise the bet before scaling. This is one focused foundation check tied to the central bet, not a ladder of cheap gates. Once credible, proceed to method formation unless new evidence reopens it.

Do not choose a dataset, operator, architecture, or regime because the candidate method appears likely to win there. If a special setting is used diagnostically, label it as such and include the experiment whose outcomes decide whether the learned principle re-enters the original standard task or system.

## Separate Probe Budget And Paper Budget

Use **probe budget** to establish the natural problem, governing principle,
nearest-rival opening, and one credible realization. Keep it concentrated enough that
weak projects fail cheaply and informative negatives redesign the construction.

Unlock **paper budget** only when the principle is simple and consequential, the
nearest rival does not already own it, one competent realization has credible positive
end-to-end value, and expansion can strengthen the contribution. Paper budget may fund
predicted task/model transfer, a data or supervision engine, scale behavior, mechanism,
and complete utility evidence. It must not fund regime shopping, indiscriminate seed
grids, or breadth whose only purpose is a larger table.

Before allocating paper budget, run one Program Expansion review. Record which axes are
earned, deferred, or unsupported and what ten times the resources would change.

## Value Of Another Experiment

An experiment deserves current priority when at least one plausible outcome would change the method design, the core paper claim, the decisive comparison, a major reviewer judgment, or the honest submission scope. If every outcome would merely make the story richer while leaving those decisions unchanged, defer it to later work.

Do not impose a fixed experiment count or deadline as a substitute for judgment. Compare the expected value of the next run with finishing a mature contribution already earned. Research remains open after a paper is completed.

Expected value includes the prize, not only information gain. A highly discriminating experiment can still be a poor allocation when both outcomes concern an increasingly private object. Prefer work that either forms the method or reconnects the learned principle to a natural standard surface.

## Put High-Information Experiments Early

Early experiments should answer uncertainties that would change the method or major allocation of compute. Examples:

- whether the intervention reaches the proposed cause;
- whether the strongest simple alternative is already sufficient;
- whether the gain survives a paired utility check;
- whether the problem is natural beyond the discovery slice;
- whether the broader population, rather than only the selected slice, carries enough value to justify the method;
- whether a mechanism discovered in the slice changes behavior on the accepted task or natural system that motivated the seed;
- whether the method is trainable at the intended scale;
- whether two causal explanations make different predictions.

Do not use cheapness as the sole criterion. Once a coherent method is ready, a completed training run may be more informative than another probe.

Do not make one early run answer every question at once. A prototype run may be designed to learn whether the intended computation activates, whether optimization can reach it, or whether the target improvement creates interference elsewhere. A claim-defining comparison should use a realization mature enough that losing to a tuned incumbent is scientifically interpretable. These are different evidential roles, not mandatory stages.

## Allocate Random Seeds By Evidence Role

Random-seed repetition estimates stochastic reliability; it does not repair a method or explain a failure. During method formation, prefer one fixed development seed or the smallest credible cohort with a paired baseline, then read the full behavior before allocating repetitions. The purpose is to expose what the current realization computes, where it helps, and where it breaks.

A trustworthy, materially bad first run from a competent realization is already evidence that the current realization has a problem. Diagnose or redesign before replication; do not launch more seeds merely hoping that one becomes positive. If the intended computation was inactive, repair implementation, optimization, or integration; if it was active and lost clearly, use raw behavior and constructive ablation to redesign the implicated component. Neither conclusion closes the primitive or field.

Additional seeds are useful when the first result is genuinely close to the noise scale, conflicts with a known variance estimate, may be an execution outlier, or when a stabilized positive method is ready for claim-level reliability. State what uncertainty the repetitions resolve. One lucky seed is not method success, and several repetitions of the same broken realization are not method progress.

Use paired seeds, splits, examples, or bootstrap units where possible so randomness does not obscure the method comparison. Do not prelaunch a large seed sweep before reading an informative development run unless parallel execution is itself justified by queue economics and every repetition is already needed for a claim or a specific instability question.

## Use Ablation To Build The Method

Ablation is not reserved for explaining a finished architecture. Plan a compact sequence of construction comparisons around live component and interaction hypotheses. Adding a missing pathway, replacing a suspect operator, freezing one learner, separating two objectives, or removing a redundant mechanism can be both a causal test and the act that creates the next method version.

Each formation experiment should say what design changes under its plausible outcomes. Prefer comparisons that expose interactions when one-at-a-time removal would be misleading. Match information, supervision, capacity, optimization effort, and evaluation closely enough to know whether the component or its treatment caused the result. Read target gains and side effects together so the next construction preserves one while repairing the other.

Do not demand that discovery ablations also serve as final confirmation. Preserve their forecasts and outcomes as development evidence. Once the intended computation is active and the design and component roles are coherent, repeat the paper-carrying necessity and interaction comparisons on appropriate held-out seeds, settings, or other fresh evidence when the claim requires it. Several failed variants do not by themselves make a method stable. Conversely, do not rerun every historical branch merely for a large table; retain only comparisons that explain the final method or a consequential boundary.

## Build A Coherent Evidence Set

Typical evidence needs include:

- **Anchor comparison:** method against strong current and simple baselines under matched conditions.
- **Value result:** effect on the accepted task or real workflow.
- **Reintegration result:** evidence that the mechanism or primitive discovered in a narrow slice changes a standard task, natural system, shared incumbent, or independently consequential population.
- **Mechanism evidence:** intervention or ablation that isolates the proposed design principle.
- **Necessity evidence:** why simpler composition does not make the primitive redundant.
- **Generality:** a second natural dataset, model family, task, or regime chosen because the thesis predicts transfer.
- **Side effects:** general capability, coverage, abstention, latency, memory, compute, or cost. Quantify the tradeoff and match it to the claim; do not demand literal zero regression unless the paper promises it.
- **Reliability:** enough seeds, confidence intervals, paired tests, or repeated runs for the field and effect size.

Not every project needs a separate experiment for every item. One well-designed factorial or paired evaluation can answer several questions.

For a new method, plan enough observation of learning dynamics and component behavior to distinguish a bad primitive from a dormant, under-optimized, or poorly integrated realization. If a method improves the target while harming another regime, include the measurements needed to locate both pathways; do not collapse the vector into a single elimination verdict before attempting an evidence-directed repair.

## Specify Each Experiment

For every block, write:

- research question;
- claim or belief it informs;
- evidence role: discovery | method formation | claim confirmation;
- relation between the evaluated sample and the intended value-bearing population;
- relation to the original program and whether this is discovery or reintegration evidence;
- compared systems and why they are fair;
- benchmark, split, sampling, and model versions;
- intervention and controls;
- metrics, paired utility metrics, and statistical analysis;
- forecast and belief update for each outcome;
- what the implementation is mature enough for this run to adjudicate;
- implementation/config path;
- compute estimate and checkpoint/resume strategy;
- artifact risks and sanity checks;
- design decision that follows.
- construction consequence: what is added, removed, replaced, separated, or retained in the next realization.
- reintegration decision: how each outcome changes return to a standard task or system.

Avoid experiments whose only purpose is to accumulate positive numbers.

## Baseline And Benchmark Discipline

Use strong, correctly configured, semantically matched versions. Include current representative systems and, when useful, canonical reproducible anchors. The newest release is not automatically the fairest baseline if it is inaccessible, unstable, changes the task, or prevents mechanism-level inspection; explain such substitutions and keep any resulting ownership threat open. Include field-standard baselines and the strongest simple explanation. Do not change candidate pools, prompts, data budgets, stopping, or evaluators asymmetrically.

Match information, supervision, and evaluation immediately; match engineering maturity before making a primitive-level conclusion. A mature incumbent should still be reported against an early prototype, but that comparison answers current end-to-end readiness, not necessarily whether the new design can work after the intended mechanism is activated and competently optimized. State which conclusion the comparison earns.

Benchmarks are evaluation anchors, not the paper contribution. Discovery slices may diagnose mechanisms, but main claims need accepted or naturally justified settings.

Choose breadth because it tests the thesis. Do not add unrelated datasets merely to enlarge a table, and do not claim generality from one convenient family.

Before the claim-defining campaign, stabilize the field-standard and strongest-simple baseline set for the intended claim. A late baseline should be added when it is semantically matched and could change the conclusion. Do not repeatedly move the standard because a related method has a similar name, uses a different setting, or only threatens an aspirational claim.

## Sanity Before Scale

Before launching a costly run:

- execute one known case end to end;
- verify data, checkpoint, evaluator, and metric direction;
- confirm the method actually changes the intended computation;
- inspect raw outputs for a small batch;
- verify logs, checkpoints, result markers, and resume behavior;
- estimate memory and runtime from a real step.

These are execution safeguards, not scientific admission gates.

## Adaptive Planning

Plans evolve as evidence arrives. Preserve registered decisive-run definitions, but revise later blocks when earlier results change the thesis or make a comparison irrelevant.

After each consequential result, ask:

- Did the result match the forecast?
- Which explanation gained or lost probability?
- Does the method need redesign before more scale?
- Did useful behavior appear that the next version should preserve, even if the registered headline failed?
- Are regressions evidence of a separable interference pathway or of the primitive itself?
- Has the current realization earned a claim-level comparison, or only a prototype-level lesson?
- Which planned experiment is now redundant?
- What new high-information comparison became visible?
- What is the observation, explanatory update, and design consequence before the paper consequence?
- What effect does this have on the current paper claim?
- Is the next run likely to change the method or paper, or is a mature contribution ready to finish?

Update the plan with reasons. Do not silently rewrite completed-run expectations.

## Independent Plan Review At Real Forks

Use `/firm:second-pi` before a claim-defining compute commitment when there is a real choice among causal tests, baselines, or method designs. Do not invoke it merely to bless a finished matrix.

Provide the original program, current paper bridge, thesis, primitive, scope debt, strongest alternative, forecasts, proposed experiment blocks, compute cost, and side-effect risks. Ask whether perfect success is worth the cost, which experiment most changes the thesis or method, whether the plan returns to a standard surface, which planned block is ceremonial, what decisive comparison is missing, and whether confound parity or a weaker-story explanation defeats the plan.

Use a fresh independent review. Record adopted and rejected recommendations in the plan rationale; the lead researcher remains responsible for the final allocation.

## Durable Plan When Useful

Write or update `EXPERIMENT_PLAN.md` when several runs, claims, or dependencies need durable coordination. Use `EXPERIMENT_TRACKER.md` when active execution would otherwise lose configs and provenance. A small discriminating experiment can be recorded directly in the existing research state or tracker; missing paperwork is not a reason to delay it.

```markdown
# Experiment Plan

## Research Bet
- original research program:
- current paper and paper-to-seed bridge:
- thesis:
- method primitive:
- strongest alternative:
- target claims:
- value spine and intended population:
- scope debt and repayment evidence:
- best-case contribution:
- reintegration target:
- budget class: probe | paper
- principle and credible positive realization:
- earned expansion axes and ten-times-resource consequence:

## Evidence Map
| Question/claim | Experiment | Evidence type | Method or paper decision it changes |
|---|---|---|---|

## Experiment [ID]: [name]
- question:
- relation to original seed and scope movement:
- forecast:
- systems and controls:
- data/model/protocol:
- metrics and utility checks:
- statistical plan:
- artifact checks:
- config and result paths:
- compute/resume plan:
- interpretation and next design decision:
- reintegration decision changed:

## Run Order
- now:
- after result X:
- parallelizable work:
- deferred and why:
- deferred beyond the current paper:

## Coverage And Limits
- completed evidence expected:
- intentionally untested scope:
- user decisions or exceptional budget:
```

The tracker should record actual command/config, status, logs, checkpoints, results, deviations, and whether the run is claim evidence or diagnostic only.

## Durable Execution

Use `run-experiment` (including Batch Mode for grids and sweeps) and `monitor-experiment` for reliable execution while retaining the same scientific ownership. A queue or interrupted run should update durable state and resume paths, not change the scientific verdict.
