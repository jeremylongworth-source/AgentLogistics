# AgentLogistics Development Roadmap

Repository: `D:\AgentLogistics`
Remote: `https://github.com/jeremylongworth-source/AgentLogistics`

This roadmap was recovered from the ChatGPT chat titled `Plan AgentLogistics
Skills` on 2026-09-03. The available task transcript preserves the roadmap
through AL-15 and begins AL-16 before the API truncates the original message.
The recovered waves below are the local execution authority. AL-16 and later
are marked as continuation candidates until the missing source text is recovered
or deliberately replanned.

## Mission

AgentLogistics will provide reusable, testable AI skills that allow
general-purpose AI agents to perform commercial logistics work with greater
structure, domain awareness, quantitative rigor, and operational consistency.

The repository should ultimately support AI capabilities comparable to:

- Warehouse Operator
- Receiving Specialist
- Inventory Control Specialist
- Warehouse Supervisor
- Warehouse Manager
- Logistics Coordinator
- Transportation Coordinator
- Warehouse Planner
- Distribution Manager
- Logistics Systems Analyst
- Continuous Improvement Specialist
- Logistics Operations Manager

AgentLogistics is a specialist repository in the same broader family as
AgentSkills and ChefSkills, but it must remain an independent project.

## Core Principles

### Atomic Skills First

A skill should perform a bounded task.

Good examples:

```text
calculate-reorder-point
investigate-inventory-discrepancy
select-picking-strategy
calculate-warehouse-capacity
analyze-carrier-performance
```

Avoid large monolithic skills such as:

```text
manage-warehouse
do-logistics
inventory-management
transportation-management
```

Large professional capabilities belong in the skillset and composition layer.

### Separate Knowledge From Procedure

A skill should distinguish:

1. what the agent must know;
2. what the agent must calculate;
3. what procedure it should follow;
4. what evidence it requires;
5. what output it should produce.

Do not turn `SKILL.md` into a logistics textbook. Supporting material should be
placed in references where appropriate.

### Progressive Disclosure

Load only the information required for the current task.

Preferred structure:

```text
skills/
  inventory-control/
    calculate-reorder-point/
      SKILL.md
      references/
        formulas.md
        examples.md
```

### Evidence-Backed Domain Knowledge

Authoritative information should be preferred over unsourced summaries.

Expected source hierarchy:

1. Government legislation and regulators
2. Official standards organizations
3. Recognized industry standards
4. Professional associations
5. Academic and technical literature
6. Major logistics technology providers for product-specific concepts
7. High-quality industry publications
8. Secondary material when primary information is unavailable

Important authorities may include Transport Canada, Canadian Centre for
Occupational Health and Safety, provincial Canadian regulators, OSHA, FMCSA,
PHMSA, CBP, CBSA, GS1, ISO, ASCM, CSCMP, IATA, IMO, and UNECE.

### Regulatory Isolation

Universal logistics knowledge must not be mixed indiscriminately with
jurisdiction-specific legal requirements.

Regulatory content must identify:

- jurisdiction;
- authority;
- applicability;
- source;
- source date where appropriate;
- last verification date;
- whether the rule may change over time.

### Safety Boundaries

AgentLogistics may assist with safety planning, hazard identification, procedure
analysis, compliance research, inspection preparation, equipment-selection
analysis, and operational risk analysis.

It must not falsely represent AI guidance as professional engineering approval,
equipment certification, operator certification, regulatory approval, or legally
binding compliance advice.

### Quantitative Correctness

Logistics calculations are first-class capabilities.

Every calculation-oriented skill should define:

- variables;
- units;
- formula;
- assumptions;
- required inputs;
- missing-input behavior;
- edge cases;
- output interpretation;
- at least one worked test case.

Unit consistency must be explicitly validated.

## Planned Architecture

This architecture is provisional until the architecture waves close.

```text
AgentLogistics/
|-- README.md
|-- ROADMAP.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- CHANGELOG.md
|-- docs/
|   |-- architecture/
|   |-- standards/
|   |-- research/
|   `-- development/
|-- skills/
|   |-- logistics-fundamentals/
|   |-- inbound-receiving/
|   |-- storage-warehousing/
|   |-- inventory-control/
|   |-- replenishment-picking/
|   |-- packing-shipping/
|   |-- material-handling/
|   |-- transportation-freight/
|   |-- warehouse-design/
|   |-- logistics-systems-data/
|   |-- performance-improvement/
|   |-- labor-planning/
|   `-- reverse-logistics/
|-- skillsets/
|-- specializations/
|-- shared/
|-- tests/
`-- tools/
```

Do not create empty directory trees merely to match this proposal. Directories
should be introduced when they have real content.

## Master Development Sequence

Each wave ends in one of:

```text
READY
PARTIALLY_READY
BLOCKED
```

No next wave should silently absorb unresolved work from the previous wave.
A handoff must record unresolved issues explicitly.

## WAVE AL-00: Repository Discovery and Baseline

Objective: establish repository truth before architecture or content work
begins.

Required artifact:

```text
docs/development/AL-00-baseline-audit.md
```

Gate: close as `READY` only when repository state and starting assumptions are
documented.

Completion token:

```text
AGENTLOGISTICS_AL_00_BASELINE_READY
```

## WAVE AL-01: Scope and Domain Contract

Objective: define what AgentLogistics is and is not.

Required artifacts:

```text
docs/architecture/domain-contract.md
docs/architecture/scope-boundaries.md
```

Gate: every planned core skill must be able to map to a domain or be rejected
as out-of-scope.

Completion token:

```text
AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY
```

## WAVE AL-02: Master Taxonomy Audit

Objective: turn the approximately 160 proposed skills into a defensible v1
taxonomy.

Audit every candidate for atomicity, duplicate intent, overlapping
responsibility, naming consistency, domain assignment, prerequisite
relationships, expected inputs, expected outputs, quantitative requirements,
regulatory dependency, and safety sensitivity.

Classify each candidate as:

```text
CORE
ADVANCED
SPECIALIST
MERGE
SPLIT
DEFER
REMOVE
```

Required artifacts:

```text
docs/architecture/master-taxonomy-v1.md
docs/architecture/taxonomy-audit.md
docs/architecture/dependency-map.md
```

Gate: no unresolved duplicate or obviously non-atomic skills remain in the core
taxonomy.

Completion token:

```text
AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY
```

## WAVE AL-03: Skill Specification Standard

Objective: define the contract every AgentLogistics skill must follow.

Required artifacts:

```text
docs/standards/skill-authoring-standard.md
docs/standards/skill-naming-standard.md
docs/standards/research-and-evidence-standard.md
docs/standards/calculation-standard.md
docs/standards/regulatory-content-standard.md
skills/inventory-control/calculate-reorder-point/
```

Gate: the sample skill must demonstrate the complete standard and pass review
before mass authoring begins.

Completion token:

```text
AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY
```

## WAVE AL-04: Validation and Evaluation Framework

Objective: create quality controls before scaling skill production.

Define tests for correct invocation, incorrect invocation, missing inputs, bad
inputs, calculation correctness, unit mismatch, ambiguous scenarios, expected
output structure, safety boundaries, jurisdiction conflicts, and unsupported
assumptions.

Required artifacts:

```text
docs/standards/testing-standard.md
docs/standards/evaluation-standard.md
tests/
```

Gate: the AL-03 reference skill must have passing tests.

Completion token:

```text
AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY
```

## WAVE AL-05: Shared Logistics Foundations

Objective: build reusable references that should not be duplicated across
individual skills.

Candidate foundations include terminology, common units, dimensions, weight and
volume conversions, pallet terminology, case/inner/each hierarchy, location
concepts, SKU terminology, lead-time concepts, throughput terminology,
inventory state terminology, order-state terminology, and KPI definitions.

Required artifacts should populate these paths only as justified:

```text
shared/glossaries/
shared/formulas/
shared/schemas/
shared/templates/
```

Gate: shared material must demonstrably reduce duplication and have an active
consumer.

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## WAVE AL-06: Warehouse Core Skillset

Objective: produce the first useful end-to-end operational capability.

Prioritized skills:

```text
analyze-logistics-operation
map-logistics-flow
identify-logistics-constraints
analyze-product-flow
analyze-order-profile
plan-inbound-receiving
verify-inbound-shipment
reconcile-asn
process-receiving-discrepancy
plan-putaway
diagnose-receiving-bottleneck
classify-storage-requirements
calculate-storage-capacity
calculate-pallet-positions
analyze-storage-utilization
plan-replenishment
select-picking-strategy
calculate-pick-productivity
plan-packing-operation
plan-shipping-stage
verify-outbound-shipment
```

Composition target:

```text
skillsets/warehouse-operator/
```

Gate: the skillset must successfully reason through receive, inspect, putaway,
store, replenish, pick, pack, stage, and ship.

Completion token:

```text
AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY
```

## WAVE AL-07: Inventory Control System

Objective: build the complete general-purpose inventory foundation.

Priority skills:

```text
classify-inventory
calculate-inventory-accuracy
calculate-inventory-turns
calculate-days-on-hand
calculate-reorder-point
calculate-safety-stock
calculate-eoq
design-min-max-policy
design-cycle-count-program
plan-physical-inventory
reconcile-inventory
investigate-inventory-discrepancy
analyze-inventory-aging
identify-dead-stock
analyze-stockout
manage-lot-controlled-inventory
manage-serialized-inventory
manage-expiration-controlled-inventory
select-inventory-rotation-policy
analyze-inventory-shrinkage
```

Composition target:

```text
skillsets/inventory-control-specialist/
```

Completion token:

```text
AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY
```

## WAVE AL-08: Storage, Slotting and Facility Planning

Objective: develop physical storage and warehouse-planning intelligence.

Build storage-system selection, pallet-position calculations, cube
calculations, density, forward vs reserve allocation, slotting, SKU velocity,
product affinity, travel-distance considerations, capacity, congestion, zoning,
and conceptual layout reasoning.

Boundary: do not represent conceptual planning as structural engineering
approval.

Composition target:

```text
skillsets/warehouse-planner/
```

Completion token:

```text
AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY
```

## WAVE AL-09: Replenishment and Fulfillment Optimization

Objective: advance warehouse core from basic execution to optimization.

Priority skills:

```text
calculate-replenishment-demand
prioritize-replenishment
plan-picking-wave
plan-batch-picking
plan-zone-picking
optimize-pick-path
analyze-pick-accuracy
diagnose-picking-bottleneck
investigate-picking-error
plan-cartonization
plan-trailer-loading
investigate-shipping-error
```

Gate: test against low-volume/high-SKU, high-volume/low-SKU, ecommerce
each-pick, case-pick, pallet movement, and mixed-order profiles.

Completion token:

```text
AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY
```

## WAVE AL-10: Material Handling Systems

Objective: enable structured material-handling analysis.

Priority skills:

```text
classify-material-handling-requirements
select-material-handling-equipment
calculate-equipment-requirements
analyze-equipment-utilization
plan-material-flow
evaluate-conveyor-application
evaluate-agv-amr-application
evaluate-asrs-application
```

Required considerations include load, dimensions, volume, travel distance,
throughput, storage height, aisle requirements, operating environment,
automation level, safety, and capital intensity.

Gate: distinguish selection analysis from equipment certification.

Completion token:

```text
AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY
```

## WAVE AL-11: Transportation and Freight Core

Objective: extend AgentLogistics beyond warehouse boundaries.

Priority skills:

```text
select-transportation-mode
plan-freight-shipment
select-carrier
compare-freight-rates
calculate-freight-cost
calculate-load-utilization
plan-freight-consolidation
plan-multi-stop-shipment
analyze-carrier-performance
audit-freight-charge
analyze-freight-accessorials
manage-freight-claim
analyze-detention
analyze-demurrage
interpret-bill-of-lading
analyze-transportation-kpis
```

Composition target:

```text
skillsets/transportation-coordinator/
```

Gate: validate truckload, LTL, and parcel reasoning separately. Do not treat
international transportation rules as universal.

Completion token:

```text
AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY
```

## WAVE AL-12: Logistics Systems and Data

Objective: build operational systems reasoning.

Core concepts include WMS, TMS, ERP, OMS, YMS, LMS, WCS, WES, EDI, and APIs.

Priority skills:

```text
map-wms-process
analyze-wms-transaction-history
diagnose-wms-inventory-issue
validate-item-master-data
validate-location-master-data
analyze-logistics-scan-events
design-logistics-barcode-flow
interpret-gs1-identifiers
design-logistics-unit-identification
analyze-edi-logistics-flow
map-erp-wms-integration
map-wms-tms-integration
analyze-logistics-data-quality
```

Special research requirement: GS1 concepts must be sourced from GS1 material
wherever possible.

Composition target:

```text
skillsets/logistics-systems-analyst/
```

Completion token:

```text
AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY
```

## WAVE AL-13: Performance and Continuous Improvement

Objective: give AgentLogistics operations-analysis capability.

Priority skills:

```text
select-logistics-kpis
build-logistics-scorecard
analyze-warehouse-kpis
analyze-throughput
diagnose-throughput-loss
identify-logistics-bottleneck
perform-logistics-root-cause-analysis
perform-logistics-pareto-analysis
map-warehouse-process
analyze-logistics-waste
compare-logistics-scenarios
build-logistics-improvement-plan
measure-improvement-result
```

Gate: improvement recommendations must distinguish observation, evidence,
inference, root cause, recommendation, expected effect, and measurement plan.

Composition target:

```text
skillsets/continuous-improvement-specialist/
```

Completion token:

```text
AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY
```

## WAVE AL-14: Labor and Operating Planning

Objective: support day-to-day warehouse management.

Priority skills:

```text
forecast-warehouse-workload
calculate-labor-requirements
plan-warehouse-staffing
balance-warehouse-workload
analyze-labor-productivity
analyze-overtime-requirements
plan-shift-handoff
build-daily-warehouse-plan
```

Composition targets:

```text
skillsets/warehouse-supervisor/
skillsets/warehouse-manager/
```

Completion token:

```text
AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY
```

## WAVE AL-15: Returns and Reverse Logistics

Objective: complete the general warehouse lifecycle.

Priority skills:

```text
process-customer-return
classify-return-disposition
inspect-returned-goods
reconcile-returned-inventory
analyze-return-reason
analyze-return-rate
plan-return-to-stock
plan-return-to-vendor
manage-damaged-inventory
manage-nonconforming-inventory
analyze-reverse-logistics-cost
design-reverse-logistics-flow
```

Completion token:

```text
AGENTLOGISTICS_AL_15_REVERSE_LOGISTICS_READY
```

## AL-16 And Later: Continuation Candidates

The recovered source begins AL-16 as Canadian Logistics Safety and Compliance,
with the objective to build the first jurisdiction-specific specialization. The
full source text was truncated at that point in the local task API.

Based on the earlier planning discussion, later waves should likely cover:

- Canadian logistics safety and compliance.
- United States logistics safety and compliance.
- Specialist packs such as food logistics, cold chain, dangerous goods,
  ecommerce, manufacturing, retail distribution, automotive, pharmaceuticals,
  international logistics, and reverse logistics refinements.
- Higher-order professional skillsets and orchestration.
- Open-source release readiness, evaluation credibility, documentation,
  contributor workflow, and publication gates.

These continuation candidates are not closed roadmap waves yet. They need a
future recovery or replanning pass before implementation.
