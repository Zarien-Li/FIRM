# Project Generation From A Sparse Brief

This is the single contract for turning a short portfolio request into project
directories. The generator turns a broad direction into a research question worth
owning and an initial idea worth trying; the renderer only packages that judgment.
A field with a benchmark and a feasible experiment is an opportunity to investigate,
not yet a seed. A precise question without a plausible way to tackle it is still
a research lead, not a project ready to launch.

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

## Find The Question In The Work

Use web research because venue scope and the frontier change. Prefer primary sources:
the official venue scope, recent accepted papers, official project pages and code,
benchmark documentation, and model releases. Record direct URLs in the manifest.

Start with a real task, training process, or workflow that researchers already care
about. Read strong methods through their implementation, evidence, and assumptions:
what they actually do, why that works in ordinary cases, and what their headline
results leave indistinguishable. Use available predictions, cases, tables, traces,
or code to trace a concrete observation to a consequential open question. Where
the observation cannot yet be verified, label it a lead and say what existing
evidence would resolve it; do not promote a limitation paragraph or a plausible
failure story to a fact.

A useful seed makes a distinction that changes a research choice. For example, an
audio-visual model may reject an unrelated audio track yet fail to tell which of
two visible actions made a plausible sound. The question is whether the system can
use evidence about a particular event, not whether it can score higher on a larger
collection of audio-visual tests. That question leaves open whether the missing
distinction is in the data, the supervision, the input path, the readout, or even the
evaluation. It does not prescribe a fusion module. Likewise, a drop after tuning a
vision encoder does not tell us whether useful information was lost or became
inaccessible to the reader. The two answers change what is worth adapting; neither
requires declaring a winner before looking at the evidence.

Write the motivation as a short argument a researcher could tell a colleague:
what makes the incumbent surprisingly good, what it still cannot tell us or do
reliably, and why resolving that gap would matter on the original task. For a
mechanistic question, the gap can be between what a trained system appears to do
and how it acquired or uses that computation; it need not be a low score. Name the
question in plain language before optimizing its title, venue pitch, or manifest.
Keep the research question specific but the answer open.

## Form An Initial Idea

Turn the distinction into a tentative design principle. Explain in ordinary prose
what the research could do differently from the strongest relevant method and why
that change might help in the cases that motivated the question. For example, if
coarse audio-visual synchrony lets a model answer without identifying the source
action, a starting idea is to make learning or inference depend on correspondence
between particular events, rather than rewarding clip-level agreement alone. That
suggests a real change without deciding whether to realize it in the examples, the
training signal, or the model's computation.

The initial idea is not a claim that the cause is known, nor a commitment to a named
module, formula, or recipe. A good seed gives the PI something to reason about and
try, not something to defend. If it fails, the PI can replace it while keeping the
original question. Saying "reproduce baselines, then find a method" does not supply
an idea; when no plausible idea survives the closest work, keep investigating
instead of rendering a project.

Inspect the existing portfolio's `PROGRAM_ORIGIN.md` and `PROJECT_IDENTITY.json` files.
Compare the decisions the proposed projects would change, not their names. If two
would use substantially the same evidence to resolve the same uncertainty, combine
them as lines of inquiry rather than creating two projects. A different model, venue,
or initial operator does not give a question a new identity.

## Select Mesoscopic Research Arenas

Apply [frontier-direction-discovery.md](frontier-direction-discovery.md) for value
and scale. Fit the question to a public task or natural workflow where strong
published methods and usable implementations make the distinction observable.
The nearest rival matters because it may already resolve that distinction or
explain away the apparent opportunity. Start from the strongest faithful existing
code path that can expose it; neither a complete baseline matrix nor a new harness
can supply a missing reason to do the project.

Let the first empirical contact follow from the question. It might compare existing
outputs on matched natural examples or inspect how a strong method makes the
relevant decision. If those facts already give an informative intervention, the
PI can build it without a separate premise experiment. Do not prescribe a fixed
method, cause, or sequence. If the available record supports only a field and a
generic ambition, return it as a direction to investigate, not a generated project.

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

Use the existing fields: give the research object in `canonicalObject`, the
source-backed reason to investigate in `whyNow`, the real decision a good answer
would change in `communityPrize`, and the open distinction together with the
initial idea and its rationale in `nonBindingLens`. Put the earliest informative contact in
`firstEmpiricalContact`. These fields convey one argument, not independent boxes
to fill. The lens remains non-binding. The renderer must not invent missing science.

The start prompt is a project-specific research commission, not a generic slogan and
not an executable research plan. It should explain this project's community prize,
canonical object, deployment boundary, current published-method map, initial idea,
and suggested empirical contact in enough detail for the PI to understand why the
project exists and what is worth trying. Frame this as a researched starting point that the PI may
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
