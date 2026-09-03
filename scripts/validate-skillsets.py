from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


WAREHOUSE_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY"
INVENTORY_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY"
WAREHOUSE_PLANNER_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY"
FULFILLMENT_OPTIMIZER_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY"
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
REQUIRED_INVENTORY_SKILLS = {
    "classify-inventory",
    "calculate-inventory-accuracy",
    "calculate-inventory-turns",
    "calculate-days-on-hand",
    "calculate-reorder-point",
    "calculate-safety-stock",
    "calculate-eoq",
    "design-min-max-policy",
    "design-cycle-count-program",
    "plan-physical-inventory",
    "reconcile-inventory",
    "investigate-inventory-discrepancy",
    "analyze-inventory-aging",
    "identify-dead-stock",
    "analyze-stockout",
    "manage-lot-controlled-inventory",
    "manage-serialized-inventory",
    "manage-expiration-controlled-inventory",
    "select-inventory-rotation-policy",
    "analyze-inventory-shrinkage",
}
REQUIRED_WAREHOUSE_PLANNER_SKILLS = {
    "analyze-product-flow",
    "analyze-order-profile",
    "classify-inventory",
    "calculate-inventory-turns",
    "classify-storage-requirements",
    "select-storage-system",
    "calculate-storage-capacity",
    "calculate-pallet-positions",
    "calculate-cube-utilization",
    "analyze-storage-utilization",
    "plan-reserve-storage",
    "plan-forward-pick-storage",
    "slot-warehouse-inventory",
    "analyze-slotting-efficiency",
    "optimize-storage-density",
    "evaluate-racking-strategy",
    "analyze-product-affinity",
    "optimize-pick-path",
    "calculate-warehouse-capacity",
    "forecast-capacity-requirements",
    "analyze-space-utilization",
    "plan-warehouse-zones",
    "plan-dock-capacity",
    "analyze-warehouse-flow",
    "identify-warehouse-congestion",
    "design-conceptual-warehouse-layout",
    "compare-warehouse-layouts",
    "plan-warehouse-expansion",
}
REQUIRED_FULFILLMENT_OPTIMIZER_SKILLS = {
    "analyze-order-profile",
    "plan-forward-pick-storage",
    "plan-replenishment",
    "calculate-replenishment-demand",
    "prioritize-replenishment",
    "select-picking-strategy",
    "plan-picking-wave",
    "plan-batch-picking",
    "plan-zone-picking",
    "optimize-pick-path",
    "calculate-pick-productivity",
    "analyze-pick-accuracy",
    "diagnose-picking-bottleneck",
    "investigate-picking-error",
    "plan-packing-operation",
    "plan-cartonization",
    "plan-shipping-stage",
    "plan-trailer-loading",
    "verify-outbound-shipment",
    "investigate-shipping-error",
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
REQUIRED_DISCREPANCY_CONFLICTS = (
    "receiving_quantity",
    "wms_balance",
    "physical_count",
    "picking_transactions",
    "adjustment_history",
)
REQUIRED_DISCREPANCY_INVARIANTS = (
    "source-by-source evidence table",
    "chronology",
    "quantity reconciliation",
    "no guessed root cause",
    "review or adjustment approval boundary",
)
REQUIRED_WAREHOUSE_PLANNER_COMPONENTS = (
    "storage_system_selection",
    "pallet_positions",
    "cube_utilization",
    "storage_density",
    "forward_reserve_allocation",
    "slotting",
    "sku_velocity",
    "product_affinity",
    "travel_distance",
    "warehouse_capacity",
    "dock_capacity",
    "congestion",
    "zoning",
    "conceptual_layout",
    "layout_comparison",
    "expansion_triggers",
)
REQUIRED_WAREHOUSE_PLANNER_INVARIANTS = (
    "unit-aware capacity calculations",
    "blocked-position source conflict",
    "forward versus reserve allocation",
    "slotting rationale",
    "product-affinity checks",
    "travel-distance considerations",
    "dock-capacity check",
    "congestion risks",
    "zoning concept",
    "conceptual layout not structural approval",
    "qualified-review boundary",
)
REQUIRED_FULFILLMENT_ORDER_PROFILES = (
    "low_volume_high_sku",
    "high_volume_low_sku",
    "ecommerce_each_pick",
    "case_pick",
    "pallet_movement",
    "mixed_orders",
)
REQUIRED_FULFILLMENT_INVARIANTS = (
    "order-profile-specific plan",
    "replenishment demand calculation",
    "replenishment priority queue",
    "wave planning",
    "batch picking",
    "zone picking",
    "pick-path considerations",
    "pick productivity check",
    "pick accuracy or error handoff",
    "bottleneck diagnosis",
    "cartonization constraints",
    "trailer-loading constraints",
    "outbound verification handoff",
    "shipping-error investigation",
    "qualified-review boundary",
)
REQUIRED_FULFILLMENT_CONSTRAINTS = (
    "wms_hold_status",
    "missing_item_dimensions",
    "carrier_cutoff",
    "staging_lane_conflict",
    "limited_loader_after_1400",
)
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
SKILLSET_REQUIREMENTS = {
    "warehouse-operator": {
        "completion_token": WAREHOUSE_COMPLETION_TOKEN,
        "skills": REQUIRED_WAREHOUSE_SKILLS,
        "prompt_token": "$warehouse-operator",
        "fixture_validator": "warehouse_flow",
    },
    "inventory-control-specialist": {
        "completion_token": INVENTORY_COMPLETION_TOKEN,
        "skills": REQUIRED_INVENTORY_SKILLS,
        "prompt_token": "$inventory-control-specialist",
        "fixture_validator": "inventory_discrepancy",
    },
    "warehouse-planner": {
        "completion_token": WAREHOUSE_PLANNER_COMPLETION_TOKEN,
        "skills": REQUIRED_WAREHOUSE_PLANNER_SKILLS,
        "prompt_token": "$warehouse-planner",
        "fixture_validator": "warehouse_planner",
    },
    "fulfillment-optimizer": {
        "completion_token": FULFILLMENT_OPTIMIZER_COMPLETION_TOKEN,
        "skills": REQUIRED_FULFILLMENT_OPTIMIZER_SKILLS,
        "prompt_token": "$fulfillment-optimizer",
        "fixture_validator": "fulfillment_optimizer",
    },
}


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


def validate_readme(path: Path, repo_root: Path, completion_token: str) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing skillset README: {relative}"]

    text = path.read_text(encoding="utf-8")
    if completion_token not in text:
        errors.append(f"{relative}: missing completion token {completion_token}")
    for heading in REQUIRED_README_HEADINGS:
        if heading not in text:
            errors.append(f"{relative}: missing heading {heading}")
    return errors


def validate_agents_file(path: Path, repo_root: Path, prompt_token: str) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing skillset agents file: {relative}"]

    text = path.read_text(encoding="utf-8")
    for phrase in ("interface:", "display_name:", "short_description:", "default_prompt:", prompt_token):
        if phrase not in text:
            errors.append(f"{relative}: missing {phrase}")
    return errors


def validate_flow_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
    completion_token: str,
) -> list[str]:
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
    if data.get("completion_token") != completion_token:
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


def validate_inventory_discrepancy_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
    known_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing inventory discrepancy fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "inventory-control-specialist":
        errors.append(f"{relative}: skillset must be inventory-control-specialist")
    if data.get("completion_token") != INVENTORY_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-07 completion token")

    conflicts = set(data.get("required_conflicts", []))
    for conflict in REQUIRED_DISCREPANCY_CONFLICTS:
        if conflict not in conflicts:
            errors.append(f"{relative}: missing required conflict {conflict}")

    evidence_sources = data.get("expected_evidence_sources", [])
    if not isinstance(evidence_sources, list) or len(evidence_sources) < 5:
        errors.append(f"{relative}: expected_evidence_sources must contain source records")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")

    for skill in data.get("supporting_skills", []):
        if skill not in known_skills:
            errors.append(f"{relative}: supporting skill {skill} has no skill package")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_DISCREPANCY_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_warehouse_planner_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing warehouse planner fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "warehouse-planner":
        errors.append(f"{relative}: skillset must be warehouse-planner")
    if data.get("completion_token") != WAREHOUSE_PLANNER_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-08 completion token")

    components = set(data.get("required_planning_components", []))
    for component in REQUIRED_WAREHOUSE_PLANNER_COMPONENTS:
        if component not in components:
            errors.append(f"{relative}: missing planning component {component}")

    source_conflicts = data.get("expected_source_conflicts", [])
    if not isinstance(source_conflicts, list) or not source_conflicts:
        errors.append(f"{relative}: expected_source_conflicts must contain at least one conflict")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_WAREHOUSE_PLANNER_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_fulfillment_optimizer_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing fulfillment optimizer fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "fulfillment-optimizer":
        errors.append(f"{relative}: skillset must be fulfillment-optimizer")
    if data.get("completion_token") != FULFILLMENT_OPTIMIZER_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-09 completion token")

    order_profiles = set(data.get("required_order_profiles", []))
    for profile in REQUIRED_FULFILLMENT_ORDER_PROFILES:
        if profile not in order_profiles:
            errors.append(f"{relative}: missing order profile {profile}")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_FULFILLMENT_OPTIMIZER_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_FULFILLMENT_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_FULFILLMENT_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

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
    name = str(manifest["name"] or "")
    skills: list[str] = manifest["skills"]
    requirements = SKILLSET_REQUIREMENTS.get(name)

    if name != skillset_dir.name:
        errors.append(f"{manifest_relative}: name must match directory {skillset_dir.name}")
    if requirements is None:
        errors.append(f"{manifest_relative}: no validator requirements for skillset {name}")
    elif manifest["completion_token"] != requirements["completion_token"]:
        errors.append(f"{manifest_relative}: missing completion token {requirements['completion_token']}")
    if not manifest["description"] or len(str(manifest["description"])) < 60:
        errors.append(f"{manifest_relative}: description is missing or too weak")

    for duplicate in duplicate_items(skills):
        errors.append(f"{manifest_relative}: duplicate skill {duplicate}")
    for skill in skills:
        if skill not in known_skills:
            errors.append(f"{manifest_relative}: unknown skill {skill}")

    if requirements is not None:
        expected_skills = requirements["skills"]
        missing = sorted(expected_skills - set(skills))
        extra = sorted(set(skills) - expected_skills)
        for skill in missing:
            errors.append(f"{manifest_relative}: missing required skill {skill}")
        for skill in extra:
            errors.append(f"{manifest_relative}: unexpected skill {skill}")

    agents_file = manifest.get("agents_file")
    if agents_file:
        prompt_token = str(requirements["prompt_token"]) if requirements else f"${name}"
        errors.extend(validate_agents_file(skillset_dir / str(agents_file), repo_root, prompt_token))
    else:
        errors.append(f"{manifest_relative}: missing agents_file")

    scenario_file = manifest.get("scenario_file")
    if not scenario_file or not (repo_root / str(scenario_file)).is_file():
        errors.append(f"{manifest_relative}: scenario_file is missing or invalid")

    fixture_file = manifest.get("fixture_file")
    if fixture_file:
        fixture_path = repo_root / str(fixture_file)
        if requirements and requirements["fixture_validator"] == "warehouse_flow":
            errors.extend(
                validate_flow_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                    str(requirements["completion_token"]),
                )
            )
        elif requirements and requirements["fixture_validator"] == "inventory_discrepancy":
            errors.extend(
                validate_inventory_discrepancy_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                    known_skills,
                )
            )
        elif requirements and requirements["fixture_validator"] == "warehouse_planner":
            errors.extend(
                validate_warehouse_planner_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        elif requirements and requirements["fixture_validator"] == "fulfillment_optimizer":
            errors.extend(
                validate_fulfillment_optimizer_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        else:
            errors.append(f"{manifest_relative}: fixture validator is not configured")
    else:
        errors.append(f"{manifest_relative}: missing fixture_file")

    readme_token = str(requirements["completion_token"]) if requirements else str(manifest["completion_token"] or "")
    errors.extend(validate_readme(skillset_dir / "README.md", repo_root, readme_token))
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
