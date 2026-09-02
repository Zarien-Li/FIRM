#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEED="${DEMO_SPEED:-1}"

pause() {
  if [[ "${SPEED}" != "0" ]]; then
    sleep "$1"
  fi
}

clear_screen() {
  if [[ -t 1 ]]; then
    printf '\033[2J\033[H'
  fi
}

slide() {
  clear_screen
  printf '\n\033[1;36m%s\033[0m\n\n' "$1"
}

slide "FIRM — research judgment for Claude Code"
printf 'Claude can search, code, run, and write.\n'
printf 'FIRM helps it decide what the evidence means and what to do next.\n'
pause 3

slide "Install as a Claude Code plugin"
printf '/plugin marketplace add Zarien-Li/FIRM\n'
printf '/plugin install firm@firm-research\n'
printf '/reload-plugins\n'
pause 4

slide "Neutral result packet"
sed -n '1,18p' "${ROOT_DIR}/demo/fixture/RESULT.md"
pause 5

slide "Run the flagship diagnosis skill"
printf 'cd demo/fixture\n'
printf 'claude\n\n'
printf '\033[1;32m/firm:method-development "Interpret RESULT.md"\033[0m\n'
pause 4

slide "What a strong response should separate"
printf '  • what the run establishes\n'
printf '  • what one seed cannot establish\n'
printf '  • which component the evidence implicates\n'
printf '  • which next experiment distinguishes the leading explanations\n'
pause 5

slide "Then continue the research loop"
printf '/firm:method-development "Develop the primitive from this evidence"\n'
printf '/firm:method-development "Plan the decisive construction experiment"\n'
printf '/firm:research-review\n\n'
printf 'A failed method is evidence—not a verdict on the field.\n'
