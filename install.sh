#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${CLAUDE_HOME:-${HOME}/.claude}/skills"
STAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_DIR="${HOME}/Desktop/research-skills-backup-${STAMP}"

mkdir -p "${TARGET_DIR}" "${TARGET_DIR}/shared-references"

changed=0
for source_path in "${ROOT_DIR}"/skills/*; do
  [[ -d "${source_path}" && -f "${source_path}/SKILL.md" ]] || continue
  name="$(basename "${source_path}")"
  target_path="${TARGET_DIR}/${name}"
  if [[ -e "${target_path}" ]]; then
    mkdir -p "${BACKUP_DIR}/skills"
    cp -R "${target_path}" "${BACKUP_DIR}/skills/${name}"
  fi
  rm -rf "${target_path}"
  cp -R "${source_path}" "${target_path}"
  changed=$((changed + 1))
done

if [[ -d "${TARGET_DIR}/shared-references" ]]; then
  mkdir -p "${BACKUP_DIR}"
  cp -R "${TARGET_DIR}/shared-references" "${BACKUP_DIR}/shared-references"
fi
cp -R "${ROOT_DIR}/shared-references/." "${TARGET_DIR}/shared-references/"

find "${TARGET_DIR}" -type d -name __pycache__ -prune -exec rm -rf {} +
find "${TARGET_DIR}" -type f -name '*.pyc' -delete

echo "Installed ${changed} research skills into ${TARGET_DIR}."
echo "Previous same-named content was backed up under ${BACKUP_DIR}."
echo "Canonical project prompt: ${ROOT_DIR}/CLAUDE-RESEARCH.md"
