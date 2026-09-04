# AgentLogistics

AgentLogistics is an open-source AI skill repository for commercial logistics,
warehousing, storage, inventory control, transportation, distribution, material
handling, logistics systems, labor planning, and operational improvement.

It gives general-purpose AI agents structured logistics procedures, output
contracts, evidence expectations, quantitative checks, and safety boundaries so
they can support practical operational analysis without pretending to provide
legal, engineering, regulatory, equipment, or certification signoff.

## Who It Is For

AgentLogistics is intended for:

- AI agent builders who need reusable logistics skills and skillsets.
- Warehouse, inventory, transportation, and distribution teams evaluating AI
  support workflows.
- Operations analysts who need structured prompts for logistics investigations,
  calculations, planning, and improvement work.
- Contributors who want to add source-backed commercial logistics knowledge in
  small, testable units.

## What It Can Do

The repository currently covers:

- inbound receiving, ASN reconciliation, discrepancies, putaway, packing,
  staging, shipping, and reverse logistics;
- inventory classification, accuracy, turns, days on hand, reorder points,
  safety stock, EOQ, cycle counts, physical inventory, discrepancies, aging,
  stockouts, shrinkage, lot control, serialization, and expiration control;
- storage requirements, pallet positions, cube utilization, reserve and forward
  pick storage, slotting, capacity, congestion, zones, docks, and conceptual
  layouts;
- replenishment, picking strategies, pick paths, picking errors, cartonization,
  trailer loading, and shipping errors;
- material-handling selection, equipment requirements, equipment utilization,
  conveyors, AGV/AMR applications, AS/RS applications, and material flow;
- freight mode selection, shipment planning, carrier selection, rate
  comparison, freight costs, load utilization, consolidation, multi-stop
  shipments, carrier performance, freight audit, accessorials, detention,
  demurrage, bills of lading, and transportation KPIs;
- logistics systems and data flows across WMS, TMS, ERP, OMS, YMS, LMS, WCS,
  WES, EDI, APIs, barcode flows, GS1 identifiers, unit identification, and data
  quality;
- KPIs, scorecards, throughput, bottlenecks, root cause analysis, Pareto
  analysis, waste, scenario comparison, improvement plans, and result
  measurement;
- labor workload forecasts, staffing plans, workload balancing, labor
  productivity, overtime analysis, shift handoffs, and daily warehouse plans;
- source-bounded Canada, United States, food cold-chain, dangerous goods, and
  international logistics specializations.

## Quick Start

Clone the repository:

```powershell
git clone https://github.com/jeremylongworth-source/AgentLogistics.git
cd AgentLogistics
```

Run the local validation wrapper:

```powershell
.\scripts\validate-all.ps1
```

Expected result:

```text
All AgentLogistics validation checks passed.
```

The validation scripts use Python and PowerShell. No package install is
currently required for the repository checks.

## How To Use The Skills

AgentLogistics skills are written for AI agents that support progressive
disclosure. Start with the relevant `SKILL.md`, then load referenced files only
when the task requires more detail.

Example skill package:

```text
skills/inventory-control/calculate-reorder-point/
|-- SKILL.md
|-- agents/openai.yaml
`-- references/
```

Example use cases:

- Use `calculate-reorder-point` when average demand, lead time, and safety
  stock must be converted into a unit-checked reorder point.
- Use `investigate-inventory-discrepancy` when receiving records, WMS balances,
  physical counts, picks, and adjustments conflict.
- Use `plan-picking-wave` when order profile, capacity, cutoff, equipment, and
  labor constraints need a picking plan.
- Use `audit-freight-charge` when an invoice, rate basis, accessorials, and
  shipment evidence need a structured freight charge review.
- Use `triage-dangerous-goods-incident-logistics` only as source-backed
  logistics triage and escalation support, not as emergency, legal, regulatory,
  or hazmat response authority.

## Wiki

The GitHub wiki provides a public orientation layer for setup, scope,
repository structure, skill authoring, validation, skillsets, specializations,
safety boundaries, roadmap status, and the v1 release-candidate audit:

```text
https://github.com/jeremylongworth-source/AgentLogistics/wiki
```

## Repository Layout

```text
AgentLogistics/
|-- .github/
|-- docs/
|   |-- architecture/
|   |-- development/
|   |-- evaluation/
|   `-- standards/
|-- scripts/
|-- shared/
|-- skills/
|-- skillsets/
|-- specializations/
|-- tests/
|-- AGENTS.md
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
|-- ROADMAP.md
`-- SECURITY.md
```

Core project references:

- `ROADMAP.md` is the development authority.
- `docs/architecture/domain-contract.md` defines the project scope.
- `docs/architecture/master-taxonomy-v1.md` defines the skill taxonomy.
- `docs/standards/skill-authoring-standard.md` defines skill package
  requirements.
- `docs/standards/research-and-evidence-standard.md` defines source handling.
- `docs/standards/calculation-standard.md` defines calculation requirements.
- `docs/standards/testing-standard.md` and
  `docs/standards/evaluation-standard.md` define validation expectations.
- `tests/expected-routing.yaml` records scenario routing expectations.

## Skillsets

Professional skillsets compose existing atomic skills instead of duplicating
their procedures:

- `skillsets/warehouse-operator/`
- `skillsets/receiving-specialist/`
- `skillsets/inventory-control-specialist/`
- `skillsets/warehouse-supervisor/`
- `skillsets/warehouse-manager/`
- `skillsets/logistics-coordinator/`
- `skillsets/transportation-coordinator/`
- `skillsets/warehouse-planner/`
- `skillsets/distribution-manager/`
- `skillsets/logistics-systems-analyst/`
- `skillsets/continuous-improvement-specialist/`
- `skillsets/logistics-operations-manager/`

See `skillsets/README.md` for the professional composition index.

## Limitations

AgentLogistics is decision-support content. It does not operate live WMS, TMS,
ERP, OMS, YMS, LMS, WCS, WES, freight, customs, carrier, government, or safety
systems.

It does not approve:

- inventory adjustments, financial postings, carrier awards, rate acceptance,
  freight claims, supplier claims, customer commitments, or payment decisions;
- live system changes, production data edits, labor commitments, staffing
  decisions, equipment purchases, facility changes, structural rack changes, or
  building expansion;
- food safety release, dangerous-goods classification approval, customs entry
  approval, legal compliance, engineering approval, operator certification,
  equipment certification, regulatory approval, or professional signoff.

Regulatory and safety-sensitive material is jurisdiction-specific unless a
source clearly states otherwise. Contributors and users must verify current
requirements with the applicable authority before acting.

## Development Status

AgentLogistics is in pre-v1 development. The completed gates are:

```text
AGENTLOGISTICS_AL_00_BASELINE_READY
AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY
AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY
AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY
AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY
AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY
AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY
AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY
AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY
AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY
AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY
AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY
AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY
AGENTLOGISTICS_AL_15_REVERSE_LOGISTICS_READY
AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY
AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY
AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY
AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY
AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY
AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY
AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY
AGENTLOGISTICS_AL_23_INTEGRATION_VALIDATED
AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY
AGENTLOGISTICS_AL_25_V1_RC_AUDIT_COMPLETE
```

Current v1 audit verdict: `V1_PARTIALLY_READY`.

No v1 release has been tagged. The next development focus is v1 hardening:
live model evaluation, source freshness checks, expanded calculation fixtures,
CI visibility, release notes, and release tagging only after those gates pass.

## Contributing

Read `CONTRIBUTING.md` before opening an issue or pull request. In short:

- keep new skills atomic;
- map each skill to one primary domain family;
- separate universal logistics practice from jurisdiction-specific content;
- cite authoritative sources for regulatory, safety, standards, and calculation
  claims;
- add or update scenarios, fixtures, evaluations, and validators when behavior
  changes;
- run `.\scripts\validate-all.ps1` before submitting.

## Security And Safety

Report tooling vulnerabilities and safety-sensitive content concerns using
`SECURITY.md`. Do not post secrets, credentials, customer data, shipment data,
facility layouts, personnel records, or other sensitive operational details in
public issues.

## License

AgentLogistics is licensed under the MIT License. See `LICENSE`.
