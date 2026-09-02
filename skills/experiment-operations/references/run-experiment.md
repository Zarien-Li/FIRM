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

Size accelerator placement from the real-path canary or a closely matched completed
run, current ownership, transient peaks, and a meaningful margin. Do not invent a
universal utilization or free-memory threshold. During method formation, normally run
and read one paired development seed before launching repetitions; never search seeds
for a favorable sign.

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

## Recover Without Changing The Experiment

OOM, preemption, SSH loss, node failure, disk failure, and missing checkpoints are
operational evidence. Record the observed cause and preserve attempt history. Resume
only when checkpoint run identity, model, optimizer, scaler, step, data order, and
config match; otherwise create a labeled new attempt.

A verified implementation, optimizer, evaluator, integration, or placement defect
normally earns one clean matched retry. If the same directional or operational failure
remains, do not launch an identical or nearby attempt without a changed cause or
load-bearing prediction supplied by the PI. Never reinterpret failure-to-run as a
scientific result.

Reallocate within authorized project policy. When the selected, preflighted experiment
cannot fit that envelope, return an evidence-grounded resource request to the persistent
PI rather than shrinking the comparison or repeatedly probing unavailable hardware.
The PI asks before exceeding a user-locked budget, permission, or resource boundary.
Pending resources are operational facts, not evidence about the method.

## Validate And Hand Off

Before declaring execution complete, verify the registered identity, terminal evidence,
expected cells, parseable artifacts, actual configuration, and deviations. Deliver the
run record, raw paths, and uninterpreted headline values to the PI; only the PI updates
scientific state after reading them.

While a long job runs, advance genuinely useful result-independent work. When nothing
useful remains, a quiet wait is healthier than generating launch paperwork or extra
experiments merely to appear active.
