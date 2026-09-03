from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


COMPLETION_TOKEN = "AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY"
REQUIRED_WAREHOUSE_SKILLS = {
    "analyze-logistics-operation",
    "map-logistics-flow",
    "identify-logistics-constraints",
    "analyze-product-flow",
    "analyze-order-profile",
    "plan-inbound-receiving",
    "verify-inbound-shipment",
    "inspect-received-goods",
    "reconcile-asn",
    "process-receiving-discrepancy",
    "plan-putaway",
    "diagnose-receiving-bottleneck",
    "classify-storage-requirements",
    "calculate-storage-capacity",
    "calculate-pallet-positions",
    "analyze-storage-utilization",
    "plan-replenishment",
    "select-picking-strategy",
    "calculate-pick-productivity",
    "plan-packing-operation",
    "plan-shipping-stage",
    "verify-outbound-shipment",
}
REQUIRED_FLOW_STEPS = [
    "receive",
    "inspect",
    "putaway",
    "store",
    "replenish",
    "pick",
    "pack",
    "stage",
    "ship",
]
REQUIRED_README_HEADINGS = (
    "## Purpose",
    "## Included Skills",
    "## End-To-End Flow",
    "## Routing Rules",
    "## Evidence Boundaries",
    "## Safety Rules",
    "## Acceptance Criteria",
    "## Validation",
)


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_manifest(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "name": None,
        "description": None,
        "completion_token": None,
        "skills": [],
        "agents_file": None,
        "scenario_file": None,
        "fixture_file": None,
    }
    current: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        scalar = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if scalar:
            key, value = scalar.group(1), scalar.group(2).strip()
            if key == "skills" and not value:
                current = "skills"
            elif key in result:
                result[key] = clean_scalar(value)
                current = None
            else:
                current = None
            continue

        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item and current == "skills":
            result["skills"].append(clean_scalar(item.group(1)))

    return result


def skill_names(repo_root: Path) -> set[str]:
    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        return set()
    return {path.parent.name for path in skills_root.glob("*/*/SKILL.md")}


def duplicate_items(items: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


def validate_readme(path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing skillset README: {relative}"]

    text = path.read_text(encoding="utf-8")
    if COMPLETION_TOKEN not in text:
        errors.append(f"{relative}: missing AL-06 completion token")
    for heading in REQUIRED_README_HEADINGS:
        if heading not in text:
            errors.append(f"{relative}: missing heading {heading}")
    return errors


def validate_agents_file(path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing skillset agents file: {relative}"]

    text = path.read_text(encoding="utf-8")
    for phrase in ("interface:", "display_name:", "short_description:", "default_prompt:", "$warehouse-operator"):
        if phrase not in text:
            errors.append(f"{relative}: missing {phrase}")
    return errors


def validate_flow_fixture(path: Path, repo_root: Path, manifest_skills: set[str]) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing skillset flow fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "warehouse-operator":
        errors.append(f"{relative}: skillset must be warehouse-operator")
    if data.get("completion_token") != COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-06 completion token")

    flow = data.get("required_flow", [])
    steps = [step.get("step") for step in flow if isinstance(step, dict)]
    if steps != REQUIRED_FLOW_STEPS:
        errors.append(f"{relative}: required flow must be {' -> '.join(REQUIRED_FLOW_STEPS)}")

    for step in flow:
        for skill in step.get("expected_skills", []):
            if skill not in manifest_skills:
                errors.append(f"{relative}: flow skill {skill} is not in skillset manifest")

    for skill in data.get("supporting_context_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: supporting skill {skill} is not in skillset manifest")

    invariants = set(data.get("required_output_invariants", []))
    for required in ("operation boundary", "flow map", "outbound verification result", "qualified-review boundaries"):
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_skillset(repo_root: Path, skillset_dir: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    manifest_path = skillset_dir / "skillset.yaml"
    manifest_relative = manifest_path.relative_to(repo_root)
    if not manifest_path.is_file():
        return [f"Missing skillset manifest: {manifest_relative}"]

    manifest = parse_manifest(manifest_path)
    name = manifest["name"]
    skills: list[str] = manifest["skills"]

    if name != skillset_dir.name:
        errors.append(f"{manifest_relative}: name must match directory {skillset_dir.name}")
    if manifest["completion_token"] != COMPLETION_TOKEN:
        errors.append(f"{manifest_relative}: missing AL-06 completion token")
    if not manifest["description"] or len(str(manifest["description"])) < 60:
        errors.append(f"{manifest_relative}: description is missing or too weak")

    for duplicate in duplicate_items(skills):
        errors.append(f"{manifest_relative}: duplicate skill {duplicate}")
    for skill in skills:
        if skill not in known_skills:
            errors.append(f"{manifest_relative}: unknown skill {skill}")

    if name == "warehouse-operator":
        missing = sorted(REQUIRED_WAREHOUSE_SKILLS - set(skills))
        extra = sorted(set(skills) - REQUIRED_WAREHOUSE_SKILLS)
        for skill in missing:
            errors.append(f"{manifest_relative}: missing required warehouse skill {skill}")
        for skill in extra:
            errors.append(f"{manifest_relative}: unexpected warehouse skill {skill}")

    agents_file = manifest.get("agents_file")
    if agents_file:
        errors.extend(validate_agents_file(skillset_dir / str(agents_file), repo_root))
    else:
        errors.append(f"{manifest_relative}: missing agents_file")

    scenario_file = manifest.get("scenario_file")
    if not scenario_file or not (repo_root / str(scenario_file)).is_file():
        errors.append(f"{manifest_relative}: scenario_file is missing or invalid")

    fixture_file = manifest.get("fixture_file")
    if fixture_file:
        errors.extend(validate_flow_fixture(repo_root / str(fixture_file), repo_root, set(skills)))
    else:
        errors.append(f"{manifest_relative}: missing fixture_file")

    errors.extend(validate_readme(skillset_dir / "README.md", repo_root))
    return errors


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    skillsets_root = repo_root / "skillsets"
    if not skillsets_root.is_dir():
        return ["Missing skillsets directory"]

    skillset_dirs = sorted(path for path in skillsets_root.iterdir() if path.is_dir())
    if not skillset_dirs:
        return ["No skillset packages found"]

    known_skills = skill_names(repo_root)
    for skillset_dir in skillset_dirs:
        errors.extend(validate_skillset(repo_root, skillset_dir, known_skills))

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

    count = len([path for path in (repo_root / "skillsets").iterdir() if path.is_dir()])
    print(f"Validated {count} skillset package(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
