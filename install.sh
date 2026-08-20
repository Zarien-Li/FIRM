#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_ROOT="${CLAUDE_HOME:-${HOME}/.claude}"
TARGET_DIR="${CLAUDE_ROOT}/skills"
SOURCE_MANIFEST="${ROOT_DIR}/managed-skills.txt"
SHARED_MANIFEST="${ROOT_DIR}/managed-shared-references.txt"
TARGET_MANIFEST="${TARGET_DIR}/.research-skills-managed"
STAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_DIR="${RESEARCH_SKILLS_BACKUP_DIR:-${HOME}/Desktop/research-skills-backup-${STAMP}}"

contains_line() {
  local needle="$1"
  local file="$2"
  grep -Fqx "${needle}" "${file}" 2>/dev/null
}

backup_path() {
  local path="$1"
  local rel="$2"
  [[ -e "${path}" ]] || return 0
  mkdir -p "${BACKUP_DIR}/$(dirname "${rel}")"
  cp -R "${path}" "${BACKUP_DIR}/${rel}"
}

[[ -f "${SOURCE_MANIFEST}" ]] || {
  echo "Missing managed skill manifest: ${SOURCE_MANIFEST}" >&2
  exit 2
}
[[ -f "${SHARED_MANIFEST}" ]] || {
  echo "Missing shared-reference manifest: ${SHARED_MANIFEST}" >&2
  exit 2
}

mkdir -p "${TARGET_DIR}"

# Remove only skills previously owned by this package or explicitly retired by it.
if [[ -f "${TARGET_MANIFEST}" ]]; then
  while IFS= read -r name; do
    [[ -n "${name}" && "${name}" != \#* ]] || continue
    if ! contains_line "${name}" "${SOURCE_MANIFEST}"; then
      backup_path "${TARGET_DIR}/${name}" "retired-skills/${name}"
      rm -rf "${TARGET_DIR}/${name}"
    fi
  done < "${TARGET_MANIFEST}"
fi

if [[ -f "${ROOT_DIR}/retired-skills.txt" ]]; then
  while IFS= read -r name; do
    [[ -n "${name}" && "${name}" != \#* ]] || continue
    if [[ -e "${TARGET_DIR}/${name}" ]]; then
      backup_path "${TARGET_DIR}/${name}" "retired-skills/${name}"
      rm -rf "${TARGET_DIR}/${name}"
    fi
  done < "${ROOT_DIR}/retired-skills.txt"
fi

installed=0
while IFS= read -r name; do
  [[ -n "${name}" && "${name}" != \#* ]] || continue
  source_path="${ROOT_DIR}/skills/${name}"
  target_path="${TARGET_DIR}/${name}"
  [[ -f "${source_path}/SKILL.md" ]] || {
    echo "Manifest entry has no SKILL.md: ${name}" >&2
    exit 2
  }
  if [[ -e "${target_path}" ]] && ! diff -qr "${source_path}" "${target_path}" >/dev/null; then
    backup_path "${target_path}" "changed-skills/${name}"
  fi
  rm -rf "${target_path}"
  cp -R "${source_path}" "${target_path}"
  installed=$((installed + 1))
done < "${SOURCE_MANIFEST}"

while IFS= read -r name; do
  [[ -n "${name}" && "${name}" != \#* ]] || continue
  [[ -f "${ROOT_DIR}/shared-references/${name}" ]] || {
    echo "Shared manifest entry is missing: ${name}" >&2
    exit 2
  }
done < "${SHARED_MANIFEST}"

for source_path in "${ROOT_DIR}"/shared-references/*; do
  [[ -f "${source_path}" ]] || continue
  name="$(basename "${source_path}")"
  contains_line "${name}" "${SHARED_MANIFEST}" || {
    echo "Unmanaged shared reference present: ${name}" >&2
    exit 2
  }
done

if [[ -d "${TARGET_DIR}/shared-references" ]] && ! diff -qr "${ROOT_DIR}/shared-references" "${TARGET_DIR}/shared-references" >/dev/null; then
  backup_path "${TARGET_DIR}/shared-references" "shared-references"
fi
rm -rf "${TARGET_DIR}/shared-references"
cp -R "${ROOT_DIR}/shared-references" "${TARGET_DIR}/shared-references"

cp "${ROOT_DIR}/CLAUDE-RESEARCH.md" "${CLAUDE_ROOT}/CLAUDE-RESEARCH.md"
cp "${SOURCE_MANIFEST}" "${TARGET_MANIFEST}"
cp "${SHARED_MANIFEST}" "${TARGET_DIR}/.research-shared-references-managed"

# Archive known pre-migration runtime files. Unknown user material is untouched.
if [[ -f "${ROOT_DIR}/legacy-runtime-paths.txt" ]]; then
  while IFS= read -r rel; do
    [[ -n "${rel}" && "${rel}" != \#* ]] || continue
    path="${CLAUDE_ROOT}/${rel}"
    if [[ -e "${path}" ]]; then
      backup_path "${path}" "legacy-runtime/${rel}"
      rm -rf "${path}"
    fi
  done < "${ROOT_DIR}/legacy-runtime-paths.txt"
fi

find "${TARGET_DIR}" -type d -name __pycache__ -prune -exec rm -rf {} +
find "${TARGET_DIR}" -type f -name '*.pyc' -delete

echo "Installed ${installed} managed research skills into ${TARGET_DIR}."
if [[ -d "${BACKUP_DIR}" ]]; then
  echo "Changed or retired content was preserved under ${BACKUP_DIR}."
else
  echo "No changed or retired runtime content required backup."
fi
echo "Runtime addendum: ${CLAUDE_ROOT}/CLAUDE-RESEARCH.md"
