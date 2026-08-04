#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${ROOT_DIR}/skills"
TARGET_DIR="${1:-${FIRM_SKILLS_DIR:-${HOME}/.claude/skills}}"

skill_dirs=()
while IFS= read -r skill_dir; do
  skill_dirs+=("${skill_dir}")
done < <(
  find "${SOURCE_DIR}" -mindepth 2 -maxdepth 2 -name SKILL.md -print \
    | sed 's#/SKILL.md$##' \
    | sort
)

missing=0
for source_path in "${skill_dirs[@]}"; do
  name="$(basename "${source_path}")"
  target_path="${TARGET_DIR}/${name}/SKILL.md"
  if [[ ! -s "${target_path}" ]]; then
    echo "MISSING skill entry: ${target_path}" >&2
    missing=$((missing + 1))
  fi
done

if [[ ${#skill_dirs[@]} -ne 17 ]]; then
  echo "Source validation failed: expected 17 skills, found ${#skill_dirs[@]}." >&2
  missing=$((missing + 1))
fi

if [[ ${missing} -ne 0 ]]; then
  echo "Verification failed: ${missing} issue(s)." >&2
  exit 1
fi

echo "Verification passed."
echo "  skills: ${#skill_dirs[@]}"
echo "  target: ${TARGET_DIR}"
