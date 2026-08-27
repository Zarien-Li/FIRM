import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const root = fs.mkdtempSync(path.join(os.tmpdir(), "firm-project-prompt-"));
const portfolio = path.join(root, "portfolio");
const output = path.join(root, "output");
const manifestFile = path.join(root, "manifest.json");
fs.mkdirSync(portfolio);

const incumbent = {
  name: "Published Incumbent",
  paperUrl: "https://example.org/incumbent",
  codeUrl: "https://example.org/incumbent-code",
  protocol: "Official protocol",
  whyDecisive: "It defines the current quality and cost trade-off.",
};
const rival = {
  name: "Nearest Rival",
  paperUrl: "https://example.org/rival",
  codeUrl: "https://example.org/rival-code",
  protocol: "Matched official protocol",
  whyDecisive: "It changes the same load-bearing computation.",
};

const manifest = {
  schemaVersion: 2,
  request: {
    userBrief: "Study a reusable editing principle.",
    targetVenues: ["ICLR"],
    broadDirections: ["image editing"],
    maximumProjects: 1,
    computeEnvelope: "Four A100 GPUs",
    exclusions: [],
    venueScopeSources: ["https://example.org/venue"],
    existingPortfolioRoot: portfolio,
  },
  researchSources: [
    { kind: "official-venue", title: "Venue", url: "https://example.org/venue", relevance: "scope" },
    { kind: "paper", title: "Incumbent", url: incumbent.paperUrl, relevance: "frontier" },
    { kind: "paper", title: "Rival", url: rival.paperUrl, relevance: "collision" },
  ],
  projects: [{
    id: "P1",
    title: "Project-Specific Editing",
    targetVenue: "ICLR",
    researchArena: "instruction-guided image editing",
    canonicalObject: "an edit that changes the requested content while preserving the rest",
    primaryOutcome: "edit fidelity and preservation under matched cost",
    standardEvidenceSurface: {
      name: "Accepted Editing Surface",
      protocol: "Use the released test population and evaluator.",
      whyCanonical: "It contains natural requested edits and preservation constraints.",
      sources: ["https://example.org/surface"],
    },
    publishedMethodBaselines: { strongIncumbent: incumbent, nearestRival: rival, additional: [] },
    substrateControls: ["released base editor"],
    whyNow: "Current editors still bind control and preservation together.",
    communityPrize: "Replace per-method preservation patches with one reusable editing principle.",
    citationSurface: "instruction editing, personalization, and video editing",
    nonBindingLens: "control and preservation may require different update semantics",
    deploymentBoundary: "the instruction, source image, and frozen editor state",
    computeEnvelope: "Four A100 GPUs",
    outsideScope: ["foundation-model pretraining"],
    firstEmpiricalContact: "Compare matched natural successes and failures of the two released methods.",
    selectionSources: [incumbent.paperUrl, rival.paperUrl],
  }],
};

fs.writeFileSync(manifestFile, `${JSON.stringify(manifest, null, 2)}\n`);
execFileSync(process.execPath, [
  path.resolve("scripts/generate_seed_project_folders.mjs"),
  manifestFile,
  output,
], { cwd: path.resolve("."), stdio: "pipe" });

const prompt = fs.readFileSync(path.join(output, "P1", "prompt.txt"), "utf8");
assert.match(prompt, /Project-Specific Editing/);
assert.match(prompt, /instruction-guided image editing/);
assert.match(prompt, /Replace per-method preservation patches/);
assert.match(prompt, /Published Incumbent/);
assert.match(prompt, /Nearest Rival/);
assert.match(prompt, /起始地图，不是已经成立的 failure/);
assert.match(prompt, /可以自行改变当前路线/);
assert.doesNotMatch(prompt, /第一轮在 .*完整标准 population 上/);
assert.doesNotMatch(prompt, /建设性 v1→v2\/v3/);

console.log("Project-generation prompt regression passed.");
