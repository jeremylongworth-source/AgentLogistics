# AgentLogistics Master Taxonomy v1

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY
```

## Scope

This document is the canonical AL-02 taxonomy for AgentLogistics. It converts
the initial planning list into named, classified skill candidates that later
waves can implement as atomic skills or compose into skillsets.

This is not a promise that every row has been implemented. It is the routing and
planning contract for what may be implemented.

## Classification

- `CORE`: foundational, broadly useful, and eligible for v1 core authoring.
- `ADVANCED`: valid atomic skill, but depends on stronger foundations,
  calculations, data quality, or multi-step operational reasoning.
- `SPECIALIST`: valid capability, but tied to a jurisdiction, industry,
  regulation, equipment class, transport mode, or specialized operating model.
- `DEFER`: valid capability, but outside the near-term v1 critical path.
- `MERGE`: not accepted as a standalone skill because another skill owns it.
- `SPLIT`: too broad and must be decomposed before implementation.
- `REMOVE`: rejected from AgentLogistics scope.

No `MERGE`, `SPLIT`, or `REMOVE` items remain in the canonical core taxonomy.
Resolved boundary decisions are recorded in `taxonomy-audit.md`.

## Priority

- `P0`: required for the first useful warehouse and inventory agent.
- `P1`: required for strong v1 coverage.
- `P2`: valuable advanced capability after the foundation is proven.
- `P3`: specialization, post-v1 candidate, or explicit later-wave work.

## Audit Fields

Each row records the AL-02 audit outcome:

- atomic candidate name;
- classification;
- priority;
- primary domain;
- expected input profile;
- expected output profile;
- calculation requirement;
- regulatory and safety sensitivity;
- prerequisite relationship.

The input and output profiles are intentionally compact. AL-03 will define the
full skill authoring standard.

## Summary Counts

| Class | Count | Notes |
|---|---:|---|
| `CORE` | 87 | Universal foundational skills. |
| `ADVANCED` | 77 | Accepted skills that require foundations, stronger procedures, or calculations. |
| `DEFER` | 3 | Valid capabilities tracked outside the immediate v1 critical path. |
| `SPECIALIST` | 2 | Valid capabilities isolated from universal core. |
| Total tracked candidates | 169 | Original 160 plus 9 source-scan additions or explicit later-wave gap captures. |

## Logistics Fundamentals

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `analyze-logistics-operation` | CORE | P0 | operation description, facilities, flows, products | operating model assessment | None | Low | None |
| `map-logistics-flow` | CORE | P0 | process steps, nodes, documents, systems | flow map and handoff list | None | Low | `analyze-logistics-operation` |
| `define-logistics-requirements` | CORE | P0 | business need, service levels, constraints | requirements brief | None | Low | `analyze-logistics-operation` |
| `identify-logistics-constraints` | CORE | P0 | operation, volumes, capacity, service promises | constraint register | Optional | Medium | `map-logistics-flow` |
| `classify-logistics-operation` | CORE | P0 | facility type, order profile, product profile | operation classification | None | Low | `analyze-logistics-operation` |
| `analyze-product-flow` | CORE | P0 | SKU/load data, movement path, handling requirements | product-flow assessment | Optional | Medium | `map-logistics-flow` |
| `analyze-order-profile` | CORE | P0 | order lines, units, frequency, channels | order-profile summary | Basic | Low | `classify-logistics-operation` |
| `calculate-logistics-lead-time` | CORE | P0 | process timestamps, queues, transit time | lead-time calculation | Required | Low | `map-logistics-flow` |
| `analyze-cost-to-serve` | ADVANCED | P1 | activity costs, order/customer/channel segments | cost-to-serve model | Required | Low | `analyze-order-profile` |
| `compare-logistics-strategies` | ADVANCED | P1 | alternatives, constraints, cost/service tradeoffs | option comparison | Optional | Low | `define-logistics-requirements` |
| `evaluate-3pl-requirements` | ADVANCED | P1 | outsource scope, volumes, service levels, systems | 3PL requirement brief | Optional | Medium | `define-logistics-requirements` |
| `manage-3pl-performance` | ADVANCED | P1 | SLA, KPI, invoice, issue and service data | 3PL performance review | Optional | Medium | `evaluate-3pl-requirements` |
| `analyze-logistics-risk` | ADVANCED | P1 | lanes, nodes, inventory, suppliers, incidents | risk register and mitigations | Optional | Medium | `map-logistics-flow` |
| `plan-logistics-network` | DEFER | P3 | demand regions, nodes, cost, service policy | network planning brief | Required | Medium | `compare-logistics-strategies` |

## Receiving and Inbound Operations

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `plan-inbound-receiving` | CORE | P0 | inbound schedule, load profile, dock capacity | receiving plan | Optional | Medium | `define-logistics-requirements` |
| `schedule-dock-appointments` | CORE | P0 | inbound loads, dock doors, labor windows | dock appointment schedule | Basic | Medium | `plan-inbound-receiving` |
| `verify-inbound-shipment` | CORE | P0 | PO, ASN, BOL, packing list, physical receipt | receiving verification | None | Medium | `plan-inbound-receiving` |
| `reconcile-asn` | CORE | P0 | ASN, PO, receipt count, shipment identifiers | ASN reconciliation | Basic | Low | `verify-inbound-shipment` |
| `inspect-received-goods` | CORE | P0 | receipt condition, photos, damage notes, specs | inspection result | None | Medium | `verify-inbound-shipment` |
| `process-receiving-discrepancy` | CORE | P0 | expected vs received quantity, documents, condition | discrepancy record and next actions | Basic | Medium | `reconcile-asn` |
| `manage-receiving-exceptions` | CORE | P0 | exception type, evidence, owner, service impact | exception workflow | None | Medium | `process-receiving-discrepancy` |
| `manage-quarantine-inventory` | CORE | P1 | hold reason, item status, location, release criteria | quarantine control plan | None | High | `inspect-received-goods` |
| `plan-putaway` | CORE | P0 | received goods, storage rules, locations | putaway plan | Optional | Medium | `verify-inbound-shipment` |
| `select-putaway-location` | ADVANCED | P1 | item attributes, location availability, rules | location recommendation | Optional | Medium | `plan-putaway` |
| `analyze-dock-to-stock-time` | ADVANCED | P1 | timestamps, process steps, queues, exceptions | dock-to-stock analysis | Required | Low | `plan-putaway` |
| `diagnose-receiving-bottleneck` | ADVANCED | P1 | inbound volume, labor, doors, timestamps, errors | bottleneck diagnosis | Optional | Medium | `analyze-dock-to-stock-time` |
| `plan-cross-dock-operation` | ADVANCED | P1 | inbound loads, outbound demand, timing, staging | cross-dock plan | Optional | Medium | `map-logistics-flow` |

## Storage and Warehousing

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `classify-storage-requirements` | CORE | P0 | SKU dimensions, weight, environment, handling rules | storage requirement class | Optional | Medium | `analyze-product-flow` |
| `select-storage-system` | CORE | P0 | SKU/load profile, velocity, building constraints | storage system recommendation | Optional | Medium | `classify-storage-requirements` |
| `calculate-storage-capacity` | CORE | P0 | location dimensions, storage method, constraints | capacity result | Required | Medium | `select-storage-system` |
| `calculate-pallet-positions` | CORE | P0 | rack/floor dimensions, pallet sizes, clearances | pallet position count | Required | Medium | `calculate-storage-capacity` |
| `calculate-cube-utilization` | CORE | P0 | usable cube, occupied cube, SKU cube | cube utilization | Required | Medium | `calculate-storage-capacity` |
| `analyze-storage-utilization` | CORE | P0 | location capacity, inventory, occupancy | utilization assessment | Required | Medium | `calculate-storage-capacity` |
| `plan-reserve-storage` | CORE | P1 | inventory profile, movement rules, replenishment need | reserve storage plan | Optional | Medium | `classify-storage-requirements` |
| `plan-forward-pick-storage` | CORE | P1 | order profile, SKU velocity, replenishment frequency | forward-pick plan | Optional | Medium | `analyze-order-profile` |
| `slot-warehouse-inventory` | ADVANCED | P1 | SKU velocity, cube, weight, affinity, locations | slotting recommendation | Optional | Medium | `plan-forward-pick-storage` |
| `analyze-slotting-efficiency` | ADVANCED | P1 | pick activity, travel, replenishment, locations | slotting efficiency analysis | Required | Medium | `slot-warehouse-inventory` |
| `optimize-storage-density` | ADVANCED | P2 | utilization, handling limits, growth, SKU mix | density improvement options | Required | Medium | `analyze-storage-utilization` |
| `evaluate-racking-strategy` | ADVANCED | P2 | load profile, selectivity, building, MHE | racking strategy analysis | Optional | High | `select-storage-system` |
| `analyze-product-affinity` | ADVANCED | P1 | co-order data, SKU groups, slot locations | affinity analysis | Required | Low | `analyze-order-profile` |

## Inventory Control

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `classify-inventory` | CORE | P0 | SKU, demand, value, criticality, control attributes | inventory classification | Optional | Low | `validate-item-master-data` |
| `calculate-inventory-accuracy` | CORE | P0 | system quantity, counted quantity, sample scope | accuracy result | Required | Low | `classify-inventory` |
| `calculate-inventory-turns` | CORE | P1 | COGS or usage, average inventory | turns calculation | Required | Low | `classify-inventory` |
| `calculate-days-on-hand` | CORE | P1 | inventory quantity/value, average demand | days-on-hand calculation | Required | Low | `classify-inventory` |
| `calculate-reorder-point` | CORE | P0 | demand, lead time, safety stock policy | reorder point | Required | Low | `calculate-logistics-lead-time` |
| `calculate-safety-stock` | ADVANCED | P1 | demand variability, lead-time variability, service target | safety stock calculation | Required | Low | `calculate-reorder-point` |
| `calculate-eoq` | ADVANCED | P2 | demand, ordering cost, carrying cost | EOQ calculation | Required | Low | `calculate-inventory-turns` |
| `design-min-max-policy` | CORE | P1 | demand, lead time, storage constraints, service target | min/max policy | Required | Low | `calculate-reorder-point` |
| `design-cycle-count-program` | CORE | P0 | SKU classes, risk, count capacity, history | cycle count program | Optional | Low | `classify-inventory` |
| `plan-physical-inventory` | CORE | P1 | facility, inventory, freeze rules, labor | physical inventory plan | Optional | Medium | `design-cycle-count-program` |
| `reconcile-inventory` | CORE | P0 | count, system balance, transactions, adjustments | reconciliation result | Basic | Medium | `calculate-inventory-accuracy` |
| `investigate-inventory-discrepancy` | ADVANCED | P1 | transaction history, counts, receipts, picks, adjustments | discrepancy investigation | Optional | Medium | `reconcile-inventory` |
| `analyze-inventory-aging` | CORE | P1 | receipt dates, movement history, on-hand inventory | aging analysis | Required | Low | `classify-inventory` |
| `identify-dead-stock` | CORE | P1 | demand history, inventory age, policy | dead-stock list | Required | Low | `analyze-inventory-aging` |
| `analyze-stockout` | ADVANCED | P1 | demand, inventory, lead time, allocation, orders | stockout cause analysis | Optional | Medium | `calculate-reorder-point` |
| `manage-lot-controlled-inventory` | CORE | P1 | lot IDs, quantities, dates, status, traceability needs | lot-control workflow | None | High | `classify-inventory` |
| `manage-serialized-inventory` | CORE | P1 | serial IDs, custody, status, transaction history | serialized inventory workflow | None | Medium | `classify-inventory` |
| `manage-expiration-controlled-inventory` | CORE | P1 | expiration dates, lot/SKU status, rotation rules | expiration-control workflow | Optional | High | `classify-inventory` |
| `select-inventory-rotation-policy` | CORE | P1 | SKU attributes, age, expiry, lot, demand | rotation policy | None | High | `classify-inventory` |
| `analyze-inventory-shrinkage` | ADVANCED | P1 | count losses, adjustments, transactions, locations | shrinkage analysis | Required | Medium | `investigate-inventory-discrepancy` |

## Replenishment and Picking

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `plan-replenishment` | CORE | P0 | forward-pick inventory, demand, reserve stock | replenishment plan | Optional | Medium | `plan-forward-pick-storage` |
| `calculate-replenishment-demand` | ADVANCED | P1 | order forecast, pick-face capacity, service window | replenishment demand | Required | Low | `plan-replenishment` |
| `prioritize-replenishment` | CORE | P0 | demand, stock status, labor, service deadlines | priority queue | Optional | Medium | `plan-replenishment` |
| `select-picking-strategy` | CORE | P0 | order profile, SKU velocity, facility layout | picking strategy | Optional | Medium | `analyze-order-profile` |
| `plan-picking-wave` | ADVANCED | P1 | orders, cutoffs, labor, equipment, zones | wave plan | Optional | Medium | `select-picking-strategy` |
| `plan-batch-picking` | ADVANCED | P1 | order lines, common SKUs, containers, sort method | batch plan | Optional | Medium | `select-picking-strategy` |
| `plan-zone-picking` | ADVANCED | P1 | zones, orders, labor, handoff rules | zone picking plan | Optional | Medium | `select-picking-strategy` |
| `optimize-pick-path` | ADVANCED | P2 | pick list, locations, constraints, equipment | path recommendation | Required | Medium | `slot-warehouse-inventory` |
| `calculate-pick-productivity` | CORE | P0 | picks, lines, units, hours, method | productivity calculation | Required | Low | `select-picking-strategy` |
| `analyze-pick-accuracy` | CORE | P1 | picks, errors, audits, order lines | accuracy analysis | Required | Medium | `calculate-pick-productivity` |
| `diagnose-picking-bottleneck` | ADVANCED | P1 | productivity, travel, replenishment, congestion, errors | bottleneck diagnosis | Optional | Medium | `calculate-pick-productivity` |
| `investigate-picking-error` | ADVANCED | P1 | pick record, SKU, location, scanner events, order | error investigation | Optional | Medium | `analyze-pick-accuracy` |

## Packing, Staging and Shipping

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `plan-packing-operation` | CORE | P0 | order profile, product attributes, stations, labor | packing plan | Optional | Medium | `select-picking-strategy` |
| `select-shipping-packaging` | CORE | P0 | product size, fragility, carrier, handling | packaging recommendation | Optional | Medium | `plan-packing-operation` |
| `plan-cartonization` | ADVANCED | P1 | item dimensions, weights, order mix, carton set | cartonization plan | Required | Medium | `select-shipping-packaging` |
| `verify-order-before-shipping` | CORE | P0 | order, picked items, pack contents, labels | order verification | None | Medium | `plan-packing-operation` |
| `plan-shipping-stage` | CORE | P0 | orders, carrier, route, cutoff, dock capacity | staging plan | Optional | Medium | `verify-order-before-shipping` |
| `manage-carrier-cutoffs` | CORE | P0 | carrier schedules, order priority, processing status | cutoff action plan | Basic | Low | `plan-shipping-stage` |
| `plan-trailer-loading` | ADVANCED | P1 | shipments, pallets, weights, stops, constraints | loading plan | Required | High | `plan-shipping-stage` |
| `verify-outbound-shipment` | CORE | P0 | shipment, BOL, labels, staged goods, carrier | outbound verification | None | Medium | `plan-shipping-stage` |
| `manage-shipping-exception` | CORE | P1 | exception type, order, carrier, service impact | exception workflow | None | Medium | `verify-outbound-shipment` |
| `investigate-shipping-error` | ADVANCED | P1 | order, shipment, scan, carrier, customer evidence | shipping error analysis | Optional | Medium | `manage-shipping-exception` |
| `calculate-order-cycle-time` | CORE | P1 | order timestamps, release, pick, pack, ship events | cycle-time calculation | Required | Low | `analyze-order-profile` |
| `analyze-order-accuracy` | CORE | P1 | order audits, errors, returns, claims | order-accuracy analysis | Required | Medium | `verify-order-before-shipping` |

## Material Handling

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `classify-material-handling-requirements` | CORE | P0 | load, dimensions, weight, distance, throughput | handling requirement class | Optional | High | `analyze-product-flow` |
| `select-material-handling-equipment` | CORE | P1 | handling requirements, facility, labor, safety constraints | equipment class comparison | Optional | High | `classify-material-handling-requirements` |
| `calculate-equipment-requirements` | ADVANCED | P1 | volumes, travel, cycle time, uptime, shifts | equipment requirement estimate | Required | High | `select-material-handling-equipment` |
| `analyze-equipment-utilization` | ADVANCED | P1 | equipment hours, moves, downtime, capacity | utilization analysis | Required | High | `calculate-equipment-requirements` |
| `plan-material-flow` | ADVANCED | P1 | facility flow, product profile, equipment, constraints | material-flow plan | Optional | High | `classify-material-handling-requirements` |
| `evaluate-conveyor-application` | ADVANCED | P2 | throughput, product profile, layout, labor | conveyor applicability review | Optional | High | `plan-material-flow` |
| `evaluate-agv-amr-application` | ADVANCED | P2 | flow, payloads, routes, systems, safety constraints | AGV/AMR applicability review | Optional | High | `plan-material-flow` |
| `evaluate-asrs-application` | ADVANCED | P2 | SKU profile, cube, throughput, building, capex | AS/RS applicability review | Optional | High | `select-storage-system` |

## Transportation and Freight

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `select-transportation-mode` | CORE | P1 | shipment profile, service need, geography, constraints | mode recommendation | Optional | Medium | `define-logistics-requirements` |
| `plan-freight-shipment` | CORE | P1 | origin, destination, goods, service, timing | freight shipment plan | Optional | Medium | `select-transportation-mode` |
| `select-carrier` | CORE | P1 | carriers, rates, service, performance, constraints | carrier recommendation | Optional | Medium | `plan-freight-shipment` |
| `compare-freight-rates` | CORE | P1 | rate quotes, lanes, weights, accessorials | rate comparison | Required | Low | `plan-freight-shipment` |
| `calculate-freight-cost` | CORE | P1 | rate basis, shipment weight/cube, accessorials | freight cost calculation | Required | Low | `compare-freight-rates` |
| `calculate-load-utilization` | CORE | P1 | trailer/container dimensions, load dimensions, weight | utilization calculation | Required | High | `plan-freight-shipment` |
| `plan-freight-consolidation` | ADVANCED | P2 | shipments, lanes, timing, cost, service | consolidation plan | Required | Medium | `calculate-freight-cost` |
| `plan-multi-stop-shipment` | ADVANCED | P2 | stops, sequence constraints, service windows, load | multi-stop plan | Optional | Medium | `plan-freight-shipment` |
| `analyze-carrier-performance` | CORE | P1 | on-time, claims, cost, tender acceptance, service | carrier scorecard | Required | Low | `select-carrier` |
| `audit-freight-charge` | ADVANCED | P1 | invoice, rate agreement, shipment facts, accessorials | freight audit result | Required | Low | `calculate-freight-cost` |
| `analyze-freight-accessorials` | ADVANCED | P1 | invoice, carrier rules, shipment events | accessorial analysis | Required | Low | `audit-freight-charge` |
| `manage-freight-claim` | CORE | P1 | damage/loss evidence, shipment docs, carrier process | claim preparation checklist | Optional | Medium | `verify-outbound-shipment` |
| `analyze-detention` | ADVANCED | P2 | appointment, arrival/departure, free time, charge rules | detention analysis | Required | Medium | `audit-freight-charge` |
| `analyze-demurrage` | ADVANCED | P2 | container/rail/port events, free time, tariff rules | demurrage analysis | Required | Medium | `audit-freight-charge` |
| `interpret-bill-of-lading` | CORE | P1 | BOL fields, shipment context, parties | BOL interpretation | None | Medium | `plan-freight-shipment` |
| `analyze-transportation-kpis` | ADVANCED | P1 | shipment metrics, cost, service, carrier data | transportation KPI analysis | Required | Low | `analyze-carrier-performance` |
| `plan-yard-operations` | DEFER | P2 | trailer/container inventory, appointments, dock plan | yard operating plan | Optional | Medium | `schedule-dock-appointments` |
| `plan-customs-broker-handoff` | SPECIALIST | P3 | import/export facts, documents, parties, jurisdiction | broker handoff checklist | None | High | `plan-freight-shipment` |
| `classify-dangerous-goods-logistics-requirements` | SPECIALIST | P3 | product hazard data, mode, jurisdiction, packaging | DG requirement research brief | None | High | `plan-freight-shipment` |

## Warehouse Design and Capacity

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `calculate-warehouse-capacity` | CORE | P0 | building dimensions, usable space, storage methods | warehouse capacity result | Required | High | `calculate-storage-capacity` |
| `forecast-capacity-requirements` | ADVANCED | P1 | growth forecast, inventory, throughput, service targets | capacity forecast | Required | Medium | `calculate-warehouse-capacity` |
| `analyze-space-utilization` | CORE | P0 | facility areas, storage, aisles, support spaces | space utilization analysis | Required | Medium | `calculate-warehouse-capacity` |
| `plan-warehouse-zones` | ADVANCED | P1 | process needs, SKU groups, MHE, travel paths | zoning concept | Optional | Medium | `analyze-space-utilization` |
| `plan-dock-capacity` | ADVANCED | P1 | inbound/outbound volume, dwell, doors, schedules | dock capacity plan | Required | High | `schedule-dock-appointments` |
| `analyze-warehouse-flow` | ADVANCED | P1 | layout, product movement, process paths, congestion | flow analysis | Optional | Medium | `map-logistics-flow` |
| `identify-warehouse-congestion` | ADVANCED | P1 | layout, volumes, labor/equipment paths, delays | congestion diagnosis | Optional | High | `analyze-warehouse-flow` |
| `design-conceptual-warehouse-layout` | ADVANCED | P2 | building, zones, storage, process requirements | conceptual layout | Optional | High | `plan-warehouse-zones` |
| `compare-warehouse-layouts` | ADVANCED | P2 | layout alternatives, assumptions, KPIs | layout comparison | Optional | High | `design-conceptual-warehouse-layout` |
| `plan-warehouse-expansion` | ADVANCED | P2 | capacity forecast, constraints, growth options | expansion planning brief | Required | Medium | `forecast-capacity-requirements` |

## Logistics Systems and Data

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `map-wms-process` | CORE | P0 | process, WMS transactions, users, status changes | WMS process map | None | Low | `map-logistics-flow` |
| `analyze-wms-transaction-history` | ADVANCED | P1 | transaction logs, timestamps, users, locations | transaction analysis | Optional | Medium | `map-wms-process` |
| `diagnose-wms-inventory-issue` | ADVANCED | P1 | WMS balances, transactions, physical evidence | WMS issue diagnosis | Optional | Medium | `analyze-wms-transaction-history` |
| `validate-item-master-data` | CORE | P0 | item master fields, dimensions, units, statuses | item data validation | Optional | Low | None |
| `validate-location-master-data` | CORE | P0 | location master, capacities, zones, statuses | location data validation | Optional | Medium | None |
| `analyze-logistics-scan-events` | ADVANCED | P1 | scan logs, timestamps, devices, process steps | scan event analysis | Optional | Medium | `map-wms-process` |
| `design-logistics-barcode-flow` | ADVANCED | P1 | process steps, IDs, labels, scanners, systems | barcode flow design | None | Medium | `map-wms-process` |
| `interpret-gs1-identifiers` | CORE | P1 | barcode strings, GS1 keys, item/logistics context | identifier interpretation | Optional | Medium | `validate-item-master-data` |
| `design-logistics-unit-identification` | ADVANCED | P1 | logistics unit needs, labels, ASN/EDI flow | unit ID design brief | None | Medium | `interpret-gs1-identifiers` |
| `analyze-edi-logistics-flow` | ADVANCED | P1 | EDI transaction set, parties, process events | EDI flow analysis | None | Low | `design-logistics-unit-identification` |
| `map-erp-wms-integration` | ADVANCED | P1 | ERP/WMS processes, master data, transactions | integration map | None | Medium | `map-wms-process` |
| `map-wms-tms-integration` | ADVANCED | P1 | WMS/TMS processes, shipment events, labels | integration map | None | Medium | `map-wms-process` |
| `analyze-logistics-data-quality` | ADVANCED | P1 | master data, transactions, exceptions, controls | data quality assessment | Optional | Medium | `validate-item-master-data` |
| `analyze-order-management-flow` | ADVANCED | P1 | OMS/order statuses, releases, exceptions, handoffs | order management flow map | None | Low | `analyze-order-profile` |

## Performance and Continuous Improvement

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `select-logistics-kpis` | CORE | P0 | operation type, goals, constraints, available data | KPI set | None | Low | `define-logistics-requirements` |
| `build-logistics-scorecard` | CORE | P1 | KPI set, targets, data owners, cadence | scorecard design | Optional | Low | `select-logistics-kpis` |
| `analyze-warehouse-kpis` | ADVANCED | P1 | warehouse KPI data, targets, trend history | KPI analysis | Required | Low | `build-logistics-scorecard` |
| `analyze-throughput` | CORE | P0 | units/orders/lines, time, capacity, process | throughput analysis | Required | Low | `map-logistics-flow` |
| `diagnose-throughput-loss` | ADVANCED | P1 | throughput, queues, downtime, labor, equipment | loss diagnosis | Optional | Medium | `analyze-throughput` |
| `identify-logistics-bottleneck` | ADVANCED | P1 | process flow, queues, capacity, cycle times | bottleneck finding | Optional | Medium | `analyze-throughput` |
| `perform-logistics-root-cause-analysis` | ADVANCED | P1 | observed issue, evidence, process history | root-cause analysis | None | Medium | `identify-logistics-bottleneck` |
| `perform-logistics-pareto-analysis` | ADVANCED | P1 | issue counts, costs, categories, timeframe | Pareto analysis | Required | Low | `select-logistics-kpis` |
| `map-warehouse-process` | CORE | P0 | warehouse process steps, roles, systems | process map | None | Low | `map-logistics-flow` |
| `analyze-logistics-waste` | ADVANCED | P1 | process map, delays, movement, defects, rework | waste analysis | Optional | Medium | `map-warehouse-process` |
| `compare-logistics-scenarios` | ADVANCED | P2 | alternatives, assumptions, KPI/cost/service data | scenario comparison | Required | Low | `build-logistics-scorecard` |
| `build-logistics-improvement-plan` | ADVANCED | P1 | root cause, constraints, actions, owners, metrics | improvement plan | Optional | Medium | `perform-logistics-root-cause-analysis` |
| `measure-improvement-result` | ADVANCED | P1 | before/after metrics, implementation dates, controls | result measurement | Required | Low | `build-logistics-improvement-plan` |
| `analyze-logistics-sustainability` | DEFER | P3 | emissions, waste, packaging, energy, transport profile | sustainability analysis | Required | Medium | `select-logistics-kpis` |

## Labor and Operational Planning

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `forecast-warehouse-workload` | ADVANCED | P1 | orders, receipts, SKU mix, seasonality, backlog | workload forecast | Required | Low | `analyze-order-profile` |
| `calculate-labor-requirements` | ADVANCED | P1 | workload, productivity, shifts, breaks, service window | labor requirement | Required | Medium | `forecast-warehouse-workload` |
| `plan-warehouse-staffing` | ADVANCED | P1 | labor requirement, skills, shifts, constraints | staffing plan | Optional | Medium | `calculate-labor-requirements` |
| `balance-warehouse-workload` | ADVANCED | P1 | workload by area, labor, equipment, priorities | balancing plan | Optional | Medium | `plan-warehouse-staffing` |
| `analyze-labor-productivity` | CORE | P1 | labor hours, output, process, standards | productivity analysis | Required | Low | `select-logistics-kpis` |
| `analyze-overtime-requirements` | ADVANCED | P1 | workload, staffing, capacity, deadlines | overtime analysis | Required | Medium | `calculate-labor-requirements` |
| `plan-shift-handoff` | CORE | P0 | open work, exceptions, staffing, priorities | shift handoff | None | Medium | `build-daily-warehouse-plan` |
| `build-daily-warehouse-plan` | ADVANCED | P1 | inbound, outbound, inventory work, labor, constraints | daily operating plan | Optional | Medium | `balance-warehouse-workload` |

## Returns and Reverse Logistics

| Skill | Class | Priority | Inputs | Outputs | Calc | Reg/Safety | Prerequisites |
|---|---|---:|---|---|---|---|---|
| `process-customer-return` | CORE | P1 | return request, order, item, condition, policy | return workflow | None | Medium | `verify-outbound-shipment` |
| `classify-return-disposition` | CORE | P1 | item condition, policy, value, safety concerns | disposition classification | Optional | High | `process-customer-return` |
| `inspect-returned-goods` | CORE | P1 | returned item, condition, photos, reason code | inspection result | None | High | `process-customer-return` |
| `reconcile-returned-inventory` | CORE | P1 | return receipt, system balance, disposition | inventory reconciliation | Basic | Medium | `reconcile-inventory` |
| `analyze-return-reason` | CORE | P1 | reason codes, customer notes, product/order data | reason analysis | Required | Medium | `process-customer-return` |
| `analyze-return-rate` | CORE | P1 | returns, shipments/orders, product/channel data | return-rate calculation | Required | Low | `analyze-return-reason` |
| `plan-return-to-stock` | CORE | P1 | disposition, inventory status, quality release criteria | return-to-stock plan | None | High | `classify-return-disposition` |
| `plan-return-to-vendor` | CORE | P1 | vendor policy, item condition, quantities, docs | RTV plan | None | Medium | `classify-return-disposition` |
| `manage-damaged-inventory` | CORE | P1 | damage type, quantity, status, location, cause | damaged-inventory workflow | Optional | High | `inspect-returned-goods` |
| `manage-nonconforming-inventory` | CORE | P1 | nonconformance, hold status, owner, disposition | nonconforming inventory workflow | None | High | `manage-quarantine-inventory` |
| `analyze-reverse-logistics-cost` | ADVANCED | P2 | returns handling, freight, labor, disposition value | reverse cost analysis | Required | Low | `analyze-return-rate` |
| `design-reverse-logistics-flow` | ADVANCED | P2 | return types, channels, facility flow, disposition paths | reverse-flow design | Optional | Medium | `process-customer-return` |

## Universal Core Exclusions

The following are intentionally not accepted as universal core skills:

| Candidate capability | Classification | Reason |
|---|---|---|
| broad supply-chain strategy | REMOVE | Too broad for AgentLogistics and overlaps procurement, manufacturing, demand planning, and finance. |
| procurement sourcing and supplier negotiation | REMOVE | Explicitly outside the universal core except as input context. |
| structural engineering approval | REMOVE | Requires qualified engineering signoff. |
| operator certification | REMOVE | Requires approved training and employer/regulator certification processes. |
| legal compliance determination | REMOVE | AgentLogistics can support research, not issue legal conclusions. |

