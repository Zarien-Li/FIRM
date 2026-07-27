# Seven-Day Release Checklist

## D-7: Lock The Public Identity

- **Owner:** choose the final GitHub owner/repository name and restore GitHub
  authentication.
- **Codex:** replace every repository placeholder, initialize the repository,
  and prepare the first clean commit.
- **Exit condition:** the public repository URL is fixed and the release check
  has no placeholders.

## D-6: Prove Installation

- **Codex:** push the repository, clone it into a clean temporary environment,
  test fresh installation, conflict backup, dry-run, and verification.
- **Owner:** confirm the README's first-run wording matches the intended user.
- **Exit condition:** a new user can install the suite from the public URL with
  one shell command and receives `Verification passed`.

## D-5: Freeze The Three Cases

- **Codex:** check every case against the current skills and remove claims that
  are not demonstrated by the artifacts.
- **Owner:** approve whether the cases may be described as sanitized composites
  of the private research history.
- **Exit condition:** all three cases are public, reproducible decision
  patterns rather than anonymous testimonials.

## D-4: Capture The Real Demo

- **Owner:** record the real Claude Code interaction and voice-over. Do not use
  a fabricated agent response.
- **Codex:** provide the exact prompt, terminal storyboard, shot order,
  captions, and timing; inspect the raw recording for scientific and privacy
  issues.
- **Exit condition:** one truthful 85-90 second recording exists.

## D-3: Edit And Embed

- **Codex:** trim the recording, prepare captions and a compact GIF/WebM
  preview, add the media to README, and verify links.
- **Owner:** approve public-facing voice, identity, and any visible account
  information.
- **Exit condition:** the value can be understood without reading the entire
  README.

## D-2: Evidence And Integrity Audit

- **Owner:** provide publishable support or revised wording for the three ARR
  reviewer-score claims.
- **Codex:** run the release checker, attribution/license audit, secret/path
  scan, and claim-language audit.
- **Exit condition:** no unresolved URL, private path, credential, unsupported
  evidence claim, or attribution issue remains.

## D-1: Public Dry Run

- **Codex:** verify an incognito clone, install, examples, demo, and rendered
  README; prepare the `v1.0.0` changelog.
- **Owner:** review the repository exactly as a first-time visitor would and
  approve launch.
- **Exit condition:** release candidate is frozen except for genuine blockers.

## D-0: Release

- **Codex:** tag `v1.0.0`, publish the GitHub release, and return the canonical
  links and tested install command.
- **Owner:** make the launch posts and respond personally to early community
  questions.

## Blocking: Owner Action

- [x] Lock the repository identity as `Zoiya-Li/ResearcherOS`.
- [x] Restore GitHub authentication for `Zoiya-Li`.
- [ ] Approve creation of the public repository and its license visibility.
- [ ] Provide publishable evidence or preferred wording for the three ARR
  reviewer-score claims.
- [ ] Record the real Claude Code response and voice-over for the 90-second
  demo. The script and fixture are ready; a real response should not be faked.

## Prepared By Codex

- [x] Reversible one-command installer with conflict backups.
- [x] Installation verifier.
- [x] Three sanitized field-tested cases.
- [x] 90-second timeline, narration, fixture, terminal preview, and recording
  checklist.
- [x] Automated release check for missing files, placeholders, and private
  paths.

## After Repository Creation

- [x] Replace repository placeholders with the canonical URL.
- [ ] Initialize Git, commit, push, and verify the public repository in an
  incognito browser.
- [ ] Test `git clone` plus `bash install.sh` in a clean temporary home.
- [ ] Add the final MP4/GIF/WebM demo asset and link it from README.
- [ ] Create release `v1.0.0` with a concise changelog.
