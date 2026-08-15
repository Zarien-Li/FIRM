---
name: baseline
description: Establishes credible empirical anchors by selecting, reproducing, and behaviorally inspecting strong field-standard baselines.
when_to_use: Use when a project needs benchmark fidelity, a trustworthy comparison, raw failure traces, or proof that an observed result is real enough to support method reasoning.
argument-hint: "[task, benchmark, or baseline]"
---

# Baseline

Use baselines to make contact with the field, not to obtain permission for ideation.

The objective is a trustworthy empirical anchor and enough behavioral evidence to ask a better research question. A reproduction is useful when you understand both its aggregate behavior and where it succeeds or fails.

## Choose Serious Anchors

Prefer:

- benchmarks and protocols commonly used in recent relevant work;
- the strongest reproducible SOTA that fits the project's resources;
- strong simple alternatives a reviewer would immediately request;
- implementations whose semantics can be inspected and extended;
- settings where residual behavior is meaningful rather than pure ceiling noise.

Do not choose a weak, obscure, or convenient baseline to manufacture a win. When code availability forces a substitute, state the difference and what uncertainty it leaves.

Choose and record an accepted benchmark or natural workflow as the anchor for each
central claim. Derived datasets, generated examples, synthetic corruptions, oracle
slices, and project-defined subsets must be labeled `training` or `diagnostic` unless
their claim-bearing status is independently justified. They may expose a mechanism or
train a component, but faster feedback or larger gains do not let them silently replace
the anchor.

Literature and leaderboards help identify candidates. Actual selection should also consider implementation health, evaluation comparability, compute, and whether per-example outputs can be inspected.

## Reproduce With Semantic Fidelity

Before trusting a result, establish:

- the intended dataset, split, preprocessing, and candidate pool;
- the actual checkpoint, prompt, decoding, stopping, and tool protocol;
- the original decision rule, objective, thresholds, and filtering;
- the evaluator, parser, metric definition, and metric direction;
- the information, supervision, labels, tools, and external computation available to every compared system;
- whether a direct deterministic, algorithmic, retrieval, or other simple procedure already performs the claimed operation;
- the expected resource regime and any meaningful deviations.

Run a small end-to-end sanity case first. Include at least one known success and one known failure when possible. Check that the evaluator can distinguish them.

Treat these as evidence-integrity failures, not scientific results:

- wrong data path or silent fallback data;
- parser or token-position mistakes;
- label leakage or circular gold construction;
- metric direction or aggregation errors;
- baseline behavior changed by local convenience edits;
- truncation, filtering, or caps that alter the task;
- endpoint or checkpoint mismatch;
- suspiciously large deltas before raw-output inspection.

If an integrity issue is repaired after results exist, mark affected conclusions invalidated or requiring rerun. Do not silently carry them forward.

Perform this semantic check before a result becomes the premise of a substantial method contract or full paper draft. After the central semantics are established, do not repeatedly reaudit them without a concrete anomaly; move on to explanation and method development.

## Read Behavior, Not Only Scores

Save and inspect representative examples:

- failures;
- successes for contrast;
- disagreements between baselines;
- cases that contradict the leading story;
- examples near decision boundaries;
- artifacts, abstentions, crashes, and truncations.

Preserve task-relevant traces such as inputs, outputs, scores, retrievals, tool calls, intermediate states, latency, cost, and metadata needed for slicing.

Do not declare reproduction complete merely because one headline number matches. The research value often lies in the structure of the residual errors.

Read residuals with both explanatory and value lenses. Record whether a candidate failure cluster has natural support, meaningful severity, and presence across systems people actually use. Do not assume that a clean residual inherits the benchmark's overall importance. A rare residual may be a diagnostic microscope; look for the broader design assumption it reveals before making it the research destination.

## Build Coverage Adaptively

Do not impose a universal requirement to finish every conceivable baseline before thinking. Start with the anchor that gives the strongest information, inspect its behavior, and let live uncertainties determine the next comparison.

Add another baseline, dataset, model, seed, or regime when it answers a concrete question such as:

- Is the phenomenon specific to one implementation?
- Is the simple alternative already sufficient?
- Does the effect survive a realistic scale or distribution change?
- Is a claimed mechanism actually generic?
- Does the apparent improvement trade away utility or coverage?

Continue until the evidence is adequate for the current decision. Record what remains unrun so later claims stay scoped.

## Use Existing Evidence

When valid local results already exist, do not rerun them ceremonially. Audit their provenance, inspect raw outputs, and reuse them. Repair only the uncertain parts.

When a baseline has been modified for instrumentation or compatibility, demonstrate that the modification preserves its semantics before treating it as the same baseline.

## Output

Maintain `BASELINE_REPRO.md` or the project's existing baseline record with:

```markdown
# Baseline Evidence

## Empirical Surface
- task, benchmark, split, metrics:
- why this surface is field-relevant:
- information and supervision budget for each comparison:
- strongest direct or deterministic alternative:

## Anchors
| System | Source/version | Intended protocol | Actual protocol | Health | Result path |
|---|---|---|---|---|---|

## Integrity Checks
- data and split:
- evaluator/parser:
- baseline semantics:
- leakage/artifact checks:
- deviations and consequences:

## Behavioral Reading
- representative failures:
- successes for contrast:
- disagreements and inconvenient cases:
- provisional clusters:
- natural support, severity, and affected systems for promising clusters:

## Current Research Consequence
- what is now credible:
- what remains uncertain:
- best next empirical question:
```

Keep raw logs and results at durable paths. The report should interpret them without replacing them.

## Continue The Same Researcher

Use `diagnose-result` when raw behavior needs contrastive organization, artifact removal, or competing explanations. Return here whenever a later hypothesis exposes a missing anchor or integrity concern. This is not a stage handoff: the same researcher retains the thesis and reads only the additional evidence needed for the live question.
