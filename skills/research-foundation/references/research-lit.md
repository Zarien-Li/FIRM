---
name: research-lit
description: Search and read primary literature for a live empirical, design, ownership, or implementation decision. Use when the field frontier, closest work, accepted protocol, or design rationale can change the research action.
---

# Research Literature

Use literature as a decision instrument, not a permission system or substitute for
empirical contact.

## Search From A Live Question

Name the uncertainty before searching, such as:

- which methods define the accepted task and current frontier;
- which implementation can faithfully reproduce the strongest incumbent;
- whether the proposed operational job or load-bearing computation already exists;
- what compromise or natural boundary remains after the nearest rival;
- how an adjacent field represents the same underlying problem;
- which protocol details determine a fair comparison.

Search again when the candidate's operational effect, intervention locus, deployment
contract, adopter, value surface, or contribution type materially changes. Seed-era
related work does not certify a new scientific identity. Search by input, output,
intervention time, user-facing job, and cost contract as well as mechanism terminology.

## Use Primary Sources And Read Complete Arguments

Prefer official proceedings and paper pages, author repositories, appendices,
supplementary material, benchmark documentation, and model releases. Use recent sources
for frontier claims and verify title, authors, venue, year, method details, and version.

For each consequential work, extract:

- problem and value claim;
- task, data, metrics, scale, and deployment assumptions;
- actual method primitive and where it acts;
- supervision, external computation, cost, latency, coverage, and capability tradeoffs;
- strongest comparisons, failure cases, and limitations;
- implementation availability and reproduction risk;
- exact relevance to the project's evidence and current decision.

Do not infer closure from title or abstract similarity. Reconstruct why the incumbent's
central assumption was adopted, what earlier problem it solved, and what changing it may
damage. Methods, ablations, code, and predecessor work often carry this rationale.

## Distinguish Literature Roles

Classify close work as a published baseline to reproduce, a component or idea to inherit,
an empirical threat requiring matched comparison, an adjacent analogy, or broad context.
A paper blocks the current novelty or value claim only when it implements the same
load-bearing idea or performs the same operational job under a comparable contract
without the claimed advantage. Exact closure still requires semantic and empirical
comparison.

`baseline.md` owns the authoritative distinction among published field methods,
backbone/substrate controls, and attribution controls. Literature search identifies the
methods, papers, implementations, assumptions, and roles; it does not replace their
reproduction with raw checkpoint evaluation or project-invented heuristics.

When experiments depend on code, record the repository and commit, license and access,
environment and hardware assumptions, missing steps, expected difficulty, and a mature
community implementation if official code is unusable.

## Codex MCP Search

When using Codex for factual or literature search, call `mcp__codex__codex` directly
with read-only sandboxing, no approval, the current project directory, and a precise
search prompt requesting primary-source URLs and explicit uncertainty. Omit the model
field so the configured provider chooses it. Preserve the returned `threadId` for the
same question and start a fresh call for unrelated work.

If the exact error is `Selected model is at capacity`, retry the identical call once.
Do not route search through `codex-search`, bare `codex`, a prompt file, or headless
Claude. Codex can locate evidence; read the primary source before making a load-bearing
decision.

## Return The Research Consequence

Write a durable literature report only when later work needs it:

```markdown
# Literature Decision Report
## Research Question
## Field Surface
- accepted tasks and protocols:
- published incumbents and implementation anchors:
## Closest Work
| Work | Primitive | Contract | Assumption or compromise | Project role |
## Research Consequence
- baseline or threat to promote:
- design or novelty pressure:
- unresolved empirical question:
- next action and why:
```

Update the project state only when literature changes the accepted surface, incumbent,
ownership threat, or design assumption. Cite a primary source for every load-bearing
fact. Literature alone cannot create a user constraint, close the program, or grant
paper maturity.
