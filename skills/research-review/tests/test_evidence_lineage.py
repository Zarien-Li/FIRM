#!/usr/bin/env python3
"""Regression tests for evidence-lineage invalidation and stale-reference scans."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "scripts" / "evidence_lineage.py"
FIXTURE = HERE / "evidence_registry_fixture.json"
STALE = HERE / "stale_handoff.md"


class EvidenceLineageTest(unittest.TestCase):
    def run_tool(self, *args: str) -> tuple[int, dict]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=False,
            capture_output=True,
            text=True,
        )
        return result.returncode, json.loads(result.stdout)

    def test_dry_run_scans_pending_invalidation_closure(self) -> None:
        code, result = self.run_tool(
            str(FIXTURE),
            "--invalidate",
            "anchor.eval.v1",
            "--scan",
            str(STALE),
        )
        self.assertEqual(code, 1)
        self.assertFalse(result["ok"])
        self.assertEqual(
            result["impacted_evidence"],
            ["anchor.eval.v1", "result.main.v1", "run.seed0.v1"],
        )
        self.assertEqual(result["impacted_claims"], ["C1", "Table1"])
        self.assertTrue(
            any(
                finding["evidence_id"] == "result.main.v1"
                for finding in result["stale_references"]
            )
        )
        self.assertFalse(result["written"])

    def test_write_persists_transitive_invalidation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            registry.write_bytes(FIXTURE.read_bytes())
            code, result = self.run_tool(
                str(registry),
                "--invalidate",
                "anchor.eval.v1",
                "--write",
            )
            self.assertEqual(code, 0)
            self.assertTrue(result["ok"])
            self.assertTrue(result["written"])
            data = json.loads(registry.read_text(encoding="utf-8"))
            self.assertTrue(
                all(
                    data["evidence"][evidence_id]["status"] == "invalidated"
                    for evidence_id in data["evidence"]
                )
            )


if __name__ == "__main__":
    unittest.main()
