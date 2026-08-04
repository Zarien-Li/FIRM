# Release Checklist

## Validate

```bash
make check
claude plugin validate .
```

`make check` validates the repository without external dependencies. The official
Claude Code validator should also pass in a current Claude Code installation before
tagging a release.

The release is blocked by invalid frontmatter, broken local references, a skill
above the line budget, unsafe command patterns, inconsistent plugin metadata, or
non-idempotent onboarding.

## Test the real install path

In a clean Claude Code session:

```text
/plugin marketplace add Zarien-Li/FIRM
/plugin install firm@firm-research
/reload-plugins
```

Verify at least:

```text
/firm:research
/firm:diagnose-result demo/fixture/RESULT.md
/firm:second-pi
```

Also test project-local onboarding:

```bash
./firm init /tmp/firm-release-test
./firm doctor /tmp/firm-release-test
```

## Review documentation truthfulness

- Every displayed command must exist.
- The demo must distinguish a guided storyboard from a real model response.
- Neutral evaluation prompts must not contain the expected conclusion.
- No unpublished titles, reviewer identities, server paths, credentials, or
  private URLs may ship.
- Historical usage claims must not be presented as controlled causal evidence.
- Upstream attribution in `NOTICE` and `LICENSE` must remain intact.

## Version and publish

Update the release version in `.claude-plugin/plugin.json` and the top-level
marketplace manifest version. Do not duplicate the plugin version inside the marketplace
entry. Then update `CHANGELOG.md`, create the Git tag, and publish the GitHub release.
After publication, repeat the marketplace install from the public repository.
Upload `assets/social-preview.png` as the repository social preview in GitHub's
repository settings so shared links use the intended launch card.
