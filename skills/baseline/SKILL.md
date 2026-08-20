---
name: baseline
description: Establish trustworthy empirical contact with a field through accepted tasks, strong incumbents, simple alternatives, substrate checks, evaluator validation, and raw behavioral reading. Use when creating or repairing the evidence foundation for research.
---

# Baseline And Empirical Contact

Build a trustworthy contact point with the field, then read what the best available
systems actually do. A baseline establishes reality and ownership; it does not choose
the paper identity or close the broader program.

## Select The Evidence Surface

Name one accepted `benchmark_anchor`: a standard task, deployed workflow, or natural
population on which the field recognizes progress. Label other artifacts as:

- `claim-bearing`: can support the intended scientific claim;
- `training`: changes the learned system but is not itself evaluation evidence;
- `diagnostic`: helps explain behavior but cannot establish field value alone.

Synthetic cases, generated data, or project-defined slices may expose a mechanism.
They do not replace an accepted anchor unless the derived population has independent
field value and the broad program is deliberately re-grounded.

Choose, within realistic resources:

- a strong reproducible direct incumbent;
- a serious simple, deterministic, or procedural alternative;
- implementations whose semantics and raw outputs can be inspected.

Do not create headroom with an obsolete, weak, or mismatched comparator. Record any
resource-driven substitution and the uncertainty it leaves.

## Resolve The Nearest Rival Early

Before naming or deeply implementing a method, identify the two or three closest
same-locus approaches. Read the closest paper and implementation and state how that
rival might already absorb the proposed principle.

Exploration may begin while a difficult rival is being reproduced, but novelty and
paper identity remain provisional. Before dependent refinement, compare against the
claim-threatening rival under matched conditions, or establish from primary sources
why it is not semantically comparable.

The purpose is ownership clarity, not ceremonial baseline completion. Prioritize the
rival most able to erase the contribution.

## Verify Substrate Competence

Confirm that the underlying model, adapter, retriever, simulator, or execution system
can competently perform the standard task without the proposed primitive. The base
system must leave an interpretable residual.

If it cannot perform the task, mark the comparison `substrate-confounded` and repair
the substrate first. Do not simultaneously change backbone ability, data treatment,
and the proposed mechanism, then attribute the package difference to the mechanism.

## Reproduce Semantics

Match the parts that can change the conclusion:

- dataset, split, preprocessing, population, candidate pool, and exclusions;
- checkpoint, prompt, decoding, stopping, tools, and mutable state;
- objective, labels, supervision, external computation, and training treatment;
- evaluator, parser, metric direction, aggregation, missing-data rule, and units;
- compute or optimization differences material to fairness.

Independently reconstruct representative headline metrics from raw outputs or
sufficient statistics. Run a small known success and failure through the entire path
when possible. A smoke test proves execution, not semantic equivalence.

Wrong paths, fallback data, parser errors, leakage, circular targets, changed
populations, checkpoint mismatch, and asymmetric protocols are integrity failures.
Invalidate affected conclusions and propagate the invalidation through dependent
claims. Use `../shared-references/experiment-integrity.md` and
`../shared-references/evidence-lineage.md` for the detailed checks.

## Read Behavior, Not Only Scores

Inspect representative:

- natural failures and matched successes;
- disagreements among serious systems;
- cases that contradict the preferred explanation;
- boundary cases, abstentions, crashes, truncations, tool traces, latency, and cost.

A headline reproduction is not empirical contact until the residual behavior is read.
Look for failure structure that is natural, consequential, and shared across systems
people use. Treat a clean rare slice as a microscope, not automatically as the
research destination.

## Add Coverage For A Question

Add another model, dataset, regime, or seed only when it resolves a named uncertainty,
for example:

- shared phenomenon versus implementation artifact;
- sufficiency of a simple alternative;
- realistic transfer or scale behavior;
- utility, coverage, latency, or cost tradeoff;
- claim scope that exceeds current evidence.

A competent bad seed first triggers implementation, optimization, and hypothesis
diagnosis. Do not launch a seed sweep to rescue a realization whose sign is already
clear. Conversely, do not generalize one failed realization into closure of a method
family or broad program.

## Record Provenance And Health

Prefer official or mature implementations. Record source, version or commit,
checkpoint, environment, local modifications, and why stronger alternatives were not
usable. Classify a key anchor as:

- `healthy`: intended path and trustworthy semantics;
- `unresolved`: claim-threatening but not yet trustworthy enough to compare;
- `fragile`: runnable with a material open risk;
- `invalid`: corrupted, incomplete, or incomparable;
- `comparison-weak`: too weak or semantically different;
- `substrate-confounded`: base capability is inadequate.

Only healthy anchors carry headline comparisons. Fragile runs may guide repair but do
not support bottleneck claims or method maturity.

## Durable Output

Update an existing baseline record or create `BASELINE_REPRO.md` when coordination
needs one. Keep it compact:

```markdown
# Baseline Evidence

## Accepted Surface
- anchor, population, split, metrics, information and training treatment:

## Systems
| System | Source/version | Actual protocol | Health | Result path |

## Ownership And Competence
- nearest rivals and closest matched evidence:
- remaining ownership threat:
- substrate competence result:

## Integrity
- evaluator/metric reconstruction:
- provenance, deviations, and invalidations:

## Behavioral Contact
- natural failures, successes, disagreements, inconvenient cases:
- observation bundle and unresolved uncertainty:
```

Return validated observations to the current research episode. Interpretation belongs
to `signal-analysis`; construction belongs to `method-primitive-synthesis`; paper
identity belongs to the later paper-formation stage.
