# AgentLogistics Specialization Roadmap

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY
```

## Purpose

This document defines the AL-19 extension architecture for specialized
logistics domains. It evaluates candidate specializations without prematurely
building every package.

Specializations may depend on universal core skills and professional skillsets.
Universal core skills must not depend on specializations.

## Extension Rules

1. Create a specialization only when the domain has unique knowledge, unique
   regulations, unique workflows, or evidence requirements that do not belong
   in the universal core.
2. Keep jurisdiction-specific rules, industry-specific regulations, and
   product-sensitive controls inside the specialization.
3. Reuse existing core skills and skillsets whenever they cover the universal
   logistics method.
4. Add new atomic skills only when a repeatable specialized task cannot be
   expressed as composition of existing skills.
5. Treat each regulatory or safety-sensitive specialization as research and
   planning support until qualified review is complete.
6. Require source maps, scenarios, fixtures, evaluation reports, and validation
   checks before marking a specialization ready.

## Candidate Evaluation

| Candidate | Domain need | Unique knowledge | Unique regulations | Unique workflows | Shared core skills | New atomic skills required | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cold-chain | Temperature-sensitive storage and transportation for products that lose value, safety, or compliance when exposed to uncontrolled conditions. | Temperature ranges, temperature monitoring, excursions, thermal packaging, lane qualification, cold-room handoffs. | Food, drug, health, carrier, workplace, and jurisdiction-specific temperature-control rules may apply. | Temperature-controlled receiving, storage, picking, packing, staging, loading, transport handoffs, excursion triage. | Receiving, storage, inventory control, transportation, systems data, performance, reverse logistics. | `classify-temperature-controlled-requirements`, `plan-temperature-controlled-storage`, `analyze-temperature-excursion`, `plan-cold-chain-handoff`. | P0 |
| food-logistics | Food storage, movement, traceability, segregation, expiry, sanitation-sensitive handling, and recall support. | Lot traceability, allergen or product segregation, FEFO, sanitation status, hold/release boundaries, recall logistics. | Food safety, sanitation, recall, labeling, transportation, and jurisdiction-specific rules may apply. | Food receiving checks, FEFO rotation, sanitation-sensitive storage, recall trace, food hold/release handoffs. | Receiving, storage, inventory control, replenishment, shipping, transportation, systems data, reverse logistics. | `classify-food-logistics-requirements`, `plan-fefo-rotation`, `manage-food-logistics-hold`, `support-food-recall-logistics`. | P0 |
| dangerous-goods | Hazardous material movement, storage, documentation, segregation, incident readiness, and mode-specific handoffs. | Hazard class, packing group, compatibility, placarding, labels, SDS, emergency response, carrier acceptance. | Dangerous-goods and hazardous-materials rules are mode-specific and jurisdiction-specific. | Classification handoff, document research, segregation planning, carrier acceptance checks, incident escalation. | Transportation, storage, material handling, systems data, compliance specializations. | `classify-dangerous-goods-logistics-requirements`, `plan-dangerous-goods-segregation`, `prepare-dangerous-goods-shipping-research`, `triage-dangerous-goods-incident-logistics`. | P1 |
| ecommerce | High-order-volume direct-to-consumer fulfillment with returns, parcel carrier constraints, customer service levels, and high SKU churn. | Order profiles, parcel rating inputs, packaging, carrier cutoffs, return reasons, marketplace or storefront order statuses. | Consumer, marketplace, carrier, privacy, product category, and jurisdiction-specific rules may apply. | Wave/batch/zone picking for eaches, packing, cartonization, parcel staging, shipping exceptions, returns triage. | Fulfillment optimization, warehouse operator, inventory control, transportation, reverse logistics, systems data. | `analyze-ecommerce-order-profile`, `plan-parcel-fulfillment-cutoffs`, `triage-ecommerce-return-flow`, `analyze-marketplace-fulfillment-exception`. | P1 |
| manufacturing | Line-side logistics, WIP movement, finished-goods staging, materials supermarkets, replenishment to production, and manufacturing interfaces. | WIP states, production schedule linkage, line-side presentation, kanban, milk runs, changeovers, materials availability. | Workplace safety, product category, quality, traceability, and industry-specific manufacturing rules may apply. | Line-side replenishment, production staging, WIP transfer, finished-goods handoff, material shortage escalation. | Inventory control, replenishment, material handling, warehouse planning, systems data, labor planning. | `map-line-side-logistics-flow`, `plan-production-material-replenishment`, `analyze-wip-logistics-status`, `plan-finished-goods-handoff`. | P1 |
| retail-distribution | Store replenishment, allocation support, cross-dock, seasonal flow, promotional readiness, and DC-to-store execution. | Store order cadence, allocation waves, cross-dock windows, seasonal peaks, store receiving constraints, retail compliance. | Retailer routing guides, labeling, chargeback, transport, labor, and product-specific rules may apply. | DC replenishment, cross-dock, store-ready palletization, wave release, promotion staging, exception reporting. | Warehouse operator, warehouse planner, fulfillment optimization, transportation, systems data, performance. | `plan-store-replenishment-flow`, `plan-retail-cross-dock-operation`, `analyze-retail-compliance-exception`, `prepare-promotion-distribution-plan`. | P2 |
| automotive | Parts logistics, sequencing, service parts, returnable packaging, supplier delivery windows, and production or dealer support. | Part supersession, kitting, sequencing, returnable containers, service-parts fill, supplier ASN quality. | Transportation, workplace safety, customs, hazardous components, quality, and customer-specific rules may apply. | Sequenced picking, kit staging, line-side delivery, returnable-container tracking, service-parts replenishment. | Inventory control, replenishment, material handling, systems data, transportation, manufacturing logistics. | `plan-automotive-parts-sequencing`, `manage-returnable-packaging-flow`, `analyze-service-parts-fill`, `reconcile-supplier-asn-quality`. | P2 |
| pharmaceuticals | Regulated product logistics with expiry, lot traceability, temperature sensitivity, controlled handling, recall, and quality release boundaries. | GDP-style logistics expectations, controlled status, quarantine, lot/serial traceability, expiry, chain of custody, excursion review. | Pharmaceutical, health authority, controlled substance, temperature, transport, documentation, and jurisdiction-specific rules may apply. | Controlled receiving, quarantine, released-stock movement, expiry management, recall support, temperature excursion handoff. | Inventory control, cold-chain, food-logistics-adjacent rotation, systems data, reverse logistics, compliance. | `classify-pharmaceutical-logistics-requirements`, `manage-pharma-quarantine-handoff`, `analyze-pharma-expiry-risk`, `support-pharma-recall-logistics`. | P2 |
| international-logistics | Cross-border and multi-country logistics involving customs handoffs, trade documents, incoterm context, duties/taxes boundaries, and mode-specific transit. | Customs broker handoffs, trade documents, party roles, incoterms, port/terminal flow, drayage, free-time, demurrage, duty/tax boundaries. | Customs, sanctions, export controls, import rules, dangerous goods, food/drug rules, and country-specific rules may apply. | Export document research, customs broker packet, import handoff, port exception triage, demurrage and detention source review. | Transportation, logistics coordinator, compliance specializations, systems data, performance, reverse logistics. | `plan-customs-broker-handoff`, `prepare-international-shipment-document-research`, `triage-port-terminal-exception`, `map-cross-border-logistics-flow`. | P2 |

## Priority Rationale

P0 candidates are the next build focus because AL-20 explicitly targets food and
cold-chain logistics and both reuse mature inventory, receiving, storage,
transportation, systems, and reverse-logistics foundations.

P1 candidates are high-value but need stronger safety, regulatory, customer, or
production-boundary design before implementation.

P2 candidates are valid extensions, but their domain rules are narrower,
heavier-weight, or better sequenced after the first industry specialization
proves the source-map and validation pattern.

## Specialization Package Standard

A future specialization package should contain:

- `README.md` with scope, source boundary, dependencies, excluded authority, and
  completion token;
- one package per atomic specialized skill under the specialization directory;
- `references/` source map for authoritative domain and jurisdiction sources;
- `agents/openai.yaml` for every invocable package;
- scenario file under `tests/scenarios/`;
- fixture file under `tests/fixtures/`;
- evaluation report under `tests/evaluations/`;
- final handoff under `docs/development/handoffs/`.

## Acceptance Criteria

Given AL-19 specialization architecture, when a candidate is reviewed, then the
review identifies domain need, unique knowledge, unique regulations, unique
workflows, shared core skills, new atomic skills required, and priority.
Evidence: this document's candidate evaluation table.

Given a proposed specialization, when it can be handled by existing universal
core skills or professional skillsets, then the specialization is not built and
the request routes to existing packages.
Evidence: extension rule 3 and the candidate table's shared core skills.

Given a proposed specialized regulatory or safety claim, when current official
sources are not available, then the output remains a research brief or evidence
request and requires qualified review.
Evidence: extension rules 2, 5, and 6.

Given AL-20 planning, when selecting the next specialization, then cold-chain
and food-logistics are the P0 candidates.
Evidence: priority rationale and the roadmap's AL-20 objective.

## Deferred Work

- Do not create industry specialization packages in AL-19.
- Do not add specialized regulatory claims without source maps.
- Do not add hard dependencies on other projects.
- Do not treat candidate atomic skill names as ready packages until a later wave
  builds and validates them.
