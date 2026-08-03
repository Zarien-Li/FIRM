<p align="center">
  <strong>FIRM</strong><br>
  <sub>CS Research Skills for AI Agents</sub>
</p>

<h1 align="center">Field-tested CS research skills for AI agents.</h1>

<p align="center">
  Seventeen skills for problem discovery, method formation, experiments,<br>
  independent second-PI review, and evidence-grounded paper writing.
</p>

<p align="center">
  <a href="#install"><strong>Install</strong></a> ·
  <a href="#see-the-difference">See the difference</a> ·
  <a href="#development-timeline">Development timeline</a> ·
  <a href="docs/getting-started.md">Documentation</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/research_skills-17-285943?style=flat-square" alt="17 research skills">
  <img src="https://img.shields.io/badge/primary_runtime-Claude_Code-D97757?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/second_PI-Codex-111318?style=flat-square" alt="Codex second PI">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2f81f7?style=flat-square" alt="MIT License"></a>
</p>

---

AI agents are good at producing motion: searches, code, experiments, plots, and
drafts. The harder problem is research judgment. FIRM helps an agent decide
**what is worth studying, what a result actually means, what to build next, and
when the evidence has earned a paper**.

## See The Difference

<p align="center">
  <img src="assets/firm-decision-demo.png" width="100%" alt="The same failed method result produces a field-closure decision without FIRM and a constructive design diagnosis with FIRM">
</p>

The example uses the runnable [`demo/fixture`](demo/fixture). One competent
negative run diagnoses the current realization. It does not justify killing the
field, and it does not justify a seed sweep. FIRM preserves the valid evidence
and chooses the next experiment that can change the design.

```bash
make demo
```

## Install

Run this inside a new or existing research project:

```bash
git clone https://github.com/Zarien-Li/FIRM.git ~/FIRM && ~/FIRM/firm init .
```

Then start Claude Code normally:

```bash
claude --append-system-prompt-file CLAUDE-RESEARCH.md
```

`firm init` preserves an existing `CLAUDE.md`, installs project-local skills,
installs the public [`CLAUDE-RESEARCH.md`](CLAUDE-RESEARCH.md) system-prompt
addendum, and creates a research-program card plus first-message templates.
Verify the installation with `~/FIRM/firm doctor .`. See the
[getting-started guide](docs/getting-started.md) for global, project-local, and
dry-run installation.

## What FIRM Does

| Discover | Build | Finish |
|---|---|---|
| Reproduce strong baselines and inspect natural successes, failures, and contradictions | Turn negative results into a constructive method lineage instead of premature closure or random seed expansion | Use an independent second PI to audit prize, fidelity, evidence, scope, and paper readiness |
| Keep the original research program and community value visible as the project evolves | Distinguish implementation, design, optimization, statistical, and transfer uncertainty | Align the final claim with controls, costs, limitations, citations, and raw artifacts |

One persistent `research-pipeline` owns the program. Specialist skills are
loaded only when their capability is needed; they are tools, not a rigid stage
machine. Read the complete [skills index](skills/INDEX.md).

## How It Works

```text
Prize -> Fidelity -> Design -> Evidence -> Entry
  ^          evidence can revise any earlier decision          |
  +-------------------------------------------------------------+
```

- **Prize:** Would the best-case result matter to the community?
- **Fidelity:** Are the task, baseline, scorer, provenance, and costs real?
- **Design:** What load-bearing method primitive follows from the evidence?
- **Evidence:** What did the run diagnose, and what remains alive?
- **Entry:** Is the contribution mature enough for full paper writing?

Codex serves as an independent second PI at consequential boundaries. It helps
reinterpret evidence, invent alternatives, and attack the strongest claim; it
does not act as a stop-button oracle, and an unavailable reviewer does not pause
the lead researcher's work.

## Development Timeline

FIRM was not written once and published as a prompt pack. Each major revision
below followed a recurring failure observed in live research.

| Time | What happened | Product change |
|---|---|---|
| **2025 Q1** | Long-running agents could execute work but repeatedly returned ordinary research decisions to the user | FIRM began as an attempt to give AI agents persistent first-author ownership |
| **2025 Q2** | Session continuity preserved files but not the reason a research direction mattered | Added a durable research program, value spine, contrary evidence, and one chosen next action |
| **2025 H2** | ARIS demonstrated useful foundations for persistent execution, portable skills, and multi-agent review | Adopted selected execution ideas, then began rebuilding the research-decision layer through field use |
| **2026 Q1** | One failed realization closed whole method families, while broken designs triggered wasteful seed expansion | Separated run, realization, primitive, and family failure; made constructive redesign the default |
| **2026 Q2** | Broad programs shrank into private cells, and failed methods were repackaged as analysis papers | Added scope debt, standard-task reintegration, positive-object tests, and independent paper entry |
| **2026-06** | Three human-verified papers developed under successive versions entered external review | Nine official ACL ARR reviews returned mean overall assessments of **3.50**, **3.33**, and **3.17** |
| **2026-07-27** | More than **100B model tokens** across five model families exposed repeated agent failure modes and overlapping workflow rules | Consolidated the system into one persistent researcher and 17 focused skills |

Only aggregate review scores are public to protect active double-blind work.
They are not acceptance decisions or a controlled estimate of FIRM's causal
effect. Every counted paper was read, checked, and approved by human authors
before submission.

FIRM is independent and unofficial. It is not maintained or endorsed by ARIS,
Anthropic, OpenAI, ACL, or ARR. Read the full
[origin and design history](docs/origin-and-design.md) and [NOTICE](NOTICE).

## Explore The System

- [Three sanitized field cases](examples/README.md)
- [Research-agent failure map](docs/failure-map.md)
- [Complete skills index](skills/INDEX.md)
- [Long-form origin and ARIS lineage](docs/origin-and-design.md)
- [Onboarding test](scripts/test-onboarding.sh)

<details>
<summary><strong>中文简介</strong></summary>

FIRM 是面向 AI Agent 的计算机科学研究 skills。它让 Agent 不只会搜索、
写代码和跑实验，还能持续判断问题是否重要、失败意味着什么、下一版方法应该
改哪里，以及现有证据是否已经足以进入论文写作。它来自长期真实研究迭代，
而不是一次性编写的 prompt 集合。

</details>

## License

FIRM is released under the [MIT License](LICENSE). Researchers remain
responsible for novelty, data, compute, authorship, citations, disclosure,
claims, and the final decision to submit.

<p align="center">
  <strong>Less wandering. Better research decisions.</strong>
</p>
