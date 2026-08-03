# FIRM Agent Guide

This file is for AI coding and research agents helping a user adopt FIRM.
Humans should start with the [README](../README.md) or the
[getting-started guide](getting-started.md).

## Product Identity

FIRM is the PI layer for long-horizon agentic research. It is not a promise to
produce a paper and not a rigid stage machine. Its job is to preserve a valuable
research program while evidence changes the concrete problem, method, and paper
identity.

## Install Into A Project

From the FIRM repository:

```bash
./firm init /absolute/path/to/research-project
./firm doctor /absolute/path/to/research-project
```

Do not overwrite user project files manually. The launcher:

- installs project-local skills under `.claude/skills/`;
- backs up same-named skill directories;
- preserves an existing `CLAUDE.md` before appending a marked FIRM block;
- creates `.firm/RESEARCH_PROGRAM.md`;
- creates first-message templates for a new project and an existing-project
  audit.

## Start The Researcher

For a new program, use `.firm/FIRST_MESSAGE_NEW.md`.

For an existing project, use `.firm/FIRST_MESSAGE_AUDIT.md` before launching
more experiments. Reconstruct the original program, current evidence, contrary
evidence, method lineage, scope debt, paper identity, active work, and one next
action.

## Behavioral Invariants

1. Keep the original broad program separate from the current paper.
2. Let credible evidence form the concrete problem.
3. Treat a competent negative method result as design evidence, not a reason
   for ceremonial seed expansion.
4. Preserve successful components and construct the next realization.
5. Use an independent second PI before major compute, identity, or manuscript
   commitments.
6. Do not let unavailable review infrastructure pause lead-researcher work.
7. Keep one compact authoritative project state.
8. Do not begin full manuscript production before evidence-bearing paper entry.

Read `skills/research-pipeline/SKILL.md` for the persistent research role and
`skills/INDEX.md` for specialist activation.
