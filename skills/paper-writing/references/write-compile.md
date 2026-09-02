# LaTeX Writing And Compilation

Use for section-level source edits and PDF production. Locate the root file, includes,
bibliography system, venue template, macros, existing build command,
`AUTHOR_ARGUMENT.md`, and `PAPER_PLAN.md`. Preserve established notation, labels,
citations, and template conventions.

## Write From Evidence

Draft from raw evidence and the author argument. Every number must come from an
artifact or generated table; causal and generalization language must survive the
post-draft claim check. Do not invent citations or results. Use an editable source for
architecture diagrams and make every visual element explain implemented computation.

## Build And Repair

Prefer the project's `Makefile`, `latexmkrc`, or documented build script; otherwise use
`latexmk` or explicit engine and bibliography passes inferred from the source. Do not
install system packages, use `sudo`, change templates, or switch engines merely to hide
an error without authorization.

Compile with file and line diagnostics. Fix the first causal error, rebuild, and repeat.
Common causes include missing or duplicate labels and keys, absent figures or data,
malformed math/tables/environments, incompatible packages, and stale generated files.
Do not delete scientific content, citations, assumptions, or figures to obtain a clean
exit.

## Inspect The Rendered Artifact

Inspect every page at final size for clipping, overlap, blanks, glyph and equation
problems, unreadable figures or tables, misplaced floats, visible overflow, page limit,
margins, headers, anonymity, and bibliography layout. Warnings require inspection, not
automatic failure.

When edits change empirical values or qualifiers, run `claim-audit` on affected claims.
When they change citation contexts or formal statements, use the corresponding
`research-review` audit. Unchanged evidence-bound checks remain valid.

Update `COMPILE_REPORT.md` with the root, engine, command, PDF path, page count, causal
errors repaired, remaining warnings and visible impact, visual inspection, files
changed, and affected check status. Success requires a coherent rendered artifact, not
only exit code zero.
