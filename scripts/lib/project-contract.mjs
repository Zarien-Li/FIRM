export function buildProjectContract({ projectId, localPath }) {
  return `# ${projectId} Project Contract

This file contains durable project-local authority and portable execution rules only.
Research behavior comes from \`~/.claude/CLAUDE-RESEARCH.md\` and the active research
skills in \`~/.claude/skills\`; do not duplicate their stages, checklists, or reviewer
rules here.

## Research Authority

Before scientific work, read \`PROGRAM_ORIGIN.md\`, \`PROJECT_IDENTITY.json\`,
\`SEED.md\`, and \`PROJECT_STATE.md\`. \`PROGRAM_ORIGIN.md\` preserves the
user-authorized arena and canonical object. \`PROJECT_IDENTITY.json\` is its immutable
structured mirror. \`PROJECT_STATE.md\` is the single current scientific state for the
project PI, the user, and portfolio tooling. No task list, session summary, review,
draft, archive, or identity \`current\` field may compete with it.

\`prompt.txt\`, archives, prior session prose, candidate methods, failure taxonomies,
paper identities, and stop or retire language are provenance or evidence only. They
cannot redefine the program merely because they are detailed or recent. Within the
sealed arena, the Research PI owns ordinary problem formulation, method construction,
experiments, diagnosis, iteration, claim calibration, and drafting. Human intervention
is reserved for changing the original program, exceptional resources or permissions,
irreversible or outward actions, genuine authority conflicts, and final submission
sign-off.

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

## Compute Execution

The project session owns scientific design, code, preparation, execution, monitoring,
result validation, and interpretation within the currently authorized resource envelope.
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

This project's Research PI is the only author of the scientific interpretation in
\`PROJECT_STATE.md\`. It is the sole current research state, not a state machine or
permission gate. Maintain it as a replacement-style current synthesis: the program
compass, strongest evidence and contrary evidence, current construction or empirical-
contact episode, credible positive object if any, latest decisive experiments, and the
next scientific action.

Keep one active episode as a scientific argument rather than a stage code: natural
problem, provisional principle, load-bearing locus, strongest published functional and
mechanistic rivals, discriminating prediction, substrate fidelity, latest evidence,
and next construction. A successor realization inherits maturity only when it preserves
the same principle and states the failed prediction, evidence-implicated component
change, preserved useful behavior, and new discriminating prediction.

Its authority is typed. Verified observations are evidence; explanations, gates,
thresholds, route choices, paper holds, and next actions are revisable PI
interpretations. Writing one of those choices into the state does not turn it into a
user constraint. A binding \`forbidden\`, \`locked\`, \`terminal\`, or equivalent rule
must cite the exact user or safety source and the object it governs. A registration
freezes one run, not future construction or the broader program.

At session start, compare \`PROJECT_STATE.md\` against authority, current artifacts, and
active work rather than copying an old session summary. Update it after a meaningful
scientific transition and before the next research action: a baseline or full experiment
is interpreted; the natural problem or explanation changes; a v1, attribution experiment,
or v2 changes the construction; the primitive changes; evidence is invalidated by an
implementation or evaluator defect; the blocker or next decisive action changes; or the
work enters paper harvest. Do not update it for routine reads, downloads, edits, or
training progress ticks.

Keep only the latest three to five decisive experiment records and link older raw
provenance. Every retained experiment record must state \`scientificQuestion\`,
\`comparison\`, \`execution\`, \`result\`, \`interpretation\`, and \`artifacts\`.
Distinguish infrastructure, implementation, evaluation, and scientific failures; never
mark infrastructure failure as scientific evidence.

Keep claim-bearing work faithful to the task, model scale, training regime, information
boundary, and compute envelope in the seed. A cheaper proxy is diagnostic until the
incumbent phenomenon and rival ordering are shown to survive there. Do not build a new
method around an effect created only by shrinking or otherwise changing the substrate.

After a credible positive object forms, maintain one active paper candidate and one
principle-predicted expansion campaign. Reconcile stale drafts or alternate method
identities before new breadth. If a method-owned precondition fails before the primary
outcome, diagnose or repair the construction on an existing accepted surface when
possible; do not count it as transfer failure or serially search for an easier dataset.
`;
}
