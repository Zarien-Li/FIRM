# Experiment Validity Protocol

## Purpose

Determine whether an experiment identifies the scientific quantity that a claim
requires. This is a validity review, not a fraud hunt and not a daily permission
gate. Honest bugs, ambiguous estimands, weak treatment contrasts, and provenance
mistakes are handled by repairing evidence, not by assigning intent.

Use this protocol when an evaluator or baseline first becomes a claim-bearing
anchor, when its semantics or code change, when a result is about to carry a
consequential claim, or when concrete evidence raises a validity concern.

## Eight Validity Dimensions

### 1. Data And Target Semantics

- Verify the dataset, labels, task unit, candidate set, inclusion/exclusion rules,
  preprocessing, and ground-truth provenance.
- Label synthetic, generated, proxy, simulated, and human-evaluated targets
  explicitly. A proxy supports only the quantity it actually measures.
- Check duplicates, circular target construction, fallback rows, truncation, and
  filtering that changes the evaluated population.

### 2. Evaluator And Information Semantics

- Trace the exact prediction position, parser, scoring direction, filtering,
  aggregation, and missing-data behavior from raw input to reported value.
- Verify what information is available at prediction time. For temporal, online,
  interactive, retrieval, or stateful systems, inspect event ordering and state
  mutation rather than assuming a split name guarantees causality.
- Check that current or future labels, events, answers, caches, reciprocal records,
  generated references, or baseline outputs cannot enter the prediction path unless
  the claimed setting explicitly permits them.

### 3. Selection Independence

- Identify every use of train, validation, development, and test data.
- Test data may not choose checkpoints, epochs, stopping, thresholds, slices,
  prompts, readers, method variants, mechanisms, or headline statistics.
- Development evidence may form a method. A claim-level estimate must use evidence
  appropriate to the claim and fresh from the choices it is supposed to evaluate.

### 4. Population And Statistical Unit

- Record the sampling frame, natural population, inclusion/exclusion, weighting,
  unit of analysis, repeated-measure structure, and hierarchy or clusters.
- Match uncertainty estimation to the independent sampling unit. Item-level
  resampling cannot stand in for author, subject, graph, conversation, environment,
  checkpoint, or run variation when those units carry dependence.
- Keep the evaluated population fixed across a contrast unless population change is
  the explicit estimand.

### 5. Treatment Identification And Fairness

- Enumerate every difference between compared systems: data exposure, labels,
  supervision, tools, objective, curriculum, adaptation, optimization, compute,
  stopping, candidate pool, and evaluator.
- A compound contrast may measure a deployment package, but it cannot identify one
  component without a matched control, factorial contrast, or appropriately narrow
  claim.
- Compare the decisive published incumbents and claim-threatening methods under
  semantically matched conditions. Use internal matched controls for attribution;
  do not invent heuristics merely to enlarge the table.

### 6. Execution Competence And Engagement

- Verify that the intended code path ran, the advertised component was active, and
  the model, baseline, attacker, relearner, or optimizer reached the competence
  required by the comparison.
- Distinguish non-engagement, non-convergence, interruption, infrastructure failure,
  and implementation defects from scientific failure.
- A smoke test proves execution and inspectability, not semantic correctness or
  method effectiveness.

### 7. Metric And Artifact Reconstruction

- Recompute representative headline cells from raw outputs or sufficient statistics.
- Record numerator, denominator, units, aggregation order, weighting, clipping,
  normalization, missing-data rule, and tolerance.
- Trace each claim through config, code revision, split, cache, checkpoint, seed,
  stopping rule, result file, table, and figure. Missing or mixed provenance blocks
  the affected claim.

### 8. Selection Provenance And Confirmation

- State whether thresholds, slices, variables, protocol pairs, cohorts, metrics, and
  headline relations were specified before or selected after observing the data.
- Exploration is legitimate. A result selected during exploration must be described
  as discovery evidence and confirmed by an appropriate fresh contrast, prediction,
  intervention, or held-out analysis before carrying a confirmatory headline.
- Check multiplicity and researcher degrees of freedom at the level needed by the
  actual claim rather than applying a ritual correction to every exploratory probe.

## Validated Foundation Anchor

After a baseline and evaluator pass the relevant checks, record one compact anchor:

```yaml
foundation_anchor:
  data_split_hash: <hash>
  evaluator_hash: <hash>
  population_spec_hash: <hash>
  baseline_config_hash: <hash>
  selection_rule_hash: <hash>
  validated_at: <timestamp>
  validity_scope: <what this anchor permits>
```

Reuse the anchor while these semantics and hashes remain unchanged. Do not rerun a
full integrity audit for every seed or ablation. Reopen only dimensions affected by
a code, data, population, treatment, evaluator, or selection change, or by new
contrary evidence.

## Independent Review And Lead-Researcher Synthesis

For high-blast-radius claim-bearing evaluation code, an independent model family may
inspect the exact code and artifacts when this can expose executor blind spots. This
is optional verification, not a universal gate, and does not make the reviewer an
authority over raw evidence.

The reviewer must report exact file and line evidence. The lead researcher then
reproduces or directly verifies each material finding, classifies it as
evidence-invalidating, method-design-changing, claim-narrowing, or deferrable, and
updates the authoritative state. Unsupported reviewer assertions remain concerns,
not scientific facts.

## Verdict And Propagation

- `PASS`: the audited evidence may support claims within the stated validity scope.
- `WARN`: preserve the exact limitation; qualify the claim or repair the affected
  dimension before making a stronger claim.
- `FAIL`: set the affected evidence to `invalidated`; remove it from active claims;
  and propagate invalidation to dependent checkpoints, analyses, tables, figures,
  drafts, and handoffs. A footnote cannot preserve a claim whose evidence is invalid.
- `BLOCKED`: required artifacts are unreadable or missing; the evidence remains
  provisional and cannot carry the claim.
- `ERROR`: reviewer or tooling failed; this is infrastructure, not PASS or FAIL.

Invalidation blocks only the affected evidence and dependent claim. It does not close
the method primitive, paper opportunity, research program, or field. Repair, rerun,
or redesign using clean evidence.

For claim-bearing evidence dependencies and transitive invalidation, follow
`evidence-lineage.md`.
