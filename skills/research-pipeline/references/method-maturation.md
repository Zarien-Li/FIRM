# Method Maturation And Rival Gap

Use this reference while turning a design opportunity into a reusable primitive,
learning from failed realizations, or deciding whether a score gain still represents a
coherent contribution.

## Begin With A Design-Giving Account

State the accepted problem, the incumbent's useful default assumption, the natural
condition where it becomes harmful, the earliest computational divergence, a contrary
case, and the behavior a replacement must preserve. Prefer a principle that changes a
load-bearing representation, state, update rule, routing rule, memory, objective
factorization, training semantics, or execution abstraction.

The final contribution should be simple enough to state in one sentence even when the
research required difficult analysis. Aim to create a concept other researchers can
use, not only a model they can compare against.

## Build A Construction Arc

Implement the smallest real version that can instantiate the principle on the accepted
surface. Read failure according to where it occurred:

- the intended treatment was not instantiated;
- the treatment activated but the predicted intermediate behavior did not change;
- the behavior changed but the primary value did not;
- value improved but utility or cost erased the advantage;
- the nearest rival already provided the same operational effect.

These are explanatory possibilities, not fixed states. Inspect artifacts and repair the
evidence-implicated component. Do not respond to one negative sign by closing the field,
and do not protect a weak construction with renamed variants, parameter sweeps, or a
search for friendly seeds.

A successor realization belongs to the same lineage when the load-bearing principle is
still present and the new design follows from the prior result. Record the failed
prediction, changed component, preserved useful behavior, and new discriminating
prediction. Otherwise treat it as a new scientific episode without inherited maturity.

## Track Method Debt With The Decisive Gap

Keep a live natural-language account of:

- the decisive published rival and the exact value or Pareto gap;
- which component of the current construction is expected to close it;
- whether removing the proposed primitive destroys the advantage;
- what additional machinery the complete system now requires;
- what behavior, cost, latency, memory, calls, supervision, or portability it trades.

Count external models, routers, retrieval or memory systems, targets, fallbacks,
supervision, extra calls, storage, dataset-specific rules, and deployment assumptions.
The question is not whether every addition is forbidden. It is whether the resulting
system still teaches one clear principle and offers a meaningful advantage a reader
would choose.

Use deletion as a design instrument: remove auxiliary machinery and ask what principle
and value remain. If almost everything can be deleted while preserving the insight, the
primitive is becoming clearer. If the original primitive can be removed without losing
the result, do not keep it as the paper's nominal center.

## Choose A Contrastive Surface From The Principle

After a coherent positive result, identify where the claimed principle predicts a
different but informative outcome. The contrast may cross a natural regime, model
family, scale, task condition, modality, or system constraint. Choose it for its ability
to distinguish a reusable mechanism from a substrate-specific trick, not because it is
easy or likely to be positive.

A competent negative contrast can refine the principle or expose a realization limit.
It does not automatically kill the method. A positive contrast can support expansion,
but breadth should follow the causal reach of the principle rather than accumulate as a
submission checklist.

## Know What A Positive Object Is

A paper-bearing method is an executed end-to-end object with valid information flow,
credible comparison, attribution to a load-bearing computation, meaningful utility and
cost, and a community consequence. The amount and shape of evidence depend on the
claim. A method name, oracle gap, one favorable cell, many experiments, or a draft does
not establish this object by itself.
