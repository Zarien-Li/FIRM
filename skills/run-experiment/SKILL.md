---
name: run-experiment
description: Launches ML experiments locally or on remote GPU servers, including single jobs, Slurm runs, queued sweeps, retries, and resume workflows.
when_to_use: Invoke explicitly only after the command, environment, output path, budget, and safety constraints are known. It can write files, use compute, and contact remote systems.
argument-hint: "[command, manifest, or experiment plan]"
disable-model-invocation: true
---

# Run an Experiment

Launch the requested experiment reproducibly and safely. This skill may consume
compute, write project files, or contact remote systems, so act only within the
explicitly established environment, budget, and access.

## 1. Recover the run contract

Read `$ARGUMENTS`, the experiment plan or registration, project instructions, and
existing run scripts. Resolve:

- scientific purpose and experiment ID;
- exact command and working directory;
- code revision and uncommitted changes;
- dataset, checkpoint, config, and seed;
- local, SSH, Slurm, or another declared scheduler;
- environment or container;
- GPU, CPU, memory, time, and monetary budget;
- durable log, checkpoint, and result paths;
- success/failure indicator and monitoring method;
- retry and resume policy.

If a field required for safe launch is unknown, ask only for that field. Do not
invent hostnames, credentials, paths, queues, or budgets.

For expensive or claim-defining runs, use `/firm:register-experiment` before launch.

## 2. Preflight without changing the system

Check:

- current git status and code revision;
- required files and datasets exist;
- command parses and configuration resolves;
- environment is available;
- disk space and output directories;
- GPU visibility and free memory where applicable;
- scheduler partition/account limits;
- port and process conflicts for services;
- an existing identical job is not already running;
- resume checkpoint compatibility.

Run a small smoke test when it is cheap and scientifically representative. Do not
interpret a smoke test as final evidence.

## 3. Handle code transfer safely

Prefer an already shared filesystem or a user-approved `rsync`/copy workflow. Show
what will be transferred and exclude secrets, datasets, checkpoints, caches, build
artifacts, and unrelated files.

Do not automatically run `git add`, `git commit`, `git push`, change remotes, or
rewrite history. When git synchronization is requested, inspect status and propose
explicit commands or operate only after the user has authorized the affected files
and remote.

Never place API keys or passwords in command arguments, logs, scripts, or chat.
Use existing environment variables, credential helpers, secret stores, or an
interactive login performed by the user.

## 4. Create a durable run directory

Use a unique, human-readable path such as:

```text
runs/<experiment-id>/<timestamp>-<seed>/
```

Record at minimum:

```text
command.sh              exact launched command
resolved-config.*       fully resolved configuration
metadata.json           revision, host, environment, seed, timestamps
stdout.log / stderr.log
checkpoints/             when applicable
result.*                 machine-readable final result
STATUS                   PENDING | RUNNING | SUCCEEDED | FAILED | CANCELLED
```

Do not overwrite a prior run. If the project has an established tracker, use it
instead of creating a parallel one.

## 5. Launch through the declared runtime

### Local process

Use the project's normal command and a durable log. For a long job, use the user's
approved process manager (`tmux`, `screen`, `nohup`, or a project runner). Capture
the PID or session name.

### SSH or direct remote GPU

Follow [references/remote-execution.md](references/remote-execution.md). Verify the
remote working directory, environment, GPU assignment, log path, and process
identity after launch.

### Slurm

Use the project's existing batch template when available. Otherwise create a
minimal script with explicit resources, output paths, and command. Submit once,
record the job ID, and verify it appears in the queue.

Do not silently switch from the requested scheduler or host because another target
looks convenient.

## 6. Verify the launch

A launch is not complete until evidence shows that the intended job started.
Confirm:

- process, session, or scheduler job exists;
- log contains the resolved command/config and first meaningful step;
- correct GPU/device is visible;
- no immediate OOM, missing-file, import, permission, or authentication error;
- checkpoint and result paths point to durable storage;
- tracker contains the exact job identifier.

If launch fails, diagnose before retrying. Do not create duplicate jobs while the
status is uncertain.

## 7. Retry and resume policy

Retry automatically only when the policy was established and the change does not
alter the scientific condition. Examples:

- transient SSH or scheduler failure;
- recoverable preemption with a compatible checkpoint;
- a documented OOM fallback already in the plan.

Record every retry and changed parameter. A batch-size, precision, sequence length,
model, data, seed, or evaluator change may alter the experiment; do not hide it as
an operational retry.

Use [references/batch-orchestration.md](references/batch-orchestration.md) for
sweeps, waves, and dependent jobs.

## 8. Return a launch record

```markdown
# Experiment Launch

- Experiment ID:
- Scientific purpose:
- Status: RUNNING | FAILED TO LAUNCH | COMPLETED QUICKLY
- Runtime: local | ssh | slurm | other
- Host/partition/device:
- Job/PID/session ID:
- Code revision and working-tree state:
- Command:
- Config and seed:
- Log path:
- Checkpoint path:
- Result path:
- Budget/time limit:
- Retry/resume policy:
- Monitoring command:
- Any deviation from the registered plan:
```

Do not claim experimental success from a successful launch. Hand the durable job
identity to `/firm:monitor-experiment`.
