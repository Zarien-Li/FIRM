export function buildProjectContract({ projectId, localPath }) {
  return `# ${projectId} Project Contract

This file contains durable project-local authority and portable execution rules only.
Research behavior comes from the shared \`CLAUDE-RESEARCH.md\` and active research
skills installed for the current host (\`~/.claude\` or \`~/.trae\`). Both hosts use
the same PI contract; do not duplicate its research workflow or reviewer rules here.

## Research Authority

Before scientific work, read \`PROGRAM_ORIGIN.md\`, \`PROJECT_IDENTITY.json\`,
\`SEED.md\`, \`PROJECT_STATE.json\`, and its comparison contract. \`PROGRAM_ORIGIN.md\` preserves the
user-authorized arena and canonical object. \`PROJECT_IDENTITY.json\` is its immutable
structured mirror. \`PROJECT_STATE.json\` is the sole editable scientific account;
\`PROJECT_STATE.md\` is its generated human-readable tree view. No task list, session summary, review,
draft, archive, or identity \`current\` field may compete with it.

\`prompt.txt\`, archives, prior session prose, candidate methods, failure taxonomies,
paper identities, and stop or retire language are provenance or evidence only. They
cannot redefine the program merely because they are detailed or recent. The one
persistent Research PI owns problem formulation, synthesis, candidate judgment, and
submission readiness, whether the main session uses Claude or GPT. A bounded collaborator
may invent, implement, execute, diagnose, or write within its assigned task, returning
evidence without silently taking ownership or changing program or paper identity. Human intervention
is reserved for changing the original program, exceptional resources or permissions,
irreversible or outward actions, genuine authority conflicts, and final submission
sign-off.

## Comparison Ownership

Carry the intended main-table comparison into development and handoffs, not just its
score vector. Recover its meaning from explicit user instructions, official protocols,
and baseline artifacts; retain source-linked conditions, permitted freedoms, and unknown
provenance in \`COMPARISON_CONTRACT.json\`. Bind consequential runs to immutable contract
snapshots, effective settings and observed deviations; a matching hash proves identity,
not fairness. Consult the active research-foundation
baseline reference when changing conditions or deciding which results belong in a table.

The PI may optimize architecture, loss, training, and implementation within those
freedoms. A diagnostic or native-recipe comparison cannot silently replace the
commissioned comparison or inherit its win count. A justified new regime needs its own
matched comparison; reuse existing results where their meaning still matches. Neither
identical training recipes nor universal baseline reruns are required. Agent-authored
plans remain revisable without routine approval; explicit user-locked conditions remain
binding. Missing provenance leaves the affected comparison unresolved, not all research
blocked.

## Portable Workspace Rules

- Project directory: \`${localPath}\`.
- Keep this code workspace below 1 GB, including hidden files but excluding symbolic-
  link targets. Store models, datasets, environments, caches, checkpoints, predictions,
  and run outputs in an explicitly authorized external data or artifact root.
- Reuse revision-pinned public assets and compatible environments before downloading or
  installing duplicates. Record source, version, canonical path, and integrity metadata.
- Never delete files, datasets, caches, checkpoints, logs, artifacts, or directories
  without explicit user confirmation. Never modify an unknown process.

Machine-specific hosts, storage mounts, credentials, worker pools, and scheduler commands
must come from an explicit local infrastructure file or current user instruction. If a
project-local \`LOCAL_INFRASTRUCTURE.md\` exists, read it before infrastructure work; it
may add operational facts but cannot change the scientific program. Do not infer missing
infrastructure, copy stale worker IDs into this contract, or publish private machine
details in project-generation manifests.

Persist explicit durable user protocol changes in their existing owner here or in the
referenced infrastructure source, recording scope and provenance and replacing superseded
instructions. Keep temporary scientific choices in the live state. A handoff must carry
these protocols without copying stale resource IDs or turning local preferences into
global rules. Current artifacts and live process facts resolve execution claims.

## Compute Execution

The persistent PI owns scientific design and interpretation; it may delegate bounded
code, preparation, execution, monitoring, and validation within the authorized envelope.
Before occupying accelerators, finish downloads, dependency setup, ordinary preprocessing,
evaluator construction, configuration, and a meaningful CPU smoke test wherever possible.
Prepare a bounded real-path canary and a complete launch command that execute the real
model, data, evaluator, and output path; neither may download dependencies or allocate
resources while accelerators are occupied.

Estimate accelerator memory and placement from a real-path canary or a closely matched
completed run, including transient peaks and a meaningful margin. Do not create fixed
project-wide free-memory or utilization gates. When capacity is temporarily unavailable,
finish useful independent preparation but do not manufacture repeated audits, hashes,
checklists, or alternate method packets as substitutes for the selected experiment.

Use only explicitly authorized devices and inspect real occupancy immediately before
launch. Run only owned processes, expose objective progress, write durable logs and
completion markers, and validate artifacts after termination. Infrastructure failure is
not scientific evidence. Waiting for capacity is not a reason to narrow or abandon the
research program.

## PI-Owned Project State

Maintain \`PROJECT_STATE.json\` using the active research-pipeline research-tree
reference and its installed templates/helper. The PI owns its scientific interpretation;
the Markdown view is generated, not a second narrative to edit. Keep the original
objective at the root and connect important questions, explanations, principles and
realizations to supporting and contrary artifacts. Node kinds and branch decisions
are scientific descriptions, not fixed stages or automatic stop rules.

Keep the focus's investment rationale and the parent question that would matter again
if this implementation fails. Revisit ancestry and relevant alternatives at consequential
results or commitments; neither a small SOTA gap nor repeated local gains selects the
branch automatically. A child's failure does not refute a whole family, and a package
gain does not establish its preferred principle. Preserve valid code and evidence when
changing the explanation.

On scientific change, update the affected nodes, goal/claim movement, remaining decisive
comparisons, next action and manuscript dependencies together. Link raw results and
execution records instead of copying logs into the tree. Consume completed unread
results on return, verify them against actual artifacts, and execute the next useful
authorized action without routine permission. A background launch is not a wakeup path.

An agent-authored plan, interpretation or hold remains revisable, not a user boundary;
record actual user-locked conditions with their source. Registration freezes one run,
not the broader program. Retain the information-flow and full-data requirements of the
active skills, including training/development/test selection, temporal/cache boundaries
and evaluator meaning. The campaign manifest owns execution completion only.

For an existing project, reconcile the prior state with authority and decisive artifacts,
preserve it as referenced history, then migrate once to the tree and generated view.
Do not fabricate missing history, overwrite live work, or automatically restart sessions.
When a paper candidate becomes supported, carry its coherent contribution through
submission readiness while keeping unresolved comparisons and manuscript updates visible.
`;
}
