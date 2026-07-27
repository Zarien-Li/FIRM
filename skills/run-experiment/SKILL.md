---
name: run-experiment
description: Deploy and run ML experiments on local GPU or remote SSH GPU servers — from single ad-hoc jobs to queued batches (multi-seed sweeps, wave transitions, teacher→student chains) with OOM-aware retry, stale-screen cleanup, and resume-on-crash. Use when user says "run experiment", "deploy to server", "跑实验", "batch experiments", "队列实验", "run grid", "multi-seed sweep", "auto-chain experiments", or needs to launch training jobs.
---

# Run Experiment

Deploy and run ML experiment: $ARGUMENTS

## Workflow

### Step 0: Scientific And Reproducibility Preflight

For research `method-paper` work, understand why the run is worth doing and make its evidence durable. The amount of registration should match the run: an exploratory sanity run needs a clear question and label; a method-development run should state whether it tests activation, optimization, integration, a component interaction, or a tradeoff and how the result changes the next construction; an expensive or claim-defining run needs a frozen forecast, comparison, and interpretation.

Before a consequential GPU launch, read the relevant existing state:

- `refine-logs/EXPERIMENT_PLAN.md` or an equivalent tracker
- `docs/research_contract.md` when the project is contracted
- `PIPELINE_STATE.md` or `RESEARCH_STATE_AUDIT.md` when available

Confirm what matters for this run:

- the run answers a live scientific or implementation question and currently outranks another probe, rerun, or consolidation action
- the run appears in the experiment tracker, or is explicitly labeled as exploratory sanity/debug evidence and is recorded immediately after launch
- the minimum sanity checks needed to trust this run have passed, or this run is itself that check
- the strongest simple alternative and decisive comparison are included when they are necessary for the intended claim; they are not universal permission gates before method work
- no pending or unread run would make this launch wasteful
- the command will write parseable outputs
- the command will write durable logs, result files, and a completion/failure marker
- the tracker records registered scale, seeds, steps/epochs, stopping condition, checkpoint path, and result path
- expensive runs have user approval

If the run is part of baseline reproduction, route through `/baseline` rules first. If the run is a large grid, multi-seed sweep, or dependent wave, use **Batch Mode (Job Queue)** below instead of single-shot deployment.

Before launching more than one random seed, name the evidence role: stochastic diagnosis, method formation, or claim confirmation. During formation, normally complete and read one paired development seed before allocating a sweep. A clear, valid negative already shows that the current realization needs repair; repeating it does not repair it. Launch another seed only when it can distinguish a plausible stochastic outlier from a systematic failure, or after a coherent positive realization needs reliability evidence. Cancel or defer queued repetitions made irrelevant by the first result.

An unregistered exploratory run may inform design, but it cannot later be promoted silently into claim-defining evidence. Before a claim-defining method run starts, record its exact configuration, forecast, comparison, utility checks, and result paths in the existing contract or tracker.

Do not force a prototype run to carry the final paper burden, and do not use that distinction to hide an end-to-end loss. Report what the run actually adjudicates. If the intended computation activates or produces a useful partial behavior, preserve the signal for the next method version; if execution or optimization is non-functional, fix that before interpreting the result as evidence against the primitive.

After submission, continue research that is independent of the running job. Prepare analysis code, evaluator checks, ablations, literature comparisons, figures, or the next evidence-conditioned branch. Do not occupy extra compute merely to appear active, and do not wait passively for the job before doing work whose validity does not depend on its result.

### Step 1: Detect Environment

Read the project's `CLAUDE.md` to determine the experiment environment:

- **Local GPU** (`gpu: local`): Look for local CUDA/MPS setup info
- **Remote direct GPU** (`gpu: remote`, `scheduler: direct` or equivalent): Look for SSH alias, conda env, code directory, and the project's permitted GPU-allocation rule
- **Remote scheduler** (`gpu: remote`, `scheduler: slurm` or equivalent): Look for login host, partition/account, resource limits, submission template, and project storage

If no server info is found in `CLAUDE.md`, ask the user.

The project's operational rules override the generic examples below. Do not convert a scheduler-managed cluster into a direct-GPU host merely because `nvidia-smi`, `screen`, or `CUDA_VISIBLE_DEVICES` appears in this skill. Do not silently convert a direct-GPU server into Slurm.

### Step 2: Pre-flight Check

Check availability using the target's actual allocation model.

**Remote scheduler (Slurm):**
```bash
ssh <server> "sinfo; squeue -u <user>"
```

Use `sacct` for completed jobs and the project log for runtime diagnosis. The login node is not a GPU node: do not run `nvidia-smi`, training, large compilation, or long evaluation there. Do not decide which physical GPU is free. Queue state and scheduler allocation are authoritative.

**Remote direct GPU (SSH):**
```bash
ssh <server> nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader
```

**Local:**
```bash
nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader
# or for Mac MPS:
python -c "import torch; print('MPS available:', torch.backends.mps.is_available())"
```

On a direct-GPU host, use the free-memory threshold defined by `CLAUDE.md`; if none is defined, `memory.used < 500 MiB` is a conservative default. This threshold does not apply to Slurm.

### Step 3: Sync Code (Remote Only)

Check the project's `CLAUDE.md` for a `code_sync` setting. If not specified, default to `rsync`.

#### Option A: rsync (default)

Only sync necessary files — NOT data, checkpoints, or large files:
```bash
rsync -avz --include='*.py' --exclude='*' <local_src>/ <server>:<remote_dst>/
```

#### Option B: git (when `code_sync: git` is set in CLAUDE.md)

Push local changes to remote repo, then pull on the server:
```bash
# 1. Push from local
git add -A && git commit -m "sync: experiment deployment" && git push

# 2. Pull on server
ssh <server> "cd <remote_dst> && git pull"
```

Benefits: version-tracked, multi-server sync with one push, no rsync include/exclude rules needed.

### Step 3.5: W&B Integration (when `wandb: true` in CLAUDE.md)

**Skip this step entirely if `wandb` is not set or is `false` in CLAUDE.md.**

Before deploying, ensure the experiment scripts have W&B logging:

1. **Check if wandb is already in the script** — look for `import wandb` or `wandb.init`. If present, skip to Step 4.

2. **If not present, add W&B logging** to the training script:
   ```python
   import wandb
   wandb.init(project=WANDB_PROJECT, name=EXP_NAME, config={...hyperparams...})

   # Inside training loop:
   wandb.log({"train/loss": loss, "train/lr": lr, "step": step})

   # After eval:
   wandb.log({"eval/loss": eval_loss, "eval/ppl": ppl, "eval/accuracy": acc})

   # At end:
   wandb.finish()
   ```

3. **Metrics to log** (add whichever apply to the experiment):
   - `train/loss` — training loss per step
   - `train/lr` — learning rate
   - `eval/loss`, `eval/ppl`, `eval/accuracy` — eval metrics per epoch
   - `gpu/memory_used` — GPU memory (via `torch.cuda.max_memory_allocated()`)
   - `speed/samples_per_sec` — throughput
   - Any custom metrics the experiment already computes

4. **Verify wandb login on the target machine:**
   ```bash
   ssh <server> "wandb status"  # should show logged in
   # If not logged in:
   ssh <server> "wandb login <WANDB_API_KEY>"
   ```

> The W&B project name and API key come from `CLAUDE.md` (see example below). The experiment name is auto-generated from the script name + timestamp.

### Step 4: Deploy

Every deployment must include durable state:

- `tee` log path in the project or approved remote workspace
- parseable result path
- checkpoint path for resumable training when applicable
- a final marker file or JSON field that records `completed`, `failed`, or `interrupted`

Session-only monitoring is not enough. If a run will outlive the current chat/tool call, write the monitor command and expected marker into `PIPELINE_STATE.md` or `EXPERIMENT_TRACKER.md` before handing off.

#### Remote scheduler (Slurm)

Submit through the scheduler using the project's existing `sbatch` template. The scheduler, not the agent, chooses the physical GPU:

```bash
ssh <server> "cd <remote_project> && sbatch scripts/<job>.sbatch"
```

The script should request only the resources justified by the run and allowed by `CLAUDE.md`, for example:

```bash
#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH -o logs/%j.out

set -euo pipefail
source <project-environment-loader>
python <script> <args>
```

Do not set `CUDA_VISIBLE_DEVICES` to a physical index in an `sbatch` script; Slurm supplies the allocated visibility. Do not add `--nodelist`, a GPU index, a GPU-model constraint, or other placement pinning unless the project rules or user explicitly require it. Follow the configured partition/account/time limit exactly. Use `sbatch` rather than an interactive allocation when the project forbids `srun --pty` or shared sessions make interactive allocation wasteful.

#### Remote direct GPU (via SSH + screen)

For each experiment, create a dedicated screen session with GPU binding:
```bash
ssh <server> "screen -dmS <exp_name> bash -c '\
  eval \"\$(<conda_path>/conda shell.bash hook)\" && \
  conda activate <env> && \
  CUDA_VISIBLE_DEVICES=<gpu_id> python <script> <args> 2>&1 | tee <log_file>'"
```

#### Local

```bash
# Linux with CUDA
CUDA_VISIBLE_DEVICES=<gpu_id> python <script> <args> 2>&1 | tee <log_file>

# Mac with MPS (PyTorch uses MPS automatically)
python <script> <args> 2>&1 | tee <log_file>
```

For local long-running jobs, use `run_in_background: true` to keep the conversation responsive.

### Step 5: Verify Launch

**Remote scheduler (Slurm):**
```bash
ssh <server> "squeue -j <job_id>; sacct -j <job_id> --format=JobID,State,Elapsed,ExitCode"
```

Confirm that the job ID, log path, output path, and resume path were recorded.

**Remote direct GPU (SSH):**
```bash
ssh <server> "screen -ls"
```

**Local:**
Check process is running and GPU is allocated.

## Batch Mode: Job Queue (Multi-Seed / Multi-Config / Wave Orchestration)

Orchestrate large batches of ML experiments on SSH remote GPU servers with proper state tracking, OOM retry, stale cleanup, and wave transitions.

Batch mode orchestrates a scientifically justified batch; it does not justify creating the batch. Before expanding random seeds, the project must already know whether repetition answers a defined stochastic uncertainty or provides reliability evidence for a coherent positive realization. A queue must not be used to search across seeds for a favorable prototype result.

The screen-based queue manager in this section is for **direct-GPU SSH hosts only**. On Slurm, use scheduler-native job arrays, dependencies, or the project's existing idempotent `sbatch` launcher; never run this queue manager on a login node and never make it assign physical GPU IDs behind Slurm's back. Preserve the same manifest, evidence-role, completion-marker, and first-seed inspection rules.

### When to Use Batch Mode

Use batch mode when single-shot deployment is insufficient:

- **≥10 jobs** that need batching across GPUs
- **Multi-seed sweeps** (e.g., 21 seeds × 12 cells)
- **Wave transitions** (run wave 1, wait, run wave 2, wait, run wave 3...)
- **Teacher+student chains** (train teacher then distill; auto-trigger student after teacher done)
- **OOM-prone configs** where you need to retry with different GPU or wait
- **Mixed seed grids** where failed cells need re-running

Do NOT use batch mode for:

- Single ad-hoc experiment (use the single-shot workflow above; rule of thumb: ≤5 jobs)
- Experiments that need manual inspection between runs
- Method-formation repetitions whose relevance depends on reading the first development seed
- Multi-seed rescue attempts after a clear valid loss; diagnose or redesign the realization instead

### Why Batch Mode Exists

Based on session audit (2026-04-16), the major wall-clock sinks in multi-seed grid experiments are:

1. **Stale screens** — python finishes, wandb uploads, screen hangs, next wave blocked
2. **OOM on shared GPU** — previous job's memory not yet released
3. **Wave race** — new wave launches before previous wave fully settles
4. **Missing checkpoints** — student launches before teacher saved
5. **Parser duplication** — rewriting multi-seed analysis python every batch

All of these are pure engineering friction that can be orchestrated.

### Job Manifest

A manifest lists jobs with explicit state:

```yaml
project: my_grid_experiment
cwd: /home/user/your_project
conda: my_env
# Optional: override conda hook path if conda is not at a standard location.
# Can be a bare path (wrapped automatically) or a full `eval "$(... shell.bash hook)"` string.
# Falls back to auto-detect of ~/anaconda3, ~/miniconda3, /opt/anaconda3, etc.,
# or the RESEARCH_CONDA_HOOK environment variable.
# conda_hook: /custom/path/to/conda
ssh: gpu-server
default_cmd: >
  python run_distill.py --backbone softmax --lam 0.5
  --K 500 --L 96 --W 16 --n_steps 30000 --batch_size 128 --lr 1e-4

preconditions:
  - type: checkpoint_exists
    path: checkpoints/transformer/teacher_L96_K500_N{N}.pt

gpus: [0, 1, 2, 3, 4, 5, 6, 7]
max_parallel: 8
gpu_free_threshold_mib: 500  # optional, default 500; raise for shared servers, lower for tight packing
oom_retry:
  delay: 120
  max_attempts: 3

jobs:
  - id: s200_N64_n50K
    args: {seed: 200, n_hidden: 64, n_train_subset: 50000, subset_seed: 2024}
  - id: s200_N128_n50K
    args: {seed: 200, n_hidden: 128, n_train_subset: 50000, subset_seed: 2024}
  # ... 14 more
```

### Job State Machine

```
pending → running → completed
                 ↘ failed_oom → pending (after delay) [retry up to N]
                 ↘ failed_other → stuck (needs manual inspection)
stale_screen_detected → cleaned → pending
```

### Wave Orchestration

A "wave" is a batch of jobs that fit available GPUs. Next wave only starts when:
1. All current-wave python processes have exited
2. No stale screens remain for current-wave tags
3. GPU memory has dropped below threshold (≤500 MiB)
4. Precondition checks pass for next-wave jobs

### Batch Workflow

#### Step B1: Parse Manifest / Build from Grid

Input can be:
- **YAML manifest** (explicit job list, recommended for complex cases)
- **Grid spec** (Cartesian product of param values, e.g., `N=[64,128,256] × n=[50K,150K,500K,652K]`)
- **Natural language description** (Claude parses into manifest)

Bind the run identifiers once so every later step (manifest save, scp, launch, monitor, resume) refers to the same paths. Set these as local shell variables before generating the manifest:

```bash
# REPLACE the placeholder path before running, or pre-export PROJECT_DIR:
PROJECT_DIR="${PROJECT_DIR:?set PROJECT_DIR to the local project root}"
RUN_TS=$(date -u +%Y%m%dT%H%M%SZ)             # one timestamp per run, reused everywhere
LOCAL_RUN_DIR="$PROJECT_DIR/experiment_queue/$RUN_TS"
mkdir -p "$LOCAL_RUN_DIR"
```

Save the built manifest to `$LOCAL_RUN_DIR/manifest.json` for reproducibility.

#### Step B2: Pre-flight

- Check SSH connection works
- Check conda env exists on remote
- Check `cwd` exists on remote
- Check all preconditions (checkpoints, input files)
- Check GPU availability (at least `max_parallel` free GPUs)

If any precondition fails, show user which jobs are blocked and why.

#### Step B3: Launch Through The Available Scheduler

This public skill does not assume an unpublished queue manager.

- On Slurm, prefer job arrays and `--dependency=afterok:<jobid>`.
- On Kubernetes, Ray, or a managed platform, use its native job and retry semantics.
- On a direct SSH host, prefer the project's existing idempotent launcher. If none exists,
  create a small project-local launcher whose behavior is visible in the repository.

For every backend, preserve the same contract:

1. save `manifest.json` under `$LOCAL_RUN_DIR`;
2. record one command, log path, expected output, dependency list, and retry limit per job;
3. write state transitions atomically to `queue_state.json`;
4. identify completion from expected artifacts, not only process disappearance;
5. inspect the first scientifically meaningful run before expanding the rest of a seed sweep;
6. resume the same run directory after interruption rather than generating a new timestamp.

Do not claim OOM retry, stale-process recovery, dependency enforcement, or resume support unless
the selected backend actually implements and verifies those behaviors.

#### Step B4: Monitoring

Users should be able to check the selected backend's durable state at any time. For a
project-local direct-host launcher, a typical query is:

```bash
ssh <server> "cat <remote_run_dir>/queue_state.json" \
  | jq '.jobs | group_by(.status) | map({(.[0].status): length}) | add'
```

For Slurm or managed platforms, query their native state and reconcile it with expected output
artifacts. `/monitor-experiment` may be used for logs, result files, and W&B metrics.

#### Step B5: Post-completion

When all jobs in `manifest.json` are `completed` or `stuck`:
- Confirm the selected backend has stopped launching work and no owned job remains unexpectedly active.
- Aggregate state into `$LOCAL_RUN_DIR/summary.md`, grouping by status and linking per-job logs and outputs.
- Local skill agent invokes `/monitor-experiment` if `analyze_on_complete: true`.

### Grid Spec Syntax

Instead of writing 24 job entries manually:

```yaml
grid:
  N: [64, 128, 256]
  n: [50000, 150000, 500000, 652000]
  seed: [42, 200, 201]
template:
  id: "s${seed}_N${N}_n${n}"
  args: {seed: ${seed}, n_hidden: ${N}, n_train_subset: ${n}}
```

Expands to 36 jobs automatically.

### Wave Chaining

For sequential phases (teacher → student):

```yaml
phases:
  - name: train_teachers
    grid:
      N: [384, 512]
    template:
      cmd: python run_train.py --direction c --backbone softmax --n_hidden ${N} ...
      output_check: checkpoints/transformer/teacher_L96_K500_N${N}.pt

  - name: distill_students
    depends_on: train_teachers
    grid:
      N: [384, 512]
      seed: [42, 200, 201]
    template:
      cmd: python run_distill.py --n_hidden ${N} --seed ${seed} ...
      output_check: figures/distill_sw_N${N}_*_seed${seed}.json
```

Scheduler enforces `depends_on`: `distill_students` jobs stay `pending` until all
`train_teachers` jobs are `completed`.

### OOM Handling

Detect OOM from stdout:
```regex
torch\.OutOfMemoryError: CUDA out of memory
```

On detection:
1. Mark job `failed_oom`
2. Kill screen
3. Wait `oom_retry.delay` seconds
4. Check if current GPU is free; if not, try another free GPU
5. Requeue as `pending`
6. Max `oom_retry.max_attempts` before marking `stuck`

### Stale Screen Detection

Every 60s, for each running screen:
1. Check screen exists (`screen -ls`)
2. Check python PID still running (`ps -p`)
3. If screen exists but python exited:
   - If expected output file exists → mark `completed`, kill stale screen
   - If no output file → mark `failed_other`, kill screen

### Resume-on-restart

If scheduler crashes / is killed:
1. Read `queue_state.json`
2. For each `running` job: check screen; if still alive, keep; if not, re-evaluate state
3. For each `pending`: continue normally
4. Idempotent: safe to restart scheduler without losing state

### Batch Output: Summary Report

```markdown
# Experiment Queue Summary

**Project**: my_grid_experiment
**Started**: 2026-04-16 11:36:29
**Completed**: 2026-04-16 18:02:14
**Total wall-clock**: 6h 25m
**Jobs**: 40 completed, 2 OOM-retried then completed, 0 stuck

## Phases
| Phase | Jobs | Success | OOM retries | Duration |
| --- | --- | --- | --- | --- |
| train_teachers | 2 | 2 | 0 | 58m |
| distill_students | 24 | 24 | 2 | 4h 02m |
| multi_seed_validation | 16 | 16 | 0 | 1h 25m |

## Results Files
- 42 JSON files in `figures/distill_sw_*.json`

## Next Steps
- Run `/monitor-experiment` on output JSONs
- Figures auto-regen via `artifact-sync` (if configured)
```

### Batch Key Rules

- **Never overlap screens on the same GPU** — always wait for `memory.used < 500 MiB` before launching new job
- **Always write state to disk** — every state change flushed to `queue_state.json`
- **Idempotent scheduler** — safe to restart; picks up from state file
- **Expected-output-based completion** — don't trust screen state alone; verify output file exists
- **Bounded retry** — max N OOM retries, then mark `stuck` and alert
- **Dependencies enforced at launch** — never launch student before teacher checkpoint exists

### Batch Known Failure Modes

- **SSH connection drop during scheduling**: use a detached, durable backend and reconnect to its state
- **GPU reservation by another user**: wait; never pre-empt or silently oversubscribe
- **Disk full on remote**: stop launching new work, preserve evidence, and report the blocked state

### Batch Example Session

User: "跑 T5+T6 全部实验：T5 = N∈{80,192} × n 4 values × seed {200,201}, T6 = N∈{384,512} × n 4 values × seed {42,200,201}; T6 需要先 train teacher"

1. Parses description into 2-phase manifest
2. Phase 1: T5 (16 jobs, no teacher dependency) + T6 teacher training (2 jobs)
3. Phase 2: T6 distillation (24 jobs, depends on teachers)
4. Deploys through the configured scheduler
5. Reports the scheduler identifier, total jobs, logs, outputs, and estimated wall-clock

Then user can check anytime or wait for summary report.

## Key Rules

- ALWAYS check availability through the configured allocation model: Slurm queue/account state for scheduler clusters, GPU memory for direct hosts
- On Slurm, submit jobs and let the scheduler assign devices; on a direct host, each experiment gets its own screen session and permitted GPU binding; local runs use a background process when appropriate
- Use `tee` to save logs for later inspection
- Run deployment commands with `run_in_background: true` to keep conversation responsive
- Report back: Slurm job ID or direct-host GPU/screen/process, command, log path, result path, completion marker, and estimated time
- Parallelize only within the configured scheduler/allocation policy and the experiment's scientific justification
- Do not parallelize random seeds merely to avoid reading the first informative result; multi-seed compute must answer a stated uncertainty or support a stabilized claim
- If the launched scale differs from the registered plan, mark the run `scope-limited` in the tracker immediately; do not let a smaller/fallback run silently become the method verdict

## CLAUDE.md Example

Users should add their server info to their project's `CLAUDE.md`:

```markdown
## Remote Server
- gpu: remote               # use pre-configured SSH server
- scheduler: direct         # direct | slurm
- SSH: `ssh my-gpu-server`
- GPU: 4x A100 (80GB each)
- Conda: `eval "$(/opt/conda/bin/conda shell.bash hook)" && conda activate research`
- Code dir: `/home/user/experiments/`
- code_sync: rsync          # default. Or set to "git" for git push/pull workflow
- wandb: false              # set to "true" to auto-add W&B logging to experiment scripts
- wandb_project: my-project # W&B project name (required if wandb: true)
- wandb_entity: my-team     # W&B team/user (optional, uses default if omitted)

## Slurm Server
- gpu: remote
- scheduler: slurm
- SSH: `ssh my-login-node`
- Partition/account/time limit: `<project-specific values>`
- Submission: `sbatch scripts/<job>.sbatch`
- Do not pin physical GPU IDs or run training on the login node
- Code dir: `/cluster/home/user/project/`

## Local Environment
- gpu: local                 # use local GPU
- Mac MPS / Linux CUDA
- Conda env: `ml` (Python 3.10 + PyTorch)
```

> **W&B setup**: Run `wandb login` on your server once (or set `WANDB_API_KEY` env var). The skill reads project/entity from CLAUDE.md and adds `wandb.init()` + `wandb.log()` to your training scripts automatically. Dashboard: `https://wandb.ai/<entity>/<project>`.
