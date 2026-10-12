# Research Responsibility Update

This maintainer note maps the thirteen issues in the user's September session review
to their maintained owners. It is not runtime context, a checklist for every run, or an
independent confirmation of the report's project-level allegations and frequencies.
The review used excerpted session material; a missing action in that material is not
proof that it never occurred.

The change preserves six skills and their specialist references. Scientific decisions
remain with the PI. No new periodic reviewer, fixed GPU-hour cutoff, variant limit,
automatic research state machine, or mandatory full-table gate was introduced.

| Report issue | Changed responsibility and observable outcome | Canonical owner |
|---|---|---|
| P1 Progress silence or chatter | The PI reports meaningful scientific movement; the execution owner verifies observation and receipt, repairs a failed observer, and states an unavailable wakeup honestly. | `research-pipeline/SKILL.md`; `experiment-operations/references/monitor-experiment.md` |
| P2 Results and manuscript diverge | Adopted or invalidated results reconcile the affected method, tables, figures, and narrative. Unresolved dependencies stay in the single state and are consumed when resolved. | `paper-writing/references/paper-writing.md` |
| P3 Variant inflation | Read a coherent comparison bundle, preserve a runnable reference, and explain the evidence motivating a repair or replacement. Joint interventions remain available when scientifically needed. | `method-development/references/method-primitive-synthesis.md` |
| P4 Weak substitutes or endless reproduction | Identify the decision served and actual implementation before investing. Label semantic deviations; revisit cost against decision value while retaining necessary rival obligations. | `research-foundation/references/baseline.md` |
| P5 Completion mistaken for validity | Verify engagement and evaluator behavior before scientific reliance. Trace anomalous observations; row counts and terminal markers alone cannot validate them. | `research-foundation/references/experiment-integrity.md`; `experiment-operations/references/run-experiment.md` |
| P6 Stale state and broken handoffs | Reconcile changed assertions against current artifacts, carry unread completed results and unresolved dependencies, and rediscover job identity after interruption. | `research-pipeline/SKILL.md`; `research-pipeline/references/collaboration.md` |
| P7 Resource economics | Measure end-to-end throughput, check actual concurrency and storage growth, reuse shared assets, and repair owned stale coordination without touching foreign processes. | `experiment-operations/references/run-experiment.md`; `experiment-operations/references/run-experiment/operations.md` |
| P8 User as institutional memory | Persist explicit durable protocols with scope and provenance in their existing project owner; replace superseded instructions and carry them into handoffs. | `research-pipeline/SKILL.md`; `scripts/lib/project-contract.mjs` |
| P9 Unowned paper agenda | The PI proposes contribution framing, title, abstract, evidence selection, and remaining submission work, while preserving final human authority. | `research-pipeline/SKILL.md`; `paper-writing/references/paper-writing.md` |
| P10 Recurring writing problems | Keep accepted editorial lessons and concrete examples in the existing author argument or plan; apply across rewrites and test with a fresh reader. | `paper-writing/references/paper-writing.md`; `paper-writing/references/auto-paper-improvement-loop.md` |
| P11 Passive research judgment | Interpret consequential results and stalled construction arcs without waiting for a user challenge. Independent review remains sparse; a verified finding includes repair and inspection. | `research-pipeline/SKILL.md`; `research-review/SKILL.md` |
| P12 Milestone treated as endpoint | Continue from an intermediate deliverable to its scientific consequence and next authorized action. Real waits, platform limits, user boundaries, and completion remain legitimate. | `research-pipeline/SKILL.md`; `research-pipeline/references/collaboration.md` |
| P13 Infrastructure death | Account for shared quotas, preserve live-job and recovery identity, reconcile on return, and verify that a notification mechanism actually reaches its recipient. | `experiment-operations/references/run-experiment.md`; `experiment-operations/references/monitor-experiment.md` |

## Runtime Limits

These edits specify responsibility; they do not install a scheduler, increase provider
quota, add a platform callback API, or wake a closed CLI by themselves. Before unattended
work relies on continuation, the execution owner must establish the available wait or
notification mechanism, demonstrate receipt, and retain recoverable job identity. If
the platform cannot supply it, expose that dependency instead of claiming automation.
No active project/session was restarted or messaged as part of this skill update.

## Integration

Claude and Trae install the same main-PI prompt and shared research responsibilities;
bounded child calls use the short task-role context rather than a second workflow.
The project generator records the durable-protocol and reconciliation obligations for
future projects without encoding worker IDs or a scientific strategy. Existing projects
inherit the installed skills when their session rereads them; changing files on disk
does not update an already-running model's context.

## Verification Scope

Validate skill structure and links, project generation, source/installed equality, and
scenario-level decisions. These checks can reveal instruction conflicts and packaging
regressions; they do not prove improved long-horizon research outcomes. Assess actual
behavior on subsequent results, interruptions, and manuscript revisions before claiming
that the recurring failures have been eliminated.

A separate read-only evaluator applied the revised instructions to seven hypothetical
cases: non-engaging baseline, stale manuscript after a tradeoff gain, absent callback
during quota interruption, costly necessary rival, interacting negative components,
stale completion with a broken lease, and recurring prose defects with a request to
remove a losing comparison. Its proposed actions preserved validity, useful iteration,
research ownership, resource boundaries, and disclosure. This is instruction-level
validation, not a rerun of those projects or evidence of future runtime reliability.
