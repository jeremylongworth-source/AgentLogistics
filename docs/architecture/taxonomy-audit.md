# AL-02 Taxonomy Audit

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY
```

## Scope

This audit evaluates the candidate AgentLogistics skill taxonomy for:

- atomicity;
- duplicate intent;
- overlapping responsibility;
- naming consistency;
- domain assignment;
- prerequisite relationships;
- expected inputs;
- expected outputs;
- quantitative requirements;
- regulatory dependency;
- safety sensitivity.

The row-level audit is recorded in `master-taxonomy-v1.md`. This file records
the reasoning, source scan, gaps, and boundary decisions behind that table.

## In Scope

- Convert the original 160 candidate skills into an auditable v1 taxonomy.
- Add source-backed gap candidates where major logistics capabilities were
  missing or underrepresented.
- Resolve duplicate and overlap concerns before implementation.
- Define which capabilities belong in universal core, advanced core,
  specialization, or deferred work.

## Out of Scope

- Authoring actual `skills/*/SKILL.md` files.
- Creating skillsets.
- Writing regulatory guidance.
- Building calculation formulas.
- Building test fixtures beyond taxonomy validation.

## Source Scan

AL-02 used a limited source scan to check breadth, not to write detailed domain
rules.

| Source | Used For | Taxonomy Effect |
|---|---|---|
| CSCMP, `SCM Definitions and Glossary of Terms`, https://cscmp.org/CSCMP/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx | Confirms logistics includes forward and reverse flow plus storage, and sits inside broader supply-chain management. | Keep logistics narrower than supply-chain management and include reverse logistics in core. |
| ASCM South Central Texas Chapter, `CLTD`, https://sctx.ascm.org/CLTD | Lists CLTD modules: logistics overview and strategy, network design, sustainability and reverse logistics, capacity and demand, order, inventory, warehouse, transportation, and global logistics. | Add explicit gap tracking for order-management flow, logistics network planning, sustainability, and risk. |
| GS1 US, `Serialized Shipping Container Codes`, https://www.gs1us.org/upcs-barcodes-prefixes/serialized-shipping-container-codes | Confirms SSCC as an 18-digit logistics-unit identifier used with GS1-128/logistics labels and ASN/EDI workflows. | Keep `interpret-gs1-identifiers` and `design-logistics-unit-identification` in systems/data. |
| OSHA, `Warehousing - Overview`, https://www.osha.gov/warehousing | Identifies warehousing hazards including powered industrial trucks, ergonomics, material handling, hazardous chemicals, slips/trips/falls, and robotics. | Keep safety sensitivity flags on material handling, storage, dock, and automation skills. Do not make safety certification claims. |
| CCOHS, `Warehouse Workers Safety Guide`, https://www.ccohs.ca/products/publications/warehouse_toc.html | Shows Canadian warehouse safety topics across manual handling, shipping/packing, materials handling equipment, powered vehicles, material storage, environment, OH&S, WHMIS, fire code, building code, and TDG. | Supports AL-16 specialization and confirms universal core must isolate Canadian regulatory requirements. |
| Transport Canada, `Transportation of dangerous goods in Canada`, https://tc.canada.ca/en/dangerous-goods/transportation-dangerous-goods-canada | Identifies TDG as a Transport Canada safety/regulatory program across modes with ERAP/CANUTEC and legal/regulatory basis. | Keep dangerous-goods requirements as specialist, not universal core. |
| eCFR, `49 CFR Part 393 Subpart I`, https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-393/subpart-I | Shows US cargo securement requirements are mode and jurisdiction specific. | Keep cargo securement and transportation compliance in US specialization unless a universal operational planning boundary is clear. |
| CBSA, `Importing commercial goods into Canada`, https://www.cbsa-asfc.gc.ca/import/guide-eng.html | Confirms commercial importing is a source-backed customs process with importer/broker documentation implications. | Add `plan-customs-broker-handoff` as a specialist candidate for AL-22/Canada work, not universal core advice. |
| IATA, `Dangerous Goods Regulations`, https://www.iata.org/en/publications/dgr/ | Confirms dangerous-goods air transport requires classifying, marking, packing, labelling, and documenting shipments under DGR. | Reinforces `classify-dangerous-goods-logistics-requirements` as specialist and high-safety. |
| APQC benchmark/process pages, including https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/dock-stock-cycle-time-hours-supplier and https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/pick-ship-cycle-time-hours-customer | Shows common logistics metrics around dock-to-stock, pick-to-ship, freight cost, and returns process efficiency. | Supports KPI, cycle-time, freight-audit, and reverse-logistics metric skills. |

## Source-Backed Gap Decisions

| Gap | Decision | Rationale |
|---|---|---|
| Customer/order management flow | Add `analyze-order-management-flow` as `ADVANCED` under systems/data. | Order management is a recognized logistics/distribution topic and connects OMS, WMS, fulfillment release, exceptions, and shipping handoffs. |
| Cross-dock operations | Add `plan-cross-dock-operation` as `ADVANCED` under receiving/inbound. | Cross-docking was in the planning discussion but missing from the 160-row candidate list. It is operationally distinct from normal receiving and shipping. |
| 3PL performance | Add `manage-3pl-performance` as `ADVANCED` under logistics fundamentals. | `evaluate-3pl-requirements` covers selection needs, but not ongoing SLA/KPI/vendor performance control. |
| Logistics risk | Add `analyze-logistics-risk` as `ADVANCED`. | Risk appears in professional logistics coverage and crosses transportation, warehousing, systems, inventory, and service continuity. |
| Logistics sustainability | Add `analyze-logistics-sustainability` as `DEFER`. | Sustainability is real logistics scope, but requires source, metrics, and likely carbon-accounting boundaries beyond early v1. |
| Yard operations | Add `plan-yard-operations` as `DEFER`. | YMS and yard execution are meaningful in larger distribution operations, but should wait until dock, transportation, and facility flow foundations exist. |
| Logistics network design | Add `plan-logistics-network` as `DEFER`. | Network design is recognized in CLTD-style logistics coverage, but the current repo should not expand into broad supply-chain network strategy before warehouse, inventory, and transportation foundations are stable. |
| Customs broker handoff | Add `plan-customs-broker-handoff` as `SPECIALIST`. | Customs documentation is jurisdiction and lane sensitive; AgentLogistics can prepare handoff material but should not provide legal brokerage advice. |
| Dangerous-goods logistics requirements | Add `classify-dangerous-goods-logistics-requirements` as `SPECIALIST`. | DG work is high-safety and regulation-sensitive across mode and jurisdiction. It belongs in AL-21 or jurisdiction modules. |

## Duplicate and Overlap Resolution

| Potential overlap | Resolution |
|---|---|
| `calculate-storage-capacity` vs `calculate-warehouse-capacity` | Storage capacity calculates capacity for storage systems or areas. Warehouse capacity includes facility-wide receiving, storage, staging, docks, support areas, flow, and expansion limits. |
| `analyze-storage-utilization` vs `analyze-space-utilization` | Storage utilization covers storage locations and inventory occupancy. Space utilization covers the whole facility footprint and operational area allocation. |
| `calculate-cube-utilization` vs `calculate-load-utilization` | Cube utilization is storage or carton/container cube. Load utilization is transportation asset utilization by cube/weight and loading constraints. |
| `verify-order-before-shipping` vs `verify-outbound-shipment` | Order verification checks packed order contents and labels. Outbound shipment verification checks staged shipment, BOL/manifest, carrier, route, and dock handoff. |
| `process-receiving-discrepancy` vs `manage-receiving-exceptions` | Discrepancy covers expected-vs-received facts. Exceptions cover operational workflow, ownership, holds, communication, and resolution tracking. |
| `select-storage-system` vs `evaluate-racking-strategy` | Storage-system selection chooses broad methods. Racking strategy evaluates pallet-rack configuration tradeoffs and safety-sensitive limits. |
| `plan-putaway` vs `select-putaway-location` | Putaway planning defines rules, sequence, and work. Location selection recommends a specific location based on item/location constraints. |
| `analyze-throughput` vs `diagnose-throughput-loss` | Throughput analysis measures flow. Throughput-loss diagnosis explains why measured throughput is below need or historical norm. |
| `identify-logistics-bottleneck` vs domain bottleneck skills | The general skill finds the constraint across a flow. Receiving and picking bottleneck skills use domain-specific evidence and procedures. |
| `manage-damaged-inventory` vs `manage-nonconforming-inventory` | Damaged inventory is condition-based. Nonconforming inventory is requirement/specification based and may include undamaged goods on hold. |
| `analyze-order-profile` vs `analyze-order-management-flow` | Order profile summarizes order mix. Order-management flow maps release/status/exception handoffs across OMS, WMS, packing, and shipping. |

## Atomicity Result

Accepted skill names follow an action-object pattern such as:

```text
calculate-reorder-point
investigate-inventory-discrepancy
select-picking-strategy
analyze-carrier-performance
```

The following broad role or textbook-style names remain rejected:

```text
manage-warehouse
do-logistics
inventory-management
transportation-management
```

Professional identities such as `warehouse-manager` or
`inventory-control-specialist` remain skillsets, not skills.

## Naming Consistency

Accepted names use lowercase letters, numbers where needed, and hyphens. The
verbs intentionally signal output type:

- `analyze-*`: interpret evidence and explain implications.
- `calculate-*`: produce explicit math with units and assumptions.
- `plan-*`: produce sequenced operational actions.
- `select-*`: compare options and recommend a choice.
- `verify-*`: check evidence against expected records.
- `reconcile-*`: resolve or explain differences between records and physical
  evidence.
- `investigate-*`: trace evidence before assigning likely cause.
- `design-*`: create a conceptual policy, model, or flow, not engineering
  certification.
- `manage-*`: coordinate an exception workflow or controlled process, not
  perform legal or supervisory authority.

## Regulatory and Safety Isolation

Universal core skills may identify that regulatory review is required. They
must not embed jurisdiction-specific compliance conclusions.

The highest-risk areas are:

- powered industrial trucks and material-handling equipment;
- racking and storage systems;
- trailer loading and cargo securement;
- dangerous goods;
- food, pharmaceutical, cold-chain, and expiration-sensitive goods;
- customs and international shipping;
- workplace safety, fire code, building code, and labor rules.

These should trigger source-backed specialization work before detailed guidance
is authored.

## Quantitative Coverage

The taxonomy preserves calculations as first-class skills or explicit
calculation requirements, including:

- lead time;
- storage capacity;
- pallet positions;
- cube utilization;
- inventory accuracy;
- inventory turns;
- days on hand;
- reorder point;
- safety stock;
- EOQ;
- replenishment demand;
- pick productivity;
- cartonization;
- order cycle time;
- order accuracy;
- equipment requirements;
- equipment utilization;
- freight rates and costs;
- load utilization;
- detention and demurrage;
- warehouse capacity;
- space utilization;
- dock capacity;
- KPI analysis;
- throughput;
- Pareto analysis;
- labor requirements;
- return rate;
- reverse logistics cost.

AL-03 must turn this into a calculation standard before any formula-heavy skills
are authored.

## Gate Result

AL-02 is `READY`.

The v1 taxonomy has no unresolved duplicate or obviously non-atomic core skills.
Known broad, regulated, or specialist capabilities are either explicitly
excluded, deferred, or isolated from the universal core.

