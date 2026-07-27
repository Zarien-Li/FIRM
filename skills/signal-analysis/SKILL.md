---
name: signal-analysis
description: Inspect raw baseline or method behavior and turn credible contrasts into competing explanations, thesis updates, design consequences, and paper consequences. Use for anomaly organization, artifact checks, surprising or contradictory results, predictive signals, simple-baseline inversions, method failures, and the interpretation of consequential runs before major redesign or submission-oriented writing; do not use it as a verdict gate.
---

# Evidence And Signal Analysis

Use signal analysis to turn observations into better explanations and methods. Do not use it as a cheap falsifier gate.

Do not first build a catalog and then begin interpretation as a separate stage. Inspect, compare, challenge, and reinterpret in one scientific motion.

## Read Raw Behavior Contrastively

Start from the smallest sufficient set of per-example predictions, references, traces, representative successes, failures, and method disagreements. An aggregate delta can locate a change but cannot define its cause.

Compare failures with matched successes, methods on the same examples, realistic with stress regimes, and diagnostic movement with actual value. Seek a repeated structural condition rather than a cluster defined by the method's own score or a post-hoc threshold. Include inconvenient cases that resist the preferred explanation.

Remove plausible measurement explanations early: parser and alignment errors, wrong labels or token positions, leakage, duplicates, truncation, asymmetric prompts or candidate pools, metric direction, denominator mistakes, unstable small samples, fallback behavior, and semantically mismatched baselines. An artifact invalidates the affected observation; it is not evidence against the field.

## Ground The Interpretation

Confirm that the relevant evidence is credible enough for the question being asked. Read representative raw cases, not only summaries. If an integrity issue dominates, repair the evidence before theorizing.

State the observation without mechanism language first:

- what changed;
- where it changed;
- where it did not;
- what the strongest contrast is;
- what value outcome accompanies it;
- what evidence contradicts the obvious story.

Also inspect the opportunity represented by the observation. Estimate from available natural evidence how common the condition is, how much value is lost when it occurs, which serious systems share it, and whether a plausible remedy could change the accepted outcome. Use this as scientific scale, not a formula. A perfectly separable cluster with negligible natural mass may still reveal a mechanism, but it has not yet earned the status of the paper's problem.

Do not equate low frequency with low importance. Severity, theoretical reach, safety consequence, or a decisive counterexample can make a rare class valuable; the research must show that leverage rather than assume it.

Before opening a deeper explanatory branch, record the observation and ask what it changes in the explanatory model and method design. Only then ask whether it threatens the bounded paper claim. It may instead revise the mechanism narrative, reveal a conditioning variable, remove a component, or create later work. A local result does not select the project's permanent contribution type.

## Generate Competing Explanations

Construct several explanations that differ causally, not just verbally. Include when plausible:

- measurement or selection artifact;
- capability or scale floor;
- representation or state limitation;
- objective or credit-assignment mismatch;
- routing, memory, attention, or retrieval failure;
- data-distribution or curriculum effect;
- generic difficulty rather than the named phenomenon;
- a hidden variable exposed by a simple baseline.

For each explanation, state what it predicts on existing cases and what observation would distinguish it from the others.

Do not select the preferred story because it leads to the most convenient method.

Do not reason by false dichotomy. Evidence against one explanation does not make another explanation true unless the alternatives are exhaustive. In particular:

- linear or nonlinear decodability is not evidence that the downstream computation uses the signal;
- equal probe scores do not imply equal state dynamics, optimization, accessibility, or causal role;
- a successful intervention may act through an artifact or side channel;
- an absent effect under one scale or regime does not establish absence elsewhere.

Match language to the evidence type: observation, prediction, intervention, natural contrast, or counterfactual. Name what each result can and cannot identify.

## Seek Explanatory Compression

Look for a variable that explains several awkward observations at once:

- cross-dataset inversions;
- a method helping one group and harming another;
- a simple rule replacing a complicated model;
- a strong probe with weak intervention value;
- an oracle success that the trained system cannot realize;
- easy and extreme regimes behaving differently while the middle remains unknown.

The best thesis often explains both the failure and the success cases. A cluster that requires a separate excuse for every exception is not yet understood.

When the sign or magnitude of a method effect varies across readers, models, datasets, scales, queries, or system states, ask whether that context is the missing variable the method should represent or condition on. Do not treat a dataset name as an explanation, and do not purchase a clean claim by shrinking to one positive cell. Test whether a shared adaptive principle can predict the heterogeneous behavior and support a method with matched fixed and simple conditional alternatives.

## Predictive Signal Versus Causal Handle

A probe, embedding separation, AUC, hidden-state feature, oracle, or attribution can be useful without being an editable cause.

Ask:

- Can the signal be intervened on while preserving the rest of the computation?
- Does the intervention improve the actual task rather than only the proxy?
- Could replacement, injection, masking, or editing create an out-of-distribution artifact?
- Does a stronger simple alternative obtain the same outcome?
- Is the gain paid for by abstention, coverage loss, deleted evidence, latency, or general-capability damage?

If intervention evidence is weak, keep the signal as diagnostic and seek the underlying causal variable.

When a method result is already available, analyze its failure layer before generating another explanation. Distinguish a dormant component, an optimization failure, an intervention that acts without task value, a useful raw effect blocked by deployment or certification, and a mechanism that works only in one natural regime. Each implies a different method revision.

## Move From Crack To Problem Class

Before centering a method on one slice, ask whether the observation reveals a broader positive object the field lacks: a state representation, execution semantic, training axis, routing principle, memory abstraction, uncertainty model, or credit-assignment rule.

State:

- the natural problem class;
- the central tension;
- the design assumption that creates it;
- why existing systems share that assumption;
- what should become possible if the assumption changes.

This is the central thesis. Keep it revisable.

Do not promote a curated anomaly into a paper problem merely because it is clean. Ask whether it occurs naturally, changes meaningful behavior, survives a fair contrast, and reveals a missing abstraction that matters beyond the discovery slice. Synthetic and oracle cases may isolate a mechanism, but they do not establish natural prevalence by themselves.

Keep three scopes distinct in the reasoning: the slice used to discover or isolate the effect, the natural class that carries scientific or practical loss, and the population a future method or paper would cover. If the slice is rare but exposes a shared design assumption, test the broader consequence of that assumption rather than optimizing only the slice. If no broader consequence survives, preserve the slice as diagnostic knowledge and return to a more valuable question.

## Design The Next Experiment

Choose an experiment because it changes a real decision. Good next experiments:

- separate the leading causal explanations;
- test a natural failure boundary of the strongest simple baseline;
- establish whether closing the failure moves value;
- test a causal intervention without proxy leakage;
- reveal whether the correct method locus is at a higher design level;
- establish trainability before a large method commitment.

Prefer an experiment that changes the method or current paper over one that only enriches the explanatory atlas. A scientifically interesting unanswered question can be deferred without being denied.

Do not keep adding local slices after the explanatory uncertainty is already low enough to build the method.

Before a decisive experiment, write a short forecast:

- expected result and confidence;
- result that would surprise us;
- how each outcome changes the thesis or method choice.

## Consult Codex When The Explanation Is Underdetermined

Use `research-review` when the evidence supports several causal stories, contains a cross-regime inversion, when a simple baseline exposes a hidden coordinate that the current thesis cannot explain, or when a consequential result could change method altitude, contribution identity, or paper maturity — consult **before the framing hardens**. This is the independent PI judgment for the scientific ambiguity; do not replace it with a menu sent to the user. Give Codex representative raw cases, the observation table, the prospective forecast, current thesis, strongest contrary evidence, and method lineage.

Ask for `Interpret -> Invent -> Attack -> Assess Maturity`: first compress the full pattern into a deeper variable, then propose the strongest design consequence or discriminating experiment, attack it with the best simpler explanation, and only then decide whether a mature bounded contribution already survives. Present raw evidence and the prospective forecast before the lead researcher's tentative framing. Start a fresh thread so the interpretation is independent. Use `mcp__codex__codex-reply` only to continue the same unresolved question with additional evidence.

Afterward, state what you adopted, what you rejected with evidence, and how the next experiment changed. Do not outsource the thesis verdict to the reviewer.

Until that synthesis is complete, the lead interpretation is provisional: do not write a terminal program label, lock a new paper identity, or promote the tentative story into the authoritative state. Codex is independent input, not final authority. Tool failure never turns into scientific approval, rejection, or pause.

## Consequential Runs: From Result To Claim

When the signal under inspection is a **consequential completed run** (claim-changing, method-shaping, or surprising), read it as a researcher, not as a verdict clerk, and apply the full treatment in this section. Preserve the honest outcome of the run while asking what the evidence changes in the living scientific model. Current validated evidence and the live thesis outrank prior status labels, draft narratives, and historical interpretations; this analysis does not choose the project's permanent identity, close a field, or make an old contract authoritative.

### Establish The Run's Evidence First

Before interpretation, verify enough of the surface to trust the result:

- completed and actually read runs, exact conditions, and durable result paths;
- protocol deviations, interrupted or invalidated runs, and diagnostic-only evidence;
- evaluator, metric, parser, data, information-budget, and baseline semantics;
- uncertainty, natural support, and whether the evidence is selected, synthetic, or extreme-only.

Repair invalid evidence before drawing scientific conclusions. Preserve the prospective forecast for a registered run and state whether that forecast was supported. The forecast fixes the verdict on that run; it does not fix the explanation, next method, paper identity, or fate of the broader program.

### Make Four Coupled Updates

Every consequential result should update four different objects. Do not let one substitute for another.

**Observation.** State what happened under the exact conditions, including effect size, uncertainty, strongest matched alternative, utility costs, and inconvenient cases. Read the full outcome vector rather than one promotion metric. Treat random-seed replication according to its evidential job: one trustworthy, materially negative seed is enough to conclude that the current realization has a problem and should be inspected or redesigned; it is not enough to close the primitive. Do not request more seeds to search for a favorable outcome. Repeat only when the sign or magnitude is plausibly unresolved by stochastic variation, an execution outlier is credible, or a coherent positive realization is ready for reliability estimation.

**Explanation.** Ask what local belief became less plausible, what residual remains unexplained, and which deeper variable could compress both successes and failures. Calibrate causal language: accessibility is not use, association is not intervention, and falsifying one explanation does not prove its complement.

**Design Consequence.** Identify what the next realization should inherit, remove, separate, condition on, reroute, or represent differently. A result that reveals a new load-bearing variable belongs first to method formation, even when it also narrows a current claim. Do not convert a newly discovered design variable directly into a boundary statement. If a component helped in one regime and hurt in another, ask whether the method wrongly assumed a fixed operator where the system needs a conditional, adaptive, factorized, or jointly learned one. Cross-setting variation can be the specification of the next method, not merely evidence against generality.

**Paper Consequence.** Only after the scientific and design updates, ask what changes in the bounded paper under construction. The result may invalidate a claim, narrow scope, revise explanation, remove a component, strengthen evidence, or remain development history. Stable observations are not automatically a mature contribution, and a local method failure does not select an analysis-paper identity.

### Distinguish Run, Realization, Primitive, And Program

Locate what the evidence was actually capable of testing:

- a particular execution or configuration;
- the competence of the current realization;
- a component interaction or method primitive;
- the explanatory thesis;
- the value-bearing problem class;
- the current paper or broader program.

The earliest unsupported link in the actual method-to-value argument matters more than a named failure category. An interrupted, dormant, unfair, under-powered, or semantically mismatched run is not evidence against a primitive. A competent realization whose intended computation is active and still loses fairly is stronger evidence, but it normally updates the primitive or abstraction before it updates the value of the field.

During method formation, treat adding, removing, replacing, freezing, rerouting, or factorizing components as constructive ablation. Preserve a negative headline result while extracting the component job, interaction, positive residual, and redesign it supports. This is prospective method evolution, not retroactive success.

### Protect Against False Closure

Do not infer that a method family, contribution type, or field is exhausted from accumulated failed variants unless those variants are competent realizations of a genuinely shared causal assumption and leave no unexplained useful residual. A long lineage is not negative proof.

Do not let all possible outcomes confirm the preferred story. For any new interpretation, name evidence that would weaken it, not merely route to another publishable branch. If positive and negative outcomes are both narrated as confirmation, the interpretation is not yet discriminating.

When a simple baseline wins, make it a theory object: explain why it works, where it naturally fails, and what principle the next method should internalize. When a result varies by model, reader, dataset, scale, or system state, test whether that context is a causal input the method must model rather than a qualifier used to shrink the claim.

### Judge Whether A Paper Object Exists

Separate true observation, candidate explanation, method-development asset, and paper contribution.

A method contribution needs a natural value-bearing problem, a competent load-bearing intervention, fair strong comparisons, end-to-end value, and an honest tradeoff surface. It need not be universal, but its exact scope must still matter.

An analysis, measurement, mechanism, theory, or systems contribution is valid only when it has an independent positive object. Mentally remove the failed method lineage and ask whether the remaining object is still natural and important, non-trivial rather than mechanically induced, confirmed beyond the evidence that selected it, consequential for a scientific or operational decision, and distinct from the strongest existing account.

Do not automatically promote stable correlations, failure atlases, failed interventions, scope boundaries, or accurate abstention into a paper. Conversely, do not reject a genuinely independent analytical object merely because it emerged during method development. Judge the object on its own burden.

If the supported scope becomes very narrow, reassess value at that scope. A precise private cell cannot borrow importance from the seed. The appropriate response is often to return to the broader natural problem or raise the design abstraction, not to add more qualifiers for a cleaner local story.

### Choose The Next Action

Choose and, within user constraints, execute the action with the greatest chance of changing the thesis, method, decisive comparison, or paper viability. This may be method repair, a discriminating contrast, a stronger matched baseline, competent optimization, a higher-level primitive, confirmation of an independently valuable analytical object, or paper completion when a contribution is genuinely mature.

Do not hand the user a menu merely because a local hypothesis failed. Use the second-PI synthesis, select the strongest reversible continuation, and execute it. Ask only for decisions that change explicit scope, exceptional budget, irreversible state, locked submission identity or venue, or portfolio-level allocation.

Permanent program pausing is a portfolio decision made in `research-pipeline`, not an ordinary result interpretation. It requires rereading the original program, considering the strongest higher-level continuation, and comparing expected value with other projects. It never means the field is exhausted.

## Update The Research State

Record the useful result in the project's existing state:

```markdown
## Thesis Update
- observation:
- discovery slice:
- value-bearing problem class and natural support:
- intended method or claim population:
- local story weakened or supported:
- competing explanations:
- strongest contrary evidence:
- current central thesis:
- confidence and scope:
- method-design consequence:
- useful behavior to preserve and harmful coupling to change:
- evidence that would weaken the new explanation:
- current paper claim and effect of this result:
- why the observation is or is not yet a mature contribution:
- best next question:
- next action and why:
```

Use a separate `SIGNAL_REPORT.md` when the reasoning or evidence table is substantial. Do not create it merely because another skill expects a file.

For a **materially consequential run**, write `RESULT_TO_CLAIM.md` instead, using this compact template (otherwise update the concise live research state directly):

```markdown
# Result Interpretation

## Evidence
- completed/read evidence and exact paths:
- integrity, uncertainty, and limitations:
- registered prediction and honest run verdict:

## Observation
- full outcome vector:
- strongest matched comparison:
- representative supporting and inconvenient cases:

## Explanation
- belief weakened:
- residual pattern:
- deeper variable and competing explanations:
- evidence that would weaken this interpretation:

## Design Consequence
- maturity of the tested realization:
- component or assumption implicated:
- useful behavior to preserve:
- next realization and its unique prediction:

## Paper Consequence
- current bounded claim affected:
- what remains supported:
- claim-threatening versus non-blocking issue:
- contribution object currently earned, if any:
- why stable evidence is or is not yet a mature paper contribution:

## Next Action
- highest-value action and why:
- what it could change:
- Codex second-PI synthesis, when scientific judgment was ambiguous:
- execution started or durable next command:
```

Update the live thesis and next action in the project's authoritative research state. Preserve old run verdicts as history, never as commands.

## From Explanation To Method

When an artifact-clean value failure, a coherent explanatory model, and a plausible design locus exist, move toward `method-primitive-synthesis` or a real trainability run. Register a consequential run compactly when needed; do not wait for a contract artifact to grant permission. The purpose of diagnosis is to improve the intervention, not to remain permanently diagnostic.

If the current explanation fails, reinterpret the evidence and continue from what remains. Do not ask the user whether the field should survive a local null.
