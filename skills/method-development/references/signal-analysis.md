---
name: signal-analysis
description: Interpret raw empirical evidence into a compact, design-giving problem model. Use when observations, contradictions, or method results must change scientific understanding rather than merely add another metric or slice.
---

# Evidence And Scientific Interpretation

Interpret evidence for the current research episode. A result need not produce a new
mechanism, method, paper asset, or project verdict.

## Begin With A Trustworthy Observation

Read the smallest sufficient set of raw predictions, references, traces, metrics, logs,
and durable artifacts. Compare matched successes and failures, competing methods on the
same examples, and target movement with utility costs. Before mechanism language, state:

- the exact population, treatment, comparator, and outcome;
- what changed, where it did not, and the uncertainty or run competence;
- representative support and inconvenient cases;
- the evidence role and artifact paths.

Use three evidence roles:

- `claim-bearing`: an accepted benchmark, natural workload, or independently justified
  population;
- `training`: evidence used to fit or select the system;
- `diagnostic`: a slice, probe, generated case, oracle, stress condition, or proxy used
  to debug or distinguish explanations.

Diagnostic evidence can reshape a design. It cannot establish prevalence, generality,
practical value, or benchmark improvement merely by being clean or numerous.

When leakage, population drift, cache state, temporal availability, evaluator meaning,
or implementation competence is genuinely in doubt, use
`research-foundation/references/experiment-integrity.md`. An invalid or interrupted
run is an execution fact, not a scientific negative. Propagate consequential
invalidation through `evidence-lineage.md`.

## Build A Problem Model At Intervention Resolution

Deep analysis is not a larger failure atlas. Reconstruct only enough of the incumbent
computation to explain the important behavior and guide a different construction:

- the natural event and accepted outcome that make the problem consequential;
- how information moves through representation, state or interaction, update or
  decision, execution, and measured utility;
- where supervision, credit, retrieval, memory, tools, or external computation enter;
- the useful default assumption behind ordinary success and the natural condition under
  which it becomes wrong;
- the earliest meaningful divergence between matched success and failure;
- what a valid intervention must change and what capability, information, or cost it
  must preserve.

The account may be causal, algorithmic, optimization-based, representational, or
systems-level. Develop it toward an explanation of successes, failures, disagreements,
and inconvenient cases, with alternatives that imply different constructions. This is
an evolving research product, not a prerequisite to train. A partial account can justify
an informative implementation whose outcomes reveal missing structure. A label that
merely renames a slice, score, or correlated feature is not a problem model.

Use code reading, matched cases, traces, literature, or controlled interventions only
when they resolve a design-relevant link. If alternatives remain underdetermined, choose
evidence that can meaningfully separate their construction consequences, including a
real training experiment when small probes cannot do so. Do not compensate
with a larger probe suite, more taxonomy, or a premature method name.

### Locate The Failure Before Choosing What To Change

Start from an actual success and a comparable failure of a competent system. Ask
what distinguishes them in the task, then follow that difference through the actual
inputs, the training signal, and the model's decision only as far as it changes
the design. A failure that first becomes visible in attention or the output does
not necessarily originate there.

For example, audio and video from the same clip can be recognized as compatible
without binding a particular sound to the action that made it. If the training
examples reward clip identity as much as event binding, changing which examples
are seen can teach a distinction without changing the model. If those examples
already distinguish the events but the loss gives the same feedback for correct
and incorrect binding, change where supervision acts. If the two cases become
indistinguishable at an input interface, a later loss cannot recover the missing
distinction from that path. Before making that last claim, check whether the cue
was absent at the source, lost in the interface, or simply missed by the probe.
An existing scorer may also conflate these outcomes; keep that measurement problem
separate from a model diagnosis.

Use the difference to choose between actual interventions. Ask what would happen
with the same model and recipe on more informative data, or with the same data and
model under different supervision, when those are the live alternatives. Existing
evidence can settle the choice; do not run all contrasts by default. Depth means
explaining why a smaller change would or would not work, not tracing more layers
or asserting a unique root cause before building anything.

Read the proposed operation at the same resolution as the explanation. If the
problem is interference in particular update directions, uniformly shrinking an
update can test its magnitude but does not selectively remove those directions.
Likewise, a useful gated variant does not realize an ungated proposal. Keep each
answer attached to the operation that produced it. Exploration remains useful
without silently replacing the original proposal or inheriting its attribution.

## Maintain Competing Explanations Sparingly

Keep the smallest useful set, normally two or three, of alternatives whose truth would
change the next design. For each, retain supporting evidence, contrary evidence, one
distinct prediction, and what remains unidentified. Update the bundle only when
accumulated evidence distinguishes those predictions. Refuting A does not prove B unless
the alternatives are exhaustive.

Distinguish an observed signature, a useful working explanation, and an explanation
actually separated from its alternatives. State what observation contradicts the
specific prediction before calling an account refuted; otherwise explain why its
priority changed and what remains unresolved. Low training error relative to validation
can implicate generalization without proving optimization adequate. An early best epoch
or early stop alone does not establish underfitting. These are examples of ambiguous
signatures, not a fixed diagnostic taxonomy. Choose an informative construction from
the best current account without requiring a finished causal proof before proceeding.

A probe can decode a distinction without showing that the model uses it. An oracle
can pick the correct branch after the answer is known without showing what evidence
a real policy could use at that moment. Before building a selector or teaching rule,
trace the cue to information available at the actual decision time and under the
intended budget. Keep privileged training signals distinct from deployment inputs.
If that link is missing, improve how evidence is obtained or how the decision is
made rather than assuming a better gate can recover the oracle gain.

## Read Method Results As Construction Evidence

Interpret versions and ablations as one arc when they share a principle. Locate the
earliest broken link among engagement, competence, proxy, coupling to regression,
context, or redundancy with a decisive alternative. Preserve what ran and extract the
useful residual, failed assumption, and design consequence. Failed variants do not add
up to family coverage; [method-primitive-synthesis.md](method-primitive-synthesis.md)
owns successor inheritance and repair. When a published comparator wins, explain its
computation, boundary, and cost before deciding whether a non-redundant need remains.

For a consequential result, compare the current method and a healthy published rival on
the same development examples, including cases each gets right and wrong. Trace the
actual inputs, intermediate states, objective/gradients or decision rule, and output
where needed to locate the earliest design-relevant disagreement. Relate it to the
rival's full paper and implementation, not a guessed explanation from its name.

Distinguish an implemented term, its effective contribution to updates, and a learned
change in behavior. A teacher can agree with the student on nearly all relevant
choices, a special loss term can leave the chosen trajectories almost unchanged,
and a lower loss can reflect an easier target. Read the evidence where it would
separate these accounts: actual targets and weights, accepted and rejected examples,
realized update contributions, or matched before/after behavior. Ask what ordinary
training would have done on the same examples. A trace can expose a degenerate
objective without proving downstream benefit or lack of benefit.

When the updated model generates or selects its next training data, reason through
the feedback loop. For example, a collector can require tagged outputs while SFT
teaches untagged ones. The next policy then produces fewer admissible examples;
normalizing only over survivors can give that shrinking, biased set a full update
and favor increasingly long targets. Each step can pass its execution checks while
the loop undermines the intended learning. Compare the changing population, effective
loss weights, and model behavior over time where they bear on the design. Repairing
that loop is not evidence of a benchmark gain.

Make the diagnosis executable: identify the computation to change, the behavior that
should move, the contrary outcome that would challenge the account, and the useful
behavior to preserve. Labels such as "insufficient representation" or "weak coupling"
are not enough without this connection. Prefer existing trajectories, predictions,
and receipts. If a needed distinction cannot be recovered, instrument the next
useful run only for what can change the design; no fixed set of probes or proof
is required before construction.
Use training/development evidence for design choices. Test-set failure analysis is
exploratory and cannot also serve as untouched confirmation of the resulting revision.

## Decide At The Scale Of The Evidence

For an ordinary result, decide whether the observation is trustworthy, whether it
changes the current design question, whether dependent work became redundant, and what
smallest next action distinguishes the live explanations. At an episode boundary, also
judge whether the natural premise and accepted outcome were actually engaged and
whether to continue the construction, redesign it, or return to the broad program.

Only an artifact-grounded candidate or independently important confirmed phenomenon
should change the paper argument. Failed methods cannot choose an analysis-paper
identity for the project.

## Durable Output

Keep ordinary raw observations in the existing notebook/run artifacts. Interpret
consequential observations in their research-tree nodes, linking supporting and contrary
artifacts rather than copying a trace. Explain whether the result changes this
implementation, the governing principle, or the parent question; uncertainty at one
level must not become a conclusion at another. The tree's `last_change` carries the
goal/claim movement and remaining decisive comparison. A useful interpretation can
leave the claim unchanged. For a compact observation artifact, use:

```markdown
## Observation
- conditions, evidence role, result, uncertainty, cost, and paths:
- support and contrary cases:
- effect on the current design question:
- explanation update, if any:
- next consequential action:
```

For a completed explanatory or construction episode, create `RESULT_TO_CLAIM.md` only
when durable coordination helps. Record validated observations, the problem model and
alternatives, construction lessons, accepted-surface consequence, and the next episode.
Paperwork must not delay a clear reversible research action.
