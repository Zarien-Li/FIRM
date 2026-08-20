---
name: monitor-experiment
description: Reconcile registered local, CPU, GPU, SSH, scheduler, and other long-running research jobs with actual processes, logs, outputs, and completion state. Use for operational monitoring and exact result handoff, not scientific interpretation.
---

# Monitor Experiment

Monitor the selected run faithfully. This skill owns operational truth, not scientific
meaning, method choice, or continuation.

## Start From Structured Identity

Read the project's configured FIRM Job Registry or scheduler record when one exists.
Otherwise read the exact run record created by `run-experiment`. Resolve:

- stable run and project IDs;
- execution environment, host, scheduler ID or process identity;
- PID start token and command fingerprint for unmanaged processes;
- config and launch command;
- log, result, checkpoint, completion marker, and resume paths;
- expected cells and dependencies;
- evidence role and registered deviations.

Do not infer ownership from a PID, terminal title, screen name, GPU memory, or Claude's
last sentence alone. Reconcile structured identity with the real process and artifacts.
If identity is absent or ambiguous, report `monitor_state_missing`; repair registration
before attaching results to a project.

## Reconcile Execution

Inspect only the mechanism actually used: local process, SSH process, scheduler,
container, queue, or application service. Prefer targeted queries over broad repeated
scans.

Classify execution as:

- `pending`: registered and waiting on a declared dependency or resource;
- `running`: matching process/job is alive and making plausible progress;
- `completed_unread`: expected output exists, parses, and terminal status is clean;
- `failed`: terminal error with preserved logs;
- `stuck`: identity is valid but progress has ceased beyond the run's own expectation;
- `interrupted`: execution vanished without a valid terminal artifact;
- `invalidated`: output exists but the registered protocol was not executed;
- `cancelled`: explicitly cancelled.

Process exit alone is not completion. A live PID alone is not progress. Validate log
movement or scheduler progress, expected outputs, parseability, terminal markers, and
the actual scale/config. Distinguish a healthy scientific wait from an operational
stall.

## Verify Result Fidelity

Before handing off a completed run, check:

- output corresponds to the registered run, config, code, data, and checkpoint;
- every expected cell is present or explicitly missing;
- metrics parse and contain no unexplained NaN, empty population, constant output, or
  impossible value;
- actual model, data, steps, seeds, population, and evaluator match registration;
- runtime, resource use, retries, and material deviations are recorded;
- raw predictions or sufficient statistics needed for independent reading exist.

Label a shortened or substituted run `scope-limited`; label a semantically different
run `invalidated`. Never silently compare it as the intended experiment.

## Hand Off One Evidence Bundle

For `completed_unread`, return a compact bundle to `signal-analysis`:

```markdown
## Completed Run Bundle
- run/project IDs and evidence role:
- config, code, data, checkpoint, and evaluator identities:
- matched comparison expected:
- raw result and prediction paths:
- log, checkpoint, and terminal marker paths:
- completed/missing cells:
- raw headline values, without interpretation:
- deviations, warnings, retries, cost, and runtime:
```

Mark `interpreting` while the bundle is being read and `interpreted` only after the
scientific observation is recorded in the authoritative research state. Monitoring
does not explain the result, invent a construction, call Codex, or decide whether to
continue.

## Notification Policy

Keep healthy `pending` and `running` jobs quiet. Notify the research session only for:

- valid `completed_unread` evidence;
- `failed`, `stuck`, `interrupted`, or `invalidated` execution;
- a preparation error the research session must repair;
- a resource conflict that cannot be resolved inside current operational policy.

Do not repeatedly deliver old completion events. Delivery must be acknowledged once
by durable event identity, and historical events must not block new work.

Long raw logs remain outside the main research context. Return exact paths, compact
facts, and only the excerpt needed to diagnose an operational failure.
