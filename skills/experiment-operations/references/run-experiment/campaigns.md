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
