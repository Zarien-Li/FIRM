<p align="center">
  <strong>FIRM</strong><br>
  <sub>Failure-Informed Research for Machines</sub>
</p>

<h1 align="center">The research judgment layer for AI coding agents.</h1>

<p align="center">
  Claude Code can run 1,000 experiments and still spend a month answering the wrong question.<br>
  FIRM keeps the broad problem alive, turns failures into better designs, and makes a paper earn its way into writing.
</p>

<p align="center">
  <a href="#start-in-one-command"><strong>Start in one command</strong></a> ·
  <a href="#see-the-difference">See the difference</a> ·
  <a href="docs/getting-started.md">Read the guide</a> ·
  <a href="examples/README.md">Inspect the cases</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/field_observation-100B%2B_model_tokens-111318?style=flat-square" alt="100B+ model tokens">
  <img src="https://img.shields.io/badge/research_tools-17-285943?style=flat-square" alt="17 research tools">
  <img src="https://img.shields.io/badge/primary_runtime-Claude_Code-D97757?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/second_PI-Codex-111318?style=flat-square" alt="Codex second PI">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2f81f7?style=flat-square" alt="MIT License"></a>
</p>

---

FIRM is an open research operating model built from the failure patterns of more
than **100B model tokens** across Claude, GPT, GLM, Kimi, and DeepSeek systems.
It is not another giant prompt, fixed stage machine, or autonomous paper mill.
It is a compact set of skills that helps an agent make the decisions a strong
first author or PI would make while the evidence is still changing.

## See The Difference

<p align="center">
  <img src="assets/firm-decision-demo.png" width="100%" alt="The same failed method result produces a field-closure decision without FIRM and a constructive design diagnosis with FIRM">
</p>

One competent run says the prototype loses. The wrong response is either to kill
the field or to search more seeds for a lucky sign. FIRM asks what component the
result actually diagnosed, what evidence survives, and which single next
experiment changes the design.

## Start In One Command

Run this inside an existing research project, or inside an empty directory for a
new one:

```bash
git clone https://github.com/Zoiya-Li/FIRM.git ~/FIRM && ~/FIRM/firm init .
```

Then start Claude Code as usual. FIRM preserves an existing `CLAUDE.md`, installs
project-local skills, creates a compact research program, and prints the exact
first message to send.

```bash
claude
```

Verify the installation at any time:

```bash
~/FIRM/firm doctor .
```

Already have `~/FIRM`? Run `git -C ~/FIRM pull` and then `~/FIRM/firm init .`.
The installer also supports [global, project-local, and dry-run modes](docs/getting-started.md).

This is backed by the runnable fixture in [`demo/fixture`](demo/fixture), not a
made-up interface. Try the 90-second terminal walkthrough:

```bash
make demo
```

## What FIRM Changes

| Protect the problem | Build through failure | Earn the paper |
|---|---|---|
| Keeps the original broad program separate from the current experiment or draft | Separates run, realization, primitive, and method-family failure | Requires an independent Prize/Fidelity/Entry review before full manuscript production |
| Tracks scope debt when a useful field quietly collapses into a private slice | Uses a bad result to choose the next constructive ablation, not an arbitrary seed sweep | Prevents failed method lineages from quietly becoming weak analysis papers |
| Reintegrates local mechanisms into a standard task, system, or value metric | Distinguishes design uncertainty from statistical uncertainty | Aligns claims, baselines, evidence, costs, limitations, and writing |

The output is intentionally small: one live state, one method lineage, one
contrary-evidence register, and one highest-value next action. FIRM adds judgment,
not paperwork.

## Why Agents Need It

Research agents usually fail after the code starts working.

| Expensive failure pattern | What it looks like in practice | FIRM's correction |
|---|---|---|
| **Seed drift** | A broad topic becomes a tiny cell only the project itself cares about | Preserve the original program, value spine, and reintegration path |
| **One-loss closure** | Method v1 loses, so the agent declares the direction exhausted | Diagnose the realization and construct v2 at the evidence-indicated locus |
| **Seed laundering** | A competent negative run triggers ten more seeds | Repair design uncertainty before paying for statistical certainty |
| **Probe addiction** | Predicting a failure is mistaken for fixing it | Every probe must change a method decision |
| **Baseline debt** | The paper forms before the strong matched baseline is correct | Audit fidelity and provenance before locking paper identity |
| **Analysis fallback** | Failed interventions are repackaged as an analysis contribution | Require a positive object that survives deletion of the failed methods |
| **Premature writing** | A polished draft creates commitment to an immature claim | Keep a candidate claim until independent paper-entry review passes |

FIRM is cheapest before the wrong experiment, not after the wrong paper.

## Field Tested, Carefully Stated

| Observed development scale | Human research checkpoint |
|---|---|
| **100B+ model tokens** across five model families and 17 deployed configurations | **3 human-verified papers** developed under successive FIRM versions |
| Repeated use across method, analysis, systems, and multimodal projects | **9 official ACL ARR reviews** with mean overall assessments of **3.50**, **3.33**, and **3.17** |

Why the token count matters: it is the failure dataset behind FIRM. At that
scale, recurring mistakes stop looking anecdotal. We observed agents repeatedly
drift from valuable seeds, overinterpret one run, expand seeds when a design is
broken, discover fatal controls after writing, and mistake activity for method
maturity. FIRM encodes the countermeasures that survived those repetitions.

The review record is reported only in aggregate to protect active double-blind
submissions. Every counted paper was read, checked, and approved by human
authors before submission. These scores are **not acceptance decisions**, and
they are not a controlled estimate of FIRM's causal effect. They are an external
checkpoint showing that this system was exercised on real papers under real
review, rather than written as an untested prompt collection.

## The Operating Model

FIRM keeps one persistent researcher active and loads specialist skills only
when they are useful:

```text
RESEARCH PROGRAM
      |
      v
Prize -> Fidelity -> Design -> Evidence -> Entry
  ^         |          |          |          |
  |         +----------+----------+----------+
  |             evidence can revise the program
  +------------------------------------------------
```

1. **Prize:** If everything works, is the result important enough to matter?
2. **Fidelity:** Are the task, baseline, scorer, provenance, and costs real?
3. **Design:** What load-bearing primitive follows from the evidence?
4. **Evidence:** What does this run diagnose, and what remains alive?
5. **Entry:** Has the current claim earned full paper writing?

Codex acts as an independent second PI at consequential boundaries. Its role is
to challenge prize and fidelity, reinterpret evidence, invent alternatives, and
attack the strongest explanation. It is not a stop-button oracle, and a Codex
outage does not pause the lead researcher's work.

## What Gets Installed

```text
your-project/
├── CLAUDE.md                    # existing instructions preserved
├── .firm/
│   ├── RESEARCH_PROGRAM.md      # broad problem, value, resources
│   ├── FIRST_MESSAGE_NEW.md     # exact new-program startup prompt
│   ├── FIRST_MESSAGE_AUDIT.md   # exact existing-project audit prompt
│   └── ...                      # backups and install metadata
└── .claude/skills/
    ├── research-pipeline/       # persistent first-author identity
    ├── research-lit/            # decision-linked literature work
    ├── baseline/                # matched reproduction and raw behavior
    ├── method-primitive-synthesis/
    ├── experiment-plan/         # adaptive, claim-aware experiments
    ├── research-review/         # independent second PI
    ├── signal-analysis/         # interpretation and design consequence
    ├── paper-writing/           # gated manuscript production
    └── ...                      # 17 focused tools in total
```

Read the complete [`skills/INDEX.md`](skills/INDEX.md). The suite is one
researcher with tools, not 17 competing personalities and not a rigid state
machine.

## Inspect Before You Trust

Start with three sanitized field cases:

| Case | The costly mistake | What FIRM changes |
|---|---|---|
| [A method loses once](examples/01-method-loss-is-not-field-loss.md) | One realization is confused with the field | Preserve valid evidence and form the next constructive ablation |
| [The seed disappears](examples/02-seed-drift.md) | A valuable program shrinks into an isolated diagnostic cell | Track scope debt and force standard-task reintegration |
| [The paper starts too early](examples/03-paper-entry-audit.md) | Writing quality hides scientific immaturity | Run independent Prize/Fidelity/Entry review first |

Then inspect the implementation:

- [`research-pipeline`](skills/research-pipeline/SKILL.md): persistent ownership and continuity
- [`method-primitive-synthesis`](skills/method-primitive-synthesis/SKILL.md): constructive method formation
- [`research-review`](skills/research-review/SKILL.md): second-PI protocol
- [`paper-writing`](skills/paper-writing/SKILL.md): evidence-gated writing
- [`scripts/test-onboarding.sh`](scripts/test-onboarding.sh): clean and repeated-install tests
- [`scripts/release-check.sh`](scripts/release-check.sh): public-release safety checks

## Origin And Lineage

FIRM began in 2025 as an attempt to make auto-research persist through real
projects, not just complete a benchmark loop. Early versions borrowed useful
execution ideas from [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep).
The project then diverged through repeated field use: research ownership,
program protection, constructive method lineage, evidence interpretation,
second-PI review, scope-debt control, paper-entry gating, and public release
safety were rebuilt across many versions.

FIRM is independent and unofficial. It is not maintained or endorsed by ARIS,
Anthropic, OpenAI, ACL, or ARR.

<details>
<summary><strong>Development field notes</strong></summary>

| Period | What broke | What changed in FIRM |
|---|---|---|
| **2025 H1** | Long agents could execute experiments but repeatedly returned ordinary decisions to the user | Added persistent first-author ownership and durable live state |
| **2025 H2** | Projects accumulated diagnostics while the method never formed | Made every probe pay rent through a concrete design consequence |
| **2026 Q1** | A failed realization closed a field, while broken designs triggered wasteful seed expansion | Separated failure levels and design uncertainty from statistical uncertainty |
| **2026 Q2** | Broad programs collapsed into private slices; failed methods became analysis fallbacks | Added value spine, scope debt, reintegration, and the analysis deletion test |
| **2026 Q2** | Strong controls and scorer bugs arrived after the paper identity had hardened | Moved fidelity and best-case prize review before major compute and writing |
| **2026 H1 external checkpoint** | Three human-verified papers entered real peer review | Nine official ACL ARR reviews returned mean overall assessments of **3.50**, **3.33**, and **3.17** |
| **2026-07-27** | Overlapping skills had become another source of agent confusion | Consolidated the system into one persistent researcher and 17 focused tools |

</details>

## Human Accountability

FIRM improves research judgment; it does not automate submission volume.
Researchers remain responsible for novelty, licenses, data provenance, compute,
authorship, citations, disclosure, claims, and the final decision to submit.
Peer review is not a unit-test endpoint. Every public result should survive
human reading and verification.

<details>
<summary><strong>中文简介</strong></summary>

FIRM 是面向 Claude Code 的研究判断层，并把 Codex 作为独立 second PI。
它解决的不是“如何多跑实验”，而是更昂贵的问题：如何避免宽泛且重要的
研究方向逐渐缩成无人关心的小切片，如何把方法失败变成下一版设计证据，
以及如何在论文真正成熟之前阻止过早写作。

这套系统来自超过 100B 模型 token 的长期实战迭代，并在三篇经过人工核实
的论文上经历了九份 ACL ARR 正式评审。公开分数仅作为真实研究使用记录，
不代表录用结果，也不声称能够单独证明 FIRM 的因果效果。

</details>

## License

FIRM is released under the [MIT License](LICENSE). Contributions should preserve
the project's core promise: better research decisions, inspectable evidence,
and human accountability.

<p align="center">
  <strong>Before your agent spends another week proving the wrong thing, give it FIRM.</strong>
</p>
