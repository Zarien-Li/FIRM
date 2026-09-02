# Monitor Experiment

Use to reconcile a registered run with real processes, logs, outputs, and termination
evidence. Start from the canonical run record in
[run-experiment.md](run-experiment.md), not a terminal title, PID, GPU allocation, or
session summary.

## Reconstruct Current Facts

Resolve the run and project IDs, host/environment, scheduler ID or process identity,
PID start token and command fingerprint when unmanaged, config and command, expected
cells and dependencies, and all artifact paths. If identity is incomplete, repair the
record before attaching outputs to a project.

Inspect only the execution mechanism actually used. Build one timestamped account of:

- whether a declared dependency or resource remains unresolved;
- whether the matching process or scheduler job exists and makes progress;
- whether the intended protocol and scale actually ran;
- whether expected outputs parse and terminal evidence is clean;
- whether execution stalled, vanished, completed, or was explicitly cancelled.

Process exit is not completion, and a live PID is not progress. Use log movement,
scheduler facts, output parsing, completion markers, and actual configuration to
distinguish healthy waiting from an operational stall. These observations do not choose
a scientific response by status label.

## Recover After Interruption

After host power loss or session restart, treat local process and queue facts as stale
until rediscovered. Reconcile the current process set, cwd, terminal tail, registry or
queue identity, exact worker, and freshest artifact.

A remote worker may outlive its local session. If the registered process still runs,
restore monitoring without resubmitting. If it vanished, reconstruct the cause and
resume only from a checkpoint compatible with the frozen run. Create at most one
replacement for an ordinary recoverable interruption, preserving and linking the old
attempt. A stale heartbeat or registry row alone is insufficient evidence.

## Validate And Deliver Once

Before handoff, verify correspondence with registered code, data, checkpoint,
population, seed, steps, treatment, and evaluator; expected and missing cells; parsed
metrics without unexplained NaNs, empty populations, constants, or impossible values;
resource use and retries; and raw predictions or sufficient statistics needed for
independent reading.

Describe every substitution, shortening, or deviation and which comparisons it cannot
support. Then deliver one compact evidence bundle containing canonical run/attempt
identity, config and provenance, raw result and prediction paths, logs/checkpoints/
markers, completed and missing cells, uninterpreted headline values, deviations,
warnings, retries, runtime, and cost.

Notify the research session when validated results are ready, execution needs repair,
or an unresolved resource conflict requires action. Keep healthy progress quiet. Record
delivery with a durable event ID and never redeliver the same completion event. The PI
reads and interprets the bundle; long logs remain at their paths.
