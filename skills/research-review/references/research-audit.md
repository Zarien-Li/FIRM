---
name: research-audit
description: "Route one independent factual audit: mode experiment verifies artifacts, evaluator, provenance, fairness, and evidence lineage; mode citation verifies bibliographic identity and local contextual support. Use only at consequential boundaries or concrete integrity risk. Scientific prize, contribution identity, headline quality, and research-state maturity belong to the independent and state-audit routes of research-review."
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, WebSearch, WebFetch, mcp__codex__codex, mcp__codex__codex-reply
---

# Research Audit

Select exactly one factual audit and load only its reference:

- `mode: experiment` -> `references/audit/experiment-mode.md`;
- `mode: citation` -> `references/audit/citation-mode.md`.

There is no headline mode. Use `/research-review` artifact review for scientific
importance, paper identity, title/scope, strongest objections, and proof review. Use
`/research-review mode: state-audit` for value continuity, scope debt, paper entry, major compute,
resume, and portfolio decisions. Use `paper-writing mode: claim-audit` for manuscript
numbers and semantic qualifiers against raw results.

## Shared Invariants

- Audit raw artifacts and primary sources before summaries.
- Use fresh reviewer context; do not reveal desired verdict, prior scores, or fix plan.
- Missing evidence is `UNVERIFIED` or `BLOCKED`, not guessed.
- A finding applies to the affected artifact and claim, not automatically the method,
  paper, field, or program.
- Preserve original artifacts. Repairs are separate actions with explicit lineage.
- Reuse a green audit while declared input hashes and semantics remain unchanged.
- Audits qualify, remove, or repair evidence; they do not invent methods, launch
  defensive experiment grids, change contribution type, or impose stop/freeze/retire.

For submission assurance, emit the human report and machine-readable JSON described in
the selected reference and `../../research-pipeline/references/shared/assurance-contract.md`. Record reviewer
identity/thread, UTC time, verdict, reason code, declared input hashes, and trace path.

## Output Routing

- experiment findings update evidence lineage and are consumed by `method-development`,
  the state-audit route in `research-review`, or `paper-writing` as needed;
- citation findings update citation contexts or metadata only after verification;
- scientific interpretation returns to the lead PI and is never delegated to this
  router.
