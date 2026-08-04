---
name: diagnose-result
description: Interprets a completed baseline or method result without confusing one failed run with failure of the broader research program.
when_to_use: Use for surprising, contradictory, negative, or mixed results; simple-baseline inversions; artifact checks; causal diagnosis; and choosing the most informative next experiment. Do not use for launching jobs.
argument-hint: "[result file or question]"
---

# Diagnose a Research Result

Turn a completed result into a calibrated scientific decision. Separate what the
artifacts establish from the story the project hoped to tell.

## 1. Establish the evidence first

Inspect the raw result, configuration, code version, evaluator, logs, and relevant
baseline artifacts. Before interpreting, answer:

- Did the intended code path run?
- Did training or optimization behave competently?
- Are the compared systems matched in data, budget, preprocessing, and evaluator?
- Is the primary metric semantically appropriate for the claim?
- Are the sample, seeds, exclusions, and provenance explicit?
- Is the observed difference large relative to known noise or uncertainty?

If any answer is materially unresolved, label the result `run-uncertain` and
recommend the smallest integrity or competence check. Do not manufacture a
scientific diagnosis from a broken run.

Use `/firm:audit-experiment` when provenance or evaluator integrity is genuinely
suspect; do not invoke a full audit for every ordinary result.

## 2. Build a contrast table

Compare systems and regimes on the target outcome and on the mechanism the method
was intended to change.

```markdown
| Condition | Target outcome | Mechanism/proxy | Cost | Important raw behavior |
|---|---:|---:|---:|---|
| Strong baseline | | | | |
| Current method | | | | |
| Relevant control | | | | |
```

A proxy change without a target change is evidence about the design, not evidence
that the target problem disappeared.

## 3. Separate four layers

Write each layer explicitly:

1. **Observation:** the literal empirical pattern.
2. **Explanation:** competing causal accounts consistent with that pattern.
3. **Design consequence:** which method assumption or primitive should change.
4. **Paper consequence:** what claim, scope, or maturity changes now.

Never smuggle an explanation into the observation. “Routing entropy changed while
action-state errors did not” is an observation. “Routing cannot solve the problem”
is a much broader claim.

## 4. Diagnose failure at the narrowest justified level

Classify the result as one or more of:

- `implementation/run failure`;
- `optimization/statistical uncertainty`;
- `current realization failure`;
- `load-bearing primitive failure`;
- `method-family or program evidence`.

State why the evidence reaches that level and why it does not reach the next one.
One competent negative realization can justify replacing its failed component. It
does not automatically justify ten more seeds, a field pivot, or an analysis-paper
relabeling.

## 5. Generate competing explanations

Produce at least two serious explanations when the mechanism is not directly
identified. For each explanation, specify:

- what it predicts in already observed cases;
- what evidence contradicts it;
- the smallest discriminating intervention;
- the method change it would imply if true.

Prefer explanations that compress several regimes or anomalies under one variable.
Distinguish a **predictive signal** from a **causal handle**: a feature may forecast
failure yet remain useless to manipulate.

## 6. Invert strong simple baselines

When a simple baseline wins, treat it as evidence about a hidden coordinate. Ask:

- What information or inductive bias does the simple baseline preserve?
- What unnecessary burden does the proposed method introduce?
- Does the baseline exploit a variable omitted from the current thesis?
- Can the baseline be turned into a controlled intervention or positive design
  object?

Do not dismiss a strong simple baseline as “too simple.” It may be the cleanest
causal clue in the project.

## 7. Choose the next experiment by information gain

The next action should distinguish explanations or change the method, not merely
add coverage. Prefer, in order:

1. a competence or integrity check if the run is uncertain;
2. a causal ablation that isolates the implicated component;
3. a matched alternative that tests the strongest competing explanation;
4. a natural or standard-surface test that repays scope debt;
5. consolidation if the paper-critical claim is already stable.

For the chosen experiment, state:

- hypothesis and competing hypothesis;
- intervention and control;
- expected outcomes under each explanation;
- result that would change the method;
- cost and why this experiment dominates the alternatives.

Do not recommend a seed sweep unless stochastic uncertainty is the actual unresolved
question.

## 8. Update the method lineage and paper state

Record:

- what this version attempted;
- what changed relative to the previous version;
- what the result diagnosed;
- what remains valid;
- what the next version inherits;
- whether the paper claim, scope, contribution type, or maturity changed.

A failed method can still produce valuable design evidence. It has not automatically
earned an analysis paper; the surviving positive object and community consequence
must be stated.

## 9. Use an independent review when ambiguity is consequential

Invoke `/firm:second-pi` before a tentative explanation hardens when:

- several causal stories remain plausible;
- a simple baseline reverses the narrative;
- the result would change method altitude or contribution identity;
- the next step requires major compute;
- the project may be entering or leaving paper-writing mode.

Provide raw artifacts, the pre-result forecast, contrary evidence, and the method
lineage. Do not supply only a polished preferred interpretation.

## Output

```markdown
# Result Diagnosis

## Evidence status
- Competence/integrity:
- Compared conditions:
- Primary result:
- Important uncertainty:

## What the result establishes

## What it does not establish

## Failure level
- Classification:
- Why this level:
- Why not the next level:

## Competing explanations
| Explanation | Supporting evidence | Contrary evidence | Discriminating test |
|---|---|---|---|

## Design consequence

## Paper consequence

## Highest-value next action
- Experiment or consolidation action:
- Expected information:
- Evidence that would change the decision:
```

Be decisive but calibrated. The output should leave the researcher knowing what
changed, what remains alive, and exactly why the next action is worth doing.
