# Experiment Operations

Load only the section matching the project's real execution environment. This reference
owns reliable execution mechanics; scientific selection remains in `run-experiment`
and `experiment-plan`.

## Common Run Record

Before launch, create or update one compact run record containing:

- stable run ID, project ID, evidence role, and dependency run IDs;
- exact command or immutable config path;
- code revision or source snapshot and local modifications;
- dataset, split, checkpoint, seed, evaluator, and environment identifiers;
- expected runtime, memory, storage, and authorized compute charge;
- log, result, checkpoint, completion, failure, and resume paths.

A debug or smoke run may use a short record. A claim-bearing run needs a frozen
forecast and matched comparison. Never launch from prose reconstructed from memory.

Make the command idempotent where practical. A retry must either resume a verified
checkpoint or write to an attempt-specific path. Never silently mix partial outputs.

## Local Process

Use the project's existing environment and launcher. Verify a real step, log creation,
result path, and interrupt/resume behavior before detaching a long run.

For an unmanaged process, record PID, process start token, command fingerprint, cwd,
and log path. PID alone is not durable identity. Use the host's configured process
manager or FIRM registry when available; do not keep a terminal open merely as a
liveness mechanism.

## Direct GPU Over SSH

Before launch:

1. verify host identity, project path, environment, code/data version, free storage,
   and checkpoint destination;
2. inspect current GPU processes, memory use, utilization, and project ownership;
3. estimate this run's peak memory from a real step or a closely matched completed run;
4. select only a device allowed by project policy and record the binding;
5. launch through the project's durable process mechanism and verify the remote PID,
   start token, command fingerprint, log growth, and first real step.

Do not transfer code by committing or pushing unrelated work. Use the project's
authorized sync method and inspect the resulting diff. Never stage an entire working
tree, create a commit, or push merely as an experiment-launch side effect.

SSH loss is not job failure. Reconnect and verify process identity plus artifacts.

## Slurm Or Managed Scheduler

Use the configured scheduler for resource allocation. Do not pin physical GPU IDs,
train on a login node, or bypass scheduler ownership.

Record scheduler job ID, submitted script/config hash, requested resources,
dependencies, output/error paths, and final accounting state. Scheduler acceptance is
not proof of execution; verify transition to running and the first real step.

Retry preemption or node failure according to scheduler policy. A changed resource
request is a new attempt under the same scientific run only when method, data,
comparison, seed, and evaluator remain unchanged.

## FIRM Or Batch Queue

FIRM is an operational fact and durable-delivery plane. Submit only a fully specified,
idempotent command through the currently installed queue interface. Record its exact
run ID and dependency IDs in the authoritative state.

Accept `WAITING_FOR_JOB` only when the registry contains that exact pending/running
run or an independently verified process exists. A card, terminal message, or stale
marker is not a live job.

On delivery:

- verify event project ID, run ID, attempt, command fingerprint, and terminal state;
- inspect the decisive log/result artifact before updating research state;
- classify queue, placement, transport, disk, and provider failures as operational;
- submit dependent waves only after prerequisites are valid and read.

Do not invent queue scripts, private ARIS commands, delivery schemas, or retry loops.
If the configured interface is missing, report the missing operational dependency
instead of replacing it with an ad hoc daemon.

## GPU Sharing And Memory Safety

Multiple processes may share a GPU when project and scheduler policy allow it. Decide
from measured peak allocation, current process ownership, allocator behavior, and a
meaningful safety margin; do not use a universal free-memory threshold.

Before co-location, account for:

- model, optimizer, activations, dataloader, compilation, and evaluation peaks;
- temporary `model.to`, checkpoint save/load, and validation spikes;
- fragmentation and other processes whose usage may grow;
- whether either job is latency-sensitive or uses exclusive collectives.

If safe headroom cannot be established, serialize the jobs or request a different
device. After launch, verify actual memory and first-step stability. An OOM caused by
placement or transient collision is operational evidence. Retry only after identifying
and changing the operational cause; repeated identical blind resubmission is not a
policy.

## Tracking And Credentials

Use existing project tracking when it helps diagnose or reproduce a run. Log the run
ID, configuration, primary and utility metrics, resource use, and artifact locations.

Never place API keys or tokens in `CLAUDE.md`, source files, configs, logs, prompts,
or shell history. Use an already authenticated client, OS keychain, approved secret
store, or ephemeral environment injection. Do not echo secrets. Missing credentials
require the project owner or configured credential provider.

A tracking outage must not destroy local evidence. Write durable local logs and
machine-readable results first; sync tracking later if useful.

## Storage And Cleanup

Check expected output size and destination capacity before launch. Keep claim-bearing
raw outputs, configs, evaluator versions, summary results, and necessary checkpoints.

Cache cleanup, model deletion, dataset deletion, checkpoint pruning, and remote
artifact removal are destructive operations. Produce a size/provenance inventory and
obtain explicit user approval before deletion. Prefer reproducible caches and
downloadable public assets as cleanup candidates, but never assume they are safe to
remove.

## Failure And Resume

Classify the observed failure before acting:

- configuration/code/data/evaluator defect;
- OOM or resource placement;
- preemption or scheduler/node failure;
- SSH/transport/provider failure;
- storage/quota failure;
- unknown.

Preserve the failed attempt, root-cause evidence, and affected claim scope. A verified
repair normally earns one clean retry. If the same failure recurs, stop blind retries
and escalate the unresolved operational cause. Never reinterpret failure-to-run as a
scientific negative.

Resume only from a checkpoint whose run identity, step, optimizer state, data order,
and config match. Otherwise start a labeled new attempt.

## Completion Handoff

A run is `completed_unread` only when terminal state, expected outputs, parseability,
and provenance are verified. Report:

- run and attempt IDs;
- actual host/device or scheduler identity;
- exact config/command and revision;
- result, log, checkpoint, and marker paths;
- actual resource use and deviations;
- failures/retries and their causes.

Then hand the artifacts to `signal-analysis`. Execution code does not mark a result
`interpreted` and does not decide the scientific route.
