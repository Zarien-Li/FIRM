# Output Manifest Protocol

Use a manifest only when several actors, artifacts, or downstream steps would
otherwise lose provenance. It is a coordination aid, not a requirement for every
non-trivial action and never a permission gate.

## When It Helps

Create or update a manifest for:

- a multi-run experiment campaign or external job queue;
- a paper, submission, rebuttal, or audit with several generated artifacts;
- a handoff where inputs, outputs, decisions, and unresolved issues are not already
  clear in one authoritative tracker or state file.

Do not create a separate manifest when the authoritative state, experiment tracker,
review trace, or paper report already records the same information. Small checks,
ordinary interpretation, and single-file edits normally need none.

## Compact Form

```markdown
# Output Manifest
skill/action:
date:
status: complete | partial | blocked

## Inputs
| Path | Role |

## Outputs
| Path | Type | Verification |

## Decisions
| Decision | Evidence |

## Open Issues
| Issue | Class | Owner/next action |

## Handoff
- next action:
- files to read:
- files to ignore:
```

Use exact paths, result IDs, review finding IDs, or artifact sections as evidence.
Avoid vague entries such as `looks good` or `reviewed manually`.

Finding classes should reuse the active vocabulary when applicable:
`EVIDENCE_INVALIDATING`, `METHOD_DESIGN_CHANGING`, `CLAIM_NARROWING`, or
`DEFERRABLE`.

Update status and append consequential decisions; do not erase provenance. Keep the
handoff small and point to raw logs rather than copying them.

A missing manifest cannot block scientifically justified work. If another actor can
reliably determine what happened from the existing authoritative artifacts, no new
manifest is needed.
