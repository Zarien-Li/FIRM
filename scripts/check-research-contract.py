#!/usr/bin/env python3
"""Run the canonical research semantic contract from the repository root."""

from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = (
    ROOT
    / "skills"
    / "research-pipeline"
    / "tests"
    / "check_semantic_contract.py"
)

if __name__ == "__main__":
    namespace = runpy.run_path(str(CHECKER))
    raise SystemExit(namespace["main"]())
