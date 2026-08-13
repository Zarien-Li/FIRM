---
name: improve-paper
description: Runs a bounded review-fix-recompile loop over an existing research paper while preserving claims, equations, labels, and user-specified edit boundaries.
when_to_use: Invoke explicitly when a draft already exists and the user wants one or two disciplined improvement rounds rather than an open-ended rewrite.
argument-hint: "[paper directory] [--style-ref source] [--edit-whitelist path]"
disable-model-invocation: true
---

# Improve an Existing Paper

Run a bounded, evidence-preserving review → fix → recompile loop. The goal is a
clearer and more defensible paper, not a higher-looking review score or a silent
change of contribution identity.

## Defaults

- two rounds maximum;
- fresh independent reviewer context for each round;
- compile and inspect after each round;
- preserve raw evidence, equations, theorem meaning, labels, citations, and venue
  constraints unless a verified correction requires a change;
- stop early when no blocking or major issue remains.

Use the paper directory and options in `$ARGUMENTS`.

## Optional controls

### `--style-ref <source>`

Use a user-provided paper or style source only for author-side organization,
section rhythm, and presentation patterns. Do not copy wording, structure unique to
the source, or scientific content. Do not show the style source or a derived style
summary to the independent reviewer.

### `--edit-whitelist <path>`

Restrict modifications to explicitly allowed files or globs. Resolve and record the
whitelist before editing. Do not bypass it through generated files, shell commands,
renames, or indirect includes. See
[references/edit-boundaries.md](references/edit-boundaries.md).

## 1. Preserve the starting point

Before edits:

- locate the root TeX file and build command;
- record the current git status;
- copy or tag the starting PDF when practical;
- identify the contribution identity and claims-evidence map;
- record the edit whitelist and files outside it;
- compile once to establish the baseline and capture existing errors.

Do not stage, commit, push, install packages, or modify unrelated project files
without explicit user authorization.

## 2. Round 1: independent review

Review the full compiled paper in a fresh context. Supply:

- the paper and relevant source files;
- the venue or target audience when known;
- the claims-evidence map and raw paths needed to verify consequential claims;
- a neutral rubric.

Do **not** supply prior scores, desired outcomes, fix plans, style exemplars, or a
summary of what the author hopes the reviewer will say.

The review should classify findings:

- `BLOCKING`: correctness, evidence, attribution, contribution identity, or
  submission compliance;
- `MAJOR`: structure, missing explanation/control, unclear method, overclaiming, or
  serious readability;
- `MINOR`: local wording, notation, layout, and polish.

Require file/section locations and concrete repairs. Use
[references/review-rubric.md](references/review-rubric.md).

## 3. Implement Round 1 fixes

Prioritize blocking, then major, then high-value minor issues. For every proposed
edit:

1. verify the issue against source and evidence;
2. decide whether to accept, modify, or reject the recommendation;
3. apply the smallest coherent edit inside the allowed boundary;
4. preserve contribution identity unless the user explicitly requested a reframe;
5. record the change and rationale.

Do not blindly implement reviewer suggestions that weaken scientific correctness,
request unsupported claims, or conflict with the actual evidence.

## 4. Recompile and inspect

Use the existing build workflow. Fix causal compile errors, undefined references,
duplicate labels, missing figures, and serious overflow. Inspect the rendered PDF,
not only the log.

For theory papers, compare restated theorems, assumptions, and equations after edits.
For empirical papers, re-check every changed numerical claim against raw artifacts.

Save the round PDF with a clear non-authoritative name such as
`main_round1.pdf`; do not overwrite the only known-good PDF until the round passes.

## 5. Round 2: fresh review

Start a new independent reviewer context with the current artifact. Do not say “we
fixed your previous comments,” reveal the Round 1 review, or ask for score
improvement. The reviewer should judge the paper as it now stands.

Implement only remaining blocking and major issues plus clearly worthwhile minor
fixes. Stop if the second review requests an open-ended new research program rather
than paper improvement; return those items as future research or evidence gaps.

## 6. Final verification

After the final compile:

- run `/firm:audit-citations` only if citation contexts changed or no fresh audit exists;
- verify only changed claims and numbers against raw evidence, reusing unchanged checks;
- check venue, anonymity, page, and artifact constraints supplied by the user or
  current authoritative instructions;
- inspect title, abstract, contribution bullets, figures, tables, limitations, and
  conclusion for a single consistent paper identity;
- ensure no file outside the whitelist changed;
- ensure no secret, private path, or temporary artifact entered the source archive.

Do not invoke `/firm:audit-research` or a new second-PI scientific review after every
round. If a proposed edit changes contribution identity or requires new science, end
the writing loop and return that issue to the research state.

## 7. Improvement log

Write `PAPER_IMPROVEMENT_LOG.md`:

```markdown
# Paper Improvement Log

## Starting point
- Root TeX:
- Baseline PDF:
- Build command:
- Contribution identity:
- Edit boundary:

## Round 1
### Review findings
| Severity | Location | Issue | Decision |
|---|---|---|---|

### Implemented changes
| File | Change | Evidence/rationale |
|---|---|---|

### Rejected recommendations
| Recommendation | Reason |
|---|---|

### Compile and visual check

## Round 2
...

## Final verification
- Compile:
- Claim check:
- Citation audit:
- Whitelist check:
- Remaining blocking/major issues:

## Deliverables
```

Report unresolved issues honestly. A bounded loop is successful when it improves
the paper without contaminating its evidence or identity, even if it does not make
every reviewer preference disappear.
