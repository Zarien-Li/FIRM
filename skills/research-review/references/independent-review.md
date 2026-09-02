# Independent Codex Review

Use an independent Codex episode to resolve one consequential uncertainty, not to
shadow the persistent PI or generate an objection backlog. The collaboration rules for
Claude implementation, Gemini co-invention, evidence transfer, and context isolation
live in `research-pipeline/references/collaboration.md`.

## Earn The Call

Default to no independent review during initial empirical contact, underdetermined
explanation, first-method invention, ordinary repair, or routine negative results. Let
accepted-task evidence answer the design question whenever it can.

Review becomes useful when the PI can name both an uncertainty and the current decision
it could reverse. Examples include:

- whether a close published method already performs the same operational job;
- whether an evaluator, information path, or causal inference supports a consequential
  claim;
- whether an artifact-grounded side result retains the original program's value before
  it receives paper-sized investment;
- whether a fixed near-final claim, citation, proof, or reported number is correct.

A deadline, disagreement, draft, large artifact directory, or failed method lineage
does not by itself earn review. Do not ask Codex to select among speculative first
principles, invent the next method, score acceptance probability, or search for every
possible weakness. A repeated call needs materially new evidence or a different
decision-relevant question.

## Frame One Decision

State the strongest evidence-supported object before asking for criticism. Supply the
accepted surface, competent substrate, decisive functional and mechanistic rivals,
relevant successes and failures, contrary cases, exact raw paths, and the decision at
stake. For interpretation, include the PI's few live explanations and the observations
that distinguish them. For a program-fidelity question, keep the original program and
current candidate separate.

Ask the reviewer to resolve only the named uncertainty, identify the supplied evidence
that bears on it, and explain whether the answer changes the current design, claim,
resource, or paper decision. If it does, request the smallest discriminating evidence
and its opportunity cost. Otherwise the useful result is `no material change`.

Open-ended prompts such as “review this project,” “find all weaknesses,” and “what else
should we run” reward objection volume. A broad boundary review, when genuinely needed,
should stay bounded to prize, fidelity, and trajectory: whether perfect success changes
an accepted community outcome, whether the work still serves the original program and
substrate, and whether the next construction inherits a real principle.

## Keep Advice In Its Place

Codex may qualify evidence or expose a decision-relevant conflict. It cannot create a
user constraint, permanent gate, defensive experiment suite, contribution-type change,
program closure, or replacement method. Venue taste and hypothetical reviewer
preferences create no task unless they alter a real submission decision.

The PI verifies factual findings against primary sources or raw artifacts and records
only the decision and evidence that changed. Advice unsupported by the supplied evidence
remains advice. Do not record `adopted` merely because the reviewer is confident.

A compact synthesis is enough:

```markdown
## Independent Review Synthesis
- question and decision at stake:
- evidence inspected:
- finding and confidence boundary:
- decision changed, or no material change:
- smallest justified action:
- reviewer thread:
```

## Proof And Artifact Review

For formal work, inspect statements, assumptions, quantifiers, domains, dependencies,
case coverage, and counterexamples. For external artifacts, apply the assurance
requirements in the parent `research-review` skill. Proof and artifact review verify an
existing object; they do not redesign the research or grant paper maturity.

## Tool Policy

Call `mcp__codex__codex` and `mcp__codex__codex-reply` without a `model` field. Retry
one identical transient capacity failure. Authentication, transport, capacity, version,
or model-routing failure is infrastructure, neither approval nor rejection; continue
non-dependent research.
