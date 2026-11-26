import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import concurrent.futures
import threading


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/research_state.py"
SPEC = importlib.util.spec_from_file_location("research_state", SCRIPT)
memory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(memory)


class ResearchMemoryTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name).resolve()
        memory.init(self.root)

    def add_branch(self):
        path = self.root / "PROJECT_STATE.json"
        state = memory.read(path)
        branch = copy.deepcopy(state["nodes"]["program"])
        branch.update(parent="program", kind="implementation", statement="Paired training",
                      interpretation="Promising development result, formal gap unmeasured",
                      comparison_ids=["main"])
        state["nodes"]["candidate"] = branch
        state["focus"].update(node_id="candidate", reason="Test signal coverage",
                              return_question="Does the signal express the intended distinction?")
        memory.write(path, state)

    def bind(self):
        self.add_branch()
        memory.write(self.root / "run.json", {"run_id": "r1", "execution": "completed"})
        memory.write(self.root / "effective.json", {"input_length": 512})
        memory.write(self.root / "departures.json", [{"field": "input_length", "expected": 96,
                     "observed": 512, "consequence": "Not the commissioned paired comparison"}])
        memory.bind_run(self.root, "run.json", "candidate", "main", "effective.json", "departures.json")
        return memory.verify_binding(self.root, "run.json")

    def test_initialization_leaves_unknown_science(self):
        state, _ = memory.state_and_contract(self.root)
        self.assertIsNone(state["program"]["objective"])
        self.assertEqual(state["claims"], [])

    def test_existing_memory_not_overwritten(self):
        with self.assertRaises(ValueError):
            memory.init(self.root)

    def test_tree_missing_parent_and_cycles_rejected(self):
        self.add_branch()
        path = self.root / "PROJECT_STATE.json"
        state = memory.read(path)
        state["nodes"]["candidate"]["parent"] = "unknown"
        memory.write(path, state)
        with self.assertRaises(ValueError):
            memory.state_and_contract(self.root)
        state["nodes"]["candidate"]["parent"] = "candidate"
        memory.write(path, state)
        with self.assertRaises(ValueError):
            memory.state_and_contract(self.root)

    def test_hash_ignores_json_format_and_key_order(self):
        self.assertEqual(memory.digest({"a": 1, "b": 2}), memory.digest({"b": 2, "a": 1}))

    def test_contract_revision_preserves_old_binding(self):
        binding = self.bind()
        path = self.root / "COMPARISON_CONTRACT.json"
        revised = memory.read(path)
        revised["comparisons"]["main"]["inputs_retrieval_tools"] = "Matched long context"
        memory.write(path, revised)
        second = memory.snapshot(self.root, "contracts", revised)
        self.assertNotEqual(binding["contract"]["sha256"], second["sha256"])
        self.assertEqual(memory.verify_binding(self.root, "run.json"), binding)

    def test_actual_config_and_deviations_are_pinned_without_verdict(self):
        binding = self.bind()
        self.assertEqual(memory.read(self.root / binding["effective_config"]["path"]), {"input_length": 512})
        self.assertEqual(binding["deviations"][0]["expected"], 96)
        self.assertNotIn("eligible", binding)
        self.assertEqual(memory.read(self.root / "PROJECT_STATE.json")["claims"], [])

    def test_tampered_snapshot_detected(self):
        binding = self.bind()
        memory.write(self.root / binding["effective_config"]["path"], {"input_length": 96})
        with self.assertRaises(ValueError):
            memory.verify_binding(self.root, "run.json")

    def test_cannot_rebind_existing_run(self):
        self.bind()
        with self.assertRaises(ValueError):
            memory.bind_run(self.root, "run.json", "candidate", "main", "effective.json", "departures.json")

    def test_binding_does_not_overwrite_concurrent_completion(self):
        self.add_branch()
        path = self.root / "run.json"
        memory.write(path, {"run_id": "r1", "execution": "running"})
        memory.write(self.root / "effective.json", {})
        memory.write(self.root / "departures.json", [])
        original = memory.snapshot

        def completed_during_binding(*args):
            memory.write(path, {"run_id": "r1", "execution": "completed", "metric": 0.7})
            return original(*args)

        with mock.patch.object(memory, "snapshot", side_effect=completed_during_binding):
            memory.bind_run(self.root, "run.json", "candidate", "main", "effective.json", "departures.json")
        self.assertEqual(memory.read(path)["metric"], 0.7)
        memory.verify_binding(self.root, "run.json")

    def test_concurrent_receipts_cannot_replace_each_other(self):
        barrier = threading.Barrier(2)
        path = self.root / "receipt.json"

        def contender(value):
            barrier.wait()
            try:
                memory.publish_new(path, value)
                return value
            except FileExistsError:
                return None

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(contender, [{"a": 1}, {"a": 2}]))
        winners = [v for v in outcomes if v is not None]
        self.assertEqual(len(winners), 1)
        self.assertEqual(memory.read(path), winners[0])

    def test_missing_renderer_field_fails_check(self):
        path = self.root / "PROJECT_STATE.json"
        state = memory.read(path)
        del state["nodes"]["program"]["statement"]
        memory.write(path, state)
        with self.assertRaises(ValueError):
            memory.state_and_contract(self.root)

    def test_receipt_does_not_follow_reused_run_identity(self):
        self.bind()
        memory.write(self.root / "run.json", {"run_id": "different"})
        with self.assertRaises(ValueError):
            memory.verify_binding(self.root, "run.json")

    def test_unknown_comparison_rejected(self):
        self.add_branch()
        path = self.root / "PROJECT_STATE.json"
        state = memory.read(path)
        state["nodes"]["candidate"]["comparison_ids"] = ["missing"]
        memory.write(path, state)
        with self.assertRaises(ValueError):
            memory.state_and_contract(self.root)

    def test_child_outcome_does_not_rewrite_parent_or_claims(self):
        self.add_branch()
        state, _ = memory.state_and_contract(self.root)
        state["nodes"]["candidate"]["interpretation"] = "Failed against the matched rival"
        memory.write(self.root / "PROJECT_STATE.json", state)
        parent = copy.deepcopy(state["nodes"]["program"])
        view = memory.render(state)
        self.assertIn("candidate", view)
        self.assertEqual(memory.read(self.root / "PROJECT_STATE.json")["nodes"]["program"], parent)
        self.assertEqual(state["claims"], [])

    def test_render_preserves_unmigrated_prose(self):
        path = self.root / "PROJECT_STATE.md"
        path.write_text("Existing independent state", encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), "render", str(self.root)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(path.read_text(), "Existing independent state")

    def test_cli_roundtrip_checks_binding_and_renders(self):
        self.bind()
        for action, args in [("check", ["--record", "run.json"]), ("render", [])]:
            result = subprocess.run([sys.executable, str(SCRIPT), action, str(self.root), *args],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("candidate", (self.root / "PROJECT_STATE.md").read_text())

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            memory.local(self.root, "../outside.json")

    def test_external_run_stays_on_explicit_artifact_disk(self):
        self.add_branch()
        with tempfile.TemporaryDirectory() as external:
            record = Path(external) / "run.json"
            config = Path(external) / "effective.json"
            departures = Path(external) / "deviations.json"
            memory.write(record, {"run_id": "external"})
            memory.write(config, {"resolved": True})
            memory.write(departures, [])
            memory.bind_run(self.root, str(record), "candidate", "main", str(config), str(departures))
            self.assertEqual(memory.verify_binding(self.root, str(record))["node_id"], "candidate")
            self.assertFalse((self.root / "run.json").exists())


if __name__ == "__main__":
    unittest.main()
