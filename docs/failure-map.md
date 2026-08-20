# The FIRM Failure Map

> AI research agents rarely fail by doing nothing. They fail by doing plausible work in the
> wrong scientific direction.

This map records recurring failure patterns observed across long-horizon research work.
It is not a taxonomy invented before use: each category exists because projects repeatedly
exposed the same underlying confusion.

The map is deliberately compact. It describes recognizable behavior, the mistaken inference
behind it, the cost to the research program, and the FIRM capability intended to repair
it.

## 1. Value And Scope Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| A broad seed such as image editing or knowledge editing becomes a paper about one project-defined cell | A reproducible phenomenon is assumed to be important merely because it is specific | The work becomes rigorous but irrelevant | Keep the original program, current paper, value spine, scope debt, and reintegration path visible in [`research`](../skills/research-pipeline/SKILL.md) |
| The agent keeps drilling inward after each result | Mechanistic depth is confused with community value | Months of work optimize an abstraction few researchers care about | Re-run Prize and Fidelity review before major method, compute, and paper-identity commitments |
| A crowded field triggers an automatic pivot | Similar terminology is treated as proof that the opening is closed | The agent abandons important, benchmarked problems without matched evidence | Promote nearby work to strong baselines and ask whether it closes the same natural failure in [`baseline`](../skills/baseline/SKILL.md) |

## 2. Method-Formation Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| Method v1 fails and the whole method family is retired | One realization is confused with the underlying primitive | Promising directions die before constructive design begins | Preserve what activated, locate the failed component, and form v2 through constructive ablation in [`method-primitive-synthesis`](../skills/method-primitive-synthesis/SKILL.md) |
| A simple baseline wins and the agent exits | Winning is treated only as rejection, not as evidence about the mechanism | The strongest clue to a better method is discarded | Explain why the baseline wins, find its natural boundary, and design beyond that boundary |
| Many method loci are attempted with no stable lineage | Experimental variety is confused with method maturity | The project accumulates runs but never forms a load-bearing primitive | Require each new version to inherit, replace, or test a specific causal component |
| Probe accuracy becomes the contribution | Predictability is confused with controllability | The project produces an atlas instead of a method | Every probe must change a design choice, eliminate an explanation, or stop |

## 3. Experiment-Allocation Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| One competent seed shows a large design failure, then ten more seeds are launched | Design uncertainty is confused with statistical uncertainty | GPU and time are spent confirming the wrong question | Diagnose or redesign after a mechanistically decisive failure; add seeds only for a defined stochastic claim |
| A noisy small effect triggers immediate redesign | Statistical uncertainty is confused with design failure | Potentially valid mechanisms are abandoned too early | Use matched seeds, confidence intervals, and power-aware replication through [`experiment-plan`](../skills/experiment-plan/SKILL.md) |
| GPU availability determines the scientific next step | Available infrastructure is mistaken for research priority | Cheap decisive reasoning is skipped while expensive jobs proliferate | Select experiments by information and paper value, then execute through [`run-experiment`](../skills/run-experiment/SKILL.md) |
| Waiting for a long run pauses the entire project | Research ownership is reduced to job monitoring | Literature, code, interpretation, controls, and writing assets remain idle | Advance independent work while [`monitor-experiment`](../skills/monitor-experiment/SKILL.md) watches the run |

## 4. Evidence-Integrity Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| The main claim is drafted before scorer, masking, provenance, or padding is audited | A plausible number is treated as a trustworthy measurement | Late audit can invalidate the paper identity | Audit evaluation boundaries before expensive scaling and again before submission with [`research-audit`](../skills/research-audit/SKILL.md) |
| A strong baseline is compared under mismatched data, cost, or training | A familiar name is mistaken for a fair incumbent | Claimed progress disappears under matched conditions | Reproduce the actual incumbent and lock comparison semantics |
| Training output exists, so optimization is assumed successful | Completion is confused with convergence | Scientific conclusions are drawn from unhealthy runs | Inspect curves, failures, checkpoints, and effective budget before interpreting results |
| A claim survives repeated retelling but loses contact with raw evidence | Narrative consistency is confused with evidential support | Unsupported causal language enters the paper | Reconstruct claims from artifacts and verify citations through [`research-audit`](../skills/research-audit/SKILL.md) |

## 5. Interpretation And Review Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| An independent model is called only when the project wants permission to stop | Collaboration is treated as judgment instead of co-research | Fatal controls arrive late and invention never benefits from a distinct creative view | Use [`research-review`](../skills/research-review/SKILL.md) selectively: Gemini for evidence-earned creative invention, sparse Codex for late red-team verification, with the lead PI retaining synthesis and action |
| Reviewer criticism becomes a permanent prohibition | A model-authored verdict is mistaken for user authority | One review silently shrinks the research program | Treat reviewer output as evidence and argument, never as an irreversible gate |
| Tool failure pauses the science | Reviewer availability is confused with research ownership | Infrastructure incidents become scientific conclusions | The primary researcher completes its own interpretation and continues non-blocked work |
| A negative result receives a sophisticated label and is treated as understanding | Naming a failure is confused with explaining it | Vocabulary grows while causal knowledge does not | Require alternative explanations, discriminating evidence, and a design consequence |

## 6. Paper-Identity And Harvest Failures

| Observable behavior | Hidden confusion | Scientific cost | FIRM response |
|---|---|---|---|
| Several failed methods are repackaged as an analysis paper | Difficulty of intervention is confused with an independent positive object | The paper has history but no contribution readers need | Apply the deletion test: if the analysis collapses when failed methods are removed, it is not yet an analysis contribution |
| Correct abstention or certification failure is presented as method success | Conservative behavior is confused with positive capability | The paper overstates what was achieved | Map results to bounded claims and real value metrics |
| Every new limitation triggers another experiment | Completeness is confused with publishability | Mature work never reaches submission | Decide whether the next result changes the bounded claim or merely broadens future work |
| A draft is started because a deadline exists | Text production is confused with contribution maturity | Writing hardens a weak or incoherent paper identity | Enter [`paper-writing`](../skills/paper-writing/SKILL.md) only when the positive object, decisive comparison, evidence, and scope are stable |

## How To Use This Map

For a stalled project, do not read the map as a checklist. Find the one behavior that best
describes the current decision, then inspect the underlying confusion:

1. recover the original research program and the current paper candidate;
2. identify whether the uncertainty is about value, design, statistics, evidence, or maturity;
3. invoke only the skill that helps resolve that uncertainty;
4. record what the new evidence changes;
5. remove any old rule that no longer reflects the project.

The goal is not to prevent failure. Productive research requires failed hypotheses. The goal is
to stop an agent from drawing a larger conclusion than the evidence supports, or spending another
week answering the wrong question.

## The Open-Source Bet

The defensible asset in autonomous research is not a longer prompt. It is accumulated knowledge
of how plausible research behavior goes wrong.

FIRM makes that knowledge inspectable. New contributions should add a failure only when
it has recurred in real use, identify the causal instruction or omission, and show that the repair
does not create an equal and opposite failure.

**The next research agent will make mistakes. It should not have to repeat all of ours.**
