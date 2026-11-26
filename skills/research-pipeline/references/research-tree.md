# Research Tree And Comparison Binding

The persistent PI owns `PROJECT_STATE.json`: one structured scientific memory with a
human-readable tree, not a log or a machine that chooses research. `PROJECT_STATE.md`
is its generated view, never a second editable interpretation. The comparison contract
records what a comparison means; run records establish what actually executed. Neither
replaces the tree or determines scientific validity by itself.

## Record Decisions At Their Actual Scale

Keep the user's problem at the root. Represent consequential questions, competing
explanations, governing principles, and implementations as connected nodes. `kind` is
descriptive language, not an enum or mandatory sequence; create a node when a separate
scientific decision needs to remain recoverable, not for every experiment. A parent
means intellectual lineage, not proof, dependency, or automatic evidence inheritance.
Use `depends_on` for other node IDs on which an interpretation actually relies.

Each node carries a statement and rationale, relevant comparison IDs, evidence links,
interpretation, unresolved questions, and next action. An evidence entry has `artifact`,
`observation`, and `bearing`: why it supports, challenges, or limits the node. Link the
run record for numerical evidence, not just a metric screenshot. Keep contradictory
and abandoned branches visible with their current interpretation. Do not rewrite an
old prediction as if it had anticipated the result. Preserve superseded reasoning in
versioned artifacts when a node's account materially changes.

`focus` names the current investment and its reason, not a permanent main method. Its
`return_question` states what unresolved issue in the parent would become relevant
again if this implementation does not answer it. Returning means reconsidering that
question with accumulated evidence, not clearing the project or restarting all work.
Keep important sibling explanations legible while developing one realization. A
negative child result does not refute its parent automatically; a successful child
does not validate the parent's preferred mechanism automatically.

At a consequential result or commitment, read the focus's ancestry, relevant siblings,
and contrary evidence. Judge whether implementation competence, the principle's
prediction, the comparison, or the larger opportunity changed. A near-frontier loss
can justify repair when the principle still explains a valuable difference. A score
increase cannot justify loyalty when extra machinery carries the gain or the key
counterexample remains unexplained. Choose from evidence and remaining opportunity,
not a failure quota, SOTA rank alone, sunk cost, or an automatic backtracking rule.

## Bind Evidence To Its Comparison

`COMPARISON_CONTRACT.json` has source-backed, stable comparison IDs. Each comparison
records its purpose/evidence role, task and target, dataset revision/splits/eligible
population, input information and retrieval/tool access, backbone regime, training
and inference conditions, evaluator/aggregation/failure handling, selection policy,
published competitors, permitted method freedoms, and unresolved provenance. Keep only
conditions that matter to this comparison; allow unknowns rather than inventing facts.
Competitor entries identify paper, implementation/revision, and native or adapted
semantics. A diagnostic comparison has its own identity; it does not overwrite the
formal obligation. A comparison may contain multiple meaningful table cells.

`user_locked_conditions` records actual user instructions and their source. A generated
plan or a collaborator's preference is not a user lock. The PI can revise its own plan.
When semantics change, explain the consequence, retain the old contract snapshot, and
identify the new comparison or revision. Changes to retrieval, training class, or
backbone are not automatically forbidden: interpret whether they are a permitted
treatment or a different evaluated object. Do not merge unmatched evidence into the
old table while that relationship is unresolved. Ordinary redesign and diagnostic work
continue autonomously; only genuine existing user boundaries require escalation.

Use `scripts/research_state.py seal <project>` to snapshot the contract by canonical
JSON SHA-256 under `.research/contracts/`. Every consequential numerical run binds its
node ID and comparison ID to that immutable contract snapshot. Preserve the run's
actual resolved configuration, including inherited defaults, with a content fingerprint.
Record deviations as field, expected, observed, and scientific consequence, with sources
where needed; an empty list means none identified, not proof that none exist.
Matching hashes prove identity, not fairness. Different hashes locate a revision,
not automatic invalidation. The PI decides which prior evidence remains comparable.

`bind-run` writes these references and PI-written deviations to an immutable
`<run-record>.comparison.json` receipt beside an existing JSON run record with its
stable `run_id`. It never read-modify-writes the experiment producer's mutable results.
The receipt binds that run identity; link both from evidence. It is a run artifact,
not another scientific state or registry. Concurrent binding cannot overwrite an
existing receipt. Contract and effective-config snapshots live under `.research/`.
The helper does not select settings,
launch experiments, score them, approve table entry, or alter campaign statuses.
Capture settings from the execution path rather than copying the intended contract.
Keep existing run records on their authorized artifact/data disk; supply explicit
absolute paths to the helper for external records/configs instead of copying the
experiment into the code directory. Snapshots contain small JSON records, not models,
predictions or datasets. Filesystem permissions and project resource authority still apply.
If the actual settings change after launch, retain the earlier binding and record the
actual attempt separately. Do not retroactively certify an unobserved configuration.

## Update The Scientific Account, Not The Activity Feed

After interpreting decisive evidence, update the affected nodes, claims, and focus
together. `last_change` names the evidence, what interpretation changed, movement
toward the original objective, claim movement, and next consequential action. No
movement is a legitimate answer: distinguish learning a useful fact from improving
the commissioned comparison. Each claim names supporting artifact paths and missing
decisive comparison IDs. Claims are current supported statements or clearly qualified
proposals, not titles promoted from a positive pilot. Keep manuscript dependencies
and execution references linked rather than duplicating their live status.

Reports to the user summarize that change in natural language. Do not print a JSON
form after every tool call or claim progress because a run completed. If evidence
invalidates a consequential claim, use the existing evidence-lineage protocol;
parentage alone does not determine the invalidation set.

## Initialize, Migrate, And Read

`scripts/research_state.py init <new-project>` copies the state and comparison templates
without overwriting existing files. Fill the actual objective from authority; unknown
science stays unknown. Use `check` for structural references and file fingerprints,
then `render` for a concise overview plus the decision tree. The helper never assesses
scientific maturity or chooses a branch. A successful check is not `REPORT OK`.

For an existing project, first read original authority and decisive artifacts. Migrate
only recoverable questions, alternatives, evidence, obligations, and live jobs from
the old prose. Mark uncertain history as uncertain; do not fabricate a tree of work
that was never evidenced. Preserve the prior state as referenced history, make the
JSON the sole editable scientific account, and replace the old live Markdown with its
generated view only after reconciliation. Do not mass-migrate active projects or
rewrite running experiments merely because the template changed. An unavailable
helper does not stop research: maintain the same JSON directly and render later.

Example binding (use the installed skill's absolute script path):

```bash
python3 <research-pipeline>/scripts/research_state.py init /path/to/project
python3 <research-pipeline>/scripts/research_state.py bind-run /path/to/project \
  --record runs/r01/run.json --node implementation-a1 --comparison main \
  --effective-config runs/r01/effective.json --deviations runs/r01/deviations.json
python3 <research-pipeline>/scripts/research_state.py check /path/to/project --record runs/r01/run.json
python3 <research-pipeline>/scripts/research_state.py render /path/to/project
```
