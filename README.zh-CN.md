<p align="center">
  <strong>FIRM</strong><br>
  <sub><strong>F</strong>ailure-<strong>I</strong>nformed <strong>R</strong>esearch for <strong>M</strong>achines</sub>
</p>

<h1 align="center">经过真实科研检验的端到端 CS Research Skills。</h1>

<p align="center">
  一个持续 GPT Research PI，加十五个有界 specialist workflows，<br>
  覆盖实现、实验、核验与论文生产。
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> ·
  <a href="#30-秒安装"><strong>安装</strong></a> ·
  <a href="#看见差异"><strong>看见差异</strong></a> ·
  <a href="#开发时间线"><strong>开发时间线</strong></a> ·
  <a href="#设计与文档"><strong>文档</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-plugin-D97757?style=flat-square" alt="Claude Code plugin">
  <img src="https://img.shields.io/badge/research_skills-6-285943?style=flat-square" alt="6 research skills">
  <img src="https://img.shields.io/badge/second_PI-independent-4C78A8?style=flat-square" alt="Independent second PI">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2f81f7?style=flat-square" alt="MIT License"></a>
</p>

---

## 核心定位

**FIRM** 的全称是 **Failure-Informed Research for Machines**。

AI Agent 很擅长制造“在推进”的感觉：搜索、代码、实验、图表和草稿。真正困难的是科研
判断。FIRM 帮助 Agent 判断什么值得研究、一个结果究竟意味着什么、下一版该构造什么，
以及证据何时真正足以支撑一篇论文。

现有的 `research-pipeline` skill 是 GPT 唯一持续科学负责人，覆盖文献、实验、解释、方法演化和
投稿；它的五份 focused references 只在当前不确定性需要时加载。其余 5 个 specialist tools
用于有界 Claude 实现和显式高级操作，不是并列 PI，也不会一次性装入 GPT 上下文。

端到端不等于静默消耗算力，也不等于按固定阶段一路推进。高影响操作仍然必须显式调用；
新证据可以让项目回到问题、基线或方法，而不是被流程强行推向论文。

## 看见差异

<p align="center">
  <img src="assets/firm-decision-demo.png" width="100%" alt="FIRM 将失败的方法结果转化为校准后的诊断和下一步设计实验">
</p>

面对同一个方法失败结果，没有 FIRM 的 Agent 可能直接关闭整个方向；FIRM 会把它转化为
对当前 realization 的构造性诊断。这个案例来自可运行的 [`demo/fixture`](demo/fixture)：
一次可信负结果可以否定当前实现，但不能据此杀死整个领域，也不能据此启动 seed sweep。
FIRM 保留有效证据，并选择真正能够改变设计判断的下一个实验。

```bash
make demo
```

该命令播放引导式终端故事板，不把预写内容伪装成模型评测。要用 Claude Code 运行中性
案例：

```bash
cd demo/fixture
claude
# 然后调用：/firm:method-development "解释 RESULT.md，再选择下一项构造"
```

## 目录

- [核心定位](#核心定位)
- [看见差异](#看见差异)
- [工作原理](#工作原理)
- [30 秒安装](#30-秒安装)
- [启动自己的端到端科研项目](#启动自己的端到端科研项目)
- [FIRM 能做什么](#firm-能做什么)
- [从任意节点进入](#从任意节点进入)
- [FIRM 解决的不是“不会做”，而是“判断错”](#firm-解决的不是不会做而是判断错)
- [一个 PI skill 与五个按需工具](#一个-pi-skill-与五个按需工具)
- [开发时间线](#开发时间线)
- [仓库结构](#仓库结构)
- [设计与文档](#设计与文档)

## 工作原理

```text
Prize -> Fidelity -> Design -> Evidence -> Entry
  ^                  新证据可以修改任何更早的判断                  |
  +---------------------------------------------------------------+
```

- **Prize：** 即使最理想结果成立，它对社区是否真正重要？
- **Fidelity：** 任务、基线、scorer、provenance 和成本是否可信？
- **Principle：** 证据支持替换领域中的哪个关键默认假设？
- **Design：** 哪个 load-bearing method primitive 真正从证据中推出？
- **Evidence：** 这次运行诊断了什么，哪些解释和方法仍然存活？
- **Expansion：** 一个由 artifacts 支撑的候选是否能长成可复用的研究计划，而不只是更大的结果表？
- **Entry：** 当前贡献是否成熟到可以进入完整论文写作？

在 explanatory pause 中，FIRM 会在正式投入方法前形成一个紧凑的问题模型：incumbent
为什么通常成功、哪个原本有用的假设在自然条件下失效、匹配成功与失败最早在哪里分叉、
什么证据与该解释矛盾，以及干预应改变什么并保留哪些普通能力。这是更深入的分析，不是
要求继续扩大 probe atlas。

`research-pipeline` 把持续掌舵和有界协作分开。GPT PI 持续负责综合、方法选择和投稿，
Claude 交付有界的实现与实验任务。独立 Codex 审查只稀疏地验证一个会改变当前决定的明确不确定性；
这不限制 GPT PI 自己持续推理。Gemini 是可选的创造型 co-PI，在充分经验
证据已经值得形成 v1、一次信息充分的失败需要真正不同的 v2 primitive，或一个由 artifacts
支撑的候选能够长成更大可复用思想时参与。主 PI 根据实时证据动态编写 Gemini prompt，再负责 collision
read、选择、实现和实验。两者都不是停止按钮，工具不可用也不会暂停研究。

Gemini 协作使用 Antigravity CLI（`agy`），属于可选能力。经过模型固定验证的标准调用只在
[`collaboration.md`](skills/research-pipeline/references/collaboration.md) 中维护；没有安装 `agy` 时，主 PI 仍继续推进，
独立 Codex 审查只在证据已经挣得的边界使用。

### 实际科研循环

<p align="center">
  <img src="assets/operational-research-loop.svg" width="100%" alt="FIRM 实际科研循环：Prize、Fidelity、Design、Experiment、Evidence 和 Entry，以及由证据驱动的反馈">
</p>

这是一个持续更新的科研循环，不是强制阶段机。一个持续 PI 始终维护原始研究计划、当前
论文、发现切片、方法谱系、scope debt、活动任务和下一步动作之间的一致性；Claude 与
Gemini 提供有界协作，连续性由 artifacts 而不是协作者叙述承载。

## 30 秒安装

要在 Trae 中使用持续 GPT PI，直接安装六个 FIRM skills，并把
[`TRAE-RESEARCH.md`](TRAE-RESEARCH.md) 作为模型指令。GPT PI 持续拥有完整项目，
在证据支持的发明节点调用 Gemini，把有界实现工作交给 Claude Code，并稀疏使用 Codex 独立核验：

```bash
git clone https://github.com/Zarien-Li/FIRM.git ~/FIRM
cd ~/FIRM
FIRM_HOST=trae ./install.sh
```

把 Trae 的 `model_instructions_file` 指向 `~/.trae/CLAUDE-RESEARCH.md`。Codex MCP、
`agy` 和 `claude` 是可选协作者；任一 provider 暂时不可用都不应暂停主 PI。

要在 Claude Code 中使用有界实现和 specialist workflows，执行：

```text
/plugin marketplace add Zarien-Li/FIRM
/plugin install firm@firm-research
/reload-plugins
```

安装后所有命令都位于 `/firm:` 命名空间，不会与其他插件的 skills 冲突。

要在支持 skills 的 GPT runtime 中快速体验：

```text
/firm:research-pipeline "作为持续的一作接管这个项目：保留重要问题，建立可信基线，记录每个结果，只在证据包能区分解释时更新理论，构造可复用 primitive，只在证据成熟时进入论文。"
```

`research-pipeline` 是持续 GPT 研究负责人，不是运行整套 skill 库的宏。它自己的 focused references
覆盖经验基础、方法成熟、执行、协作和投稿；specialist 只承担有界任务。

## 用一句组合需求生成项目

不需要手写每一份 Seed。只需向 Codex 提供目标刊物、大概方向、项目数量上限、算力范围、
特殊排除项和现有项目路径，并让它读取
[`research-foundation/project-generation.md`](skills/research-foundation/references/project-generation.md)，
调查当前官方 scope、近期完整论文和公开实现，再输出符合内置 schema 的 manifest。快速检查
排序后的候选后，渲染接受的项目：

```bash
node ~/FIRM/scripts/generate_seed_project_folders.mjs manifest.json /path/to/new-projects
```

生成器会为每个项目创建 `PROGRAM_ORIGIN.md`、`SEED.md`、`PROJECT_IDENTITY.json`、
`PROJECT_STATE.md`、`CLAUDE.md` 和 `prompt.txt`。它拒绝覆盖已有目录、脑补缺失科学字段、
复用已有项目编号、新建 benchmark 或要求新增人工标注。Codex 只选择值得进入的研究场域；
具体自然问题和方法由项目 Research PI 在真实经验接触后形成。

## 启动自己的端到端科研项目

对于长期严肃科研项目，推荐使用项目级安装，让 Research Program、首轮 Prompt 和 skills
跟随研究仓库一起保存。

### 1. 只需克隆一次 FIRM

```bash
git clone https://github.com/Zarien-Li/FIRM.git ~/FIRM
```

### 2. 初始化科研仓库

```bash
mkdir my-research-project
cd my-research-project
~/FIRM/firm init .
~/FIRM/firm doctor .
```

初始化器会保留已有 `CLAUDE.md`，并创建：

```text
my-research-project/
├── CLAUDE.md
├── .claude/skills/            # 6 个项目级 FIRM skills
└── .firm/
    ├── RESEARCH_PROGRAM.md
    ├── FIRST_MESSAGE_NEW.md
    └── FIRST_MESSAGE_AUDIT.md
```

### 3. 定义 Research Program Seed

填写 [`.firm/RESEARCH_PROGRAM.md`](templates/RESEARCH_PROGRAM.md)，在重要领域和价值
表面层面说明：

- 哪个结果真正有价值，谁会因此改变科学、工程或运营决策；
- 公认 benchmark、真实工作流、SOTA 和强基线；
- 价值指标、副作用、成本和安全指标；
- 算力、模型、数据与时间边界；
- 当前实验表面能够和不能够证明什么。

不要预先指定最终失败或方法。Seed 打开的是一个重要研究计划，具体问题和设计由后续证据
决定。

### 4. 启动持续一作会话

```bash
claude --append-system-prompt-file ~/FIRM/CLAUDE-RESEARCH.md
```

新研究计划可以直接使用
[`.firm/FIRST_MESSAGE_NEW.md`](templates/FIRST_MESSAGE_NEW.md)，或者调用：

```text
/research-pipeline "从 .firm/RESEARCH_PROGRAM.md 开始，建立最强的经验接触点，并执行当前最高价值的可逆动作。"
```

已有项目使用
[`.firm/FIRST_MESSAGE_AUDIT.md`](templates/FIRST_MESSAGE_AUDIT.md)，先重建原始计划、
证据、方法谱系、scope debt、活动任务、论文成熟度和一个下一步动作，再启动更多工作。

也可以随时输出两类 Prompt：

```bash
~/FIRM/firm prompt new
~/FIRM/firm prompt audit
```

### 5. 沿着证据继续推进

持续研究者负责推进文献、基线、方法构造、实验、结果诊断和论文决策，同时维护一个紧凑
项目状态。具有副作用的工作流仍然必须显式调用，因此 FIRM 不会静默消耗算力、检查远程
任务或重写论文。

## FIRM 能做什么

| Discover | Build | Finish |
|---|---|---|
| 复现强基线，检查自然成功、失败和矛盾案例 | 把负结果转化为构造性方法谱系；让 Claude 有界实现、Gemini 受邀发明 | 由持续 GPT PI 把研究成熟到投稿；独立 Codex 只解决一个明确不确定性或近终稿事实核验 |
| 在项目演化中持续保留原始研究计划和社区价值 | 区分实现、设计、优化、统计和迁移不确定性 | 让最终 claim 与控制实验、成本、局限、引用和原始产物保持一致 |

一个持续 GPT PI 负责整个研究计划。Specialist workflows 与协作模型是有界工具，不是刚性阶段机或额外科学负责人。

## 从任意节点进入

FIRM 可以从一个新方向、已有仓库、完成的结果、活动实验或论文草稿开始：

| 当前情况 | 直接入口 |
|---|---|
| 选择一个重要且可进入的研究领域 | `/firm:research-foundation [领域或约束]` |
| 启动或恢复完整研究计划 | `/firm:research-pipeline [目标或项目状态]` |
| 建立领域标准的可信基线 | `/firm:research-foundation [任务或 benchmark]` |
| 解释结果、发明或修复 primitive、规划决定性实验 | `/firm:method-development [证据、方法或当前问题]` |
| 注册、启动、恢复或监控实验 | `/firm:experiment-operations [run 或 campaign]` |
| 独立攻击一个关键科研决策 | `/firm:research-review [决策或证据包]` |
| 审计论文入口、写作、改进或转投 | `/firm:research-review`，然后 `/firm:paper-writing [论文目录]` |

涉及算力、远程系统、破坏性操作、整篇稿件或正式提交的能力，仍必须服从工具权限与项目
授权。科学上相关不等于获得不可逆操作权限。

## FIRM 解决的不是“不会做”，而是“判断错”

| 常见科研 Agent 失败 | FIRM 的处理方式 |
|---|---|
| 方法 v1 失败，于是宣布整个方向无效 | 在 run / realization / primitive / family 四个层级上校准结论 |
| 一个负结果后立刻扩十个 seeds | 先区分设计不确定性和统计不确定性 |
| 一个项目私有的小切片逐渐变成论文全部价值 | 分开维护原始研究计划、当前论文、发现切片和 scope debt |
| 方法失败后倒推包装成 analysis paper | 要求分析对象本身具有独立价值，而不是失败历史的副产品 |
| 每次都给用户十个下一步选项 | 按信息增益和研究价值选择一个最高价值动作 |
| 一个正结果立刻触发更多 seed 和数据集 | 先做 Program Expansion，只资助能增强中心原则的扩展 |
| 草稿越来越完整，反过来绑架后续实验 | 从原始结果、匹配基线和真实范围重建 claim |

FIRM 不是刚性阶段机。一个持续研究者负责整个研究计划，specialist skills 只在其能力
真正有用时进入。

### 三个核心思想

**失败层级。** 一次可信的负结果可以否定当前 realization，但不能自动否定 primitive、
方法家族或整个研究计划。

**构造性方法谱系。** 每一版方法都记录 causal bet、实际激活了什么、哪里失败、什么仍然
成立，以及下一版必须改变什么。

**论文与研究计划分离。** 原始研究计划、当前论文、发现切片和 scope debt 是四个不同
对象。一个狭窄结果不能只靠宽泛领域名称借来重要性。

**正向研究计划扩张。** 当一个真实方法首次成立后，lead PI 会判断其简单原则能否扩展成
可复用 primitive、监督或数据引擎、可预测的跨任务规律或系统能力。Probe budget 用来
验证 opening；paper budget 只集中给那些投入越大、中心科学贡献越强的想法。

## 一个 PI skill 与五个按需工具

`research-pipeline` 是 GPT 唯一持续 PI 入口；五个合并后的工具分别负责领域接触、方法形成、实验执行、独立核验和论文写作。合并前的完整细则仍保存在各工具按需加载的 references 中。

- **持续 PI：** `research-pipeline`
- **领域与证据基础：** `research-foundation`
- **解释、方法与实验设计：** `method-development`
- **实验注册、运行与监控：** `experiment-operations`
- **协作与核验：** `research-review`
- **写作、改进与转投：** `paper-writing`

当前职责边界见 [Research Skills Ownership Map](REFORM_MAP.md)。

## 开发时间线

FIRM 不是一次写完后发布的 prompt pack。下面每次主要修订都来自真实研究中反复出现的
Agent 失败模式。

| 时间 | 发生了什么 | 产品变化 |
|---|---|---|
| 2025 Q1 | 长期运行的 Agent 能执行工作，却反复把普通科研决策退回给用户 | FIRM 开始尝试让 AI Agent 承担持续一作式所有权 |
| 2025 Q2 | 会话连续性保留了文件，却没有保留一个研究方向为何重要 | 增加持久 Research Program、value spine、反面证据和一个选定的下一步动作 |
| 2025 H2 | ARIS 展示了持久执行、可移植 skills 和多 Agent 评审的有效基础 | 采用部分执行思想，并通过真实使用重建科研决策层 |
| 2026 Q1 | 一个 realization 失败会关闭整个方法家族，坏设计又会触发浪费性的 seed expansion | 区分 run、realization、primitive 和 family failure，把构造性重设计设为默认 |
| 2026 Q2 | 宽泛研究计划不断收缩成私有小切片，失败方法被重新包装成 analysis paper | 增加 scope debt、标准任务重新接入、positive-object test 和独立 paper entry |
| 2026-06 | 在连续版本下开发的三篇经人工核验论文进入外部评审 | 9 份 ACL ARR 官方评审给出的 mean overall assessment 分别为 3.50、3.33 和 3.17 |
| 2026-07-27 | 五个模型家族累计超过 100B model tokens，暴露出重复 Agent 失败与工作流重叠 | 将系统收敛为一个持续研究者和聚焦 specialist workflows |
| 2026-09 | 长上下文仍让多份“各自正确”的 skills 争夺科研所有权 | 将现有 `research-pipeline` 设为 GPT 唯一 PI 入口，把细节移到按需 references，并把 run 状态限制为纯机械事实 |

为了保护仍处于双盲流程中的工作，这里只公开聚合评审分数。它们不是录用决定，也不是
FIRM 因果效果的受控估计。所有计入的论文都经过人类作者阅读、核验和批准后才投稿。

## 仓库结构

```text
FIRM/
├── .claude-plugin/   # Claude Code 插件与 marketplace 清单
├── skills/           # 一个 GPT PI skill 与有界 specialist workflows
├── templates/        # 可选的项目级科研初始化模板
├── examples/         # 脱敏后的科研 Agent 失败案例
├── demo/             # 中性结果诊断 fixture 与演示脚本
├── docs/             # 架构、失败地图、入门和发布文档
├── scripts/          # 校验、onboarding 和 release checks
├── assets/           # README 与社交预览素材
├── firm              # 项目级 init、doctor、list 和 prompt 工具
└── install.sh        # 全局或项目级直接安装脚本
```

每个公开能力位于 `skills/<name>/SKILL.md`。详细流程和 schema 放在所属 skill 的
`references/` 中，避免把无关说明同时加载进运行上下文。

## 设计与文档

- [入门指南](docs/getting-started.md)
- [Research Skills Ownership Map](REFORM_MAP.md)
- [科研 Agent 失败地图](docs/failure-map.md)
- [三个脱敏案例](examples/README.md)
- [设计来源与演化](docs/origin-and-design.md)
- [Agent 与维护者指南](docs/agent-guide.md)
- [贡献指南](CONTRIBUTING.md)

## License

MIT。FIRM 不能替代研究者对创新性、数据、算力、作者署名、引用、披露、claim 和最终投稿
决定的责任。
