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

A selected project should be recognizable to an active research community without
being either an entire field or a private cell. Prefer a canonical input-to-output or
training object such as instruction-guided image editing, latent reasoning, KV-cache
compression, or synthetic-data selection. Reject umbrellas that jointly contain
several independent systems or outcomes, and reject projects already defined by a
specific proposed module.

Choose projects whose best-case result could change a community decision, replace a
consequential default assumption with a simple reusable primitive, and remain useful
across model generations. Citation reach, timeliness, feasibility, and differentiation
are reasons for selection, not numerical gates.

For every selected arena establish from sources:

- one canonical object and one primary outcome;
- an accepted natural benchmark or workflow whose population actually instantiates
  that object and whose metric can register its value;
- one named strong recent published-method incumbent and the nearest claim-threatening
  published rival, separately from raw backbones and attribution controls;
- the information available when a deployed method must act;
- a first empirical contact that reproduces methods and reads raw natural behavior,
  without presupposing the failure or solution;
- a realistic compute and data envelope; and
- explicit neighboring work that is outside this project.

All projects must use existing public tasks, released labels, automatic evaluation,
or naturally available system evidence. Do not select a direction whose central
contribution or valid evaluation requires building a new benchmark or collecting new
human judgments.

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

## Compact Invocation

The normal user-facing prompt should stay short:

```text
Read the active frontier-direction-discovery skill and its PROJECT_GENERATION.md.
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
