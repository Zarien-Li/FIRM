---
name: research-review
description: Use Codex as an independent second PI and co-author — as a single independent pass or a bounded multi-round co-author loop with implementation and re-evaluation. Covers raw-evidence interpretation, method invention, experiment design, claim challenge, contribution-maturity judgment, research improvement, and submission assurance. Use especially before surprising or contradictory results harden into project state, when simple baselines invert a story, causal explanations compete, method design plateaus, evidence/methods/claims need independent reinterpretation, or a major compute or paper commitment approaches.
---

# Research Review

Use Codex to improve the research, not merely to approve a verdict.
For contribution-identity changes and paper entry, also follow
[the research control protocol](../shared-references/research-control-protocol.md).

## Runtime Role

Codex is the independent second PI for scientific judgments that would otherwise be escalated to the user. The lead researcher remains responsible for understanding the project, preparing trustworthy evidence, implementing and running work, and synthesizing the decision. This is collaboration between researchers, not delegation of ownership.

Codex can return `ENTRY: PASS` or `ENTRY: HOLD` for complete manuscript work.
That gate protects the paper claim only. Codex cannot create a user constraint,
declare a locus forbidden, or permanently close a method family, seed, or field.
Any such recommendation remains `[REVIEW]` advice unless the user explicitly adopts
it. The lead researcher may challenge `HOLD` with new raw evidence and a fresh
review, but may not self-promote it to `PASS`.

Invoke this skill when a competent researcher could reasonably choose materially different explanations, method designs, contribution identities, or paper-readiness judgments from the same evidence. In particular, review before writing a consequential `stop`, `freeze`, `retire`, `exhausted`, analysis fallback, method-family change, or submission-readiness conclusion. Do not invoke it for routine monitoring, obvious bugs, or every ablation.

The review must precede the lead narrative whenever feasible. If urgency required a provisional interpretation, label it provisional and do not promote it into the authoritative live state until the independent pass is synthesized. Never ask the user to choose among ordinary scientific continuations that Codex and the lead researcher can evaluate inside the established scope and budget.

## Reviewer Selection Policy

Use a genuinely independent model or context as the second PI. This suite was developed with
Codex MCP, but the scientific protocol does not depend on one provider. When Codex MCP is
available, calls to `mcp__codex__codex` and `mcp__codex__codex-reply` should omit the `model`
field and inherit the account default. With another reviewer, choose the strongest available
reasoning model and preserve fresh-thread independence.

Never hard-code, guess, enumerate, or silently downgrade model slugs. Record the reviewer
provider and model only when the runtime exposes them reliably.

After conversation compaction, any explicit model name recovered from session history, memory,
an old artifact, or an example is stale operational state. Re-read this skill and omit the model
field rather than replaying that name.

## Prepare A Small Evidence Packet

Provide the smallest sufficient context in an order that protects independence:

1. the original research program, canonical community tasks or systems, current paper candidate, and their proposed bridge;
2. raw result table, representative successes, failures, and inconvenient cases;
3. exact conditions, integrity notes, natural support, accumulated scope qualifiers, and paired utility costs;
4. prospective forecast and what the run was mature enough to test;
5. closest incumbent, strongest simple alternative, and contrary evidence;
6. method lineage as observations and lessons, without terminal labels;
7. current thesis and the lead researcher's tentative interpretation, explicitly marked tentative;
8. the scientific decision currently facing the researcher.

Do not lead with the desired answer, a pause recommendation, an analysis-paper fallback, or a summary that hides contrary cases. Old contracts, drafts, and state labels are provenance, not premises, unless current evidence independently supports them.

For a paper-entry review, do not provide only the manuscript or its author-written
summary. Include all development and claim-level seeds, failed and non-converged
runs, material secondary metrics, the strongest simple and published baselines,
pending claim-threatening work, and any post-result change to the primary metric,
population, positive object, or contribution type.

Prefer giving Codex durable paths to raw tables, logs, code, registrations, and representative cases in the project `cwd` so it can verify the packet. Include the lead researcher's prior forecast before revealing the preferred post-result explanation. A polished draft is never the sole evidence packet for deciding whether its own story is valid.

## Choose Thread Semantics

Use `mcp__codex__codex` for a fresh independent pass when:

- reinterpreting evidence;
- inventing a new method family;
- reviewing a major experiment plan;
- auditing a result or claim without narrative contamination;
- reconsidering a major reframe, paper identity, or portfolio-level pause.

Use `mcp__codex__codex-reply` only when continuing the same scientific dispute with new evidence, correcting a factual misunderstanding, or asking Codex to compare a revised method against its earlier objection.

Do not reuse a thread across unrelated pivots. Do not open repeated fresh threads to shop for a favorable verdict.

## Ask Through Five Perspectives

Use this order:

### Prize And Fidelity

- Restate the original program and the current paper separately. Has the latter become a silent replacement for the former?
- List every material task, benchmark, system, population, metric, or abstraction change and identify whether the user or agent introduced it.
- If the current plan succeeds perfectly, what is the strongest honest contribution and which community decision, standard task, or serious system changes?
- Which qualifiers and private restrictions have accumulated, and what evidence repays that scope debt?
- Was any substrate chosen because the candidate method had headroom or cleaner identification there?
- What is the shortest credible path from the discovery slice back to a natural standard surface?
- Is a locally correct result being optimized after its best-case scientific prize has already become too small?

### Interpret

- Where did this project's actual method-to-claim argument first become unsupported, and is a distinction missing from the researcher's current framing?
- What deeper variable explains the full pattern?
- Did the experiment test the right abstraction?
- Which observations resist the current thesis?
- What hidden coordinate does the simple baseline or inversion reveal?
- Which positive residual should the next method inherit rather than discard?
- What was the current realization mature enough to test, and are prototype weakness and primitive weakness being conflated?
- Which component or interaction comparison would most change the next construction, rather than merely explain the current one?

### Invent

- What would a strong PI build or test next if the current paper framing did not exist?
- What design assumption do all attempted methods share?
- What higher-level representation, state, objective, routing, memory, training, or system primitive follows?
- Which experiment best separates the leading causal accounts?
- How should a competent next realization preserve the observed gain while removing its interference or utility cost?
- What constructive ablation would add, remove, replace, freeze, reroute, or factorize the right part of the method?

### Attack

- What is the strongest correct-but-unimportant rejection?
- Is this an important opening or merely an unoccupied intersection of qualifiers?
- If the phenomenon is rare, does severity, theoretical reach, or a decisive counterexample make it consequential anyway?
- Does the specific problem earn its own significance, or borrow importance from the broad seed or benchmark?
- Is the discovery slice functioning as a microscope for a broader shared design failure, or has it silently become a tiny deployment population?
- What simpler composition could make the method unnecessary?
- What artifact, confound, benchmark issue, or utility cost could mimic success?
- Which assumption is most likely to fail?
- Was the paper object, slice, threshold, or explanation selected on the same evidence now offered as confirmation?
- Is the proposed relation non-trivial, or partly induced by definitions, metrics, candidate construction, or conditioning?
- Are failed methods being used as evidence for a bottleneck or impossibility they did not isolate?
- Is a tuned incumbent being used to reject an immature prototype before the proposed computation was activated or competently optimized?
- Have accumulated prohibitions made the design space artificially empty, and which are genuine constraints versus historical residue?

### Assess Maturity

- Does a mature paper contribution exist yet, or are there stable findings and useful assets whose importance, actionability, or confirmation is still incomplete?
- What is the strongest bounded contribution already supported by the evidence, if one exists?
- If failed branches and project history were removed, would the proposed contribution remain natural, consequential, and supported?
- If contribution type changed, was the new type independently earned or adopted as a fallback?
- Which objection would genuinely invalidate that contribution, and which would only narrow scope or revise wording?
- After all honest narrowing, is the supported claim still consequential enough for the intended audience and venue?
- Which proposed experiment could change the method, core claim, main comparison, or contribution maturity?
- Which attractive questions should be deferred to later work?
- Is the highest-value next action another experiment, method repair, or completion of the current paper?

For complete manuscript entry, issue three explicit judgments:

- `PRIZE`: the strongest honest best-case contribution and why the audience cares;
- `FIDELITY`: whether the proposed fingerprint and claim match all raw evidence,
  including contrary metrics, seeds, costs, and scope;
- `ENTRY`: `PASS` only when the positive object is mature, the decisive comparison
  is fair, reliability is appropriate, and no unresolved contradiction is likely
  to change correctness, importance, contribution identity, or the main result;
  otherwise `HOLD` with one highest-value research action.

Do not average these judgments into a score. Strong writing or stable findings
cannot compensate for failed fidelity or an immature positive object.

### Decide

- State one recommended scientific action inside the established scope and budget.
- Explain why it dominates the strongest alternative and what new evidence would reverse the choice.
- Distinguish work the lead researcher should execute now from a true user-level decision.

Require a constructive continuation before adversarial criticism, but do not assume that every constructive continuation belongs in the current paper. The second PI should help the lead researcher form a better method and recognize a mature contribution, not merely authorize stopping or continued probing. A portfolio pause may be recommended only after the broad seed and strongest higher-level continuation have been considered; a local failure cannot supply that judgment by itself.

Do not recommend paper completion merely because a relationship is stable or the project is old, expensive, or tiring. The positive object must still be natural, consequential, appropriately novel, actionable or explanatory, and supported at the requested contribution level. Stability is an evidence property, not a contribution property.

`No mature paper contribution yet` is an acceptable judgment. It should normally be followed by a concrete design or confirmation action, not a terminal label. Conversely, do not reject a genuine analysis contribution merely because it originated during method development; judge whether its object, confirmation, and consequence stand independently after the failed lineage is removed.

Reject closed victory framing. Ask what result would actually weaken the tentative interpretation or method. If every outcome can be routed to a different publishable story, require a more discriminating thesis before endorsing the program state.

## Example MCP Call

Call `mcp__codex__codex` with maximum available reasoning effort and a prompt shaped like:

```text
You are the second PI and co-author for this project.

EVIDENCE PACKET
[original research program, current paper candidate, paper-to-seed bridge, scope qualifiers,
thesis, value spine, discovery slice versus natural and claimed populations, raw contrasts,
exact conditions, contrary evidence, method lineage, closest incumbent, simple alternative,
current decision]

First assess PRIZE AND FIDELITY: distinguish the original program from the current paper,
state the best-case honest contribution if the plan succeeds, identify unpaid scope debt,
and propose the shortest reintegration path to a standard task or natural system.
Then INTERPRET the full evidence and identify the deeper variable or wrong abstraction.
Locate where the actual method-to-claim argument first became unsupported, without forcing the evidence into a preset taxonomy, and preserve what still worked.
Then INVENT the strongest higher-level method or discriminating experiment without inheriting
the current paper framing. ATTACK that proposal with the strongest simpler explanation,
artifact, utility cost, reviewer objection, post-selection risk, and mechanically induced relation.
Also attack SIGNIFICANCE: decide whether the concrete opening has meaningful natural support and
community leverage, or is only a clean unoccupied corner borrowing importance from the broad field.
Test CONTRIBUTION IDENTITY: remove failed branches and project history, then judge whether
the proposed contribution still has an independent natural object, confirming evidence, and
scientific consequence. Finally ASSESS MATURITY: state whether a mature paper contribution exists;
if it does, give the strongest bounded contribution that survives and distinguish claim-threatening
objections from scope limits. If it does not, preserve the real findings without manufacturing a
paper story and choose the method-building or confirmation action with highest expected value.

When this is a paper-entry review, end with:

```text
PRIZE: [best-case contribution and audience consequence]
FIDELITY: PASS or HOLD — [raw-evidence reason]
ENTRY: PASS or HOLD — [paper-entry reason]
IDENTITY FINGERPRINT: [problem | type | positive object | primitive |
population/task | primary metric | decisive baseline]
```

Explicitly name evidence that would weaken your preferred interpretation. Do not allow positive
and negative outcomes to become separate victory branches.

End with one recommended next research action, why it dominates the strongest alternative, what
the lead researcher should execute without asking the user, and what evidence would change it.
```

Save the returned thread ID when the question may require follow-up. Use `mcp__codex__codex-reply` with that ID and only the new evidence or precise dispute.

## MCP Failure Handling

Treat Codex transport, authentication, model-availability, and version failures as infrastructure failures, not scientific evidence.

- Use the configured `mcp__codex__codex` tool by default. The configured server is the Codex CLI running in `mcp-server` mode; do not describe it as a separate older implementation without checking the exact configured executable and version.
- Make one call with no `model` field. If a compacted session first attempted a stale explicit model, correct it with one no-model call; do not try a sequence of model names.
- If the tool says a model is unsupported or requires a newer Codex version, do not guess alternate model slugs, weaken reasoning, or fall back to a bare `codex` command. Preserve the evidence packet and review question, report the infrastructure fault, and retry after the MCP configuration or Claude session is refreshed.
- After a user-level MCP command changes, a running Claude Code session may still own the old subprocess. Restart Claude Code before judging the repair unsuccessful.
- If direct CLI execution is explicitly needed for `repo-direct` verification, resolve the executable with `command -v codex`, record `codex --version`, and use that exact executable for the run. Do not assume a user-specific installation path or create a prompt file merely to work around an MCP version error.
- Never convert an unavailable second-PI review into approval, rejection, or a research pause. Record `second_pi_status: deferred_tool_unavailable`, perform an explicit self-adversarial `Interpret -> Invent -> Attack -> Assess Maturity` pass as the lead researcher, and continue work that does not depend on the missing independent judgment. Preserve the packet for a later fresh Codex review.

## Main-Researcher Synthesis

Codex is independent scientific input, not authority over user constraints or the
research program. Reconcile the response with local evidence:

```markdown
## Codex Second-PI Synthesis
- question reviewed:
- insight adopted:
- suggestion rejected and evidence:
- thesis change:
- method or experiment change:
- effect on the current paper claim:
- claim-threatening versus non-blocking objections:
- contribution-maturity judgment:
- Prize/Fidelity/Entry judgment, when applicable:
- paper identity fingerprint and whether it changed:
- constraint provenance check: no reviewer advice promoted to `[USER]`
- next action and why:
- execution started or durable next command:
- thread ID, if continued:
```

Update the existing research state before reporting a scientific decision to the user. Remove or demote any live-state instruction contradicted by the synthesis while preserving it as dated history. Then execute the chosen reversible action; do not end with an unranked menu or wait for the user to repeat the second PI's work. Create a separate review report only when the reasoning is substantial or needed for audit.

End the dialogue when it has changed the thesis, method, experiment, claim, or maturity judgment concretely. Do not loop for ceremonial convergence. The lead researcher must synthesize and act rather than asking Codex to become the project's final authority.

## Looped Mode: Bounded Multi-Round Co-Author Loop

Use the single-pass flow above for one independent judgment. Switch to **looped mode** when evidence, methods, experiment plans, or claims need independent reinterpretation, **constructive redesign, implementation fixes, and re-review** — i.e. when the point is not one verdict but a bounded review → implement → re-evaluate cycle. Do not run a score-optimization treadmill.

### Choose The Purpose

- `purpose: research` is the default. Improve the thesis, method, or decisive experiment.
- `purpose: submission` audits a completed evidence package and paper claim.

Use at most four rounds by default. A round is useful only when it changes a scientific decision, evidence surface, implementation, or supported claim.

### Preserve Loop State

Maintain:

- `AUTO_REVIEW.md`: cumulative raw reviews, researcher syntheses, actions, and results;
- `REVIEW_STATE.json`: purpose, round, thread ID, active question, pending runs, and status;
- the project's main research state: thesis, contrary evidence, method lineage, next action.

Persist state after each round. An interrupted experiment remains pending work, not a negative result.

### Round Mechanics

Each round uses the same evidence-packet rules and the same `Interpret -> Invent -> Attack -> Assess Maturity -> Decide` passes as the single-pass flow. Codex tool failures do not count as review rounds. On authentication, transport, unsupported-model, or "requires a newer version" errors, keep the round pending and follow the MCP Failure Handling section above. Do not guess model names, switch to a weaker model, or invoke PATH-dependent `codex exec` as an automatic fallback.

For `purpose: submission`, additionally ask for verified claims, unsupported
claims, missing comparisons, and explicit Prize/Fidelity/Entry judgments.

Thread semantics follow the rules above: `codex-reply` when new evidence addresses the same scientific dispute; a fresh thread when the thesis or method family changes substantially, an independent claim audit is needed, or the previous thread has become anchored to an obsolete framing. Never shop for a favorable verdict.

### Implement And Re-Evaluate

Execute the selected change within existing permissions and user constraints:

- repair an evidence or implementation defect;
- redesign the primitive at a higher level;
- run a discriminating or claim-defining experiment;
- add a strong missing comparison;
- narrow an unsupported claim;
- improve paper text only after the evidence is sufficient.

Do not automatically implement every requested ablation. Implement a review action when it materially affects the thesis, causal claim, method necessity, fair comparison, or supported scope. Replace ceremonial checklist work with a more decisive test and explain the choice.

For running experiments, record configs, commands, logs, checkpoints, deviations, and result paths. Obtain user confirmation for exceptional compute, locked-scope changes, destructive operations, or permanent termination.

When results arrive, compare them with the forecast, inspect raw cases, update the thesis, and continue the same Codex thread if the scientific question remains the same.

### Optional Review Strength

- `standard`: Codex reviews the supplied evidence packet.
- `memory`: keep unresolved explanations and suspicions across rounds in the same thread.
- `repo-direct`: use a fresh independent Codex process with read access to verify code, metrics, result files, and claims. Use this primarily for evidence or submission audit, not as the default idea generator.

For `repo-direct`, resolve and record the reviewer executable and version when direct CLI execution is genuinely required. MCP or another structured reviewer interface remains preferable because it preserves thread identity and tool boundaries.

All strengths use the same pass order. Greater adversarial access does not remove the constructive co-author role, and deeper invention does not automatically become another obligation for the current paper.

### Loop Completion

For `purpose: research`, finish when:

- a concrete thesis, method, or decisive-experiment change has been implemented;
- its immediate evidence has been interpreted when available;
- another review round would not change the current best action enough to justify its cost.

The best action may be consolidation. Do not keep the loop alive merely because Codex can invent another deeper question after the current claim is already earned.

Do not require a positive score. End with the best next research action, not a declaration that the field passed review.

For `purpose: submission`, finish when independent evidence and claim audits
support the intended scope and the reviewer returns `ENTRY: PASS`. `HOLD` means
unresolved submission work or an identity reset, not research failure and not field
closure.

At the round limit, state the unresolved scientific disagreement and recommend one continuation. Do not automatically pivot to an analysis paper or permanent stop.

### Loop Review Record

Append the complete raw Codex response and the researcher synthesis to `AUTO_REVIEW.md`. Preserve thread IDs for continued disputes. Update `REVIEW_STATE.json` to `completed` only when the loop ends for one of the reasons above.
