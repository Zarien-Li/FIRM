---
name: frontier-direction-discovery
description: Discover consequential research programs and empirical entry points in a field. Use when selecting or refreshing a broad direction, identifying accepted benchmark and SOTA surfaces, or finding valuable shared tensions without pre-committing to a mechanism or searching only for untouched topics.
---

# Frontier Direction Discovery

Find a field worth sustained work and a credible way to enter it. Do not attempt to name the final paper before empirical contact.

## What Makes A Strong Program

Prefer directions with:

- clear scientific or practical value;
- active top-venue work and strong baselines;
- accepted benchmarks or real workflows with inspectable residual behavior;
- feasible access to models, data, and implementations;
- room for a method or system design contribution;
- important tradeoffs, assumptions, or shared limitations not fully represented by headline metrics.

Prefer programs where success could replace a consequential default assumption with a
simple reusable principle, not merely add a module to one incumbent. Consider whether
the principle could change downstream design choices, survive model-generation change,
and create a broad citation surface. Use the upside guidance in `research-pipeline`;
these are selection priors, not a promise or numerical gate.

Crowdedness is usually a positive signal of importance and evaluation maturity, not proof. Check whether the activity serves a real scientific or practical value rather than a fashionable leaderboard, and whether incumbents leave a consequential shared limitation. The question is not whether nobody has entered the field.

## Search The Field Surface

Use recent papers, accepted-paper lists, leaderboards, repositories, appendices, and issue discussions to learn:

- what tasks and metrics the community trusts;
- which baseline families recur;
- which implementations are reproducible;
- where methods trade quality for cost, robustness, coverage, or generality;
- which regimes are omitted or simplified;
- what real users or systems still cannot rely on.

Do not convert a limitation paragraph directly into an established research problem. Treat it as a candidate observation or abstraction to test independently; it may survive, change shape, or be replaced by a better problem.

## Form A Research Program Card

Use the template in `research-pipeline/SEED_TEMPLATE.md`. Name:

- field and value;
- empirical surface;
- recent published baselines and strongest incumbents;
- non-binding lens;
- resource and contribution constraints.

The lens can guide what traces to save or comparisons to inspect. It cannot dictate the final mechanism or stopping condition.

## Judge Feasibility Without Shrinking Ambition

Check whether the project can obtain meaningful empirical contact under its resources. Distinguish:

- a phenomenon visible at available scale;
- a frontier-only question that needs different resources;
- a benchmark or implementation currently inaccessible;
- a feasible field whose first chosen experiment is simply poor.

Do not replace a difficult method question with a benchmark-only, prompt-only, or analysis-only project for convenience.

## Output

Produce a small ranked set only when the user is choosing among fields. For each direction include:

- field and value;
- accepted empirical surface;
- representative SOTA/baselines;
- why active work makes the direction timely;
- non-binding failure lens;
- method-level opportunity classes;
- resource reality and major risk;
- first empirical contact.

Recommend one direction and explain the bet. Once selected, create the program card and begin empirical work rather than continuing abstract search.

Return the selection to `research-pipeline` by updating the existing authoritative
state with primary-source evidence, the original program/value target, canonical
tasks and metrics, accepted recent published baselines, resource boundaries, non-binding
lens, first empirical contact, planned lifecycle, and one next action. Use a
mergeable `research_state_patch` only when a structured handoff is useful; it is not
mandatory. Neither form creates a locked paper identity or user constraint:
preserve the user's seed verbatim and label the direction rationale
`[INTERPRETATION]`.
