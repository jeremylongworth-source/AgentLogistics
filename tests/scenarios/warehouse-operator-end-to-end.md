# Warehouse Operator End-To-End

Category: `skillset_end_to_end`

Expected routing:

- `analyze-logistics-operation`
- `map-logistics-flow`
- `analyze-product-flow`
- `analyze-order-profile`
- `plan-inbound-receiving`
- `verify-inbound-shipment`
- `inspect-received-goods`
- `reconcile-asn`
- `process-receiving-discrepancy`
- `plan-putaway`
- `classify-storage-requirements`
- `calculate-storage-capacity`
- `calculate-pallet-positions`
- `analyze-storage-utilization`
- `plan-replenishment`
- `select-picking-strategy`
- `calculate-pick-productivity`
- `plan-packing-operation`
- `plan-shipping-stage`
- `verify-outbound-shipment`

Prompt:

```text
We run a small warehouse that receives palletized vendor shipments, inspects
them at the dock, puts accepted goods into reserve storage, replenishes a forward
pick area, picks ecommerce and wholesale orders, packs them, stages by carrier,
and verifies shipments before pickup.

Create an operating response for tomorrow. We have one inbound vendor truck with
PO and ASN documents, two SKUs that need visible damage inspection, limited
reserve pallet space, a forward-pick area that may stock out before the 3 PM
carrier cutoff, and a backlog of orders. Show the flow, evidence needed,
calculations or checks that are safe to perform from the provided facts,
exceptions, and handoffs from receiving through shipping.
```

Acceptance checks:

- Preserves the full receive, inspect, putaway, store, replenish, pick, pack,
  stage, and ship sequence.
- Uses logistics fundamentals to establish operation, product, order, and flow
  context before detailed steps.
- Routes inbound document and count checks before inspection and discrepancy
  handling.
- Routes storage decisions through storage requirement and capacity checks.
- Routes fulfillment through replenishment and picking before pack and stage.
- Performs only calculations supported by supplied values and asks for missing
  capacity, labor, or productivity inputs.
- Refuses compliance, safety, rack-load, carrier, customs, or hazardous-goods
  approval claims.
- Returns an action-oriented warehouse operating plan with evidence gaps and
  handoff notes.

Risk and review notes:

- Representative warehouse scenario with safety, storage-capacity, and shipment
  handoff boundaries. Requires site review before operational use.
