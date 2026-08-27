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
  return `这是 ${project.id} 的全新 Claude Code 研究会话。用户授权的研究场域是：${project.researchArena}。canonical object 是：${project.canonicalObject}。唯一 primary outcome 是：${project.primaryOutcome}。目标投稿社区是 ${project.targetVenue}。\n\n先完整读取 \`CLAUDE.md\`、\`PROGRAM_ORIGIN.md\`、\`PROJECT_IDENTITY.json\`、\`SEED.md\`、唯一当前状态 \`PROJECT_STATE.md\`、\`~/.claude/CLAUDE-RESEARCH.md\`，以及当前动作需要的 active research skills。标题和 non-binding lens 不是既定 failure、机制或 method；旧 session、review 和候选方法也不能覆盖 authority。\n\n第一轮在 ${project.standardEvidenceSurface.name} 的完整标准 population 上，按原协议忠实复现命名的近期论文方法 ${methods[0].name} 和最近邻 ${methods[1].name}，并把 ${project.substrateControls.join("、")} 仅作为 substrate/attribution controls。核验 surface 确实实例化 canonical object、primary outcome 能看见目标价值、本地结果与论文报告语义一致，以及方法输入在决策时刻可得；直接阅读自然成功、失败、分歧和反例。不要用简单 heuristic、oracle、synthetic slice、clean subset 或私有指标替代 published-method contact。\n\n你是本项目 Research PI，负责从可信经验接触、问题解释、primitive 发明、真实实现、建设性 v1→v2/v3 消融一直推进到诚实论文。首个明确坏的 paired development seed 先诊断和重构设计，不通过扩 seed、模型、数据集或切片寻找正号。只在有意义的科学转折后更新 \`PROJECT_STATE.md\`；普通研究决策不交还用户，最终投稿和其他对外动作由用户签字。GPU 使用完全遵循当前项目 \`CLAUDE.md\`。\n`;
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
    schemaVersion: 3,
    updatedAt: createdAt,
    stage: "empirical contact not started",
    overview: {
      arena: project.researchArena,
      canonicalObject: project.canonicalObject,
      primaryMetric: project.primaryOutcome,
      mainBaselines: methods.map((method) => method.name),
    },
    currentResearch: {
      question: "What consequential natural design limitation remains after faithful published-method contact on the canonical object?",
      progress: "The arena and empirical entry point are selected; no project-specific failure, method, result, or paper identity has been earned.",
      strongestEvidence: "Primary sources establish a current field, accepted surface, and reproducible comparison targets; no claim-bearing project experiment has completed.",
      strongestContraryEvidence: "No project-specific contrary evidence has yet been collected.",
      currentProblem: "Establish faithful method reproduction, surface fidelity, evaluator validity, deployment information parity, and raw natural behavior before narrowing the problem.",
    },
    experiments: [],
    method: {
      primitive: "None.",
      maturity: "No candidate or realization has been earned.",
      mainRisk: "Prematurely converting the selection lens or a diagnostic proxy into the project identity.",
    },
    paper: {
      status: "Not started.",
      spine: "None; no credible positive object exists.",
      missingEvidence: "Faithful published-method contact, a natural problem account, and a positive deployable realization.",
    },
    nextAction: {
      description: project.firstEmpiricalContact,
      why: "The project must earn its failure and intervention locus from accepted-task behavior.",
      wouldChangeIf: "Primary-source or reproduction evidence shows the selected surface, methods, or compute envelope cannot faithfully instantiate the authorized arena.",
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
  return `# Project State\n\nThis is the sole replacement-style current scientific state for the project PI, user, and portfolio tooling. Keep at most the latest five decisive experiments; live GPU/process details and historical ledgers belong in leases, logs, and artifacts.\n\n<!-- FIRM_PROJECT_STATE_V3 -->\n\`\`\`json\n${JSON.stringify(state, null, 2)}\n\`\`\`\n`;
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
    "prompt.txt": buildPrompt(project),
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
