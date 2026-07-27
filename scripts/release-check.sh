#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
errors=0

required=(
  README.md
  LICENSE
  NOTICE
  FAILURE_MAP.md
  assets/firm-hero.png
  assets/arr-2026-may-review-evidence.png
  docs/ORIGIN_AND_DESIGN.md
  install.sh
  scripts/verify-install.sh
  examples/README.md
  examples/01-method-loss-is-not-field-loss.md
  examples/02-seed-drift.md
  examples/03-paper-entry-audit.md
  demo/90-second-demo.md
  demo/recording-checklist.md
  demo/fixture/CLAUDE.md
  demo/fixture/RESULT.md
  demo/fixture/PROMPT.md
)

for path in "${required[@]}"; do
  if [[ ! -s "${ROOT_DIR}/${path}" ]]; then
    echo "MISSING: ${path}" >&2
    errors=$((errors + 1))
  fi
done

if grep -R -n -E 'REPOSITORY_URL|<your-repository-url>|YOUR_ACCOUNT' \
  "${ROOT_DIR}/README.md" "${ROOT_DIR}/demo" >/tmp/firm-placeholders.txt; then
  echo "UNRESOLVED repository placeholders:" >&2
  cat /tmp/firm-placeholders.txt >&2
  errors=$((errors + 1))
fi

if grep -R -n -E 'ResearcherOS|researcheros' \
  "${ROOT_DIR}" --exclude='release-check.sh' >/tmp/firm-legacy-brand.txt; then
  echo "LEGACY brand references:" >&2
  cat /tmp/firm-legacy-brand.txt >&2
  errors=$((errors + 1))
fi

if grep -R -n -E '/Users/[^ /]+|BEGIN (RSA|OPENSSH) PRIVATE KEY' \
  "${ROOT_DIR}" --exclude='release-check.sh' >/tmp/firm-private-paths.txt; then
  echo "POSSIBLE private paths or credentials:" >&2
  cat /tmp/firm-private-paths.txt >&2
  errors=$((errors + 1))
fi

if [[ ${errors} -ne 0 ]]; then
  echo "Release check failed with ${errors} blocking category/categories." >&2
  exit 1
fi

echo "Release check passed."
