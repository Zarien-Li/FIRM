---
name: research-contract
description: Lightweight registration for an expensive or claim-defining experiment. Freeze the run's configuration, forecast, comparison, interpretation, and durable paths without freezing the living thesis, method evolution, or permission to continue research.
---

# Experiment Registration

A contract is a provenance device for consequential runs, not a research constitution, stage transition, or permission gate.

The living thesis remains in the project's concise research state. Revise it when evidence changes what is plausible. Registration freezes only what a particular run was intended to test, how it was configured, and how its outcomes would be interpreted. Never rewrite that forecast after seeing the result.

The contract has authority over the provenance and honest verdict of its exact run only. It cannot prohibit a later redesign, select the permanent paper identity, or turn an agent-authored restriction into a user constraint. After the run, current evidence and the live thesis decide what to build next.

## When Registration Is Worthwhile

Register a run when it is expensive, difficult to repeat, central to a paper claim, vulnerable to configuration drift, or likely to be reinterpreted post hoc. Exploratory analysis, small debugging runs, and ordinary method iteration do not need a separate contract merely to proceed.

Before a real method campaign, the researcher should already understand the natural value-bearing failure, current causal thesis, proposed design change, strongest simple alternative, and honest evaluation path. These are scientific reasons to spend, not boxes that grant permission.

A registration may cover one constructive ablation or method-formation step rather than a finished architecture. Freeze the local component or interaction hypothesis, comparison, and forecast; do not freeze the whole evolving method. After reading the outcome, preserve that run's verdict and register the next construction prospectively if the design changes.

## What To Freeze

Record only what is needed to preserve outcome integrity:

- question and unique prediction;
- exact method and semantically matched baselines;
- data, model, split, candidate pool, prompt/protocol, evaluator, metrics, seeds, steps, stopping, and budget;
- expected result, confidence, and a genuinely surprising result;
- what positive, null, and negative outcomes would say about this run, including at least one observation that would weaken the current explanation rather than create another victory branch;
- what each outcome cannot establish about the broader method family, contribution type, or field;
- for a construction ablation, what each outcome would add, remove, replace, separate, or retain in the next method realization;
- utility, coverage, latency, cost, or general-capability checks needed for the intended claim;
- sanity and artifact controls;
- config, code revision, checkpoint, log, result, and resume paths.

If reality forces a change after launch, create a new run version and record why. Do not silently alter candidate pools, baseline settings, metrics, stopping, or denominators.

## Baseline And Claim Integrity

Do not register a strawman victory. Use current, correctly configured, semantically matched baselines. A close paper becomes a serious baseline or ownership threat; it closes the opening only when matched evidence resolves the same reproduced failure under the relevant constraints.

Separate what the run can support: phenomenon, causal explanation, method necessity, end-to-end value, and breadth. One diagnostic or one metric rarely establishes all of them. A probe, oracle, separable representation, external solver, abstention policy, or certificate is not silently promoted into deployable method success.

## After The Run

Preserve the registered verdict exactly. Then return to `research-pipeline` and `signal-analysis` to interpret what the result teaches. A missed target can motivate a prospectively registered method revision without changing the predecessor's outcome. It does not by itself terminate a method family or contribution type.

Do not carry a registration's `negative` interpretation into later sessions as a ban. Later evidence may reveal that the run tested the wrong abstraction, an immature realization, or a context variable the next method should model. Preserve that reinterpretation alongside the original verdict.

## Compact Record

Use the project's existing tracker or `docs/research_contract.md`:

```markdown
# Registered Experiment: [ID]

- living thesis at launch:
- current paper claim affected:
- question and unique prediction:
- method and strongest matched alternatives:
- models/data/splits/protocol:
- metrics and paired utility checks:
- seeds/budget/stopping:
- sanity and confound controls:
- expected / surprising result:
- interpretation if positive / null / negative:
- evidence that would weaken the current explanation:
- conclusions this run cannot support:
- config/code/checkpoint/log/result/resume paths:
- status: proposed | running | completed | interrupted | invalidated
- version changes after launch:
```

Keep the record compact. Raw results and evolving explanations belong in result artifacts and the authoritative research state, not in the registration.
