#!/usr/bin/env python3
"""Validate FIRM's Claude Code skills and release metadata with stdlib only."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "auto-paper-improvement-loop",
    "baseline",
    "experiment-plan",
    "frontier-direction-discovery",
    "method-primitive-synthesis",
    "monitor-experiment",
    "paper-writing",
    "research-audit",
    "research-contract",
    "research-lit",
    "research-pipeline",
    "research-review",
    "research-state-audit",
    "resubmit-pipeline",
    "run-experiment",
    "signal-analysis",
}
BANNED: dict[str, re.Pattern[str]] = {}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
NAMESPACED_SKILL_RE = re.compile(r"/firm:([a-z0-9-]+)")
TRUTHY = {"true", "yes", "on", "1"}
FALSY = {"false", "no", "off", "0"}
DEMO_LEAKAGE = (
    "do not close the field",
    "do not launch more seeds",
    "identify the load-bearing failed component",
)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated YAML frontmatter")
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}: malformed frontmatter line: {raw!r}")
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data


def check_relative_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in LINK_RE.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link: {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    names = {path.parent.name for path in skill_files}

    if names != EXPECTED:
        missing = sorted(EXPECTED - names)
        extra = sorted(names - EXPECTED)
        if missing:
            errors.append(f"missing skills: {', '.join(missing)}")
        if extra:
            errors.append(f"unexpected skills: {', '.join(extra)}")

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        if line_count > 500:
            errors.append(f"{path.relative_to(ROOT)}: {line_count} lines (limit 500)")

        try:
            fm = parse_frontmatter(text, path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        for key in ("name", "description"):
            if not fm.get(key):
                errors.append(f"{path.relative_to(ROOT)}: missing frontmatter key {key}")
        if fm.get("name") != path.parent.name:
            errors.append(
                f"{path.relative_to(ROOT)}: name {fm.get('name')!r} does not match directory"
            )
        if len(fm.get("description", "")) < 40:
            errors.append(f"{path.relative_to(ROOT)}: description is too vague")
        listing_text = fm.get("description", "").strip()
        if len(listing_text) > 1536:
            errors.append(
                f"{path.relative_to(ROOT)}: description + when_to_use exceeds 1536 characters"
            )
        for boolean_key in ("disable-model-invocation", "user-invocable", "background"):
            value = fm.get(boolean_key)
            if value and value.lower() not in TRUTHY | FALSY:
                errors.append(
                    f"{path.relative_to(ROOT)}: invalid boolean for {boolean_key}: {value!r}"
                )
        if fm.get("background") and fm.get("context") != "fork":
            errors.append(
                f"{path.relative_to(ROOT)}: background is only valid with context: fork"
            )

        errors.extend(check_relative_links(path, text))

    # Validate all Markdown links in references and top-level public docs.
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        errors.extend(check_relative_links(path, path.read_text(encoding="utf-8")))

    searchable = []
    for path in ROOT.rglob("*"):
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() in {
            ".md", ".sh", ".py", ".html", ".json", ""
        }:
            try:
                searchable.append((path, path.read_text(encoding="utf-8")))
            except UnicodeDecodeError:
                pass
    for label, pattern in BANNED.items():
        for path, text in searchable:
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: banned pattern: {label}")

    # Every documented plugin command must resolve to a shipped skill.
    for path, text in searchable:
        for command in NAMESPACED_SKILL_RE.findall(text):
            if command not in EXPECTED:
                errors.append(
                    f"{path.relative_to(ROOT)}: unknown namespaced skill /firm:{command}"
                )

    # The public demo must not reveal the scientific conclusion in its prompt.
    demo_prompt = (ROOT / "demo/fixture/PROMPT.md").read_text(encoding="utf-8").lower()
    for leaked_phrase in DEMO_LEAKAGE:
        if leaked_phrase in demo_prompt:
            errors.append(
                f"demo/fixture/PROMPT.md: answer leakage: {leaked_phrase!r}"
            )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required_command in (
        "/plugin marketplace add Zarien-Li/FIRM",
        "/plugin install firm@firm-research",
        "/reload-plugins",
    ):
        if required_command not in readme:
            errors.append(f"README.md: missing installation command {required_command!r}")
    if "firm audit" in readme:
        errors.append("README.md: documents unsupported command 'firm audit'")

    manifests = [
        ROOT / ".claude-plugin/plugin.json",
        ROOT / ".claude-plugin/marketplace.json",
    ]
    for path in manifests:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    try:
        plugin = json.loads(manifests[0].read_text(encoding="utf-8"))
        market = json.loads(manifests[1].read_text(encoding="utf-8"))
        listing = market["plugins"][0]
        if plugin.get("name") != "firm" or listing.get("name") != "firm":
            errors.append("plugin name must be 'firm' in both manifests")
        if plugin.get("version") != market.get("version"):
            errors.append("plugin and marketplace release versions do not match")
        if "version" in listing:
            errors.append("declare the plugin version only in plugin.json, not twice")
        if market.get("name") != "firm-research":
            errors.append("marketplace name must be 'firm-research'")
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"plugin metadata is incomplete: {exc}")

    if errors:
        print("FIRM validation failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("FIRM validation passed.")
    print(f"  skills: {len(skill_files)}")
    print("  max SKILL.md lines:", max(len(p.read_text(encoding='utf-8').splitlines()) for p in skill_files))
    print("  plugin: firm@firm-research")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
