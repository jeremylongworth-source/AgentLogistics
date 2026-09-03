# AgentLogistics

AgentLogistics is an open-source AI skill repository for commercial logistics,
warehousing, storage, inventory movement, transportation, distribution,
material handling, logistics systems, and operational improvement.

The project is intended to make general-purpose AI agents better at structured
logistics work: identifying constraints, tracing operational evidence,
performing unit-aware calculations, separating universal practice from
jurisdiction-specific rules, and producing practical outputs for logistics
operators and managers.

## Status

AgentLogistics is in initial repository development.

Current completed gates:

- `AGENTLOGISTICS_AL_00_BASELINE_READY`
- `AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY`
- `AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY`
- `AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY`
- `AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY`
- `AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY`
- `AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY`
- `AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY`
- `AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY`
- `AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY`
- `AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY`
- `AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY`
- `AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY`
- `AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY`
- `AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY`
- `AGENTLOGISTICS_AL_15_REVERSE_LOGISTICS_READY`
- `AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY`

The next planned wave is AL-17: United States Logistics Safety and Compliance.

## Scope

The core project covers 13 domain families:

1. Logistics Fundamentals
2. Receiving and Inbound
3. Storage and Warehousing
4. Inventory Control
5. Replenishment and Picking
6. Packing, Staging and Shipping
7. Material Handling
8. Transportation and Freight
9. Warehouse Design and Capacity
10. Logistics Systems and Data
11. Performance and Continuous Improvement
12. Labor and Operational Planning
13. Returns and Reverse Logistics

Specializations such as Canada, United States, food logistics, cold chain,
dangerous goods, ecommerce, manufacturing, retail distribution, automotive,
pharmaceuticals, and international logistics should remain isolated from the
universal core until their sources, jurisdiction, and safety boundaries are
clear.

## Repository Layout

Current real content:

```text
AgentLogistics/
|-- docs/
|   |-- architecture/
|   |-- development/
|   `-- standards/
|-- scripts/
|-- shared/
|-- skills/
|-- skillsets/
|-- specializations/
|-- tests/
|-- AGENTS.md
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
`-- ROADMAP.md
```

Future waves may add additional validation tooling when new repository areas
have real content.

Core architecture artifacts:

- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/master-taxonomy-v1.md`
- `docs/architecture/taxonomy-audit.md`
- `docs/architecture/dependency-map.md`

Core standards artifacts:

- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/calculation-standard.md`
- `docs/standards/regulatory-content-standard.md`
- `docs/standards/testing-standard.md`
- `docs/standards/evaluation-standard.md`

Reference skill:

- `skills/inventory-control/calculate-reorder-point/`

Warehouse skillset:

- `skillsets/warehouse-operator/`

Inventory skillset:

- `skillsets/inventory-control-specialist/`

Warehouse planning skillset:

- `skillsets/warehouse-planner/`

Fulfillment optimization skillset:

- `skillsets/fulfillment-optimizer/`

Material handling skillset:

- `skillsets/material-handling-analyst/`

Transportation skillset:

- `skillsets/transportation-coordinator/`

Logistics systems skillset:

- `skillsets/logistics-systems-analyst/`

Continuous improvement skillset:

- `skillsets/continuous-improvement-specialist/`

Warehouse supervisor skillset:

- `skillsets/warehouse-supervisor/`

Warehouse manager skillset:

- `skillsets/warehouse-manager/`

Reverse logistics skill family:

- `skills/reverse-logistics/`

Canada specialization:

- `specializations/canada/`

Current test target:

- `tests/fixtures/calculate-reorder-point-cases.json`
- `tests/fixtures/inventory-discrepancy-investigation.json`
- `tests/fixtures/warehouse-planner-layout-concept.json`
- `tests/fixtures/fulfillment-optimizer-order-profiles.json`
- `tests/fixtures/material-handling-selection-analysis.json`
- `tests/fixtures/transportation-coordinator-multimode-core.json`
- `tests/fixtures/logistics-systems-analyst-integration-data-quality.json`
- `tests/fixtures/continuous-improvement-specialist-performance-review.json`
- `tests/fixtures/warehouse-supervisor-daily-operating-plan.json`
- `tests/fixtures/warehouse-manager-labor-operating-plan.json`
- `tests/fixtures/reverse-logistics-return-lifecycle.json`
- `tests/fixtures/canada-compliance-source-triage.json`
- `tests/expected-routing.yaml`

Shared foundations:

- `shared/README.md`
- `shared/glossaries/common-units.md`
- `shared/glossaries/inventory-state-terms.md`
- `shared/formulas/reorder-point.md`
- `shared/schemas/reorder-point-calculation.schema.json`
- `shared/templates/calculation-output.md`

## Development Model

AgentLogistics follows a wave-based roadmap. Each wave must close as:

- `READY`
- `PARTIALLY_READY`
- `BLOCKED`

Unresolved work must be recorded explicitly before the next wave starts.

Run local validation with:

```powershell
.\scripts\validate-all.ps1
```

## Safety Boundary

AgentLogistics may help with safety planning, hazard identification, procedure
analysis, compliance research, inspection preparation, equipment-selection
analysis, and operational risk analysis.

It must not present AI-generated guidance as professional engineering approval,
equipment certification, operator certification, regulatory approval, legally
binding compliance advice, or a substitute for qualified professional review.

## License

MIT
