---
name: resubmit-pipeline
description: Prepare an existing paper for a new venue through physical isolation, reviewer-concern mapping, bounded evidence-preserving edits, anonymity checks, recompilation, and a source diff. Use when results and contribution identity are frozen and no new experiments, theorems, citations, or framework changes are allowed.
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Resubmit An Existing Paper

This skill orchestrates a constrained venue transfer. It does not own general paper
writing, improvement-loop internals, experiment/citation audits, or scientific review.

## When It Applies

Require:

- a prior submission and reviewer corpus;
- a user-selected target venue;
- frozen experimental results and contribution identity;
- permission for text/layout changes within an explicit boundary;
- no new experiments, theorem changes, bibliography mutations, or method redesign.

Use `paper-writing` when structural rewriting or a new manuscript is needed. Return to
research when a critical concern requires new evidence or a changed contribution.

## Inputs

Resolve:

- source submission directory and immutable baseline PDF/source hash;
- target venue template, page/anonymity/artifact rules, and deadline;
- reviewer comments, meta-review, author response, and known weaknesses;
- allowed/forbidden paths and operations;
- destination directory, which must not already exist.

Do not infer permission to overwrite an earlier venue directory.

## 1. Create Physical Isolation

Create a new sibling directory atomically and copy only source, figures, bibliography,
and build files needed for the target. Exclude caches, generated junk, credentials,
private notes, old review traces, and unrelated artifacts. Preserve the source
submission unchanged.

Record in `.resubmit/STATE.md`:

- source/destination paths and hashes;
- source and target venues;
- frozen scientific identity and results;
- edit boundary;
- current phase and build status.

## 2. Establish Health, Venue, And Anonymity

Compile the copied source before edits. Record pre-existing failures separately from
new failures. Inspect target template and rules from authoritative venue sources.

Scan source, PDF metadata, acknowledgements, comments, filenames, repository URLs,
supplementary text, self-citations, and generated artifacts for identity leakage.
Anonymize only what the venue requires; do not corrupt citation meaning or erase
scientific provenance from internal records.

## 3. Map Reviewer Concerns Before Editing

Create `KNOWN_WEAKNESSES.md`:

```markdown
| ID | Reviewer concern | Evidence in current paper | Severity | Text-fixable? | Allowed repair | Location |
|---|---|---|---|---|---|---|
```

Classify each concern:

- `resolved-already`;
- `text-fixable` through clarification, qualification, reorganization, or limitation;
- `format/venue`;
- `requires-new-science`;
- `incorrect-reviewer-premise`, with evidence.

Do not weaken related work or hide contrary results to make a concern text-fixable.
When a blocking concern requires new science, stop the dependent resubmit path and ask
the user whether to reopen research; do not silently broaden the edit boundary.

If reviewer-facing responses are requested, map each response to a manuscript change
or explain why no change is scientifically warranted. Do not promise unperformed work.

## 4. Build The Edit Whitelist

Write `.resubmit/edit_whitelist.yaml` for `/auto-paper-improvement-loop`:

- permit only target-venue source and layout files needed for the approved edits;
- forbid prior-submission directories, raw results, code, `.bib`, `.sty`, and `.bst`
  unless the user explicitly authorizes a venue-format exception;
- forbid new citations, bibliography entries, theorem environments, numerical claims,
  and deletion of existing evidence-bearing material;
- require approval for whole-abstract rewrites, section deletion, or any operation that
  could alter contribution identity;
- map every intended edit to a weakness ID or venue requirement.

The whitelist is the machine boundary; prose instructions are not a substitute.

## 5. Run Bounded Improvement

Invoke `/auto-paper-improvement-loop` once with the destination directory, whitelist,
and human checkpoint enabled. Its fresh reviewers judge the current artifact without
seeing prior scores, desired acceptance outcome, or style exemplars.

Accept only edits mapped to a weakness ID, venue rule, or independently verified
artifact defect. At most two rounds are allowed. Do not trigger another round merely
because a reviewer score remains low.

## 6. Run Only The Audits Actually Affected

Use the single audit owners:

- changed numerical or semantic claims: `paper-writing mode: claim-audit`;
- changed citation contexts: `/research-audit mode: citation --soft-only`;
- changed theorem wording or restatements: `/research-review` proof audit;
- uncertain underlying result validity: `/research-audit mode: experiment`;
- final scientific identity/headline risk: `/research-review` artifact review.

There is no separate `headline` audit mode. Do not rerun unchanged audits whose input
hashes and semantics remain fresh.

## 7. Compile And Compare

Use `paper-writing mode: compile` with the target template. Check page limit, fonts,
bibliography, references, figure readability, overflow, anonymity, and supplementary
packaging.

Generate a source-to-target diff and classify every change:

- venue/template migration;
- reviewer-mapped scientific clarification;
- scope/claim qualification;
- anonymity;
- layout-only;
- unexpected or out-of-boundary.

Any unexpected scientific change blocks completion until reconciled. Never push to
Overleaf, GitHub, or another remote without explicit authorization.

## Completion Criteria

Complete only when:

- source submission remains unchanged;
- target compiles and meets venue/anonymity rules;
- every accepted edit maps to a concern or venue requirement;
- no forbidden operation occurred;
- affected audits are fresh and non-blocking;
- no unresolved concern is misrepresented as solved;
- contribution identity and frozen results remain unchanged.

## Output

Write `RESUBMIT_REPORT.md` with source/destination hashes, concern mapping, edit
boundary, round summaries, rejected recommendations, source diff classification,
compile/anonymity status, affected audits, unresolved science, and deliverable paths.
Keep reviewer traces under the destination's trace directory when configured.
