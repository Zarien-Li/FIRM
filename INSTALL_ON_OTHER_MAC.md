# Install On Another Mac

This package contains the canonical managed research skills, shared references, and
runtime research addendum. It excludes sessions, credentials, model/data caches,
server configuration, and project artifacts.

## Install

Extract the package and run:

```bash
bash install.sh
```

For a persistent GPT PI in Trae instead, run:

```bash
FIRM_HOST=trae bash install.sh
```

The installer:

- installs exactly the skill names in `managed-skills.txt`;
- replaces the managed shared-reference tree atomically;
- archives changed, retired, and known legacy research runtime files on the Desktop;
- removes only previously managed or explicitly listed retired skills;
- leaves unrelated user skills untouched;
- installs the six skills and the host-appropriate prompt under `~/.claude` or
  `~/.trae`.

For a research project, copy `CLAUDE-RESEARCH.md` into the project root and launch the
model with that file as its appended system prompt. Continue an existing conversation
only when its project state and raw artifacts are present on that computer.

## Verify

```bash
python3 skills/research-pipeline/tests/check_semantic_contract.py
python3 -m unittest skills/research-review/tests/test_evidence_lineage.py -v
while read -r name; do
  case "$name" in ""|\#*) continue ;; esac
  diff -qr "skills/$name" "$HOME/.claude/skills/$name" || exit 1
done < managed-skills.txt
```

Run tests with `PYTHONDONTWRITEBYTECODE=1` when checking an immutable archive.
