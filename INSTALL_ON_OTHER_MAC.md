# Install On Another Mac

This archive contains the current research and paper-writing skills, shared
research references, and the canonical `CLAUDE-RESEARCH.md` prompt. It does not
contain Claude Code sessions, API keys, credentials, or machine-specific server
configuration.

## Install

1. Extract the archive.
2. Open Terminal in the extracted directory.
3. Run:

```bash
bash install.sh
```

The installer backs up every same-named destination skill before replacing it.
Unrelated skills in `~/.claude/skills` are left untouched.

For each research project, copy `CLAUDE-RESEARCH.md` into the project root and
start Claude Code with:

```bash
claude --append-system-prompt-file CLAUDE-RESEARCH.md
```

Use `--continue` only when that computer already has the corresponding Claude
Code conversation. Skills do not require copying credentials or session files.

## Verify

```bash
find ~/.claude/skills -maxdepth 2 -name SKILL.md | sort
```

The package installs only the research-related skills included under `skills/`
and the shared references under `shared-references/`.
