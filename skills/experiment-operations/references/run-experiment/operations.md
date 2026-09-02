# Environment-Specific Operations

Load only the section matching the project's real environment. The canonical record,
preflight, recovery, and handoff remain in [run-experiment.md](../run-experiment.md).

## Local Process

Use the existing project environment and launcher. Verify a real step and interruption
behavior before detaching a long run. For an unmanaged process, add PID, start token,
command fingerprint, cwd, and log path to the run record; PID alone is not durable
identity. Use an existing process manager or registry when configured rather than an
open terminal as the liveness mechanism.

## Direct GPU Over SSH

Verify host identity, project path, environment, synced code/data, free storage, and
checkpoint destination. Inspect current GPU processes, memory, utilization, and
ownership, then bind only an allowed device using peak memory measured by the canonical
canary. Launch through the project's durable mechanism and verify the remote identity,
log growth, and first real step.

Use only the project's authorized synchronization method and inspect the resulting
diff. Do not stage, commit, or push unrelated work as a launch side effect. SSH loss is
not job failure; reconnect and reconcile process identity and artifacts.

## Slurm Or Managed Scheduler

Use the configured scheduler. Do not pin physical GPU IDs, train on a login node, or
bypass scheduler ownership. Record the scheduler ID, script/config hash, resources,
dependencies, output/error paths, and final accounting state. Acceptance into a queue
does not prove execution; verify running state and a real step.

A resource-only change may be a new attempt under the same run when method, data,
comparison, seed, and evaluator remain unchanged. Preserve the reason and accounting.

## Optional FIRM Or Batch Queue

Use this section only when the project actually configures such a queue. Submit a fully
specified, idempotent command through its installed interface and record the run and
dependency IDs. A claimed wait is real only when the exact registry/queue identity or
an independently verified worker exists.

On delivery, match project, run, attempt, and command fingerprint; inspect the result
before research-state updates; and keep transport or placement failures operational.
Do not invent private queue commands or schemas. If the queue is absent, use another
already authorized execution path; report the missing dependency only when none exists.

## GPU Sharing And Memory Safety

Share a device only when project and scheduler policy allow it. Account for model,
optimizer, activations, dataloader, compilation, evaluation, checkpoint, transfer,
fragmentation, and other processes that may grow. Decide from measured peaks and a
meaningful margin, not a universal free-memory or utilization threshold.

After launch, verify actual memory and first-step stability. Treat OOM from placement
or transient collision as an operational cause and change that cause before retrying.
Serialize or move jobs when safe headroom cannot be established.

## Tracking And Credentials

Use existing tracking when it improves diagnosis or reproduction. Local machine-readable
results remain authoritative during a tracking outage.

Never put keys or tokens in project instructions, source, configs, logs, prompts, or
shell history. Use an authenticated client, approved secret store, keychain, or
ephemeral injection without echoing secrets. Missing credentials require their owner
or configured provider.

## Storage And Cleanup

Check expected output size and destination capacity. Preserve claim-bearing raw
outputs, configs, evaluator identity, summaries, and checkpoints needed for recovery or
verification.

Before destructive cache, model, dataset, checkpoint, or remote-artifact cleanup,
produce a size/provenance inventory and obtain explicit user approval. Prefer
reproducible public caches as candidates, but never assume they are safe to remove.
