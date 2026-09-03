# Reverse Logistics Return Lifecycle

Category: `reverse_logistics_return_lifecycle`

Expected routing:

- `process-customer-return`
- `classify-return-disposition`
- `inspect-returned-goods`
- `reconcile-returned-inventory`
- `analyze-return-reason`
- `analyze-return-rate`
- `plan-return-to-stock`
- `plan-return-to-vendor`
- `manage-damaged-inventory`
- `manage-nonconforming-inventory`
- `analyze-reverse-logistics-cost`
- `design-reverse-logistics-flow`

Prompt:

```text
Build a reverse-logistics lifecycle brief for DC-08. We need the customer return
workflow, returned-goods inspection, disposition classification, returned
inventory reconciliation, return reason analysis, return-rate calculation,
return-to-stock plan, return-to-vendor plan, damaged-inventory workflow,
nonconforming-inventory workflow, reverse logistics cost analysis, and a
reverse-flow design.

Evidence:
- RMA R-8842 authorized 120 EA of SKU RL-440 from ecommerce customer order
  SO-77881. Customer reason code is DAMAGED, but the customer note says "wrong
  item and crushed packaging." Return policy says unopened sellable units may
  be considered for restock after inspection and quality release.
- Carrier tracking shows 10 cartons delivered to the returns dock at 09:35.
  WMS return receipt posted 116 EA at 10:12 into location RTN-INSPECT. ERP has
  not posted the return receipt. OMS shows refund pending review.
- Inspection at 11:20 found 90 EA unopened with intact inner packaging, 18 EA
  with crushed outer packaging but readable lot labels, 6 EA with leaking
  product, and 2 EA missing from the received cartons. Photos are referenced by
  inspection ticket Q-552 but are not attached to this request.
- Item master shows lot control yes, serial control no, expiry control yes,
  ambient storage, hazmat flag blank, and customer resale restriction unknown.
  Lot L24A expires 2027-02-28. The quality hold record says release criteria
  are required before any return-to-stock move.
- Vendor policy excerpt says defective units may be eligible for RTV with vendor
  authorization, inspection notes, photos, original PO, and carton count. Vendor
  authorization is not yet present.
- Current disposition proposal from operations: 90 EA return to stock, 18 EA
  rework/repack review, 6 EA damaged hold, 2 EA shortage investigation, and any
  confirmed defect to RTV if vendor authorization arrives.
- Last month: 1,240 returns on 48,000 shipped orders. SKU RL-440 had 88 returns
  on 1,760 shipped orders. Reason counts for RL-440 were DAMAGED 46, WRONG_ITEM
  25, QUALITY 12, LATE 5. Duplicate RMA records may exist for two cases.
- Cost evidence: average inspection labor is 0.12 hours per returned unit at a
  supplied planning rate of 24.00 per hour, inbound return freight for this RMA
  is 186.50, repack material is 0.80 per reworked unit, RTV outbound freight is
  estimated at 92.00 if authorized, scrap handling is estimated at 1.15 per
  damaged unit, and resale recovery value is 18.00 per released unit.

Do not approve refunds, credits, warranty decisions, inventory adjustments,
quality release, return-to-stock release, RTV claim, vendor debit, disposal,
destruction, recall action, customer remedy, financial posting, hazmat
classification, safety determination, or live OMS/WMS/ERP/TMS/RMA/quality
system changes. Treat this as planning support requiring qualified review.
```

Acceptance checks:

- Output invokes all twelve AL-15 priority skills.
- Return workflow maps request, authorization, receipt, inspection, disposition, inventory, customer, vendor, transportation, and financial handoffs.
- Inspection separates observed condition, customer-stated reason, source evidence, photos gap, lot and expiry controls, and quality release needs.
- Disposition classification labels return-to-stock, rework/repack, damaged hold, shortage investigation, RTV, scrap, and review-required paths without approval.
- Inventory reconciliation compares authorized, delivered, received, inspected, held, missing, proposed return-to-stock, proposed RTV, damaged, and ERP/WMS/OMS status quantities.
- Return reason analysis separates DAMAGED, WRONG_ITEM, QUALITY, LATE, customer notes, inspection evidence, and miscoding risk.
- Return-rate calculation defines numerator, denominator, timeframe, exclusions, SKU segment, reason segment, duplicate risk, and comparison basis.
- Return-to-stock plan requires inspection evidence, quality release, lot/expiry controls, status, location, relabel or repack needs, and system-change boundary.
- RTV plan requires vendor authorization, documents, photos, quantity, packaging, shipping handoff, and claim/credit boundary.
- Damaged-inventory workflow separates damage evidence, cause gap, affected quantity, hold, claim review, safety escalation, and disposal boundary.
- Nonconforming-inventory workflow separates requirement failure from physical damage and identifies hold owner, criteria, disposition, and release boundary.
- Reverse-cost analysis calculates inspection labor, freight, rework material, RTV freight estimate, scrap handling estimate, resale recovery, net cost, assumptions, and financial approval boundary.
- Reverse-flow design covers return types, channels, facility steps, disposition paths, controls, systems, exceptions, owners, metrics, and review boundaries.
- Output blocks refund approval, credit approval, warranty approval, inventory adjustment, quality release, RTV claim approval, vendor debit, disposal/destruction approval, recall action, financial posting, regulated-product determination, and live system changes.

Risk and review notes:

- Scenario data is synthetic and does not require live systems, credentials, private customer data, or private employee data.
- Regulated, hazardous, food, pharma, medical, recalled, contaminated, safety-sensitive, financially material, or customer-critical goods require qualified review.
