# FIRM Skills Index

FIRM is a Claude Code plugin with 17 research skills. Plugin commands use the
`/firm:` namespace. A project-local installation uses the same names without the
namespace, for example `/diagnose-result`.

## Start here

| Skill | Use it for | Invocation |
|---|---|---|
| `research` | Own a program through contact, construction, expansion, and paper harvest | `/firm:research [goal or project state]` |
| `diagnose-result` | Interpret a coherent evidence bundle or completed construction arc | `/firm:diagnose-result [result bundle]` |
| `design-method` | Cultivate or repair one load-bearing primitive across versions | `/firm:design-method [evidence or failed component]` |
| `plan-experiments` | Plan an evidence-bearing episode or paper campaign | `/firm:plan-experiments [method, claim, budget]` |
| `second-pi` | Use a critical or creative independent co-PI at one consequential episode boundary | `/firm:second-pi [role and evidence packet]` |
| `write-paper` | Plan, draft, compile, or verify a paper from validated evidence | `/firm:write-paper [paper directory or section]` |

## Discover and anchor

| Skill | Responsibility | Activation |
|---|---|---|
| `discover-direction` | Find a consequential and feasible research program from the field surface | May activate when relevant |
| `literature-review` | Search and synthesize papers, implementations, benchmarks, and close work for a live decision | May activate when relevant |
| `baseline` | Select, reproduce, and behaviorally inspect strong field-standard anchors | May activate when relevant |
| `research` | Preserve the Program Compass, current episode, positive object, paper spine, and next scientific action | May activate when relevant |

## Diagnose and design

| Skill | Responsibility | Activation |
|---|---|---|
| `diagnose-result` | Separate observation from inference and read evidence at bundle or episode scale | May activate when relevant |
| `design-method` | Cultivate a load-bearing architecture, objective, state, memory, routing, training, data, or systems primitive | May activate when relevant |
| `plan-experiments` | Build a coherent construction episode or positive-expansion campaign | May activate when relevant |
| `second-pi` | Use Codex for maturity-matched critical review or Gemini for evidence-grounded creative invention/expansion | May activate when relevant; runs in a fork |

## Run and verify

| Skill | Responsibility | Activation |
|---|---|---|
| `register-experiment` | Freeze the purpose, exact configuration, forecast, and interpretation of a costly or decisive run | May activate when relevant |
| `run-experiment` | Launch local, SSH, Slurm, queued, retry, or resume workflows with durable provenance | **Explicit invocation only** |
| `monitor-experiment` | Inspect owned jobs, logs, metrics, and outputs without silently changing them | **Explicit invocation only** |
| `audit-experiment` | Independently audit artifacts, evaluator semantics, provenance, fairness, and claim scope | **Explicit invocation only; fresh fork** |
| `audit-research` | Audit continuity, value, scope debt, contribution identity, and paper readiness at a real boundary while consuming rather than repeating factual audits | Fresh fork |

## Write and finish

| Skill | Responsibility | Activation |
|---|---|---|
| `write-paper` | Plan, draft, compile, and verify a manuscript against raw evidence | **Explicit invocation only** |
| `improve-paper` | Run bounded fresh-review and revision rounds without inventing missing science | **Explicit invocation only** |
| `audit-citations` | Verify source existence, metadata, and support for each consequential citation context | **Explicit invocation only; fresh fork** |
| `make-figures` | Produce reproducible publication figures and LaTeX tables | **Explicit invocation only** |

## Recommended combinations

- **A method lost:** `diagnose-result` → `design-method` → `plan-experiments`
- **The project is drifting:** `research` → `audit-research`; add one maturity-matched `second-pi` role only when independent judgment can change the decision
- **A costly run is approaching:** `plan-experiments` → `register-experiment` → `run-experiment`
- **A draft may be premature:** `audit-research` → `second-pi` paper-entry → `write-paper`
- **Submission cleanup:** run only affected claim/citation checks + `make-figures` + `improve-paper`

Specialists are tools, not required stages. Invoke the smallest skill that resolves
the current uncertainty.
