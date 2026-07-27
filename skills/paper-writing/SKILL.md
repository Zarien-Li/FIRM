---
name: paper-writing
description: "Plan, draft, structure, compile, and polish a research paper from validated evidence. Uses full-text reference-paper apprenticeship through isolated subagents, a single claims-evidence spine, figure-aware section planning, LaTeX generation, LaTeX-to-PDF compilation with error fixing, zero-context claim-to-evidence verification, and independent citation review. Use for paper outlining, structural rewriting, section drafting, a complete report-to-PDF workflow, compiling a paper (\"编译论文\", \"compile paper\", \"build PDF\", \"生成PDF\"), or verifying that paper numbers match raw results (\"审查论文数据\", \"check paper claims\", \"verify numbers\", \"论文数字核对\")."
---

# Workflow 3: Paper Writing Pipeline

Orchestrate a complete paper writing workflow for: **$ARGUMENTS**

## Overview

This skill runs a complete paper pipeline in a single skill, chaining sub-skills where they remain independent:

```
/paper-writing → /paper-figure → LaTeX writing → compile → /auto-paper-improvement-loop
  (plan)         (plots)        (Phase 3)     (Phase 4)   (review & polish ×2)
                                          ↓ audit gates (inline, this skill):
                                    proof audit → claim audit → citation audit
```

Compilation (Phase 4) and the zero-context paper claim audit (Phase 4.7 / 5.5) are built into this skill — they used to be standalone skills and are now phases. Each phase builds on the previous one's output. The final deliverable is a polished, reviewed `paper/` directory with LaTeX source and compiled PDF.

The workflow treats writing as scientific argument design, not as transcription of the experiment log. Reference papers may teach structure and rhetorical technique, but never supply this paper's claims or evidence.

For complete manuscript work, follow
[the research control protocol](../shared-references/research-control-protocol.md).
Research continuity does not imply manuscript continuity: the program may continue
while a paper candidate is reset or frozen.

## Constants

- **VENUE = `ICLR`** — Target venue. Options: `ICLR`, `NeurIPS`, `ICML`, `CVPR`, `ACL`, `AAAI`, `ACM`, `IEEE_JOURNAL` (IEEE Transactions / Letters), `IEEE_CONF` (IEEE conferences). Affects style file, page limit, citation format.
- **MAX_IMPROVEMENT_ROUNDS = 2** — Number of review→fix→recompile rounds in the improvement loop.
- **REVIEWER_MODEL = `account-default`** — Use Codex MCP without a `model` field for all reviews; inherit the current account model per `/research-review`.
- **AUTO_PROCEED = false** — Auto-continue is allowed within mechanical assembly such as figure generation, LaTeX compilation, and improvement rounds. Marking a PDF `submission-ready` and deciding venue-specific LLM disclosure still require user approval because they are consequential submission decisions. Set `true` only for a pure recompile of an already-approved submission.
- **HUMAN_CHECKPOINT = false** — When `true`, the improvement loop (Phase 5) pauses after each round's review to let you see the score and provide custom modification instructions. When `false` (default), the loop runs fully autonomously. Passed through to `/auto-paper-improvement-loop`.
- **ILLUSTRATION = `false`** — Non-data figures (architecture diagrams, pipeline figures, method illustrations) are created manually and placed in `figures/` before Phase 3.

> Override inline: `/paper-writing "NARRATIVE_REPORT.md" — venue: NeurIPS, human checkpoint: true`
> IEEE example: `/paper-writing "NARRATIVE_REPORT.md" — venue: IEEE_JOURNAL`

## Inputs

This pipeline accepts one of:

1. **`NARRATIVE_REPORT.md`** (best) — structured research narrative with claims, experiments, results, figures
2. **Research direction + experiment results** — the skill will help draft the narrative first
3. **Existing `PAPER_PLAN.md`** — skip Phase 1, start from Phase 2

For submission-oriented empirical papers, also require:

- `PAPER_ENTRY.md` with `entry: PASS`
- `RESULT_TO_CLAIM.md`
- `RESEARCH_STATE_AUDIT.md` or an equivalent `/research-state-audit` artifact when contribution type changed or another consequential boundary was audited
- provenance for the method claim or claim-defining experiment, including the relevant registration when one exists

These are requirements for complete submission-oriented planning, LaTeX writing,
automatic expansion, and readiness claims. Before `entry: PASS`, maintain a compact
`CANDIDATE_CLAIM.md` containing the provisional fingerprint, one-sentence claim,
intended main figure/table, supported facts, and claim-threatening evidence. Do not
create or polish a full `main.tex` merely to organize research.

Narrow edits, mechanical compilation, or evidence correction of an existing
manuscript remain allowed, but they do not confer maturity. If the user explicitly
requests an exploratory draft before PASS, label it `exploratory — ENTRY HOLD`, keep
the missing evidence visible, and do not run automatic prose expansion,
submission-polish loops, or readiness packaging.

Reuse the project's existing narrative, candidate claim, paper plan, or concise
research state when possible. Do not create parallel documents merely to satisfy an
artifact name.

If `RESULT_TO_CLAIM.md` is missing, create it with `/signal-analysis`
(Consequential Runs: From Result To Claim) before starting a submission-oriented
paper. If it concludes that no paper contribution exists yet, that claim-changing
evidence is missing, or that the requested venue exceeds the honest ceiling, do not
label the output submission-ready for that venue. If useful, update only
`CANDIDATE_CLAIM.md` from supported facts and the candidate contribution rather
than pretending the project has no intellectual shape.

If `PAPER_ENTRY.md` is missing or stale, build it from raw artifacts and request a
fresh Codex Prize/Fidelity/Entry review through `/research-review`. The writer may
assemble the packet, but may not award itself `PASS`. A previous paper, review
score, polished abstract, or user-visible deadline is not a substitute.

If `RESULT_TO_CLAIM.md` says the strongest honest result is still a private slice, do not start by writing a top-tier paper of any contribution type. First either broaden or independently confirm the evidence, obtain user approval before formally committing a changed submission claim, or preserve the slice as a limitation or diagnostic asset inside a stronger story.

Writing cannot repair lost significance. Before using the seed's broad motivation, read the original program separately from the current paper and verify an evidence-backed paper-to-seed bridge: what broad value remains, what narrower insight was earned, and how the contribution reconnects to a naturally affected population, meaningful severity, a shared incumbent defect, or a scientific, engineering, or operational decision that changes. A precise cell does not inherit the benchmark's importance merely because it was discovered there.

Record material scope debt in prose: the qualifiers, private slices, model/dataset restrictions, and exceptions needed for the claim, plus the evidence that repays each important narrowing. This is not a numeric readiness score. It prevents the manuscript from hiding an unsupported population behind broad field language.

If the available input is only a direction card, project instruction, brainstormed idea,
research program card, pilot note, or literature gap, return to research. Those are not
paper-writing inputs.

If the state audit reports missing claim-changing baselines, pending or unread decisive runs, invalidated conclusions, proxy evidence carrying the headline, or undigested failures, return to the named research work before submission-oriented planning.

The more detailed the input (especially figure descriptions and quantitative results), the better the output.

## Authority Boundary

This skill writes and audits a contribution that research has already earned. It does not choose the permanent contribution identity, reinterpret a failed method into an analysis paper, freeze the broader thesis, or decide that a field has been exhausted.

Current validated evidence and the live research state outrank an old draft, paper plan, contract, or earlier `RESULT_TO_CLAIM.md`. If they conflict, update the research interpretation first. A working draft is a lossy view of the research, never its constitution.

Stable evidence is not sufficient by itself. Before submission-oriented writing, require a mature positive object: a competent method with end-to-end value, or an independently important analytical, theoretical, measurement, or systems object with confirmation and consequence. Writing cannot turn a stable boundary, correlation, failure atlas, or sequence of failed methods into a contribution.

Writing and submission audits may block claims in a manuscript. They cannot prohibit future method redesign or become program-level scientific verdicts.

Treat paper identity as a fingerprint:
`problem | contribution type | positive object | primitive | population/task |
primary metric | decisive baseline`. If contribution type, positive object,
primitive, primary metric, or claimed population changes, freeze the old manuscript
and require a new paper-entry review. The new identity inherits evidence and
lessons, not readiness.

Trip the manuscript circuit breaker when a decisive baseline wins the registered
primary outcome, the metric/population/object changes after results, seed provenance
is mixed or selectively excluded, a fair control reverses the central claim, the
advertised method was never implemented, or only a selected private cell survives.
Finish atomic work, mark the manuscript `frozen — ENTRY HOLD`, reconcile raw
evidence, and return to research. Do not start a rebuttal grid whose only scientific
job is preserving the title.

## Reference-Paper Apprenticeship With Context Isolation

For a new high-stakes paper or a major structural rewrite, study a small set of excellent full papers before freezing the outline. Skip this only when the project already has current writing-model reports for the same venue, contribution type, and paper claim, or when the task is a narrow local edit.

Select 2--4 papers that are useful writing exemplars, not merely topical neighbors. Match the target venue, contribution type (method, systems, theory, measurement), argument shape, and evidence burden. Include a strong recent accepted paper when possible, but do not choose papers only because their terminology resembles ours.

Treat exemplar quality as a research judgment, not a search-ranking result. Before assigning a paper to a reading subagent, verify its bibliographic identity and publication status from the official venue proceedings, journal page, DOI record, or another authoritative source. Search snippets, citation aggregators, author webpages, and arXiv metadata can help discovery but cannot by themselves establish that a paper is an accepted venue paper.

Build the set from field-appropriate high-quality sources:

- prefer full papers from the target venue or a peer venue with comparable selectivity and reviewing standards;
- give extra weight to best-paper candidates or awards, distinguished/spotlight/oral papers, widely recognized field-defining papers, and recent papers whose structure has survived serious peer review;
- include both a recent target-venue exemplar and a canonical exemplar when that combination is useful, rather than selecting only new or only highly cited work;
- judge writing quality directly after opening the full paper. Prestige or citation count is a useful prior, not proof that its exposition fits this project;
- use a preprint only when it is unusually influential or uniquely matched and no adequate peer-reviewed exemplar exists. Label it as a preprint and never let unreviewed papers dominate the set;
- do not use predatory or unclear journals, low-quality conference proceedings, student reports, blog posts, workshop extended abstracts, or papers from unverifiable venues as writing exemplars. A workshop paper is eligible only when the target itself is a workshop or the paper is a canonical exception, and the reason must be recorded;
- do not mistake topic similarity for exemplar quality. A weaker paper can remain in related work, but it must not teach the paper's structure merely because it uses the same keywords.

Record the quality rationale beside each selected paper: official publication source, venue and year, contribution type, why its argument is structurally matched, and why it is a credible writing model. If fewer than two strong peer-reviewed exemplars survive verification, broaden the search across adjacent top venues or contribution types instead of lowering the quality bar silently.

Download and preserve the complete PDFs. Do not infer writing technique from abstracts, blog summaries, or metadata. Use one fresh subagent per paper so full-text reading does not consume the main researcher's context. Give each subagent the PDF, target venue, contribution type, and only the minimum project context needed to judge transferability. Each subagent writes `writing_models/<paper-slug>.md` containing:

- the paper's one-sentence argumentative spine;
- the job of every section and the transition between sections;
- the introduction's rhetorical beats and where the main claim first becomes precise;
- how intuition, formalism, algorithm, and implementation are sequenced;
- how experiments are organized by research question rather than chronology;
- the role of each main figure/table in the argument;
- how related work, limitations, exceptions, and negative results are positioned;
- reusable writing techniques, paper-specific choices that should not transfer, and failure modes to avoid;
- exact section/page pointers for important observations, without long quotations or copied prose.

Then launch a separate synthesis subagent. It reads only the per-paper writing models plus this project's bounded claim and claims-evidence matrix, not the full PDFs or the entire research history. It writes `writing_models/SYNTHESIS.md` with:

- patterns shared across the exemplars;
- disagreements that reflect paper type rather than universal rules;
- the recommended one-sentence spine for our paper;
- a proposed section order and the scientific job of each section;
- a figure/table argument map;
- specific structural moves to borrow and choices to reject;
- a short list of claim-threatening evidence gaps that writing cannot repair.

The main thread reads the synthesis and only targeted page excerpts when a concrete ambiguity remains. Never paste several full papers or all per-paper notes into the main context. The main researcher owns the final outline and checks every borrowed structural move against the project's real evidence. This is context isolation, not delegation of scientific judgment.

Reuse existing `writing_models/` artifacts when they remain matched and current. Do not repeatedly reread the same PDFs merely to create more paperwork. Never pass reference PDFs or writing-model reports to independent claim, citation, or reviewer agents; those reviewers must judge the submitted artifact without author-side coaching.

## Prose Structure Discipline

Apply these rules in paper planning, LaTeX writing, and improvement rounds:

- Open with the **problem class**, not the private crack. The introduction should make a reviewer accept that the field has a missing dimension before presenting the method. A good structure is: natural setting -> recurring class of failures -> missing abstraction/design dimension -> method as the natural implementation.
- Keep the value ancestry honest. Distinguish the slice that exposed the problem from the natural class that carries the loss and the population the paper claims. Use the slice as a microscope when appropriate, but do not widen it rhetorically or let broad field motivation conceal a tiny supported scope.
- Make the reintegration result visible in the argument. A method or principle learned in a narrow slice should return to the accepted task or natural system before the paper claims field-level leverage; otherwise the paper must ground importance in an independently consequential rare case, theory result, or operational decision.
- Prefer **positive inevitability** over negative ownership. Related work should not read like "A/B/C lack our five operations." First define the object the paper creates (training axis, execution semantics, state representation, routing/update primitive), then show why existing systems are special cases or incomplete with respect to that object.
- State naturality honestly. If evidence comes from induced drift, adversarial slices, small workloads, or constructed counterfactuals, say what prevalence is and is not claimed, and include the natural trace/transfer evidence that makes the class believable.
- State irreducibility. Before the final draft, the paper must answer the obvious substitute: stronger SOTA, plain SFT/objective, validator+lineage, cache key+retry, calibrated threshold, verifier, or wrapper. If the paper cannot answer it, the contribution is not yet submission-ready.
- Do not overuse bold text. Use bold only for genuinely load-bearing terms, not for every contribution, caveat, or paragraph lead.
- Do not overuse `itemize`/bullet lists. Use lists only when the content is a true enumeration, protocol, contribution list, or compact comparison. Explanations, motivations, related-work positioning, and limitations should usually be cohesive prose.
- Do not split every one or two sentences into separate paragraphs. Build paragraphs around a complete idea: claim, support, and transition.
- Do not create a `subsection` or `subsubsection` for one or two short paragraphs. Merge small units into the parent section unless the heading names a real conceptual unit used later.
- Prefer fewer, stronger sections with flowing argumentation over many tiny labelled fragments.
- During auto-improvement, remove unnecessary bold/list/heading churn before polishing style. A paper that reads like a checklist is not submission-ready prose.
- Do not strawman related work, baselines, reviewer objections, negative results, or limitations. Before criticizing an incumbent or objection, write its strongest faithful version and then explain the actual difference. Do not make the paper look stronger by weakening what it compares against.
- Give the paper one load-bearing spine. Every section, experiment, and figure should either establish the problem, explain the design, test a necessary prediction, delimit scope, or support the final claim. Do not preserve research chronology or every interesting branch.
- Write the abstract as one compact argument unless the venue explicitly requires otherwise: problem and stakes, discovered design insight, method, strongest evidence, and honest scope. A late result earns at most the space warranted by how much it changes the spine.
- Keep the introduction at the level of problem, missing abstraction, contribution, and evidence preview. Do not duplicate the method section or introduce detailed equations before they are needed.
- Organize related work by scientific relationship, not project-internal labels such as `C1`, `H3`, or ledger names. Keep it proportionate to the page budget and use it to position the positive object, not to enumerate absent components.
- Organize experiments around questions and claims, not run order. Every stated finding needs a visible experiment, theorem, trace, or system measurement; every major experiment should have a clear claim-level purpose.
- Put consequential negative or boundary findings in Results/Analysis when they change interpretation. Limitations state what remains unsupported; they should not hide an inconvenient measurement.
- Distinguish induced from natural behavior, mechanism existence from prevalence, one cell from generality, and scale sensitivity from cross-setting transfer. Preserve those distinctions in the title, abstract, captions, and conclusion.
- Give each figure and table a rhetorical job. Figure 1 should normally establish the natural problem, missing abstraction, and intervention locus; it must not introduce a new unsupported claim. Captions explain the takeaway and scope, not merely the axes.
- Once a mature positive object, bounded claim, decisive comparison, and paper-critical evidence are all supported, stabilize the manuscript spine. Open a new experiment only when it could change correctness, value, novelty, the method itself, or a likely reviewer decision; otherwise finish the paper. This stabilizes the manuscript, not the broader research program.

## Explicit Style-Reference Shortcut (`--style-ref: <source>`, opt-in)

This shortcut extracts mechanical style statistics from one user-selected source. It does not replace the full-text, subagent-based apprenticeship above. When the user does not pass `--style-ref`, skip only this helper; still use the apprenticeship when the writing task warrants it.

When `--style-ref: <source>` is in `$ARGUMENTS`, derive a compact structural profile before
Phase 1. If the host repository includes an `extract_paper_style.py` helper, it may be used.
Otherwise assign the source paper to an isolated reading subagent and consume only its compact
structural report. Missing optional tooling must not abort ordinary paper writing.

```bash
if [ -f tools/extract_paper_style.py ]; then
  python3 tools/extract_paper_style.py --source "<source>"
else
  echo "optional style helper absent; use isolated reading or skip --style-ref" >&2
fi
```

Then forward `--style-ref: <source>` only to the **writer-side** sub-skills:
- `/paper-writing` (Phase 1) — outline structure
- `/paper-writing` (Phase 3) — section-by-section prose


**Strict rules:**

- Use `style_profile.md` as **structural** guidance only. Match section-count tendency, theorem density, caption-length distribution, sentence cadence, math display ratio, citation style.
- **Never copy prose, claims, examples, or terminology** from anything reachable through the cache.
- **Never pass `--style-ref` (or the cache contents) to reviewer / auditor sub-skills** — Phase 4.5 (`/research-review` proof audit), Phase 4.7 / 5.5 (claim audit), Phase 5 (`/auto-paper-improvement-loop` reviewer), Phase 5.8 (`/citation-audit`) MUST run on the artifact alone. Cross-model review independence (`../shared-references/reviewer-independence.md`).

## Pipeline

### Phase 0: Assurance Setup

Resolve the active `assurance` level and persist it so Phase 6's external
verifier reads the same value. **Run once at pipeline start, before Phase 1.**

#### Phase 0.5: Contribution Readiness Check

For any empirical paper, read `PAPER_ENTRY.md`, the latest
`RESULT_TO_CLAIM.md`, and live research state before Phase 1. Verify that the entry
artifact matches the current identity fingerprint and raw evidence. When they
disagree, current validated evidence wins and the old entry automatically becomes
`HOLD`.

If `entry` is not `PASS`, stop the complete manuscript pipeline before reference
apprenticeship, figure production, outline freezing, LaTeX expansion, or polish.
Return the highest-value named research action and update `CANDIDATE_CLAIM.md`.
Existing-draft compilation or a user-requested narrow edit may continue without
changing maturity, but the result remains `exploratory — ENTRY HOLD`.

Also read the latest research state audit when this is a contribution-type change, submission-oriented draft, or other boundary that warranted one, and confirm:

- baseline suite is complete or explicitly irrelevant to the supported scope
- no pending/unread full run can change the paper claim
- invalidated conclusions have been removed or rerun
- toy/proxy/probe-only evidence is not carrying broad claims
- the paper claim is traceable to completed evidence and, for registered decisive runs, preserves the prospective forecast rather than relying on a direction card
- the identity fingerprint has not changed since the independent entry review
- all seed runs use traceable trainer/config provenance and post-hoc exclusions are visible
- no manuscript circuit-breaker condition is active

Before planning prose, trace the ancestry of the intended title, abstract sentences, and contribution bullets: identify the raw artifact/theorem that supports each, its scope, and the caveat that changes its wording. A compact map is useful when the draft is complex, but do not turn it into paperwork. The purpose is to keep the paper's intellectual shape faithful to what was actually learned. A manually rewritten example, proxy encoding, mixed-seed table, synthetic slice, or diagnostic-only result may appear only with that boundary visible; it cannot silently carry a broad or method-level sentence.

Trace the seed-to-paper ancestry separately: preserve the original program, state the current bounded paper, enumerate material scope debt, and identify completed reintegration evidence on a standard task or natural system. When direct reintegration is not the source of value, state the independently earned severity, theoretical consequence, or operational consequence instead. The title and abstract may name the broad field only to the degree this bridge supports; they cannot borrow the seed's importance for a private result.

Judge the intended contribution on its own terms:

- A method paper needs a natural value problem, a load-bearing intervention, fair strong comparisons, end-to-end value, and an honest account of costs and scope.
- An analysis, mechanism, or measurement paper needs an independently valuable positive object, selection provenance, a non-trivial explanation or measurement, confirming rather than only exploratory evidence, a scientific consequence, and a distinction from the strongest existing analytical account.
- Every contribution type must remain important at the exact supported scope. Check natural support, severity, affected systems or decisions, and whether the concrete object has community leverage independent of the broad seed.
- The best-case prize must be visible at the paper boundary. State what the strongest honest contribution would be if all remaining non-claim-threatening work succeeded; do not polish a paper whose ceiling is already a correct but inconsequential private-cell result.
- A contribution type that changed after unsuccessful method development must be newly earned, and its use as the formal submission identity must be user-approved. Research-stage exploration of that identity is autonomous. Remove the failed lineage mentally: the paper should still have a natural object, confirmation, and consequence. Failed implementations cannot serve as negative proof of a bottleneck or impossibility unless they are valid isolating interventions.

Calibrate title-level scientific nouns to the evidence. An association or decomposition need not be called a mechanism. A predictor requires evidence on observations that did not select it. A mechanism requires isolating evidence appropriate to the domain. A law requires out-of-sample explanatory or predictive force, uncertainty, and meaningful boundaries; a small number of environments connected by a fitted story is discovery evidence, not a law by itself. `Universal` requires genuinely broad heterogeneous support.

If the current interpretation concludes that there are true findings or analysis
assets but no mature paper contribution yet, return to the named claim-changing
research. `CANDIDATE_CLAIM.md` may remain for continuity, but do not polish it into
apparent maturity. If a paper contribution exists only at a lower venue ceiling or
narrower scope, write to that honest scope only with user agreement and a fresh
entry review. If pending evidence can invalidate the object, main comparison, or
contribution identity, wait for or repair it. If the contribution is earned and
remaining questions only broaden later work, proceed without manufacturing new
obligations.

This check asks whether the project has earned its intended paper story. Later numeric, citation, and proof audits verify that the written story remains locally and globally faithful; they cannot create a contribution that was absent here.

**Resolution order** (first match wins):

1. Explicit `--assurance: draft | submission` in `$ARGUMENTS`
2. Derived from `--effort:`
   - `lite` / `balanced` → `draft` (default, **zero change from current behavior**)
   - `max` / `beast` → `submission`
3. Default: `draft`

**Action:**

```bash
mkdir -p paper/.research-skills
echo "<resolved-level>" > paper/.research-skills/assurance.txt   # draft or submission
```

**What each level does downstream:**

- **`draft`** — Existing behavior. Audits run only when their content detector
  matches (Phase 4.5 / 4.7 / 5.5 / 5.8). Missing artifacts are non-blocking.
  Silent-skip allowed.
- **`submission`** — The three mandatory audits (proof audit via `/research-review`,
  claim audit via Phase 4.7, citation-audit) are treated as load-bearing gates. Each
  sub-audit must emit its JSON artifact (PASS / WARN / FAIL / NOT_APPLICABLE /
  BLOCKED / ERROR) — never silent-skip. Phase 6 runs
  the self-contained audit-artifact verification in Phase 6; any missing, stale, malformed, or
  blocking artifact prevents a submission-ready report.

**Escape hatch:** a user wanting the old "beast = depth-only, no audit gate"
can pass `--effort: beast, assurance: draft` explicitly. Legal but
discouraged for actual submissions. See
`shared-references/assurance-contract.md` for the full contract.

**Announce the resolved level in-line before Phase 1:**

```
📋 Assurance: <level> (derived from effort: <effort>)
   <either "current behavior, no audit gate" OR "mandatory self-contained audit verification">
```

### Phase 1: Paper Plan

Invoke `/paper-writing` to create the structural outline:

```
/paper-writing "$ARGUMENTS"
```

If `--style-ref: <source>` was passed in `$ARGUMENTS` and the helper succeeded above, append `--style-ref: <source>` to the invocation: `/paper-writing "<topic> --style-ref: <source>"`. (Writer-side phase — forwarding is allowed; reviewer/auditor phases below must not see the style ref.)

**What this does:**
- Reuse or complete `writing_models/SYNTHESIS.md` through the context-isolated apprenticeship above
- Parse NARRATIVE_REPORT.md for claims, evidence, and figure descriptions
- Freeze a one-sentence paper spine and give every planned section a scientific job
- Build a **Claims-Evidence Matrix** — every claim maps to evidence, every experiment supports a claim
- Import the supported scope, contribution identity, strongest supported contribution if one exists, missing claim-changing evidence, and honest venue judgment from `RESULT_TO_CLAIM.md`
- Design section structure according to the paper's argument and venue, not a fixed section count
- Plan figure/table placement with data sources
- Record what each section deliberately excludes so the introduction, method, and experiments do not duplicate one another
- Scaffold citation structure
- Account-default Codex reviews the plan for completeness

**Output:** `PAPER_PLAN.md` with section plan, figure plan, citation scaffolding.

`PAPER_PLAN.md` must include the paper spine, section contracts, claims-evidence matrix, figure/table argument map, honest scope distinctions, and the relevant structural lessons adopted or rejected from `writing_models/SYNTHESIS.md`.

**Progress update:** Present the plan summary to the user, then continue to Phase 2 by default.

```
📐 Paper plan complete:
- Title: [proposed title]
- Sections: [N] ([list])
- Figures: [N] auto-generated + [M] manual
- Target: [VENUE], [PAGE_LIMIT] pages
```

Do not stop merely to ask whether figure generation should begin. Treat
`AUTO_PROCEED=true` as the default for an already authorized writing task whose
current fingerprint still has `entry: PASS`. Pause when entry becomes stale or a
circuit breaker trips, the user explicitly requested staged approval, the plan
changes a user-locked title/contribution identity/venue or formal deliverable,
required evidence is missing, exceptional spending or an irreversible external
action is involved, or the user interrupts with a change. If the user requests
changes while work continues, incorporate the newest instruction before the next
irreversible or submission-facing action.

### Phase 2: Figure Generation

If `--style-ref: <source>` was passed in `$ARGUMENTS` and the helper succeeded above, append `--style-ref: <source>` to every writer-side sub-skill invocation in this pipeline (Phases 1, 2b, 3, 5). Do **not** append it to reviewer/auditor invocations (Phases 4.5, 4.7, 5.5, 5.8).

Invoke `/paper-figure` to generate data-driven plots and tables:

```
/paper-figure "PAPER_PLAN.md"
```

**What this does:**
- Read figure plan from PAPER_PLAN.md
- Generate matplotlib/seaborn plots from JSON/CSV data
- Generate LaTeX comparison tables
- Create `figures/latex_includes.tex` for easy insertion
- Account-default Codex reviews figure quality and captions

**Output:** `figures/` directory with PDFs, generation scripts, and LaTeX snippets.

> **Scope:** `paper-figure` covers data plots and comparison tables. Architecture diagrams, pipeline figures, and method illustrations are handled in Phase 2b below.

#### Phase 2b: Architecture & Illustration (Manual)

All non-data figures — architecture diagrams, pipeline figures, method illustrations — are created manually:

- Draw them with draw.io, Figma, Keynote, or TikZ and place them in `figures/` before Phase 3
- `paper-figure` preserves any existing figures in `figures/` and generates only the LaTeX `\includegraphics` snippets for them
- Mark them `[MANUAL]` in the figure plan and `latex_includes.tex`

**Checkpoint:** List generated vs manual figures.

```
📊 Figures complete:
- Data plots (auto, Phase 2): [list]
- Manual (need your input): [list]
- LaTeX snippets: figures/latex_includes.tex

[If manual figures needed]: Please add them to figures/ before I proceed.
[If none needed]: Shall I proceed with LaTeX writing?
```

### Phase 3: LaTeX Writing

Invoke `/paper-writing` to generate section-by-section LaTeX:

```
/paper-writing "PAPER_PLAN.md"
```

If `--style-ref: <source>` was passed in `$ARGUMENTS` and the helper succeeded above, append `--style-ref: <source>` to the invocation: `/paper-writing "PAPER_PLAN.md --style-ref: <source>"`.

**What this does:**
- Write each section following the plan, with proper LaTeX formatting
- Preserve the one-sentence spine while giving each section a distinct job; do not narrate experiment chronology
- Keep the abstract compact, the introduction non-duplicative, related work field-facing, and results claim-indexed
- Insert figure/table references from `figures/latex_includes.tex`
- Build `references.bib` from citation scaffolding
- Clean stale files from previous section structures
- Automated bib cleaning (remove uncited entries)
- De-AI polish (remove "delve", "pivotal", "landscape"...)
- Account-default Codex reviews each section for quality

**Output:** `paper/` directory with `main.tex`, `sections/*.tex`, `references.bib`, `math_commands.tex`.

**Checkpoint:** Report section completion.

```
✍️ LaTeX writing complete:
- Sections: [N] written ([list])
- Citations: [N] unique keys in references.bib
- Stale files cleaned: [list, if any]

Shall I proceed with compilation?
```

### Phase 4: Compilation

Compile the LaTeX paper to a clean candidate PDF and fix any issues. This phase is
self-contained — it can also be invoked standalone when the user asks to
"编译论文 / compile paper / 生成PDF". Compilation alone does not confer a
submission-ready label.

**Constants:**

- **COMPILER = `latexmk`** — LaTeX build tool. Handles multi-pass compilation automatically.
- **ENGINE = `pdflatex`** — LaTeX engine. Options: `pdflatex` (default), `xelatex` (for CJK/custom fonts), `lualatex`.
- **MAX_COMPILE_ATTEMPTS = 3** — Maximum attempts to fix errors and recompile.
- **PAPER_DIR = `paper/`** — Directory containing LaTeX source files.
- **MAX_PAGES** — Page limit. ML conferences: main body to Conclusion end (excluding references & appendix). ICLR=9, NeurIPS=9, ICML=8. **IEEE venues: references ARE included in page count.** IEEE journal ≈ 12-14 pages, IEEE conference ≈ 5-8 pages (all inclusive).

**Step 1: Verify prerequisites**

```bash
# Check LaTeX installation
which pdflatex && which latexmk && which bibtex

# If not installed, provide instructions:
# macOS: brew install --cask mactex-no-gui
# Ubuntu: sudo apt-get install texlive-full
# Server: conda install -c conda-forge texlive-core

# Must exist
ls $PAPER_DIR/main.tex
# Should exist
ls $PAPER_DIR/references.bib
ls $PAPER_DIR/sections/*.tex
ls $PAPER_DIR/figures/*.pdf 2>/dev/null || ls $PAPER_DIR/figures/*.png 2>/dev/null
```

**Step 2: First compilation attempt**

```bash
cd $PAPER_DIR
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee compile.log
```

**Step 3: Error diagnosis and auto-fix**

If compilation fails, read `compile.log` and fix common errors:

| Error | Fix |
|---|---|
| `! LaTeX Error: File 'somepackage.sty' not found.` | `tlmgr install somepackage`, or remove the `\usepackage` if unused |
| `LaTeX Warning: Reference 'fig:xyz' undefined` | Check `\label{fig:xyz}` exists in the correct figure environment |
| `! LaTeX Error: File 'figures/fig1.pdf' not found.` | Check extension (.png vs .pdf); update `\includegraphics` path |
| `LaTeX Warning: Citation 'smith2024' undefined` | Add the missing entry to `references.bib` or fix the citation key |
| `[VERIFY]` markers in text | Left by LaTeX writing — search for the correct information or flag to the user |
| `Overfull \hbox (12.5pt too wide)` | Minor: usually ignorable. If severe (>20pt), rephrase text or adjust figure width |
| BibTeX syntax (`expecting a ',' or a '}'`) | Fix missing comma, unmatched braces, special characters in title |
| `\crefname` undefined for custom theorem types | Ensure `\crefname{assumption}{Assumption}{Assumptions}` etc. are in the preamble after `\newtheorem` |

**Step 4: Iterative fix loop** — up to MAX_COMPILE_ATTEMPTS rounds of compile → parse errors → auto-fix → recompile. For each error: read the message, locate source file and line, apply fix, recompile.

**Stuck after 2 attempts?** If Codex plugin is installed, ask Codex to independently read the LaTeX source and `compile.log` to spot issues Claude missed (conflicting packages, encoding problems, subtle macro errors). If not installed, continue with Claude's own diagnosis.

**Step 5: Post-compilation checks**

```bash
ls -la main.pdf                    # exists and non-trivial
pdfinfo main.pdf | grep Pages      # page count
grep -c "LaTeX Warning.*undefined" compile.log   # undefined refs → 0
grep -c "Citation.*undefined" compile.log        # undefined citations → 0
```

Automated checklist:
- [ ] PDF file exists and is > 100KB (not empty/corrupt)
- [ ] Total page count is reasonable (MAX_PAGES + appendix + references)
- [ ] No "??" in the PDF (undefined references — grep the log)
- [ ] No "[?]" in the PDF (undefined citations — grep the log)
- [ ] Figures are rendered (not missing image placeholders)

**Visual review (automated):** if the compiled PDF exists, read it directly for a quick visual scan — figure readability, layout, figures near their first reference, table alignment, no content past margins. This is a quick scan, not a full review; the improvement loop does deeper visual review.

**Step 6: Page count verification (CRITICAL)**

- **ML conferences (ICLR/NeurIPS/ICML/CVPR/ACL/AAAI):** main body = first page through end of Conclusion; references and appendix NOT counted.
- **IEEE venues:** TOTAL page count including references must fit the limit.

Precise check using `pdftotext`:

```bash
pdftotext main.pdf - | python3 -c "
import sys
text = sys.stdin.read()
pages = text.split('\f')
for i, page in enumerate(pages):
    if 'Ethics Statement' in page or 'Reproducibility' in page:
        print(f'Conclusion ends on page {i+1}')
    if any(w in page for w in ['References', 'Bibliography']):
        lines = [l for l in page.split('\n') if l.strip()]
        for l in lines[:3]:
            if 'References' in l or 'Bibliography' in l:
                print(f'References start on page {i+1}')
                break
"
```

If Conclusion ends mid-page and References start on the same page, the main body is that page number (e.g. both on page 9 → main body ≈ 8.5 pages, fine for a 9-page limit). If over limit: identify the longest sections and suggest specific cuts (move proofs to appendix, compress tables, tighten writing). Report: "Main body is X pages (limit: MAX_PAGES). Suggestion: move [specific content] to appendix."

**Step 6.5: Stale file detection** — find orphaned section files not `\input`ed by `main.tex`:

```bash
for f in paper/sections/*.tex; do
    base=$(basename "$f")
    if ! grep -q "$base" paper/main.tex; then
        echo "WARNING: $f is not referenced by main.tex — consider removing"
    fi
done
```

**Step 7: Submission readiness checks** (for conference submission):

- [ ] **Anonymous**: no author names, affiliations, or self-citations that reveal identity
- [ ] **Page limit**: main body within MAX_PAGES (to end of Conclusion)
- [ ] **Font embedding**: `pdffonts main.pdf | grep -v "yes"` returns nothing
- [ ] **No supplementary mixed in**: appendix clearly after `\newpage\appendix`
- [ ] **File size**: reasonable (< 50MB for most venues, < 10MB preferred)
- [ ] **No `[VERIFY]` markers**: search the PDF text for leftovers

**Compile rules:**

- **Never delete the user's source files** — only modify to fix errors
- **Keep compile.log** — useful for debugging
- **Don't suppress warnings** — report them, let the user decide
- **If LaTeX is not installed**, provide clear installation instructions rather than failing silently
- **Font embedding is critical** — some venues reject PDFs with non-embedded fonts
- **Page count rules differ by venue** — ML: main body to Conclusion (refs excluded). IEEE: total pages including references.

**Common venue requirements:**

| Venue | Style File | Citation | Page Limit | Refs in limit? | Submission |
|-------|-----------|----------|------------|----------------|------------|
| ICLR 2026 | `iclr2026_conference.sty` | `natbib` (`\citep`/`\citet`) | 9 pages (to Conclusion end) | No | OpenReview |
| NeurIPS 2025 | `neurips_2025.sty` | `natbib` (`\citep`/`\citet`) | 9 pages (to Conclusion end) | No | OpenReview |
| ICML 2025 | `icml2025.sty` | `natbib` (`\citep`/`\citet`) | 8 pages (to Conclusion end) | No | OpenReview |
| IEEE Journal | `IEEEtran.cls` [journal] | `cite` (`\cite{}`, numeric) | ~12-14 pages (Transactions) / ~4-5 (Letters) | **Yes** | IEEE Author Portal / ScholarOne |
| IEEE Conference | `IEEEtran.cls` [conference] | `cite` (`\cite{}`, numeric) | 5-8 pages (varies by conf) | **Yes** | EDAS / IEEE Author Portal |

**Output:** `paper/main.pdf`

**Checkpoint:** Report compilation results.

```
🔨 Compilation complete:
- Status: SUCCESS
- Pages: [X] (main body) + [Y] (references) + [Z] (appendix)
- Within page limit: YES/NO
- Undefined references: 0
- Undefined citations: 0

Shall I proceed with the improvement loop?
```

### Phase 4.5: Proof Verification (theory papers only)

**Skip this phase if the paper contains no theorems, lemmas, or proofs.**

```
if paper contains \begin{theorem} or \begin{lemma} or \begin{proof}:
    Run /research-review "paper/" as a proof audit (fresh thread, maximum reasoning).
    The account-default Codex reviewer is asked to:
    - Verify all proof steps (hypothesis discharge, interchange justification, etc.)
    - Check for logic gaps, quantifier errors, missing domination conditions
    - Attempt counterexamples on key lemmas
    - Generate PROOF_AUDIT.md with issue list + severity (FATAL/CRITICAL/MAJOR/MINOR)
      and PROOF_AUDIT.json (verdict PASS/WARN/FAIL/BLOCKED/ERROR)

    If FATAL or CRITICAL issues found:
        Fix before proceeding to improvement loop
    If only MAJOR/MINOR:
        Proceed, improvement loop may address remaining issues
else:
    skip — no proofs, no action; at assurance=submission still emit
    PROOF_AUDIT.json with verdict NOT_APPLICABLE
```

### Phase 4.7: Paper Claim Audit (zero-context evidence verification)

**Skip if no result files exist (e.g., survey/position papers with no experiments).** This phase is self-contained — it can also be invoked standalone when the user asks to "审查论文数据 / check paper claims / 论文数字核对".

**Why this exists:** the executor writes experiments AND writes the paper — it "knows" what the results should be. This creates confirmation bias: rounding 84.7% up to 85.3%, reporting best seed instead of average, citing metrics from a different config, claiming "improves by 15%" when the delta is 12.8%. A **fresh reviewer with zero prior context** catches these because it has no expectations — it just compares paper text vs raw files.

**How this differs from other audits:**

| Audit | Question it answers |
|-------|-------------------|
| `/experiment-audit` | Is the experiment code honest? (fake GT, normalization fraud) |
| `/signal-analysis` | Does the data scientifically support this claim? |
| **Claim audit (this phase)** | **Does the paper report the data truthfully and precisely?** |

**Core principle — zero-context, fresh reviewer.** The auditor receives ONLY paper .tex files (the claims) and raw result files (the evidence). It does NOT receive: EXPERIMENT_LOG.md, EXPERIMENT_TRACKER.md, AUTO_REVIEW.md, NARRATIVE_REPORT.md, any executor summary or interpretation, any prior audit results, or any conversation history. This is **stricter than reviewer-independence** — it's zero-context evidence audit.

**Step 1: Collect files (executor — do NOT read or interpret them)**

Paper files (claims) — paths shown relative to the shell's working directory so you can find them with `ls`; when writing them into `audited_input_hashes`, use paths relative to the paper dir (no `paper/` prefix) per the artifact contract below:

```
paper/main.tex                # → hash key: main.tex
paper/sections/*.tex          # → hash key: sections/*.tex
paper/tables/*.tex (if separate)   # → hash key: tables/*.tex
```

Result files (evidence):

```
results/*.json, results/*.jsonl, results/*.csv, results/*.tsv
outputs/*.json, outputs/*.csv
wandb-summary.json (if exists)
**/metrics.json, **/eval_results.json
**/config.yaml, **/args.json (experiment configs)
```

Exclude (no summaries, no interpretations): EXPERIMENT_LOG.md, EXPERIMENT_TRACKER.md, AUTO_REVIEW*.md, NARRATIVE_REPORT.md, PAPER_PLAN.md, findings.md — any .md file that is an executor-written summary.

**Step 2: Fresh reviewer audit (account-default Codex — NEW thread, no reply)**

**CRITICAL: Use `mcp__codex__codex` (new thread), NEVER `mcp__codex__codex-reply`.** Every run must be a fresh context.

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a paper-to-evidence auditor. You have ZERO prior context about
    this research. You will receive only paper source files and raw result
    files. Your job is to verify that every number in the paper exactly
    matches the raw evidence.

    Paper files to read:
    [list .tex file paths]

    Result files to read:
    [list .json/.csv/.yaml file paths]

    ## Audit Protocol

    ### A. Extract Every Quantitative Claim
    For each number, percentage, comparison, or scope statement in the paper:
    - Location (section, table, caption, or inline text)
    - Exact claim text
    - The number or comparison being made

    ### B. Trace Each Claim to Evidence
    For each extracted claim, find the supporting raw data:
    - Which result file contains this number?
    - What is the EXACT value in that file?
    - Match status: exact_match / rounding_ok / mismatch

    ### C. Check These Specific Failure Modes

    1. **Number inflation**: Paper says 85.3%, raw file says 84.7%
       Rule: only standard rounding to displayed precision is allowed

    2. **Best-seed cherry-pick**: Paper says "achieves 90.2%" but
       that's the best of 5 seeds; mean is 87.1%
       Rule: check if paper specifies "average" / "best" / "median"

    3. **Config mismatch**: Paper compares Method A vs Baseline B,
       but they used different hyperparameters / datasets / splits
       Rule: verify config files show same settings for compared methods

    4. **Aggregation mismatch**: Paper says "average over 5 seeds"
       but result files show only 3 runs
       Rule: count actual runs vs claimed count

    5. **Delta error**: Paper says "improves by 15%" but
       actual delta is (85.3 - 73.1) / 73.1 = 16.7%
       Rule: verify arithmetic of all relative improvements

    6. **Caption-table mismatch**: Figure caption describes
       something different from what the figure/table actually shows
       Rule: cross-check every caption against its content

    7. **Scope overclaim**: Paper says "consistently outperforms"
       but only tested on 2 datasets
       Rule: check if language matches actual evaluation scope

    8. **Semantic scope promotion**: The paper preserves the number but
       silently upgrades what the experiment means. Check especially for:
       - induced or adversarial cases described as naturally prevalent;
       - existence of a mechanism described as its frequency or dominance;
       - one model, dataset, cell, or same-dataset scale probe described as
         cross-setting generality;
       - oracle, probe, separability, or diagnostic success described as a
         deployable method result;
       - abstention, filtering, certification, or refusal described as task
         performance improvement;
       - a substantive negative result hidden only in limitations while the
         abstract, introduction, or results retain the broader positive claim.
       Rule: verify the claim's scientific meaning and qualifiers against the
       exact intervention, population, setting, and evaluation represented by
       the raw evidence.

    ## Output Format (per claim)
    For each claim, report:
    - claim_id: sequential number
    - location: section/table/figure
    - paper_text: exact quote from paper
    - paper_value: the number claimed
    - evidence_file: which raw file
    - evidence_value: the actual number
    - status: exact_match | rounding_ok | ambiguous_mapping |
              missing_evidence | config_mismatch | aggregation_mismatch |
              number_mismatch | scope_overclaim | scope_promotion |
              unsupported_claim
    - details: explanation if not exact_match

    Overall verdict: PASS | WARN | FAIL
```

**Step 3: Write report (executor)**

Parse the reviewer's response and write `PAPER_CLAIM_AUDIT.md`:

```markdown
# Paper Claim Audit Report

**Date**: [today]
**Auditor**: Codex account-default, maximum available reasoning (fresh zero-context thread)
**Paper**: [paper title from tex]

## Overall Verdict: [PASS | WARN | FAIL]

## Claims Verified: [N total]
- exact_match: [count]
- rounding_ok: [count]
- ambiguous_mapping: [count]
- missing_evidence: [count]
- mismatch: [count]

## Issues Found

### [FAIL/WARN] Claim #N: [description]
- **Location**: Section X / Table Y / Figure Z
- **Paper says**: "..."
- **Evidence shows**: ...
- **Status**: [status]
- **Fix**: [specific correction needed]

## All Claims (detailed)

| # | Location | Paper Value | Evidence Value | Status |
|---|----------|-------------|---------------|--------|
| 1 | Table 2 | 85.3% | 85.28% | rounding_ok |
| 2 | Abstract | "15% improvement" | 12.8% | number_mismatch |
| ... |
```

Also write `PAPER_CLAIM_AUDIT.json` for machine consumption (contract below).

**Step 4: Print summary**

```
📋 Paper Claim Audit Complete

  Claims verified: 24
  exact_match:     18
  rounding_ok:      3
  ambiguous:         1
  ⚠️ mismatch:      2

  Overall: ⚠️ WARN

  See PAPER_CLAIM_AUDIT.md for details.
```

**Verdict handling (advisory in `draft` mode, gated in `submission` mode):**

- `PASS` → continue normally
- `WARN` → print warning, continue, flag draft as "check numbers before submission"
- `FAIL` → fix mismatched numbers before the improvement loop; do NOT mark as submission-ready

The improvement loop (`/auto-paper-improvement-loop`) reads `PAPER_CLAIM_AUDIT.json` when it exists and fixes mismatched claims as priority items.

**Claim-audit rules:**

- **Fresh thread EVERY run.** Never use `codex-reply`. Never carry context.
- **Zero executor interpretation.** Only file paths. No summaries.
- **Only raw results.** No EXPERIMENT_LOG, no AUTO_REVIEW, no human summaries.
- **Rounding rule.** Only standard rounding to displayed precision. 84.7% → 84.7% or 85% is OK. 84.7% → 85.3% is NOT OK.
- **Audit meaning, not only arithmetic.** A numerically exact statement still fails when it promotes induced evidence to natural prevalence, a diagnostic to a method, a single cell to generality, or abstention to performance.
- **Qualifiers are evidence-bearing.** Words such as natural, general, robust, deployable, causal, consistent, and solved require their own traceable support; removing a qualifier can change the claim even when every number remains unchanged.
- **Cross-model.** Reviewer must be a different model family from executor.

**Submission artifact emission.** This phase **always** writes `paper/PAPER_CLAIM_AUDIT.json` when it runs as a submission gate, regardless of detector outcome. A detector-negative run (paper has no numeric claims) emits verdict `NOT_APPLICABLE`; a paper-with-numeric-claims-but-no-raw-results run emits `BLOCKED`. Silent skip is forbidden at `assurance=submission` because Phase 6 relies on this artifact existing at a predictable path.

The artifact conforms to the schema in `shared-references/assurance-contract.md` (`audit_skill` stays the stable identifier `"paper-claim-audit"` for verifier compatibility):

```json
{
  "audit_skill":      "paper-claim-audit",
  "verdict":          "PASS | WARN | FAIL | NOT_APPLICABLE | BLOCKED | ERROR",
  "reason_code":      "all_numbers_match | rounding_drift | missing_raw_results | ...",
  "summary":          "One-line human-readable verdict summary.",
  "audited_input_hashes": {
    "main.tex":                              "sha256:...",
    "sections/5.evidence.tex":               "sha256:...",
    "/abs/path/to/results/run_2026_04_19.json": "sha256:..."
  },
  "trace_path":       ".research-skills/traces/paper-claim-audit/<date>_run<NN>/",
  "thread_id":        "<codex mcp thread id>",
  "reviewer_model":   "account-default",
  "reviewer_reasoning": "xhigh",
  "generated_at":     "<UTC ISO-8601>",
  "details": {
    "total_claims":   <int>,
    "mismatches":     [ ... per-claim issue records ... ],
    "result_files":   [ ... raw files consulted ... ]
  }
}
```

**`audited_input_hashes` scope:** hash the **declared input set** passed into this audit invocation — the exact `.tex` files and raw result / config files this run read — not a repo-wide union and not the reviewer's self-reported subset. The external verifier rehashes these entries; any mismatch flags `STALE`.

**Path convention:** keys are **paths relative to the paper directory** for in-paper files — so
`main.tex`, not `paper/main.tex` — and **absolute paths** for out-of-paper files such as
external `results/` directories. This makes deterministic re-hashing possible.

**Verdict decision table:**

| Input state                                           | Verdict          | `reason_code` example |
|-------------------------------------------------------|------------------|-----------------------|
| No numeric claims detected in paper                   | `NOT_APPLICABLE` | `no_numeric_claims`   |
| Numeric claims detected, no raw result files found    | `BLOCKED`        | `no_raw_evidence`     |
| All claims reconcile to raw data                      | `PASS`           | `all_numbers_match`   |
| Minor rounding drift only, no material mismatch       | `WARN`           | `rounding_drift`      |
| Any material mismatch (wrong number, config mismatch) | `FAIL`           | `claim_mismatch`      |
| Reviewer invocation failed (network / malformed)      | `ERROR`          | `reviewer_error`      |

**Thread independence.** Every invocation uses a fresh `mcp__codex__codex` thread. Never `codex-reply`. Do not accept prior audit outputs (PROOF_AUDIT, CITATION_AUDIT, EXPERIMENT_LOG, AUTO_REVIEW summaries) as input to this audit — the fresh thread preserves reviewer independence per `shared-references/reviewer-independence.md`.

**Human-readable sibling.** `paper/PAPER_CLAIM_AUDIT.md` is written alongside the JSON for
readers. The JSON is authoritative for Phase 6 verification; the Markdown is for humans. The
audit emits evidence, while the submission gate decides whether it blocks finalization.

### Phase 5: Auto Improvement Loop

Invoke `/auto-paper-improvement-loop` to polish the paper:

```
/auto-paper-improvement-loop "paper/"
```

If `--style-ref: <source>` was passed in `$ARGUMENTS` and the helper succeeded above, append `--style-ref: <source>` to the invocation: `/auto-paper-improvement-loop "paper/ --style-ref: <source>"`. The improvement loop's reviewer sub-agent will still NOT see the style ref (the loop's own SKILL forbids it); only the fix-implementation phase consumes it.

**What this does (2 rounds):**

**Round 1:** account-default Codex reviews the full paper → identifies CRITICAL/MAJOR/MINOR issues → Claude Code implements fixes → recompile → save `main_round1.pdf`

**Round 2:** a fresh account-default Codex thread re-reviews independently → identifies remaining issues → Claude Code implements fixes → recompile → save `main_round2.pdf`

**Typical improvements:**
- Fix assumption-model mismatches
- Soften overclaims to match evidence
- Add missing interpretations and notation
- Strengthen limitations section
- Add theory-aligned experiments if needed

**Output:** Three PDFs for comparison + `PAPER_IMPROVEMENT_LOG.md`.

**Format check** (included in improvement loop Step 8): After final recompilation, auto-detect and fix overfull hboxes (content exceeding margins), verify page count vs venue limit, and ensure compact formatting. Location-aware thresholds: any main-body overfull blocks completion regardless of size; appendix overfulls block only if >10pt; bibliography overfulls block only if >20pt.

### Phase 5.5: Final Paper Claim Audit (MANDATORY submission gate)

After `/auto-paper-improvement-loop` finishes, **rerun** the claim audit procedure (Phase 4.7) before the final report whenever the paper contains numeric claims and machine-readable raw result files exist.

Use the same detectors as Phase 4.7:
- numeric-claim regex over `paper/main.tex` and `paper/sections/*.tex`
- raw-evidence file search in `results/`, `outputs/`, `experiments/`, and `figures/` for `.json`, `.jsonl`, `.csv`, `.tsv`, `.yaml`, or `.yml`

This phase is **mandatory** if both detectors are positive. It blocks the final report.
If numeric claims exist but no raw result files are found, stop and warn the user before declaring the paper complete.
If no numeric claims exist, skip.

```bash
NUMERIC_CLAIMS=$(rg -n -e '[0-9]+(\.[0-9]+)?\s*(%|\\%|±|\\pm|x|×)' \
  -e '(accuracy|BLEU|F1|AUC|mAP|top-1|top-5|error|loss|perplexity|speedup|improvement)' \
  paper/main.tex paper/sections 2>/dev/null || true)

RAW_RESULT_FILES=$(find results outputs experiments figures -type f \
  \( -name '*.json' -o -name '*.jsonl' -o -name '*.csv' -o -name '*.tsv' -o -name '*.yaml' -o -name '*.yml' \) 2>/dev/null | head -200)

if [ -n "$NUMERIC_CLAIMS" ] && [ -n "$RAW_RESULT_FILES" ]; then
    Run the claim audit (Phase 4.7 procedure, fresh thread)
    If FAIL:
        Fix mismatched numbers before the final report
elif [ -n "$NUMERIC_CLAIMS" ]; then
    Stop and warn: the paper contains numeric claims but no raw evidence files were found
fi
```

**Empirical motivation:** in a real submission run, the final paper claimed a narrower experiment grid than the raw JSON actually contained, and a tolerance value was rounded down past the actual relative error. Both were caught only after a manual claim-audit run in the final round; the improvement loop did not detect them.

### Phase 5.8: Citation Audit (submission gate)

After the final claim audit passes, run `/citation-audit` to verify every `\cite{...}` along three axes: existence, metadata correctness, and context appropriateness. This is the fourth and final layer of the evidence-and-claim assurance stack (`experiment-audit` → `signal-analysis` → claim audit → `citation-audit`).

```
if paper/references.bib (or paper.bib) exists and contains entries cited from sec/*.tex:
    Run /citation-audit "paper/"
    Fresh cross-family account-default reviewer via Codex MCP with web/DBLP/arXiv lookup
    verifies each entry:
      (i)   EXISTENCE — paper resolves at claimed arXiv ID / DOI / venue
      (ii)  METADATA — author names, year, venue, title match canonical sources
      (iii) CONTEXT — cited paper actually establishes the claim it supports

    Output:
      - CITATION_AUDIT.md (human-readable per-entry verdict report)
      - CITATION_AUDIT.json (machine-readable verdict ledger)
      - Per-entry verdicts: KEEP / FIX / REPLACE / REMOVE

    If any REPLACE or REMOVE verdicts:
        Surface to user for human approval — never auto-modify content claims
    If only FIX verdicts (metadata corrections):
        Apply with user confirmation, then recompile
    If all KEEP:
        Pass — bibliography clean for submission
else:
    skip — no bib file or no citations
```

**Why this is the most diagnostic of the four audit layers:** wildly fake citations are easy to spot. The dangerous failure mode is a real paper used to support a claim it does not actually establish (wrong-context citations) — these slip past metadata-only checks and damage submission credibility. Run cost is wall-clock heavy (web lookup per entry); run once per submission, not per save.

**Empirical motivation:** in a real submission run, several real papers were cited in contexts they did not actually support, and at least one bib entry shipped with `author = "Anonymous"` because the metadata had not been resolved. None were caught by the improvement loop or numeric claim audit; only fresh web-lookup review surfaced them.

### Phase 6: Final Report

**Phase 6.0 — Submission Gate**

Before writing the Final Report, resolve the active assurance level. This
uses the **same derivation rule as Phase 0** so a run where Phase 0 was
skipped or its write failed cannot silently downgrade a `beast` / `max` /
`--assurance: submission` invocation back to draft.

**Resolution at the gate** (re-derive; do not trust `.research-skills/assurance.txt`
alone):

1. Parse `$ARGUMENTS` for an explicit `--assurance: draft | submission` or
   an `--effort: lite | balanced | max | beast` directive.
2. Derive the expected level:
   - explicit `assurance:` wins
   - else `lite` / `balanced` → `draft`, `max` / `beast` → `submission`
   - else `draft`
3. Read `paper/.research-skills/assurance.txt`. If the file is missing, write it now
   with the derived level.
4. If the file's value **disagrees** with the derived level (e.g. file
   says `draft` but `$ARGUMENTS` says `beast`), **overwrite** the file
   with the derived level and surface a one-line warning in-chat:
   `assurance.txt was draft but the current invocation says submission; overriding.`
5. Use the re-derived level as authoritative for the rest of Phase 6.

```bash
# Final authoritative value, written and read from the same source
ASSURANCE=<derived-from-$ARGUMENTS>        # draft | submission
mkdir -p paper/.research-skills
echo "$ASSURANCE" > paper/.research-skills/assurance.txt
```

If `ASSURANCE=draft`, skip directly to the Final Report template below —
**current behavior, no change** for the default `balanced` user.

If `ASSURANCE=submission`, run the pre-flight checklist below. Do not
self-declare "audits complete" from conversation memory.

#### Submission pre-flight checklist

Print this checklist verbatim at the start of Phase 6.0 and confirm each row
before proceeding. This resists the common failure mode of the model
skipping audits while claiming to have run them.

```
📋 Submission audits required before Final Report:
   [ ] 1. /research-review (proof audit) → paper/PROOF_AUDIT.json
   [ ] 2. claim audit (Phase 4.7)  → paper/PAPER_CLAIM_AUDIT.json
   [ ] 3. /citation-audit       → paper/CITATION_AUDIT.json
   [ ] 4. Re-hash every declared audit input and compare it with audited_input_hashes
   [ ] 5. Validate each audit JSON and block on missing, stale, malformed, FAIL, BLOCKED, or ERROR
```

#### Invoking the three audits

Each sub-audit runs in a **fresh Codex thread** (never `codex-reply`,
never pass prior audit output as context — this preserves reviewer
independence per `shared-references/reviewer-independence.md`).

Each sub-audit **always** emits its JSON artifact, even when the content
detector is negative. A detector-negative run emits verdict
`NOT_APPLICABLE`; a silent skip is forbidden. See the "Submission artifact
emission" section of each audit's SKILL.md.

Order:

1. `/research-review "paper/"` (proof audit, fresh thread) → writes
   `paper/PROOF_AUDIT.json` (emits `NOT_APPLICABLE` if the paper contains no
   theorems / lemmas / proofs)
2. claim audit (Phase 4.7 procedure, fresh thread) → writes
   `paper/PAPER_CLAIM_AUDIT.json` (emits `NOT_APPLICABLE` if the paper has no
   numeric claims; emits `BLOCKED` if numeric claims exist but raw result
   files are missing)
3. `/citation-audit "paper/"` → writes `paper/CITATION_AUDIT.json`
   (emits `NOT_APPLICABLE` if no `.bib` file or no `\cite{...}` usage)

#### Verifying audit artifacts

The release is self-contained and does not assume an unpublished verifier script. Validate the
three JSON artifacts directly:

1. each required artifact exists and parses as JSON;
2. its verdict is not `FAIL`, `BLOCKED`, or `ERROR`;
3. every path in `audited_input_hashes` still exists and its current hash matches;
4. the artifact names the expected audit skill and assurance level;
5. any `NOT_APPLICABLE` verdict includes a concrete detector reason.

Write the combined result to
`paper/.research-skills/audit-verifier-report.json`. Use status `OK`, `MISSING`,
`STALE`, `BLOCKING_VERDICT`, or `SCHEMA_INVALID` for each audit. A local repository may provide
an optional deterministic verifier that implements the same contract, but the workflow must
remain understandable and executable without private tooling.

---

**Phase 6.1 — Final Report** (runs only after the submission gate is green,
or directly if `assurance=draft`)

```markdown
# Paper Writing Pipeline Report

**Input**: [NARRATIVE_REPORT.md or topic]
**Venue**: [ICLR/NeurIPS/ICML/CVPR/ACL/AAAI/ACM/IEEE_JOURNAL/IEEE_CONF]
**Assurance**: [draft | submission]
**Submission-ready**: [yes | no]   <!-- yes iff entry=PASS, assurance=submission, verifier exit 0, and user approved -->
**Date**: [today]

## Pipeline Summary

| Phase | Status | Output |
|-------|--------|--------|
| 0. Assurance Setup | ✅ | paper/.research-skills/assurance.txt = [draft\|submission] |
| 0.5 Paper Entry | PASS | PAPER_ENTRY.md ([fingerprint]) |
| 1. Paper Plan | ✅ | PAPER_PLAN.md |
| 2. Figures | ✅ | figures/ ([N] auto + [M] manual) |
| 3. LaTeX Writing | ✅ | paper/sections/*.tex ([N] sections, [M] citations) |
| 4. Compilation | ✅ | paper/main.pdf ([X] pages) |
| 5. Improvement | ✅ | [score0]/10 → [score2]/10 |
| 4.5 Proof Audit | [PASS\|WARN\|FAIL\|NOT_APPLICABLE\|BLOCKED\|ERROR] | PROOF_AUDIT.{md,json} |
| 5.5 Paper Claim Audit | [PASS\|WARN\|FAIL\|NOT_APPLICABLE\|BLOCKED\|ERROR] | PAPER_CLAIM_AUDIT.{md,json} |
| 5.8 Citation Audit | [PASS\|WARN\|FAIL\|NOT_APPLICABLE\|BLOCKED\|ERROR] | CITATION_AUDIT.{md,json} |
| 6.0 Assurance Verifier | [OK\|STALE\|BLOCKING_VERDICT\|HAS_ISSUES\|SCHEMA_INVALID\|MISSING] per audit (N/A if draft) | .research-skills/audit-verifier-report.json |

## Improvement Scores
| Round | Score | Key Changes |
|-------|-------|-------------|
| Round 0 | X/10 | Baseline |
| Round 1 | Y/10 | [summary] |
| Round 2 | Z/10 | [summary] |

## Deliverables
- PAPER_ENTRY.md — Independent Prize/Fidelity/Entry verdict for this fingerprint
- paper/main.pdf — Final polished paper
- paper/main_round0_original.pdf — Before improvement
- paper/main_round1.pdf — After round 1
- paper/main_round2.pdf — After round 2
- paper/PAPER_IMPROVEMENT_LOG.md — Full review log
- paper/PROOF_AUDIT.{md,json} — Proof-obligation verification (always emitted at `assurance=submission`; `NOT_APPLICABLE` when no theorems)
- paper/PAPER_CLAIM_AUDIT.{md,json} — Numerical claim verification (always emitted at `assurance=submission`; `NOT_APPLICABLE` when no numeric claims; omitted in `draft` mode if Phase 5.5 detector was negative)
- paper/CITATION_AUDIT.{md,json} — Bibliography verification (always emitted at `assurance=submission`; `NOT_APPLICABLE` when no `.bib` or no `\cite{...}`; omitted in `draft` mode if Phase 5.8 detector was negative)
- paper/.research-skills/audit-verifier-report.json — Combined audit verification report (submission only)

## Remaining Issues (if any)
- [items from final review that weren't addressed]

## Next Steps
- [ ] Visual inspection of PDF
- [ ] Add any missing manual figures
- [ ] Submit to [venue] via OpenReview / CMT / HotCRP
```

## Output Protocols

> Follow these shared protocols for all output files:
> - **[Output Manifest Protocol](../shared-references/output-manifest.md)** — log every output to MANIFEST.md

## Key Rules

- **Paper entry precedes full writing.** Complete planning, LaTeX expansion, figure
  production, and polish require a current `PAPER_ENTRY.md` with `entry: PASS`.
  A stale identity fingerprint or active circuit breaker returns the manuscript to
  `ENTRY HOLD`.
- **Large file handling**: If the current editing tool cannot write a large artifact, split the artifact into smaller planned files or use the approved editing mechanism for the current environment. Do not bypass active tool or permission rules.
- **Current evidence bounds prose.** Do not make the title, abstract, contribution list, or venue-readiness statement stronger than the latest validated evidence and live research state. `RESULT_TO_CLAIM.md` is a revisable interpretation, not authority over future research.
- **The paper cannot borrow the seed's prize.** Preserve an explicit original-program/current-paper distinction, disclose material scope debt, and make the paper-to-seed bridge or independent consequence visible in the title-level argument.
- **Prose structure discipline is binding.** Avoid excessive bold, excessive `itemize`, one-or-two-sentence paragraph fragmentation, and tiny subsections/subsubsections. Use cohesive paragraphs and headings only for real conceptual units.
- **No strawman writing.** Related work, limitations, rebuttal-style paragraphs, and baseline discussion must steelman the strongest competing claim before differentiating. Do not argue against a weaker invented version of an incumbent, reviewer concern, or failed result.
- **Use reference papers through isolated subagents.** Full PDFs and detailed per-paper notes stay out of the main thread. The main writer consumes `writing_models/SYNTHESIS.md`, checks targeted passages only when needed, and remains responsible for evidence and scientific judgment.
- **One spine, not a lab notebook.** Remove branches, probes, and historical details that do not support the bounded contribution. Do not let the most recent result automatically become the paper's center.
- **Every sentence class has an evidence burden.** Audit induced versus natural, existence versus prevalence, cell-specific versus general, and diagnostic versus value claims wherever they appear, including captions and conclusion.
- **No submission-ready label without user approval.** Even when `PAPER_ENTRY.md`
  remains `PASS`, `RESULT_TO_CLAIM.md` supports the intended contribution and all
  audit artifacts verify cleanly, present the audit summary (entry fingerprint,
  claim alignment, and page limit) before writing `submission-ready: yes`. The
  human confirms that the evidence supports submission, not merely that automated
  checks are green.
- **Resolve LLM disclosure at submission.** Before labelling a top-tier submission `submission-ready`, resolve the venue's LLM-use policy and ask the user how to disclose LLM-assisted content for this paper. Do not auto-insert or auto-omit a disclosure.
- **Don't skip phases.** Each phase builds on the previous one — skipping leads to errors.
- **Checkpoint between phases** when AUTO_PROCEED=false. Present results and wait for approval.
- **Manual figures first.** If the paper needs architecture diagrams or qualitative results, the user must provide them before Phase 3.
- **Compilation must succeed** before entering the improvement loop. Fix all errors first.
- **Preserve all PDFs.** The user needs round0/round1/round2 for comparison.
- **Document everything.** The pipeline report should be self-contained.
- **Respect page limits.** If the paper exceeds the venue limit, suggest specific cuts before the improvement loop.

## Composing with Other Workflows

```
/frontier-direction-discovery "direction"   ← Workflow 1: find directions
implement                           ← write code
/run-experiment                     ← deploy experiments
/research-review "paper topic"      ← Workflow 2: iterate research (Looped Mode)
/paper-writing "NARRATIVE_REPORT.md"  ← Workflow 3: you are here
                                         submit! 🎉

Or use /research-pipeline for the Workflow 1+2 end-to-end flow,
then /paper-writing for the final writing step.
```

## Typical Timeline

| Phase | Duration | Can sleep? |
|-------|----------|------------|
| 1. Paper Plan | 5-10 min | No |
| 2. Figures | 5-15 min | No |
| 3. LaTeX Writing | 15-30 min | Yes ✅ |
| 4. Compilation | 2-5 min | No |
| 5. Improvement | 15-30 min | Yes ✅ |

**Draft end-to-end: ~45-90 min** for the mechanical assembly from a narrative report to a compiling PDF (Phases 1-5 above). This estimate covers assembly only.

**Submission-ready duration is evidence-dependent and not promised as a fixed total.** A `submission-ready: yes` label additionally requires the submission audit, all four audit layers (`experiment-audit` → `signal-analysis` → claim audit → `citation-audit`) green at `assurance=submission`, and user approval for readiness and disclosure. How long that takes scales with how many findings require fixes and recompiles. Draft assembly is mechanical; submission readiness is evidence-dependent.
