# Transportation Coordinator Multimode Core

Category: `transportation_multimode_core`

Expected routing:

- `select-transportation-mode`
- `plan-freight-shipment`
- `select-carrier`
- `compare-freight-rates`
- `calculate-freight-cost`
- `calculate-load-utilization`
- `plan-freight-consolidation`
- `plan-multi-stop-shipment`
- `analyze-carrier-performance`
- `audit-freight-charge`
- `analyze-freight-accessorials`
- `manage-freight-claim`
- `analyze-detention`
- `analyze-demurrage`
- `interpret-bill-of-lading`
- `analyze-transportation-kpis`

Prompt:

```text
We need a review-ready transportation plan and freight analysis for next week's domestic outbound work. Do not book, tender, dispatch, route, pay invoices, file claims, approve legal terms, approve customs or dangerous-goods compliance, or change any live TMS, ERP, carrier, broker, financial, customs, or shipment records. Do not apply international ocean, customs, port, rail, tariff, or jurisdiction-specific rules as universal truckload, LTL, or parcel rules.

Shipment profile:

- Truckload: 2 domestic dry-van lanes from Ohio to Texas. Each load has 24 pallets, 42,000 lb, and a requested delivery window within 3 business days. Trailer usable cube is listed as 3,600 cubic feet, and estimated freight cube is 2,880 cubic feet.
- LTL: 14 domestic customer shipments across the Midwest, 1 to 5 pallets each, 18,600 lb total, mixed class data, two liftgate deliveries, and three appointment deliveries. A routing guide lists Carrier A and Carrier B as approved LTL carriers.
- Parcel: 640 cartons for ecommerce orders, 5,200 lb total, mostly residential delivery, with a two-day service promise for 70 percent of the cartons.

Rate and cost evidence:

- Truckload quote A is $2,850 linehaul plus 18 percent fuel. Truckload quote B is $2,650 linehaul plus 22 percent fuel and a $95 tracking fee.
- LTL quote summary is $4,980 linehaul, $610 fuel, $220 liftgate, and $180 appointment fees. Freight class is missing for 4 shipments.
- Parcel manifest estimate is $7,420 base charges plus $1,115 residential surcharge and $390 delivery-area surcharge. Dimensional-weight source rules were not supplied.

Carrier and shipment context:

- Carrier A: 94 percent on-time delivery across 310 shipments, 88 percent tender acceptance, 1.1 percent claims rate, and frequent appointment fee disputes.
- Carrier B: 91 percent on-time delivery across 280 shipments, 96 percent tender acceptance, 0.6 percent claims rate, and higher linehaul on this lane.
- Consolidation option: 6 Midwest LTL shipments could move together if Friday delivery is acceptable. Current separate estimate is $2,340; consolidated estimate is $1,875 before any new accessorials.
- Multi-stop option: One truckload could serve Dallas then Austin, but Austin must unload first if its pallets are rear-loaded. Dallas appointment is 09:00 to 11:00 and Austin appointment is 13:00 to 15:00.

Audit, documents, and exception context:

- Invoice INV-778 shows the LTL charges above plus a $175 reweigh fee and a $250 detention fee. The scale ticket source for reweigh was not supplied. Detention record says check-in 08:05, dock-in 09:10, unload complete 11:25, departure 11:45, with 2 hours free time and $85 per hour after free time.
- One imported container shipment has a terminal storage/demurrage concern. The user only provided event dates and no tariff, terminal schedule, free-time source, broker note, customs release, or carrier rule. Do not use that container rule for the domestic TL, LTL, or parcel shipments.
- BOL BOL-443 lists shipper DC-12, consignee Retailer 17, 12 pallets, 18,200 lb, prepaid terms, and a delivery appointment reference. The invoice says 18,850 lb.
- Claim issue CL-91: one LTL pallet arrived damaged. Available evidence includes photos at delivery, signed POD noting damage, product invoice value of $1,460, and customer email. No carrier claim form or deadline source was supplied.

Build a response covering mode selection, freight shipment planning, carrier selection, freight rate comparison, freight cost calculation, load utilization, consolidation, multi-stop planning, carrier performance, freight charge audit, accessorial analysis, freight claim preparation, detention analysis, demurrage source gaps, BOL interpretation, transportation KPIs, missing evidence, and review-required actions.
```

Acceptance checks:

- Validates truckload, LTL, and parcel reasoning separately.
- Does not treat international ocean, customs, port, rail, tariff, or jurisdiction-specific rules as universal domestic truckload, LTL, or parcel rules.
- Calculates supported freight cost, fuel, utilization, consolidation savings, detention time/charge, carrier performance, or KPI values only from supplied facts.
- Routes invoice issues through freight audit, accessorial analysis, detention, and demurrage as appropriate.
- Treats missing freight class, dimensional-weight rules, reweigh source, demurrage tariff/free-time source, carrier claim form, and claim deadline as missing evidence.
- Distinguishes planning and review support from live tendering, booking, dispatch, payment approval, legal approval, customs approval, dangerous-goods approval, and claim filing.

Risk and review notes:

- Synthetic scenario only. The case includes no private customer data or live system requirement. Transportation manager, carrier, finance, legal, customs broker, insurance, safety, and qualified operations review may be required before operational use.
