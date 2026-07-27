#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${ROOT_DIR}/skills"
TARGET_DIR="${1:-${RESEARCHEROS_SKILLS_DIR:-${HOME}/.claude/skills}}"

missing=0
skill_count=0
reference_count=0

for source_path in "${SOURCE_DIR}"/*; do
  [[ -d "${source_path}" ]] || continue
  name="$(basename "${source_path}")"
  target_path="${TARGET_DIR}/${name}"

  if [[ ! -d "${target_path}" ]]; then
    echo "MISSING directory: ${target_path}" >&2
    missing=$((missing + 1))
    continue
  fi

  if [[ -f "${source_path}/SKILL.md" ]]; then
    skill_count=$((skill_count + 1))
    if [[ ! -s "${target_path}/SKILL.md" ]]; then
      echo "MISSING skill entry: ${target_path}/SKILL.md" >&2
      missing=$((missing + 1))
    fi
  fi
done

if [[ -d "${TARGET_DIR}/shared-references" ]]; then
  reference_count="$(find "${TARGET_DIR}/shared-references" -type f -name '*.md' | wc -l | tr -d ' ')"
fi

if [[ ${missing} -ne 0 ]]; then
  echo "Verification failed: ${missing} required paths are missing." >&2
  exit 1
fi

echo "Verification passed."
echo "  skills: ${skill_count}"
echo "  shared references: ${reference_count}"
echo "  target: ${TARGET_DIR}"
