# Demo Recording Checklist

## Before recording

- Test the exact public marketplace install in a clean Claude Code session.
- Run `make check` from a clean clone.
- Use `demo/fixture/PROMPT.md` without adding the desired conclusion.
- Capture a real `/firm:signal-analysis RESULT.md` response.
- Preserve the raw response in the release notes or demo branch when practical.

## Capture

- Use 16:9 at 1080p or higher and a readable terminal font.
- Hide notifications and remove usernames, machine paths, API keys, private paper
  titles, server addresses, and reviewer identities.
- Distinguish generated output from explanatory captions.
- Do not present `make demo` as a live model evaluation.

## Final checks

- Every command shown exists in the released repository.
- The install command matches README exactly.
- The model response is not edited into a stronger conclusion than it produced.
- Historical usage is not described as a controlled benchmark.
- Upstream inspiration is credited without implying endorsement.
