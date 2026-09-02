---
name: monitor-experiment
description: Reconcile registered local, CPU, GPU, SSH, scheduler, and other long-running research jobs with actual processes, logs, outputs, and termination evidence. Use for operational monitoring and exact result handoff, not scientific interpretation.
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
- intended evidentiary use and registered deviations.

Do not infer ownership from a PID, terminal title, screen name, GPU memory, or Claude's
last sentence alone. Reconcile structured identity with the real process and artifacts.
If identity is absent or ambiguous, report the missing identity facts directly and
repair registration before attaching results to a project.

## Reconcile Execution

Inspect only the mechanism actually used: local process, SSH process, scheduler,
container, queue, or application service. Prefer targeted queries over broad repeated
scans.

Build one timestamped factual account: whether the declared dependency or resource is
still unresolved; whether the matching process or scheduler job exists and progresses;
whether it terminated; whether expected outputs parse and terminal evidence is clean;
whether progress ceased beyond the run's own expectation; whether execution vanished;
whether the registered protocol actually ran; and whether someone explicitly
cancelled it. Do not map these observations onto a fixed status taxonomy or let a
status choose the scientific response.

Process exit alone is not completion. A live PID alone is not progress. Validate log
movement or scheduler progress, expected outputs, parseability, terminal markers, and
the actual scale/config. Distinguish a healthy scientific wait from an operational
stall.

## Recover After Host Power Loss Or Session Restart

Treat every local PID, TTY, endpoint, container, queue row, and run status as stale
until rediscovered. Reconcile the current process set, project cwd, visible terminal
tail, newest main-chain history, Registry row, canonical queue object, exact worker,
and freshest artifact before taking action.

A remote worker may survive loss of the local Claude session. If it is alive and owned
by the registered run, restore monitoring and do not resubmit. If the worker is gone,
reconstruct what happened from terminal artifacts and resume only from a validated checkpoint
under the same frozen contract. Submit at most one replacement for an ordinary
recoverable interruption, preserving the failed attempt and linking its provenance.
Never duplicate a run merely because the laptop rebooted or an old terminal is absent.

For a claimed wait, require both the exact Registry pending/running row and either its
canonical pending/running queue object or an independently verified live worker. A
Registry row, heartbeat, GPU allocation, or old terminal message alone is insufficient.

## Verify Result Fidelity

Before handing off a completed run, check:

- output corresponds to the registered run, config, code, data, and checkpoint;
- every expected cell is present or explicitly missing;
- metrics parse and contain no unexplained NaN, empty population, constant output, or
  impossible value;
- actual model, data, steps, seeds, population, and evaluator match registration;
- runtime, resource use, retries, and material deviations are recorded;
- raw predictions or sufficient statistics needed for independent reading exist.

Describe shortened, substituted, or semantically different execution exactly and list
which intended comparisons it cannot support. Never silently compare it as the intended experiment.

## Hand Off One Evidence Bundle

When execution and expected outputs have been mechanically validated, return a compact
bundle to `signal-analysis`:

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

Record delivery with a durable event identity. Scientific interpretation exists only
in the authoritative research state after the PI reads the bundle. Monitoring does not
explain the result, invent a construction, call Codex, or decide whether to continue.

## Notification Policy

Keep healthy waiting or progressing jobs quiet. Notify the research session when
validated outputs are ready to read, when factual execution evidence requires repair
or an explicit retry decision, when preparation failed, or when a resource conflict
cannot be resolved inside current operational policy. Describe the observed facts and
artifact paths rather than sending a state label.

Do not repeatedly deliver old completion events. Delivery must be acknowledged once
by durable event identity, and historical events must not block new work.

Long raw logs remain outside the main research context. Return exact paths, compact
facts, and only the excerpt needed to diagnose an operational failure.
