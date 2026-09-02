#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { buildProjectContract } from "./lib/project-contract.mjs";

const manifestPath = process.argv[2];
const outputRoot = process.argv[3];

if (!manifestPath || !outputRoot) {
  throw new Error("usage: node scripts/generate_seed_project_folders.mjs <project-generation-manifest.json> <new-output-root>");
}
if (fs.existsSync(outputRoot)) {
  throw new Error(`refusing to overwrite existing output root: ${outputRoot}`);
}

const manifestText = fs.readFileSync(manifestPath, "utf8");
const manifest = JSON.parse(manifestText);
const manifestHash = crypto.createHash("sha256").update(manifestText).digest("hex");
const standingPortfolioExclusions = [
  "new benchmark construction",
  "new human annotation, preference, rating, or judgment collection",
];

function requireObject(value, label) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new Error(`${label} must be an object`);
  }
  return value;
}

function requireString(value, label) {
  if (typeof value !== "string" || !value.trim()) throw new Error(`${label} must be a non-empty string`);
  return value.trim();
}

function requireArray(value, label, minimum = 0) {
  if (!Array.isArray(value) || value.length < minimum) {
    throw new Error(`${label} must be an array with at least ${minimum} item(s)`);
  }
  return value;
}

function requireUrl(value, label) {
  const text = requireString(value, label);
  let parsed;
  try {
    parsed = new URL(text);
  } catch {
    throw new Error(`${label} must be an absolute URL`);
  }
  if (!new Set(["http:", "https:"]).has(parsed.protocol)) throw new Error(`${label} must use http or https`);
  return text;
}

function checkAllowedKeys(object, allowed, label) {
  const unknown = Object.keys(object).filter((key) => !allowed.includes(key));
  if (unknown.length) throw new Error(`${label} has unknown field(s): ${unknown.join(", ")}`);
}

function validatePublishedMethod(method, label) {
  const object = requireObject(method, label);
  checkAllowedKeys(object, ["name", "paperUrl", "codeUrl", "protocol", "whyDecisive"], label);
  return {
    name: requireString(object.name, `${label}.name`),
    paperUrl: requireUrl(object.paperUrl, `${label}.paperUrl`),
    codeUrl: object.codeUrl === null || object.codeUrl === undefined ? null : requireUrl(object.codeUrl, `${label}.codeUrl`),
    protocol: requireString(object.protocol, `${label}.protocol`),
    whyDecisive: requireString(object.whyDecisive, `${label}.whyDecisive`),
  };
}

function validateProject(project, index, request) {
  const label = `projects[${index}]`;
  const object = requireObject(project, label);
  const allowed = [
    "id", "title", "targetVenue", "researchArena", "canonicalObject", "primaryOutcome",
    "standardEvidenceSurface", "publishedMethodBaselines", "substrateControls", "whyNow",
    "communityPrize", "citationSurface", "nonBindingLens", "deploymentBoundary",
    "computeEnvelope", "outsideScope", "firstEmpiricalContact", "selectionSources",
  ];
  checkAllowedKeys(object, allowed, label);

  const id = requireString(object.id, `${label}.id`);
  if (!/^[A-Z][A-Z0-9_]{1,20}$/.test(id)) throw new Error(`${label}.id must match ^[A-Z][A-Z0-9_]{1,20}$`);
  const targetVenue = requireString(object.targetVenue, `${label}.targetVenue`);
  if (!request.targetVenues.includes(targetVenue)) {
    throw new Error(`${label}.targetVenue is not present in request.targetVenues`);
  }

  const surface = requireObject(object.standardEvidenceSurface, `${label}.standardEvidenceSurface`);
  checkAllowedKeys(surface, ["name", "protocol", "whyCanonical", "sources"], `${label}.standardEvidenceSurface`);
  const surfaceSources = requireArray(surface.sources, `${label}.standardEvidenceSurface.sources`, 1)
    .map((url, sourceIndex) => requireUrl(url, `${label}.standardEvidenceSurface.sources[${sourceIndex}]`));

  const baselines = requireObject(object.publishedMethodBaselines, `${label}.publishedMethodBaselines`);
  checkAllowedKeys(baselines, ["strongIncumbent", "nearestRival", "additional"], `${label}.publishedMethodBaselines`);
  const strongIncumbent = validatePublishedMethod(baselines.strongIncumbent, `${label}.publishedMethodBaselines.strongIncumbent`);
  const nearestRival = validatePublishedMethod(baselines.nearestRival, `${label}.publishedMethodBaselines.nearestRival`);
  if (strongIncumbent.name === nearestRival.name) {
    throw new Error(`${label} must identify distinct strongIncumbent and nearestRival methods`);
  }
  const additional = requireArray(baselines.additional, `${label}.publishedMethodBaselines.additional`)
    .map((method, methodIndex) => validatePublishedMethod(method, `${label}.publishedMethodBaselines.additional[${methodIndex}]`));

  const selectionSources = requireArray(object.selectionSources, `${label}.selectionSources`, 2)
    .map((url, sourceIndex) => requireUrl(url, `${label}.selectionSources[${sourceIndex}]`));
  for (const method of [strongIncumbent, nearestRival]) {
    if (!selectionSources.includes(method.paperUrl)) {
      throw new Error(`${label}.selectionSources must include the paper URL for ${method.name}`);
    }
  }

  return {
    id,
    title: requireString(object.title, `${label}.title`),
    targetVenue,
    researchArena: requireString(object.researchArena, `${label}.researchArena`),
    canonicalObject: requireString(object.canonicalObject, `${label}.canonicalObject`),
    primaryOutcome: requireString(object.primaryOutcome, `${label}.primaryOutcome`),
    standardEvidenceSurface: {
      name: requireString(surface.name, `${label}.standardEvidenceSurface.name`),
      protocol: requireString(surface.protocol, `${label}.standardEvidenceSurface.protocol`),
      whyCanonical: requireString(surface.whyCanonical, `${label}.standardEvidenceSurface.whyCanonical`),
      sources: surfaceSources,
    },
    publishedMethodBaselines: { strongIncumbent, nearestRival, additional },
    substrateControls: requireArray(object.substrateControls, `${label}.substrateControls`, 1)
      .map((item, itemIndex) => requireString(item, `${label}.substrateControls[${itemIndex}]`)),
    whyNow: requireString(object.whyNow, `${label}.whyNow`),
    communityPrize: requireString(object.communityPrize, `${label}.communityPrize`),
    citationSurface: requireString(object.citationSurface, `${label}.citationSurface`),
    nonBindingLens: requireString(object.nonBindingLens, `${label}.nonBindingLens`),
    deploymentBoundary: requireString(object.deploymentBoundary, `${label}.deploymentBoundary`),
    computeEnvelope: requireString(object.computeEnvelope, `${label}.computeEnvelope`),
    outsideScope: [...new Set([
      ...requireArray(object.outsideScope, `${label}.outsideScope`, 1)
        .map((item, itemIndex) => requireString(item, `${label}.outsideScope[${itemIndex}]`)),
      ...standingPortfolioExclusions,
    ])],
    firstEmpiricalContact: requireString(object.firstEmpiricalContact, `${label}.firstEmpiricalContact`),
    selectionSources,
  };
}

function validateManifest(input) {
  const object = requireObject(input, "manifest");
  checkAllowedKeys(object, ["schemaVersion", "request", "researchSources", "projects"], "manifest");
  if (object.schemaVersion !== 2) throw new Error("manifest.schemaVersion must be 2");

  const requestInput = requireObject(object.request, "request");
  checkAllowedKeys(requestInput, ["userBrief", "targetVenues", "broadDirections", "maximumProjects", "computeEnvelope", "exclusions", "venueScopeSources", "existingPortfolioRoot"], "request");
  const maximumProjects = Number(requestInput.maximumProjects);
  if (!Number.isInteger(maximumProjects) || maximumProjects < 1 || maximumProjects > 20) {
    throw new Error("request.maximumProjects must be an integer between 1 and 20");
  }
  const request = {
    userBrief: requireString(requestInput.userBrief, "request.userBrief"),
    targetVenues: requireArray(requestInput.targetVenues, "request.targetVenues", 1)
      .map((item, index) => requireString(item, `request.targetVenues[${index}]`)),
    broadDirections: requireArray(requestInput.broadDirections, "request.broadDirections", 1)
      .map((item, index) => requireString(item, `request.broadDirections[${index}]`)),
    maximumProjects,
    computeEnvelope: requireString(requestInput.computeEnvelope, "request.computeEnvelope"),
    exclusions: requireArray(requestInput.exclusions, "request.exclusions")
      .map((item, index) => requireString(item, `request.exclusions[${index}]`)),
    venueScopeSources: requireArray(requestInput.venueScopeSources, "request.venueScopeSources", 1)
      .map((url, index) => requireUrl(url, `request.venueScopeSources[${index}]`)),
    existingPortfolioRoot: requireString(requestInput.existingPortfolioRoot, "request.existingPortfolioRoot"),
  };

  const researchSources = requireArray(object.researchSources, "researchSources", 3).map((source, index) => {
    const label = `researchSources[${index}]`;
    const item = requireObject(source, label);
    checkAllowedKeys(item, ["kind", "title", "url", "relevance"], label);
    const kind = requireString(item.kind, `${label}.kind`);
    if (!new Set(["official-venue", "paper", "code", "benchmark", "model"]).has(kind)) {
      throw new Error(`${label}.kind is invalid`);
    }
    return {
      kind,
      title: requireString(item.title, `${label}.title`),
      url: requireUrl(item.url, `${label}.url`),
      relevance: requireString(item.relevance, `${label}.relevance`),
    };
  });
  if (!researchSources.some((source) => source.kind === "paper")) {
    throw new Error("researchSources must include at least one primary paper");
  }

  const projectInputs = requireArray(object.projects, "projects", 1);
  if (projectInputs.length > request.maximumProjects) {
    throw new Error(`projects contains ${projectInputs.length} entries but maximumProjects is ${request.maximumProjects}`);
  }
  const projects = projectInputs.map((project, index) => validateProject(project, index, request));
  const ids = new Set(projects.map((project) => project.id));
  if (ids.size !== projects.length) throw new Error("project IDs must be unique");
  for (const project of projects) {
    if (fs.existsSync(path.join(request.existingPortfolioRoot, project.id))) {
      throw new Error(`project ID already exists in the portfolio: ${project.id}`);
    }
  }

  return { schemaVersion: 2, request, researchSources, projects };
}

function slugify(value) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 72);
}

function baselineList(project) {
  return [
    project.publishedMethodBaselines.strongIncumbent,
    project.publishedMethodBaselines.nearestRival,
    ...project.publishedMethodBaselines.additional,
  ];
}

function renderSources(urls) {
  return urls.map((url) => `- ${url}`).join("\n");
}

function buildProgramOrigin(project, request) {
  const methods = baselineList(project);
  return `# Program Origin: ${project.title}

## Authority Status

- **Status:** accepted project-generation arena lock.
- **Origin ID:** \`${project.id.toLowerCase()}-${slugify(project.title)}-${new Date().toISOString().slice(0, 10).replaceAll("-", "")}\`.
- **User brief:** ${request.userBrief}
- **Generation manifest SHA-256:** \`${manifestHash}\`.

## Authorized Program

- **Target venue:** ${project.targetVenue}
- **Research arena:** ${project.researchArena}
- **Canonical object:** ${project.canonicalObject}
- **Single primary outcome:** ${project.primaryOutcome}
- **Standard evidence surface:** ${project.standardEvidenceSurface.name}; ${project.standardEvidenceSurface.protocol}
- **Deployment boundary:** ${project.deploymentBoundary}
- **Compute envelope:** ${project.computeEnvelope}

## Published-Method Contact

- **Strong incumbent:** ${methods[0].name} — ${methods[0].paperUrl}
- **Nearest claim-threatening rival:** ${methods[1].name} — ${methods[1].paperUrl}
- **Substrate and attribution controls:** ${project.substrateControls.join("; ")}

## Selection Rationale

The following is an evidence-grounded generation interpretation, not an established failure or paper thesis.

- **Why now:** ${project.whyNow}
- **Community prize:** ${project.communityPrize}
- **Potential citation surface:** ${project.citationSurface}
- **Non-binding lens:** ${project.nonBindingLens}

## Boundaries

Outside this project: ${project.outsideScope.join("; ")}.

No failure, causal explanation, method, result, or paper identity is authorized in advance. Diagnostic evidence remains instrumental until it reintegrates into the canonical object with deployment-available information and changes the primary outcome.

## Primary Sources

${renderSources(project.selectionSources)}
`;
}

function buildSeed(project) {
  const methods = baselineList(project);
  return `# ${project.id} Research Seed: ${project.title}

Status: generated from a current primary-source project-selection manifest. \`PROGRAM_ORIGIN.md\` preserves the accepted arena; the specific failure, explanation, method, and paper remain open.

## Arena And Value

- **Target venue:** ${project.targetVenue}
- **Research arena:** ${project.researchArena}
- **Canonical object:** ${project.canonicalObject}
- **Single primary outcome:** ${project.primaryOutcome}
- **Why this could matter:** ${project.communityPrize}
- **Potential citation surface:** ${project.citationSurface}

## Empirical Surface

- **Accepted surface:** ${project.standardEvidenceSurface.name}
- **Protocol:** ${project.standardEvidenceSurface.protocol}
- **Why it instantiates the object:** ${project.standardEvidenceSurface.whyCanonical}
- **Strong published-method incumbent:** ${methods[0].name} (${methods[0].paperUrl})
- **Nearest claim-threatening published rival:** ${methods[1].name} (${methods[1].paperUrl})
- **Backbone/substrate and attribution controls:** ${project.substrateControls.join("; ")}
- **Deployment information boundary:** ${project.deploymentBoundary}

## Discovery Freedom

- **Non-binding lens:** ${project.nonBindingLens}
- **First empirical contact:** ${project.firstEmpiricalContact}

The lens is not a pre-approved failure or solution. Read natural successes, failures, disagreements, and inconvenient cases on the full accepted population before choosing a problem model or load-bearing primitive. Oracle, synthetic, clean-subset, privileged-label, and proxy evidence remains diagnostic until a deployable realization returns to the canonical object.

## Constraints

- **Compute envelope:** ${project.computeEnvelope}
- **Outside this project:** ${project.outsideScope.join("; ")}
`;
}

function buildPrompt(project) {
  const methods = baselineList(project);
  const additionalMethods = methods.slice(2).map((method) => method.name).join("、") || "暂无预先指定的其他方法";
  return `# ${project.id} 研究委托：${project.title}\n\n你是这个项目持续负责的第一作者和 Research PI。这里给你的不是一条待执行的实验流水线，而是一项需要你真正理解、判断、发明和完成的研究委托。你的责任是让项目最终形成对 ${project.targetVenue} 社区有意义、证据可靠、能够被人自然讲清楚的贡献；具体问题、解释、方法和研究顺序必须由真实证据形成。\n\n## 这个项目为什么存在\n\n用户授权的研究场域是：${project.researchArena}\n\n社区正在处理的 canonical object 是：${project.canonicalObject}\n\n最重要的价值结果是：${project.primaryOutcome}\n\n现在值得研究它，是因为：${project.whyNow}\n\n如果项目成功，真正的 community prize 是：${project.communityPrize}\n\n它潜在的 citation surface 是：${project.citationSurface}\n\n方法在真实决策时只能使用以下信息：${project.deploymentBoundary}\n\n可用资源边界是：${project.computeEnvelope}\n\n## 项目生成时看到的研究地图\n\n当前被认为最自然的经验入口是 ${project.standardEvidenceSurface.name}。它的标准协议是：${project.standardEvidenceSurface.protocol}。它之所以可能代表这个研究对象，是因为：${project.standardEvidenceSurface.whyCanonical}\n\n生成阶段识别出的强 incumbent 是 ${methods[0].name}：${methods[0].whyDecisive}\n\n最近的 claim-threatening rival 是 ${methods[1].name}：${methods[1].whyDecisive}\n\n其他值得知道的已发表方法包括：${additionalMethods}\n\n可用于理解 substrate 和归因、但不能冒充论文方法 baseline 的对象包括：${project.substrateControls.join("；")}\n\n生成阶段提出的一个非约束性观察角度是：${project.nonBindingLens}\n\n生成阶段建议的首次经验接触是：${project.firstEmpiricalContact}\n\n以上内容是经过文献调研形成的起始地图，不是已经成立的 failure、因果解释、方法假设或强制实验顺序。你应检查这些入口是否忠实、是否仍然代表最重要的问题。若新证据说明另一种比较、surface、顺序或问题解释更有信息价值，你可以自行改变当前路线；但要在 \`PROJECT_STATE.md\` 中说明什么证据改变了判断，并保持与上面的研究场域和价值目标相连。\n\n## 你的研究职责\n\n开始前，完整读取 \`CLAUDE.md\`、\`PROGRAM_ORIGIN.md\`、\`PROJECT_IDENTITY.json\`、\`SEED.md\`、唯一当前状态 \`PROJECT_STATE.md\`、\`~/.claude/CLAUDE-RESEARCH.md\`，以及当前工作真正需要的 research skills。先形成你自己对项目价值、现有知识和最大不确定性的理解，再决定第一项工作；不要因为 prompt 提到了某个实验就机械执行。\n\n你需要持续承担完整研究责任：与近期已发表方法建立可信经验接触；阅读自然成功、失败、分歧和反常案例；把问题分析到足以改变设计；提出并真实实现有承重作用的贡献；从每次实现中学习并建设性地修改；完成与实际 claim 相匹配的比较、消融、效用和代价证据；在研究对象成熟时写成面向人类读者的论文。它们是你需要最终覆盖的研究责任，不是必须依次通过的阶段状态。\n\n不要把项目生成器的 lens、某篇论文的 framing、一个方便的 slice、旧会话结论或第一次实现变成永久路线。也不要为了显得开放而无目的地扩展模型、数据集或实验。研究自由意味着根据证据选择最能改变理解或设计的行动，并在一个方向获得信息后真正更新思考。\n\n持续维护 \`PROJECT_STATE.md\`，让用户能够知道项目在研究什么、最强证据与反证是什么、当前解释和贡献是否成立、真正的问题在哪里，以及下一步为何值得做。它是可修正的科学叙述，不是任务清单、审批表或命令日志。已验证事实具有证据权威；你写入的 gate、阈值、hold、路线和 next action 仍是可修正的解释，除非逐字引用用户或安全来源。实验注册只冻结一次 run。\n\n可信正对象形成后，保持一个 active paper candidate 和一条由同一原理预测的 expansion campaign。若一个 method-owned 前置条件在 primary outcome 之前失败，先在已有 accepted surface 上诊断或修复构造；不要把它算作 transfer 失败，也不要连续寻找更容易满足同一协议的数据集。若 method、paper-entry、draft 与 state 指向不同论文身份，先统一当前正对象再增加 breadth。\n\n普通、可逆的研究判断由你自主决定。只有改变用户授权的研究场域、使用异常资源或权限、执行不可逆或对外动作、遇到无法消解的权威冲突，以及最终投稿签字时才交还用户。Gemini 和 Codex 都是按需合作的 co-PI；它们可以拓展或攻击你的思考，但不能替代你的 ownership。GPU 与服务器操作遵循本项目 \`CLAUDE.md\`。\n\n现在先读项目权威与已有证据，写出你对这个具体项目的独立理解，然后选择最有研究价值的第一项行动并开始推进。\n`;
}

function buildEpisodeDirective(project) {
  return `
## 当前研究 episode 的维护方式

不要用固定阶段编号描述进度。持续只维护一个 active research episode：自然问题、暂定原理、承重计算位置、功能与机制上的已发表强对手、区分性预测、基质忠实度、最新证据和下一构造。v2/v3 只有在继承同一原理，并明确上一预测哪里失败、证据要求改变哪个组件、保留什么有效行为、产生什么新预测时，才能继承之前的成熟度；否则应诚实开启新 episode，而不是用新缩写掩盖方法轮盘。

Claim-bearing 研究必须忠实于本项目 seed 的任务、模型规模、训练方式、信息边界和算力范围（${project.computeEnvelope}）。便宜 proxy 只有在证明 incumbent 现象与 rival 排序仍成立后才能承载主张。若动机中的 incumbent 效应只因模型或任务被缩小而消失，不要围绕这个 proxy 异常发明论文方法，应回到忠实基质。

等待 GPU 是运行事实，不是新的科学阶段。完成真正有用且互不依赖的准备后，保持所选实验稳定；不要用重复审计、hash、checklist、方法菜单或备用 packet 代替运行。

项目的完成目标是等待用户最终事实、作者和上传确认的投稿包，不是第一版完整稿或第一次编译成功。把第一版稿当作科学集成测试：若它暴露承重 baseline、evaluator、method identity、transfer、utility 或 cost 缺口，继续完成对应研究并重写依赖内容；若新增工作只会形成防御性 breadth 或装饰表格，则及时收口。
`;
}

function buildIdentity(project, request) {
  const methods = baselineList(project);
  return {
    schema_version: 2,
    project_id: `${project.id.toLowerCase()}-${slugify(project.title)}`,
    identity_version: "project-generation-v2",
    origin_source: {
      type: "user_brief_plus_primary_source_generation",
      user_brief: request.userBrief,
      manifest_sha256: manifestHash,
    },
    origin: {
      research_arena: project.researchArena,
      canonical_object: project.canonicalObject,
      primary_outcome: project.primaryOutcome,
      evidence_surface: project.standardEvidenceSurface,
      published_method_baselines: methods,
      substrate_controls: project.substrateControls,
      deployment_boundary: project.deploymentBoundary,
      target_venue: project.targetVenue,
    },
    selection_interpretation: {
      why_now: project.whyNow,
      community_prize: project.communityPrize,
      citation_surface: project.citationSurface,
      non_binding_lens: project.nonBindingLens,
      sources: project.selectionSources,
    },
    boundaries: {
      compute_envelope: project.computeEnvelope,
      outside_scope: project.outsideScope,
      failure_preselected: false,
      method_preselected: false,
    },
    state_contract: {
      current_state_source: "PROJECT_STATE.md",
      legacy_current_fields_are_authority: false,
    },
  };
}

function buildProjectState(project) {
  const createdAt = new Date().toISOString();
  const methods = baselineList(project);
  return {
    schemaVersion: 4,
    updatedAt: createdAt,
    programCompass: {
      arena: project.researchArena,
      canonicalObject: project.canonicalObject,
      primaryOutcome: project.primaryOutcome,
      acceptedSurface: project.standardEvidenceSurface.name,
      explicitBoundaries: [project.computeEnvelope, ...project.outsideScope],
    },
    activeEpisode: {
      naturalProblem: "Determine which consequential natural design limitation remains after faithful published-method contact on the canonical object.",
      principle: "not-yet-earned",
      loadBearingLocus: "not-yet-earned",
      publishedRivals: {
        functional: methods[0].name,
        mechanistic: methods[1].name,
      },
      prediction: "Natural successes, failures, and rival disagreements on the accepted surface will reveal whether a shared design opportunity exists.",
      substrateFidelity: {
        intendedRegime: `${project.canonicalObject}; ${project.computeEnvelope}`,
        actualRegime: "not run",
        incumbentEffectReproduced: false,
        evidence: "No local claim-bearing reproduction has completed.",
      },
      inheritance: {
        parentRealization: "none",
        failedPrediction: "not applicable",
        preservedBehavior: "not applicable",
        changedComponent: "not applicable",
        discriminatingPrediction: "not applicable",
      },
      latestEvidence: "Primary sources establish a current field, accepted surface, and reproducible comparison targets; no project-specific experiment has completed.",
      strongestContraryEvidence: "No project-specific contrary evidence has yet been collected.",
      nextConstruction: project.firstEmpiricalContact,
      redirectCondition: "Primary-source or reproduction evidence shows that the selected surface, methods, or substrate cannot faithfully instantiate the authorized program.",
    },
    experiments: [],
    method: {
      primitive: "None.",
      maturity: "No candidate or realization has been earned.",
      mainRisk: "Prematurely converting the selection lens or a diagnostic proxy into the project identity.",
    },
    positiveObject: {
      assessment: "The PI has not yet established a paper-sized research candidate from current artifacts.",
      description: "none",
      evidence: [],
    },
    campaignManifest: null,
    paper: {
      status: "Not started.",
      spine: "None; the PI has not established a paper-sized candidate from current artifacts.",
      missingEvidence: "Faithful published-method contact, a natural problem account, and a positive deployable realization.",
    },
    gpu: {
      needed: null,
      reason: "Decide only after non-GPU preparation and a meaningful real-path smoke test.",
    },
    needsUser: {
      required: false,
      reason: "No user-owned decision is currently required.",
    },
    history: {
      note: "Fresh project generated from a validated v2 manifest; no legacy state sources exist.",
      legacySources: [],
    },
    reporting: {
      owner: "project-pi",
      migrationPending: false,
      reconciledAt: createdAt,
    },
  };
}

function renderProjectState(state) {
  return `# Project State\n\nThis is the sole replacement-style current scientific state for the project PI, user, and portfolio tooling. Keep at most the latest five decisive experiments; live GPU/process details and historical ledgers belong in leases, logs, and artifacts. The active episode is a scientific argument, not a fixed stage code. Verified evidence is factual; agent-authored gates, holds, route choices, and next actions remain revisable interpretations unless they cite an exact user or safety source. Registration freezes one run, not future construction. Repair semantic contradictions from artifacts before continuing; do not edit labels merely to satisfy tooling.\n\n<!-- FIRM_PROJECT_STATE_V4 -->\n\`\`\`json\n${JSON.stringify(state, null, 2)}\n\`\`\`\n`;
}

const validated = validateManifest(manifest);
fs.mkdirSync(outputRoot, { recursive: false });

for (const project of validated.projects) {
  const dir = path.join(outputRoot, project.id);
  fs.mkdirSync(dir);
  const files = {
    "PROGRAM_ORIGIN.md": buildProgramOrigin(project, validated.request),
    "SEED.md": buildSeed(project),
    "PROJECT_IDENTITY.json": `${JSON.stringify(buildIdentity(project, validated.request), null, 2)}\n`,
    "PROJECT_STATE.md": renderProjectState(buildProjectState(project)),
    "CLAUDE.md": buildProjectContract({
      projectId: project.id,
      localPath: path.join(outputRoot, project.id),
    }),
    "prompt.txt": `${buildPrompt(project)}${buildEpisodeDirective(project)}`,
  };
  for (const [name, content] of Object.entries(files)) {
    fs.writeFileSync(path.join(dir, name), content, "utf8");
  }
}

const summary = {
  schemaVersion: 2,
  sourceManifest: path.resolve(manifestPath),
  sourceManifestSha256: manifestHash,
  userBrief: validated.request.userBrief,
  projectCount: validated.projects.length,
  projects: validated.projects.map((project) => ({
    id: project.id,
    title: project.title,
    targetVenue: project.targetVenue,
    researchArena: project.researchArena,
  })),
};
fs.writeFileSync(path.join(outputRoot, "MANIFEST.json"), `${JSON.stringify(summary, null, 2)}\n`, "utf8");
console.log(`generated ${validated.projects.length} validated project folder(s) at ${outputRoot}`);
