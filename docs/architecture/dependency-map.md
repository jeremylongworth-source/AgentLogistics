# AgentLogistics Dependency Map

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY
```

## Purpose

This document records the prerequisite structure for the AgentLogistics master
taxonomy. It is a planning dependency map, not an implementation graph. AL-03
will define how individual skills declare dependencies in their metadata.

## Dependency Rules

- Foundational analysis skills must precede optimization skills.
- Data validation must precede data diagnosis.
- Measurement must precede diagnosis.
- Diagnosis must precede improvement planning.
- Universal core skills must not depend on jurisdiction or industry
  specializations.
- Safety-sensitive planning skills may identify a need for specialist review,
  but they must not depend on unbuilt regulatory content.

## System Spine

The repository should develop from general logistics understanding into
warehouse lifecycle execution, then into optimization and specialization.

```text
analyze-logistics-operation
  -> classify-logistics-operation
  -> define-logistics-requirements
  -> map-logistics-flow
  -> analyze-product-flow
  -> analyze-order-profile
```

These skills should exist before higher-order warehouse, inventory,
transportation, or systems skillsets rely on the taxonomy.

## Warehouse Lifecycle Chain

```text
plan-inbound-receiving
  -> schedule-dock-appointments
  -> verify-inbound-shipment
  -> reconcile-asn
  -> inspect-received-goods
  -> process-receiving-discrepancy
  -> manage-receiving-exceptions
  -> manage-quarantine-inventory
  -> plan-putaway
  -> select-putaway-location
```

Cross-docking branches from inbound receiving and reconnects to outbound
staging:

```text
plan-inbound-receiving
  -> plan-cross-dock-operation
  -> plan-shipping-stage
```

## Storage and Slotting Chain

```text
classify-storage-requirements
  -> select-storage-system
  -> calculate-storage-capacity
  -> calculate-pallet-positions
  -> calculate-cube-utilization
  -> analyze-storage-utilization
```

Advanced storage optimization:

```text
analyze-order-profile
  -> plan-forward-pick-storage
  -> slot-warehouse-inventory
  -> analyze-product-affinity
  -> analyze-slotting-efficiency
  -> optimize-storage-density
```

Racking remains safety-sensitive:

```text
select-storage-system
  -> evaluate-racking-strategy
```

## Inventory Control Chain

Core inventory visibility:

```text
validate-item-master-data
  -> classify-inventory
  -> calculate-inventory-accuracy
  -> reconcile-inventory
  -> investigate-inventory-discrepancy
```

Policy and replenishment math:

```text
calculate-logistics-lead-time
  -> calculate-reorder-point
  -> calculate-safety-stock
  -> design-min-max-policy
```

Financial and aging indicators:

```text
classify-inventory
  -> calculate-inventory-turns
  -> calculate-days-on-hand
  -> analyze-inventory-aging
  -> identify-dead-stock
```

Control attributes:

```text
classify-inventory
  -> manage-lot-controlled-inventory
  -> manage-expiration-controlled-inventory
  -> select-inventory-rotation-policy
```

```text
classify-inventory
  -> manage-serialized-inventory
```

Loss and service diagnostics:

```text
reconcile-inventory
  -> investigate-inventory-discrepancy
  -> analyze-inventory-shrinkage
```

```text
calculate-reorder-point
  -> analyze-stockout
```

## Replenishment and Picking Chain

```text
analyze-order-profile
  -> select-picking-strategy
  -> plan-replenishment
  -> calculate-replenishment-demand
  -> prioritize-replenishment
```

Picking method branches:

```text
select-picking-strategy
  -> plan-picking-wave
```

```text
select-picking-strategy
  -> plan-batch-picking
```

```text
select-picking-strategy
  -> plan-zone-picking
```

Optimization and error analysis:

```text
slot-warehouse-inventory
  -> optimize-pick-path
```

```text
select-picking-strategy
  -> calculate-pick-productivity
  -> analyze-pick-accuracy
  -> investigate-picking-error
```

```text
calculate-pick-productivity
  -> diagnose-picking-bottleneck
```

## Packing, Staging and Shipping Chain

```text
select-picking-strategy
  -> plan-packing-operation
  -> select-shipping-packaging
  -> plan-cartonization
  -> verify-order-before-shipping
  -> plan-shipping-stage
  -> verify-outbound-shipment
```

Carrier and loading branches:

```text
plan-shipping-stage
  -> manage-carrier-cutoffs
```

```text
plan-shipping-stage
  -> plan-trailer-loading
```

Shipping exception branch:

```text
verify-outbound-shipment
  -> manage-shipping-exception
  -> investigate-shipping-error
```

Order metrics:

```text
analyze-order-profile
  -> calculate-order-cycle-time
  -> analyze-order-accuracy
```

## Material Handling Chain

```text
analyze-product-flow
  -> classify-material-handling-requirements
  -> select-material-handling-equipment
  -> calculate-equipment-requirements
  -> analyze-equipment-utilization
```

Flow and automation branches:

```text
classify-material-handling-requirements
  -> plan-material-flow
  -> evaluate-conveyor-application
```

```text
plan-material-flow
  -> evaluate-agv-amr-application
```

```text
select-storage-system
  -> evaluate-asrs-application
```

## Transportation and Freight Chain

```text
define-logistics-requirements
  -> select-transportation-mode
  -> plan-freight-shipment
  -> select-carrier
```

Cost and audit branch:

```text
plan-freight-shipment
  -> compare-freight-rates
  -> calculate-freight-cost
  -> audit-freight-charge
  -> analyze-freight-accessorials
```

Utilization and planning branch:

```text
plan-freight-shipment
  -> calculate-load-utilization
  -> plan-freight-consolidation
  -> plan-multi-stop-shipment
```

Documentation and claims branch:

```text
plan-freight-shipment
  -> interpret-bill-of-lading
  -> verify-outbound-shipment
  -> manage-freight-claim
```

Performance branch:

```text
select-carrier
  -> analyze-carrier-performance
  -> analyze-transportation-kpis
```

Specialist branches:

```text
plan-freight-shipment
  -> plan-customs-broker-handoff
```

```text
plan-freight-shipment
  -> classify-dangerous-goods-logistics-requirements
```

## Warehouse Design and Capacity Chain

```text
calculate-storage-capacity
  -> calculate-warehouse-capacity
  -> analyze-space-utilization
  -> forecast-capacity-requirements
```

Layout branch:

```text
analyze-space-utilization
  -> plan-warehouse-zones
  -> analyze-warehouse-flow
  -> identify-warehouse-congestion
  -> design-conceptual-warehouse-layout
  -> compare-warehouse-layouts
```

Dock and expansion branches:

```text
schedule-dock-appointments
  -> plan-dock-capacity
```

```text
forecast-capacity-requirements
  -> plan-warehouse-expansion
```

## Logistics Systems and Data Chain

Master data:

```text
validate-item-master-data
  -> interpret-gs1-identifiers
  -> design-logistics-unit-identification
```

```text
validate-location-master-data
  -> map-wms-process
```

WMS diagnosis:

```text
map-wms-process
  -> analyze-wms-transaction-history
  -> diagnose-wms-inventory-issue
```

Capture and integration:

```text
map-wms-process
  -> analyze-logistics-scan-events
  -> design-logistics-barcode-flow
```

```text
design-logistics-unit-identification
  -> analyze-edi-logistics-flow
```

```text
map-wms-process
  -> map-erp-wms-integration
```

```text
map-wms-process
  -> map-wms-tms-integration
```

Data quality:

```text
validate-item-master-data
  -> analyze-logistics-data-quality
```

```text
analyze-order-profile
  -> analyze-order-management-flow
```

## Performance and Continuous Improvement Chain

Measurement:

```text
define-logistics-requirements
  -> select-logistics-kpis
  -> build-logistics-scorecard
  -> analyze-warehouse-kpis
```

Throughput:

```text
map-logistics-flow
  -> analyze-throughput
  -> diagnose-throughput-loss
  -> identify-logistics-bottleneck
```

Improvement:

```text
map-warehouse-process
  -> analyze-logistics-waste
  -> perform-logistics-pareto-analysis
  -> perform-logistics-root-cause-analysis
  -> build-logistics-improvement-plan
  -> measure-improvement-result
```

Scenario comparison:

```text
build-logistics-scorecard
  -> compare-logistics-scenarios
```

Risk and sustainability:

```text
map-logistics-flow
  -> analyze-logistics-risk
```

```text
select-logistics-kpis
  -> analyze-logistics-sustainability
```

## Labor and Operational Planning Chain

```text
analyze-order-profile
  -> forecast-warehouse-workload
  -> calculate-labor-requirements
  -> plan-warehouse-staffing
  -> balance-warehouse-workload
  -> build-daily-warehouse-plan
  -> plan-shift-handoff
```

Productivity and overtime:

```text
select-logistics-kpis
  -> analyze-labor-productivity
```

```text
calculate-labor-requirements
  -> analyze-overtime-requirements
```

## Returns and Reverse Logistics Chain

```text
verify-outbound-shipment
  -> process-customer-return
  -> inspect-returned-goods
  -> classify-return-disposition
```

Inventory branches:

```text
classify-return-disposition
  -> plan-return-to-stock
  -> reconcile-returned-inventory
```

```text
classify-return-disposition
  -> plan-return-to-vendor
```

```text
inspect-returned-goods
  -> manage-damaged-inventory
```

```text
manage-quarantine-inventory
  -> manage-nonconforming-inventory
```

Analysis branch:

```text
process-customer-return
  -> analyze-return-reason
  -> analyze-return-rate
  -> analyze-reverse-logistics-cost
  -> design-reverse-logistics-flow
```

## First Useful Build Order

AL-03 and AL-04 should build the standards and tests before any broad skill
authoring. After that, the first useful implementation order is:

1. logistics spine;
2. warehouse lifecycle P0 skills;
3. inventory P0 skills;
4. storage/capacity P0 calculations;
5. picking/packing/shipping P0 flow;
6. KPI and throughput P0 measurement;
7. AL-06 warehouse-operator skillset.

## Blocked Dependencies

No AL-02 dependency is blocked. The following dependencies are intentionally
held for later waves:

- `plan-logistics-network` waits for network-design scope decisions.
- `plan-yard-operations` waits for dock, transportation, and facility-flow
  foundations.
- `analyze-logistics-sustainability` waits for source-backed metrics and
  accounting boundaries.
- `plan-customs-broker-handoff` waits for jurisdiction/international logistics
  specialization.
- `classify-dangerous-goods-logistics-requirements` waits for dangerous-goods
  regulatory standards.

