# Research Control Protocol

Use this protocol when maintaining a long research program, setting a Claude Code
`/goal`, changing contribution identity, or deciding whether complete paper writing
may begin. It protects scientific continuity without protecting a failed paper.

## 1. Separate Authority From Evidence

Only explicit user instructions, safety rules, and live operational constraints can
create binding limits. Scientific claims are controlled by validated raw evidence.
Agent interpretations, Codex reviews, registrations, drafts, memories, and compacted
summaries preserve reasoning and provenance; they cannot silently become user
constraints.

Tag consequential live-state statements:

- `[USER]` explicit scope, resource, venue, deliverable, or irreversible boundary;
- `[EVIDENCE]` validated observation with a durable raw-artifact path;
- `[INTERPRETATION]` current causal or scientific reading;
- `[REVIEW]` Codex or other reviewer advice;
- `[HISTORY]` superseded framing retained only for provenance.

Any use of `binding`, `locked`, `forbidden`, `no re-entry`, or an equivalent phrase
must cite the explicit user instruction or external rule that created it. Otherwise
rewrite it as an interpretation or remove it from the live state. A reviewer can
block a paper-entry decision; it cannot close a method family, seed, or field.

## 2. Use Bounded Goals

Keep the durable research-program objective in project state. Do not use an
open-ended `/goal` whose completion condition is “obtain a spotlight method,”
“finish the paper,” or “keep researching until success.” A stop hook cannot judge
scientific maturity and will reward narrative motion.

A session goal should cover one evidence-bearing research cycle:

`interpret -> construct or repair -> run/read a representative test -> update state`

It may complete with a positive result, an honest directional loss and diagnosed
redesign, or a paper-identity reset. It may not complete merely because prose,
reports, more seeds, or a new claim were produced. The broad program remains active
after the bounded goal completes.

## 3. Keep Program And Paper Identity Separate

Maintain:

- the original research program and value target;
- one current paper candidate, which may also be `none`.

Keep a scope-movement record whenever the task, benchmark, system, population,
metric, or abstraction changes. State who introduced the change, why the resulting
object matters independently, what bridge evidence connects it to a shared natural
class, and which standard-task or system test reintegrates it with the original
program. A narrower explanation is not automatically a more mature paper.

Do not choose a dataset, operator, architecture, threshold band, or synthetic regime
because the current method has headroom or cleaner identification there. Such a
setting may be a diagnostic microscope, but it cannot become the contribution
substrate until its importance is established independently.

Fingerprint the current paper candidate by problem class, contribution type,
positive object, load-bearing method or scientific primitive, claimed population or
standard task, primary metric, and decisive baseline. Changing the contribution
type, positive object, primitive, primary metric, or claimed population is a new
paper identity. A major change to the standard task or decisive baseline normally is
as well.

When identity changes:

1. finish already-running atomic work;
2. freeze the old manuscript as historical evidence;
3. set the new candidate maturity to `candidate`;
4. reassess prize, fidelity, scope debt, and seed-to-paper reintegration;
5. continue from a concise state, preferably in a fresh session.

The new identity inherits raw evidence and lessons, not maturity, submission
readiness, title, or a promise that a paper exists.

## 4. Distinguish Design From Statistical Uncertainty

Use one healthy paired development seed to learn the direction of a new realization.

- A clear meaningful loss to the decisive baseline is design evidence. Diagnose or
  redesign before allocating repetitions.
- A positive result or a result genuinely near the stochastic resolution boundary
  may justify claim-level repetitions.
- A failed or non-converged seed remains part of reliability evidence. Repair the
  trainer or report the failure rate; do not discard it post hoc as an outlier.
- More seeds estimate uncertainty around a stable method. They do not search for a
  favorable run or rescue a negative mean.

## 5. Require Independent Paper Entry

Complete manuscript planning and LaTeX writing require `PAPER_ENTRY.md` with
`entry: PASS`. Before PASS, maintain research notes or a compact
`CANDIDATE_CLAIM.md`, not a polished submission manuscript.

Build `PAPER_ENTRY.md` from raw artifacts, not from the current draft. It records:

- original program, current paper fingerprint, and their bridge;
- material scope changes, their provenance, and substrate-choice justification;
- positive object and whether the claimed method/system actually exists;
- predeclared primary metric and all material secondary metrics;
- decisive simple and published baselines under semantic and budget parity;
- all development and claim-level seeds with one trainer and explicit exclusions;
- strongest supporting and contrary evidence;
- standard-task or natural-system value, scope debt, costs, and side effects;
- claim-threatening pending or unread work;
- a fresh Codex `PRIZE`, `FIDELITY`, and `ENTRY` review.

`ENTRY: PASS` requires a mature positive object, fair decisive comparison,
appropriate reliability, and no unresolved contradiction likely to change the
paper’s correctness, importance, contribution identity, or main result. `HOLD`
means continue research or reset identity. It does not close the program. The lead
researcher may challenge a review with new raw evidence and request a fresh review;
it may not self-promote `HOLD` to `PASS`.

Use this compact schema rather than a persuasive essay:

```markdown
# PAPER_ENTRY
entry: HOLD | PASS
reviewed_at:
codex_thread:

original_program:
fingerprint: problem | type | positive object | primitive | population/task | primary metric | decisive baseline
program_to_paper_bridge:
scope_movement_and_provenance:
substrate_choice_justification:
implemented_positive_object:
primary_result:
material_secondary_results:
decisive_baseline_result:
seed_ledger:
contrary_evidence:
standard_task_value:
scope_debt:
costs_and_side_effects:
pending_claim_threats:

prize: PASS | HOLD — reason
fidelity: PASS | HOLD — reason
entry_review: PASS | HOLD — reason
```

The final `entry` is `PASS` only when all three independent judgments pass on the
same fingerprint. A missing field is evidence for `HOLD`, not an invitation to fill
it from the manuscript narrative.

## 6. Trip The Manuscript Circuit Breaker

Freeze submission-oriented writing and return the paper candidate to `candidate`
when new evidence shows any of the following:

- the decisive baseline wins on the registered primary outcome;
- the primary metric, population, or contribution object changes after results;
- seed provenance is mixed, a failed seed was excluded post hoc, or reliability is
  materially unresolved;
- a fair control reverses the central mechanism or necessity claim;
- the advertised positive method or system was never implemented;
- the standard task fails while only a selected private cell remains;
- the contribution type changes or a failed-method lineage becomes the new evidence.

After a trip, reconcile raw evidence and obtain a fresh Prize/Fidelity/Entry review.
Do not launch a rebuttal grid whose only purpose is preserving the frozen title.
A new experiment must follow from a named scientific redesign or discriminating
question. Deadline pressure changes portfolio choices, never evidence thresholds.

## 7. Keep State Compaction-Safe

Keep the live state concise and link to raw artifacts. Do not paste long historical
verdicts into its top section. A compacted conversation or memory summary is a
locator, not evidence and not authority. Before consequential resumption, verify any
claim-bearing summary against the current live state and named raw artifacts.
