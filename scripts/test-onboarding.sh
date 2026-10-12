#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "${TEST_ROOT}"' EXIT

PROJECT="${TEST_ROOT}/project"
bash "${ROOT_DIR}/firm" init "${PROJECT}" >/dev/null
bash "${ROOT_DIR}/scripts/verify-install.sh" "${PROJECT}/.claude/skills" >/dev/null

for host in claude trae; do
  runtime_home="${TEST_ROOT}/home-${host}"
  HOME="${runtime_home}" FIRM_HOST="${host}" \
    RESEARCH_SKILLS_BACKUP_DIR="${TEST_ROOT}/backup-${host}" \
    bash "${ROOT_DIR}/install.sh" >/dev/null
  bash "${ROOT_DIR}/scripts/verify-install.sh" \
    "${runtime_home}/.${host}/skills" >/dev/null
done

cmp "${ROOT_DIR}/CLAUDE-RESEARCH.md" \
  "${TEST_ROOT}/home-claude/.claude/CLAUDE-RESEARCH.md"
cmp "${ROOT_DIR}/CLAUDE-RESEARCH.md" \
  "${TEST_ROOT}/home-trae/.trae/CLAUDE-RESEARCH.md"
cmp "${TEST_ROOT}/home-claude/.claude/CLAUDE-RESEARCH.md" \
  "${TEST_ROOT}/home-trae/.trae/CLAUDE-RESEARCH.md"
[[ -L "${ROOT_DIR}/TRAE-RESEARCH.md" ]]
[[ "$(readlink "${ROOT_DIR}/TRAE-RESEARCH.md")" == "CLAUDE-RESEARCH.md" ]]
for host in claude trae; do
  cmp "${ROOT_DIR}/skills/research-pipeline/references/delegated-task.md" \
    "${TEST_ROOT}/home-${host}/.${host}/skills/research-pipeline/references/delegated-task.md"
done

required=(
  CLAUDE.md
  .firm/RESEARCH_PROGRAM.md
  .firm/FIRST_MESSAGE_NEW.md
  .firm/FIRST_MESSAGE_AUDIT.md
)

for path in "${required[@]}"; do
  if [[ ! -s "${PROJECT}/${path}" ]]; then
    echo "MISSING onboarding artifact: ${path}" >&2
    exit 1
  fi
done

before_hash="$(find "${PROJECT}/.claude/skills" -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum)"
bash "${ROOT_DIR}/firm" init "${PROJECT}" >/dev/null
after_hash="$(find "${PROJECT}/.claude/skills" -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum)"

if [[ "${before_hash}" != "${after_hash}" ]]; then
  echo "Second initialization changed an unchanged installation." >&2
  exit 1
fi

if find "${PROJECT}/.claude/skills" -maxdepth 1 -type d -name '.firm-backup-*' | grep -q .; then
  echo "Second initialization created an unnecessary backup." >&2
  exit 1
fi

marker_count="$(grep -Fc '<!-- FIRM:BEGIN -->' "${PROJECT}/CLAUDE.md")"
if [[ "${marker_count}" -ne 1 ]]; then
  echo "FIRM CLAUDE.md block is not idempotent." >&2
  exit 1
fi

EXISTING_PROJECT="${TEST_ROOT}/existing-project"
mkdir -p "${EXISTING_PROJECT}"
printf '# Existing user instructions\n' > "${EXISTING_PROJECT}/CLAUDE.md"
bash "${ROOT_DIR}/firm" init "${EXISTING_PROJECT}" >/dev/null

grep -Fq '# Existing user instructions' "${EXISTING_PROJECT}/CLAUDE.md"
grep -Fq '<!-- FIRM:BEGIN -->' "${EXISTING_PROJECT}/CLAUDE.md"
grep -Fq '# Existing user instructions' "${EXISTING_PROJECT}/.firm/CLAUDE.md.before-firm"

MISSING_PROJECT="${TEST_ROOT}/missing-project"
if bash "${ROOT_DIR}/firm" doctor "${MISSING_PROJECT}" >/dev/null 2>&1; then
  echo "FIRM doctor unexpectedly accepted a missing project." >&2
  exit 1
fi
if [[ -e "${MISSING_PROJECT}" ]]; then
  echo "FIRM doctor created the missing project it was asked to inspect." >&2
  exit 1
fi

bash "${ROOT_DIR}/firm" doctor "${PROJECT}" >/dev/null

HOST_ISOLATION_PROJECT="${TEST_ROOT}/host-isolation-project"
FIRM_HOST=trae TRAE_HOME="${TEST_ROOT}/must-not-install-global-trae" \
  bash "${ROOT_DIR}/firm" init "${HOST_ISOLATION_PROJECT}" >/dev/null
cmp "${ROOT_DIR}/CLAUDE-RESEARCH.md" \
  "${HOST_ISOLATION_PROJECT}/.claude/CLAUDE-RESEARCH.md"
if [[ -e "${TEST_ROOT}/must-not-install-global-trae" ]]; then
  echo "Claude project-local init unexpectedly modified the Trae runtime." >&2
  exit 1
fi

echo "Onboarding test passed."
