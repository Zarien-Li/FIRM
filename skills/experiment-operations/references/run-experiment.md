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

1. Read current authority and unread results; confirm that the run still answers a
   live scientific question.
2. Reconcile disagreements among state, tracker, code, tasks, and manuscript from raw
   artifacts.
3. Verify the intended method and matched comparator, accepted population, treatment,
   metric direction, evaluator entrypoint, scale, seed, stopping, and forecast.
4. Confirm that every method-visible input is available at decision time. Test, future,
   target, cache, and external information must respect the declared boundary.
5. For a claim-bearing method comparison, include the decisive published incumbent
   and claim-threatening published rival required by the claim.
6. Run one small real-path canary. Inspect raw output, component engagement, substrate
   competence, derived metrics, log and result creation, checkpoint/resume behavior,
   runtime, and peak memory.
7. Confirm durable parseable outputs, attempt-specific paths, capacity, and authorized
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
load-bearing prediction. Never reinterpret failure-to-run as a scientific result.

Reallocate within authorized project policy. Ask only before exceeding a user-locked
budget, permission, or resource boundary.

## Validate And Hand Off

Before declaring execution complete, verify terminal evidence, expected cells,
parseable artifacts, provenance, actual scale/configuration, and material deviations.
Then provide the PI with the run record plus raw result paths and headline values,
without scientific interpretation. Update authoritative research state only after the
PI reads the evidence.

While a long job runs, advance genuinely useful result-independent work. When nothing
useful remains, a quiet wait is healthier than generating launch paperwork or extra
experiments merely to appear active.
