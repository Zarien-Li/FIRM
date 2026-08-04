# Agent and Maintainer Guide

FIRM is a Claude Code skills repository, not a standalone research platform. The
product is the quality and composability of the 17 `SKILL.md` workflows.

## Product identity

FIRM helps a capable coding agent make better scientific decisions after reading
literature, inspecting evidence, running an experiment, or approaching a paper
boundary. It should complement existing tools rather than recreate them.

## Repository layout

```text
.claude-plugin/     plugin and marketplace manifests
skills/             one directory per callable skill
examples/           sanitized recurring failure patterns
demo/fixture/       neutral result-diagnosis case
templates/          optional project-local bootstrap files
scripts/            validation and onboarding tests
```

Each public skill directory must contain `SKILL.md`. Detailed material should live
inside that skill's `references/` or `scripts/` directory so the main instruction
remains concise.

## Skill design rules

1. Give each skill one clear job and explicit non-goals.
2. Write the description so Claude can distinguish it from neighboring skills.
3. Keep the main `SKILL.md` below 500 lines.
4. Use project-relative evidence paths and prefer raw artifacts over summaries.
5. Set `disable-model-invocation: true` for workflows with compute, remote,
   destructive, manuscript-wide, or submission-oriented side effects.
6. Use `context: fork` for genuinely independent review.
7. Never require a specific external model or MCP server for core behavior.
8. Never include automatic `git push`, plaintext credentials, or unconfirmed
   destructive commands.

## Validation

Run:

```bash
make check
```

This validates frontmatter, skill count, line budgets, relative references,
plugin JSON, installer behavior, and unsafe command patterns.

## Evaluate a change

Test a skill against at least:

- a case where it should activate;
- a neighboring case where another skill should activate;
- a case where doing nothing or asking for missing evidence is correct;
- the failure pattern the change is intended to repair;
- the opposite failure the new instruction might create.

For judgment changes, compare fresh sessions on the same neutral evidence packet.
Do not leak the desired conclusion into the user prompt.
