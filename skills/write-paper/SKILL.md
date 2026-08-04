---
name: write-paper
description: Plans, drafts, compiles, and verifies a research paper from validated evidence, with a claims-to-evidence spine and submission-oriented checks.
when_to_use: Invoke explicitly for a paper outline, structural rewrite, section drafting, complete LaTeX-to-PDF workflow, or verification that manuscript numbers match raw results.
argument-hint: "[paper directory, outline, or section]"
disable-model-invocation: true
---

# Write a Research Paper

Produce a paper whose claims, numbers, figures, and scope are traceable to validated
project evidence. Do not use prose quality to compensate for an immature or
contradicted contribution.

## 1. Establish the writing boundary

Read the current research state, raw results, method notes, experiment plan,
relevant audits, venue template, and existing manuscript. Determine whether the
request is:

- exploratory outlining;
- section-level drafting or rewriting;
- full manuscript production;
- compilation and repair;
- submission-oriented verification.

For full submission-oriented writing, confirm that the current bounded contribution
has:

- an important natural or standard research object;
- a real implemented method or a clearly defined empirical thesis;
- a fair strong comparison;
- paper-critical evidence with credible provenance;
- an honest scope and known limitations.

When these are absent, write only the requested exploratory artifact and label the
missing evidence. Use `/firm:audit-research` when paper readiness is genuinely
unclear.

## 2. Build the claims-to-evidence spine

Before drafting, create or update `CLAIMS_EVIDENCE.md`:

```markdown
| ID | Intended claim | Evidence and raw path | Scope | Figure/table | Risk |
|---|---|---|---|---|---|
| C1 | | | | | |
```

Every headline claim must map to raw evidence. Distinguish:

- observation from explanation;
- development result from final evaluation;
- selected slice from intended population;
- correlation from causal evidence;
- method contribution from analysis contribution;
- measured result from interpretation or hypothesis.

Do not draft a stronger sentence than the evidence row supports.

## 3. Plan the paper around one contribution identity

Write `PAPER_PLAN.md` with:

- one-sentence problem;
- one-sentence contribution;
- positive object: what works, is explained, or is newly enabled;
- load-bearing primitive or thesis;
- decisive baseline and primary metric;
- paper-to-program bridge;
- section purpose and required evidence;
- figure/table plan;
- limitations and non-claims.

Use the detailed planning checklist in
[references/planning.md](references/planning.md). If the contribution type,
positive object, method primitive, primary metric, or claimed population changes,
stop and explicitly update the paper identity before continuing.

## 4. Draft evidence-first

Recommended order:

1. results and evidence-bearing figures/tables;
2. method, assumptions, and complexity;
3. experimental setup and comparison fairness;
4. introduction and contributions;
5. related work;
6. limitations, ethics, and conclusion;
7. abstract and title last.

For each section:

- state its job before writing;
- use exact values from raw artifacts or generated tables;
- explain why a comparison is decisive, not merely that it is larger;
- place caveats next to the affected claim;
- avoid invented citations, generic novelty language, and unsupported causal verbs;
- preserve notation and terminology across sections.

Reference papers may be studied for organization and rhetorical patterns, but never
copied or used as evidence. Keep author-side style study separate from independent
review.

## 5. Generate figures and tables from sources

Use `/firm:make-figures` for nontrivial plots. Every figure or table must have:

- a documented data source;
- a script or reproducible generation path when possible;
- readable labels at final paper size;
- units, uncertainty, and sample definition;
- a caption that states the comparison and takeaway without exceeding the data;
- no decorative element that obscures the scientific message.

Never transcribe important numbers manually when they can be generated from result
files.

## 6. Compile and repair systematically

Use the project's existing build command first. If none exists, inspect the root
TeX file and bibliography system before choosing `latexmk`, `pdflatex`, `xelatex`,
or `lualatex`. Do not install system packages or use `sudo` without explicit user
approval.

Follow [references/latex-and-compilation.md](references/latex-and-compilation.md).
Fix the first real error, recompile, and repeat. Do not hide errors by deleting
content or switching templates. Preserve a compile log and final PDF path.

## 7. Run independent checks

For submission-oriented work, run these as separate fresh passes:

1. **Claim audit:** verify manuscript claims and numbers against raw evidence using
   [references/claim-audit.md](references/claim-audit.md).
2. **Citation audit:** invoke `/firm:audit-citations`.
3. **Scientific review:** invoke `/firm:second-pi` on the compiled paper and raw
   evidence packet.
4. **Experiment integrity:** invoke `/firm:audit-experiment` only when the relevant
   evidence has not already been audited or provenance is uncertain.

Do not give an independent reviewer prior scores, fix summaries, desired outcomes,
or style exemplars. Review the artifact, evidence, and explicit evaluation rubric.

## 8. Apply fixes without claim drift

Classify review findings:

- `BLOCKING`: correctness, evidence, attribution, or contribution identity;
- `MAJOR`: missing explanation, comparison, limitation, or structural clarity;
- `MINOR`: wording, notation, formatting, and local presentation.

Fix blocking issues first. After edits, recompile and re-run affected checks. Do not
silently change the primary metric, population, baseline, or contribution type to
make the paper pass.

Use `/firm:improve-paper` only after the evidence and identity are stable.

## 9. Final report

Return:

```markdown
# Paper Writing Report

## Contribution identity
- Problem:
- Contribution:
- Scope:
- Primary evidence:

## Deliverables
- Root TeX:
- PDF:
- Claims-evidence map:
- Figure/table sources:

## Verification
- Compilation:
- Claim audit:
- Citation audit:
- Independent review:

## Remaining issues
- Blocking:
- Major:
- Minor:

## Honest non-claims and limitations

## Next action
```

For a final submission pass, use
[references/submission-checklist.md](references/submission-checklist.md).
