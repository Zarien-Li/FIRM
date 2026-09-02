---
name: baseline
description: Establish trustworthy empirical contact with a field through accepted tasks, recent published methods, strong incumbents, substrate checks, evaluator validation, and raw behavioral reading. Use when creating or repairing the evidence foundation for research.
---

# Baseline And Empirical Contact

Build a trustworthy contact point with the field, then read what the best available
systems actually do. A baseline establishes reality and ownership; it does not choose
the paper identity or close the broader program.

## Baseline Means A Published Field Method

Use comparison names precisely:

- A **backbone or substrate control** is an unmodified Qwen, Llama, CLIP, diffusion
  model, retriever, simulator, or other foundation system. It establishes that the
  underlying system can perform the task and leaves interpretable residual headroom.
  It is not a field-method baseline unless the research claim is specifically about
  choosing foundation models.
- A **matched control or ablation** isolates the project's treatment, component, or
  training change. It supports attribution. It is not a field-method baseline.
- A **baseline** is a named method or system proposed in the relevant research
  literature, with its paper, venue/year, method semantics, implementation, and
  evaluation protocol identified. The decisive set includes a strong reproducible
  recent incumbent, the strongest published method performing the same operational job
  under a comparable deployment contract, and the nearest mechanistic or same-locus
  rival when it differs.

When the user asks to “run the baseline,” interpret this as reproducing methods from
recent field papers, not merely evaluating raw Qwen/Llama checkpoints. Recent means
the current frontier and relevant preceding publication cycles, while retaining an
older method when it remains a recognized incumbent. Select by claim and field use,
not by a fixed paper count.

Do not invent project-specific heuristics to pad the comparison table. A simple method
belongs only when it is already a recognized published or field-standard comparator
for the accepted protocol. Empirical contact is not complete when only backbones,
prompts, or internal controls have run. Before reporting `baseline reproduced` or
optimizing a proposed method, reproduce at least one strong recent published method
and identify the nearest serious published rival, or record the concrete reproduction
blocker and keep method claims provisional.

## Give Baselines Three Different Jobs

Do not wait for one giant comparison matrix, and do not let one early incumbent stand
for the eventual paper. Maintain three claim-dependent envelopes:

- **Empirical contact set:** before locking the problem or method, reproduce a competent
  recent incumbent on the accepted surface, inspect raw behavior, and identify the
  closest operational and mechanistic neighbors.
- **Candidate-judgment set:** before paper-sized optimization, fairly compare the
  realized method with the strongest functional rival and nearest mechanistic rival
  that could erase its value or novelty, plus the matched attribution control.
- **Submission envelope:** for a candidate worth focused maturation, cover the published methods,
  accepted surfaces, model regimes, reliability, and efficiency evidence expected by
  the actual bounded claim and target community.

These are responsibilities, not fixed paper counts or stages. A method may be explored
while an expensive comparator is being repaired, but the PI's candidate argument must
acknowledge incomplete or semantically weak rival evidence. Do not run the submission
envelope before an informative candidate exists merely to manufacture apparent maturity.

## Select The Evidence Surface

Name one accepted `benchmark_anchor`: a standard task, deployed workflow, or natural
population on which the field recognizes progress. Label other artifacts as:

- `claim-bearing`: can support the intended scientific claim;
- `training`: changes the learned system but is not itself evaluation evidence;
- `diagnostic`: helps explain behavior but cannot establish field value alone.

Synthetic cases, generated data, or project-defined slices may expose a mechanism.
They do not replace an accepted anchor unless the derived population has independent
field value and the broad program is deliberately re-grounded.

Confirm **surface fidelity** before drawing a problem conclusion: representative
examples in the accepted population must actually instantiate the canonical object,
and the primary outcome must be capable of changing when that object improves. A short
clip cannot establish a long-event problem; an aggregate score insensitive to the
target behavior cannot carry its value; a hand-selected clean region cannot stand in
for the full deployment population. Such evidence is still useful, but label it
diagnostic and return to an accepted surface before method identity or paper entry.

Confirm **deployment availability** at the same time. List the information used by an
incumbent, diagnostic, and proposed intervention, and ask whether each signal exists at
the moment the deployed system must act. Oracle regions, gold boundaries, hidden
labels, future context, privileged annotations, and clean subsets may locate headroom;
they do not establish a deployable opening. Before method formation, either realize the
principle from available inputs on the canonical object or keep it as an unresolved
diagnostic opportunity.

Before the first result guides method choice, use
`../shared-references/experiment-integrity.md` to record the train/development/test,
temporal, cache, target, external-signal, and checkpoint-selection flow in the run plan.

Choose, within realistic resources:

- a strong reproducible published method incumbent from recent relevant literature;
- the strongest functional rival and nearest mechanistic rival required by the claim;
- the backbone/substrate control needed to establish base competence;
- implementations whose semantics and raw outputs can be inspected.

Do not create headroom with an obsolete, weak, or mismatched comparator. Record any
resource-driven substitution and the uncertainty it leaves.

## Resolve The Nearest Rival Early

Before naming or deeply implementing a method, identify the two or three closest
approaches by operational effect and by mechanism. Read the closest papers and
implementations and state how either rival might already absorb the proposed principle
or erase its practical value. Repeat this step when the method's actual job or
deployment contract materially changes; seed-era neighbors do not certify a new
scientific identity.

Exploration may begin while a difficult rival is being reproduced, but novelty and
paper identity remain provisional. Before dependent refinement, compare against the
claim-threatening rival under matched conditions, or establish from primary sources
why it is not semantically comparable.

If the local reproduction remains materially below the paper's result under the same
accepted protocol, do not declare the lower number a frozen incumbent after a local
sweep. Reconcile checkpoint, data, evaluator, optimization, and reporting semantics or
mark the anchor unresolved. An unresolved anchor can guide engineering, but it cannot
establish method superiority or mature the paper.

The purpose is ownership clarity, not ceremonial baseline completion. Prioritize the
rival most able to erase the contribution.

## Verify Substrate Competence

Confirm that the underlying model, adapter, retriever, simulator, or execution system
can competently perform the standard task without the proposed primitive. The base
system must leave an interpretable residual.

If it cannot perform the task, mark the comparison `substrate-confounded` and repair
the substrate first. Do not simultaneously change backbone ability, data treatment,
and the proposed mechanism, then attribute the package difference to the mechanism.
Passing this check establishes substrate competence, not baseline reproduction.

## Preserve Seed-Regime Fidelity

Substrate competence is not enough when the seed targets a particular model scale,
context length, training regime, modality, data distribution, or deployment boundary.
For claim-bearing discovery, record the intended regime and the regime actually run.
Reproduce the incumbent's motivating positive behavior on the intended regime before
building a method around its residual failure. A cheap proxy is useful only when direct
evidence shows that it preserves the phenomenon, rival ordering, and intervention
opportunity.

If a published method helps at the seed's scale but loses on a much smaller local model,
the local loss is a proxy-regime result. It does not license a project devoted to fixing
that small-model artifact. Either return to the intended substrate or first establish a
scientifically valuable small-regime problem with its own accepted surface and rivals.

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
- whether a recognized published comparator already explains the effect;
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
| System | Role | Paper/venue/year | Source/version | Actual protocol | Health | Result path |

## Ownership And Competence
- nearest rivals and closest matched evidence:
- remaining ownership threat:
- substrate competence result:
- intended seed regime, actual regime, and incumbent-effect fidelity:

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
