# Security Policy

Claude Code skills can read files, run commands, contact remote systems, consume
compute, and modify manuscripts. Review this repository before granting tool
permissions, especially in repositories containing secrets or unpublished work.

FIRM marks side-effectful workflows as explicit-only. Even then, users should
review commands involving:

- remote hosts or schedulers;
- paid APIs or large compute allocations;
- deletion, overwrite, or repository history changes;
- credentials and environment variables;
- publication, submission, or external communication.

FIRM skills must never embed plaintext secrets, automatically push to a remote
repository, or treat tool access as authorization for an irreversible action.

Report a vulnerability privately through GitHub's security advisory mechanism for
this repository. Include the affected skill, the unsafe path, impact, and a minimal
reproduction. Do not include real credentials or private research data.
