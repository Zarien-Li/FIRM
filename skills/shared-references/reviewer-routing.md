# Reviewer Routing Protocol

## Core Principle

**Use the reviewer whose independence and failure mode best match the question being asked.**

This protocol decides when to use fresh reviewers, reply-thread reviewers, local checks, and fallback reviewers when a preferred tool is unavailable.

## Reviewer Modes

| Mode | Use When | Independence |
|---|---|---|
| `fresh` | You need an independent judgment of the current artifact. | High |
| `reply` | You need the same reviewer to check whether its own prior feedback was resolved. | Medium |
| `local` | You need a mechanical checklist or no external reviewer is available. | Low |
| `cross_compare` | You need to compare independent reviewers and identify disagreement. | Highest |

## Default Rule

Use `fresh` for any review that can affect external readiness.

Use `reply` only for iterative resolution of a prior reviewer's own comments.

Use `local` only for non-blocking checks or when tools are unavailable.

## Review Type Routing

| Review Type | Default Mode | Required Independence | Notes |
|---|---|---|---|
| Acceptance / publishability | `fresh` | High | Reviewer reads primary artifacts directly. |
| Claim audit | `fresh` | High | Must not receive executor's interpretation of results. |
| Citation audit | `fresh` | High | Reviewer checks sentence-to-source support. |
| Headline and scope adversarial review | `fresh` | High | Must be adversarial and uncoached; judges the submitted claim, not the research program. |
| Experiment integrity | `fresh` | High | Executor must not judge its own experiments. |
| Rebuttal stress test | `fresh` | High | Reviewer acts as skeptical area chair or reviewer. |
| Revision check | `reply` | Medium | Same reviewer can verify its own issues. |
| Slide polish | `fresh` or `local` | Medium | Fresh if stakes are high. |
| Poster polish | `fresh` or `local` | Medium | Fresh if for conference presentation. |
| Mechanical formatting | `local` | Low | Compilation, page limit, missing assets. |

## Reviewer Roles

Use precise roles rather than generic "review this":

- `senior_ml_reviewer`
- `theory_reviewer`
- `experiment_reviewer`
- `systems_reviewer`
- `citation_auditor`
- `adversarial_reviewer`
- `area_chair`
- `clarity_editor`
- `venue_fit_reviewer`
- `rebuttal_stress_tester`

## Fresh Review Prompt Shape

Fresh review prompts may include:

- Reviewer role
- Review objective
- Venue constraints
- File paths
- Required output format

Fresh review prompts must not include:

- Executor summaries
- Executor opinions
- Previous reviewer findings
- Claimed strengths
- Suggested answers

See `reviewer-independence.md`.

## Reply Review Prompt Shape

Reply review prompts may include:

- The reviewer's own prior finding IDs
- Changed file paths
- A request to verify whether each issue is resolved

Reply review prompts must not include:

- Executor arguments trying to persuade the reviewer
- New claims that are not in the artifact
- Selective excerpts that hide surrounding context

## Cross-Compare

Use `cross_compare` when:

- A paper is near submission
- Two reviewers disagree on soundness or novelty
- A central claim is controversial
- A rejection risk remains unclear

Cross-compare output must list:

- Agreements
- Disagreements
- Highest-risk unresolved issue
- Which artifact change would reduce risk most

## Tool Fallbacks

When a preferred reviewer tool is unavailable:

1. Preserve the review mode if possible.
2. Preserve independence before preserving convenience.
3. If no external reviewer exists, run a local checklist and mark mode as `local`.
4. Do not label local review as independent.

Fallback table:

| Preferred Tool | Fallback |
|---|---|
| External Codex reviewer | Fresh local session or available multi-agent reviewer |
| Gemini reviewer | Another independent model/tool |
| Zotero-backed citation check | Local bibliography and PDF check |
| Obsidian-backed context check | Filesystem notes check |
| No reviewer tool | Local checklist with `local` mode |

## Routing Output

Before launching a major review, record:

```markdown
Review route:
- Review type:
- Reviewer role:
- Mode: fresh | reply | local | cross_compare
- Tool/model:
- Independence required: high | medium | low
- Trace file:
```

## Final Rule

Do not downgrade a required independent review to a local check without marking the final decision as lower confidence.
