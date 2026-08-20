---
name: auto-paper-improvement-loop
description: Improve an existing research paper through bounded evidence-led editing, recompilation, and visual inspection. Use only after the contribution identity and evidence are stable; reserve external red-team review for an optional near-final pass.
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Bounded Paper Improvement

Improve clarity, structure, fidelity, and presentation without optimizing reviewer
scores or silently changing the science.

## Preconditions And Boundary

Read the paper, `CLAIMS_EVIDENCE.md`, `PAPER_PLAN.md`, current contribution identity,
build command, venue constraints, and git status. Use this loop only when the positive
object and evidence are stable enough that writing can resolve the remaining issues.

If a requested fix requires a new result, broader population, stronger causal claim,
new contribution type, or changed primary metric, record it as a research gap and stop
the dependent edit. Return scientific work to `research-pipeline`; do not manufacture
supporting prose.

Defaults:

- at most two self-edit rounds;
- stop after Round 1 if no blocking or major artifact issue remains;
- no fresh Codex reviewer per round; use one optional near-final pass only when it can
  verify a named factual, claim, citation, or proof risk;
- compile and visually inspect after each round;
- never stage, commit, push, install packages, or modify unrelated files without
  explicit authorization.

## Optional Edit Boundary

When `--edit-whitelist <yaml-or-json>` is provided, resolve it before review and apply
it to every edit. Support:

- `allowed_paths` and `forbidden_paths`;
- forbidden additions: citations, bibliography entries, theorem environments, or
  numerical claims;
- forbidden deletions: existing citations or theorem environments;
- operations requiring user approval, such as deleting sections or rewriting the
  abstract wholesale;
- `max_edits_per_round`.

Path denial overrides allowance. Match paths relative to the paper directory. Record
every rejected edit with file, proposed operation, rule, reviewer concern, and whether
it remains unresolved. Never bypass the whitelist through generated files, shell
commands, renames, or includes.

`--style-ref` is author-side structural guidance only. Never copy wording or expose the
source/profile to reviewers.

## Preserve The Starting Point

Before editing:

- locate the root source and existing build command;
- compile once and preserve the known-good PDF;
- record current errors and page count;
- save the contribution identity and claims-evidence hash;
- record the whitelist and all files currently changed.

Do not overwrite the only good artifact. Use `main_round1.pdf` and
`main_round2.pdf` or equivalent names until final verification.

## One Improvement Round

### 1. Fresh artifact review

Give a fresh reviewer the compiled paper, source files needed to locate issues, venue
constraints, and a neutral rubric. Do not provide prior scores, desired verdict,
previous review, fix summary, style exemplar, or project history.

Require findings with exact location, evidence, and minimal repair, classified as:

- `BLOCKING`: correctness, evidence fidelity, attribution, contribution identity, or
  submission compliance;
- `MAJOR`: missing explanation, fair comparison, limitation, structure, or serious
  readability;
- `MINOR`: local wording, notation, layout, and polish.

The reviewer may identify scientific gaps but may not turn them into invented text or
automatic research tasks.

### 2. Lead-author adjudication

Verify every recommendation against source and evidence. Mark it `accept`, `modify`,
`reject`, or `research-gap`. Apply blocking, then major, then worthwhile minor fixes.
Reject suggestions that weaken related work, hide negative evidence, inflate scope, or
change the contribution merely to improve a score.

When a local edit changes notation, claim strength, or terminology, inspect abstract,
introduction, method, results, captions, appendix, limitations, and conclusion for
global consistency.

### 3. Recompile and inspect

Delegate compilation details to `paper-writing mode: compile`. Fix causal errors,
undefined references, duplicate labels, missing figures, and serious overflow. Inspect
the PDF, not only the log.

For theory papers, compare theorem restatements and assumptions. For empirical papers,
run `paper-writing mode: claim-audit` only for numerical or semantic claims affected by
the edits. Unchanged green audits remain valid when their declared input hashes remain
fresh.

### 4. Checkpoint

Append to `PAPER_IMPROVEMENT_LOG.md`:

```markdown
## Round N
- starting and ending PDF:
- reviewer thread/model:
- blocking / major / minor findings:
- accepted, modified, rejected, and research-gap recommendations:
- whitelist rejections:
- files changed:
- compile and visual status:
- affected audits rerun:
- unresolved issues:
- continue another round: yes/no and why:
```

Pause only when the user requested a checkpoint, an operation requires approval, or a
blocking issue cannot be repaired through writing.

## Round 2 And Convergence

If Round 2 is warranted, use a new reviewer who sees only the current artifact and
neutral rubric. Never say what Round 1 changed. Implement only remaining blocking and
major issues plus clearly worthwhile minor repairs.

Stop when:

- no writing-repairable blocking or major issue remains;
- compilation and visual inspection pass;
- affected claim/proof/citation checks are fresh;
- another round would optimize taste or reviewer score rather than correctness.

Do not add a third round automatically. A new scientific objection returns to research;
a changed paper identity requires a fresh evidence-grounded paper entry, plus user
approval only when an explicitly locked boundary changes.

## Final Report

Return the starting/final PDFs, files changed, accepted and rejected recommendations,
compile status, affected audit status, remaining research gaps, whitelist compliance,
and whether the manuscript is improved but still not submission-ready. Reviewer score
movement is optional context, never the success criterion.

Store the optional independent review trace using the shared tracing convention when
configured.
