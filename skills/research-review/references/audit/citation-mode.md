# Mode: Citation And Source Integrity

Verify that every cited work exists, its metadata is correct, and each local citation
context says no more than the source establishes. Run once near submission or after
material citation-context changes, not after every draft save.

Options:

- `--uncited`: also report bibliography entries never cited;
- `--soft-only`: preserve bibliography and citation keys; propose accurate wording or
  manual checks instead of deleting/replacing sources.

## Discover The Citation Surface

Locate root/section files, `.bib` files or inline bibliography, bibliography style, and
all citation commands. Map each key to every citing sentence/paragraph with file and
line. Preserve multi-citation groups while judging what each source supports.

## Verify Identity From Authoritative Sources

Prefer:

1. publisher or proceedings page;
2. DOI/Crossref metadata;
3. DBLP for computer-science metadata;
4. arXiv or official author page;
5. trusted scholarly index only when primary sources are unavailable.

Open the source; do not verify from title similarity or search snippets. Check title,
ordered authors, year, venue, volume/issue/pages, DOI/arXiv ID, version type, retraction
or correction status when relevant, and duplicate entries under different keys.

## Verify Contextual Support

Read enough of the abstract and relevant section/result/limitation to classify every
context:

- `SUPPORTED`: directly supports the stated claim and scope;
- `PARTIAL`: supports a narrower or related claim;
- `BACKGROUND_ONLY`: relevant but not evidence for the asserted result/mechanism;
- `CONTRADICTED`;
- `WRONG_SOURCE`;
- `UNVERIFIABLE`.

Scrutinize “first/only/SOTA” claims, numbers, causal or mechanism attribution, method
ownership, task/model/population transfer, and sentences where one citation is made to
support several clauses.

## Choose The Least Destructive Repair

Assign one action:

- `KEEP`;
- `FIX_METADATA`;
- `NARROW_SENTENCE`;
- `SPLIT_CLAIM`;
- `ADD_SOURCE` after verifying a direct source;
- `REPLACE_SOURCE` when the intended source is verified;
- `REMOVE_CITATION` for irrelevant/fabricated entries;
- `MANUAL_CHECK` when access is insufficient.

Under `--soft-only`, use only `KEEP`, `FIX_METADATA` when allowed,
`NARROW_SENTENCE`, `SPLIT_CLAIM`, or `MANUAL_CHECK`. Never invent a replacement.

## Apply And Recompile Only When Requested

The audit itself emits findings. If fixes are requested, first preserve the original
BibTeX and sentence plus the authoritative source used. Distinguish metadata repair
from claim repair, edit only affected text/entry, then use `paper-writing mode:
compile` to check undefined citations, duplicate keys, bibliography output, and broken
commands.

## Verdict And Output

Use:

- `PASS`: cited identities and contexts are supported;
- `WARN`: metadata or wording repair is needed but the source relationship survives;
- `FAIL`: fabricated/wrong/contradictory citation materially supports a claim;
- `BLOCKED`: consequential entries cannot be accessed or verified;
- `NOT_APPLICABLE`: no citations;
- `ERROR`: audit failed.

Write `CITATION_AUDIT.md`:

```markdown
# Citation Audit
- cited keys / contexts:
- verdict:
- reviewer/thread/time:

## Priority fixes
## Entry-by-entry audit
| Key | Location | Identity | Metadata | Context | Action | Primary source |
|---|---|---|---|---|---|---|

## Detailed issues
- current sentence:
- what the source supports:
- exact repair:

## Uncited entries  # only with --uncited
## Remaining manual checks
```

At submission assurance also write `CITATION_AUDIT.json` using the shared assurance
schema with declared input hashes and per-context details. Keep concise source
locations; do not reproduce copyrighted text beyond what verification requires.

Never mark an entry verified from another model's summary, fabricate metadata, or
silently alter bibliography/claims during the audit.
