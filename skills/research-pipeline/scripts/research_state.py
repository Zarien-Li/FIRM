"""Maintain research memory and immutable comparison identities, not research policy."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile


SKILL = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def publish_new(path, value):
    """Publish a complete immutable receipt without replacing any existing writer."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def local(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Record path escapes project: {name}")
    return path


def artifact(root, name):
    # Explicit absolute paths support authorized external artifact/data disks.
    path = Path(name)
    return path.resolve() if path.is_absolute() else local(root, name)


def snapshot(root, folder, value):
    fingerprint = digest(value)
    path = local(root, f".research/{folder}/{fingerprint}.json")
    if path.exists():
        if read(path) != value:
            raise ValueError(f"Modified immutable snapshot: {path}")
    else:
        write(path, value)
    return {"path": str(path.relative_to(root)), "sha256": fingerprint}


def state_and_contract(root):
    state = read(root / "PROJECT_STATE.json")
    contract = read(local(root, state["comparison_contract"]))
    if state.get("schema_version") != 1 or contract.get("schema_version") != 1:
        raise ValueError("Unsupported memory format version")
    def require(obj, key, types):
        if key not in obj or not isinstance(obj[key], types):
            raise ValueError(f"Missing or malformed field: {key}")

    for key in ("program", "focus", "nodes", "last_change"):
        require(state, key, dict)
    require(state["program"], "objective", (str, type(None)))
    require(state["program"], "authority", list)
    require(state["focus"], "node_id", str)
    require(contract, "comparisons", dict)
    for key in ("claims", "execution_refs", "manuscript_dependencies"):
        require(state, key, list)
    nodes = state["nodes"]
    for node in nodes.values():
        if not isinstance(node, dict):
            raise ValueError("Research node must be an object")
        require(node, "parent", (str, type(None)))
        require(node, "statement", (str, type(None)))
        for key in ("evidence", "comparison_ids", "depends_on", "unresolved"):
            require(node, key, list)
    if not nodes or len([n for n in nodes.values() if n["parent"] is None]) != 1:
        raise ValueError("Research tree needs one root")
    for ident, node in nodes.items():
        seen, current = set(), ident
        while current is not None:
            if current in seen or current not in nodes:
                raise ValueError(f"Broken ancestry at {ident}")
            seen.add(current)
            current = nodes[current]["parent"]
        if any(d not in nodes for d in node.get("depends_on", [])):
            raise ValueError(f"Unknown dependency at {ident}")
        for comparison in node.get("comparison_ids", []):
            if comparison not in contract["comparisons"]:
                raise ValueError(f"Unknown comparison at {ident}: {comparison}")
        for evidence in node.get("evidence", []):
            if not isinstance(evidence, dict):
                raise ValueError(f"Malformed evidence at {ident}")
            for key in ("artifact", "observation", "bearing"):
                require(evidence, key, str)
    if state["focus"]["node_id"] not in nodes:
        raise ValueError("Focus references an unknown node")
    for claim in state.get("claims", []):
        if not isinstance(claim, dict):
            raise ValueError("Claim must be an object")
        require(claim, "id", str)
        require(claim, "statement", (str, type(None)))
        require(claim, "missing_comparisons", list)
        for comparison in claim.get("missing_comparisons", []):
            if comparison not in contract["comparisons"]:
                raise ValueError(f"Unknown comparison in claim: {comparison}")
    return state, contract


def init(root):
    sources = {
        "PROJECT_STATE.json": SKILL / "assets/PROJECT_STATE.template.json",
        "COMPARISON_CONTRACT.json": SKILL.parent / "research-foundation/assets/COMPARISON_CONTRACT.template.json",
    }
    if any((root / name).exists() for name in sources):
        raise ValueError("Existing memory or contract; reconcile it instead of overwriting")
    for name, source in sources.items():
        write(root / name, read(source))


def bind_run(root, record, node, comparison, effective_config, deviations):
    state, contract = state_and_contract(root)
    if node not in state["nodes"] or comparison not in contract["comparisons"]:
        raise ValueError("Run references unknown research node or comparison")
    path = artifact(root, record)
    run = read(path)
    receipt = path.with_name(path.name + ".comparison.json")
    if receipt.exists() or "comparison_binding" in run:
        raise ValueError("Run already bound; preserve it and use a separate actual attempt")
    if not isinstance(run.get("run_id"), str) or not run["run_id"]:
        raise ValueError("Existing run record needs its stable run_id")
    config = read(artifact(root, effective_config))
    departures = read(artifact(root, deviations))
    if not isinstance(config, dict) or not isinstance(departures, list):
        raise ValueError("Effective config must be an object; deviations must be an array")
    if any(not isinstance(d, dict) or not all(k in d for k in
           ("field", "expected", "observed", "consequence")) for d in departures):
        raise ValueError("Deviation needs field, expected, observed, and consequence")
    binding = {
        "run_id": run["run_id"],
        "node_id": node,
        "comparison_id": comparison,
        "contract": snapshot(root, "contracts", contract),
        "effective_config": snapshot(root, "configs", config),
        "deviations": departures,
    }
    publish_new(receipt, binding)
    return receipt


def verify_binding(root, record):
    path = artifact(root, record)
    run = read(path)
    binding = read(path.with_name(path.name + ".comparison.json"))
    if binding["run_id"] != run["run_id"]:
        raise ValueError("Run identity differs from its immutable comparison receipt")
    state, _ = state_and_contract(root)
    if binding["node_id"] not in state["nodes"]:
        raise ValueError(f"Missing research node in {record}")
    for key in ("contract", "effective_config"):
        ref = binding[key]
        if digest(read(local(root, ref["path"]))) != ref["sha256"]:
            raise ValueError(f"Fingerprint mismatch: {record} {key}")
    pinned_contract = read(local(root, binding["contract"]["path"]))
    if binding["comparison_id"] not in pinned_contract["comparisons"]:
        raise ValueError(f"Missing pinned comparison: {record}")
    return binding


def render(state):
    def prose(value):
        return str(value) if value is not None else "Not yet established"

    focus = state["focus"]
    lines = ["# Project Research Tree", "", "> Generated from PROJECT_STATE.json; edit the JSON, not this view.",
             "", "## Original Objective", prose(state["program"]["objective"]),
             "", "## Current Investment", f"Node: `{focus['node_id']}`",
             prose(focus.get("reason")), "Return question: " + prose(focus.get("return_question")),
             "", "## Scientific Change"]
    for key, value in state["last_change"].items():
        lines.append(f"- {key.replace('_', ' ')}: {prose(value)}")
    lines.extend(["", "## Research Tree"])

    def visit(ident, depth):
        node = state["nodes"][ident]
        prefix = "  " * depth
        mark = " [current investment]" if ident == focus["node_id"] else ""
        lines.append(f"{prefix}- `{ident}` ({node.get('kind', 'research')}){mark}: {prose(node['statement'])}")
        for key in ("rationale", "interpretation", "unresolved", "next_action", "comparison_ids", "depends_on"):
            if node.get(key):
                lines.append(f"{prefix}  - {key.replace('_', ' ')}: {node[key]}")
        for item in node.get("evidence", []):
            lines.append(f"{prefix}  - evidence `{item['artifact']}`: {item['observation']} ({item['bearing']})")
        for child, data in state["nodes"].items():
            if data["parent"] == ident:
                visit(child, depth + 1)

    root = next(k for k, n in state["nodes"].items() if n["parent"] is None)
    visit(root, 0)
    lines.extend(["", "## Current Claims"])
    for claim in state.get("claims", []):
        lines.append(f"- `{claim['id']}`: {claim['statement']}")
        for key in ("evidence", "missing_comparisons", "qualification"):
            if claim.get(key):
                lines.append(f"  - {key.replace('_', ' ')}: {claim[key]}")
    for key in ("execution_refs", "manuscript_dependencies"):
        if state.get(key):
            lines.extend(["", "## " + key.replace("_", " ").title()])
            lines.extend(f"- {item}" for item in state[key])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("init", "seal", "bind-run", "check", "render"))
    parser.add_argument("project", type=Path)
    parser.add_argument("--record", help="Existing JSON run record; use an explicit absolute path for external artifacts")
    parser.add_argument("--node")
    parser.add_argument("--comparison")
    parser.add_argument("--effective-config")
    parser.add_argument("--deviations")
    args = parser.parse_args()
    root = args.project.resolve()
    try:
        if args.action == "init":
            init(root)
            print("Initialized unknown science; fill from authority and evidence.")
            return
        state, contract = state_and_contract(root)
        if args.action == "seal":
            print(json.dumps(snapshot(root, "contracts", contract)))
        elif args.action == "bind-run":
            if not all((args.record, args.node, args.comparison, args.effective_config, args.deviations)):
                raise ValueError("bind-run requires record, node, comparison, effective-config, deviations")
            receipt = bind_run(root, args.record, args.node, args.comparison, args.effective_config, args.deviations)
            print(f"Comparison receipt: {receipt}; scientific comparability has not been assessed.")
        elif args.action == "check":
            if args.record:
                verify_binding(root, args.record)
            print("Structure/references checked" + ("; run fingerprints checked" if args.record else "")
                  + ". Not a verification of scientific claims or artifact contents.")
        elif args.action == "render":
            path = root / "PROJECT_STATE.md"
            marker = "> Generated from PROJECT_STATE.json; edit the JSON, not this view."
            if path.exists() and marker not in path.read_text(encoding="utf-8"):
                raise ValueError("Existing prose state; reconcile and preserve it before rendering")
            path.write_text(render(state), encoding="utf-8")
            print(path)
    except (OSError, ValueError, KeyError, TypeError, RecursionError) as error:
        parser.exit(1, f"Memory error: {error}\n")


if __name__ == "__main__":
    main()
