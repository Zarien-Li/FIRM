# Claim-Bearing Evidence Lineage

## Scope

Use lineage tracking only when a result is about to support a consequential claim or
paper. Exploratory runs need honest paths and labels, not a registry entry for every
probe. This protocol prevents invalid evidence from surviving in downstream state,
figures, drafts, and handoffs.

## Minimal Registry

Maintain one project-level `EVIDENCE_REGISTRY.json` when a bounded paper candidate
exists. Each claim-bearing item has a stable ID:

```json
{
  "schema_version": 1,
  "evidence": {
    "result.main.v1": {
      "status": "provisional",
      "depends_on": ["anchor.eval.v1", "run.seed0.v1"],
      "artifacts": ["results/main.json", "paper/tables/main.tex"],
      "supports": ["C1", "Table1"],
      "reason": null,
      "superseded_by": null
    }
  }
}
```

Allowed status values are `provisional`, `valid`, `invalidated`, and `superseded`.
Dependencies may represent datasets, splits, evaluators, caches, checkpoints,
selection rules, runs, analyses, or derived assets.

## Invalidation Rule

When one item becomes invalid:

1. record the exact reason and source evidence;
2. compute the transitive set of dependent items;
3. mark every dependent item `invalidated` unless it has an independent valid path;
4. remove affected claims from the live claim set;
5. remove or qualify dependent manuscript claims and update the authoritative state;
6. scan tables, figures, drafts, handoffs, and summaries for stale references;
7. preserve historical files, but label them invalidated rather than deleting them;
8. restore a claim only through a new clean evidence item and explicit supersession.

`WARN` does not trigger transitive invalidation. It propagates the exact qualifier to
dependent claims. `FAIL` can never be represented only by a limitation sentence or
footnote.

## Authority

Raw artifacts and reproducible validity findings determine evidence status. A draft,
review, memory, status summary, or handoff cannot promote an invalidated item. Later
timestamps do not override stronger evidence. A reviewer identifies risks; the lead
researcher verifies the material finding and applies the lineage update.

## Verification

Use `research-audit/scripts/evidence_lineage.py` to validate the registry, compute an
invalidation impact set, and scan selected text assets for references to invalidated
evidence IDs or artifact paths. The script reports impact; it does not rewrite paper
prose automatically.
