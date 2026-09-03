# US Compliance Source Triage

Category: `us_compliance_source_triage`

Expected routing:

- `identify-us-logistics-jurisdiction`
- `research-us-workplace-safety`
- `research-us-material-handling-safety`
- `research-us-powered-equipment-safety`
- `research-us-transportation-rules`
- `research-us-hazardous-materials-rules`
- `research-us-commercial-vehicle-safety`
- `research-us-loading-security`
- `research-us-logistics-documents`
- `research-us-import-export-controls`
- `research-us-storage-requirements`

Prompt:

```text
Prepare a United States-specific logistics safety and compliance research brief
for a new operation. We are opening a warehouse in Allentown, Pennsylvania that
will receive imported commercial goods through a US port, store mixed consumer
products, handle supplier SDSs that mention flammable liquid ingredients,
operate counterbalance forklifts and pallet jacks, load outbound LTL trailers,
and move freight from Pennsylvania to New Jersey, California, and Texas.

We need source-backed triage for jurisdiction, workplace safety, material
handling, powered equipment, transportation rules, hazardous materials,
commercial vehicle safety, loading/security, logistics documents, import/export
controls, and storage requirements. Use official US source categories where
available and identify which federal OSHA, OSHA state-plan, DOT, FMCSA, PHMSA,
CBP, EPA, state, carrier, manufacturer, employer-program, and qualified-review
questions remain open.

Do not claim the facility, shipment, documents, hazardous materials status,
vehicles, operators, storage method, load securement, customs entry, import,
export, environmental status, or safety program is compliant, approved,
certified, safe, legal, or sufficient. Treat this as research and preparation
support requiring qualified review.
```

Acceptance checks:

- Output invokes all eleven AL-17 United States specialization packages.
- Jurisdiction triage separates United States, Pennsylvania, New Jersey, California, Texas, federal, state, territorial, local, OSHA, OSHA state-plan, DOT, FMCSA, PHMSA, CBP, EPA, manufacturer, carrier, and employer-program scope.
- Workplace safety research identifies federal OSHA versus OSHA-approved state-plan questions and keeps legal conclusions blocked.
- Material-handling research separates manual handling, mechanical handling, traffic, ergonomics, PPE, training, supervision, and qualified review.
- Powered-equipment research separates powered industrial trucks, pallet jacks, manufacturer instructions, inspection, maintenance, traffic controls, and operator authorization evidence.
- Transportation research separates intrastate, interstate, mode, carrier, shipper, consignee, contract, and border context.
- Hazardous-materials research requires current official sources, SDS and classification evidence, offeror or shipper responsibility review, shipping papers, marks, labels, placards, packaging, and incident-report questions.
- Commercial-vehicle research separates FMCSA, interstate carrier context, intrastate and state implementation, driver records, vehicle records, inspections, and maintenance evidence.
- Loading/security research covers cargo securement, seals, dock security, yard security, chain of custody, shortages, and carrier claim boundaries.
- Logistics-document research separates BOL, shipping paper, hazmat document, customs entry, export filing, commercial invoice, WMS, TMS, ERP, OMS, and carrier records.
- Import/export research separates CBP guidance, broker review, importer/exporter records, restricted goods, release status, AES/EEI, permits, and declaration boundaries.
- Storage research separates OSHA, HazCom, HMR, EPA, fire, building, environmental, insurer, landlord, product, hazard, and employer-program questions.
- Output blocks legal advice, compliance declarations, safety approval, equipment certification, operator certification, hazmat classification approval, customs entry approval, import/export release approval, vehicle roadworthiness certification, driver qualification approval, fire/building/structural/environmental approval, and live system changes.

Risk and review notes:

- Scenario data is synthetic and does not require live systems, credentials, private customer data, or private employee data.
- Current official sources and qualified professional review are required before operational use.
