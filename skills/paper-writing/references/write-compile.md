# LaTeX Writing And Compilation

Load for `write` or `compile` mode.

## Write From The Author Argument And Evidence

Locate the root file, section includes, bibliography system, venue template, existing
macros, `AUTHOR_ARGUMENT.md`, and `PAPER_PLAN.md`. Preserve established notation,
labels, citations, and template conventions. Use raw evidence while drafting. Create or
refresh `CLAIMS_EVIDENCE.md` only after a narrative draft exists, then use it to repair
unsupported claims rather than to generate paragraph order or prose.

Every numerical value comes from a raw artifact or generated table. Every
causal/mechanism/generalization word must survive the post-draft claim check. Do not add
invented citations or results. Preserve the author argument, field-natural language,
and paragraph movement while repairing factual issues.

For architecture illustrations, use a source-editable representation and record the
scientific job of each visual element. Decorative complexity cannot replace an
explanatory diagram.

## Select The Existing Build Workflow

Prefer, in order:

1. project `Makefile`, `latexmkrc`, or documented script;
2. `latexmk` with the correct engine and bibliography backend;
3. explicit `pdflatex`/`xelatex`/`lualatex` plus BibTeX/Biber passes inferred from the
   source.

Do not install system packages, use `sudo`, change the venue template, or switch engine
merely to hide an error without explicit approval. If a dependency is missing, report
the exact package/tool and ask the environment owner to install it.

## Repair Causally

Compile with file/line errors and preserve the log. Fix the first real error, rebuild,
and repeat. Common causal classes:

- missing/duplicate labels or bibliography keys;
- unresolved references or citations;
- missing figure/data files;
- malformed tables, math, braces, or environments;
- incompatible packages or engine assumptions;
- stale generated files masking source changes.

Do not delete scientific content, comments, citations, theorem assumptions, or figures
to make compilation pass. Record material source changes.

## Inspect The Rendered PDF

Render or open the PDF and check every page at final size:

- clipping, overlap, blank pages, missing glyphs, broken equations;
- illegible figure labels, legends, colors, or table text;
- floats separated from their discussion;
- overfull boxes that visibly damage the main body;
- page count, margins, headers, anonymity, and bibliography layout;
- consistency of title, abstract, contribution bullets, captions, limitations, and
  conclusion.

Warnings are evidence to inspect, not automatic blockers. Classify them by visible
impact and venue relevance.

## Formal And Empirical Regression Checks

If theorem wording, assumptions, or equations changed, compare every restatement and
invoke `/research-review` proof audit when the change is consequential.

If numerical claims or semantic qualifiers changed, invoke `paper-writing mode:
claim-audit` for affected files. If citation contexts changed, invoke
`/research-audit mode: citation` for affected contexts. Unchanged green checks need not
be repeated.

## Output

Write or update `COMPILE_REPORT.md`:

```markdown
# Compile Report
- root / engine / command:
- status and PDF path:
- page count and venue limit:
- errors fixed:
- remaining warnings and visible impact:
- visual inspection:
- changed files:
- affected audits required/completed:
```

Never claim success from exit code alone; a valid final artifact must compile and render
coherently.
