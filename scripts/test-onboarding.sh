#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "${TEST_ROOT}"' EXIT

PROJECT="${TEST_ROOT}/project"
bash "${ROOT_DIR}/firm" init "${PROJECT}" >/dev/null
bash "${ROOT_DIR}/scripts/verify-install.sh" "${PROJECT}/.claude/skills" >/dev/null

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

echo "Onboarding test passed."
