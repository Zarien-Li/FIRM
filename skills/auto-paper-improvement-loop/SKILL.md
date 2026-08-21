---
name: auto-paper-improvement-loop
description: Improve an existing research paper through human-reader editing, evidence-led revision, recompilation, and visual inspection. Use only after the contribution identity and evidence are stable; reserve external verification for an optional near-final named factual uncertainty.
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Human-Reader Paper Improvement

Improve authorial voice, field-natural language, paragraph movement, specificity,
memorability, fidelity, and presentation without optimizing reviewer scores or silently
changing the science.

## Preconditions And Boundary

Read the paper, `AUTHOR_ARGUMENT.md`, `PAPER_PLAN.md`, post-draft
`CLAIMS_EVIDENCE.md` when available, current contribution identity, build command,
venue constraints, and git status. Use this loop only when the positive object and
evidence are stable enough that writing can resolve the remaining issues.

If a requested fix requires a new result, broader population, stronger causal claim,
new contribution type, or changed primary metric, record it as a research gap and stop
the dependent edit. Return scientific work to `research-pipeline`; do not manufacture
supporting prose.

Defaults:

- normally one or two human-reader edit rounds, with each round justified by a concrete
  opportunity to improve meaning, voice, progression, specificity, or memorability;
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

### 1. Fresh human-reader edit

Give a fresh editor the compiled paper and only the context an intended human reader
would reasonably have. The editor is not a reviewer and does not decide acceptance,
request experiments, enumerate objections, or score the paper.

After a normal ten-minute read, the editor first writes from memory, in prose:

- the problem the paper studies;
- what the reader was expected to believe before the paper;
- the surprising fact or principle;
- why it matters;
- the one idea likely to remain memorable.

The editor then gives a short editorial letter identifying where attention broke,
where paragraph-to-paragraph movement was unclear, where language sounded generic
rather than field-native, where concrete experience was replaced by jargon, and where
the manuscript lost or recovered an authorial voice. Use exact locations when useful,
but do not emit a severity taxonomy, checklist, reviewer simulation, or list of
defensive controls.

### 2. Lead-author revision

Compare the reader's retelling with `AUTHOR_ARGUMENT.md`. Revise the manuscript where
the intended argument failed to survive reading. Prefer concrete scientific language,
deliberate emphasis, and causal paragraph progression over generic transitions or
additional qualifications. Preserve recommendations that reflect genuine reader
confusion; reject edits that hide evidence, inflate scope, or turn prose into reviewer
appeasement.

Caveats stay local only when they materially change interpretation. Other real
boundaries belong in a concise Limitations section. Internal non-claims and audit notes
are not manuscript content.

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
- editor thread/model:
- ten-minute reader retelling:
- author-argument mismatches:
- voice, field-language, progression, specificity, and memorability edits:
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

If Round 2 is warranted, use a new human-reader editor who sees only the current
artifact. Never say what Round 1 changed. Revise only where the intended argument still
does not survive a natural read or where prose remains generic, discontinuous, vague,
or forgettable.

Stop when:

- an intended reader can accurately retell the problem, changed belief, surprise,
  significance, and takeaway;
- the prose has a consistent authorial voice and uses field-natural, concrete language;
- paragraphs advance the argument rather than announce checklist functions;
- compilation and visual inspection pass;
- affected claim/proof/citation checks are fresh;
- another round would no longer improve meaning, voice, or reader understanding.

Scientific taste is part of successful communication, not cosmetic score optimization.
Do not stop merely because remaining problems concern emphasis, rhythm, specificity,
or memorability.

Do not add a third round automatically. A new scientific objection returns to research;
a changed paper identity requires a fresh evidence-grounded paper entry, plus user
approval only when an explicitly locked boundary changes.

## Final Report

Return the starting/final PDFs, files changed, reader retelling before and after,
author-argument mismatches repaired, compile status, affected audit status, remaining
research gaps, whitelist compliance, and whether the manuscript is improved but still
not submission-ready. Reviewer score movement is optional context, never the success
criterion.

Store the optional independent review trace using the shared tracing convention when
configured.
