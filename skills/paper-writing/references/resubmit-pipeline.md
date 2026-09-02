# Resubmit An Existing Paper

Use this mode for a bounded venue transfer when a prior submission and reviews exist,
the target venue is user-selected, the contribution and results are frozen, and the
allowed edits are explicit. Structural rewriting, new science, or a changed paper
identity returns to ordinary writing or research.

## Isolate The New Submission

Resolve the source submission and its PDF/source hashes, target venue rules, reviewer
corpus, edit boundary, and a destination that does not yet exist. Create a sibling
directory and copy only the source, figures, bibliography, and build files needed for
the target. Exclude caches, credentials, private notes, review traces, and unrelated
artifacts. Preserve the original submission unchanged.

Record source and destination paths and hashes, venues, frozen identity and results,
edit boundary, phase, and build status in `.resubmit/STATE.md`.

Compile the copy before editing so pre-existing failures remain distinguishable. Check
the authoritative target template and rules. Scan source, rendered metadata,
acknowledgements, comments, filenames, URLs, supplements, self-citations, and generated
artifacts for identity leakage; anonymize only what the venue requires.

## Map Concerns To Permitted Repairs

Create `KNOWN_WEAKNESSES.md` with each reviewer concern, current evidence, whether it
is already resolved, text-fixable, format-related, dependent on new science, or based
on an incorrect premise, plus the allowed repair and manuscript location.

Clarification, qualification, reorganization, and honest limitation may be text fixes.
Do not weaken related work, hide contrary results, or promise unperformed work. A
blocking concern that requires new evidence leaves the resubmit boundary; ask the user
whether to reopen research only when that changes an explicit locked scope.

Translate the approved repairs into `.resubmit/edit_whitelist.yaml`:

- allow only destination source and target-layout files needed for mapped edits;
- protect the prior submission, raw results, code, bibliography, style files, citations,
  theorems, and evidence-bearing material unless explicitly authorized;
- mark operations that require approval, such as deleting a section or changing the
  contribution identity;
- associate every intended edit with a weakness ID or venue requirement.

The whitelist is the mutation boundary. Do not bypass it through generated files,
renames, shell operations, or includes.

## Revise And Verify

Run `paper-writing mode: improvement` on the destination with the whitelist. Accept
only edits mapped to a concern, venue rule, or independently verified artifact defect.
Use at most two reader rounds, each justified by a remaining communication problem.

Run only checks affected by actual edits: `claim-audit` for changed empirical claims,
`research-review` for changed citation contexts or proofs, and experiment audit only
when the validity of underlying evidence is genuinely uncertain. Compile and inspect
through `paper-writing mode: compile` using the target template.

Generate a source-to-target diff and classify each change as venue migration,
reviewer-mapped clarification, scope qualification, anonymity, layout, or unexpected.
An unexpected scientific change blocks completion until reconciled.

## Deliver

Complete when the source remains unchanged, the destination meets venue and anonymity
rules, every accepted edit maps to its authority, affected checks are fresh, unresolved
concerns are represented honestly, and the contribution identity and frozen results
remain intact. Do not upload or push externally without explicit authorization.

Write `RESUBMIT_REPORT.md` with source/destination hashes, concern mapping, edit
boundary, reader-round summary, rejected edits, diff classification, compilation and
anonymity status, affected checks, unresolved science, and deliverable paths.
