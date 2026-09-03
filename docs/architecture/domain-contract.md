# AgentLogistics Domain Contract

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY
```

## Purpose

This document defines the core AgentLogistics domain model. Every core skill
must map to exactly one primary domain family and may declare secondary related
domains when needed.

The contract exists to prevent three failure modes:

- broad textbook-like skill names;
- duplicated skills across adjacent domains;
- accidental mixing of universal logistics methods with jurisdiction-specific
  regulatory rules.

## Core Domain Families

### 1. Logistics Fundamentals

Foundational reasoning about commercial logistics systems, flows, nodes,
constraints, tradeoffs, terminology, service levels, lead times, throughput,
capacity, unit loads, cost-to-serve, and logistics operating models.

Example skill intents:

- analyze a logistics operation;
- map a logistics flow;
- identify logistics constraints;
- distinguish inbound, outbound, forward, and reverse flows.

### 2. Receiving and Inbound

Inbound dock, trailer arrival, unloading, shipment verification, ASN
reconciliation, inspection, receiving discrepancies, quarantine handoff, dock
scheduling, and inbound bottlenecks.

Example skill intents:

- plan inbound receiving;
- verify an inbound shipment;
- reconcile an ASN;
- process a receiving discrepancy.

### 3. Storage and Warehousing

Physical storage methods, location types, reserve and forward storage, rack and
shelving concepts, storage requirements, space utilization, pallet positions,
warehouse lifecycle concepts, and warehousing operations that are not primarily
inventory-policy decisions.

Example skill intents:

- classify storage requirements;
- calculate storage capacity;
- calculate pallet positions;
- analyze storage utilization.

### 4. Inventory Control

Inventory records, accuracy, reconciliation, counts, policies, safety stock,
reorder points, EOQ, turns, days on hand, shrinkage, dead stock, aging, lot
control, serial control, expiration control, rotation policies, and discrepancy
investigation.

Example skill intents:

- calculate reorder point;
- design a cycle-count program;
- reconcile inventory;
- investigate an inventory discrepancy.

### 5. Replenishment and Picking

Forward-pick replenishment, picking method selection, wave, batch, zone, path,
pick productivity, pick accuracy, pick errors, and demand-driven picking
workflow.

Example skill intents:

- plan replenishment;
- select a picking strategy;
- calculate pick productivity;
- diagnose a picking bottleneck.

### 6. Packing, Staging and Shipping

Packing operation design, cartonization, order verification, staging, outbound
shipment verification, loading preparation, trailer loading analysis, shipping
exceptions, and dock-to-carrier handoff.

Example skill intents:

- plan a packing operation;
- plan a shipping stage;
- verify an outbound shipment;
- investigate a shipping error.

### 7. Material Handling

Movement of goods inside and around logistics facilities, including load
characteristics, equipment classes, conveyors, AGV/AMR applicability, AS/RS
applicability, flow, travel distance, throughput, equipment utilization, and
high-level equipment selection analysis.

Example skill intents:

- classify material-handling requirements;
- select material-handling equipment;
- calculate equipment requirements;
- evaluate a conveyor application.

### 8. Transportation and Freight

Shipment planning beyond the warehouse door, mode selection, carrier selection,
freight rates, freight cost, load utilization, consolidation, multi-stop
shipments, carrier performance, freight audit, accessorials, detention,
demurrage, claims, bills of lading, and transportation KPIs.

Example skill intents:

- select a transportation mode;
- calculate freight cost;
- analyze carrier performance;
- audit a freight charge.

### 9. Warehouse Design and Capacity

Conceptual facility planning, layout reasoning, dock and staging capacity,
storage system fit, cube utilization, slotting, SKU velocity, product affinity,
travel distance, congestion, zoning, expansion capacity, and flow design.

Example skill intents:

- calculate warehouse capacity;
- analyze layout constraints;
- recommend a slotting approach;
- compare conceptual warehouse scenarios.

### 10. Logistics Systems and Data

Operational systems and data flows including WMS, TMS, ERP, OMS, YMS, LMS,
WCS, WES, EDI, APIs, item masters, location masters, transaction history,
scan events, data quality, barcodes, GS1 identifiers, logistics unit
identification, and system integration maps.

Example skill intents:

- map a WMS process;
- diagnose a WMS inventory issue;
- validate item master data;
- interpret GS1 identifiers.

### 11. Performance and Continuous Improvement

Metrics, scorecards, throughput analysis, bottleneck diagnosis, root-cause
analysis, Pareto analysis, process mapping, waste analysis, scenario comparison,
improvement planning, and measurement of operational changes.

Example skill intents:

- select logistics KPIs;
- build a logistics scorecard;
- identify a logistics bottleneck;
- build a logistics improvement plan.

### 12. Labor and Operational Planning

Workload forecasting, labor requirements, staffing plans, workload balancing,
labor productivity, overtime analysis, shift handoffs, and daily warehouse
operating plans.

Example skill intents:

- forecast warehouse workload;
- calculate labor requirements;
- plan warehouse staffing;
- build a daily warehouse plan.

### 13. Returns and Reverse Logistics

Customer returns, return disposition, returned-goods inspection, returned
inventory reconciliation, return reasons, return rates, return-to-stock,
return-to-vendor, damaged inventory, nonconforming inventory, reverse logistics
cost, and reverse flow design.

Example skill intents:

- process a customer return;
- classify return disposition;
- reconcile returned inventory;
- design a reverse logistics flow.

## Mapping Rule

Each new core skill proposal must state:

- primary domain family;
- secondary related domains, if any;
- problem being solved;
- expected trigger;
- non-trigger boundary;
- required evidence or inputs;
- expected output;
- calculation requirement, if any;
- regulatory dependency, if any;
- safety sensitivity, if any.

If a proposed skill cannot map cleanly to one primary family, it should be
split, merged into an existing skill, moved to a specialization, or rejected as
out-of-scope.

## Skillset Rule

Professional roles are compositions, not atomic skills. A role such as
`warehouse-manager` or `inventory-control-specialist` belongs under
`skillsets/` and should route to multiple atomic skills.

## Regulatory Rule

Regulatory content is not part of a universal domain unless the source is truly
jurisdiction-neutral. Most safety, transportation, customs, dangerous-goods,
employment, and facility requirements belong in a jurisdiction or industry
specialization.
