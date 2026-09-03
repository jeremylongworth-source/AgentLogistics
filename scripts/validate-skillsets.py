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
MATERIAL_HANDLING_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY"
TRANSPORTATION_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY"
SYSTEMS_DATA_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY"
CONTINUOUS_IMPROVEMENT_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY"
LABOR_PLANNING_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY"
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
REQUIRED_MATERIAL_HANDLING_ANALYST_SKILLS = {
    "analyze-product-flow",
    "identify-logistics-constraints",
    "select-storage-system",
    "plan-warehouse-zones",
    "classify-material-handling-requirements",
    "select-material-handling-equipment",
    "calculate-equipment-requirements",
    "analyze-equipment-utilization",
    "plan-material-flow",
    "evaluate-conveyor-application",
    "evaluate-agv-amr-application",
    "evaluate-asrs-application",
}
REQUIRED_TRANSPORTATION_COORDINATOR_SKILLS = {
    "select-transportation-mode",
    "plan-freight-shipment",
    "select-carrier",
    "compare-freight-rates",
    "calculate-freight-cost",
    "calculate-load-utilization",
    "plan-freight-consolidation",
    "plan-multi-stop-shipment",
    "analyze-carrier-performance",
    "audit-freight-charge",
    "analyze-freight-accessorials",
    "manage-freight-claim",
    "analyze-detention",
    "analyze-demurrage",
    "interpret-bill-of-lading",
    "analyze-transportation-kpis",
}
REQUIRED_LOGISTICS_SYSTEMS_ANALYST_SKILLS = {
    "map-wms-process",
    "analyze-wms-transaction-history",
    "diagnose-wms-inventory-issue",
    "validate-item-master-data",
    "validate-location-master-data",
    "analyze-logistics-scan-events",
    "design-logistics-barcode-flow",
    "interpret-gs1-identifiers",
    "design-logistics-unit-identification",
    "analyze-edi-logistics-flow",
    "map-erp-wms-integration",
    "map-wms-tms-integration",
    "analyze-logistics-data-quality",
}
REQUIRED_CONTINUOUS_IMPROVEMENT_SPECIALIST_SKILLS = {
    "select-logistics-kpis",
    "build-logistics-scorecard",
    "analyze-warehouse-kpis",
    "analyze-throughput",
    "diagnose-throughput-loss",
    "identify-logistics-bottleneck",
    "perform-logistics-root-cause-analysis",
    "perform-logistics-pareto-analysis",
    "map-warehouse-process",
    "analyze-logistics-waste",
    "compare-logistics-scenarios",
    "build-logistics-improvement-plan",
    "measure-improvement-result",
}
REQUIRED_LABOR_PLANNING_SKILLS = {
    "forecast-warehouse-workload",
    "calculate-labor-requirements",
    "plan-warehouse-staffing",
    "balance-warehouse-workload",
    "analyze-labor-productivity",
    "analyze-overtime-requirements",
    "plan-shift-handoff",
    "build-daily-warehouse-plan",
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
REQUIRED_MATERIAL_HANDLING_CONSIDERATIONS = (
    "load",
    "dimensions",
    "volume",
    "travel_distance",
    "throughput",
    "storage_height",
    "aisle_requirements",
    "operating_environment",
    "automation_level",
    "safety",
    "capital_intensity",
)
REQUIRED_MATERIAL_HANDLING_INVARIANTS = (
    "requirement classification",
    "equipment class comparison",
    "equipment requirement estimate",
    "equipment utilization analysis",
    "material-flow plan",
    "conveyor applicability review",
    "AGV/AMR applicability review",
    "AS/RS applicability review",
    "selection analysis not equipment certification",
    "qualified-review boundary",
)
REQUIRED_MATERIAL_HANDLING_CONSTRAINTS = (
    "load_weight",
    "pallet_dimensions",
    "daily_volume",
    "travel_distance",
    "peak_throughput",
    "storage_height",
    "aisle_width",
    "operating_environment",
    "automation_readiness",
    "safety_near_miss",
    "capital_intensity",
)
REQUIRED_MATERIAL_HANDLING_BLOCKED_APPROVALS = (
    "equipment_certification",
    "operator_certification",
    "load_rating_certification",
    "traffic_safety_approval",
    "guarding_approval",
    "building_fire_electrical_structural_approval",
    "procurement_approval",
    "live_system_configuration",
)
REQUIRED_TRANSPORTATION_MODES = (
    "truckload",
    "ltl",
    "parcel",
)
REQUIRED_TRANSPORTATION_INVARIANTS = (
    "truckload reasoning",
    "LTL reasoning",
    "parcel reasoning",
    "transportation mode recommendation",
    "freight shipment plan",
    "carrier recommendation",
    "rate comparison",
    "freight cost calculation",
    "load utilization calculation",
    "consolidation plan",
    "multi-stop plan",
    "carrier performance scorecard",
    "freight audit result",
    "accessorial analysis",
    "freight claim preparation",
    "detention analysis",
    "demurrage source-gap analysis",
    "BOL interpretation",
    "transportation KPI analysis",
    "international rules not universal",
    "qualified-review boundary",
)
REQUIRED_TRANSPORTATION_CONSTRAINTS = (
    "domestic_truckload",
    "domestic_ltl",
    "domestic_parcel",
    "international_rule_boundary",
    "missing_freight_class",
    "missing_dimensional_weight_rules",
    "missing_reweigh_source",
    "missing_demurrage_tariff",
    "missing_claim_deadline",
    "no_live_booking_or_tender",
    "no_invoice_payment_approval",
)
REQUIRED_TRANSPORTATION_BLOCKED_APPROVALS = (
    "no_live_tender_or_booking",
    "no_invoice_payment_approval",
    "no_claim_filing_approval",
    "no_customs_approval",
    "no_dangerous_goods_approval",
    "no_legal_approval",
    "no_carrier_contract_approval",
)
REQUIRED_LOGISTICS_SYSTEMS = (
    "WMS",
    "TMS",
    "ERP",
    "OMS",
    "YMS",
    "LMS",
    "WCS",
    "WES",
    "EDI",
    "APIs",
)
REQUIRED_SYSTEMS_DATA_INVARIANTS = (
    "WMS process map",
    "WMS transaction chronology",
    "WMS inventory issue diagnosis",
    "item master validation",
    "location master validation",
    "scan-event analysis",
    "barcode-flow design",
    "GS1 identifier interpretation",
    "logistics unit identification design",
    "EDI logistics flow analysis",
    "ERP-WMS integration map",
    "WMS-TMS integration map",
    "logistics data-quality analysis",
    "GS1 source-backed boundary",
    "no live system changes",
    "qualified-review boundary",
)
REQUIRED_SYSTEMS_DATA_CONSTRAINTS = (
    "source_system_lineage",
    "timestamp_timezone_conflict",
    "uom_pack_hierarchy_mismatch",
    "missing_item_dimensions",
    "location_pickable_flag_conflict",
    "duplicate_sscc_scan",
    "missing_ship_confirm",
    "unsourced_gs1_claims_blocked",
    "no_production_configuration",
    "api_permission_boundary",
)
REQUIRED_SYSTEMS_DATA_GS1_SOURCES = (
    "GS1 Application Identifiers",
    "GS1 System Architecture",
    "GS1 Digital Link URI Syntax",
    "GS1 Barcode Syntax Resource",
)
REQUIRED_SYSTEMS_DATA_BLOCKED_ACTIONS = (
    "live_wms_configuration",
    "live_tms_configuration",
    "live_erp_update",
    "master_data_change_approval",
    "edi_production_change",
    "api_credential_use",
    "regulatory_compliance_approval",
)
REQUIRED_CONTINUOUS_IMPROVEMENT_GATE_ELEMENTS = (
    "observation",
    "evidence",
    "inference",
    "root cause",
    "recommendation",
    "expected effect",
    "measurement plan",
)
REQUIRED_CONTINUOUS_IMPROVEMENT_KPI_DOMAINS = (
    "service",
    "quality",
    "cost",
    "productivity",
    "throughput",
    "inventory",
    "space",
    "labor",
    "safety",
)
REQUIRED_CONTINUOUS_IMPROVEMENT_INVARIANTS = (
    "KPI set",
    "scorecard design",
    "warehouse KPI analysis",
    "throughput analysis",
    "throughput loss diagnosis",
    "bottleneck finding",
    "root-cause analysis",
    "Pareto analysis",
    "warehouse process map",
    "waste analysis",
    "scenario comparison",
    "improvement plan",
    "improvement result measurement",
    "recommendation gate distinction",
    "no unsupported causal proof",
    "qualified-review boundary",
)
REQUIRED_CONTINUOUS_IMPROVEMENT_CONSTRAINTS = (
    "baseline_measurement",
    "target_definition",
    "cadence_owner",
    "throughput_unit",
    "capacity_constraint",
    "downtime_or_queue_evidence",
    "bottleneck_not_symptom",
    "root_cause_not_guess",
    "pareto_category_counts",
    "process_waste_categories",
    "scenario_assumption_boundary",
    "measurement_plan",
    "no_production_change_approval",
)
REQUIRED_CONTINUOUS_IMPROVEMENT_BLOCKED_ACTIONS = (
    "live_system_configuration",
    "staffing_change_approval",
    "labor_discipline_approval",
    "financial_commitment_approval",
    "capital_project_approval",
    "layout_change_approval",
    "safety_or_regulatory_approval",
    "guaranteed_improvement_claim",
)
REQUIRED_LABOR_PLANNING_COMPONENTS = (
    "workload forecast",
    "labor requirement",
    "staffing plan",
    "workload balancing",
    "labor productivity analysis",
    "overtime analysis",
    "shift handoff",
    "daily operating plan",
)
REQUIRED_LABOR_PLANNING_TIME_BASES = (
    "planning_date",
    "shift_window",
    "productive_hours",
    "scheduled_hours",
    "break_time",
    "service_window",
)
REQUIRED_LABOR_PLANNING_INVARIANTS = (
    "workload forecast by area",
    "productive labor-hour calculation",
    "staffing coverage by skill",
    "workload balancing by priority",
    "labor productivity analysis",
    "overtime exposure calculation",
    "shift handoff with owners",
    "daily warehouse operating plan",
    "paid versus productive time boundary",
    "qualified-review boundary",
)
REQUIRED_LABOR_PLANNING_CONSTRAINTS = (
    "inbound_volume",
    "outbound_volume",
    "inventory_work",
    "backlog",
    "productivity_standard",
    "break_schedule",
    "service_window",
    "skill_coverage",
    "equipment_constraint",
    "overtime_limit",
    "shift_handoff_open_work",
    "no_labor_law_approval",
    "no_staffing_approval",
)
REQUIRED_LABOR_PLANNING_BLOCKED_ACTIONS = (
    "live_schedule_publish",
    "payroll_approval",
    "hiring_approval",
    "labor_discipline_approval",
    "wage_hour_compliance_approval",
    "union_contract_interpretation",
    "safety_or_regulatory_approval",
    "live_system_configuration",
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
    "material-handling-analyst": {
        "completion_token": MATERIAL_HANDLING_COMPLETION_TOKEN,
        "skills": REQUIRED_MATERIAL_HANDLING_ANALYST_SKILLS,
        "prompt_token": "$material-handling-analyst",
        "fixture_validator": "material_handling",
    },
    "transportation-coordinator": {
        "completion_token": TRANSPORTATION_COMPLETION_TOKEN,
        "skills": REQUIRED_TRANSPORTATION_COORDINATOR_SKILLS,
        "prompt_token": "$transportation-coordinator",
        "fixture_validator": "transportation",
    },
    "logistics-systems-analyst": {
        "completion_token": SYSTEMS_DATA_COMPLETION_TOKEN,
        "skills": REQUIRED_LOGISTICS_SYSTEMS_ANALYST_SKILLS,
        "prompt_token": "$logistics-systems-analyst",
        "fixture_validator": "systems_data",
    },
    "continuous-improvement-specialist": {
        "completion_token": CONTINUOUS_IMPROVEMENT_COMPLETION_TOKEN,
        "skills": REQUIRED_CONTINUOUS_IMPROVEMENT_SPECIALIST_SKILLS,
        "prompt_token": "$continuous-improvement-specialist",
        "fixture_validator": "continuous_improvement",
    },
    "warehouse-supervisor": {
        "completion_token": LABOR_PLANNING_COMPLETION_TOKEN,
        "skills": REQUIRED_LABOR_PLANNING_SKILLS,
        "prompt_token": "$warehouse-supervisor",
        "fixture_validator": "labor_planning",
    },
    "warehouse-manager": {
        "completion_token": LABOR_PLANNING_COMPLETION_TOKEN,
        "skills": REQUIRED_LABOR_PLANNING_SKILLS,
        "prompt_token": "$warehouse-manager",
        "fixture_validator": "labor_planning",
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


def validate_material_handling_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing material handling fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "material-handling-analyst":
        errors.append(f"{relative}: skillset must be material-handling-analyst")
    if data.get("completion_token") != MATERIAL_HANDLING_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-10 completion token")

    considerations = set(data.get("required_considerations", []))
    for consideration in REQUIRED_MATERIAL_HANDLING_CONSIDERATIONS:
        if consideration not in considerations:
            errors.append(f"{relative}: missing required consideration {consideration}")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_MATERIAL_HANDLING_ANALYST_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_MATERIAL_HANDLING_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_MATERIAL_HANDLING_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

    blocked_approvals = set(data.get("blocked_approvals", []))
    for required in REQUIRED_MATERIAL_HANDLING_BLOCKED_APPROVALS:
        if required not in blocked_approvals:
            errors.append(f"{relative}: missing blocked approval {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_transportation_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing transportation fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "transportation-coordinator":
        errors.append(f"{relative}: skillset must be transportation-coordinator")
    if data.get("completion_token") != TRANSPORTATION_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-11 completion token")

    modes = set(data.get("required_modes", []))
    for mode in REQUIRED_TRANSPORTATION_MODES:
        if mode not in modes:
            errors.append(f"{relative}: missing transportation mode {mode}")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_TRANSPORTATION_COORDINATOR_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_TRANSPORTATION_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_TRANSPORTATION_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

    blocked_approvals = set(data.get("blocked_approvals", []))
    for required in REQUIRED_TRANSPORTATION_BLOCKED_APPROVALS:
        if required not in blocked_approvals:
            errors.append(f"{relative}: missing blocked approval {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_systems_data_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing systems data fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "logistics-systems-analyst":
        errors.append(f"{relative}: skillset must be logistics-systems-analyst")
    if data.get("completion_token") != SYSTEMS_DATA_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-12 completion token")

    systems = set(data.get("required_systems", []))
    for system in REQUIRED_LOGISTICS_SYSTEMS:
        if system not in systems:
            errors.append(f"{relative}: missing logistics system {system}")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_LOGISTICS_SYSTEMS_ANALYST_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_SYSTEMS_DATA_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_SYSTEMS_DATA_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

    gs1_sources = set(data.get("gs1_required_sources", []))
    for required in REQUIRED_SYSTEMS_DATA_GS1_SOURCES:
        if required not in gs1_sources:
            errors.append(f"{relative}: missing GS1 source {required}")

    blocked_actions = set(data.get("blocked_actions", []))
    for required in REQUIRED_SYSTEMS_DATA_BLOCKED_ACTIONS:
        if required not in blocked_actions:
            errors.append(f"{relative}: missing blocked action {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_continuous_improvement_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing continuous improvement fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != "continuous-improvement-specialist":
        errors.append(f"{relative}: skillset must be continuous-improvement-specialist")
    if data.get("completion_token") != CONTINUOUS_IMPROVEMENT_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-13 completion token")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_CONTINUOUS_IMPROVEMENT_SPECIALIST_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    gate_elements = set(data.get("required_gate_elements", []))
    for required in REQUIRED_CONTINUOUS_IMPROVEMENT_GATE_ELEMENTS:
        if required not in gate_elements:
            errors.append(f"{relative}: missing recommendation gate element {required}")

    kpi_domains = set(data.get("required_kpi_domains", []))
    for required in REQUIRED_CONTINUOUS_IMPROVEMENT_KPI_DOMAINS:
        if required not in kpi_domains:
            errors.append(f"{relative}: missing KPI domain {required}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_CONTINUOUS_IMPROVEMENT_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_CONTINUOUS_IMPROVEMENT_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

    blocked_actions = set(data.get("blocked_actions", []))
    for required in REQUIRED_CONTINUOUS_IMPROVEMENT_BLOCKED_ACTIONS:
        if required not in blocked_actions:
            errors.append(f"{relative}: missing blocked action {required}")

    scenario_file = data.get("scenario_file")
    if not scenario_file or not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario_file is missing or invalid")

    return errors


def validate_labor_planning_fixture(
    path: Path,
    repo_root: Path,
    manifest_skills: set[str],
    expected_skillset: str,
) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    if not path.is_file():
        return [f"Missing labor planning fixture: {relative}"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if data.get("skillset") != expected_skillset:
        errors.append(f"{relative}: skillset must be {expected_skillset}")
    if data.get("completion_token") != LABOR_PLANNING_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-14 completion token")

    for skill in data.get("expected_skills", []):
        if skill not in manifest_skills:
            errors.append(f"{relative}: expected skill {skill} is not in skillset manifest")
    missing_expected_skills = sorted(
        REQUIRED_LABOR_PLANNING_SKILLS - set(data.get("expected_skills", []))
    )
    for skill in missing_expected_skills:
        errors.append(f"{relative}: missing expected skill {skill}")

    components = set(data.get("required_planning_components", []))
    for required in REQUIRED_LABOR_PLANNING_COMPONENTS:
        if required not in components:
            errors.append(f"{relative}: missing planning component {required}")

    time_bases = set(data.get("required_time_bases", []))
    for required in REQUIRED_LABOR_PLANNING_TIME_BASES:
        if required not in time_bases:
            errors.append(f"{relative}: missing time basis {required}")

    invariants = set(data.get("required_output_invariants", []))
    for required in REQUIRED_LABOR_PLANNING_INVARIANTS:
        if required not in invariants:
            errors.append(f"{relative}: missing output invariant {required}")

    constraints = set(data.get("required_constraints", []))
    for required in REQUIRED_LABOR_PLANNING_CONSTRAINTS:
        if required not in constraints:
            errors.append(f"{relative}: missing constraint {required}")

    blocked_actions = set(data.get("blocked_actions", []))
    for required in REQUIRED_LABOR_PLANNING_BLOCKED_ACTIONS:
        if required not in blocked_actions:
            errors.append(f"{relative}: missing blocked action {required}")

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
        elif requirements and requirements["fixture_validator"] == "material_handling":
            errors.extend(
                validate_material_handling_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        elif requirements and requirements["fixture_validator"] == "transportation":
            errors.extend(
                validate_transportation_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        elif requirements and requirements["fixture_validator"] == "systems_data":
            errors.extend(
                validate_systems_data_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        elif requirements and requirements["fixture_validator"] == "continuous_improvement":
            errors.extend(
                validate_continuous_improvement_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                )
            )
        elif requirements and requirements["fixture_validator"] == "labor_planning":
            errors.extend(
                validate_labor_planning_fixture(
                    fixture_path,
                    repo_root,
                    set(skills),
                    name,
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
