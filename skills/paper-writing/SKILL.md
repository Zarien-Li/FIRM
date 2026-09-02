---
name: paper-writing
description: Form, draft, mature, compile, and verify a research paper from validated evidence through a submission-ready package. Use for paper structure, section writing, reproducible figures, LaTeX compilation, manuscript-driven scientific gap discovery, numeric claim checking, or a full evidence-to-submission workflow. It owns authorship and orchestration, while independent scientific, experiment, and citation audits remain in their dedicated skills.
---

# Paper Writing

Write the strongest honest paper supported by the project. Prose cannot create missing
science, and an audit cannot create a contribution that research has not earned.

## Select One Mode

Resolve the request before loading details:

- `plan`: author argument, paper identity, narrative architecture, and figure plan;
- `write`: draft or revise sections from the author argument, plan, and evidence;
- `figures`: generate reproducible figures and tables;
- `compile`: build and visually inspect the PDF;
- `claim-audit`: verify manuscript claims and numbers against raw evidence;
- `full`: iterate research, authorship, verification, and assembly until the bounded
  paper is submission-ready or one explicit user-owned action remains;
- `research-draft`: organize a provisional positive object without implying paper entry.

Load only the needed reference:

- figures and tables: `references/figures.md`;
- LaTeX writing and compilation: `references/write-compile.md`;
- numeric and semantic claim fidelity: `references/claim-audit.md`;
- submission assembly and final report: `references/submission.md`.

Do not recursively invoke `paper-writing` from its own modes.

`full` does not mean "produce one complete draft." The first coherent draft is an
integration test. If it exposes a missing claim-bearing result, unresolved decisive
rival, invalid evaluator, changed method identity, or material cost/scope gap, return
that exact issue to the owning research skill, then revise the manuscript from the new
evidence. Continue until the package satisfies the submission boundary below. Do not
manufacture completeness through prose or open unrelated experiments.

## Establish The Writing Boundary

Read the authoritative research state, original program, raw decisive results, method
specification, strongest fair comparisons, relevant audits, venue rules, and current
manuscript. Treat drafts and prior reviews as claims to verify.

Do not treat a submission-shaped manuscript as mature until the PI can defend an
artifact-grounded method candidate or independently valuable, independently confirmed
non-method object. Earlier writing may clarify the reader, prior belief, surprise,
stakes, and missing evidence, but it cannot turn an immature object into a paper. A
`research-draft` may organize a provisional positive object without implying maturity.

Do not create a paper-entry status file or automated maturity gate. The lead PI writes
one claim-dependent candidate argument in the paper portion of `PROJECT_STATE.md`,
grounded directly in raw evidence. It should make clear:

- important natural or standard problem;
- positive object and exact contribution type;
- paper-bearing method, or independently confirmed non-method object;
- a frozen accepted natural benchmark, population, claim-relevant value surface,
  evaluator, and matched resource budget;
- a bounded, claim-sufficient set of decisive healthy published-method comparisons,
  including the strongest incumbent and directly claim-threatening rival known at
  the time of the judgment;
- an end-to-end realized method with a meaningful pre-specified advantage: either
  primary-metric superiority or a defensible Pareto gain in capability, quality,
  robustness, coverage, latency, memory, compute, supervision, or adoption cost;
- paired utility, retention, capability, safety, latency, and cost checks required by
  the claim;
- raw provenance, strongest contrary evidence, and scope debt;
- paper-to-program bridge and current contribution identity.

If the current contribution materially differs from the original program or preceding
construction lineage in operational effect, intervention locus, intended adopter,
accepted value surface, or contribution type, prior paper maturity does not transfer.
The PI's argument must cite a fresh literature decision for the new identity, including the
strongest functional rival and nearest mechanistic rival, and record one bounded
independent check of prize, program fidelity, and ownership. That check may return
`no material change`; it must not produce a general review, experiment menu, or higher
evidence bar.

Comparison membership is determined by what systems actually do under their deployment
contracts, not by the manuscript's nouns. Claim narrowing cannot delete a stronger
functional alternative. A zero-regression or retention result guaranteed by selective
routing is a design property, not an empirical advantage; the argument must instead show
utility on the affected population, end-to-end population value, coverage, and total
cost. Counts of experiments, scripts, audits, pages, PDFs, or release artifacts provide
no paper-entry evidence.

Do not require a parallel matrix of maturity fields or a fresh Codex verdict. An
optional near-final independent check may verify one named factual, claim, citation, or
proof uncertainty after the paper object exists. If a load-bearing anchor is later
downgraded, revise the candidate argument and every dependent claim while preserving
independent text and artifacts. Planning, provisional drafting, narrow editing, and
compilation may still expose scientific gaps; do not polish an immature candidate into
apparent maturity or let prose displace evidence acquisition.

A method program cannot become an analysis paper because its methods failed. A changed
contribution type requires an independently valuable object, independent confirmation,
a scientific consequence, and a fresh paper identity before contribution-directed
writing. A sparse late-stage verification may resolve a named uncertainty in the
resulting fixed object but does not select the identity. Ask the user only if an explicitly
locked project or deliverable boundary changes.

When evaluator repair, population repair, or provenance invalidation removes a
load-bearing result, preserve independent prose and artifacts but reset submission
entry. Rebuild the scientific object on the repaired surface and reconsider its prize
and nearest rivals; do not treat a surviving subset gain as automatic continuity of
the same paper.

## Establish The Author Argument Before The Outline

Before outlining sections, write a one-page `AUTHOR_ARGUMENT.md` in continuous prose.
It answers only:

- who the intended human reader is;
- what that reader currently believes or takes for granted;
- which observed fact changes that belief;
- why the change matters scientifically or practically;
- what the reader should understand, do, or investigate differently after reading.

Do not use tables, numerical inventories, contribution bullets, reviewer objections,
scope matrices, or non-claim lists in this document. Concrete facts may be named, but
the document is an authorial explanation rather than an evidence ledger. It should
sound natural when read aloud and make the paper's intellectual movement clear without
requiring section labels.

Trace seed-to-paper ancestry separately:

`original program -> natural problem -> explanation -> positive object -> accepted task
or natural system -> bounded paper`

The current object must matter at its exact supported specificity; it cannot borrow
importance from a broad field name or prestigious benchmark.

## Use Claims-Evidence As A Post-Draft Verification Tool

Do not generate prose, section order, paragraph order, or rhetorical transitions from
`CLAIMS_EVIDENCE.md`. After a complete narrative draft exists, create or update it:

```markdown
| ID | Draft claim and location | Raw evidence/path | Scope | Figure/table | Required qualification | Status |
|---|---|---|---|---|---|---|
| C1 | | | | | | supported / provisional / blocked |
```

Map every consequential title phrase, abstract sentence, contribution statement,
principal figure, and conclusion claim to evidence. Distinguish observation from
explanation, association from cause, discovery slice from claimed population,
development evidence from confirmation, and diagnostic from method evidence. Repair
unsupported prose after this check, but do not flatten a sound narrative into one
paragraph per claim row.

## Let A Dedicated Author Learn Directly From Excellent Papers

For high-stakes writing, select two to four genuinely strong, venue-relevant papers
using primary sources and delegate each full-paper reading to a separate fresh
subagent. Use these priorities:

- respected top-tier venue or field-defining archival outlet;
- closely matched contribution type, not merely shared keywords;
- clear evidence that the paper is exemplary, such as award/spotlight status,
  sustained influence, or strong field recognition;
- full text and reliable metadata available.

Assign each exemplar a distinct rhetorical role rather than averaging them into a
single template. For example, one may guide how the Introduction creates stakes and
surprise, another how Results order evidence, and another how Discussion turns findings
into consequences. Record why each paper was chosen and which section-level decision
it informs.

Do not create a synthesis of recurring patterns. Averaging exemplary papers removes
the distinctive choices that make them human and memorable.

Use one fresh author subagent for a coherent section or draft. Give that author:

- the complete selected exemplar papers for the relevant rhetorical roles;
- `AUTHOR_ARGUMENT.md`;
- the paper-bearing method or analytical object and decisive raw evidence;
- the venue and audience;
- the existing draft when revising.

The author subagent reads the exemplars in full and directly writes the section draft.
It adapts rhetorical decisions, paragraph movement, evidence timing, field-natural
language, and degree of specificity without copying wording, examples, claims, or
distinctive terminology. It may depart from every exemplar when this paper's argument
requires a different choice. The lead PI verifies the draft against evidence and the
author argument; it does not regenerate the section from a compact report.

This delegation keeps bulk reading out of the lead PI's context without discarding the
writing information before authorship. Reference papers remain author-side material
and must not be shown to an independent factual auditor.

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
- strongest honest claim and the change in reader understanding it supports;
- decisive comparison and primary value metric;
- paper-to-program bridge;
- section-level narrative movement and supporting evidence;
- figure/table rhetorical job;
- limitations or tradeoffs that materially change interpretation.

Organize experiments by questions and claims, not run chronology. Give the paper one
spine: every section and figure establishes the problem, explains the design, tests a
necessary prediction, measures value/cost, or bounds the claim.

The introduction should make clear why future work on the relevant problem would need
to engage with the phenomenon, principle, primitive, or resource. This is the citation
surface. State it as a scientific consequence, not promotional language.

## Draft The Problem Story Early, Then Rewrite It From Stable Evidence

Write a provisional Introduction from `AUTHOR_ARGUMENT.md` early enough that the
research question, prior belief, and surprise guide presentation choices. It is a
thinking instrument, not a frozen claim. Draft the method or analytical object,
results, setup, figures, and tables from evidence, then rewrite the Introduction once
the central result and contribution are stable. Write the abstract and title last.

Prefer cohesive paragraphs and fewer meaningful sections over checklist prose. A
paragraph need not announce its function. Use related work where it sharpens the
reader's model of the problem; do not turn the prose into a pre-emptive exchange with
reviewers.

Place a caveat beside a result only when it changes how that result should be
interpreted. Collect other genuine boundaries in a concise Limitations section.
Internal scope notes, rejected claims, and non-claim lists do not automatically enter
the manuscript.

The abstract should preserve the paper's particular argument rather than fill a fixed
sequence of rhetorical slots. Calibrate nouns such as prediction, mechanism, cause,
law, generality, robustness, and deployment against evidence during the post-draft
claim check.

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
| Is the scientific contribution important, coherent, and memorable? | lead PI plus human-reader editor |
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

Do not report project completion at the first full draft, first compiled PDF, or first
passing prose edit. Completion means `references/submission.md` can truthfully explain
that the bounded package is ready apart from the user's final factual, authorship, and
upload decisions. If it cannot, name the smallest evidence-grounded maturation agenda, assign
each item to its scientific or writing owner, execute the reversible items, and return
to assembly. A missing optional breadth experiment or speculative reviewer preference
does not belong on that agenda.

For final output, follow `references/submission.md` and report deliverable paths,
compilation status, audit freshness, unresolved factual or presentation issues,
material interpretation boundaries, and the single next action. Keep this operational
report separate from manuscript prose.
