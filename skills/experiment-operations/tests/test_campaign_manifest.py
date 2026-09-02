import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "campaign_manifest.py"


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, args)],
        check=False,
        capture_output=True,
        text=True,
    )


class CampaignManifestTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_claim_start_complete_and_no_duplicate_claim(self):
        manifest = self.root / "CAMPAIGN_MANIFEST.json"
        manifest.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "campaignId": "c1",
                    "scientificQuestion": "q",
                    "protocol": {},
                    "cells": [
                        {
                            "cellId": "a",
                            "fingerprint": "f-a",
                            "purpose": "compare the current method with its decisive rival",
                            "method": "m",
                            "surface": "s",
                            "model": "x",
                            "seed": 0,
                            "dependencies": [],
                            "status": "planned",
                            "attempts": [],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

        claim = run("claim", manifest, "--worker", "w1")
        self.assertEqual(claim.returncode, 0, claim.stderr)
        payload = json.loads(claim.stdout)
        token = payload["leaseToken"]
        self.assertEqual(run("claim", manifest, "--worker", "w2").returncode, 2)

        attempt_dir = self.root / "attempt-1"
        started = run(
            "start",
            manifest,
            "--cell",
            "a",
            "--token",
            token,
            "--run-id",
            "r1",
            "--attempt-path",
            attempt_dir,
        )
        self.assertEqual(started.returncode, 0, started.stderr)

        result = attempt_dir / "result.json"
        marker = attempt_dir / "DONE"
        result.write_text("{}", encoding="utf-8")
        marker.write_text("ok\n", encoding="utf-8")
        completed = run(
            "complete",
            manifest,
            "--cell",
            "a",
            "--token",
            token,
            "--run-id",
            "r1",
            "--marker",
            marker,
            "--artifact",
            f"result={result}",
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(
            json.loads(manifest.read_text(encoding="utf-8"))["cells"][0]["status"],
            "completed",
        )

    def test_duplicate_fingerprint_is_rejected(self):
        manifest = self.root / "CAMPAIGN_MANIFEST.json"
        cell = {
            "fingerprint": "same",
            "status": "planned",
            "dependencies": [],
            "attempts": [],
        }
        manifest.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "campaignId": "c1",
                    "protocol": {},
                    "cells": [dict(cell, cellId="a"), dict(cell, cellId="b")],
                }
            ),
            encoding="utf-8",
        )
        self.assertEqual(run("validate", manifest).returncode, 2)

    def test_requeue_closes_running_attempt_before_new_claim(self):
        manifest = self.root / "CAMPAIGN_MANIFEST.json"
        manifest.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "campaignId": "c2",
                    "protocol": {},
                    "cells": [
                        {
                            "cellId": "a",
                            "fingerprint": "f-a",
                            "status": "running",
                            "dependencies": [],
                            "claim": {"worker": "w1", "token": "t1"},
                            "attempts": [
                                {
                                    "attempt": 1,
                                    "runId": "r1",
                                    "status": "running",
                                    "attemptPath": str(self.root / "attempt-1"),
                                }
                            ],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        result = run("requeue", manifest, "--cell", "a", "--reason", "host interruption")
        self.assertEqual(result.returncode, 0, result.stderr)
        cell = json.loads(manifest.read_text(encoding="utf-8"))["cells"][0]
        self.assertEqual(cell["status"], "planned")
        self.assertEqual(cell["attempts"][0]["status"], "interrupted")
        self.assertNotIn("claim", cell)

    def test_completion_cannot_borrow_marker_from_another_attempt(self):
        manifest = self.root / "CAMPAIGN_MANIFEST.json"
        attempt_dir = self.root / "attempt-1"
        attempt_dir.mkdir()
        manifest.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "campaignId": "c3",
                    "protocol": {},
                    "cells": [
                        {
                            "cellId": "a",
                            "fingerprint": "f-a",
                            "status": "running",
                            "dependencies": [],
                            "claim": {"worker": "w1", "token": "t1"},
                            "attempts": [
                                {
                                    "attempt": 1,
                                    "runId": "r1",
                                    "status": "running",
                                    "attemptPath": str(attempt_dir),
                                }
                            ],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        foreign = self.root / "foreign"
        foreign.mkdir()
        marker = foreign / "DONE"
        result = foreign / "result.json"
        marker.write_text("ok\n", encoding="utf-8")
        result.write_text("{}", encoding="utf-8")
        completed = run(
            "complete",
            manifest,
            "--cell",
            "a",
            "--token",
            "t1",
            "--run-id",
            "r1",
            "--marker",
            marker,
            "--artifact",
            f"result={result}",
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("inside active attempt path", completed.stderr)


if __name__ == "__main__":
    unittest.main()
