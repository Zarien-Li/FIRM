#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${ROOT_DIR}/skills"
TARGET_DIR="${FIRM_SKILLS_DIR:-${HOME}/.claude/skills}"
DRY_RUN=0

usage() {
  cat <<'USAGE'
Install FIRM skills directly for Claude Code.

The recommended installation path is the plugin marketplace. Use this script for
legacy global installation or project-local copies.

Usage:
  bash install.sh [--target PATH | --project PATH] [--dry-run]

Options:
  --project PATH   Install into PATH/.claude/skills.
  --target PATH    Install directly into a skills directory.
  --dry-run        Show what would change without writing files.

Unchanged skills are left untouched. A changed same-named directory is moved to a
timestamped backup before the FIRM version is installed.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      [[ $# -ge 2 ]] || { echo "error: --target requires a path" >&2; exit 2; }
      TARGET_DIR="$2"
      shift 2
      ;;
    --project)
      [[ $# -ge 2 ]] || { echo "error: --project requires a path" >&2; exit 2; }
      [[ -d "$2" ]] || { echo "error: project directory not found: $2" >&2; exit 2; }
      TARGET_DIR="$2/.claude/skills"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -d "${SOURCE_DIR}" ]] || {
  echo "error: skills directory not found: ${SOURCE_DIR}" >&2
  exit 1
}

skill_dirs=()
while IFS= read -r skill_dir; do
  skill_dirs+=("${skill_dir}")
done < <(
  find "${SOURCE_DIR}" -mindepth 2 -maxdepth 2 -name SKILL.md -print \
    | sed 's#/SKILL.md$##' \
    | sort
)

if [[ ${#skill_dirs[@]} -ne 17 ]]; then
  echo "error: expected 17 source skills, found ${#skill_dirs[@]}" >&2
  exit 1
fi

timestamp="$(date +%Y%m%d-%H%M%S)"
backup_dir="${TARGET_DIR}/.firm-backup-${timestamp}"
installed=0
unchanged=0
backed_up=0

echo "FIRM installer"
echo "  source: ${SOURCE_DIR}"
echo "  target: ${TARGET_DIR}"

if [[ ${DRY_RUN} -eq 0 ]]; then
  mkdir -p "${TARGET_DIR}"
fi

for source_path in "${skill_dirs[@]}"; do
  name="$(basename "${source_path}")"
  target_path="${TARGET_DIR}/${name}"

  if [[ -d "${target_path}" ]] && diff -qr "${source_path}" "${target_path}" >/dev/null 2>&1; then
    echo "  unchanged: ${name}"
    unchanged=$((unchanged + 1))
    continue
  fi

  if [[ -e "${target_path}" ]]; then
    echo "  backup: ${name} -> ${backup_dir}/${name}"
    if [[ ${DRY_RUN} -eq 0 ]]; then
      mkdir -p "${backup_dir}"
      mv "${target_path}" "${backup_dir}/${name}"
    fi
    backed_up=$((backed_up + 1))
  fi

  echo "  install: ${name}"
  if [[ ${DRY_RUN} -eq 0 ]]; then
    cp -R "${source_path}" "${target_path}"
  fi
  installed=$((installed + 1))
done

if [[ ${DRY_RUN} -eq 1 ]]; then
  echo "Dry run complete: ${installed} install, ${unchanged} unchanged, ${backed_up} backup."
  exit 0
fi

bash "${ROOT_DIR}/scripts/verify-install.sh" "${TARGET_DIR}"

echo
echo "Installed or updated ${installed} skill(s); ${unchanged} unchanged."
if [[ ${backed_up} -gt 0 ]]; then
  echo "Backed up ${backed_up} changed directory/directories to:"
  echo "  ${backup_dir}"
fi
echo "Restart Claude Code or run /reload-plugins when applicable."
