# Reliable Multi-Run Campaigns

Use this reference when several cells, workers, baselines, datasets, models, or seeds
must form one evidence envelope. It owns mechanics only. Scientific interpretation
remains in `PROJECT_STATE.md` and raw analysis.

## One Mechanical Manifest

Create `CAMPAIGN_MANIFEST.json` beside the campaign launcher. It contains:

```json
{
  "schemaVersion": 1,
  "campaignId": "stable-name",
  "scientificQuestion": "one question this matrix answers",
  "protocol": {
    "codeRevision": "revision-or-source-hash",
    "dataId": "dataset-and-split-id",
    "evaluatorId": "evaluator-version-or-hash",
    "informationBoundaryId": "run-contract-or-hash"
  },
  "cells": [
    {
      "cellId": "unique-semantic-cell",
      "fingerprint": "hash-of-method-surface-model-seed-and-frozen-config",
      "purpose": "free-text reason this cell matters to the current comparison",
      "method": "published-or-project-method",
      "surface": "accepted-surface",
      "model": "model-id",
      "seed": 0,
      "dependencies": [],
      "status": "planned",
      "attempts": []
    }
  ]
}
```

Statuses are execution facts, not scientific stages. A cell is complete only when its
latest attempt records an exact run ID, command/config identity, durable artifacts, and
a validated terminal marker. Metrics may live in the result artifact; interpretation
does not belong in the manifest.

## Concurrency Invariants

- Claim a cell with an atomic lock or scheduler/database transaction. Reading `planned`
  and writing `running` in separate unprotected operations is invalid.
- Derive one immutable fingerprint from every input that changes the comparison. Reject
  duplicate fingerprints unless the cells are declared repetitions with distinct seeds.
- Give every attempt a new output directory. Never let retries, workers, or methods
  share a writable result path.
- Recheck dependencies and the shared manifest immediately before launch. Fixed shards
  may seed work, but idle workers should claim globally available cells.
- Write the terminal marker only after the process exits successfully and expected
  outputs parse. A log ending, absent PID, or controller exit is not completion.
- Resume only when model, optimizer, scheduler, scaler, step, data order, and frozen
  config are compatible. Otherwise create a labeled new attempt.
- Never auto-requeue an unknown or stale attempt. Verify process identity and artifacts,
  then explicitly release or requeue it while preserving attempt history.
- Check destination capacity before the campaign and account for caches, checkpoints,
  raw predictions, temporary saves, and concurrent writers.

## Bundled Helper

`scripts/campaign_manifest.py` provides POSIX file-locking, atomic replacement,
validation, summary, claim, start, complete, fail, and explicit requeue operations for
a manifest on a shared filesystem. Run it on the host that can see the output marker.
Use scheduler-native transactions instead when the filesystem does not provide reliable
advisory locks.

The project launcher remains responsible for the actual training command. It receives
the claimed cell, writes the exact command/config into the attempt directory, starts the
process, and calls `complete` only after validating outputs. The helper never chooses a
cell for scientific reasons and never updates research maturity.
