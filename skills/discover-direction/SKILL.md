---
name: discover-direction
description: Finds consequential and feasible computer-science research directions from the field surface rather than generating generic idea lists.
when_to_use: Use when choosing a new research program, refreshing a stalled direction, mapping benchmark and SOTA tensions, or identifying a high-value empirical entry point.
argument-hint: "[field, topic, or constraints]"
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

Use the template in [`references/program-card.md`](references/program-card.md). Name:

- field and value;
- empirical surface;
- SOTA and simple baselines;
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
