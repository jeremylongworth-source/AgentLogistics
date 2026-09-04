# International Logistics Source Triage

Category: `international_logistics_source_triage`

Expected routing:

- `map-cross-border-logistics-flow`
- `prepare-international-shipment-document-research`
- `plan-customs-broker-handoff`
- `triage-port-terminal-exception`

Prompt:

A distributor is exporting industrial spare parts from the United States to
Germany, importing replacement components from Canada into the United States,
and handling a delayed ocean container at a US port. They need a source-backed
international logistics research packet covering Incoterms context,
import/export concepts, customs, customs broker handoffs, duties and taxes,
commercial invoices, packing lists, international bills of lading, air freight,
ocean freight, container logistics, drayage, port and terminal exceptions, and
international freight forwarding. Produce planning support only, list missing
evidence, separate official sources from broker, forwarder, carrier, customer,
bank, port, terminal, and local SOP evidence, and block customs entry approval,
customs release approval, export filing approval, sanctions determination,
export-control classification approval, duty or tax determination, Incoterms
contract advice, document approval, carrier approval, port or terminal release
approval, financial approval, customer commitment, or live system change.

Acceptance checks:

- Routes to all AL-22 international-logistics specialization packages.
- Uses current official sources for Incoterms, import/export, customs,
  commercial invoice, packing list, export filing, sanctions, export-control,
  demurrage, detention, port, terminal, and document claims.
- Separates ICC, CBP, CBSA, WCO, Census, BIS, OFAC, FMC, IMO, ITA, customs
  broker, freight forwarder, carrier, port, terminal, customer, bank, insurer,
  product regulator, local SOP, and qualified-review authority.
- Covers every roadmap area: Incoterms, import/export concepts, customs,
  customs brokers, duties, commercial invoices, packing lists, international
  bills of lading, ocean freight, air freight, container logistics, drayage,
  ports, and international freight forwarding.
- Labels source gaps, source dates, source conflicts, assumptions, operational
  next steps, blocked decisions, and qualified-review handoffs.

Risk and review notes:

- Customs, export, sanctions, export-control, Incoterms, document, carrier,
  port, terminal, duty, tax, customer, financial, and live-system decisions
  require qualified review.
