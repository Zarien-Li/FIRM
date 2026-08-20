# Submission Assembly And Final Report

Use only for `assurance: submission`. Draft and research-draft work do not require all
submission artifacts.

## Re-Derive The Boundary

Before finalization, read current user instructions and `PAPER_ENTRY.md`; do not trust a
stale state label. Confirm the contribution identity, claimed population, primary
metric, decisive incumbent, and positive object still match the compiled paper and raw
evidence.

If identity changed, stop submission finalization and obtain user approval plus a new
paper-entry review. Do not repair identity drift through wording alone.

## Required Independent Checks

Run only checks whose owner and input surface apply:

1. `/research-audit mode: experiment` for unaudited or changed claim-bearing
   experiment/evaluator/provenance;
2. `paper-writing mode: claim-audit` for manuscript numbers and semantic qualifiers;
3. `/research-audit mode: citation` for bibliography identity and citation context;
4. `/research-review` proof audit when formal claims exist;
5. `/research-review` artifact review for final scientific prize, identity, title,
   scope, alternatives, and likely reviewer objections.

Do not give artifact reviewers prior scores, desired outcomes, fix summaries, style
exemplars, or other audit verdicts. Give the paper and raw evidence packet needed to
judge it.

Reuse an audit when its declared inputs, hashes, and semantics remain unchanged. Rerun
only checks affected by later edits.

## Validate Audit Artifacts

For every required JSON artifact verify:

- expected audit identity and schema;
- verdict is not `FAIL`, `BLOCKED`, or `ERROR`;
- declared input set covers the files/claims under review;
- recomputed hashes match;
- reviewer/thread/time and trace are present when required;
- `WARN` qualifiers appear in the manuscript and final report.

Missing, malformed, or stale artifacts block only the final readiness claim. A
host-provided verifier may automate these checks, but the workflow must not depend on a
private repository or script.

## Venue And Package Check

Using authoritative venue rules, verify:

- anonymity and metadata;
- page and supplementary limits;
- fonts, margins, bibliography style, and required sections;
- figure/table readability and accessibility;
- artifact/data/code statements and ethics/limitations when applicable;
- no credentials, private paths, review identities, temporary files, or hidden author
  metadata in the submission package.

Do not upload or formally submit without explicit user approval.

## Final Report

Write `PAPER_REPORT.md`:

```markdown
# Paper Report

## Contribution identity
- problem, positive object, contribution type, scope:
- decisive evidence and paper-to-program bridge:

## Deliverables
- root source / PDF / figures / package:

## Verification
| Check | Artifact | Verdict | Freshness | Remaining qualifier |
|---|---|---|---|---|

## Compilation and venue compliance
## Blocking / major / minor remaining issues
## Honest non-claims and limitations
## User approval still required
## Single next action
```

Use `submission-ready: yes` only when paper entry, compilation, applicable audits,
venue compliance, and disclosure are all green. A polished PDF alone is not readiness.
