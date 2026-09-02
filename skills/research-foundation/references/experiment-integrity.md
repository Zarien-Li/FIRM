# Experiment Integrity

Use this reference when evidence may guide a method, anchor a consequential comparison,
or support a claim. The purpose is to identify what the experiment actually measures
and whether the comparison can answer the scientific question. It is not a standing
review ceremony or a mechanism for closing a research direction.

## Information Boundary

Before the first result is allowed to choose or reshape a method, map the path from raw
example to reported metric:

- which train, development, and test records, labels, references, generated outputs,
  caches, retrieval banks, demonstrations, teacher signals, and external models enter
  each stage;
- which evidence chooses prompts, checkpoints, stopping, thresholds, slices, readers,
  variants, mechanisms, hyperparameters, and headline statistics;
- what information exists at each decision time in temporal, online, editing,
  retrieval, interactive, or stateful systems, including when mutable state changes;
- how the evaluator parses, filters, aggregates, scores, and handles missing outputs;
- which natural population and sampling frame the reported quantity represents.

Trace at least one known example through the real code path. Development evidence may
form a method, but confirmatory evidence must remain independent of the choices it is
supposed to evaluate. If the information path changes materially, reconsider the
dependent results rather than preserving them with prose.

## Statistical Unit And Population

Record the unit of analysis, independent sampling unit, repeated-measure structure,
hierarchy or clustering, inclusion rules, and weighting. Match uncertainty estimation
to the unit that actually varies independently: item-level resampling cannot replace
author, subject, graph, conversation, environment, checkpoint, or run variation when
those units carry dependence.

Keep the evaluated population fixed across a contrast unless population change is the
estimand. Label synthetic, generated, proxy, simulated, sampled, and human-evaluated
targets for what they are; none inherits the scope of the natural task merely because
its signal is clean.

## Matched Treatment

Enumerate the differences between compared systems: data exposure, labels,
supervision, tools, objective, curriculum, adaptation, optimization, compute, stopping,
candidate pool, and evaluator. A compound contrast may estimate a deployed package,
but it cannot attribute the result to one component. Use matched controls, a factorial
contrast, or a narrower claim for attribution.

Compare the decisive published incumbents under semantically matched conditions.
Internal controls explain a mechanism; they do not replace strong published baselines
or justify filling a table with convenient heuristics.

## Execution Competence

Verify that the intended code path ran, the advertised component was active, and each
model, baseline, optimizer, attacker, or relearner reached the competence needed for the
comparison. Check convergence and engagement using behavior appropriate to the system,
not merely process survival.

Keep implementation defects, non-engagement, undertraining, interruption, and
infrastructure failure separate from scientific failure. A smoke test establishes that
the path executes and can be inspected; it does not establish semantic correctness or
method effectiveness.

## Artifact Reconstruction

Recompute representative headline cells from raw outputs or sufficient statistics.
Record numerator, denominator, units, aggregation order, weighting, clipping,
normalization, missing-data behavior, and numerical tolerance. Trace consequential
results through data and split identity, config, code revision, cache, checkpoint,
randomness, stopping rule, result file, table, and figure.

When a stable baseline and evaluator have been established, preserve a compact anchor
containing their data, evaluator, population, configuration, and selection identities.
Reuse it while those semantics remain unchanged. Revisit only the dimensions touched by
a code, data, population, treatment, evaluator, or selection change, or by concrete
contrary evidence.

If an integrity problem is verified, qualify or invalidate only the affected evidence
and its dependent claims, then repair, rerun, or redesign from clean evidence. Missing
artifacts leave a claim unverified; tool failure is an execution fact. Neither outcome
by itself closes the primitive, paper opportunity, program, or field. Use the shared
evidence-lineage reference when invalidation must propagate across derived artifacts.
