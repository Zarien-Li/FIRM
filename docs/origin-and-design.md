# Origin and Design

[Back to the README](../README.md)

> Most autonomous-research tools optimize execution. FIRM focuses on the
> scientific decisions between executions.

## Why FIRM exists

Long-running research agents rarely fail only because they cannot search, code,
or launch a job. They fail in plausible ways after evidence arrives:

- one failed implementation becomes a verdict on an entire method family;
- one clear design loss triggers a large seed sweep;
- a simple baseline win is treated as an exit rather than a mechanistic clue;
- a clean but project-specific slice silently replaces the important problem;
- probes and taxonomies accumulate without changing a design decision;
- a draft hardens before provenance, evaluator semantics, and the strongest
  matched baseline are secure;
- after the core claim is mature, the standard keeps moving and the paper never
  gets harvested.

FIRM was developed by repeatedly revising Claude Code research workflows against
these failures. It is a collection of callable skills rather than a claim that a
single fixed pipeline can automate scientific discovery.

## The durable design changes

### One researcher, not a stage machine

Earlier workflows tended to accumulate stages, gates, and ledgers. Those structures
made progress easy to count, but provisional agent judgments could become permanent
rules. FIRM instead uses one persistent `research` skill and narrowly scoped
specialists. A skill is a capability, not permission to enter the next stage.

### Failure is diagnosed at several levels

A negative outcome can indicate:

1. a broken or untrustworthy run;
2. a failed realization of an idea;
3. a failed load-bearing primitive;
4. a broader method-family failure.

The conclusion should stop at the narrowest level supported by the evidence. This
prevents both premature closure and wasteful persistence.

### Method versions form a constructive lineage

A method attempt is useful when it reveals which causal assumption, component, or
interaction failed. The next version should inherit what worked and change the
implicated element. FIRM therefore records method evolution as:

```text
causal bet → component change → observed activation → failure → surviving part → next repair
```

This is different from collecting unrelated variants or searching for a lucky
positive seed.

### Program value and paper scope stay separate

A broad research program can produce a narrower valid paper, but the paper must earn
importance at its actual scope. FIRM separates:

- the original research program;
- the current paper candidate;
- the diagnostic or discovery slice;
- the scope debt created by successive restrictions;
- the evidence that reconnects the contribution to a natural task or system.

The purpose is not to force every paper to solve the whole field. It is to prevent a
small private cell from borrowing significance from a broad field name.

### Explanation is a problem model, not a probe inventory

Between empirical contact and construction, FIRM reconstructs the relevant incumbent
computation and why its default assumption is useful, then explains the earliest
matched success/failure divergence, contrary evidence, intervention locus, and behavior
to preserve. The required depth is the depth needed to choose among genuinely different
designs, not exhaustive causal identification of the entire model.

### Independent collaboration follows comparative advantage

The `research-review` skill keeps one persistent GPT PI for synthesis, continuity, and
submission; Claude supplies bounded implementation and experiment episodes, Gemini is
invited for evidence-earned creative invention, and an independent Codex episode
sparingly verifies one named decision-relevant uncertainty. External-model prose never
becomes project authority; artifacts cross collaborator boundaries.

### Finishing is a scientific decision

FIRM resists two opposite errors: writing a polished paper before the contribution
is real, and withholding a bounded mature paper because more experiments are always
possible. Paper entry depends on a positive object, an implemented contribution, a
fair decisive comparison, traceable evidence, and honest scope—not project age,
file count, or deadline pressure.

## Relationship to ARIS

FIRM is independent and unofficial. It is not maintained or endorsed by the ARIS
authors.

ARIS demonstrated useful foundations for skill-based research automation,
persistent artifacts, end-to-end execution, and adversarial review. Selected
workflow concepts and portions of FIRM's early skill lineage were adapted from ARIS
under the MIT License. Continued use led to substantial restructuring around
research judgment, failure-level calibration, constructive method lineage, scope
debt, and paper/program separation.

| ARIS-informed foundation | FIRM's current focus |
|---|---|
| Portable `SKILL.md` workflows | A Claude Code plugin with precise, on-demand research skills |
| Persistent artifacts | Compact evidence-linked research state rather than many permission ledgers |
| Executor and reviewer roles | A fresh second PI used at genuine ambiguity, not as a terminal oracle |
| End-to-end research automation | Judgment after negative, mixed, or contradictory evidence |
| Review and assurance | Early integrity checks and honest paper-entry decisions |

Upstream attribution is preserved in [NOTICE](../NOTICE) and [LICENSE](../LICENSE).

## What counts as evidence for a skill change

FIRM's strongest development signal is a recurring failure pattern:

1. the agent behaves plausibly but makes a scientifically costly decision;
2. the hidden confusion can be stated precisely;
3. a minimal instruction repairs that confusion;
4. neutral cases show the repair does not create the opposite error;
5. obsolete or conflicting instructions are removed.

Internal research usage and human review of resulting work motivated the system,
but they are not presented as a controlled estimate of FIRM's causal effect. The
public repository therefore emphasizes inspectable skills, neutral examples,
explicit safety boundaries, and reproducible installation rather than a headline
usage number.

## Why one GPT PI skill and bounded specialists

FIRM does not try to win by containing every research utility. Literature APIs,
benchmark launchers, plotting libraries, LaTeX tools, and general coding agents
already exist. The existing `research-pipeline` is the one persistent GPT PI surface.
Its focused references carry only the details needed by the current uncertainty;
specialist skills remain bounded workflows for implementation and explicit operations:

- choosing and preserving a consequential problem;
- establishing credible empirical contact;
- interpreting evidence at the right level;
- constructing and repairing a method;
- allocating experiments by information value;
- auditing integrity and scope;
- recognizing and writing a mature bounded contribution.

The suite should become clearer and more reliable, not merely longer.

## What FIRM does not promise

- autonomous scientific discovery on every problem;
- a paper, acceptance, or reviewer score;
- that every negative result contains a viable method;
- that a fresh reviewer is always correct;
- that skills replace domain expertise or researcher responsibility;
- that research can be made safe through prompts alone.

FIRM is an inspectable layer of research guidance. The human researchers remain
responsible for novelty, data, compute, authorship, citations, disclosure, claims,
and submission.
