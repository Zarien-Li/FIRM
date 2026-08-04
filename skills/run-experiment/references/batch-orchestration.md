# Batch orchestration

Use a manifest rather than generating an opaque shell loop.

```yaml
experiment: exp-017
max_concurrent: 2
failure_policy: continue-independent
jobs:
  - id: seed-1
    command: python train.py --seed 1
    output: runs/exp-017/seed-1
    depends_on: []
  - id: seed-2
    command: python train.py --seed 2
    output: runs/exp-017/seed-2
    depends_on: []
```

For each job, track:

- `PENDING`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCELLED`, or `BLOCKED`;
- scheduler/PID/session ID;
- attempts and exact reason for retry;
- output and checkpoint paths;
- deviations from the manifest.

## Rules

- enforce the declared concurrency and resource limits;
- do not launch downstream jobs before dependencies produce valid artifacts;
- stop duplicate jobs by checking durable IDs and outputs;
- distinguish transient infrastructure failure from scientific failure;
- keep failed outputs rather than overwriting them;
- aggregate only compatible runs;
- do not add seeds post hoc solely to search for a favorable result.

A wave transition should be triggered by an explicit scientific or operational
condition, not by a hidden ad hoc decision in the launcher.
