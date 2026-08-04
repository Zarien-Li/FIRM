---
name: literature-review
description: Searches and analyzes papers, implementations, benchmarks, and related-work terrain for a live research decision.
when_to_use: Use when understanding a field, locating close work, choosing baselines, checking novelty, finding implementations, or testing a specific technical assumption.
argument-hint: "[research question]"
---

# Literature Review for a Live Research Decision

Search to change a research decision, not to accumulate a generic bibliography.
Start from the exact question in `$ARGUMENTS` and the current project's thesis,
method, benchmark, or uncertainty.

## 1. Define the decision

State what the search must resolve, for example:

- Is the claimed problem already established on a natural benchmark?
- What are the strongest fair baselines?
- Has the proposed primitive already appeared under another name?
- Which paper owns a result, method, dataset, or metric?
- What implementation is closest enough to reproduce?
- Which assumption or compromise separates nearby methods?

Write one sentence describing how the answer will change the project.

## 2. Search the field surface

Use multiple query families:

- canonical task, dataset, metric, and benchmark names;
- mechanism and method-family names, including synonyms;
- the observed failure pattern in behavioral language;
- recent venue and year filters;
- exact-title, author, citation, and implementation queries for close work;
- references and citing papers of the closest sources.

Search broadly enough to avoid vocabulary lock-in, then narrow around the closest
work. Do not search only for “papers that do not do our idea.”

## 3. Prefer primary sources

Use the paper itself, official proceedings or publisher page, arXiv, project page,
official repository, dataset card, and benchmark documentation. Use surveys and
secondary summaries to map terminology, then verify consequential claims in the
primary source.

For every load-bearing factual statement, preserve a source and exact location or
passage. Never infer paper content from a search-result snippet.

## 4. Read for research consequences

For each close work, extract:

- problem and claimed contribution;
- task, dataset, model scale, and evaluation setting;
- method primitive and causal or empirical motivation;
- strongest result and strongest limitation;
- assumptions, compromises, and hidden costs;
- code and data availability;
- relation to the current project: baseline, adjacent, competing, enabling, or
  potentially novelty-threatening.

Do not reduce related work to keyword overlap. Compare the positive object,
load-bearing primitive, population, and decisive evidence.

## 5. Promote serious work to the right role

A paper should become a baseline when it is:

- a field-standard anchor;
- the strongest relevant recent method;
- the closest method sharing the intended value surface;
- a simple alternative that tests the same causal bet;
- or a method likely to expose whether the proposed contribution is unnecessary.

A close paper is not automatically a fair baseline if it solves a different task,
uses unavailable supervision, or has incomparable cost. State the mismatch rather
than hiding it.

## 6. Check implementations

For important repositories, verify:

- official or author-linked status;
- license and accessibility;
- supported datasets, checkpoints, and hardware;
- last meaningful maintenance;
- exact evaluation script and preprocessing;
- open issues that affect reproducibility;
- whether the released code matches the paper version.

Record the commit or release used when the implementation will anchor experiments.

## 7. Synthesize, do not list

Organize the literature around the decision:

- field consensus and accepted empirical surface;
- strongest contradiction or unresolved tension;
- closest work and exact overlap;
- what remains scientifically open;
- what must change in the current problem, method, baseline set, or claim.

A useful review may conclude that the current idea is already known, that the
benchmark is too weak, that a stronger baseline is required, or that the project's
real distinction lies at a different level.

## Output

```markdown
# Literature Decision Report

## Research decision
- Question:
- How the answer changes the project:

## Field surface
- Canonical tasks/datasets/metrics:
- Strongest recent anchors:
- Accepted limitations or tensions:

## Closest work
| Work | Setting | Primitive | Strongest evidence | Limitation | Role for this project |
|---|---|---|---|---|---|

## Implementation landscape
| Repository | Official? | Reproducibility notes | Intended use |
|---|---|---|---|

## Novelty and overlap
- Already established:
- Partially overlapping:
- Still open:

## Research consequence
- Problem update:
- Baseline update:
- Method update:
- Claim/scope update:
- Highest-value next action:

## Sources
- Preserve direct links or identifiers and the exact claims they support.
```

Be explicit about uncertainty and source access. Do not claim exhaustive coverage
unless the search procedure genuinely supports it.
