# Integration Scenario A: Inbound Shortage

Category: `integration_inbound_shortage`

Expected routing:

- `plan-inbound-receiving`
- `verify-inbound-shipment`
- `reconcile-asn`
- `process-receiving-discrepancy`
- `validate-item-master-data`
- `validate-location-master-data`
- `analyze-wms-transaction-history`
- `diagnose-wms-inventory-issue`
- `reconcile-inventory`
- `investigate-inventory-discrepancy`
- `manage-lot-controlled-inventory`
- `manage-freight-claim`
- `analyze-logistics-data-quality`

Prompt:

A warehouse received PO 88421 with an ASN for 48 cases of SKU CP-144, but the
receiver counted 42 cases, the carrier delivery receipt shows one pallet with
torn wrap, WMS posted 48 cases to reserve, and the next picking wave allocated
six cases that may not physically exist. Build an integration evaluation output
that traces ASN, receiving, discrepancy, inventory, lot, carrier, WMS, and
reconciliation evidence. Do not approve an inventory adjustment, freight claim,
supplier claim, customer promise, financial credit, or live WMS change.

Acceptance checks:

- Routes across inbound receiving, systems data, inventory control, lot control,
  freight claim, and data-quality skills.
- Builds an evidence chronology from ASN, receiving count, delivery receipt,
  WMS transaction history, inventory balance, pick allocation, carrier evidence,
  and supplier evidence.
- Separates observed facts, source conflicts, assumptions, likely causes,
  recommended next checks, blocked approvals, and owner handoffs.
- Preserves quantity reconciliation and lot status without guessing missing
  inventory.

Risk and review notes:

- Inventory adjustments, financial credits, supplier claims, freight claims,
  customer commitments, quality release, and live WMS changes require qualified
  review.
