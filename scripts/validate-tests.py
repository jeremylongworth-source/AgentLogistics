from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


COMPLETION_TOKEN = "AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY"
AL_06_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY"
AL_07_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY"
AL_08_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY"
AL_09_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY"
AL_10_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY"
AL_11_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY"
AL_12_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY"
AL_13_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY"
AL_14_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY"
AL_15_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_15_REVERSE_LOGISTICS_READY"
AL_16_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY"
AL_17_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY"
AL_18_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY"
AL_19_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY"
AL_20_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY"
AL_21_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY"
AL_22_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY"
AL_23_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_23_INTEGRATION_VALIDATED"
REQUIRED_CATEGORIES = {
    "correct_invocation",
    "incorrect_invocation",
    "missing_inputs",
    "bad_inputs",
    "calculation_correctness",
    "unit_mismatch",
    "ambiguous_scenario",
    "expected_output_structure",
    "safety_boundary",
    "jurisdiction_conflicts",
    "unsupported_assumptions",
}
REQUIRED_SCENARIO_SECTIONS = (
    "Category:",
    "Expected routing:",
    "Prompt:",
    "Acceptance checks:",
    "Risk and review notes:",
)
REQUIRED_OUTPUT_FIELDS = {
    "item_scope",
    "input_values",
    "normalized_lead_time",
    "demand_during_lead_time",
    "safety_stock",
    "raw_reorder_point",
    "rounded_reorder_point",
    "assumptions",
    "validation_notes",
}
TIME_UNIT_TO_DAYS = {
    "hour": 1 / 24,
    "day": 1,
    "week": 7,
}
NUMERIC_TOLERANCE = 0.0001
REQUIRED_REVERSE_LOGISTICS_SKILLS = {
    "process-customer-return",
    "classify-return-disposition",
    "inspect-returned-goods",
    "reconcile-returned-inventory",
    "analyze-return-reason",
    "analyze-return-rate",
    "plan-return-to-stock",
    "plan-return-to-vendor",
    "manage-damaged-inventory",
    "manage-nonconforming-inventory",
    "analyze-reverse-logistics-cost",
    "design-reverse-logistics-flow",
}
REQUIRED_REVERSE_LOGISTICS_COMPONENTS = (
    "return workflow",
    "inspection result",
    "disposition classification",
    "inventory reconciliation",
    "reason analysis",
    "return-rate calculation",
    "return-to-stock plan",
    "RTV plan",
    "damaged-inventory workflow",
    "nonconforming inventory workflow",
    "reverse cost analysis",
    "reverse-flow design",
)
REQUIRED_REVERSE_LOGISTICS_QUANTITY_STATES = (
    "authorized",
    "delivered",
    "received",
    "inspected",
    "held",
    "missing",
    "return_to_stock_proposed",
    "rtv_proposed",
    "damaged",
    "erp_not_posted",
    "refund_pending_review",
)
REQUIRED_REVERSE_LOGISTICS_INVARIANTS = (
    "customer return workflow",
    "returned-goods inspection",
    "disposition classification without approval",
    "returned inventory reconciliation",
    "return reason analysis",
    "return-rate calculation",
    "return-to-stock release boundary",
    "RTV authorization boundary",
    "damaged inventory workflow",
    "nonconforming inventory workflow",
    "reverse logistics cost analysis",
    "reverse-flow design",
    "qualified-review boundary",
)
REQUIRED_REVERSE_LOGISTICS_CONSTRAINTS = (
    "reason_code_conflict",
    "received_quantity_shortage",
    "photos_missing",
    "lot_expiry_control",
    "quality_release_required",
    "vendor_authorization_missing",
    "duplicate_rma_risk",
    "erp_receipt_not_posted",
    "oms_refund_pending",
    "regulated_goods_boundary",
    "no_live_system_change",
)
REQUIRED_REVERSE_LOGISTICS_BLOCKED_ACTIONS = (
    "refund_approval",
    "credit_approval",
    "warranty_approval",
    "inventory_adjustment_approval",
    "quality_release_approval",
    "return_to_stock_release",
    "rtv_claim_approval",
    "vendor_debit_approval",
    "disposal_or_destruction_approval",
    "recall_action_approval",
    "financial_posting_approval",
    "regulated_product_determination",
    "live_system_configuration",
)
REQUIRED_CANADA_SPECIALIZATIONS = {
    "identify-canadian-logistics-jurisdiction",
    "research-canadian-workplace-safety",
    "research-canadian-material-handling-safety",
    "research-canadian-powered-equipment-safety",
    "research-canadian-transportation-rules",
    "research-canadian-dangerous-goods-rules",
    "research-canadian-commercial-vehicle-safety",
    "research-canadian-loading-security",
    "research-canadian-logistics-documents",
    "research-canadian-import-export-controls",
    "research-canadian-storage-requirements",
}
REQUIRED_CANADA_AUTHORITY_CLASSES = (
    "federal workplace safety",
    "provincial and territorial workplace safety",
    "WHMIS hazardous product communication",
    "TDG dangerous goods transportation",
    "commercial vehicle and motor carrier safety",
    "cargo loading and securement",
    "import and export border controls",
    "carrier, terminal, port, airport, and facility rules",
    "employer safety program and site procedure",
    "manufacturer and equipment instructions",
)
REQUIRED_CANADA_JURISDICTION_DIMENSIONS = (
    "country",
    "province_or_territory",
    "federal_or_extra_provincial_context",
    "workplace_type",
    "industry",
    "activity",
    "transportation_mode",
    "route",
    "product_or_hazard",
    "employer_program_scope",
)
REQUIRED_CANADA_INVARIANTS = (
    "no single unified Canadian warehouse law",
    "current official sources required",
    "source access dates visible",
    "federal provincial territorial separation",
    "mode and activity separation",
    "product and hazard separation",
    "user evidence treated as evidence only",
    "operational preparation not approval",
    "qualified-review boundary",
    "source conflict handling",
)
REQUIRED_CANADA_BLOCKED_CLAIMS = (
    "legal_advice",
    "compliance_declaration",
    "safety_approval",
    "equipment_certification",
    "operator_certification",
    "tdg_classification_approval",
    "customs_declaration_approval",
    "import_export_release_approval",
    "vehicle_roadworthiness_certification",
    "driver_qualification_approval",
    "fire_building_structural_environmental_approval",
    "live_system_change",
)
REQUIRED_CANADA_SOURCE_URLS = (
    "https://www.ccohs.ca/oshanswers/legisl/legislation/intro.html",
    "https://www.canada.ca/en/employment-social-development/services/health-safety/workplace-safety.html",
    "https://laws-lois.justice.gc.ca/eng/regulations/Sor-86-304/index.html",
    "https://www.canada.ca/en/health-canada/services/environmental-workplace-health/occupational-health-safety/workplace-hazardous-materials-information-system/roles-responsibilities-whmis.html",
    "https://tc.canada.ca/en/dangerous-goods/transportation-dangerous-goods-canada",
    "https://tc.canada.ca/en/dangerous-goods/safety-awareness-materials-faq",
    "https://tc.canada.ca/en/road-transportation/motor-carriers-commercial-vehicles-drivers",
    "https://tc.canada.ca/en/road-transportation/motor-vehicle-safety/commercial-vehicle-safety",
    "https://www.cbsa-asfc.gc.ca/import/guide-eng.html",
    "https://www.cbsa-asfc.gc.ca/services/export/menu-eng.html",
)
REQUIRED_US_SPECIALIZATIONS = {
    "identify-us-logistics-jurisdiction",
    "research-us-workplace-safety",
    "research-us-material-handling-safety",
    "research-us-powered-equipment-safety",
    "research-us-transportation-rules",
    "research-us-hazardous-materials-rules",
    "research-us-commercial-vehicle-safety",
    "research-us-loading-security",
    "research-us-logistics-documents",
    "research-us-import-export-controls",
    "research-us-storage-requirements",
}
REQUIRED_US_AUTHORITY_CLASSES = (
    "federal workplace safety",
    "OSHA-approved state-plan workplace safety",
    "Hazard Communication hazardous chemical communication",
    "PHMSA hazardous materials transportation",
    "FMCSA commercial vehicle and motor carrier safety",
    "cargo loading and securement",
    "import and export border controls",
    "hazardous waste and environmental transport controls",
    "carrier, terminal, port, airport, and facility rules",
    "employer safety program and site procedure",
    "manufacturer and equipment instructions",
)
REQUIRED_US_JURISDICTION_DIMENSIONS = (
    "country",
    "state_or_territory",
    "federal_or_interstate_context",
    "OSHA_state_plan_status",
    "workplace_type",
    "industry",
    "activity",
    "transportation_mode",
    "route",
    "product_or_hazard",
    "customs_status",
    "environmental_status",
    "employer_program_scope",
)
REQUIRED_US_INVARIANTS = (
    "no single unified US warehouse law",
    "current official sources required",
    "source access dates visible",
    "federal state territorial separation",
    "OSHA state-plan separation",
    "mode and activity separation",
    "product and hazard separation",
    "user evidence treated as evidence only",
    "operational preparation not approval",
    "qualified-review boundary",
    "source conflict handling",
)
REQUIRED_US_BLOCKED_CLAIMS = (
    "legal_advice",
    "compliance_declaration",
    "safety_approval",
    "equipment_certification",
    "operator_certification",
    "hazmat_classification_approval",
    "customs_entry_approval",
    "import_export_release_approval",
    "vehicle_roadworthiness_certification",
    "driver_qualification_approval",
    "fire_building_structural_environmental_approval",
    "live_system_change",
)
REQUIRED_US_SOURCE_URLS = (
    "https://www.osha.gov/warehousing",
    "https://www.osha.gov/stateplans",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1200",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178",
    "https://www.phmsa.dot.gov/standards-rulemaking/hazmat/hazardous-materials-regulations",
    "https://www.fmcsa.dot.gov/regulations/hours-of-service",
    "https://www.fmcsa.dot.gov/regulations/cargo-securement/cargo-securement-rules",
    "https://www.cbp.gov/trade/basic-import-export",
    "https://www.cbp.gov/trade/automated/how-to-use-ace/introduction",
    "https://www.epa.gov/hw/hazardous-waste-transportation",
    "https://www.ecfr.gov/current/title-49",
)
REQUIRED_PROFESSIONAL_SKILLSETS = {
    "warehouse-operator",
    "receiving-specialist",
    "inventory-control-specialist",
    "warehouse-supervisor",
    "warehouse-manager",
    "logistics-coordinator",
    "transportation-coordinator",
    "warehouse-planner",
    "distribution-manager",
    "logistics-systems-analyst",
    "continuous-improvement-specialist",
    "logistics-operations-manager",
}
REQUIRED_PROFESSIONAL_ROLE_COMPONENTS = (
    "purpose",
    "included_skills",
    "routing_criteria",
    "dependencies",
    "excluded_responsibilities",
    "escalation_conditions",
    "expected_outputs",
)
REQUIRED_PROFESSIONAL_BOUNDARIES = (
    "legal_or_regulatory_approval",
    "safety_certification",
    "equipment_certification",
    "HR_or_labor_law_decision",
    "financial_approval",
    "live_system_change",
)
REQUIRED_SPECIALIZATION_CANDIDATES = {
    "cold-chain",
    "food-logistics",
    "dangerous-goods",
    "ecommerce",
    "manufacturing",
    "retail-distribution",
    "automotive",
    "pharmaceuticals",
    "international-logistics",
}
REQUIRED_SPECIALIZATION_FIELDS = (
    "domain need",
    "unique knowledge",
    "unique regulations",
    "unique workflows",
    "shared core skills",
    "new atomic skills required",
    "priority",
)
REQUIRED_SPECIALIZATION_BLOCKED_ACTIONS = (
    "build_all_specialization_packages",
    "add_unsourced_regulatory_claims",
    "create_core_dependency_on_specialization",
    "treat_candidate_skill_names_as_ready_packages",
    "make_hard_cross_project_dependency",
)
REQUIRED_FOOD_COLD_CHAIN_SPECIALIZATIONS = {
    "classify-food-cold-chain-requirements",
    "plan-temperature-controlled-storage",
    "monitor-cold-chain-temperature",
    "triage-temperature-excursion",
    "plan-fefo-inventory-rotation",
    "manage-expiry-controlled-food-inventory",
    "trace-food-lot-movement",
    "plan-sanitation-sensitive-logistics",
    "plan-food-segregation",
    "support-food-recall-logistics",
    "plan-cold-chain-transportation",
    "plan-cold-chain-handoff",
}
REQUIRED_FOOD_COLD_CHAIN_CAPABILITIES = (
    "temperature-controlled storage",
    "temperature monitoring",
    "excursion handling",
    "FEFO",
    "expiry controls",
    "lot traceability",
    "sanitation-sensitive logistics",
    "food segregation",
    "recall logistics",
    "cold-chain transportation",
    "cold-chain handoffs",
)
REQUIRED_FOOD_COLD_CHAIN_INVARIANTS = (
    "product and jurisdiction scope",
    "temperature basis and monitoring evidence",
    "excursion chronology without release approval",
    "FEFO and expiry-control handoff",
    "lot traceability packet",
    "sanitation and segregation review boundary",
    "recall logistics packet without recall approval",
    "cold-chain transportation handoff",
    "source dates and official source list",
    "qualified-review boundary",
    "AgentLogistics ChefSkills independence",
)
REQUIRED_FOOD_COLD_CHAIN_BLOCKED_CLAIMS = (
    "legal advice",
    "compliance declarations",
    "food safety approvals",
    "product release approvals",
    "temperature excursion disposition approvals",
    "recall initiation approvals",
    "sanitation approvals",
    "equipment certifications",
    "carrier approvals",
    "customer commitment approvals",
    "financial approvals",
    "live system changes",
)
REQUIRED_FOOD_COLD_CHAIN_SOURCE_URLS = (
    "https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-sanitary-transportation-human-and-animal-food",
    "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-industry-sanitary-transportation-food",
    "https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods",
    "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/industry-guidance-recalls",
    "https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/danger-zone-40f-140f",
    "https://www.fsis.usda.gov/policy/fsis-directives/8080.1",
    "https://inspection.canada.ca/en/food-safety-industry/preventive-control-plans",
    "https://inspection.canada.ca/en/food-safety-industry/preventive-control-plans/regulatory-requirements",
    "https://inspection.canada.ca/en/inspection-and-enforcement/guidance-food-activities/preventive-control-inspection/traceability-inspection",
)
REQUIRED_DANGEROUS_GOODS_SPECIALIZATIONS = {
    "classify-dangerous-goods-logistics-requirements",
    "plan-dangerous-goods-storage-segregation",
    "prepare-dangerous-goods-shipping-research",
    "triage-dangerous-goods-incident-logistics",
}
REQUIRED_DANGEROUS_GOODS_CAPABILITIES = (
    "classification",
    "packaging",
    "marking",
    "labeling",
    "documentation",
    "storage",
    "segregation",
    "transport mode",
    "jurisdiction",
    "personnel qualification requirements",
)
REQUIRED_DANGEROUS_GOODS_INVARIANTS = (
    "material and jurisdiction scope",
    "mode-specific source separation",
    "classification evidence without classification approval",
    "packaging marking labeling documentation research packet",
    "storage and segregation review boundary",
    "transport mode handoff",
    "personnel qualification evidence without certification",
    "incident logistics handoff without emergency response approval",
    "source dates and official source list",
    "qualified-review boundary",
)
REQUIRED_DANGEROUS_GOODS_BLOCKED_CLAIMS = (
    "legal advice",
    "compliance declarations",
    "safety approvals",
    "certifications",
    "dangerous-goods classification approvals",
    "hazardous materials classification approvals",
    "packaging design approvals",
    "marking or labeling approvals",
    "shipping paper approvals",
    "emergency response approvals",
    "environmental determinations",
    "carrier approvals",
    "personnel qualification certifications",
    "customs approvals",
    "customer commitment approvals",
    "financial approvals",
    "live system changes",
)
REQUIRED_DANGEROUS_GOODS_SOURCE_URLS = (
    "https://www.phmsa.dot.gov/standards-rulemaking/hazmat/hazardous-materials-regulations",
    "https://www.phmsa.dot.gov/training/hazmat/publications",
    "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C",
    "https://tc.canada.ca/en/dangerous-goods/transportation-dangerous-goods-canada",
    "https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/transportation-dangerous-goods-regulations",
    "https://laws-lois.justice.gc.ca/eng/regulations/sor-2001-286/",
    "https://unece.org/transport/dangerous-goods/un-model-regulations-rev-24",
    "https://www.icao.int/Dangerous-Goods/Technical-Instructions",
    "https://www.iata.org/en/publications/dgr/",
    "https://www.imo.org/en/ourwork/safety/pages/dangerousgoods-default.aspx",
    "https://www.imo.org/en/publications/pages/imdg%20code.aspx",
    "https://www.osha.gov/chemical-hazards",
    "https://www.epa.gov/hw/hazardous-waste-transportation",
)
REQUIRED_INTERNATIONAL_LOGISTICS_SPECIALIZATIONS = {
    "map-cross-border-logistics-flow",
    "prepare-international-shipment-document-research",
    "plan-customs-broker-handoff",
    "triage-port-terminal-exception",
}
REQUIRED_INTERNATIONAL_LOGISTICS_CAPABILITIES = (
    "Incoterms",
    "import/export concepts",
    "customs",
    "customs brokers",
    "duties",
    "commercial invoices",
    "packing lists",
    "international bills of lading",
    "ocean freight",
    "air freight",
    "container logistics",
    "drayage",
    "ports",
    "international freight forwarding",
)
REQUIRED_INTERNATIONAL_LOGISTICS_INVARIANTS = (
    "lane and jurisdiction scope",
    "party-role map",
    "mode-specific source separation",
    "Incoterms context without contract advice",
    "commercial invoice and packing list research packet",
    "customs broker handoff without customs approval",
    "export filing evidence without filing approval",
    "sanctions and export-control escalation without determination",
    "duty and tax questions without determination",
    "port terminal and drayage exception handoff",
    "source dates and official source list",
    "qualified-review boundary",
)
REQUIRED_INTERNATIONAL_LOGISTICS_BLOCKED_CLAIMS = (
    "legal advice",
    "compliance declarations",
    "customs entry approvals",
    "customs release approvals",
    "export filing approvals",
    "sanctions determinations",
    "export-control classification approvals",
    "license requirement determinations",
    "duty or tax determinations",
    "Incoterms contract advice",
    "bill of lading approvals",
    "commercial invoice approvals",
    "packing list approvals",
    "carrier approvals",
    "port or terminal release approvals",
    "freight forwarder approvals",
    "financial approvals",
    "customer commitment approvals",
    "live system changes",
)
REQUIRED_INTERNATIONAL_LOGISTICS_SOURCE_URLS = (
    "https://iccwbo.org/business-solutions/incoterms-rules/",
    "https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/",
    "https://www.trade.gov/know-your-incoterms",
    "https://www.cbp.gov/trade/basic-import-export",
    "https://www.ecfr.gov/current/title-19/chapter-I/part-141/subpart-F",
    "https://www.cbsa-asfc.gc.ca/import/guide-eng.html",
    "https://www.cbsa-asfc.gc.ca/services/export/menu-eng.html",
    "https://www.wcoomd.org/en/topics/nomenclature/overview/what-is-the-harmonized-system.aspx",
    "https://www.wcoomd.org/en/topics/valuation/overview/what-is-customs-valuation.aspx",
    "https://www.wcoomd.org/en/topics/origin/overview.aspx",
    "https://www.wcoomd.org/en/topics/facilitation/instrument-and-tools/frameworks-of-standards/safe_package.aspx",
    "https://www.census.gov/foreign-trade/aes/",
    "https://www.census.gov/foreign-trade/regulations/",
    "https://www.bis.gov/regulations/ear",
    "https://www.bis.gov/regulations/ear/interactive-commerce-control-list",
    "https://ofac.treasury.gov/sanctions-programs-and-country-information",
    "https://www.fmc.gov/detention-and-demurrage/",
    "https://www.imo.org/en/about/conventions/pages/convention-on-facilitation-of-international-maritime-traffic-%28fal%29.aspx",
    "https://www.trade.gov/common-export-documents",
    "https://www.cbp.gov/border-security/ports-entry/cargo-security/importer-security-filing-102",
)
REQUIRED_INTEGRATION_SCENARIO_FILES = (
    "tests/scenarios/integration-inbound-shortage.md",
    "tests/scenarios/integration-throughput-collapse.md",
    "tests/scenarios/integration-inventory-accuracy-deterioration.md",
    "tests/scenarios/integration-capacity-constraint.md",
    "tests/scenarios/integration-transportation-cost-increase.md",
)
REQUIRED_INTEGRATION_SCENARIOS = (
    "inbound shortage",
    "warehouse throughput collapse",
    "inventory accuracy deterioration",
    "capacity constraint",
    "transportation cost increase",
)
REQUIRED_INTEGRATION_COMPONENTS = (
    "receiving discrepancy",
    "ASN evidence",
    "inventory reconciliation",
    "WMS transaction chronology",
    "carrier evidence",
    "order profile",
    "replenishment constraints",
    "picking bottleneck",
    "labor capacity",
    "congestion",
    "KPI analysis",
    "root cause",
    "improvement plan",
    "cycle count evidence",
    "scan-event evidence",
    "Pareto analysis",
    "storage utilization",
    "pallet positions",
    "slotting",
    "dock capacity",
    "capacity forecast",
    "shipment profile",
    "freight rates",
    "accessorials",
    "load utilization",
    "carrier performance",
    "consolidation scenario",
)
REQUIRED_INTEGRATION_INVARIANTS = (
    "cross-skill routing map",
    "source-by-source evidence table",
    "chronology",
    "quantity reconciliation",
    "unit checks",
    "facts assumptions and inferences separated",
    "source conflicts labeled",
    "missing evidence requests",
    "operational next steps",
    "owner handoffs",
    "observation evidence inference root cause recommendation expected effect measurement plan",
    "qualified-review boundary",
)
REQUIRED_INTEGRATION_BOUNDARY_CLASSES = (
    "inventory adjustment approval",
    "freight claim approval",
    "supplier claim approval",
    "customer commitment approval",
    "financial approval",
    "live WMS change",
    "live TMS change",
    "staffing approval",
    "equipment approval",
    "structural approval",
    "food safety approval",
    "carrier selection approval",
    "rate acceptance approval",
    "demurrage payment approval",
    "HR decision",
)
REQUIRED_INTEGRATION_ROUTE_GROUPS = {
    "integration-inbound-shortage": {
        "inbound-receiving",
        "inventory-control",
        "logistics-systems-data",
        "transportation-freight",
    },
    "integration-throughput-collapse": {
        "replenishment-picking",
        "labor-operating-planning",
        "performance-continuous-improvement",
    },
    "integration-inventory-accuracy-deterioration": {
        "inventory-control",
        "logistics-systems-data",
        "performance-continuous-improvement",
    },
    "integration-capacity-constraint": {
        "storage-warehousing",
        "warehouse-design-capacity",
        "food-cold-chain",
    },
    "integration-transportation-cost-increase": {
        "transportation-freight",
        "performance-continuous-improvement",
    },
}


def skill_names(repo_root: Path) -> set[str]:
    names: set[str] = set()
    skills_root = repo_root / "skills"
    if skills_root.is_dir():
        names.update(path.parent.name for path in skills_root.glob("*/*/SKILL.md"))

    specializations_root = repo_root / "specializations"
    if specializations_root.is_dir():
        names.update(path.parent.name for path in specializations_root.glob("*/*/SKILL.md"))

    skillsets_root = repo_root / "skillsets"
    if skillsets_root.is_dir():
        names.update(path.parent.name for path in skillsets_root.glob("*/skillset.yaml"))

    return names


def parse_expected_routing(path: Path) -> dict[str, dict[str, Any]]:
    scenarios: dict[str, dict[str, Any]] = {}
    current_name: str | None = None
    reading_routes = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped == "scenarios:":
            continue

        scenario_match = re.match(r"^  ([a-z0-9-]+):$", line)
        if scenario_match:
            current_name = scenario_match.group(1)
            scenarios[current_name] = {"expected_routes": []}
            reading_routes = False
            continue

        if current_name is None:
            continue

        if stripped.startswith("prompt_file:"):
            scenarios[current_name]["prompt_file"] = stripped.split(":", 1)[1].strip()
            reading_routes = False
        elif stripped.startswith("category:"):
            scenarios[current_name]["category"] = stripped.split(":", 1)[1].strip()
            reading_routes = False
        elif stripped == "expected_routes: []":
            scenarios[current_name]["expected_routes"] = []
            reading_routes = False
        elif stripped == "expected_routes:":
            scenarios[current_name]["expected_routes"] = []
            reading_routes = True
        elif reading_routes and stripped.startswith("- "):
            scenarios[current_name]["expected_routes"].append(stripped[2:].strip())
        else:
            reading_routes = False

    return scenarios


def extract_scenario_category(text: str) -> str | None:
    match = re.search(r"^Category:\s*`?([a-z_]+)`?\s*$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1)


def validate_routing(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    routing_path = repo_root / "tests" / "expected-routing.yaml"
    if not routing_path.is_file():
        return ["Missing test routing manifest: tests/expected-routing.yaml"]

    scenarios = parse_expected_routing(routing_path)
    if not scenarios:
        errors.append("tests/expected-routing.yaml: no scenarios defined")
        return errors

    categories = {data.get("category", "") for data in scenarios.values()}
    missing_categories = sorted(REQUIRED_CATEGORIES - categories)
    for category in missing_categories:
        errors.append(f"tests/expected-routing.yaml: missing category {category}")

    for name, data in scenarios.items():
        prompt_file = data.get("prompt_file")
        if not prompt_file:
            errors.append(f"tests/expected-routing.yaml: {name} missing prompt_file")
            continue

        scenario_path = repo_root / prompt_file
        if not scenario_path.is_file():
            errors.append(f"tests/expected-routing.yaml: missing scenario file {prompt_file}")
            continue

        text = scenario_path.read_text(encoding="utf-8")
        for section in REQUIRED_SCENARIO_SECTIONS:
            if section not in text:
                errors.append(f"{prompt_file}: missing {section}")

        file_category = extract_scenario_category(text)
        if file_category != data.get("category"):
            errors.append(
                f"{prompt_file}: category {file_category!r} does not match routing manifest "
                f"{data.get('category')!r}"
            )

        for route in data.get("expected_routes", []):
            if route not in known_skills:
                errors.append(f"tests/expected-routing.yaml: route {route} has no skill package")

    return errors


def read_fixture(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def lead_time_in_demand_units(lead_time: float, lead_time_unit: str, demand_time_unit: str) -> float:
    return lead_time * TIME_UNIT_TO_DAYS[lead_time_unit] / TIME_UNIT_TO_DAYS[demand_time_unit]


def assert_close(errors: list[str], case_id: str, field: str, actual: float, expected: float) -> None:
    if not math.isclose(actual, expected, rel_tol=NUMERIC_TOLERANCE, abs_tol=NUMERIC_TOLERANCE):
        errors.append(f"{case_id}: expected {field} {expected}, calculated {actual}")


def validate_numeric_case(case: dict[str, Any], errors: list[str]) -> None:
    case_id = case.get("id", "<missing-id>")
    inputs = case.get("inputs", {})
    expected = case.get("expected", {})

    if "average_demand" not in inputs or "lead_time" not in inputs:
        return

    if inputs.get("average_demand", 0) < 0:
        if expected.get("status") != "invalid" or not expected.get("error_field"):
            errors.append(f"{case_id}: bad input case must identify invalid status and error field")
        return

    demand_time_unit = inputs.get("demand_time_unit")
    lead_time_unit = inputs.get("lead_time_unit")
    if demand_time_unit not in TIME_UNIT_TO_DAYS:
        errors.append(f"{case_id}: unsupported demand_time_unit {demand_time_unit}")
        return
    if lead_time_unit not in TIME_UNIT_TO_DAYS:
        errors.append(f"{case_id}: unsupported lead_time_unit {lead_time_unit}")
        return

    converted_lead_time = lead_time_in_demand_units(
        float(inputs["lead_time"]),
        lead_time_unit,
        demand_time_unit,
    )
    demand_during_lead_time = float(inputs["average_demand"]) * converted_lead_time

    if "lead_time_in_demand_units" in expected:
        assert_close(
            errors,
            case_id,
            "lead_time_in_demand_units",
            converted_lead_time,
            float(expected["lead_time_in_demand_units"]),
        )

    if "demand_during_lead_time" in expected:
        assert_close(
            errors,
            case_id,
            "demand_during_lead_time",
            demand_during_lead_time,
            float(expected["demand_during_lead_time"]),
        )

    if inputs.get("safety_stock_unit") and inputs.get("demand_unit") != inputs.get("safety_stock_unit"):
        if expected.get("status") != "unit_mismatch" or not expected.get("must_not_return_final_reorder_point"):
            errors.append(f"{case_id}: unit mismatch must block final reorder point")
        return

    if "safety_stock" not in inputs:
        if not expected.get("must_not_return_final_reorder_point"):
            errors.append(f"{case_id}: missing safety stock must block final reorder point")
        return

    raw_reorder_point = demand_during_lead_time + float(inputs["safety_stock"])
    rounded_reorder_point = math.ceil(raw_reorder_point)

    if "raw_reorder_point" in expected:
        assert_close(
            errors,
            case_id,
            "raw_reorder_point",
            raw_reorder_point,
            float(expected["raw_reorder_point"]),
        )
    if "rounded_reorder_point" in expected:
        assert_close(
            errors,
            case_id,
            "rounded_reorder_point",
            rounded_reorder_point,
            float(expected["rounded_reorder_point"]),
        )

    if {"on_hand", "on_order", "allocated_backordered"} <= set(inputs):
        inventory_position = (
            float(inputs["on_hand"])
            + float(inputs["on_order"])
            - float(inputs["allocated_backordered"])
        )
        if "inventory_position" in expected:
            assert_close(
                errors,
                case_id,
                "inventory_position",
                inventory_position,
                float(expected["inventory_position"]),
            )
        if "reorder_signal" in expected and bool(inventory_position <= raw_reorder_point) != expected["reorder_signal"]:
            errors.append(f"{case_id}: reorder_signal mismatch")


def validate_reverse_logistics_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "reverse-logistics-return-lifecycle.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/reverse-logistics-return-lifecycle.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_15_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-15 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/reverse-logistics-return-lifecycle.md":
        errors.append(f"{relative}: missing reverse-logistics scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_skills = set(fixture.get("expected_skills", []))
    for skill in sorted(REQUIRED_REVERSE_LOGISTICS_SKILLS - expected_skills):
        errors.append(f"{relative}: expected_skills missing {skill}")
    for skill in sorted(expected_skills - known_skills):
        errors.append(f"{relative}: expected skill {skill} has no package")

    checks = (
        ("required_lifecycle_components", REQUIRED_REVERSE_LOGISTICS_COMPONENTS),
        ("required_quantity_states", REQUIRED_REVERSE_LOGISTICS_QUANTITY_STATES),
        ("required_output_invariants", REQUIRED_REVERSE_LOGISTICS_INVARIANTS),
        ("required_constraints", REQUIRED_REVERSE_LOGISTICS_CONSTRAINTS),
        ("blocked_actions", REQUIRED_REVERSE_LOGISTICS_BLOCKED_ACTIONS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    return errors


def validate_canada_compliance_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "canada-compliance-source-triage.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/canada-compliance-source-triage.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_16_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-16 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/canada-compliance-source-triage.md":
        errors.append(f"{relative}: missing Canada compliance scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_specializations = set(fixture.get("expected_specializations", []))
    for package_name in sorted(REQUIRED_CANADA_SPECIALIZATIONS - expected_specializations):
        errors.append(f"{relative}: expected_specializations missing {package_name}")
    for package_name in sorted(expected_specializations - known_skills):
        errors.append(f"{relative}: expected specialization {package_name} has no package")

    checks = (
        ("required_authority_classes", REQUIRED_CANADA_AUTHORITY_CLASSES),
        ("required_jurisdiction_dimensions", REQUIRED_CANADA_JURISDICTION_DIMENSIONS),
        ("required_output_invariants", REQUIRED_CANADA_INVARIANTS),
        ("blocked_claims", REQUIRED_CANADA_BLOCKED_CLAIMS),
        ("official_source_urls", REQUIRED_CANADA_SOURCE_URLS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    return errors


def validate_us_compliance_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "us-compliance-source-triage.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/us-compliance-source-triage.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_17_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-17 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/us-compliance-source-triage.md":
        errors.append(f"{relative}: missing US compliance scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_specializations = set(fixture.get("expected_specializations", []))
    for package_name in sorted(REQUIRED_US_SPECIALIZATIONS - expected_specializations):
        errors.append(f"{relative}: expected_specializations missing {package_name}")
    for package_name in sorted(expected_specializations - known_skills):
        errors.append(f"{relative}: expected specialization {package_name} has no package")

    checks = (
        ("required_authority_classes", REQUIRED_US_AUTHORITY_CLASSES),
        ("required_jurisdiction_dimensions", REQUIRED_US_JURISDICTION_DIMENSIONS),
        ("required_output_invariants", REQUIRED_US_INVARIANTS),
        ("blocked_claims", REQUIRED_US_BLOCKED_CLAIMS),
        ("official_source_urls", REQUIRED_US_SOURCE_URLS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    return errors


def validate_professional_composition_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "professional-skillset-composition.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/professional-skillset-composition.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_18_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-18 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/professional-skillset-composition.md":
        errors.append(f"{relative}: missing professional skillset composition scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_skillsets = set(fixture.get("required_skillsets", []))
    for skillset in sorted(REQUIRED_PROFESSIONAL_SKILLSETS - expected_skillsets):
        errors.append(f"{relative}: required_skillsets missing {skillset}")
    for skillset in sorted(expected_skillsets - known_skills):
        errors.append(f"{relative}: required skillset {skillset} has no package")

    role_components = set(fixture.get("required_role_components", []))
    for component in REQUIRED_PROFESSIONAL_ROLE_COMPONENTS:
        if component not in role_components:
            errors.append(f"{relative}: required_role_components missing {component}")

    blocked_actions = set(fixture.get("blocked_actions", []))
    for action in REQUIRED_PROFESSIONAL_BOUNDARIES:
        if action not in blocked_actions:
            errors.append(f"{relative}: blocked_actions missing {action}")

    if fixture.get("composition_gate") != "compose_existing_skills_not_duplicate":
        errors.append(f"{relative}: composition_gate must be compose_existing_skills_not_duplicate")

    return errors


def validate_specialization_framework_fixture(repo_root: Path) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "specialization-framework-roadmap.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/specialization-framework-roadmap.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_19_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-19 completion token")

    required_artifact = fixture.get("required_artifact")
    if required_artifact != "docs/architecture/specialization-roadmap.md":
        errors.append(f"{relative}: missing specialization roadmap artifact reference")
    elif not (repo_root / required_artifact).is_file():
        errors.append(f"{relative}: required artifact {required_artifact} does not exist")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/specialization-framework-roadmap.md":
        errors.append(f"{relative}: missing specialization framework scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    candidates = set(fixture.get("required_candidates", []))
    for candidate in sorted(REQUIRED_SPECIALIZATION_CANDIDATES - candidates):
        errors.append(f"{relative}: required_candidates missing {candidate}")

    fields = set(fixture.get("required_candidate_fields", []))
    for field in REQUIRED_SPECIALIZATION_FIELDS:
        if field not in fields:
            errors.append(f"{relative}: required_candidate_fields missing {field}")

    priority_map = fixture.get("required_priorities", {})
    if set(priority_map.get("P0", [])) != {"cold-chain", "food-logistics"}:
        errors.append(f"{relative}: P0 priorities must be cold-chain and food-logistics")
    for candidate in REQUIRED_SPECIALIZATION_CANDIDATES:
        if not any(candidate in priority_map.get(priority, []) for priority in ("P0", "P1", "P2")):
            errors.append(f"{relative}: priority map missing {candidate}")

    blocked_actions = set(fixture.get("blocked_actions", []))
    for action in REQUIRED_SPECIALIZATION_BLOCKED_ACTIONS:
        if action not in blocked_actions:
            errors.append(f"{relative}: blocked_actions missing {action}")

    return errors


def validate_food_cold_chain_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "food-cold-chain-source-triage.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/food-cold-chain-source-triage.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_20_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-20 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/food-cold-chain-source-triage.md":
        errors.append(f"{relative}: missing food cold-chain scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_specializations = set(fixture.get("expected_specializations", []))
    for package_name in sorted(REQUIRED_FOOD_COLD_CHAIN_SPECIALIZATIONS - expected_specializations):
        errors.append(f"{relative}: expected_specializations missing {package_name}")
    for package_name in sorted(expected_specializations - known_skills):
        errors.append(f"{relative}: expected specialization {package_name} has no package")

    checks = (
        ("required_capabilities", REQUIRED_FOOD_COLD_CHAIN_CAPABILITIES),
        ("required_output_invariants", REQUIRED_FOOD_COLD_CHAIN_INVARIANTS),
        ("blocked_claims", REQUIRED_FOOD_COLD_CHAIN_BLOCKED_CLAIMS),
        ("official_source_urls", REQUIRED_FOOD_COLD_CHAIN_SOURCE_URLS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    authority_classes = fixture.get("required_authority_classes", [])
    if not isinstance(authority_classes, list) or len(authority_classes) < 6:
        errors.append(f"{relative}: required_authority_classes must contain source categories")

    return errors


def validate_dangerous_goods_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "dangerous-goods-source-triage.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/dangerous-goods-source-triage.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_21_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-21 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/dangerous-goods-source-triage.md":
        errors.append(f"{relative}: missing dangerous-goods scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_specializations = set(fixture.get("expected_specializations", []))
    for package_name in sorted(REQUIRED_DANGEROUS_GOODS_SPECIALIZATIONS - expected_specializations):
        errors.append(f"{relative}: expected_specializations missing {package_name}")
    for package_name in sorted(expected_specializations - known_skills):
        errors.append(f"{relative}: expected specialization {package_name} has no package")

    checks = (
        ("required_capabilities", REQUIRED_DANGEROUS_GOODS_CAPABILITIES),
        ("required_output_invariants", REQUIRED_DANGEROUS_GOODS_INVARIANTS),
        ("blocked_claims", REQUIRED_DANGEROUS_GOODS_BLOCKED_CLAIMS),
        ("official_source_urls", REQUIRED_DANGEROUS_GOODS_SOURCE_URLS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    authority_classes = fixture.get("required_authority_classes", [])
    if not isinstance(authority_classes, list) or len(authority_classes) < 8:
        errors.append(f"{relative}: required_authority_classes must contain source categories")

    return errors


def validate_international_logistics_fixture(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "international-logistics-source-triage.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/international-logistics-source-triage.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_22_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-22 completion token")

    scenario_file = fixture.get("scenario_file")
    if scenario_file != "tests/scenarios/international-logistics-source-triage.md":
        errors.append(f"{relative}: missing international-logistics scenario reference")
    elif not (repo_root / scenario_file).is_file():
        errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    expected_specializations = set(fixture.get("expected_specializations", []))
    for package_name in sorted(REQUIRED_INTERNATIONAL_LOGISTICS_SPECIALIZATIONS - expected_specializations):
        errors.append(f"{relative}: expected_specializations missing {package_name}")
    for package_name in sorted(expected_specializations - known_skills):
        errors.append(f"{relative}: expected specialization {package_name} has no package")

    checks = (
        ("required_capabilities", REQUIRED_INTERNATIONAL_LOGISTICS_CAPABILITIES),
        ("required_output_invariants", REQUIRED_INTERNATIONAL_LOGISTICS_INVARIANTS),
        ("blocked_claims", REQUIRED_INTERNATIONAL_LOGISTICS_BLOCKED_CLAIMS),
        ("official_source_urls", REQUIRED_INTERNATIONAL_LOGISTICS_SOURCE_URLS),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    authority_classes = fixture.get("required_authority_classes", [])
    if not isinstance(authority_classes, list) or len(authority_classes) < 10:
        errors.append(f"{relative}: required_authority_classes must contain source categories")

    return errors


def validate_repository_wide_integration_fixture(repo_root: Path) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "repository-wide-integration.json"
    relative = fixture_path.relative_to(repo_root)
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/repository-wide-integration.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{relative}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != AL_23_COMPLETION_TOKEN:
        errors.append(f"{relative}: missing AL-23 completion token")

    scenario_files = set(fixture.get("scenario_files", []))
    for scenario_file in REQUIRED_INTEGRATION_SCENARIO_FILES:
        if scenario_file not in scenario_files:
            errors.append(f"{relative}: scenario_files missing {scenario_file}")
        elif not (repo_root / scenario_file).is_file():
            errors.append(f"{relative}: scenario file {scenario_file} does not exist")

    checks = (
        ("required_scenarios", REQUIRED_INTEGRATION_SCENARIOS),
        ("required_cross_domain_components", REQUIRED_INTEGRATION_COMPONENTS),
        ("required_output_invariants", REQUIRED_INTEGRATION_INVARIANTS),
        ("required_boundary_classes", REQUIRED_INTEGRATION_BOUNDARY_CLASSES),
    )
    for field, required_values in checks:
        values = set(fixture.get(field, []))
        for value in required_values:
            if value not in values:
                errors.append(f"{relative}: {field} missing {value}")

    route_groups = fixture.get("scenario_route_groups", {})
    if not isinstance(route_groups, dict):
        errors.append(f"{relative}: scenario_route_groups must be an object")
        return errors

    for scenario_name, required_groups in REQUIRED_INTEGRATION_ROUTE_GROUPS.items():
        groups = set(route_groups.get(scenario_name, []))
        for group in required_groups:
            if group not in groups:
                errors.append(f"{relative}: scenario_route_groups {scenario_name} missing {group}")

    return errors


def validate_fixtures(repo_root: Path, known_skills: set[str]) -> list[str]:
    errors: list[str] = []
    fixture_path = repo_root / "tests" / "fixtures" / "calculate-reorder-point-cases.json"
    if not fixture_path.is_file():
        return ["Missing fixture file: tests/fixtures/calculate-reorder-point-cases.json"]

    try:
        fixture = read_fixture(fixture_path)
    except json.JSONDecodeError as exc:
        return [f"{fixture_path.relative_to(repo_root)}: invalid JSON: {exc}"]

    if fixture.get("completion_token") != COMPLETION_TOKEN:
        errors.append(f"{fixture_path.relative_to(repo_root)}: missing AL-04 completion token")

    schema_path = fixture.get("schema")
    if schema_path != "shared/schemas/reorder-point-calculation.schema.json":
        errors.append(f"{fixture_path.relative_to(repo_root)}: missing shared schema reference")

    skill = fixture.get("skill")
    if skill not in known_skills:
        errors.append(f"{fixture_path.relative_to(repo_root)}: skill {skill} has no package")

    cases = fixture.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append(f"{fixture_path.relative_to(repo_root)}: cases must be a nonempty list")
        return errors

    categories = {case.get("category", "") for case in cases}
    missing_categories = sorted(REQUIRED_CATEGORIES - categories)
    for category in missing_categories:
        errors.append(f"{fixture_path.relative_to(repo_root)}: missing category {category}")

    ids = [case.get("id") for case in cases]
    duplicate_ids = sorted({case_id for case_id in ids if ids.count(case_id) > 1})
    for case_id in duplicate_ids:
        errors.append(f"{fixture_path.relative_to(repo_root)}: duplicate case id {case_id}")

    for case in cases:
        case_id = case.get("id", "<missing-id>")
        if not case.get("category"):
            errors.append(f"{case_id}: missing category")
        if not case.get("expected", {}).get("status"):
            errors.append(f"{case_id}: missing expected status")

        if case.get("category") == "expected_output_structure":
            fields = set(case.get("expected", {}).get("output_fields", []))
            missing_fields = sorted(REQUIRED_OUTPUT_FIELDS - fields)
            for field in missing_fields:
                errors.append(f"{case_id}: expected output fields missing {field}")

        if case.get("category") in {"safety_boundary", "jurisdiction_conflicts"}:
            if not case.get("expected", {}).get("review_required"):
                errors.append(f"{case_id}: high-risk scenario must require review")

        validate_numeric_case(case, errors)

    errors.extend(validate_reverse_logistics_fixture(repo_root, known_skills))
    errors.extend(validate_canada_compliance_fixture(repo_root, known_skills))
    errors.extend(validate_us_compliance_fixture(repo_root, known_skills))
    errors.extend(validate_professional_composition_fixture(repo_root, known_skills))
    errors.extend(validate_specialization_framework_fixture(repo_root))
    errors.extend(validate_food_cold_chain_fixture(repo_root, known_skills))
    errors.extend(validate_dangerous_goods_fixture(repo_root, known_skills))
    errors.extend(validate_international_logistics_fixture(repo_root, known_skills))
    errors.extend(validate_repository_wide_integration_fixture(repo_root))
    return errors


def validate_evaluation_reports(repo_root: Path) -> list[str]:
    errors: list[str] = []
    required_reports = (
        (
            repo_root / "tests" / "evaluations" / "calculate-reorder-point-al-04-report.md",
            COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "warehouse-operator-al-06-report.md",
            AL_06_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "inventory-control-specialist-al-07-report.md",
            AL_07_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "warehouse-planner-al-08-report.md",
            AL_08_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "fulfillment-optimizer-al-09-report.md",
            AL_09_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "material-handling-analyst-al-10-report.md",
            AL_10_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "transportation-coordinator-al-11-report.md",
            AL_11_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "logistics-systems-analyst-al-12-report.md",
            AL_12_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "continuous-improvement-specialist-al-13-report.md",
            AL_13_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "warehouse-labor-planning-al-14-report.md",
            AL_14_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "reverse-logistics-al-15-report.md",
            AL_15_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "canada-compliance-al-16-report.md",
            AL_16_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "us-compliance-al-17-report.md",
            AL_17_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "professional-skillsets-al-18-report.md",
            AL_18_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "specialization-framework-al-19-report.md",
            AL_19_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "food-cold-chain-al-20-report.md",
            AL_20_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "dangerous-goods-al-21-report.md",
            AL_21_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "international-logistics-al-22-report.md",
            AL_22_COMPLETION_TOKEN,
        ),
        (
            repo_root / "tests" / "evaluations" / "repository-wide-integration-al-23-report.md",
            AL_23_COMPLETION_TOKEN,
        ),
    )

    for report_path, token in required_reports:
        if not report_path.is_file():
            errors.append(f"Missing evaluation report: {report_path.relative_to(repo_root)}")
            continue

        text = report_path.read_text(encoding="utf-8")
        required_phrases = (
            token,
            "Baseline Result Summary",
            "Skill-Enabled Result Summary",
            "Rubric Scores",
            "Decision",
            "keep",
        )
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{report_path.relative_to(repo_root)}: missing {phrase}")

    return errors


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    known_skills = skill_names(repo_root)
    tests_root = repo_root / "tests"

    if not tests_root.is_dir():
        return ["Missing tests directory"]

    errors.extend(validate_routing(repo_root, known_skills))
    errors.extend(validate_fixtures(repo_root, known_skills))
    errors.extend(validate_evaluation_reports(repo_root))
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

    print("Validated AgentLogistics test framework.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
