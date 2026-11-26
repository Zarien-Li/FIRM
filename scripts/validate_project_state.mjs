#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const input = process.argv[2];
if (!input) {
  console.error("usage: node scripts/validate_project_state.mjs <project-directory|PROJECT_STATE.json>");
  process.exit(2);
}
const absolute = path.resolve(input);
const project = fs.statSync(absolute).isDirectory() ? absolute : path.dirname(absolute);
if (!fs.existsSync(path.join(project, "PROJECT_STATE.json"))) {
  console.error("Legacy prose state: reconcile from authority/artifacts before migration. No scientific verdict.");
  process.exit(2);
}
const here = path.dirname(fileURLToPath(import.meta.url));
const helper = path.join(here, "../skills/research-pipeline/scripts/research_state.py");
const result = spawnSync("python3", [helper, "check", project], { stdio: "inherit" });
if (result.error) console.error(result.error.message);
process.exit(result.status ?? 1);
