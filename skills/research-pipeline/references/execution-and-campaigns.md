# Execution And Campaigns

Use this reference for claim-bearing run bundles, bounded delegation, completion
reconciliation, and recovery after interruption. It governs operational truth, not
scientific judgment.

## Prepare Before Occupying Accelerators

Finish dependencies, downloads, preprocessing, evaluator construction, configuration,
and a meaningful real-path smoke test before accelerator launch when feasible. Estimate
memory and placement from a real canary or a closely matched completed run. The launch
command should expose progress, write durable logs, preserve raw predictions, and place
completion evidence in an attempt-specific output directory.

Infrastructure failure, queue delay, SSH loss, preemption, and implementation failure
are not scientific outcomes. Preserve enough identity to resume or rerun without
attaching partial output to a claim.

## Manifest Only Mechanical Truth

For a multi-run comparison, maintain one `CAMPAIGN_MANIFEST.json` containing:

- campaign and project identity;
- the expected experimental cells and their scientific comparison labels;
- immutable run fingerprint and exact command/config identity;
- attempt identity, host or scheduler identity, and start/end timestamps;
- attempt-specific log, artifact, checkpoint, and terminal-marker paths;
- mechanical disposition such as unclaimed, active, completed, or failed;
- validation that required artifacts and the terminal marker belong to that attempt.

Use atomic claims or a lock so two workers cannot run the same cell. Never borrow a
completion marker or result from an older output directory. A rerun creates a new
attempt while preserving prior evidence.

These dispositions exist only to coordinate execution. The manifest may say how many
expected cells have valid outputs. It cannot label a method successful, a result
decisive, a candidate mature, or a paper ready. The GPT PI reads completed artifacts and
writes their scientific meaning in the sole project state.

## Reconcile Before Interpretation

Compare registry identity, process or scheduler state, logs, terminal markers, expected
row counts, raw prediction files, and evaluator output. Distinguish ongoing execution,
valid completion, incomplete output, identity ambiguity, and completed evidence not yet
interpreted by the PI. These are factual descriptions rather than a scientific taxonomy.

Do not infer completion from a silent terminal, GPU memory, an old checkpoint, or a
session summary. Do not infer failure from temporary zero utilization during a known
loading or CPU preprocessing interval; use command-specific progress and logs.

## Allocate Repetition For A Scientific Reason

Seeds and repeated cells answer uncertainty questions. Use them to estimate stochastic
variation, stabilize a coherent positive effect, or support the reliability required by
the claim. A competent paired negative result first deserves diagnosis of the design,
implementation, and evaluator; additional seeds should not serve as a lottery for a
positive sign.

Run ordering remains adaptive. Prioritize comparisons that can change the method or
paper decision, while allowing independent preparation to proceed during long jobs.
