# Independent Experiment Audit

Use this mode at a consequential claim boundary or for a concrete doubt about evaluator
semantics, information flow, execution, treatment parity, statistical unit, selection,
or provenance. Scientific standards and repair consequences are defined once in
`research-foundation/references/experiment-integrity.md`; apply them here from an
independent evidence context rather than restating them as another checklist.

## Evidence And Reconstruction

Inspect the declared claim and primary artifacts needed to reproduce it: exact command
and resolved config, code revision, environment, model and checkpoint, data and split,
population, treatment, evaluator and parser, raw predictions or sufficient statistics,
logs, retries and exclusions, comparison budgets, registration, and manuscript objects
that depend on the result.

Verify artifact identity and intended code-path engagement, then reconstruct
representative values from raw outputs. Follow the information available at decision
time, the independent statistical unit, matched treatment, baseline competence,
selection provenance, and every transformation into the reported claim. Missing
evidence leaves the affected quantity unverified; interruption or audit-tool failure is
an execution fact, not evidence for or against the method.

Report exact artifact and code evidence for each material finding and the smallest
affected claim set. Preserve raw artifacts. Repair occurs separately, and verified
invalidation propagates through the shared evidence-lineage record. The audit does not
choose a method, contribution type, paper identity, or broader research verdict.

## Output

Write `EXPERIMENT_AUDIT.md` only when durable coordination is needed:

```markdown
# Experiment Audit
- audited claim and declared inputs:
- reviewer, thread, and time:

## Reconstruction
- code path, population, treatment, statistical unit, metric, and result:

## Findings
| Finding | Primary evidence | Affected claim/artifact | Required repair or qualifier |

## Evidence Lineage
- still usable:
- unverified or invalidated:
- superseding evidence, if any:
```

If an external submission format requires machine-readable assurance, also emit its
required JSON with declared input hashes and per-finding evidence. Do not edit results,
registrations, or manuscript claims from inside the audit.
