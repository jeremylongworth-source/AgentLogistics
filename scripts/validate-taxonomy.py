from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TABLE_SKILL_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*(?:CORE|ADVANCED|SPECIALIST|DEFER|MERGE|SPLIT|REMOVE)\s*\|"
)
REQUIRED_TOKEN = "AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY"


def extract_skill_names(taxonomy_text: str) -> list[str]:
    names: list[str] = []
    for line in taxonomy_text.splitlines():
        match = TABLE_SKILL_RE.match(line)
        if match:
            names.append(match.group(1))
    return names


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    taxonomy_path = repo_root / "docs" / "architecture" / "master-taxonomy-v1.md"
    audit_path = repo_root / "docs" / "architecture" / "taxonomy-audit.md"
    dependency_path = repo_root / "docs" / "architecture" / "dependency-map.md"
    handoff_path = repo_root / "docs" / "development" / "handoffs" / "AL-02-final-handoff.md"

    for path in (taxonomy_path, audit_path, dependency_path, handoff_path):
        if not path.is_file():
            errors.append(f"Missing AL-02 artifact: {path.relative_to(repo_root)}")

    if not taxonomy_path.is_file():
        return errors

    taxonomy_text = taxonomy_path.read_text(encoding="utf-8")
    names = extract_skill_names(taxonomy_text)

    if REQUIRED_TOKEN not in taxonomy_text:
        errors.append("master-taxonomy-v1.md: missing AL-02 completion token")

    if len(names) < 160:
        errors.append(f"master-taxonomy-v1.md: expected at least 160 skills, found {len(names)}")

    bad_names = [name for name in names if not SKILL_NAME_RE.match(name)]
    for name in bad_names:
        errors.append(f"master-taxonomy-v1.md: invalid skill slug {name}")

    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    for name in duplicates:
        errors.append(f"master-taxonomy-v1.md: duplicate skill slug {name}")

    for path in (audit_path, dependency_path, handoff_path):
        if path.is_file() and REQUIRED_TOKEN not in path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(repo_root)}: missing AL-02 completion token")

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

    taxonomy_path = repo_root / "docs" / "architecture" / "master-taxonomy-v1.md"
    count = len(extract_skill_names(taxonomy_path.read_text(encoding="utf-8")))
    print(f"Validated {count} taxonomy skill candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
