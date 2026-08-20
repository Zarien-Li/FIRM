---
name: research-contract
description: Prospectively register an expensive or claim-defining experiment so its configuration, forecast, interpretation, and durable paths cannot drift after results. It protects one run; it never licenses or terminates research.
---

# Experiment Registration

Register consequential runs for provenance and honest interpretation. The contract
freezes one run, not the living program, paper identity, method family, or permission
to continue.

## When To Register

Use a contract when a run is expensive, hard to repeat, claim-defining, vulnerable to
configuration drift, or likely to be reinterpreted post hoc. Ordinary debugging,
small probes, and early construction iterations may use the existing tracker.

Before launch, ensure the intended comparison is meaningful: the anchor and evaluator
are healthy enough, the substrate is competent, the population and metric carry the
question, and the run can preserve semantic comparability. If not, register it as
debugging or repair rather than claim evidence.

## Freeze The Run

Record:

- question and unique prediction;
- exact construction and semantically matched alternatives;
- data, population, model, split, prompt/protocol, evaluator, metrics, seeds, steps,
  stopping, and resource budget;
- expected result, genuinely surprising result, and confidence;
- what positive, null, and negative outcomes say about this run;
- what no outcome can establish about the broader method, program, or contribution;
- component and paired utility comparisons belonging to the evidence bundle;
- sanity checks whose failure invalidates the run;
- config, code revision, checkpoint, log, result, and resume paths.

For a construction arc, register the local prediction of the current version. Do not
pretend it is already the final method. Numeric thresholds must reflect attainable
headroom, metric resolution, and variance; they describe this run, not an automatic
kill, promotion, or paper-entry rule.

After launch, never silently change candidates, data, denominator, metric, stopping,
or success definition. Version the registration and record why reality forced a
change.

## Read The Outcome Honestly

Preserve the prospective verdict exactly. Then let `signal-analysis` interpret the
result inside the full evidence bundle. A missed prediction may reveal an implementation
defect, immature realization, wrong mechanism, or poor problem choice. It does not
retroactively change the forecast and does not by itself close a family or field.

## Compact Record

Use the project tracker or `docs/research_contract.md`:

```markdown
# Registered Experiment: [ID]
- question and unique prediction:
- construction and matched alternatives:
- model/data/population/protocol/evaluator:
- metrics, component comparison, and utility check:
- seeds/steps/stopping/budget:
- sanity and invalidation controls:
- expected / surprising outcome:
- interpretation if positive / null / negative:
- conclusions no outcome can support:
- config/code/checkpoint/log/result/resume paths:
- status: proposed | running | completed | interrupted | invalidated
- version changes after launch:
```

Keep raw results and evolving explanation outside the contract. Registration is not a
stage gate and cannot become a historical ban in a later session.
