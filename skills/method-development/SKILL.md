---
name: method-development
description: Interpret empirical evidence, form a design-giving problem account, cultivate and repair one load-bearing method primitive, and plan decisive construction or expansion experiments. Use throughout method formation rather than spawning a new idea after every result.
---

# Method Development

Develop one coherent scientific construction under the continuing ownership of
`research-pipeline`. Analysis, invention, and experiment design are coupled activities;
they are not separate approval stages.

Construction is also a way to discover the explanation. Begin with a consequential
question and enough evidence to make an informative attempt; the final mechanism need
not be known in advance. Preserve continuity of the problem and accumulated lessons,
not allegiance to the first formula. Judge optimization by what it can teach or repair,
not by whether the changed variable is called a rank, schedule, threshold, or module.

The target is a principled, economical method, not an ad hoc heuristic package. Keep
diagnostic shortcuts distinct from the contribution. When choosing or revising a
candidate, use the principle-and-simplification guidance in
[method-primitive-synthesis.md](references/method-primitive-synthesis.md); elegance
must survive implementation and comparison, not just the method's description.

Improve the method within the intended main comparison, not by silently changing its
evaluation conditions. A useful native or diagnostic result guides construction;
`research-foundation/references/baseline.md` owns whether it can enter the main table.

Start construction from a verified task, data and evaluation path. When it is a good
fit, keep a strong published method runnable and reuse its implementation. For a
learning problem, prefer fixing the training data with the recipe and model intact.
If the data already carry the right signal but the recipe does not teach the behavior,
change how the model learns. Change architecture locally only when the evidence points
to a limitation of the existing representation, interface, or computation. This is an
order of preference, not a sequence of required runs. Follow the evidence directly when
it already locates the problem, including in inference rather than training.

Start with the foundation's comparable successes, failures, and disagreements, not
with a module to justify. Identify what the model needs to learn or do differently
while keeping the behavior that already works. Trace the actual inputs, updates or
decisions, and any feedback into the next round of training data as far as needed
to choose an intervention. Alternatives matter when they lead to different changes;
read existing cases or traces first, and construct when that is the informative way
to distinguish them.

Make the explanation constrain the implementation: check what the proposed change
actually alters and what it leaves intact. If it cannot express the claimed
intervention, redesign it or treat it as a distinct diagnostic, not as an
implementation of the original idea. Use `signal-analysis.md` to connect behavior
to the change and `method-primitive-synthesis.md` to judge its net value on the
original task. Verify what the model learned, not just that the code ran.

Keep implementation and log-heavy diagnosis in bounded host subagents when separable;
the PI reads the evidence that changes the design. When the current explanation
cannot account for an important counterexample and the next implementation would
commit the project to that explanation, start an
[independent design race](../research-pipeline/references/collaboration.md#independent-design-race).
Let both collaborators investigate the original evidence before seeing the PI's
interpretation or each other's proposal. Do not wait until the PI has already
named a second explanation. Ask what each design would change on the original
task and what observation would change the choice. For other open invention
questions, see [co-invention guidance](references/method-primitive-synthesis.md#use-co-invention-at-a-real-invention-point).

Own improvement beyond v1: connect real experiments, model/code analysis, relevant
primary literature, and published competitors' behavior to the next implemented change.
Continue toward the commissioned performance target and a simple, supported submission
within authorized resources. The synthesis reference owns target interpretation,
comparison coverage, and simplification; neither a first positive result nor a first
draft completes this responsibility.

## Route The Work

- To read raw results, distinguish observations from explanations, compare problem
  models, or extract construction lessons, read
  [signal-analysis.md](references/signal-analysis.md).
- To propose, implement, ablate, diagnose, repair, simplify, or expand a load-bearing
  primitive, read
  [method-primitive-synthesis.md](references/method-primitive-synthesis.md).
- To choose an empirical-contact, explanatory, construction, expansion, or claim
  campaign, including comparisons, seeds, ordering, and compute, read
  [experiment-plan.md](references/experiment-plan.md).

Read more than one reference when the live research episode genuinely couples those
jobs. Preserve the full construction lineage and return the scientific synthesis to the
single project state; do not create parallel method identities or procedural gates.
