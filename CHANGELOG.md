# Changelog

## Unreleased

- Consolidated sixteen callable research skills into six entrypoints: one persistent
  `research-pipeline` PI and five on-demand tools for foundation, method development,
  experiment operations, review, and paper writing. Moved retained protocols, scripts,
  tests, and shared principles under their owning skill, then removed overlapping
  instructions that repeated another skill's responsibility. Removed the separate
  top-level `shared-references` installation surface.
- Made the existing `research-pipeline` the sole persistent GPT PI surface. Its entry
  point now routes to five focused references for empirical foundations, collaboration,
  method maturation, execution truth, and submission; Trae installs only this skill,
  while Claude receives a compact bounded-collaborator prompt and specialist workflows.
  Replaced phrase-matching semantic tests with packaging and progressive-disclosure
  checks, while keeping historical scientific regressions as test scenarios rather than
  runtime rules.
- Reorganized multi-model responsibility around one persistent GPT PI, bounded Claude
  implementation/experiment episodes, invited Gemini invention, and sparse independent
  Codex verification. Added artifact-grounded candidate judgment without scientific
  status enums or maturity classifiers; early information-flow mapping; three distinct
  baseline responsibilities; method debt and contrastive-surface reasoning; fresh
  scientific-episode boundaries; and a mechanical, atomic campaign-manifest helper.
- Defined research baselines as named methods from recent relevant papers rather than
  raw foundation checkpoints or project-invented heuristics. Backbone runs now establish
  substrate competence, matched controls serve attribution, and field contact requires
  a strong reproducible published incumbent plus the nearest claim-threatening method.
- Added a PI-owned single `PROJECT_STATE.md` contract: projects repair and update one
  shared scientific state after meaningful transitions, while dashboards and
  Codex are limited to mechanical provenance, freshness, process, and seed-fidelity
  checks. Competing pipeline/status files and identity-current fields are historical
  provenance, not parallel authority. Mechanically migrated state remains explicitly
  pending and unverified until the project PI reconciles its claims against current
  artifacts. Added regression coverage against control-plane-authored research judgments.
- Added restart-safe experiment recovery: rediscover remote workers and artifacts after
  host or session loss, avoid duplicate submissions, and allow authorized project-owned
  execution paths when FIRM is unavailable.
- Required every Gemini improvement proposal to be collision-checked, implemented, and
  validated by the lead PI before it changes method maturity or paper evidence.
- Replaced the absolute "beat every baseline" SOTA gate with a pre-specified,
  claim-dependent value contract: decisive comparisons must rule out the intended
  alternative, while a meaningful Pareto advantage may establish contribution value.
- Restored early `AUTHOR_ARGUMENT.md` and provisional problem-story writing after a
  credible positive object, while keeping submission maturity grounded in decisive
  evidence rather than prose.
- Restored direct exemplar-informed authorship: one isolated author subagent reads the
  complete role-relevant papers, argument, and evidence instead of drafting from an
  averaged synthesis.
- Restored semantic and regression coverage for design-giving problem analysis,
  defensive Codex reviews, human-reader editing, and correlation-to-method jumps.
- Rebuilt paper authorship around a one-page `AUTHOR_ARGUMENT.md` that identifies the
  human reader, prior belief, belief-changing fact, significance, and intended change
  in understanding before outlining begins.
- Demoted claims-evidence tables to post-draft factual verification so evidence audits
  repair unsupported prose without generating section order, transitions, or voice.
- Replaced exemplar-report synthesis with a dedicated author subagent that reads full,
  role-specific exemplary papers together with the paper's argument and evidence, then
  directly drafts a coherent section.
- Replaced reviewer-style prose optimization with human-reader editing based on
  ten-minute recall, authorial voice, field-natural language, paragraph progression,
  specificity, and memorability.
- Moved non-consequential caveats to Limitations and allowed an early problem-story
  Introduction that is rewritten after the central evidence stabilizes.
- Replaced open-ended Codex red-team review with decision-focused verification: one
  named uncertainty, one current decision it could reverse, an explicit action burden
  for every recommendation, and `no material change` when no intervention is justified.
- Added a design-giving problem model between empirical contact and construction:
  reconstruct incumbent computation and rationale, the useful default assumption,
  earliest matched success/failure divergence, contrary evidence, intervention locus,
  falsifying counterfactual, and behavior that a method must preserve.
- Aligned literature reading and explanatory experiments with that problem model so
  deeper analysis replaces correlation-to-method jumps without reviving exhaustive
  probe atlases.

## 1.2.0 - 2026-08-20

- Replaced the public alias layer with the byte-identical local canonical skill
  payload: 16 skills, shared references, `CLAUDE-RESEARCH.md`, and installer.

- Split independent collaboration by comparative advantage: Codex is now a sparse
  late-stage red-team verifier, while optional Gemini 3.1 Pro collaboration supplies evidence-grounded creative
  invention before v1, during substantive v2 redesign, and during positive program
  expansion. Gemini prompts remain episode-authored, and proposals require normal
  literature collision checks, implementation, and experiments.
- Replaced per-result gate logic with a flexible research-episode rhythm: competent
  empirical contact, explanatory pause, one protected construction arc, credible
  positive object, program expansion, paper formation, and stabilization.
- Added a concise Program Compass and Current Research Episode as the canonical live
  state, while demoting historical stop, paper-readiness, and continuation labels to
  provenance rather than scientific authority.
- Changed method development from serial candidate tests into constructive v1-to-vN
  cultivation that preserves activated computation and design lessons.
- Restored timely paper harvest: paper accounting begins after a credible positive
  object, while Program Expansion determines whether a positive deserves paper-sized
  resources.
- Consolidated accumulated lessons into a maintenance principle registry and
  regression-scenario suite so shorter daily skills do not discard hard-won failure
  knowledge.
- Separated submission-sufficient evidence from post-sufficiency scale expansion:
  close every claim-critical link locally, but move table-enlarging thousand-GPU-hour
  sweeps to designated high-compute infrastructure once they can no longer change the
  paper's correctness, novelty, or viability.

## 1.1.1

- Added accepted benchmark anchors and explicit claim-bearing, training, and
  diagnostic artifact roles so derived data cannot silently become the paper target.
- Added paper-asset targets and continuation evidence for construction-scale work.
- Changed competent-negative handling to consolidate or re-ground before another
  method episode, without imposing a mechanical episode limit.
- Added a release-time semantic contract check for these research-yield principles.

## 1.1.0

- Added Scientific Upside and one-sentence replacement-principle formation before
  method naming.
- Added Program Expansion review after the first credible positive realization.
- Split probe budget from paper budget so large campaigns fund contribution growth,
  not regime shopping or defensive table expansion.
- Added the 80% deletion and ten-times-resource tests for reusable primitives.
- Added connected contribution stacks for papers with one governing identity.
- Changed result handling so observations update by default; explanations, methods,
  and paper identity update only from discriminating evidence bundles.

## 1.0.0

- Added official Claude Code plugin and marketplace manifests.
- Reworked all 16 skill descriptions for clearer activation boundaries.
- Added explicit-only safeguards for compute, remote, manuscript-wide, and
  artifact-level audit workflows.
- Made `research-review` provider-neutral and independent through a fresh context.
- Rebuilt the flagship result-diagnosis, method-design, experiment, audit, and
  paper workflows with progressive disclosure.
- Added a neutral demo fixture, concise documentation, validation CI, and an
  idempotent project-local installer.
- Removed automatic remote pushes, plaintext-key examples, default `sudo`
  installation, and unsupported commands from public documentation.
