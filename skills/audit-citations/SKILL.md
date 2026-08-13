---
name: audit-citations
description: Independently verifies that bibliography entries are real, correctly attributed, and used in contexts the cited sources actually support.
when_to_use: Invoke explicitly before submission or when checking hallucinated papers, wrong authors or years, venue and version mismatches, unsupported citation contexts, or uncited bibliography entries.
argument-hint: "[paper directory] [--uncited] [--soft-only]"
disable-model-invocation: true
context: fork
background: false
---

# Citation Audit

Audit the bibliography and every consequential citation context from a fresh
reviewer perspective. A syntactically valid BibTeX entry is not enough: the work
must exist, its metadata must be correct, and the surrounding sentence must not
claim more than the source establishes.

This skill owns citation identity, metadata, and contextual support only. Manuscript
numbers belong to `write-paper`, experiment provenance to `audit-experiment`,
scientific importance and paper identity to `second-pi`, and state maturity to
`audit-research`. A citation finding repairs attribution or wording; it cannot create
science or become another headline review. Reuse an audit when bibliography and
citing-context hashes are unchanged.

## Inputs and modes

Use the paper directory in `$ARGUMENTS`, or infer it from the current project.
Recognize two optional modes:

- `--uncited`: also list bibliography entries never cited in the manuscript;
- `--soft-only`: do not delete or replace citations automatically; propose wording
  that accurately narrows the citing sentence when possible.

Do not treat a manuscript draft, prior audit, or generated bibliography summary as
an authoritative source.

## 1. Discover the citation surface

Locate:

- `.bib` files and any inline `thebibliography` blocks;
- the root TeX file and all included section files;
- citation commands such as `\cite`, `\citep`, `\citet`, `\parencite`, and
  project-specific variants;
- bibliography style or venue constraints when relevant.

Build a mapping from each citation key to every citing sentence or paragraph, with
file and line location. Preserve multi-citation groups: each source must support
its own implied portion of the claim.

## 2. Verify bibliographic identity

For every cited entry, use authoritative or primary sources whenever possible:

1. publisher or proceedings page;
2. DOI/Crossref metadata;
3. DBLP for computer-science metadata;
4. arXiv or the authors' official paper page;
5. a trusted scholarly index only when primary pages are unavailable.

Check:

- title;
- complete and ordered author list;
- publication year;
- venue or journal;
- volume, issue, pages, DOI, and arXiv identifier when present;
- whether the cited version is a preprint, workshop paper, conference paper, or
  journal extension;
- duplicate entries under different keys.

Do not infer metadata from search snippets. Open the source page or paper.

## 3. Verify contextual support

Read enough of the cited work—abstract, relevant section, method, result, or
limitation—to judge the citing sentence. Classify each citation context:

- `SUPPORTED`: the source directly supports the claim at the stated scope;
- `PARTIAL`: the source supports a narrower or related claim;
- `BACKGROUND_ONLY`: the source is relevant but does not establish the asserted
  result or mechanism;
- `CONTRADICTED`: the source conflicts with the citing sentence;
- `UNVERIFIABLE`: the source or relevant content cannot be reliably accessed;
- `WRONG_SOURCE`: another work appears to be intended.

Check especially:

- “first,” “only,” “state of the art,” and broad field-summary claims;
- numerical results and dataset sizes;
- causal or mechanistic statements;
- attribution of a method to the correct paper;
- claims transferred from one task, model scale, or population to another;
- citations attached to several clauses that only support one clause.

## 4. Choose the least destructive repair

For each issue, recommend one action:

- `KEEP`: metadata and context are correct;
- `FIX_METADATA`: same work, incorrect BibTeX fields;
- `NARROW_SENTENCE`: retain the citation but reduce the claim to what it supports;
- `SPLIT_CLAIM`: separate supported and unsupported clauses;
- `ADD_SOURCE`: current source is insufficient; add a direct source;
- `REPLACE_SOURCE`: a different work was clearly intended;
- `REMOVE_CITATION`: source is irrelevant or fabricated;
- `MANUAL_CHECK`: evidence remains ambiguous.

Under `--soft-only`, prefer `NARROW_SENTENCE`, `SPLIT_CLAIM`, or `MANUAL_CHECK` and
show the exact proposed rewrite. Never silently invent a replacement reference.

## 5. Apply changes only with traceability

When the user asked for fixes, edit only after producing the audit table. Before
changing files:

- preserve the original BibTeX and citing sentence in the report;
- record the authoritative source used;
- distinguish metadata correction from claim correction;
- do not alter unrelated prose;
- re-run citation-key and LaTeX checks after edits.

Do not add a paper merely because its title sounds relevant. Verify it first.

## 6. Recompile and check

After approved edits:

- compile the paper using the project's existing workflow;
- check undefined citations and duplicate keys;
- verify that every edited key resolves;
- ensure the bibliography output reflects the corrected metadata;
- confirm that no citation command or brace was broken.

## Output

Write `CITATION_AUDIT.md` in the paper directory when permitted.

```markdown
# Citation Audit

## Summary
- Cited keys:
- Verified works:
- Metadata issues:
- Context issues:
- Unverifiable entries:
- Uncited entries:  # only with --uncited

## Priority fixes

## Entry-by-entry audit
| Key | Identity | Metadata | Context | Action | Evidence source |
|---|---|---|---|---|---|

## Detailed issues
### `key` — ACTION
- Location:
- Current sentence:
- What the source actually supports:
- Metadata correction, if any:
- Proposed rewrite or replacement:
- Authoritative verification source:

## Uncited bibliography entries

## Remaining manual checks
```

For a machine-readable companion, use the schema in
[references/audit-schema.md](references/audit-schema.md).

## Non-negotiable rules

- Never mark an entry verified from title similarity alone.
- Never fabricate a DOI, venue, author, page range, or replacement citation.
- Never use a prior model's citation summary as the sole evidence.
- Do not quote large portions of copyrighted papers; record concise supporting
  evidence and source locations.
- If access is insufficient, say `UNVERIFIABLE` and identify the exact missing
  verification.
