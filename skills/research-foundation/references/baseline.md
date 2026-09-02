---
name: baseline
description: Establish trustworthy empirical contact through accepted tasks, recent published methods, substrate competence, evaluator validation, and raw behavior. Use before method claims or when the empirical foundation is uncertain.
---

# Baseline And Empirical Contact

Build a trustworthy contact point with the field, then read what serious systems do.
Baseline evidence establishes reality and ownership; it does not choose the paper
identity or close the program.

## Name Comparators Precisely

- A **published-method baseline** is a named method or system from the relevant
  literature with its paper, venue/year, operational semantics, implementation, and
  evaluation protocol identified.
- A **backbone or substrate control** is an unmodified foundation model, retriever,
  simulator, or execution system used to establish base competence and residual
  headroom.
- A **matched control or ablation** isolates the project's treatment, component, or
  training change for attribution.

When asked to run “the baseline,” reproduce methods proposed in recent field papers,
not merely raw Qwen, Llama, CLIP, diffusion, or analogous checkpoints. Retain an older
method when it remains a recognized incumbent. Do not invent weak project-specific
heuristics to fill the table; a simple method belongs when it is a recognized published
or field-standard comparator for the accepted protocol.

Before reporting field contact or optimizing a proposed method, reproduce at least one
strong recent published method and identify the strongest functional and nearest
mechanistic rivals, or record the concrete blocker and keep method claims provisional.

## Give Baselines Different Scientific Jobs

The comparison set grows with the decision, not with a fixed paper count:

- **field contact:** one competent recent incumbent on the accepted surface, raw
  behavior, and the closest operational and mechanistic neighbors;
- **candidate judgment:** the realized method against the strongest functional rival,
  nearest mechanistic rival, and matched attribution control that could erase its value
  or novelty;
- **submission claim:** the bounded published methods, accepted surfaces, model regimes,
  reliability, and efficiency evidence owed by the actual claim.

Exploratory construction may proceed while an expensive comparator is being repaired,
but the PI must keep ownership and maturity provisional. Do not run a full submission
matrix before an informative candidate exists merely to manufacture progress.

## Establish An Accepted And Deployable Surface

Name one `benchmark_anchor`: a standard task, deployed workflow, or natural population
on which the field recognizes progress. Label other evidence as claim-bearing, training,
or diagnostic. Synthetic cases, generated data, or project-defined slices can expose a
mechanism but do not replace the anchor without independent field value and deliberate
program re-grounding.

Confirm that representative examples actually instantiate the canonical object and the
primary outcome can register its improvement. A truncated task, insensitive aggregate
metric, or hand-selected clean region may be useful diagnostically but cannot carry the
problem or paper identity.

Also list what information each system uses at the moment a deployed decision must be
made. Oracle regions, gold boundaries, hidden labels, future context, privileged
annotations, and clean subsets can locate headroom; they do not establish a deployable
opening. Before method formation, realize the principle from available inputs or retain
it as an unresolved diagnostic opportunity.

## Verify Substrate And Regime Competence

Confirm that the underlying model and execution path competently perform the standard
task without the proposed primitive. If not, mark the evidence `substrate-confounded`
and repair the substrate before attributing a package difference to the method.

Record the intended and actual model scale, context length, training regime, modality,
distribution, and deployment boundary. Reproduce the incumbent's motivating positive
behavior in the intended regime before building around its residual failure. A cheaper
proxy is claim-bearing only when evidence shows that it preserves the phenomenon, rival
ordering, and intervention opportunity. A proxy-specific failure does not redefine the
project without its own accepted value and rivals.

## Reproduce Semantics And Resolve Rivals

Match the protocol elements capable of changing the conclusion: data and split,
population and candidate pool, checkpoint and decoding, tools and mutable state,
objective and supervision, external computation, evaluator and parser, metric direction
and aggregation, missing-data policy, and materially different optimization or compute.

Independently reconstruct representative headline metrics from raw outputs or sufficient
statistics. Run a known success and failure through the complete path when possible. A
smoke test proves execution, not semantic equivalence. Use the shared integrity and
evidence-lineage references for a concrete information-flow risk or invalidation.

Before novelty lock, identify the two or three closest approaches by operational effect
and mechanism. Ask whether they absorb the proposed principle or erase its practical
value. Repeat when the method's actual job or deployment contract changes. If a local
reproduction remains materially below the paper under the same protocol, reconcile the
checkpoint, data, evaluator, optimization, and reporting semantics or keep the anchor
unresolved; do not freeze the weaker number as the incumbent.

## Read Behavior, Not Only Scores

Inspect natural failures and matched successes, disagreements among serious systems,
cases contradicting the preferred explanation, boundary behavior, abstentions, crashes,
truncation, tool traces, latency, and cost. A headline metric is not empirical contact
until its residual behavior has been read. Treat a clean rare slice as a microscope, not
automatically as the research destination.

Add another model, dataset, regime, or seed only to resolve a named uncertainty about
shared behavior, implementation artifacts, recognized comparators, transfer, scale,
utility, or claim scope. A competent bad seed triggers diagnosis before expansion; it
does not close the method family or broad program.

## Record Provenance And Health

Record source, version or commit, checkpoint, environment, local changes, and why a
stronger implementation was unavailable. Use factual health labels when helpful:

- `healthy`: intended path and trustworthy semantics;
- `unresolved`: important but not yet comparable;
- `fragile`: runnable with a material open risk;
- `invalid`: corrupted, incomplete, or incomparable;
- `comparison-weak`: too weak or semantically different;
- `substrate-confounded`: base capability is inadequate.

These labels describe evidence; they do not make scientific decisions. Only healthy
anchors carry headline comparisons.

## Durable Output

Create or update `BASELINE_REPRO.md` only when coordination needs it:

```markdown
# Baseline Evidence
## Accepted Surface
- anchor, population, split, metrics, information and training treatment:
## Systems
| System | Role | Paper | Source/version | Actual protocol | Health | Result path |
## Ownership And Competence
- closest rivals, substrate result, intended and actual regime:
## Integrity
- metric reconstruction, deviations, and invalidations:
## Behavioral Contact
- failures, successes, disagreements, contrary cases, and unresolved uncertainty:
```

Return validated observations to the current project state. `method-development` owns
their interpretation and any subsequent construction.
