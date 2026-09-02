#!/usr/bin/env python3
"""Check packaging and progressive-disclosure structure without encoding science."""

from __future__ import annotations

import re
from pathlib import Path


HERE = Path(__file__).resolve()
PACKAGE_ROOT = HERE.parents[3]
PACKAGED = (PACKAGE_ROOT / "managed-skills.txt").is_file()

if PACKAGED:
    ROOT = PACKAGE_ROOT
    SKILLS = ROOT / "skills"
    SKILL_MANIFEST = ROOT / "managed-skills.txt"
else:
    SKILLS = HERE.parents[2]
    ROOT = SKILLS.parent
    SKILL_MANIFEST = SKILLS / ".research-skills-managed"

PI = SKILLS / "research-pipeline"
PI_ENTRY = PI / "SKILL.md"
PI_REFERENCES = {
    "collaboration.md",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def manifest_entries(path: Path) -> set[str]:
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path}: invalid frontmatter")
    block = text[4 : text.find("\n---\n", 4)]
    data = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("\"'")
    return data


def relative_link_errors(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes package: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken link: {target}")
    return errors


def main() -> int:
    failures: list[str] = []

    if not PI_ENTRY.is_file():
        failures.append("missing existing research-pipeline PI entrypoint")
    else:
        try:
            metadata = frontmatter(PI_ENTRY)
            if metadata.get("name") != "research-pipeline":
                failures.append("research-pipeline frontmatter name changed")
            description = metadata.get("description", "")
            if not description or len(description) > 1536:
                failures.append("research-pipeline description is missing or oversized")
        except ValueError as exc:
            failures.append(str(exc))

        if len(PI_ENTRY.read_text(encoding="utf-8").splitlines()) > 300:
            failures.append("research-pipeline entrypoint exceeds 300 lines")

    actual_pi_references = {
        path.name for path in (PI / "references").glob("*.md") if path.is_file()
    }
    if actual_pi_references != PI_REFERENCES:
        failures.append(
            "research-pipeline focused references mismatch: "
            f"missing={sorted(PI_REFERENCES - actual_pi_references)}, "
            f"extra={sorted(actual_pi_references - PI_REFERENCES)}"
        )

    for path in [PI_ENTRY, *(PI / "references").glob("*.md")]:
        if path.is_file():
            failures.extend(relative_link_errors(path))

    manifest = manifest_entries(SKILL_MANIFEST)
    actual = {
        path.name
        for path in SKILLS.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if not manifest.issubset(actual):
        failures.append(f"managed skills missing: {sorted(manifest - actual)}")
    if PACKAGED and actual != manifest:
        failures.append(f"unmanaged packaged skills present: {sorted(actual - manifest)}")

    residue_roots = [SKILLS / name for name in manifest]
    residue = [
        str(path.relative_to(ROOT))
        for base in residue_roots
        for path in base.rglob("*")
        if path.name == "__pycache__" or (path.is_file() and path.suffix == ".pyc")
    ]
    if residue:
        failures.append(f"generated Python residue present: {residue}")

    if failures:
        print("Research packaging contract failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Research packaging contract passed "
        f"({len(manifest)} skills; one GPT PI plus five on-demand tools)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
