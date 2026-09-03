from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


COMPLETION_TOKEN = "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY"
PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)
REQUIRED_SHARED_FILES = (
    "shared/README.md",
    "shared/glossaries/common-units.md",
    "shared/glossaries/inventory-state-terms.md",
    "shared/formulas/reorder-point.md",
    "shared/schemas/reorder-point-calculation.schema.json",
    "shared/templates/calculation-output.md",
)
TEXT_EXTENSIONS = {".md", ".py", ".ps1", ".yaml", ".yml", ".json"}
IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def text_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        relative_parts = path.relative_to(repo_root).parts
        if any(part in IGNORED_DIRS for part in relative_parts):
            continue
        files.append(path)
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_json_schema(repo_root: Path, relative: str, text: str) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    for key in ("$schema", "$id", "title", "type", "required", "properties"):
        if key not in data:
            errors.append(f"{relative}: missing schema key {key}")

    if data.get("x-agentlogistics-completion-token") != COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-05 completion token")

    required = set(data.get("required", []))
    for key in ("schema", "skill", "completion_token", "cases"):
        if key not in required:
            errors.append(f"{relative}: required list missing {key}")

    return errors


def validate_required_files(repo_root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_SHARED_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing AL-05 shared file: {relative}")
            continue

        text = read_text(path)
        if PLACEHOLDER_RE.search(text):
            errors.append(f"{relative}: unresolved placeholder marker")

        if path.suffix.lower() == ".json":
            errors.extend(validate_json_schema(repo_root, relative, text))
        elif COMPLETION_TOKEN not in text:
            errors.append(f"{relative}: missing AL-05 completion token")

    return errors


def validate_active_consumers(repo_root: Path) -> list[str]:
    errors: list[str] = []
    all_files = text_files(repo_root)

    for relative in REQUIRED_SHARED_FILES:
        normalized = relative.replace("\\", "/")
        consumers: list[Path] = []
        for path in all_files:
            path_relative = path.relative_to(repo_root).as_posix()
            if path_relative == normalized:
                continue
            text = read_text(path).replace("\\", "/")
            if normalized in text:
                consumers.append(path)

        if not consumers:
            errors.append(f"{relative}: no active consumer references this shared file")

    return errors


def validate_fixture_schema_reference(repo_root: Path) -> list[str]:
    fixture_path = repo_root / "tests" / "fixtures" / "calculate-reorder-point-cases.json"
    if not fixture_path.is_file():
        return ["Missing reorder point fixture for shared schema validation"]

    data = json.loads(read_text(fixture_path))
    expected_schema = "shared/schemas/reorder-point-calculation.schema.json"
    if data.get("schema") != expected_schema:
        return [f"{fixture_path.relative_to(repo_root)}: schema must be {expected_schema}"]
    return []


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    shared_root = repo_root / "shared"

    if not shared_root.is_dir():
        return ["Missing shared directory"]

    errors.extend(validate_required_files(repo_root))
    errors.extend(validate_active_consumers(repo_root))
    errors.extend(validate_fixture_schema_reference(repo_root))
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

    print(f"Validated {len(REQUIRED_SHARED_FILES)} shared foundation file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
