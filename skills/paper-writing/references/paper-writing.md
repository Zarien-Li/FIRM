# Paper Writing

Write the strongest honest paper supported by the project for a human audience. The
same lead PI owns the argument, manuscript-revealed scientific repairs, and final
assembly; specialized references provide mechanics without becoming separate owners.

## Modes And Specialized References

- `plan`: form `AUTHOR_ARGUMENT.md`, contribution identity, narrative architecture,
  and figure jobs.
- `write`: draft or revise sections from the author argument and raw evidence.
- `research-draft`: use an early problem story to clarify research without implying
  submission maturity.
- `full`: carry one bounded paper through drafting, scientific repair, verification,
  and assembly until only a user-owned sign-off or external action remains.
- `figures`: read [figures.md](figures.md).
- `compile`: read [write-compile.md](write-compile.md).
- `claim-audit`: read [claim-audit.md](claim-audit.md).
- `improvement`: read
  [auto-paper-improvement-loop.md](auto-paper-improvement-loop.md).
- `submission`: read [submission.md](submission.md).
- `resubmit`: read [resubmit-pipeline.md](resubmit-pipeline.md).

Load only the reference required by the current mode. Do not recursively invoke this
skill merely to change modes.

## Establish The Writing Boundary

Read the authoritative research state, original program, raw decisive results, method
specification, strongest fair comparisons, relevant audits, venue rules, and current
manuscript. Treat drafts and prior reviews as claims to verify.

Focused paper work requires an artifact-grounded method candidate or an independently
valuable and confirmed non-method object. The paper portion of `PROJECT_STATE.md`
should state, in ordinary prose, the natural problem, positive object, contribution
type, accepted population and evaluator, decisive published-method comparisons,
meaningful primary or Pareto advantage, required utility/cost checks, contrary evidence,
scope debt, and the bridge back to the original program. Counts of experiments, audits,
pages, or PDFs are not evidence of maturity.

Judge comparisons by what systems actually do, not by names used in the draft. Include
the strongest functional alternative and mechanistic rival required by the claim. A
design-guaranteed retention property is not itself empirical utility; report value on
the affected and end-to-end populations, coverage, and total cost where relevant.

Early planning and a `research-draft` may clarify the reader, prior belief, surprise,
stakes, and missing evidence. They do not establish submission readiness. Likewise,
failed methods do not automatically create an analysis paper: a changed contribution
type needs its own important object, consequence, evidence, audience, and literature
position.

If evaluator, population, provenance, or contribution identity materially changes,
revisit every dependent claim and comparison. Preserve valid prose and artifacts, but
do not transfer maturity from the old object. Ask the user only when an explicit
project, venue, deliverable, or other user-owned boundary changes.

## Establish The Author Argument Before The Outline

Before outlining sections, write a one-page `AUTHOR_ARGUMENT.md` in continuous prose.
It answers:

- who the intended human reader is;
- what that reader currently believes or takes for granted;
- which observed fact changes that belief;
- why the change matters scientifically or practically;
- what the reader should understand, do, or investigate differently after reading.

Do not use tables, inventories, contribution bullets, reviewer objections, or non-claim
lists. This is an authorial explanation, not an evidence ledger. It should sound
natural aloud and make the paper's intellectual movement clear without section labels.

Trace seed-to-paper ancestry separately:

`original program -> natural problem -> explanation -> positive object -> accepted task
or natural system -> bounded paper`

The current object must matter at its supported specificity rather than borrowing
importance from a broad field name or prestigious benchmark.

## Let A Dedicated Author Learn Directly From Excellent Papers

For high-stakes writing, select two to four genuinely strong, venue-relevant papers
from primary sources. Prefer respected venues or field-defining outlets, a closely
matched contribution type, evidence of real influence or recognition, and reliable
full text.

Assign each exemplar a distinct rhetorical role, such as Introduction, Results,
Method, or Discussion. Record why it was selected and which writing decision it should
inform. Do not average papers into a universal template.

Use one fresh author subagent for a coherent section or draft. Give it the complete
role-relevant exemplars, `AUTHOR_ARGUMENT.md`, the contribution and decisive raw
evidence, venue and audience, and any draft being revised. The subagent reads the
papers in full and writes directly, adapting rhetorical choices, paragraph movement,
evidence timing, field-natural language, and specificity without copying wording or
claims. It may depart from every exemplar.

The lead PI checks the result against evidence and the author argument; it does not
regenerate the section from a compact synthesis. Keep exemplar material author-side
and out of factual audits.

## Plan Around One Contribution Identity

One identity means one governing scientific principle, not one contribution bullet.
When earned, a connected stack may include a recurring phenomenon, replacement
principle or reusable primitive, executable realization, predicted generalization or
mechanism finding, and reusable data or system machinery. Use only supported,
connected layers. Do not force a quota, promote ablations, combine unrelated projects,
or hide an earned program behind one benchmark delta.

Write `PAPER_PLAN.md` with:

- literal problem, stakes, prior belief, and changed understanding;
- default assumption, one-sentence replacement principle, and positive object;
- connected contribution layers and evidence for each;
- strongest honest claim, decisive comparison, and primary value metric;
- paper-to-program bridge;
- section-level narrative movement;
- each figure or table's rhetorical job;
- tradeoffs or limitations that materially change interpretation.

Organize evidence by scientific questions, not run chronology. Every section and
figure should establish the problem, explain the design, test a prediction, measure
value/cost, or bound the claim. Make clear why future work on the problem would need to
engage with the phenomenon, principle, primitive, or resource; that is the citation
surface, not a promotional slogan.

## Draft For A Human Reader

Write a provisional Introduction early enough that the research question, prior
belief, and surprise guide presentation choices. Rewrite it after the central result
and contribution stabilize. Draft method, results, setup, figures, and tables from raw
evidence; write the abstract and title last.

Prefer cohesive paragraphs and fewer meaningful sections over checklist prose. Use
related work where it sharpens the reader's model rather than staging a pre-emptive
exchange with reviewers. Place a caveat beside a result only when it changes that
result's interpretation; put other genuine boundaries in a concise Limitations
section. Internal scope notes and rejected claims are not manuscript prose.

Preserve this paper's particular argument instead of filling fixed rhetorical slots.
Calibrate causal, mechanism, generality, robustness, deployment, and SOTA language
against the post-draft evidence check.

## Verify After The Narrative Exists

Create `CLAIMS_EVIDENCE.md` only after a substantive narrative draft. For each
consequential title phrase, abstract sentence, contribution, principal visual, and
conclusion claim, record its location, raw evidence, scope, required qualification,
and status. Distinguish observation from explanation, association from cause,
discovery from confirmation, and diagnostic from deployed method evidence.

Use the map to repair unsupported prose, never to generate section order, paragraph
order, or transitions. Detailed reconstruction belongs to
[claim-audit.md](claim-audit.md). Experiment/evaluator validity, citation support,
project-state judgment, and proofs belong to `research-review`; manuscript numbers and
qualifiers belong here; scientific importance and memorability remain the lead PI's
and human reader's responsibility. Reuse checks whose inputs and semantics are
unchanged.

Use [figures.md](figures.md) for reproducible visuals and
[write-compile.md](write-compile.md) for LaTeX production and rendered-PDF inspection.

## Stabilize And Finish

Treat the first coherent draft as an integration test. If it exposes an invalid
evaluator, missing claim-bearing result, unresolved decisive rival, method defect, or
material utility/cost gap, return that exact issue to its research owner, resolve it,
and revise. Do not open work for optional breadth or speculative reviewer preferences.

After contribution identity and evidence stabilize, use
[auto-paper-improvement-loop.md](auto-paper-improvement-loop.md) for human-reader
editing. Finish with [submission.md](submission.md). Completion means a coherent,
verified, venue-compliant package awaiting only final human factual, authorship, legal,
or upload approval, not merely a full draft or compiled PDF.
