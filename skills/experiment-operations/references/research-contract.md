# Experiment Registration

Use prospective registration when a run is expensive, hard to repeat, claim-defining,
vulnerable to configuration drift, or likely to be reinterpreted after seeing results.
Debugging, smoke tests, and early construction may use the ordinary run record.

Registration freezes the scientific meaning of one run. It does not freeze the living
program, method family, paper identity, or permission to redesign.

## Register Before Launch

First establish that the substrate and evaluator are healthy enough and that the
population, metric, anchor, and comparison can answer the intended question. Otherwise
label the run as debugging or repair rather than claim evidence.

Record in the project tracker or `docs/research_contract.md`:

- question and unique prediction;
- current construction and semantically matched alternatives;
- model, data, population, split, treatment, evaluator, metrics, seeds, stopping, and
  authorized budget;
- expected and genuinely surprising outcomes;
- what positive, null, and negative results would teach about this run;
- conclusions that no outcome can establish about the broader method or program;
- component, utility, and sanity comparisons required by the evidence bundle;
- code/config/checkpoint identity and the canonical run ID from `run-experiment`.

Choose numeric expectations from attainable headroom, metric resolution, and known
variance. They are forecasts for interpretation, not automatic kill, promotion, or
paper-entry thresholds.

After launch, do not silently change the candidate, data, denominator, metric,
stopping, or success definition. Version a forced change and explain it; use a new run
record when it changes semantic identity.

## Preserve The Forecast

After completion, preserve the prospective forecast unchanged and pass the artifact
bundle to `method-development`. A missed prediction may expose a defect, immature
realization, wrong mechanism, or poor problem choice; it neither rewrites the forecast
nor closes a method family by itself.

Keep evolving explanations and raw results outside the registration. The canonical
execution paths, attempts, completion evidence, and resource facts belong to the run
record defined in [run-experiment.md](run-experiment.md).
