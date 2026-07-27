#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${ROOT_DIR}/skills"
TARGET_DIR="${FIRM_SKILLS_DIR:-${HOME}/.claude/skills}"
DRY_RUN=0

usage() {
  cat <<'EOF'
Install FIRM skills for Claude Code.

Usage:
  bash install.sh [--target PATH | --project PATH] [--dry-run]

Environment:
  FIRM_SKILLS_DIR  Override the default ~/.claude/skills target.

Options:
  --project PATH   Install into PATH/.claude/skills.
  --target PATH    Install directly into a skills directory.
  --dry-run        Show what would change without writing files.

Existing directories with the same names are moved into a timestamped backup
inside the target directory before installation.
EOF
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

timestamp="$(date +%Y%m%d-%H%M%S)"
backup_dir="${TARGET_DIR}/.firm-backup-${timestamp}"
installed=0
backed_up=0

echo "FIRM installer"
echo "  source: ${SOURCE_DIR}"
echo "  target: ${TARGET_DIR}"

if [[ ${DRY_RUN} -eq 0 ]]; then
  mkdir -p "${TARGET_DIR}"
fi

for source_path in "${SOURCE_DIR}"/*; do
  [[ -d "${source_path}" ]] || continue
  name="$(basename "${source_path}")"
  target_path="${TARGET_DIR}/${name}"

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
  echo "Dry run complete: ${installed} directories would be installed."
  exit 0
fi

bash "${ROOT_DIR}/scripts/verify-install.sh" "${TARGET_DIR}"

echo
echo "Installed ${installed} FIRM directories."
if [[ ${backed_up} -gt 0 ]]; then
  echo "Backed up ${backed_up} existing directories to:"
  echo "  ${backup_dir}"
fi
echo "Restart Claude Code, or ask the current session to reread active skills."
