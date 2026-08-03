# Start With FIRM

This guide takes a new user from an empty directory to the first evidence-bearing
research decision. FIRM is tested primarily with Claude Code. Codex CLI is
recommended as the independent second PI.

## Prerequisites

Required:

```bash
git --version
claude --version
```

Recommended for independent review:

```bash
codex --version
```

If Codex CLI is installed but not connected to Claude Code:

```bash
claude mcp add codex -s user -- codex mcp-server
claude mcp list
```

Restart an already-running Claude Code session after changing MCP configuration.
FIRM continues useful lead-researcher work when Codex is unavailable; it records
the independent review as deferred instead of turning tool failure into a
scientific verdict.

## Install Once

```bash
git clone https://github.com/Zoiya-Li/FIRM.git ~/FIRM
chmod +x ~/FIRM/firm
```

## Path A: Start A New Research Program

Initialize a project:

```bash
~/FIRM/firm init ~/research/my-project
```

FIRM creates:

```text
my-project/
├── CLAUDE.md
├── CLAUDE-RESEARCH.md       # public research system-prompt addendum
├── .claude/skills/           # project-local FIRM skills
└── .firm/
    ├── RESEARCH_PROGRAM.md
    ├── FIRST_MESSAGE_NEW.md
    └── FIRST_MESSAGE_AUDIT.md
```

Open `.firm/RESEARCH_PROGRAM.md` and fill in the field, accepted empirical
surface, community value, resource boundary, and non-binding research lens.
Do not preselect the final failure or method.

Then start Claude Code:

```bash
cd ~/research/my-project
claude --append-system-prompt-file CLAUDE-RESEARCH.md
```

Paste the contents of `.firm/FIRST_MESSAGE_NEW.md`.

## Path B: Audit An Existing Project

Attach FIRM without deleting existing project instructions:

```bash
~/FIRM/firm init ~/research/existing-project
```

If `CLAUDE.md` already exists, FIRM preserves a backup at
`.firm/CLAUDE.md.before-firm` and appends a marked FIRM block. Complete
`.firm/RESEARCH_PROGRAM.md` from the project's original objective, not from its
latest method or draft.

Start Claude Code in the project and paste
`.firm/FIRST_MESSAGE_AUDIT.md`. The first task is an evidence reconstruction,
not another experiment.

## Verify The Installation

```bash
~/FIRM/firm doctor ~/research/my-project
```

A healthy installation reports the skill count, shared-reference count, Claude
Code availability, and optional Codex CLI availability.

## What The First Useful Run Should Produce

The filenames may follow an existing project convention, but the substance
should include:

1. One compact authoritative research state, commonly `PIPELINE_STATE.md`.
2. The original broad program and the current paper fingerprint as separate
   objects.
3. Strongest evidence and strongest contrary evidence with durable paths.
4. A constructive method lineage: causal bet, competent realization, failure,
   surviving component, and next construction.
5. Scope debt and a path back to a standard task or natural value surface.
6. One chosen next action, why it dominates, and what evidence would change it.
7. A Codex Prize/Fidelity synthesis when an independent decision is warranted.

Do not expect a paper on the first run. Before full manuscript production, FIRM
expects `CANDIDATE_CLAIM.md` while the contribution is changing and an
independently reviewed `PAPER_ENTRY.md` with `entry: PASS` when it is mature.

## Common First-Run Mistakes

| Mistake | Correct use |
|---|---|
| Start with “find me a novel idea” | Define a valuable field and empirical surface first |
| Paste a preferred mechanism into the seed | Keep it as a non-binding lens |
| Ask for ten seeds after method v1 loses | Diagnose design uncertainty before statistical uncertainty |
| Ask Codex only after the draft is complete | Use it before expensive compute and paper-identity commitments |
| Treat generated files as progress | Judge method construction, evidence, and paper entry |

## Useful Commands

```bash
~/FIRM/firm prompt new
~/FIRM/firm prompt audit
~/FIRM/firm doctor .
bash ~/FIRM/install.sh --dry-run
```

For the product rationale and exact skill catalog, return to
[README](../README.md) and [skills index](../skills/INDEX.md).
