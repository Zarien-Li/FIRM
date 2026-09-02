#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${1:-${FIRM_SKILLS_DIR:-${HOME}/.claude/skills}}"
MANIFEST="${ROOT_DIR}/managed-skills.txt"
failures=0
count=0

while IFS= read -r name; do
  [[ -n "${name}" && "${name}" != \#* ]] || continue
  count=$((count + 1))
  source_path="${ROOT_DIR}/skills/${name}"
  target_path="${TARGET_DIR}/${name}"
  if [[ ! -f "${target_path}/SKILL.md" ]]; then
    echo "MISSING managed skill: ${target_path}" >&2
    failures=$((failures + 1))
  elif ! diff -qr "${source_path}" "${target_path}" >/dev/null; then
    echo "MISMATCH managed skill: ${name}" >&2
    failures=$((failures + 1))
  fi
done < "${MANIFEST}"

if [[ "${count}" -ne 6 ]]; then
  echo "Manifest validation failed: expected 6 skills, found ${count}." >&2
  failures=$((failures + 1))
fi

if [[ "${failures}" -ne 0 ]]; then
  echo "Verification failed: ${failures} issue(s)." >&2
  exit 1
fi

echo "Verification passed."
echo "  managed skills: ${count}"
echo "  target: ${TARGET_DIR}"
