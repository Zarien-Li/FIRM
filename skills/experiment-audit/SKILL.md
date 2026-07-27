---
name: experiment-audit
description: "Strict boundary audit of experiment integrity before consequential claims, paper writing, submission, or when provenance is genuinely suspect. Uses account-default Codex review to check fake ground truth, score normalization fraud, phantom results, config mismatch, and scope inflation; never invoke as a routine creativity gate."
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Experiment Audit: Cross-Model Integrity Verification

Audit experiment integrity for: **$ARGUMENTS**

Run this at a claim boundary or when concrete evidence raises an integrity concern. Do not run it after every exploratory experiment, and do not interpret a missing audit artifact as permission to stop ordinary research or method iteration.

## Why This Exists

LLM agents can produce fraudulent experimental results through:
1. **Fake ground truth** — creating synthetic "reference" from model outputs, then reporting high agreement as performance
2. **Score normalization** — dividing metrics by the model's own max to get 0.99+
3. **Phantom results** — claiming numbers from files that don't exist or functions never called
4. **Insufficient scope** — reporting 2-scene pilots as "comprehensive evaluation"

These are NOT intentional deception — they are failure modes of optimizing agents that lack integrity constraints. This skill adds that constraint.

## Core Principle

**The executor (Claude) collects file paths. The account-default Codex reviewer reads code and judges integrity. The executor does NOT participate in integrity judgment.**

This follows `shared-references/reviewer-independence.md` and `shared-references/experiment-integrity.md`.

## Workflow

### Step 1: Collect Artifacts (Executor — Claude)

Locate and list these files WITHOUT reading or summarizing their content:

```
Scan project directory for:
1. Evaluation scripts:    *eval*.py, *metric*.py, *test*.py, *benchmark*.py
2. Result files:          *.json, *.csv in results/, outputs/, logs/
3. Ground truth paths:    look in eval scripts for data loading (dataset paths, GT references)
4. Experiment tracker:    EXPERIMENT_TRACKER.md, EXPERIMENT_LOG.md
5. Paper claims:          NARRATIVE_REPORT.md, paper/sections/*.tex, PAPER_PLAN.md
6. Config files:          *.yaml, *.toml, *.json configs with metric definitions
```

**DO NOT summarize, interpret, or explain any file content.** Only collect paths.

### Step 2: Send to Reviewer (account-default Codex MCP)

Pass ONLY file paths and the audit checklist to the reviewer. The reviewer reads everything directly.

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  sandbox: read-only
  cwd: [project directory]
  prompt: |
    You are an experiment integrity auditor. Read ALL files listed below
    and check for the following fraud patterns.

    Files to read:
    - Evaluation scripts: [list paths]
    - Result files: [list paths]
    - Experiment tracker: [list paths]
    - Paper claims: [list paths]
    - Config files: [list paths]

    ## Audit Checklist

    ### A. Ground Truth Provenance
    For each evaluation script:
    1. Where does "ground truth" / "reference" / "target" come from?
    2. Is it loaded from the DATASET, or generated/derived from MODEL OUTPUTS?
    3. If derived: is it explicitly labeled as proxy evaluation?
    4. Are official eval scripts used when available for this benchmark?
    FAIL if: GT is derived from model outputs without explicit proxy labeling.

    ### B. Score Normalization
    For each metric computation:
    1. Is any metric divided by max/min/mean of the model's OWN output?
    2. Are raw scores reported alongside any normalized scores?
    3. Are any scores suspiciously close to 1.0 or 100%?
    FAIL if: Normalization denominator comes from prediction statistics.

    ### C. Result File Existence
    For each claim in the paper/narrative:
    1. Does the referenced result file actually exist?
    2. Does the claimed metric key exist in that file?
    3. Does the claimed NUMBER match what's in the file?
    4. Is the experiment tracker status DONE (not TODO/IN_PROGRESS)?
    FAIL if: Claimed results reference nonexistent files or mismatched numbers.

    ### D. Dead Code Detection
    For each metric function defined in eval scripts:
    1. Is it actually CALLED in any evaluation pipeline?
    2. Does its output appear in any result file?
    WARN if: Metric functions exist but are never called.

    ### E. Scope Assessment
    1. How many scenes/datasets/configurations were actually tested?
    2. How many seeds/runs per configuration?
    3. Does the paper use words like "comprehensive", "extensive", "robust"?
    4. Is the actual scope sufficient for those claims?
    WARN if: Scope language exceeds actual evidence.

    ### F. Evaluation Type Classification
    Classify each evaluation as:
    - real_gt: uses dataset-provided ground truth
    - synthetic_proxy: uses model-generated reference
    - self_supervised_proxy: no GT by design
    - simulation_only: simulated environment
    - human_eval: human judges

    ## Output Format

    For each check (A-F), report:
    - Status: PASS | WARN | FAIL
    - Evidence: exact file:line references
    - Details: what specifically was found

    Overall verdict: PASS | WARN | FAIL
    
    Be thorough. Read every eval script line by line.
```

### Step 3: Parse and Write Report (Executor — Claude)

Parse the reviewer's response and write `EXPERIMENT_AUDIT.md`:

```markdown
# Experiment Audit Report

**Date**: [today]
**Auditor**: Codex account-default, maximum available reasoning (cross-model, read-only)
**Project**: [project name]

## Overall Verdict: [PASS | WARN | FAIL]

## Integrity Status: [pass | warn | fail]

## Checks

### A. Ground Truth Provenance: [PASS|WARN|FAIL]
[details + file:line evidence]

### B. Score Normalization: [PASS|WARN|FAIL]
[details]

### C. Result File Existence: [PASS|WARN|FAIL]
[details]

### D. Dead Code Detection: [PASS|WARN|FAIL]
[details]

### E. Scope Assessment: [PASS|WARN|FAIL]
[details]

### F. Evaluation Type: [real_gt | synthetic_proxy | ...]
[classification + evidence]

## Action Items
- [specific fixes if WARN or FAIL]

## Claim Impact
- Claim 1: [supported | needs qualifier | unsupported]
- Claim 2: ...
```

Also write `EXPERIMENT_AUDIT.json` for machine consumption:

```json
{
  "date": "2026-04-10",
  "auditor": "codex-account-default",
  "overall_verdict": "warn",
  "integrity_status": "warn",
  "checks": {
    "gt_provenance": {"status": "pass", "details": "..."},
    "score_normalization": {"status": "warn", "details": "..."},
    "result_existence": {"status": "pass", "details": "..."},
    "dead_code": {"status": "pass", "details": "..."},
    "scope": {"status": "warn", "details": "..."},
    "eval_type": "real_gt"
  },
  "claims": [
    {"id": "C1", "impact": "supported"},
    {"id": "C2", "impact": "needs_qualifier"}
  ]
}
```

### Step 4: Print Summary

```
🔬 Experiment Audit Complete

  GT Provenance:      ✅ PASS — real dataset GT used
  Score Normalization: ⚠️ WARN — boundary metric uses self-reference
  Result Existence:    ✅ PASS — all files exist, numbers match
  Dead Code:           ✅ PASS — all metric functions called
  Scope:               ⚠️ WARN — 2 scenes, paper says "comprehensive"

  Overall: ⚠️ WARN
  
  See EXPERIMENT_AUDIT.md for details.
```

## Integration with Other Skills

### Boundary Invocation Only

Do not run this skill automatically after `run-experiment` (single-shot or Batch Mode). Invoke it when a result is about to support a consequential claim, when paper writing or submission begins, or when concrete provenance concerns arise.

The audit never blocks continued investigation, debugging, or method repair. It does block the affected evidence from supporting a claim until a material integrity failure is repaired, rerun, or explicitly removed from the claim.

- `PASS`: evidence may proceed to scientific interpretation.
- `WARN`: preserve the exact limitation and decide whether it narrows the claim or requires repair.
- `FAIL`: do not use the affected result as claim evidence.

### Read by /signal-analysis (if exists)

```
if EXPERIMENT_AUDIT.json exists:
    read integrity_status
    attach to verdict: {claim_supported: "yes", integrity_status: "warn"}
    if integrity_status == "fail":
        downgrade verdict display: "yes [INTEGRITY CONCERN]"
else:
    do not assume an audit was required; verify ordinary provenance directly
    mark as "provisional — no integrity audit"
```

### Read by /paper-writing (if exists)

```
if EXPERIMENT_AUDIT.json exists AND integrity_status == "fail":
    add footnote to affected claims: "Note: integrity audit flagged concerns with this evaluation"
```

## Key Rules

- **Reviewer independence**: executor collects paths, reviewer judges. Period.
- **Never block**: warn loudly, never halt the pipeline.
- **File-as-switch**: no EXPERIMENT_AUDIT.md = skill was never run = zero impact on existing behavior.
- **Cross-model**: the reviewer MUST be a different model family from the executor.
- **Honest about limits**: the audit catches common patterns, not all possible fraud. It is a safety net, not a guarantee.

### Anti-Rationalization Check (from `shared-references/multi-model-roles.md`)

Check whether experiment results have been re-interpreted to fit a narrative different from the original contract. Specifically verify:
- Do the paper's claims match the contract's success signals?
- Have failure signals been silently redefined?
- Has the scope been expanded beyond what the contract specified?

See `shared-references/context-hygiene.md` for contract traceability rules.

## Acknowledgements

Motivated by observed failures in agent-driven experiments where executor agents created proxy
ground truth from model outputs or normalized scores against the model's own maximum. The audit
patterns are retained because they recurred in practice, not because issue numbers carry
authority.
