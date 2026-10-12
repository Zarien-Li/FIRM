# Reliable Multi-Run Campaigns

Use when several cells, workers, baselines, datasets, models, or seeds form one evidence
envelope. Keep scientific interpretation in `PROJECT_STATE.md`; the campaign manifest
records execution only.

## One Mechanical Manifest

Create `CAMPAIGN_MANIFEST.json` beside the launcher. Use
[`campaign_manifest.py`](../../scripts/campaign_manifest.py) and its validator as the
schema authority. Use its `--help` for commands. The
manifest identifies the campaign and frozen protocol, then records each semantic cell's
ID, immutable fingerprint, purpose, method, surface, model, seed, dependencies,
mechanical status, claim, and attempt history.

A completed cell must identify its exact run and command/config, attempt-specific
artifacts, and validated terminal marker. Metrics may live in artifacts; interpretation
does not belong in the manifest. The script's statuses coordinate execution and carry
no scientific authority.

## Concurrency Invariants

For a selected field matrix, provide one documented command that can run or resume
the campaign from its manifest, using the existing project environment and authorized
workers. Worker IDs and resource envelopes come from current project authority, not
examples in this skill. The command should perform missing work and report unresolved
cells; neither a successful launcher exit nor partial outputs mean the matrix completed.

On a limited authorized canary allocation, exercise every distinct method, backbone,
data/evaluator, and launch path whose differences could cause a cell to fail. Reuse
coverage where the execution path is genuinely shared and explain its boundary. Check
actual component engagement, predictions, scoring, output identity, and resumability;
one generic forward pass cannot certify every baseline. Canary outputs remain separate
from full-protocol comparison results. A canary reduces risk, not a guarantee of no bugs.

Schedule independent ready cells concurrently using measured memory peaks and end-to-end
throughput. Multiple processes on one device are appropriate only when authorized and
their combined transient peaks, CPU/RAM, I/O, and scoring demands fit; measure whether
co-location improves useful throughput rather than merely increasing process count.
Keep semantically dependent work ordered. Do not occupy the full allocation while
downloads, installations, or shared preprocessing that can run elsewhere remain undone.

Validate concurrency on the actual workers: distinct claimed cells must be making real
progress, not only have live PIDs. Measure sustained throughput after startup and inspect
serial model loading, tokenization, data access, synchronization, and scoring bottlenecks.
Optimize these before scaling. A requested high GPU-utilization target motivates tuning,
but neither a universal 90% floor nor a sampled peak establishes execution quality.
Preserve numerical and protocol equivalence through performance changes and refresh
forecasts from measured progress.

- Claim a cell atomically through the helper or scheduler/database transaction.
- Fingerprint every comparison-changing input. Reject duplicate fingerprints unless
  cells are declared repetitions with distinct seeds.
- Give every attempt a new writable directory; never mix retries or workers.
- Recheck dependencies and the shared manifest immediately before launch. Workers may
  claim any globally ready cell rather than trusting stale fixed shards.
- Publish completion only after successful exit, output parsing, and marker validation.
- Resume only from a checkpoint compatible with the canonical run identity.
- Reconcile an unknown or stale attempt before explicitly requeueing it; preserve its
  history.
- Check destination capacity for caches, predictions, checkpoints, temporary saves,
  and concurrent writers.

The launcher owns the actual experiment command. It claims a cell, records the exact
command/config in the attempt directory, launches it, and calls `complete` only after
validation. Use scheduler-native transactions when shared storage does not support
reliable POSIX advisory locking.
