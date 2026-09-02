# Project Generation From A Sparse Brief

This is the single contract for turning a short portfolio request into project
directories. It replaces prompts that ask an agent to read every research skill and
invent dozens of fields at once.

## What The User Supplies

Only require:

- target venue or journal;
- one or more broad directions;
- maximum number of projects;
- compute envelope;
- data, annotation, modality, or contribution exclusions that genuinely matter.

Two exclusions are already global and must not be requested again: no new benchmark
construction and no new human annotation, preference, rating, or judgment collection.
Every generated project inherits them automatically.

An adequate request can be one sentence:

> Generate up to five ICLR projects in image editing, each feasible within four A100s;
> prefer lightweight adaptation over foundation-model pretraining.

The generation action owns the remaining research. Do not ask the user to name the
failure, benchmark, baseline, mechanism, or method.

## Research Before Selection

Use web research because venue scope and the frontier change. Prefer primary sources:
the official venue scope, recent accepted papers, official project pages and code,
benchmark documentation, and model releases. Record direct URLs in the manifest.

Read enough complete papers to understand the canonical task, current load-bearing
methods, evaluation protocol, compute scale, and unresolved shared design pressure.
Do not generate projects from titles, limitation snippets, survey taxonomies, or trend
lists alone.

Inspect the existing portfolio's `PROGRAM_ORIGIN.md` and `PROJECT_IDENTITY.json` files.
Reject duplicates that change only a model, dataset, metric, threshold, layer, or
candidate operator.

## Select Mesoscopic Research Arenas

Apply [frontier-direction-discovery.md](frontier-direction-discovery.md) rather than
duplicating its value and scale criteria. For generation, additionally reject portfolio
duplicates and require enough primary evidence to name the canonical object and outcome,
accepted public task or natural workflow, recent published-method incumbent, nearest
claim-threatening rival, deployment information boundary, realistic compute envelope,
neighboring exclusions, and a first contact that reads natural behavior without
presupposing the failure or solution.

Every selected project uses existing public tasks, released labels, automatic
evaluation, or naturally available system evidence. Do not select an arena whose
central contribution requires a new benchmark or new human judgments.

If a published method lacks usable code, record the concrete feasibility risk instead
of replacing it with a weak heuristic. If the canonical behavior is not visible at the
available scale, do not shrink it into an easy proxy and call that the project.

## Output Contract

Write one JSON object matching
[`project-generation.schema.json`](project-generation.schema.json). The `projects`
array contains only selected projects, ranked by expected scientific value. The
requested count is a maximum. Every factual frontier statement and baseline identity
must point to a primary source.

The manifest records the interpretation behind selection, but its lens remains
non-binding. The deterministic renderer creates authority, state, contract, and start
prompt files; it must not invent missing scientific fields.

The start prompt is a project-specific research commission, not a generic slogan and
not an executable research plan. It should explain this project's community prize,
canonical object, deployment boundary, current published-method map, non-binding lens,
and suggested empirical contact in enough detail for the PI to understand why the
project exists. Those details must be framed as a researched launch map that the PI may
reorder or revise when new evidence warrants it. Do not turn the named surface,
incumbents, first contact, `v1 -> v2`, contribution type, or paper route into mandatory
steps. The prompt transfers scientific ownership; the skills supply capabilities; the
project PI decides the research route.

Neither the manifest nor rendered files may state that the project continues only if
the non-binding lens or first empirical contact succeeds. Do not create durable
thresholds, transfer quotas, dataset-count requirements, or stop language. A gate may
describe one experiment's interpretable population, but it cannot authorize the
research program or prevent evidence-directed repair of a method-owned construction.

## Compact Invocation

The normal user-facing prompt should stay short:

```text
Read the active research-foundation skill and its project-generation.md reference.
Create a project-generation manifest from this brief, using current web research and
primary sources. Validate it against project-generation.schema.json, but do not render
folders yet.

Venue: <venue>
Broad direction: <direction>
Maximum projects: <count>
Compute: <budget>
Exclusions: <constraints>
Existing portfolio: <path>
Output manifest: <path>
```

After the user has inspected the concise ranked selection, render it with:

```bash
node scripts/generate_seed_project_folders.mjs <manifest.json> <new-output-root>
```

Rendering is the explicit acceptance action. The renderer refuses to overwrite an
existing root or to repair incomplete scientific fields.
