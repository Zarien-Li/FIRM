# Human-Reader Paper Improvement

Use after the contribution identity and evidence are stable. Improve authorial voice,
field-natural language, paragraph movement, specificity, memorability, fidelity, and
presentation. This is editing for readers, not reviewer-score optimization or a way to
change the science silently.

## Prepare The Round

Read the paper, author argument, plan, available post-draft claim map, build command,
venue constraints, and current changes. Compile once and preserve the known-good PDF.
An edit that requires new science or a changed contribution returns that precise gap to
`research-pipeline`; do not write around it.

Normally use one or two rounds. Each round must have a concrete opportunity to improve
meaning or reader understanding. Use an optional near-final independent check only for
a named factual, claim, citation, or proof uncertainty, not as a reviewer ritual.

## Respect An Optional Edit Boundary

When an edit whitelist is supplied, resolve it before editing. It may define allowed
and forbidden paths, forbidden additions or deletions, approval-required operations,
and a maximum edit count. Denial overrides allowance. Log rejected edits with their
location, proposed operation, rule, and unresolved consequence. Do not bypass the
boundary through shell commands, generated files, renames, or includes.

A style reference guides author-side structure only. Never copy its wording or expose
it to factual auditors or human-reader editors.

## Run One Human-Reader Round

Give a fresh editor the compiled paper and only the context an intended reader would
reasonably have. The editor is not a reviewer: it does not score acceptance, request
experiments, enumerate objections, or apply a severity taxonomy.

After a natural ten-minute read, the editor writes from memory:

- the problem;
- the prior belief;
- the surprising fact or principle;
- why it matters;
- the idea most likely to remain memorable.

It then writes a short editorial letter locating where attention broke, paragraph
movement became unclear, language stopped sounding field-natural, jargon displaced
concrete experience, or authorial voice disappeared. Exact locations are useful;
checklists are not.

Compare this retelling with `AUTHOR_ARGUMENT.md` and revise where the intended argument
did not survive reading. Propagate changes in notation, terminology, or claim strength
across every affected section, caption, and appendix; the main writing reference owns
caveat placement and prose principles.

Compile and inspect through `paper-writing mode: compile`. Rerun claim, citation, or
proof checks only where edits changed their inputs or semantics.

Append a compact entry to `PAPER_IMPROVEMENT_LOG.md` containing the starting and ending
PDFs, editor identity, remembered retelling, mismatches repaired, files changed,
whitelist rejections, compile/audit status, unresolved issues, and whether another
round has a concrete purpose.

## Converge

If a second round is useful, use a new editor who sees only the current artifact and
does not know Round 1's changes. Stop when an intended reader can accurately retell the
problem, changed belief, surprise, significance, and takeaway; the prose has a coherent
voice; paragraphs advance the argument; and the affected production and evidence checks
pass.

Do not add a third round automatically. Continue only when another pass can improve
meaning, voice, specificity, or memorability. A new scientific gap returns to research;
a changed paper identity returns to the writing boundary.

Report the starting and final PDFs, reader retelling before and after, important edits,
compile and affected-audit status, whitelist compliance, and any remaining scientific
gap. Do not use predicted reviewer-score movement as the success criterion.
