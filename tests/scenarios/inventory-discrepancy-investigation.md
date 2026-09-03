# Inventory Discrepancy Investigation

Category: `inventory_discrepancy_investigation`

Expected routing:

- `classify-inventory`
- `calculate-inventory-accuracy`
- `reconcile-inventory`
- `investigate-inventory-discrepancy`
- `verify-inbound-shipment`
- `process-receiving-discrepancy`
- `analyze-stockout`
- `manage-lot-controlled-inventory`
- `analyze-inventory-shrinkage`

Prompt:

```text
We need a review-ready investigation for SKU AL-VALVE-14, lot L2408-A,
in location RES-A-03. Do not guess the root cause. Trace the evidence,
quantify what can be reconciled, list conflicts, and tell us what records
are still missing before any inventory adjustment is approved.

Evidence snapshot:

- Purchase order expected 100 each. The inbound receiving worksheet says
  96 each were received on August 28 at 09:20, but the receiving clerk's
  note says 4 cases of 25 each were unloaded and one case label was torn.
- The ASN says 100 each shipped. The BOL has no shortage notation.
- WMS balance at the start of September 1 was 82 each available and 8
  each allocated. The item ledger export shows a receipt of 96 each, two
  picks of 12 each and 6 each, a transfer out of 10 each, and a manual
  adjustment of -4 each with reason code "count correction".
- Physical cycle count on September 1 at 14:10 found 64 each in RES-A-03.
  A recount at 15:05 found 65 each. The count sheet says two loose eaches
  had no readable lot label.
- The picking log shows order SO-7781 picked 12 each from RES-A-03 and
  SO-7790 short-picked 6 each even though the WMS still showed available
  balance. A picker note says the forward pick face was empty before noon.
- Adjustment history shows the -4 each was entered after the first count
  but before the recount. No approver is listed in the export.

Build a source-by-source evidence table, transaction chronology, quantity
bridge, conflict list, evidence-ranked candidate causes, and missing
evidence list. Include any lot-control, stockout, shrinkage, and receiving
discrepancy handoffs that are supported by the facts.
```

Acceptance checks:

- Includes all five conflict classes: receiving quantity, WMS balance,
  physical count, picking transactions, and adjustment history.
- Builds a transaction chronology before naming candidate causes.
- Shows a quantity reconciliation bridge and identifies the unsupported
  transaction signs or timing gaps.
- Separates source facts, calculated values, assumptions, conflicts, and
  missing evidence.
- Ranks candidate causes by cited evidence and avoids a guessed root cause.
- Preserves lot-control, stockout, shrinkage, and receiving-discrepancy
  handoff boundaries.
- States that inventory adjustment approval requires owner review.

Risk and review notes:

- Synthetic scenario only. The case includes no private customer data,
  live system requirement, or accusation. Any operational adjustment,
  financial write-off, or personnel action requires site owner review.
