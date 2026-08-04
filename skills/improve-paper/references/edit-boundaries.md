# Edit boundaries

An edit whitelist may contain explicit paths or glob patterns. Resolve it relative
to the paper root and print the resolved set before editing.

## Allowed

- direct edits to resolved files;
- generated PDFs and build artifacts in declared output directories;
- temporary files outside the repository when needed for compilation.

## Forbidden without explicit expansion

- editing included files outside the resolved set;
- renaming or moving files to evade the boundary;
- changing bibliography, figures, templates, scripts, or data not listed;
- changing git configuration, hooks, remotes, or submodules;
- broad formatting commands that touch the whole repository;
- staging, committing, pushing, deleting, or installing software.

At the end of every round, compare the working-tree diff with the resolved whitelist
and report any violation before proceeding.
