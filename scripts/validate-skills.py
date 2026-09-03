from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)

REQUIRED_SECTIONS = (
    "Overview",
    "Triggers",
    "Non-Triggers",
    "Required Inputs",
    "Optional Inputs",
    "Assumptions",
    "Core Workflow",
    "Calculations",
    "Validation",
    "Exception Handling",
    "Source Usage",
    "Output Contract",
    "Safety Requirements",
    "References",
    "Examples",
    "Testing",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def taxonomy_names(repo_root: Path) -> set[str]:
    taxonomy_path = repo_root / "docs" / "architecture" / "master-taxonomy-v1.md"
    if not taxonomy_path.is_file():
        return set()

    text = taxonomy_path.read_text(encoding="utf-8")
    return set(re.findall(r"\|\s*`([^`]+)`\s*\|", text))


def skill_paths(repo_root: Path) -> list[Path]:
    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        return []
    return sorted(skills_root.glob("*/*/SKILL.md"))


def check_required_sections(relative: Path, text: str) -> list[str]:
    errors: list[str] = []
    positions: list[int] = []

    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^## {re.escape(section)}\s*$", text, re.MULTILINE)
        if not match:
            errors.append(f"{relative}: missing required section ## {section}")
            continue
        positions.append(match.start())

    if len(positions) == len(REQUIRED_SECTIONS) and positions != sorted(positions):
        errors.append(f"{relative}: required sections are not in standard order")

    return errors


def validate_skill(repo_root: Path, path: Path, known_taxonomy_names: set[str]) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    skill_dir = path.parent
    skill_name = skill_dir.name
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    if PLACEHOLDER_RE.search(text):
        errors.append(f"{relative}: unresolved placeholder marker")

    if not SKILL_NAME_RE.match(skill_name):
        errors.append(f"{relative}: invalid skill directory name {skill_name}")

    if frontmatter.get("name") != skill_name:
        errors.append(f"{relative}: frontmatter name must match directory {skill_name}")

    description = frontmatter.get("description", "")
    if len(description) < 40 or PLACEHOLDER_RE.search(description):
        errors.append(f"{relative}: frontmatter description is missing or too weak")

    if frontmatter.get("license") != "MIT":
        errors.append(f"{relative}: frontmatter license must be MIT")

    if skill_name not in known_taxonomy_names:
        errors.append(f"{relative}: skill name is not listed in master taxonomy")

    errors.extend(check_required_sections(relative, text))

    agent_config = skill_dir / "agents" / "openai.yaml"
    if not agent_config.is_file():
        errors.append(f"{relative}: missing agents/openai.yaml")
    else:
        config_text = agent_config.read_text(encoding="utf-8")
        config_relative = agent_config.relative_to(repo_root)
        for required in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if required not in config_text:
                errors.append(f"{config_relative}: missing {required}")
        if f"${skill_name}" not in config_text:
            errors.append(f"{config_relative}: default prompt must mention ${skill_name}")
        if PLACEHOLDER_RE.search(config_text):
            errors.append(f"{config_relative}: unresolved placeholder marker")

    references_dir = skill_dir / "references"
    if not references_dir.is_dir():
        errors.append(f"{relative}: missing references directory")
    else:
        reference_files = sorted(references_dir.glob("*.md"))
        if not reference_files:
            errors.append(f"{relative}: references directory has no markdown references")
        for reference_path in reference_files:
            reference_text = reference_path.read_text(encoding="utf-8").strip()
            reference_relative = reference_path.relative_to(repo_root)
            if len(reference_text) < 100:
                errors.append(f"{reference_relative}: reference content is too short")
            if PLACEHOLDER_RE.search(reference_text):
                errors.append(f"{reference_relative}: unresolved placeholder marker")

    return errors


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    paths = skill_paths(repo_root)
    known_taxonomy_names = taxonomy_names(repo_root)

    if not paths:
        errors.append("No skills found under skills/<domain>/<skill>/SKILL.md")
        return errors

    for path in paths:
        errors.extend(validate_skill(repo_root, path, known_taxonomy_names))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(skill_paths(repo_root))} skill package(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
