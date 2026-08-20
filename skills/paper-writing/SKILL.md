---
name: paper-writing
description: Plan, draft, compile, and verify a research paper from validated evidence. Use for paper structure, section writing, reproducible figures, LaTeX compilation, numeric claim checking, or a full evidence-to-PDF workflow. It owns authorship and orchestration, while independent scientific, experiment, and citation audits remain in their dedicated skills.
---

# Paper Writing

Write the strongest honest paper supported by the project. Prose cannot create missing
science, and an audit cannot create a contribution that research has not earned.

## Select One Mode

Resolve the request before loading details:

- `plan`: claims-evidence spine, paper identity, outline, and figure plan;
- `write`: draft or revise sections from the approved spine;
- `figures`: generate reproducible figures and tables;
- `compile`: build and visually inspect the PDF;
- `claim-audit`: verify manuscript claims and numbers against raw evidence;
- `full`: run the applicable modes in order;
- `research-draft`: organize a provisional positive object without implying paper entry.

Load only the needed reference:

- figures and tables: `references/figures.md`;
- LaTeX writing and compilation: `references/write-compile.md`;
- numeric and semantic claim fidelity: `references/claim-audit.md`;
- submission assembly and final report: `references/submission.md`.

Do not recursively invoke `paper-writing` from its own modes.

## Establish The Writing Boundary

Read the authoritative research state, original program, raw decisive results, method
specification, strongest fair comparisons, relevant audits, venue rules, and current
manuscript. Treat drafts and prior reviews as claims to verify.

Do not create a Paper Spine until research has produced a credible positive method or
an independently valuable, independently confirmed non-method object. A
`research-draft` may organize that object earlier without implying paper maturity.

For submission-oriented writing, require an evidence-bearing `PAPER_ENTRY.md` owned by
the lead PI and grounded directly in raw evidence. It must establish:

- important natural or standard problem;
- positive object and exact contribution type;
- paper-bearing method, or independently confirmed non-method object;
- decisive incumbent, the most claim-threatening rival, their health, and fair end-to-end comparison;
- utility, capability, latency, or cost tradeoff;
- raw provenance, strongest contrary evidence, and scope debt;
- paper-to-program bridge and current contribution identity.

Do not require a parallel matrix of maturity fields or a fresh Codex verdict. An
optional near-final red-team audit may verify factual, claim, citation, or proof
integrity after the paper object exists. If a load-bearing anchor is later downgraded,
submission-oriented writing returns to hold while independent text and artifacts
remain preserved.

If entry is absent or `HOLD`, `plan`, `research-draft`, narrow editing, and compilation
may continue when useful, but label them `research draft - ENTRY HOLD`. Do not expand
an immature candidate into submission-shaped prose.

A method program cannot become an analysis paper because its methods failed. A changed
contribution type requires an independently valuable object, independent confirmation,
a scientific consequence, and a fresh paper identity before contribution-directed
writing. A sparse late-stage review may challenge the resulting fixed object but does
not select the identity. Ask the user only if an explicitly
locked project or deliverable boundary changes.

## Build One Claims-Evidence Spine

Create or update `CLAIMS_EVIDENCE.md`:

```markdown
| ID | Intended claim | Raw evidence/path | Scope | Figure/table | Caveat | Status |
|---|---|---|---|---|---|---|
| C1 | | | | | | supported / provisional / blocked |
```

Every title phrase, abstract sentence, contribution bullet, principal figure, and
conclusion claim must map to this spine. Distinguish observation from explanation,
association from cause, discovery slice from claimed population, development evidence
from confirmation, and diagnostic from method evidence.

Trace seed-to-paper ancestry separately:

`original program -> natural problem -> explanation -> positive object -> accepted task
or natural system -> bounded paper`

The current object must matter at its exact supported specificity; it cannot borrow
importance from a broad field name or prestigious benchmark.

## Learn Writing From Excellent Papers Without Polluting The Main Context

For high-stakes writing, select two to four genuinely strong, venue-relevant papers
using primary sources and delegate each full-paper reading to a separate fresh
subagent. Use these priorities:

- respected top-tier venue or field-defining archival outlet;
- closely matched contribution type, not merely shared keywords;
- clear evidence that the paper is exemplary, such as award/spotlight status,
  sustained influence, or strong field recognition;
- full text and reliable metadata available.

Each subagent reads one paper in full and returns a compact structural report: argument
arc, section jobs, evidence ordering, figure rhetoric, related-work positioning,
limitations, sentence/paragraph cadence, and practices worth adapting. It must not
copy prose, examples, claims, or distinctive terminology.

A separate synthesis subagent consumes only the compact reading reports and writes
`writing_models/SYNTHESIS.md`: recurring successful patterns, contribution-type-specific
choices, disagreements among exemplars, and candidate structures for this paper. The
main writer reads only that synthesis. Full papers and bulk reading never enter the
main context. Reference papers and synthesis are author-side material and must never be
shown to an independent reviewer or auditor.

An optional user-selected `--style-ref` may guide mechanical structure only. If no
local extractor exists, delegate the reading rather than installing tooling
automatically.

## Plan Around One Contribution Identity

One identity means one governing scientific principle, not one contribution bullet.
When earned by evidence, build a connected contribution stack around that principle:

- an important or named recurring phenomenon;
- a replacement principle or reusable primitive;
- a trainable/executable realization with accepted-task value;
- a predicted generalization, scale, model-family, or mechanism finding;
- reusable data, supervision, or system machinery.

Use only layers that are independently supported and causally connected. Do not force
a quota, inflate ablations into contributions, or combine unrelated projects. Equally,
do not hide an earned research program behind one benchmark delta.

Write `PAPER_PLAN.md` with:

- literal problem and stakes;
- default assumption, one-sentence replacement principle, and positive object;
- connected contribution layers and evidence for each;
- strongest honest claim and explicit non-claims;
- decisive comparison and primary value metric;
- paper-to-program bridge and scope;
- section job, supporting evidence, and transition;
- figure/table rhetorical job;
- limitations and known tradeoffs.

Organize experiments by questions and claims, not run chronology. Give the paper one
spine: every section and figure establishes the problem, explains the design, tests a
necessary prediction, measures value/cost, or bounds the claim.

The introduction should make clear why future work on the relevant problem would need
to engage with the phenomenon, principle, primitive, or resource. This is the citation
surface. State it as a scientific consequence, not promotional language.

## Draft Evidence First

Recommended order:

1. results, tables, and figures;
2. method or analytical object;
3. setup and comparison fairness;
4. introduction and contributions;
5. related work;
6. limitations and conclusion;
7. abstract and title last.

Prefer cohesive paragraphs and fewer meaningful sections over checklist prose. State
the strongest faithful version of related work and reviewer objections before
differentiating. Put consequential negative or boundary findings beside the result
they qualify, not only in limitations.

The abstract should be one compact argument: problem and stakes, design insight,
positive object, strongest evidence, and honest scope. Calibrate nouns: prediction,
mechanism, cause, law, generality, robustness, and deployment each require distinct
evidence.

## Generate, Compile, And Inspect

Generate important figures and tables from source artifacts, not manual transcription.
Each needs a reproducible path, final-size readability, uncertainty/sample definition,
and a caption whose takeaway stays within the data.

Use the project's existing build command. Do not install packages, use `sudo`, change
templates, or delete content to hide errors without explicit approval. Fix the first
causal compile error, rebuild, and inspect the rendered PDF for clipping, overflow,
illegible figures, broken references, and page-limit problems.

## Audit Ownership

Each check has one owner:

| Question | Owner |
|---|---|
| Did experiment/evaluator/provenance validly identify the quantity? | `/research-audit mode: experiment` |
| Do manuscript numbers and semantic qualifiers match raw evidence? | `paper-writing mode: claim-audit` |
| Do citations exist and support their local contexts? | `/research-audit mode: citation` |
| Is the scientific contribution important, coherent, and defensible? | `/research-review` artifact review |
| Is project state/value/identity ready for a boundary decision? | `/research-state-audit` |
| Are formal statements and proofs correct? | `/research-review` proof audit |

Do not rerun a green audit when its declared inputs and semantics are unchanged. Audit
findings qualify, remove, or repair claims; they do not invent experiments or redesign
the research program.

Use `/auto-paper-improvement-loop` only after contribution identity and evidence are
stable. It improves the artifact; it cannot resolve missing science.

## Stabilize And Finish

Once an important bounded contribution, positive object, decisive comparison, and
paper-critical evidence are stable, open new experiments only when they could change
correctness, importance, novelty, the object itself, or a likely reviewer decision.
Otherwise finish the paper. Research can remain open after submission.

For final output, follow `references/submission.md` and report deliverable paths,
compilation status, audit freshness, blocking/major/minor issues, honest non-claims,
and the single next action.
