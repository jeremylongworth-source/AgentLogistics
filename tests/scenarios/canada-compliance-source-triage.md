# Canada Compliance Source Triage

Category: `canada_compliance_source_triage`

Expected routing:

- `identify-canadian-logistics-jurisdiction`
- `research-canadian-workplace-safety`
- `research-canadian-material-handling-safety`
- `research-canadian-powered-equipment-safety`
- `research-canadian-transportation-rules`
- `research-canadian-dangerous-goods-rules`
- `research-canadian-commercial-vehicle-safety`
- `research-canadian-loading-security`
- `research-canadian-logistics-documents`
- `research-canadian-import-export-controls`
- `research-canadian-storage-requirements`

Prompt:

```text
Prepare a Canada-specific logistics safety and compliance research brief for a
new operation. We are opening a warehouse in Brampton, Ontario that will receive
imported commercial goods from the United States, store mixed consumer products,
handle some supplier SDSs that mention flammable liquid ingredients, operate
counterbalance forklifts and pallet jacks, load outbound LTL trailers, and move
some freight from Ontario to Quebec and Nova Scotia.

We need source-backed triage for jurisdiction, workplace safety, material
handling, powered equipment, transportation rules, dangerous goods, commercial
vehicle safety, loading/security, logistics documents, import/export controls,
and storage requirements. Use official Canadian source categories where
available and identify which provincial, federal, Transport Canada, CBSA,
WHMIS, TDG, carrier, manufacturer, employer-program, and qualified-review
questions remain open.

Do not claim the facility, shipment, documents, dangerous goods status,
vehicles, operators, storage method, load securement, customs release, import,
export, or safety program is compliant, approved, certified, safe, legal, or
sufficient. Treat this as research and preparation support requiring qualified
review.
```

Acceptance checks:

- Output invokes all eleven AL-16 Canada specialization packages.
- Jurisdiction triage separates Canada, Ontario, Quebec, Nova Scotia, federal, provincial, territorial, municipal, carrier, customs, WHMIS, TDG, manufacturer, and employer-program scope.
- Workplace safety research identifies federal versus provincial or territorial OHS questions and keeps legal conclusions blocked.
- Material-handling research separates manual handling, mechanical handling, traffic, ergonomics, PPE, training, supervision, and qualified review.
- Powered-equipment research separates forklifts, pallet jacks, manufacturer instructions, inspection, maintenance, traffic controls, and operator authorization evidence.
- Transportation research separates intraprovincial, interprovincial, mode, carrier, shipper, consignee, contract, and border context.
- Dangerous-goods research requires current official sources, SDS and classification evidence, consignor responsibility review, TDG documents, marks, containment, and incident-report questions.
- Commercial-vehicle research separates federal extra-provincial carrier context from provincial and territorial implementation, driver records, vehicle records, inspections, and maintenance evidence.
- Loading/security research covers load securement, seals, dock security, yard security, chain of custody, shortages, and carrier claim boundaries.
- Logistics-document research separates BOL, waybill, TDG shipping document, customs release, export report, commercial invoice, WMS, TMS, ERP, OMS, and carrier records.
- Import/export research separates CBSA guidance, broker review, importer/exporter records, restricted goods, release status, permits, and declaration boundaries.
- Storage research separates OHS, WHMIS, TDG, fire, building, environmental, insurer, landlord, product, hazard, and employer-program questions.
- Output blocks legal advice, compliance declarations, safety approval, equipment certification, operator certification, TDG classification approval, customs declaration approval, import/export release approval, vehicle roadworthiness certification, driver qualification approval, fire/building/structural/environmental approval, and live system changes.

Risk and review notes:

- Scenario data is synthetic and does not require live systems, credentials, private customer data, or private employee data.
- Current official sources and qualified professional review are required before operational use.
