<p align="center">
  <img src="assets/firm-hero.png" width="100%" alt="Failed research branches converging into an evidence-guided trajectory">
</p>

<h1 align="center">FIRM</h1>

<p align="center">
  <strong>The PI layer your research agent is missing.</strong><br>
  Your agent can run experiments. FIRM stops it from confidently researching the wrong thing.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/field_tested-100B%2B_model_tokens-171717?style=flat-square" alt="100B+ model tokens">
  <img src="https://img.shields.io/badge/research_skills-17-1d4ed8?style=flat-square" alt="17 research skills">
  <img src="https://img.shields.io/badge/license-MIT-15803d?style=flat-square" alt="MIT License">
  <a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"><img src="https://img.shields.io/badge/lineage-ARIS-b91c1c?style=flat-square" alt="ARIS lineage"></a>
</p>

<p align="center">
  <a href="#start-in-5-minutes"><strong>Start in 5 minutes</strong></a>
  ·
  <a href="#three-real-failure-patterns"><strong>See the cases</strong></a>
  ·
  <a href="FAILURE_MAP.md"><strong>Open the failure map</strong></a>
  ·
  <a href="GETTING_STARTED.md"><strong>Full setup guide</strong></a>
</p>

<p align="center">
  <img src="assets/firm-field-tested.png" width="100%" alt="FIRM field record: 100B+ model tokens, 3 research papers, 9 official ARR reviews, and mean overall assessments of 3.50, 3.33, and 3.17">
</p>

<p align="center">
  <strong>Not a weekend prompt pack.</strong> FIRM was repeatedly rebuilt inside
  long-running research programs, then tested against the mistakes those programs actually made.
</p>

---

Most auto-research systems reward motion: more searches, more jobs, more files,
more prose. They do not reliably notice when the research itself has gone wrong.

FIRM installs the missing PI layer. It keeps the important seed visible,
forces failures to change the next design, brings in an independent model
before expensive commitments, and prevents a plausible narrative from becoming
a paper before the evidence is ready.

> **Installation takes one command. Recovering from a month of seed drift does not.**

If your agent only writes code, you do not need FIRM. If it decides **what to
test, what a failure means, and when a paper exists**, you do.

## Start In 5 Minutes

<p align="center">
  <img src="assets/firm-first-run.png" width="100%" alt="FIRM first run: attach to a project, define the research program, start Claude with a second PI, and receive one next action">
</p>

**1. Attach FIRM to a project**

```bash
git clone https://github.com/Zoiya-Li/FIRM.git ~/FIRM
chmod +x ~/FIRM/firm
~/FIRM/firm init ~/research/my-project
```

This installs project-local skills, preserves existing instructions, and creates
a research-program card plus two first-message templates.

**2. Define the program**

Complete `~/research/my-project/.firm/RESEARCH_PROGRAM.md`: field, accepted
benchmarks or real workflow, community value, strong baseline families, and
resource boundary. Do not preselect the final failure or method.

**3. Start the researcher**

```bash
cd ~/research/my-project
claude
```

| Your situation | First message |
|---|---|
| Starting a new field or program | Paste the contents of `.firm/FIRST_MESSAGE_NEW.md` |
| Auditing an existing project | Paste the contents of `.firm/FIRST_MESSAGE_AUDIT.md` |

The first useful output is not a paper. It is one evidence-backed research
state: original program, current method and paper identity, contrary evidence,
scope debt, constructive method lineage, and one next action.

For Codex second-PI setup, existing-project behavior, expected artifacts, and
troubleshooting, follow the [zero-to-first-decision guide](GETTING_STARTED.md).

## The Failures That Consume Weeks

| Pattern | Without FIRM | With FIRM |
|---|---|---|
| **Baseline shock** | A stronger baseline arrives late and resets the paper | Reproduce matched incumbents before the claim hardens |
| **Method panic** | One loss closes the family, or triggers a meaningless seed sweep | Separate design failure from statistical uncertainty and construct the next version |
| **Seed drift** | An important field becomes a clean result in a private cell | Track scope debt and require a path back to standard value |
| **Probe addiction** | Predicting the failure is mistaken for fixing it | Require every probe to change a method decision |
| **Paper theater** | Files and plots are counted as maturity | Audit raw evidence, contribution prize, and paper entry before full drafting |

These are recurring behaviors observed across live projects, not hypothetical
prompt mistakes. The full [failure map](FAILURE_MAP.md) connects each symptom
to its hidden confusion, scientific cost, and repair.

FIRM is cheapest before the wrong experiment, not after the wrong paper.

## Five Decisions Before Another Week Of Compute

<p align="center">
  <img src="assets/firm-five-decisions.png" width="100%" alt="Five FIRM research checkpoints: Prize, Fidelity, Design, Evidence, and Entry">
</p>

| Checkpoint | The question FIRM forces | What changes |
|---|---|---|
| **01 · PRIZE** | If everything works, will the community care? | Low-value private cells cannot borrow importance from the original seed |
| **02 · FIDELITY** | Is the current paper still solving the program we started? | Qualifiers become visible scope debt with an explicit repayment path |
| **03 · DESIGN** | Did the run fail, the realization fail, or the primitive fail? | The next experiment repairs a causal component instead of decorating v1 |
| **04 · EVIDENCE** | Do raw artifacts support the story under matched controls? | An independent second PI interprets, invents, and attacks before commitment |
| **05 · ENTRY** | Is there an earned positive object and decisive comparison? | Full manuscript work waits for `PAPER_ENTRY.md: PASS` |

## What Appears In Your Project

| Artifact | Why it matters |
|---|---|
| **One compact live state** | Keeps the original program, current paper, contrary evidence, scope debt, method lineage, active jobs, and one chosen next action together |
| **A constructive method lineage** | Records what activated, what failed, and what the next version must preserve or change |
| **Independent second-PI synthesis** | Challenges prize, fidelity, explanation, method design, and maturity before sunk cost takes over |
| **`CANDIDATE_CLAIM.md`** | Keeps the claim provisional while research is still changing |
| **`PAPER_ENTRY.md`** | Stops polished writing from outrunning the evidence |

One persistent `research-pipeline` owns the program. The other skills are
on-demand capabilities, not permission gates or a rigid state machine.

## Three Real Failure Patterns

| Case | What goes wrong | Corrective move |
|---|---|---|
| [A method loses once](examples/01-method-loss-is-not-field-loss.md) | One realization is confused with the field, while extra seeds cannot repair design | Preserve the program and form the next constructive ablation |
| [The paper drifts from the seed](examples/02-seed-drift.md) | A rigorous private cell replaces the important problem | Expose scope debt and require a reintegration path |
| [Writing starts too early](examples/03-paper-entry-audit.md) | Experimental volume is mistaken for contribution maturity | Run evidence integrity and independent paper-entry review |

The cases are sanitized composites distilled from recurring behavior in real
research programs. They are decision patterns, not claims that one prompt
guarantees a paper.

## Why 100B+ Tokens Matter

The scale is not decoration. It is the failure dataset behind FIRM. Across
long-running projects, we watched research agents close fields after one bad
realization, multiply seeds after a design failure, drift from important
programs into private cells, and write polished papers before checking decisive
controls. The skills were revised, merged, or deleted whenever those failures
showed that the system itself was teaching the wrong research behavior.

The total was accumulated primarily across five model families and 17 deployed
model or research-runtime configurations:

| Family | Models or configurations used in live research |
|---|---|
| **GLM** | `glm-4.7`, `glm-5.1`, `glm-5.2`, `glm-5.7` |
| **Kimi** | `kimi-k2.5`, `kimi-k2.6`, `kimi-k3` |
| **Claude** | `claude-opus-4.6`, `claude-opus-4.7`, `claude-opus-4.8`, and the `claude-fable-5` research configuration |
| **DeepSeek** | `deepseek-v4-pro` |
| **GPT** | `gpt-5.1`, `gpt-5.2`, `gpt-5.3`, `gpt-5.4`, `gpt-5.5` |

These labels describe the systems used in real sessions. The token total is not
an equal-allocation, head-to-head model benchmark, and no per-model performance
ranking is implied.

## External Review Record

Three papers developed under successive workflow versions received **nine
official ACL ARR reviews**, with mean overall assessments of **3.50**,
**3.33**, and **3.17**.

We report only the aggregate score record. Paper identities, submission
metadata, reviewer identifiers, review text, and dashboard screenshots remain
private while the work may still participate in anonymous review. The scores
show that successive workflow versions were used to produce serious research;
they are not an acceptance claim or a controlled estimate of FIRM's causal
effect.

## Skill System

| Research responsibility | Skills |
|---|---|
| Own the program | `research-pipeline` |
| Establish empirical contact | `frontier-direction-discovery`, `research-lit`, `baseline`, `signal-analysis` |
| Form and test methods | `method-primitive-synthesis`, `experiment-plan`, `research-contract`, `run-experiment`, `monitor-experiment` |
| Review evidence and claims | `research-review`, `experiment-audit`, `research-state-audit`, `citation-audit` |
| Write and improve the paper | `paper-writing`, `paper-figure`, `auto-paper-improvement-loop` |

See [the complete skill index](skills/INDEX.md) for activation guidance and
shared references.

The suite is primarily tested with Claude Code's `SKILL.md` format. The
Markdown workflows can be adapted to Codex and other agent runtimes by mapping
tool names to their equivalents.

## Origin And Lineage

FIRM began in 2025 as an attempt to make auto-research persist through real
scientific uncertainty rather than merely complete a workflow. Selected
foundations were adapted from
[ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep),
including portable Markdown skills, persistent artifacts, and cross-model
review. Later versions were repeatedly restructured through live research.

FIRM is independent and unofficial. It is not maintained or endorsed by the
ARIS authors. Attribution is preserved in [NOTICE](NOTICE).

Read the [long-form origin, design rationale, evidence, and ARIS
relationship](docs/ORIGIN_AND_DESIGN.md).

## Field Notes

This is the development log that matters: not every new feature, but the moments
when live research forced us to reject part of our own operating model.

| Period | Major turn |
|---|---|
| **2025 · Original thesis** | We learned that keeping an agent running is easier than keeping it scientifically responsible. The goal changed from an autonomous loop to a persistent first author grounded in durable evidence. |
| **2025–early 2026 · Workflow foundation** | Portable skills, artifacts, and cross-model review made long research possible. Selected ARIS foundations became the starting scaffold, not a permanent architecture. |
| **2026 H1 · State-machine break** | The early S0–S6 state machine, kill ledgers, and cheap-falsifier gates made agents obey workflow verdicts instead of reinterpreting science. Permanent terminal labels and stage permissions were deleted. |
| **2026 H1 · Method-formation break** | One failed realization was closing whole method families, while competent negative designs triggered wasteful seed expansion. FIRM separated run, realization, primitive, and family failure, then made constructive redesign the default response to design evidence. |
| **2026 H1 · Value and scope break** | Broad programs kept shrinking into private cells, and failed methods were being repackaged as analysis papers. Program/paper separation, value spine, scope debt, reintegration, and the analysis-paper deletion test were introduced. |
| **2026 H1 · Evidence and harvest break** | Baseline, scorer, provenance, and control failures arrived after drafts hardened, while moving standards kept mature work unfinished. Evidence integrity moved earlier; candidate claims and independent paper entry made finishing part of research. |
| **2026 H1 · Second-PI break** | Codex was being used late as a stop judge, and MCP outages were allowed to pause research. Review moved upstream into `Prize/Fidelity → Interpret → Invent → Attack → Decide`; infrastructure failure lost scientific authority. |
| **2026 H1 · External checkpoint** | Three human-verified papers developed under successive versions received nine official ACL ARR reviews, with mean overall assessments of **3.50**, **3.33**, and **3.17**. Only aggregate scores are public. |
| **2026-07-27 · Consolidation** | After more than **100B model tokens** across five model families and 17 deployed configurations, overlapping skills and audits were reduced to one persistent researcher, 17 focused tools, a failure map, project onboarding, and a tested first-run path. |

### Human Accountability

FIRM is designed to improve research judgment, not automate submission volume
or use peer review as a debugging endpoint. Every paper included in the review
record was manually checked by a human author before submission. Human authors
reviewed the final manuscript, its claims, supporting evidence and provenance,
citations, and the decision to submit. Nothing was submitted automatically;
scientific and publication responsibility remained with the authors.

<details>
<summary><strong>中文简介</strong></summary>

大多数 auto-research 项目优化的是一次实验闭环。FIRM
关注的是机器如何在许多轮失败、反常结果和方法重构中保持研究判断。

它不是保证论文产出的固定流程，而是一组经过长期真实研究反复修改的
skills：防止重要 seed 漂移成无人关心的小问题，区分设计失败与统计不确定性，
让 probe 服务于方法设计，在写作前完成证据审计，并在贡献成熟时及时收获。

FIRM 不把同行评审当作自动化测试集。计入上述评审记录的每篇论文都由人类作者
在投稿前核对最终稿、研究主张、支撑证据及其来源、引用和投稿决定；没有论文被
Agent 自动提交，科研与发表责任始终由作者承担。

</details>

## License

FIRM is released under the [MIT License](LICENSE). Selected lineage from ARIS
is credited in [NOTICE](NOTICE).

<p align="center">
  <strong>Before your agent spends another week proving the wrong thing, give it FIRM.</strong>
</p>
