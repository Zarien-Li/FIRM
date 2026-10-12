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

## Establish Observation And Receipt

Choose the observation mechanism from the actual runtime. Prefer scheduler completion
events, a durable local watcher, or a supported task notification. A watcher that writes
a file cannot by itself wake a model session. Identify the receiving session and how it
will notice the event, and verify delivery on the real path before relying on it. Reuse
one monitor per job or campaign instead of starting a new one on each conversation turn.

When no event channel exists, use bounded status checks spaced according to expected
progress, costs, and platform limits. Keep the parent active through the supported wait
mechanism when possible. If the session cannot wait or resume automatically, preserve
the completion location and exact recovery action and report that limitation. Do not
promise background follow-up, invent a timer, or spin a long SSH/sleep loop as a wakeup
mechanism. Do not create recurring automation without the user's authorization.

Monitor both useful job progress and observation health. If expected evidence stops
arriving or the observer disconnects, reconnect and reconcile before declaring the job
stalled or completed. A timeout should reflect this job's expected next observable
progress, including legitimate loading or phases that only write at completion; it
does not authorize killing an unknown process. Refresh forecasts when measured
throughput or the bottleneck changes materially.

## Recover After Interruption

After host power loss or session restart, treat local process and queue facts as stale
until rediscovered. Reconcile the current process set, cwd, terminal tail, registry or
queue identity, exact worker, and freshest artifact.

A remote worker may outlive its local session. If the registered process still runs,
restore monitoring without resubmitting. If it vanished, reconstruct the cause and
resume only from a checkpoint compatible with the frozen run. Before a replacement,
exclude a duplicate live execution, establish what makes recovery viable, and preserve
and link the old attempt. Repeated interruptions call for diagnosis and a cost-aware
recovery decision, not an arbitrary retry cap. A stale heartbeat or registry row alone
is insufficient evidence.

For provider quota exhaustion, authentication loss, or a suspended parent session,
preserve the next action and any surviving job separately from the conversation state.
Use a documented reset time or supported retry mechanism when available. Do not open
replacement sessions against the same exhausted quota or assume that all remote jobs
died with the parent. On return, first consume completed results and reconcile partial
attempts before allocating more work. Report an unavailable wakeup or credential as an
operational dependency with a concrete recovery path.

## Validate And Deliver Once

Validate the registered identity and completion requirements in
[run-experiment.md](run-experiment.md), including expected and missing cells, parsed
metrics, deviations, retries, runtime, cost, and raw outputs needed for independent
reading. Deliver one compact evidence bundle with those facts and durable paths; do not
repeat long logs or add scientific interpretation.

Notify the research session when validated results are ready, execution needs repair,
or an unresolved resource conflict requires action. Record the event identity and its
receipt in the existing run record or supported delivery system. Distinguish an event
written, notification sent, and receipt confirmed; a failed or unacknowledged delivery
is retried idempotently or reconciled on resume, not marked handled and forgotten. The
PI reads and interprets the bundle and owns concise user-facing progress. Keep unchanged
monitoring chatter out of the conversation; long logs remain at their paths.
