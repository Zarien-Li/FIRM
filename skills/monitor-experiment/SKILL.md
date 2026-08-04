---
name: monitor-experiment
description: Checks running experiments, collects logs and result files, and summarizes progress without inventing missing outcomes.
when_to_use: Invoke explicitly to inspect local, screen, Slurm, SSH, or W&B jobs and connect completed outputs back to the research state.
argument-hint: "[job, server, or result path]"
disable-model-invocation: true
---

# Monitor an Experiment

Inspect the requested jobs and return an evidence-linked status. Monitoring is
read-oriented: do not restart, cancel, delete, or modify jobs unless the user
explicitly requests that action after the diagnosis.

## 1. Recover durable job identity

Read the launch record, tracker, scheduler ID, PID/session name, host, working
directory, log path, checkpoint path, and expected result path. On shared servers,
attribute jobs by project path and command, not only by Linux username or container
name.

If the requested job cannot be uniquely identified, show the plausible candidates
and the evidence needed to distinguish them. Do not attach another researcher's
process to the project.

## 2. Inspect runtime status

Use the runtime that actually launched the job:

- local PID/process manager;
- `tmux` or `screen` session;
- Slurm queue and accounting;
- remote process over an already authorized SSH connection;
- W&B or another tracker configured by the project.

Collect:

- current state and elapsed time;
- latest meaningful log lines;
- step/epoch/progress indicator;
- recent loss or task metrics when available;
- GPU memory/utilization and obvious stalls;
- checkpoint creation and freshness;
- errors, preemption, OOM, disk, or evaluator failures;
- final result file existence and parseability.

Do not dump large raw logs into the main response. Read enough context around the
first causal error and preserve exact paths for deeper inspection.

## 3. Classify the status

Use one of:

- `RUNNING_HEALTHY`;
- `RUNNING_SLOW_OR_UNCERTAIN`;
- `STALLED`;
- `FAILED_INFRASTRUCTURE`;
- `FAILED_EXPERIMENT`;
- `PREEMPTED_RESUMABLE`;
- `COMPLETED_UNVERIFIED`;
- `COMPLETED_VALID`;
- `NOT_FOUND`;
- `AMBIGUOUS_IDENTITY`.

A process exit with a file present is not automatically a valid completion. Check
that the expected evaluator ran and the result corresponds to the requested config.

## 4. Decide the operational next step

Recommend exactly one of:

- continue monitoring;
- inspect a named error or artifact;
- resume from a verified checkpoint;
- repair and relaunch under `/firm:run-experiment`;
- collect completed outputs for `/firm:diagnose-result`;
- ask the user before cancellation or another irreversible action.

Do not change scientific parameters under the label “resume.” If a batch size,
precision, seed, data, evaluator, or model changes, record it as a new run or an
explicit deviation.

## 5. Return a concise report

```markdown
# Experiment Status

- Experiment/job ID:
- Project path:
- Runtime and host:
- Status:
- Elapsed/progress:
- Latest meaningful evidence:
- GPU/resource state:
- Checkpoint:
- Result artifact:
- Error or uncertainty:
- Recommended next action:
- Exact command or path for the next inspection:
```

For multiple jobs, add a compact table and expand only failed or decision-relevant
cases. Once valid results exist, hand them to `/firm:diagnose-result`; monitoring
itself should not make the scientific claim.
