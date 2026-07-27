---
name: research-lit
description: Search and analyze papers, implementations, benchmarks, baselines, and related-work terrain for a live research question. Use to understand the field, choose serious empirical anchors, promote close work to baselines, identify assumptions and compromises, or test a specific novelty and implementation concern.
---

# Research Literature

Use literature to improve empirical and design decisions. It is a terrain map, not a permission system.

## Start With A Research Question

Search for a concrete need such as:

- field-standard benchmark and baseline families;
- the strongest current implementation for a reproduced failure;
- whether a proposed causal operator already exists;
- what compromise or regime limit close methods leave;
- how an adjacent field represents a similar problem;
- which implementation details determine a fair comparison.

Avoid broad search as a substitute for running or reading local evidence.

## Source Policy

Prefer primary sources:

- official paper pages and proceedings;
- author or project repositories;
- official documentation and benchmark pages;
- appendices and supplementary material.

Use recent sources for frontier claims. Verify title, authors, venue, year, and method details before recording them.

## Codex MCP Search

When using Codex for literature or factual search, call `mcp__codex__codex` directly. Search is
not a separate Codex script or MCP: it is the same tool as review with a search-oriented prompt.

```yaml
mcp__codex__codex:
  sandbox: read-only
  approval-policy: never
  cwd: /absolute/path/to/current/project
  prompt: |
    Use web search to answer this precise research question: [QUESTION].
    Return concise findings with primary-source URLs and explicit dates where relevant.
    Distinguish verified facts from uncertain or conflicting evidence.
```

Omit the `model` field; the configured provider selects it. Preserve the returned `threadId`, but
start a fresh call for an unrelated search. If the exact error is `Selected model is at capacity`,
retry the identical call once. Do not route the request through `codex-search`, bare `codex`, a
prompt file, or a headless Claude process. Search results locate evidence; read the primary paper,
official proceedings page, repository, or benchmark source before making a load-bearing decision.

## Read For Decisions

For each important work, extract:

- problem and value claim;
- task, data, metrics, and scale;
- actual method primitive;
- assumptions and required supervision;
- strongest baselines;
- cost, latency, coverage, or capability tradeoffs;
- failure cases and limitations;
- implementation availability;
- exact relevance to the project's reproduced evidence.

Do not infer exact closure from abstract similarity.

## Interpret Related Work

Classify close work as:

- baseline to reproduce;
- component or idea to inherit;
- empirical threat requiring matched comparison;
- adjacent analogy;
- broad contextual work.

A paper blocks the current method claim only when it implements the same load-bearing idea and matched evidence shows it already closes the same failure without the claimed advantage. Otherwise it raises the differentiation bar and improves the project.

## Implementation Landscape

When experiments depend on code, record:

- chosen repository and commit/version;
- license and model/data access;
- environment and hardware assumptions;
- missing scripts or undocumented steps;
- expected reproduction difficulty;
- viable community implementation if official code is unusable.

## Output

Write a literature report only when it will guide later work:

```markdown
# Literature Decision Report

## Research Question
- ...

## Field Surface
- accepted tasks/benchmarks:
- recurring SOTA and simple baselines:
- implementation anchors:

## Closest Work
| Work | Primitive | Evidence surface | Assumption/compromise | Role in our project |
|---|---|---|---|---|

## Research Consequence
- stronger baseline to promote:
- novelty/design pressure:
- unresolved empirical question:
- next action and why:
```

Do not end a live empirical program from literature alone.
