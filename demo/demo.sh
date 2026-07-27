#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEED="${DEMO_SPEED:-3}"

pause() {
  sleep "$1"
}

clear_screen() {
  printf '\033[2J\033[H'
}

slide() {
  clear_screen
  printf '\n\033[1;36m%s\033[0m\n\n' "$1"
}

slide "Research agents do not usually fail at launching experiments."
printf 'They fail after the first method loses.\n'
printf 'They drift from an important seed into a private cell.\n'
printf 'They polish a paper before the evidence is ready.\n'
pause "$((4 * SPEED))"

slide "ResearcherOS"
printf '100B+ model tokens of failure-driven research judgment.\n\n'
printf '  seed drift  |  premature closure  |  probe addiction\n'
printf '  seed theater  |  late integrity failure  |  endless research\n'
pause "$((5 * SPEED))"

slide "One-command install"
printf '$ git clone https://github.com/Zoiya-Li/ResearcherOS.git && \\\n'
printf '    cd ResearcherOS && bash install.sh\n\n'
printf '\033[1;32mVerification passed.\033[0m\n'
pause "$((5 * SPEED))"

slide "A real decision pattern"
sed -n '1,16p' "${ROOT_DIR}/demo/fixture/RESULT.md"
pause "$((5 * SPEED))"

slide "The ResearcherOS response"
printf '1. One clear loss diagnoses this realization.\n'
printf '2. Do not sweep seeds. Do not close the field.\n'
printf '3. Repair the component the evidence implicates.\n'
pause "$((6 * SPEED))"

slide "Independent second PI"
printf 'Prize / Fidelity / Entry\n'
printf '        -> Interpret -> Invent -> Attack\n'
pause "$((5 * SPEED))"

slide "Inherit the failure map."
printf 'Do not pay to rediscover it.\n\n'
printf 'Open source now.\n'
