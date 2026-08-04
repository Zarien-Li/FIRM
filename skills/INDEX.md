# FIRM Skills Index

FIRM is a Claude Code plugin with 17 research skills. Plugin commands use the
`/firm:` namespace. A project-local installation uses the same names without the
namespace, for example `/diagnose-result`.

## Start here

| Skill | Use it for | Invocation |
|---|---|---|
| `research` | Start or resume a project with one persistent first-author perspective | `/firm:research [goal or project state]` |
| `diagnose-result` | Interpret a completed, negative, mixed, or surprising result | `/firm:diagnose-result [result path]` |
| `design-method` | Invent or repair the load-bearing method primitive | `/firm:design-method [evidence or failed component]` |
| `plan-experiments` | Select decisive comparisons and adaptive next steps | `/firm:plan-experiments [method, claim, budget]` |
| `second-pi` | Obtain a fresh independent critique of a consequential decision | `/firm:second-pi [decision or evidence packet]` |
| `write-paper` | Plan, draft, compile, or verify a paper from validated evidence | `/firm:write-paper [paper directory or section]` |

## Discover and anchor

| Skill | Responsibility | Activation |
|---|---|---|
| `discover-direction` | Find a consequential and feasible research program from the field surface | May activate when relevant |
| `literature-review` | Search and synthesize papers, implementations, benchmarks, and close work for a live decision | May activate when relevant |
| `baseline` | Select, reproduce, and behaviorally inspect strong field-standard anchors | May activate when relevant |
| `research` | Preserve the original program, current paper, evidence, method lineage, scope debt, and next action | May activate when relevant |

## Diagnose and design

| Skill | Responsibility | Activation |
|---|---|---|
| `diagnose-result` | Calibrate what a completed result establishes and choose the smallest discriminating next test | May activate when relevant |
| `design-method` | Convert a causal thesis into a load-bearing architecture, objective, state, memory, routing, training, data, or systems primitive | May activate when relevant |
| `plan-experiments` | Build a claim-aware, compute-efficient experiment plan | May activate when relevant |
| `second-pi` | Review prize, fidelity, interpretation, alternatives, attacks, maturity, and decision in a fresh context | May activate when relevant; runs in a fork |

## Run and verify

| Skill | Responsibility | Activation |
|---|---|---|
| `register-experiment` | Freeze the purpose, exact configuration, forecast, and interpretation of a costly or decisive run | May activate when relevant |
| `run-experiment` | Launch local, SSH, Slurm, queued, retry, or resume workflows with durable provenance | **Explicit invocation only** |
| `monitor-experiment` | Inspect owned jobs, logs, metrics, and outputs without silently changing them | **Explicit invocation only** |
| `audit-experiment` | Independently audit artifacts, evaluator semantics, provenance, fairness, and claim scope | **Explicit invocation only; fresh fork** |
| `audit-research` | Audit continuity, scope drift, contribution maturity, and paper readiness at a real boundary | Fresh fork |

## Write and finish

| Skill | Responsibility | Activation |
|---|---|---|
| `write-paper` | Plan, draft, compile, and verify a manuscript against raw evidence | **Explicit invocation only** |
| `improve-paper` | Run bounded fresh-review and revision rounds without inventing missing science | **Explicit invocation only** |
| `audit-citations` | Verify source existence, metadata, and support for each consequential citation context | **Explicit invocation only; fresh fork** |
| `make-figures` | Produce reproducible publication figures and LaTeX tables | **Explicit invocation only** |

## Recommended combinations

- **A method lost:** `diagnose-result` → `design-method` → `plan-experiments`
- **The project is drifting:** `research` → `second-pi` → `audit-research`
- **A costly run is approaching:** `plan-experiments` → `register-experiment` → `run-experiment`
- **A draft may be premature:** `audit-experiment` → `second-pi` → `write-paper`
- **Submission cleanup:** `audit-citations` + `make-figures` + `improve-paper`

Specialists are tools, not required stages. Invoke the smallest skill that resolves
the current uncertainty.
