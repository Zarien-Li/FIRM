# Getting Started

FIRM is distributed as a Claude Code plugin. The plugin path is recommended
because it provides clean `/firm:` command names, updates, and no collisions with
other skills.

## Install the plugin

In Claude Code:

```text
/plugin marketplace add Zarien-Li/FIRM
/plugin install firm@firm-research
/reload-plugins
```

Confirm the install:

```text
/help
```

Search for commands beginning with `/firm:`.

## First useful calls

For an existing research project:

```text
/firm:research "Reconstruct the original program, current evidence, method lineage, scope debt, and one next action"
```

For a completed result:

```text
/firm:diagnose-result path/to/result.json
```

For an independent critique:

```text
/firm:second-pi "Review the current interpretation and method decision from raw evidence"
```

The skills inspect the current project and arguments you provide. Give durable
paths to raw results, configs, logs, code, and drafts whenever possible.

## Explicit-only skills

The following skills can cause material side effects or perform
submission-oriented work, so Claude will not auto-invoke them:

```text
/firm:run-experiment
/firm:monitor-experiment
/firm:audit-experiment
/firm:write-paper
/firm:improve-paper
/firm:audit-citations
/firm:make-figures
```

Invoke them deliberately with the relevant path or command.

## Project-local installation

Use this only when a repository should carry its own copy of FIRM:

```bash
git clone https://github.com/Zarien-Li/FIRM.git ~/FIRM
~/FIRM/firm init /absolute/path/to/project
~/FIRM/firm doctor /absolute/path/to/project
```

This creates:

```text
project/
├── CLAUDE.md                 # existing content preserved; one marked FIRM block appended
├── .claude/skills/           # the 17 project-local skills
└── .firm/
    ├── RESEARCH_PROGRAM.md
    ├── FIRST_MESSAGE_NEW.md
    └── FIRST_MESSAGE_AUDIT.md
```

Start Claude Code normally:

```bash
cd /absolute/path/to/project
claude
```

Project-local commands are not plugin-namespaced, so use `/research`,
`/diagnose-result`, and so on.

## Start a new program

Fill in `.firm/RESEARCH_PROGRAM.md` at the level of the important field and value
surface. Do not preselect the final failure or method. Then use
`.firm/FIRST_MESSAGE_NEW.md` as the first request or run:

```text
/research "Start from .firm/RESEARCH_PROGRAM.md and establish the best empirical contact point"
```

## Audit an existing project

Attach FIRM, then run:

```text
/research "Audit this existing project before more experiments: recover the original program, strongest evidence and contrary evidence, method lineage, scope debt, paper maturity, active jobs, and one recommended next action"
```

Do not treat file count, experiment count, or draft polish as evidence of paper
maturity.

## Update or remove

Plugin installs are managed by Claude Code's plugin interface. For a project-local
copy, rerun `firm init`; unchanged skills are left untouched and changed FIRM
skills are backed up before replacement.
