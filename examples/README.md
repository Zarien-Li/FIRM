# Three Field-Tested Failure Patterns

These are sanitized composite cases distilled from recurring behavior across
live research programs. They are not benchmark scores or claims that one
prompt deterministically produces the shown decision.

Each case contains:

- the research situation;
- the failure mode of an unassisted long-horizon agent;
- the FIRM intervention;
- a copy-paste starting prompt;
- the artifacts and decision that should emerge.

| Case | Failure pattern | Skills in the foreground |
|---|---|---|
| [1. A method loses once](01-method-loss-is-not-field-loss.md) | Premature closure versus wasteful seed expansion | `research-pipeline`, `method-primitive-synthesis`, `experiment-plan` |
| [2. The paper drifts from the seed](02-seed-drift.md) | A clean private cell replaces an important program | `research-pipeline`, `research-review`, `research-state-audit` |
| [3. A draft starts before the method is ready](03-paper-entry-audit.md) | Experimental volume is mistaken for paper maturity | `experiment-audit`, `research-review`, `paper-writing` |

For the 90-second release demo, use Case 1 with the fixture in
[`../demo/fixture`](../demo/fixture).
