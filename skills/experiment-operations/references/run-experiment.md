# Run Experiment

Execute a scientifically selected experiment faithfully and durably. The run record
below is the canonical operational identity used by registration, launch, monitoring,
retry, and handoff.

## Canonical Run Record

For every run retain:

- stable run and project IDs, evidence role, and dependency IDs;
- exact command or immutable config and code revision/source snapshot;
- model/checkpoint, data/split, population, seed, treatment, and evaluator identities;
- environment, expected runtime, memory, storage, and authorized compute charge;
- attempt-specific log, result, checkpoint, completion/failure marker, and resume paths;
- actual resource use, protocol deviations, and conclusions those deviations exclude.

Link a main-table run to its existing comparison specification and record the effective
settings, including defaults inherited from loaders, native scripts and evaluators.
Verify the mapping on the real path when it changes. A run can faithfully execute its
own spec and still be outside the main table's conditions; label and deliver that fact
rather than treating a successful exit as authority to fill the cell. The comparison
meaning and permitted method freedoms belong to `research-foundation/references/baseline.md`,
not an automatic allow/deny classifier in the launcher.

For a formal dataset comparison, also retain the official split/eligible-population
identity, expected coverage, actual record identities/counts, and missing or failed
outputs. Apply the full-data policy in `research-foundation/references/baseline.md`:
canaries and partial attempts cannot complete a full-protocol cell. Do not improve a
reported metric by silently dropping failures or changing its denominator.

A debug run may use a compact record. An expensive or claim-defining run also needs the
prospective registration in [research-contract.md](research-contract.md). Never launch
from prose reconstructed from memory.

## Preflight Once, End To End

Before a consequential launch:

1. Resolve the selected experiment plan and current authority; do not launch stale work.
2. Verify that run identity, implementation, comparison, data, evaluator, seed, stopping,
   forecast, and output paths match that plan.
3. Apply [experiment-integrity](../../research-foundation/references/experiment-integrity.md)
   to any information, treatment, statistical, competence, or reconstruction question
   touched by this run rather than duplicating its scientific checks here.
4. Run one small real-path canary. Inspect raw output, component engagement, substrate
   competence, derived metrics, log and result creation, checkpoint/resume behavior,
   runtime, and peak memory.
5. Confirm durable parseable outputs, attempt-specific paths, capacity, and authorized
   compute.

A smoke test proves execution only. If evaluator or implementation repair is still in
progress, label the run as debugging evidence.
Include generation and scoring in the feasibility check, not only training. Establish
their memory, runtime, storage, dependencies, and output semantics before committing
to a campaign whose results depend on them. Reuse completed intermediate artifacts
only after verifying compatibility with the current protocol; an existing failure file
is not a completed cell and must not silently suppress recovery.

Carry the method-specific competence evidence from experiment integrity into the run:
the actual adapted/updated parameters, optimization progress and convergence, selected
checkpoint, and the inference computation used for scoring. Check enough of the native
recipe and affected path to distinguish a design loss from incomplete learning or an
unused treatment. Return an unresolved competence problem for repair, not a leaderboard
number presented as a healthy comparison.

Size accelerator placement from the real-path canary or a closely matched completed
run, current ownership, transient peaks, and a meaningful margin. Do not invent a
universal utilization or free-memory threshold. During method formation, normally run
and read one paired development seed before launching repetitions; never search seeds
for a favorable sign.

Measure useful end-to-end throughput after startup, including data access, generation,
scoring, and output writes. Forecast time to the next interpretable result from that
measurement, not accelerator count. Inspect an unexpectedly slow path for redundant
model loading, serial work, CPU/I/O waits, or synchronization before scaling. Batch,
shard, or overlap independent work when it preserves the comparison; verify the actual
concurrency and throughput after launch. Loading and short CPU phases can be legitimate;
utilization alone neither proves progress nor authorizes terminating a job.

## Launch In The Actual Environment

Read project `CLAUDE.md`, then load only the matching section of
[run-experiment/operations.md](run-experiment/operations.md): local process, direct GPU
over SSH, scheduler, optional queue, GPU sharing, tracking, storage, or recovery.
Project rules override generic mechanics. If essential server information is absent,
ask one focused operational question.

For a campaign whose completeness matters, also read
[run-experiment/campaigns.md](run-experiment/campaigns.md) and use one
`CAMPAIGN_MANIFEST.json`. The manifest tracks execution and artifacts, never scientific
maturity.

Make commands idempotent where practical. A retry must resume a compatible checkpoint
or use a new attempt directory. Keep long jobs detached or scheduler-managed and verify
the registered process/job identity, first real step, log growth, result path, and
checkpoint behavior after launch.

Register long-running jobs in the configured registry when one exists, using scheduler
ID or PID plus start token and command fingerprint. PID, terminal, queue row, or GPU
allocation alone does not prove progress or completion.

Establish the monitor, its recipient, and the resumption mechanism before leaving a
long run unattended, following [monitor-experiment.md](monitor-experiment.md). Account
for shared provider quotas and host capacity when starting concurrent model sessions
as well as experiments; more concurrent agents need not increase research throughput.

## Recover Without Changing The Experiment

OOM, preemption, SSH loss, node failure, disk failure, and missing checkpoints are
operational evidence. Record the observed cause and preserve attempt history. Resume
only when checkpoint run identity, model, optimizer, scaler, step, data order, and
config match; otherwise create a labeled new attempt.

Repair verified implementation, optimizer, evaluator, integration, or placement defects
and validate the repair on the affected path. Retry according to the changed cause,
recoverable work, and authorized cost, not a fixed attempt allowance. Repeating an
unchanged failing command is not recovery. When repairs accumulate, return the actual
cost and remaining obstacle to the PI for an execution decision rather than silently
changing the comparison. Never reinterpret failure-to-run as a scientific result.

Reallocate within authorized project policy. When the selected, preflighted experiment
cannot fit that envelope, return an evidence-grounded resource request to the persistent
PI rather than shrinking the comparison or repeatedly probing unavailable hardware.
The PI asks before exceeding a user-locked budget, permission, or resource boundary.
Pending resources are operational facts, not evidence about the method.

## Validate And Hand Off

Before declaring execution complete, verify the registered identity, terminal evidence,
expected cells, parseable artifacts, actual configuration, and deviations. Deliver the
run record, raw paths, engagement and evaluator evidence, headline values, and unresolved
anomalies to the PI. Distinguish execution completion from evidence validity and PI
interpretation; do not mark unscored or unvalidated work ready for comparison. Only the
PI updates scientific state after reading the evidence.

For a matrix, reconcile completed, partial, incompatible, and unresolved cells with the
chosen comparison plan and its table sources. Explain coverage gaps and preserve the
planned obligation until it is resolved or explicitly revised. A successful run on one
method, backbone, or benchmark cannot stand in for the rest.
If the persistent PI is also the executor, perform this evidence handoff yourself and
continue interpretation; do not wait for a user message to receive your own results.

While a long job runs, advance genuinely useful result-independent work. When nothing
useful remains, a quiet wait is healthier than generating launch paperwork or extra
experiments merely to appear active.
