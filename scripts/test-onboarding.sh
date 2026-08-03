#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "${TEST_ROOT}"' EXIT

PROJECT="${TEST_ROOT}/project"

bash "${ROOT_DIR}/firm" init "${PROJECT}" >/dev/null
bash "${ROOT_DIR}/scripts/verify-install.sh" \
  "${PROJECT}/.claude/skills" >/dev/null

required=(
  CLAUDE.md
  CLAUDE-RESEARCH.md
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

if ! cmp -s "${ROOT_DIR}/CLAUDE-RESEARCH.md" \
  "${PROJECT}/CLAUDE-RESEARCH.md"; then
  echo "Installed CLAUDE-RESEARCH.md does not match the public prompt." >&2
  exit 1
fi

bash "${ROOT_DIR}/firm" init "${PROJECT}" >/dev/null

marker_count="$(
  grep -Fc '<!-- FIRM:BEGIN -->' "${PROJECT}/CLAUDE.md"
)"
if [[ "${marker_count}" -ne 1 ]]; then
  echo "FIRM CLAUDE.md block is not idempotent." >&2
  exit 1
fi

EXISTING_PROJECT="${TEST_ROOT}/existing-project"
mkdir -p "${EXISTING_PROJECT}"
printf '# Existing user instructions\n' > "${EXISTING_PROJECT}/CLAUDE.md"
printf '# Existing research prompt\n' > "${EXISTING_PROJECT}/CLAUDE-RESEARCH.md"
bash "${ROOT_DIR}/firm" init "${EXISTING_PROJECT}" >/dev/null

grep -Fq '# Existing user instructions' "${EXISTING_PROJECT}/CLAUDE.md"
grep -Fq '<!-- FIRM:BEGIN -->' "${EXISTING_PROJECT}/CLAUDE.md"
grep -Fq '# Existing user instructions' \
  "${EXISTING_PROJECT}/.firm/CLAUDE.md.before-firm"
grep -Fq '# Existing research prompt' \
  "${EXISTING_PROJECT}/CLAUDE-RESEARCH.md"

MISSING_PROJECT="${TEST_ROOT}/missing-project"
if bash "${ROOT_DIR}/firm" doctor "${MISSING_PROJECT}" >/dev/null 2>&1; then
  echo "FIRM doctor unexpectedly accepted a missing project." >&2
  exit 1
fi
if [[ -e "${MISSING_PROJECT}" ]]; then
  echo "FIRM doctor created the missing project it was asked to inspect." >&2
  exit 1
fi

echo "Onboarding test passed."
