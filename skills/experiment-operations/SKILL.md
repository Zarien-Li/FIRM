---
name: experiment-operations
description: Register, launch, resume, monitor, reconcile, and hand off local or remote research experiments with durable commands, manifests, logs, artifacts, completion evidence, and resource discipline. Use after the scientific question and comparison have been selected.
---

# Experiment Operations

Own execution truth, not scientific direction. Every registration, launch, retry,
monitoring event, and handoff for a run shares one identity and artifact chain.

## Route The Work

- For prospective registration of a consequential or expensive run, read
  [research-contract.md](references/research-contract.md).
- For the canonical preflight, run record, launch, recovery, and handoff lifecycle, read
  [run-experiment.md](references/run-experiment.md). Load environment-specific detail
  only when needed from
  [operations.md](references/run-experiment/operations.md).
- For a multi-run campaign, read
  [campaigns.md](references/run-experiment/campaigns.md) and use
  `scripts/campaign_manifest.py` when its mechanical manifest is appropriate.
- For factual process/log/artifact reconciliation, especially after interruption, read
  [monitor-experiment.md](references/monitor-experiment.md).

Mechanical records establish what ran and what artifacts completed. The PI interprets
what those artifacts mean.
