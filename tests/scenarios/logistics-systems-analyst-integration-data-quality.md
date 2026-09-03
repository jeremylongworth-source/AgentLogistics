# Logistics Systems Analyst Integration Data Quality

Category: `logistics_systems_data_quality`

Expected routing:

- `map-wms-process`
- `analyze-wms-transaction-history`
- `diagnose-wms-inventory-issue`
- `validate-item-master-data`
- `validate-location-master-data`
- `analyze-logistics-scan-events`
- `design-logistics-barcode-flow`
- `interpret-gs1-identifiers`
- `design-logistics-unit-identification`
- `analyze-edi-logistics-flow`
- `map-erp-wms-integration`
- `map-wms-tms-integration`
- `analyze-logistics-data-quality`

Prompt:

```text
We need a logistics systems analyst brief for DC-03. Map the WMS process from
ASN receipt through putaway, replenishment, picking, packing, staging, ship
confirm, and inventory update. Include ERP, OMS, TMS, YMS, LMS, WCS, WES, EDI,
and API handoffs where the evidence supports them.

Evidence:
- ERP item master shows SKU ALC-778 base UOM EA, case pack 12, no item cube,
  no gross weight, GTIN field 00012345678905, lot control yes, expiry control
  yes, hazmat blank, temperature flag ambient.
- WMS item master shows SKU ALC-778 base UOM EA, case pack 10, length/width/
  height blank, catch-weight no, lot required, expiry required, status active.
- Location A-01-03 is a pick face in the slotting file, but WMS location master
  has type reserve, pickable false, replenishable true, capacity 5 pallets, and
  status active.
- WMS balance for ALC-778 at A-01-03 is 124 EA available. ERP inventory ledger
  shows 96 EA available. Physical count at 15:10 Eastern found 100 EA.
- WMS transactions show receipt 240 EA at 08:03 Eastern, putaway 120 EA to
  R-12-04 at 08:42, move 120 EA from R-12-04 to A-01-03 at 10:12, pick confirm
  20 EA at 12:25, reversal 20 EA at 12:31, adjustment +4 EA at 14:05 without
  attached supervisor approval, and cycle count 100 EA at 15:10.
- Scan logs show pallet SSCC candidate value 000123456789012345 scanned twice
  at pack, no ship-confirm scan for carton C-10018, one handheld scanner clock
  appears to be UTC while WMS reports Eastern, and TMS received a late manifest
  update at 16:33.
- The label sample includes GS1-style data fields for GTIN, batch or lot, expiry
  date, serial, and pallet SSCC. Do not invent GS1 rules; use official GS1
  source material wherever possible before interpreting identifiers or proposing
  the barcode flow.
- Middleware shows an ASN/despatch advice message accepted by EDI at 07:54,
  posted to WMS at 08:01, and a receipt confirmation queued to ERP until 15:45.
  An API retry log shows the ship-confirm payload reached ERP before TMS sent
  carrier tracking back to WMS.

Return an evidence-backed brief that includes the WMS process map, transaction
chronology, WMS inventory issue diagnosis, item and location master validation,
scan-event analysis, GS1-aware barcode and unit-identification flow, EDI flow,
ERP-WMS integration map, WMS-TMS integration map, and logistics data-quality
assessment. Do not configure live systems, change master data, post inventory
adjustments, call production APIs, transmit EDI, certify GS1 compliance, or
approve any financial, legal, regulatory, safety, or audit outcome.
```

Acceptance checks:

- Output covers WMS, TMS, ERP, OMS, YMS, LMS, WCS, WES, EDI, and APIs where evidence supports them.
- Output invokes all thirteen AL-12 priority skills.
- WMS process map distinguishes operational steps, system transactions, manual work, status changes, source records, and handoffs.
- WMS transaction chronology accounts for receipt, putaway, move, pick, reversal, adjustment, cycle count, timezone issues, and source-system lineage.
- Inventory diagnosis reconciles WMS, ERP, physical count, transactions, holds or allocations if supplied, and UOM or pack-hierarchy conflicts without guessing root cause.
- Item master validation flags missing dimensions and weight, UOM or case-pack mismatch, identifier fields, lot and expiry controls, and operational impact.
- Location master validation flags location type, zone or pickability conflicts, capacity assumptions, status, and physical-use evidence.
- Scan-event analysis identifies duplicate SSCC scan, missing ship-confirm scan, late manifest update, device timestamp conflict, and source evidence gaps.
- Barcode and logistics-unit design use official GS1 source material wherever possible before interpreting GTIN, SSCC, GLN, batch or lot, serial, expiry date, Application Identifier, Digital Link, or EPCIS concepts.
- EDI, ERP-WMS, and WMS-TMS integration maps identify sender, receiver, trigger, payload or field groups, acknowledgements, retries, errors, status propagation, and reconciliation controls.
- Data-quality assessment includes completeness, validity, consistency, uniqueness, timeliness, accuracy, lineage, ownership, controls, risk priority, and remediation handoff.
- Recommendations are planning support and do not become production configuration, master-data approval, inventory adjustment, EDI transmission, API credential use, freight booking, or compliance approval.

Risk and review notes:

- GS1 concepts require official GS1 sources wherever possible and must not be treated as compliance certification.
- Live WMS, TMS, ERP, OMS, YMS, LMS, WCS, WES, EDI, API, scanner, label, inventory, master-data, financial, carrier, customer, supplier, and trading-partner changes are out of scope.
- Financially material, customer-critical, regulated, privacy, cybersecurity, audit, safety, or production-system conclusions require qualified review.
