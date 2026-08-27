#!/usr/bin/env node

import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(here, "..");
const generator = path.join(repositoryRoot, "scripts/generate_seed_project_folders.mjs");
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "firm-project-generator-test-"));
const portfolio = path.join(temp, "portfolio");
fs.mkdirSync(portfolio);

const method = (name, suffix) => ({
  name,
  paperUrl: `https://example.org/paper-${suffix}`,
  codeUrl: `https://github.com/example/${suffix}`,
  protocol: "Official public task split and metric.",
  whyDecisive: "It is a recent same-task published method with a directly threatening computation.",
});

const manifest = {
  schemaVersion: 2,
  request: {
    userBrief: "Generate one ICLR project in image editing within four A100s.",
    targetVenues: ["ICLR"],
    broadDirections: ["image editing"],
    maximumProjects: 1,
    computeEnvelope: "At most four A100 GPUs; no foundation pretraining.",
    exclusions: ["foundation-model pretraining"],
    venueScopeSources: ["https://iclr.cc/Conferences/2027/CallForPapers"],
    existingPortfolioRoot: portfolio,
  },
  researchSources: [
    { kind: "official-venue", title: "ICLR call", url: "https://iclr.cc/Conferences/2027/CallForPapers", relevance: "Official scope." },
    { kind: "paper", title: "Method A", url: "https://example.org/paper-a", relevance: "Strong incumbent." },
    { kind: "benchmark", title: "Existing benchmark", url: "https://example.org/benchmark", relevance: "Accepted surface." },
  ],
  projects: [{
    id: "T01",
    title: "Instruction-Guided Image Editing",
    targetVenue: "ICLR",
    researchArena: "instruction-guided image editing with open models",
    canonicalObject: "An open editor transforms a source image according to a natural-language instruction.",
    primaryOutcome: "Official edit-success quality at a fixed preservation and compute contract.",
    standardEvidenceSurface: {
      name: "An existing public image-editing benchmark",
      protocol: "Use its released split, labels, and automatic metrics.",
      whyCanonical: "Its full population contains source-image and instruction conditioned edits.",
      sources: ["https://example.org/benchmark"],
    },
    publishedMethodBaselines: {
      strongIncumbent: method("Published Editor A", "a"),
      nearestRival: method("Published Editor B", "b"),
      additional: [],
    },
    substrateControls: ["Released base editor without project adaptation", "matched component ablation"],
    whyNow: "Recent open editors expose a reproducible accepted task with unresolved tradeoffs.",
    communityPrize: "A reusable editing primitive could change how open editors preserve unrequested content.",
    citationSurface: "Instruction editing, personalization, localized generation, and multimodal adaptation.",
    nonBindingLens: "Inspect whether requested and preserved content compete inside the editor.",
    deploymentBoundary: "Only the source image, user instruction, and model-computable features are available.",
    computeEnvelope: "One released editor, lightweight adaptation, and at most four A100 GPUs.",
    outsideScope: ["foundation-model pretraining"],
    firstEmpiricalContact: "Reproduce both published methods on the released protocol and inspect matched natural successes, failures, and disagreements.",
    selectionSources: ["https://example.org/paper-a", "https://example.org/paper-b", "https://example.org/benchmark"],
  }],
};

function run(input, outputName, expectedStatus = 0) {
  const manifestPath = path.join(temp, `${outputName}.json`);
  const outputRoot = path.join(temp, outputName);
  fs.writeFileSync(manifestPath, `${JSON.stringify(input, null, 2)}\n`);
  const result = spawnSync(process.execPath, [generator, manifestPath, outputRoot], { encoding: "utf8" });
  assert.equal(result.status, expectedStatus, `stdout=${result.stdout}\nstderr=${result.stderr}`);
  return { result, outputRoot };
}

try {
  const { outputRoot } = run(manifest, "valid");
  const projectRoot = path.join(outputRoot, "T01");
  const expected = ["PROGRAM_ORIGIN.md", "SEED.md", "PROJECT_IDENTITY.json", "PROJECT_STATE.md", "CLAUDE.md", "prompt.txt"];
  assert.deepEqual(fs.readdirSync(projectRoot).sort(), expected.sort());

  const seed = fs.readFileSync(path.join(projectRoot, "SEED.md"), "utf8");
  const prompt = fs.readFileSync(path.join(projectRoot, "prompt.txt"), "utf8");
  const claude = fs.readFileSync(path.join(projectRoot, "CLAUDE.md"), "utf8");
  assert.match(seed, /Strong published-method incumbent/);
  assert.match(seed, /new benchmark construction/);
  assert.match(seed, /new human annotation, preference, rating, or judgment collection/);
  assert.doesNotMatch(seed, /strong and simple baselines/i);
  assert.doesNotMatch(prompt, /Ask Codex for an early|强基线和简单基线/);
  assert.match(claude, /LOCAL_INFRASTRUCTURE\.md/);
  assert.match(claude, /below 1 GB/);
  assert.match(claude, /replacement-style current synthesis/);

  const duplicateBaseline = structuredClone(manifest);
  duplicateBaseline.projects[0].publishedMethodBaselines.nearestRival.name = "Published Editor A";
  run(duplicateBaseline, "duplicate-baseline", 1);

  const tooMany = structuredClone(manifest);
  tooMany.request.maximumProjects = 1;
  tooMany.projects.push({ ...structuredClone(tooMany.projects[0]), id: "T02" });
  run(tooMany, "too-many", 1);

  const existing = run(manifest, "existing");
  const rerun = spawnSync(process.execPath, [generator, path.join(temp, "existing.json"), existing.outputRoot], { encoding: "utf8" });
  assert.equal(rerun.status, 1);
  assert.match(rerun.stderr, /refusing to overwrite/);

  fs.mkdirSync(path.join(portfolio, "T01"));
  run(manifest, "portfolio-id-conflict", 1);

  console.log("project generator tests passed");
} finally {
  fs.rmSync(temp, { recursive: true, force: true });
}
