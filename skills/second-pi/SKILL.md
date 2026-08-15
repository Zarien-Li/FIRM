---
name: second-pi
description: Uses an independent reviewer with exactly one role matched to evidence maturity: Field/Prize before natural contact is complete, Interpret after a competent evidence bundle, Method Challenge after the lead PI proposes constructions, Program Expansion after a credible positive realization, and artifact, paper-entry, or proof review only for later fixed artifacts.
when_to_use: Invoke explicitly at a consequential scientific decision whose evidence maturity matches one review role; never after every result.
argument-hint: "[role and evidence packet]"
context: fork
background: false
---

# Independent Second PI

The reviewer is an independent scientific colleague, not the program's judge, first source
of theory, experiment queue, or user authority. The lead PI owns empirical contact,
explanations, first method proposals, synthesis, implementation, and final decisions.

Choose exactly one role. Never combine field selection, causal interpretation, method
invention, and submission judgment in one review.

## Field/Prize

Use before competent natural contact or when reconsidering the broad empirical
surface. Ask the reviewer to assess:

- the important capability, decision, or value frontier;
- accepted tasks, natural systems, and relevant populations;
- direct, simple, and nearest-locus incumbents;
- evidence needed to show that a residual is natural, consequential, and unowned;
- substrate and evaluation risks that could make the opening illusory.

Field/Prize must not propose a hidden variable, mechanism, method name, architecture,
objective, diagnostic slice, or method experiment. It maps the prize and missing
contact, not the solution.

## Interpret

Use only after the project has:

- a healthy standard-task evaluator and competent substrate;
- a competent direct incumbent and serious simple alternative;
- the nearest same-locus rivals identified and the closest feasible one inspected;
- natural successes, failures, disagreements, and inconvenient cases;
- a bundle large enough to distinguish explanations rather than one isolated result.

Provide the lead PI's two or three competing explanations. Ask the reviewer to compare their
predictions, support, contradictions, and unidentified remainder. Interpret may
identify a design-relevant variable only when the natural evidence distinguishes it.
It does not invent a method.

## Method Challenge

Use only after the lead PI independently proposes a concrete candidate set with real
alternatives at the level the evidence supports; do not require a fixed candidate
count merely to unlock review.
Provide the evidence bundle, competent substrate, nearest-rival threat, expected
end-to-end value, utility risks, and proposed construction episodes.

Ask the reviewer to expose redundancy, compare unique predictions, identify missing component
or interaction controls, and strengthen the best construction. It may repair a PI
proposal; it must not create the project's first method from an underdetermined
observation.

After a competent negative, Method Challenge must not automatically invent the next
method or hidden variable. First assess whether the accepted benchmark still supports
an untested load-bearing prediction and whether another episode would create a named
paper asset. Otherwise recommend consolidation or re-grounding while preserving valid
evidence; do not issue stop, freeze, or contribution-type verdicts.

The output is one construction episode containing a real implementation, one
component/interaction comparison, and one paired utility check. It is not a serial
chain of gates.

## Program Expansion

Use only after a credible positive realization has end-to-end value and a coherent
governing principle. Supply that principle, the realization, decisive rival, utility
surface, current scope, and expansion axes proposed by the lead PI.

Ask the reviewer to identify the largest scientifically coherent form of the idea:

- which expansion would strengthen the central principle rather than add table rows;
- whether it can create reusable supervision, data, architecture, systems, or tooling;
- which task/model/scale transfer is predicted rather than merely convenient;
- what can be deleted to make the idea simpler and easier to adopt;
- whether ten times the resources would deepen the contribution or only stabilize it.

Do not begin with reviewer objections. This role allocates positive ambition and paper
budget; it does not grant paper entry, prove causality through scale, or turn a failed
method lineage into another contribution type.

## Later Artifact Roles

- **artifact reviewer:** adversarial scientific review of contribution importance,
  identity, title/scope, strongest alternatives, and likely reviewer objections after
  a trained/executable method has coherent positive end-to-end evidence, or a fixed
  non-method object has independent confirmation;
- **paper-entry:** Prize/Fidelity/Entry review of a complete bounded paper package;
- **proof-audit:** isolated verification of formal statements and proofs.

A deadline, draft, long history, or failed method lineage does not justify these
roles. A method failure does not authorize analysis-paper review. There is no separate
headline audit: title, scope, and paper identity belong to artifact review.

This skill does not verify experiment implementation or provenance, bibliography
identity, or manuscript numbers. Route those to `/firm:audit-experiment`,
`/firm:audit-citations`, and `/firm:write-paper` claim checking respectively.

For artifact, paper-entry, and proof roles, use a fresh context and provide no prior
scores, desired verdict, fix summary, style exemplar, or hidden author-side argument.
Interpret may receive the competing explanations it is explicitly asked to compare,
and Method Challenge may receive lead-PI constructions.

## Review Episodes, Not Every Result

Before any second-PI call, inspect the latest construction marker. If
`[FIRM CONSTRUCTION_LEASE id=<id> state=active]` has not been followed by the matching
`state=complete` or `state=released`, defer the review. Intermediate training points,
component outputs, and GPU status do not authorize Interpret or Method Challenge.

Call the second PI when independent judgment could change a consequential decision:

- adopt or reject a natural problem after contact;
- choose among lead-PI constructions;
- allocate a paper-sized expansion program after a credible positive realization;
- redesign after a completed construction episode;
- materially change task, population, metric, primitive, contribution type, or paper
  identity;
- enter submission-oriented writing.

Do not invoke it after every probe, ablation, seed, or component result. A smoke test,
cheap negative, or additional caveat is not a new evidence maturity level.

## Evidence Packet

Give only what the selected role needs, with raw evidence before the preferred story:

- sealed original program and current candidate separately;
- exact evaluation conditions and durable raw paths;
- evaluator and substrate health;
- direct incumbent, simple alternative, and nearest same-locus rivals;
- representative natural successes, failures, disagreements, and contradictions;
- supplied explanations for Interpret;
- supplied constructions for Method Challenge;
- supplied principle and expansion axes for Program Expansion;
- scope movement and unresolved ownership threats.
- benchmark anchor, artifact roles, last anchor movement, paper-asset target and
  expected delta, and evidence supporting continued investment in the lineage.

Old contracts, drafts, state labels, and prior reviews are provenance, not premises.

## Lead-PI Synthesis

The lead researcher independently adjudicates the response and records:

```markdown
## Second-PI Synthesis
- role and question:
- evidence bundle or construction episode reviewed:
- accepted insight and evidence:
- deferred suggestion and why:
- rejected suggestion and evidence:
- explanation or construction change:
- nearest-rival/substrate consequence:
- scope or contribution-type change: none | exact user-approved change
- thread ID:
- selected next action:
```

Do not write `ADOPTED` merely because the reviewer is confident. Material validity findings
must be verified against raw artifacts before they change evidence status.

## Bounded Dialogue

Use a fresh reviewer context when the role changes, a new evidence bundle is complete,
or genuine independence is needed. Continue the same reviewer thread only when
corrected facts or new evidence address the same unresolved dispute. Do not shop for
agreement.

Default to one pass per role and evidence bundle. A second pass needs new evidence that
directly addresses the first disagreement.

Prompt skeletons:

```text
Field/Prize: Assess the value frontier, accepted surfaces, decisive incumbents,
nearest same-locus work, and missing natural-contact evidence. Do not propose a
mechanism, hidden variable, method, or method-shaped experiment.

Interpret: Compare the supplied competing explanations against the bundled natural
evidence. State what is distinguished and what remains unidentified. Do not invent a
method.

Method Challenge: Compare the lead PI's supplied constructions against the nearest
rival and evidence. Challenge redundancy, unique predictions, value, and costs, then
recommend one construction episode.

Program Expansion: Given the credible positive realization and supplied principle,
identify its largest coherent scientific form. Separate contribution-strengthening
expansion from extra rows, test adoption and cross-generation value, apply the 80%
deletion and ten-times-resource tests, and do not start with defensive objections.
```

## Concern Triage

For later reviews classify concerns as:

- `EVIDENCE_INVALIDATING`;
- `METHOD_DESIGN_CHANGING`;
- `CLAIM_NARROWING`;
- `DEFERRABLE`.

Only the first two normally create immediate research work. A review should not
produce a defensive experiment checklist. Contribution-type change follows
`../audit-research/references/research-control-protocol.md` and requires an independent
object plus user approval.

## Proof Audit

In proof-audit mode inventory formal statements, map proofs and dependencies, inspect
assumptions, quantifiers, domains, case coverage, limits, and hidden regularity, and
attempt counterexamples. Report exact file/line evidence and minimal repairs. For
submission assurance write `PROOF_AUDIT.md` with exact dependencies, findings, and
repairs. Proof audit does not redesign research or grant paper entry.

## Tool Policy

Use a fresh Claude fork by default. When Codex MCP or another genuinely independent
reviewer is configured, it may provide the independent pass; use its account default
instead of guessing model names. Retry one exact transient capacity failure.
Authentication, transport, capacity, and version failures are infrastructure. Record
`second_pi_status: deferred_tool_unavailable` and continue non-dependent research;
missing review is neither approval nor rejection.
