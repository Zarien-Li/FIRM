# Empirical Foundation

Use this reference when entering a field, reproducing published methods, selecting the
evidence surface, auditing information flow, or interpreting natural behavior.

## Start From The Accepted Object

Identify the task or natural system practitioners actually use, the primary outcome,
the population that carries value, the relevant cost and side effects, and the methods
that define current practice. A private slice can reveal a mechanism but cannot silently
replace the accepted object.

Read natural successes, failures, disagreements, and surprising cases. Do not stop at a
headline score. The goal of contact is to understand the computation and compromise of
serious systems well enough that a consequential design question can emerge.

## Map Information Before Method-Guiding Evidence

Before treating a result as design evidence, trace in ordinary prose:

- which examples and labels belong to training, development, test, and reporting;
- where model, prompt, hyperparameter, checkpoint, or threshold selection occurs;
- what temporal state, future information, cache, preprocessing, and retrieved content
  each stage can access;
- how targets, external signals, generated data, and prior model outputs are produced;
- what the evaluator consumes, filters, aggregates, and reports;
- which artifacts preserve the exact predictions and selections.

This is not a compliance box. It is a causal account of how the reported number was
created. Revisit it whenever the task, evaluator, cache, generated supervision, or
selection procedure materially changes. A later audit can verify the account, but it
should not be the first time the PI asks these questions.

## Give Comparisons Different Jobs

Comparison responsibility depends on the scientific decision.

**Field contact.** Reproduce at least one serious recent published method closely enough
to establish that the task, data, evaluator, and substrate behave as the field expects.
Resolve material gaps from the accepted protocol instead of freezing a convenient weak
local number.

**Construction judgment.** Confront the strongest method that performs the same
operational job and the nearest method that uses the same mechanism or intervention
locus. This prevents a candidate from borrowing novelty from a missing rival.

**Submission evidence.** Assemble the claim-dependent set needed for the bounded paper:
the methods a reader would actually choose between, matched utility and cost, relevant
model or task coverage, and uncertainty appropriate to the claim. Do not turn this into
a universal leaderboard requirement.

Base checkpoints such as Qwen, Llama, CLIP, or a diffusion backbone are substrate
controls unless the claim is about backbone choice. Internal ablations establish
attribution. Oracles establish headroom. None replaces published field methods.

## Preserve Semantic Fidelity

For each decisive system, record paper and implementation identity, revision, data and
split, preprocessing, checkpoint, prompts or decoding, training budget, evaluator,
selection rule, resource cost, and known deviations. Compare systems under the same
operational contract unless the scientific claim is explicitly about that difference.

Treat a cheaper model, smaller task, synthetic corruption, clean subset, or alternative
metric as diagnostic until it preserves the motivating phenomenon and rival ordering.
If the phenomenon vanishes because the substrate changed, do not design a method for the
proxy artifact.

## Turn Behavior Into A Design Question

Cluster behavior only to discover shared computation and value, not to manufacture a
paper taxonomy. For an apparent failure, compare matched successes and counterexamples:
what information was available, which computation used it, what competing objective was
served, and where the paths diverged. Ask whether the primary metric can register the
desired improvement and whether the intervention can access its required signal at
deployment time.

An empirical opening is meaningful when it points to a changeable assumption shared by
important systems, not merely a region where one chosen model scores badly.
