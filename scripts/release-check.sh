#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  README.md
  README.zh-CN.md
  CLAUDE-RESEARCH.md
  CONTRIBUTING.md
  SECURITY.md
  CHANGELOG.md
  CITATION.cff
  LICENSE
  NOTICE
  .claude-plugin/plugin.json
  .claude-plugin/marketplace.json
  REFORM_MAP.md
  managed-skills.txt
  managed-shared-references.txt
  retired-skills.txt
  legacy-runtime-paths.txt
  docs/getting-started.md
  assets/firm-decision-demo.png
  assets/social-preview.png
  assets/source/social-preview.html
  assets/source/firm-decision-demo.html
  firm
  install.sh
  scripts/validate_skills.py
  scripts/check-research-contract.py
  scripts/test-onboarding.sh
  templates/CLAUDE_FIRM_BLOCK.md
  demo/fixture/CLAUDE.md
  demo/fixture/RESULT.md
  demo/fixture/PROMPT.md
)

for path in "${required[@]}"; do
  if [[ ! -s "${ROOT_DIR}/${path}" ]]; then
    echo "MISSING: ${path}" >&2
    exit 1
  fi
done

bash -n "${ROOT_DIR}/firm"
bash -n "${ROOT_DIR}/install.sh"
bash -n "${ROOT_DIR}/scripts/test-onboarding.sh"
bash -n "${ROOT_DIR}/scripts/verify-install.sh"
PYTHONDONTWRITEBYTECODE=1 python3 "${ROOT_DIR}/scripts/validate_skills.py"
PYTHONDONTWRITEBYTECODE=1 python3 "${ROOT_DIR}/scripts/check-research-contract.py"
PYTHONDONTWRITEBYTECODE=1 python3 \
  "${ROOT_DIR}/skills/research-audit/tests/test_evidence_lineage.py" -v
bash "${ROOT_DIR}/scripts/test-onboarding.sh"

if grep -R -n -E '/Users/[^ /]+|BEGIN (RSA|OPENSSH) PRIVATE KEY|REPOSITORY_URL|YOUR_ACCOUNT' \
  "${ROOT_DIR}" --exclude='release-check.sh' --exclude='.git' --exclude-dir='.git' >/tmp/firm-release-secrets.txt; then
  echo "Possible private path, credential, or placeholder:" >&2
  cat /tmp/firm-release-secrets.txt >&2
  exit 1
fi

echo "Release check passed."
