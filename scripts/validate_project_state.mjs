#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const statePath = process.argv[2];
if (!statePath) {
  console.error("usage: node scripts/validate_project_state.mjs <PROJECT_STATE.md>");
  process.exit(2);
}

const absolutePath = path.resolve(statePath);
const text = fs.readFileSync(absolutePath, "utf8");
const match = text.match(/<!-- FIRM_PROJECT_STATE_V4 -->[\s\S]*?```json\s*([\s\S]*?)\s*```/);
if (!match) {
  console.error(`${absolutePath}: missing FIRM_PROJECT_STATE_V4 JSON block`);
  process.exit(1);
}

let state;
try {
  state = JSON.parse(match[1]);
} catch (error) {
  console.error(`${absolutePath}: invalid state JSON: ${error.message}`);
  process.exit(1);
}

const errors = [];
const get = (object, dottedPath) => dottedPath
  .split(".")
  .reduce((value, key) => (value && typeof value === "object" ? value[key] : undefined), object);

const requireText = (dottedPath) => {
  const value = get(state, dottedPath);
  if (typeof value !== "string" || value.trim() === "") {
    errors.push(`${dottedPath} must be non-empty text`);
  }
};

if (state.schemaVersion !== 4) {
  errors.push(`schemaVersion must be 4, found ${JSON.stringify(state.schemaVersion)}`);
}

for (const dottedPath of [
  "updatedAt",
  "programCompass.arena",
  "programCompass.canonicalObject",
  "programCompass.primaryOutcome",
  "programCompass.acceptedSurface",
  "activeEpisode.naturalProblem",
  "activeEpisode.principle",
  "activeEpisode.loadBearingLocus",
  "activeEpisode.publishedRivals.functional",
  "activeEpisode.publishedRivals.mechanistic",
  "activeEpisode.prediction",
  "activeEpisode.substrateFidelity.intendedRegime",
  "activeEpisode.substrateFidelity.actualRegime",
  "activeEpisode.substrateFidelity.evidence",
  "activeEpisode.latestEvidence",
  "activeEpisode.strongestContraryEvidence",
  "activeEpisode.nextConstruction",
  "activeEpisode.redirectCondition",
  "method.primitive",
  "method.maturity",
  "paper.status",
  "paper.spine",
]) {
  requireText(dottedPath);
}

if (!Array.isArray(state.experiments)) {
  errors.push("experiments must be an array");
} else if (state.experiments.length > 5) {
  errors.push("experiments must retain at most five decisive records");
}

if (!state.positiveObject || typeof state.positiveObject.exists !== "boolean") {
  errors.push("positiveObject.exists must be boolean");
}

const inheritance = state.activeEpisode?.inheritance;
if (!inheritance || typeof inheritance !== "object") {
  errors.push("activeEpisode.inheritance must be present");
} else {
  requireText("activeEpisode.inheritance.parentRealization");
  const parent = String(inheritance.parentRealization || "").trim().toLowerCase();
  if (parent && !["none", "not applicable"].includes(parent)) {
    for (const key of [
      "failedPrediction",
      "preservedBehavior",
      "changedComponent",
      "discriminatingPrediction",
    ]) {
      const value = String(inheritance[key] || "").trim().toLowerCase();
      if (!value || ["none", "not applicable", "n/a", "unknown"].includes(value)) {
        errors.push(`activeEpisode.inheritance.${key} is required for a successor realization`);
      }
    }
  }
}

const nextConstruction = String(state.activeEpisode?.nextConstruction || "");
const gpuNeeded = state.gpu?.needed;
if (gpuNeeded === false && /\b(gpu|accelerator|worker)\b|启动.{0,8}(训练|实验)|提交.{0,8}(训练|实验)/i.test(nextConstruction)) {
  errors.push("gpu.needed is false but activeEpisode.nextConstruction describes accelerator execution");
}

const positiveExists = state.positiveObject?.exists === true;
const paperStatus = String(state.paper?.status || "");
const methodMaturity = String(state.method?.maturity || "");
if (!positiveExists && /(submission[- ]?ready|paper[- ]?bearing|claim[- ]?ready|stable manuscript)/i.test(`${paperStatus} ${methodMaturity}`)) {
  errors.push("paper or method maturity claims a paper-bearing object while positiveObject.exists is false");
}

if (errors.length > 0) {
  console.error(`PROJECT_STATE semantic validation failed: ${absolutePath}`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`PROJECT_STATE semantic validation passed: ${absolutePath}`);
