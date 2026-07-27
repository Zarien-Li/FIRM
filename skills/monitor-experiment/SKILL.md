---
name: monitor-experiment
description: Monitor running experiments, check progress, collect results. Use when user says "check results", "is it done", "monitor", or wants experiment output.
---

# Monitor Experiment Results

Monitor: $ARGUMENTS

## Workflow

### Step 0: Durable State Preflight

Before polling, read the project state/tracker when available (`PIPELINE_STATE.md`, `EXPERIMENT_TRACKER.md`, `refine-logs/EXPERIMENT_PLAN.md`). Identify the durable state surfaces:

- launch command and expected screen/process/job id
- log path
- result path
- checkpoint path, if any
- expected completion marker or final result file
- registered scale, seeds, and stopping condition

A session-only reminder, Claude cron, or chat promise is not a monitor. If no durable log/result/marker path exists, report `monitor_state_missing` and create/update the project tracker before interpreting the run.

### Step 1: Check What's Running

Before polling, identify the expected run matrix from the experiment plan or user's request:

- expected datasets
- expected baselines/methods
- expected seeds
- expected GPUs
- expected result files

Report progress as `completed / expected`, not just "some files exist."

**SSH server:**
```bash
ssh <server> "screen -ls"
```

### Step 2: Collect Output from Each Screen
For each screen session, capture the last N lines:
```bash
ssh <server> "screen -S <name> -X hardcopy /tmp/screen_<name>.txt && tail -50 /tmp/screen_<name>.txt"
```

If hardcopy fails, check for log files or tee output.

### Step 3: Check for JSON Result Files
```bash
ssh <server> "ls -lt <results_dir>/*.json 2>/dev/null | head -20"
```

If JSON results exist, fetch and parse them:
```bash
ssh <server> "cat <results_dir>/<latest>.json"
```

### Step 3.5: Pull W&B Metrics (when `wandb: true` in CLAUDE.md)

**Skip this step entirely if `wandb` is not set or is `false` in CLAUDE.md.**

Pull training curves and metrics from Weights & Biases via Python API:

```bash
# List recent runs in the project
ssh <server> "python3 -c \"
import wandb
api = wandb.Api()
runs = api.runs('<entity>/<project>', per_page=10)
for r in runs:
    print(f'{r.id}  {r.state}  {r.name}  {r.summary.get(\"eval/loss\", \"N/A\")}')
\""

# Pull specific metrics from a run (last 50 steps)
ssh <server> "python3 -c \"
import wandb, json
api = wandb.Api()
run = api.run('<entity>/<project>/<run_id>')
history = list(run.scan_history(keys=['train/loss', 'eval/loss', 'eval/ppl', 'train/lr'], page_size=50))
print(json.dumps(history[-10:], indent=2))
\""

# Pull run summary (final metrics)
ssh <server> "python3 -c \"
import wandb, json
api = wandb.Api()
run = api.run('<entity>/<project>/<run_id>')
print(json.dumps(dict(run.summary), indent=2, default=str))
\""
```

**What to extract:**
- **Training loss curve** — is it converging? diverging? plateauing?
- **Eval metrics** — loss, PPL, accuracy at latest checkpoint
- **Learning rate** — is the schedule behaving as expected?
- **GPU memory** — any OOM risk?
- **Run status** — running / finished / crashed?

**W&B dashboard link** (include in summary for user):
```
https://wandb.ai/<entity>/<project>/runs/<run_id>
```

> This gives the review loop (`/research-review` Looped Mode) richer signal than just screen output — training dynamics, loss curves, and metric trends over time.

### Step 4: Summarize Results

Present results in a comparison table:
```
| Experiment | Metric | Delta vs Baseline | Status |
|-----------|--------|-------------------|--------|
| Baseline  | X.XX   | —                 | done   |
| Method A  | X.XX   | +Y.Y              | done   |
```

After reading results, update or request an update to the top of `PIPELINE_STATE.md` / `EXPERIMENT_TRACKER.md` with:

- completed/running/failed/unread status for each expected cell
- exact result paths read
- exact logs checked
- invalidated or interrupted runs
- single best next monitor or analysis action

### Step 5: Interpret
- Compare against known baselines
- Flag unexpected results (negative delta, NaN, divergence)
- Suggest next steps based on findings

## Key Rules
- Always show raw numbers before interpretation
- Compare against the correct baseline (same config)
- Note if experiments are still running (check progress bars, iteration counts)
- If results look wrong, check training logs for errors before concluding
- If a metric is exactly zero, empty, NaN, identical across implausible conditions, or missing for many cells, treat it as a possible code/eval bug first, not as a scientific result
- Respect user-specified GPU allocation; if a job appears on the wrong GPU, flag it directly
- Avoid repeated broad scans. Prefer one targeted command that reads persisted logs and expected result files
- Do not draw scientific conclusions from session-only state. Conclusions require persisted logs/results or an explicit `interrupted/resume` record.
- If a run finished under a different scale than registered (fewer steps, fewer seeds, smaller model, filtered data, lower max length, fallback method), label it `scope-limited` or `invalidated` before interpreting.
- If the project tracks infrastructure cost locally, include it when available; otherwise do not invent cost estimates or cleanup actions tied to removed infrastructure helpers
- **Sub-agent isolation** (from `shared-references/context-hygiene.md`): Use sub-agents for bulk monitoring. Main session receives only structured result summaries, not raw screen output.
