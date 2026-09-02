---
name: run-experiment
description: Launch reliable local, direct-GPU SSH, Slurm, or queued research experiments with durable configs, logs, checkpoints, results, completion markers, budget tracking, and resume paths. Use after the scientific run is selected; load only the matching operations reference section.
---

# Run Experiment

Execute the selected experiment faithfully and durably. This skill owns deployment,
not scientific problem selection. Use `experiment-plan` for why the run matters and
`signal-analysis` after results complete.

## Scientific Preflight

Read the authoritative live state and tracker. Before a consequential launch confirm:

- the run answers a current question and no unread result makes it wasteful;
- its intended evidentiary use is stated in ordinary language, including what the run
  can and cannot teach;
- method, comparator, population, treatment, evaluator, metric, scale, seed, stopping,
  and forecast match the plan or registration;
- the information-boundary map is present before a method-guiding run and the command
  cannot see disallowed test, future, target, cache, or external information;
- a full method comparison includes the decisive published incumbent and nearest
  claim-threatening published method under matched treatment;
- the command writes parseable results, durable logs, completion/failure status, and
  checkpoints/resume information when applicable;
- expected compute fits the authorized operational budget.

If active state, tasks, tracker, or manuscript disagree about method, evaluator,
baseline, optimizer, run status, or next action, reconcile from code and raw artifacts
before launch. A task label cannot revive a stale method or paper identity.

An exploratory run may proceed with a compact record. An expensive or claim-defining
run needs a frozen forecast and exact provenance, normally through
`research-contract` or the tracker.

A registration, tracker gate, or state forecast governs the named run and its verdict;
it does not prohibit a later formative redesign. If current evidence changes the
method-owned treatment before claim confirmation, register the new run explicitly
rather than treating the old protocol as permanent project authority.

## Protect Interpretability

Before a main run:

- verify data/checkpoint paths, evaluator entrypoint, metric direction, and key
  derived-metric computation;
- record evaluation population and every material training-treatment difference;
- verify intended component engagement and substrate competence;
- run a small end-to-end execution and inspect raw output;
- estimate memory and runtime from a real step;
- confirm checkpoint, log, result, and final-marker writes.

Size accelerator admission from the real-path canary or a closely matched completed
run: measured peak allocation, expected transient peaks, current ownership, and a
meaningful margin. Do not invent universal utilization or free-memory thresholds. A
GPU wait is an operational fact, not a scientific pause: finish only genuinely useful
result-independent preparation, then stop generating audits, hashes, launch checklists,
or alternate method packets merely to appear active.

A smoke test proves execution, not semantic equivalence or scientific effectiveness.
If the evaluator is still being repaired, record that limitation directly rather than
letting a status label imply scientific competence.

When implementation repeatedly fails, record observed failure, verified root cause,
files changed, why the repair addresses the cause, and which earlier runs are
invalidated. If root cause remains unknown, the next run is debugging evidence.

A verified implementation/optimizer/evaluator/integration defect normally earns one
clean matched rerun. If its directional loss remains, do not launch another nearby
variant without a changed load-bearing assumption and prediction.

Before launching multiple seeds, verify their named role in `experiment-plan`. During
method formation, normally complete and read one paired development seed first. Do
not use a queue to search seeds for a favorable result; cancel repetitions made
irrelevant by the first decisive result.

## Route By Environment

Read the project `CLAUDE.md` and use its actual allocation model:

- **local:** CUDA or MPS process under project rules;
- **direct GPU over SSH:** inspect permitted device availability and bind only an
  allowed free device;
- **Slurm/scheduler:** submit through the configured scheduler and never pin physical
  GPU IDs or train on the login node;
- **batch queue:** use only for scientifically justified independent jobs, required
  repetitions, or dependency waves.

Project rules override generic examples. If server information is absent, ask one
focused operational question.

Read `references/operations.md` only for the needed environment: local process,
direct-GPU SSH, Slurm/managed scheduler, FIRM/batch queue, GPU sharing, tracking,
storage, or failure/resume. The reference contains mechanics only and never overrides
the scientific plan or project-specific environment rules.

For a multi-cell campaign whose completeness matters to a candidate or paper argument,
also read `references/campaigns.md`. Maintain one mechanical
`CAMPAIGN_MANIFEST.json`; do not make `PROJECT_STATE.md`, a draft, or session prose
remember matrix completion. The manifest tracks execution identity and artifacts only
and never decides what a result means.

## Durable Lifecycle

Do not force jobs through a fixed lifecycle taxonomy or let a run-state label decide a
scientific action. Preserve timestamped mechanical events instead: who claimed the
work, exact launch identity, observed process or scheduler facts, output validation,
termination evidence, artifact reading, and any explicit retry or invalidation reason.
The campaign helper may use internal execution statuses for atomic concurrency, but
they have no authority outside that manifest and never mean that evidence was
scientifically interpreted.

For every run retain:

- stable run ID and exact command/config;
- environment, code revision, data/checkpoint identifiers;
- log, result, checkpoint, completion marker, and resume paths;
- expected and actual resource charge when measurable;
- protocol deviation and resulting evidence scope.

Register long-running local, CPU, GPU, SSH, scheduler, and container jobs in the
configured FIRM Job Registry when available. Store environment-specific identity: a
scheduler ID, or PID plus start token and command fingerprint for unmanaged processes.
Registry writes must be atomic. Process or terminal absence is not completion; verify
identity and expected output. A completion marker records validated execution only;
the research episode still owns interpretation.

## Launch And Verify

Use the matching command from the operations reference, then verify registered job
identity, GPU allocation when relevant, log creation, result path, and checkpoint or
resume behavior. Keep long jobs detached or scheduler-managed according to project
rules.

Report compactly:

- run ID and intended evidentiary use;
- scheduler job or direct host/GPU/process;
- command/config path;
- log, result, checkpoint, marker, and resume paths;
- expected runtime and operational-budget status.

Do not stream large logs into the main context. Use `monitor-experiment` for progress
and result reconciliation. While a job runs, advance result-independent work rather
than occupying compute or waiting passively.

## Failure Handling

- OOM, preemption, SSH loss, stale screen, disk failure, and missing checkpoints are
  operational states, not scientific results.
- Retry only through the bounded project/queue policy and preserve attempt history.
- If actual scale, steps, seeds, model, data, or method differ from registration,
  describe the exact deviation and exclude every conclusion it no longer supports.
- Reallocate inside the authorized budget and project GPU policy; ask before exceeding
  them or changing a user-locked resource rule.

After mechanically valid completion, hand exact result/config/log paths to
`signal-analysis` and update the authoritative state or tracker after evidence reading.
Do not pre-interpret the science here.
