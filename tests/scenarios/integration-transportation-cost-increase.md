# Integration Scenario E: Transportation Cost Increase

Category: `integration_transportation_cost_increase`

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
- `analyze-detention`
- `analyze-demurrage`
- `analyze-transportation-kpis`
- `compare-logistics-scenarios`
- `build-logistics-improvement-plan`

Prompt:

Transportation cost per shipped case increased 18 percent quarter over quarter.
Shipment data shows more LTL moves, lower trailer cube utilization, repeated
detention at one customer, two demurrage invoices on import containers, fuel
surcharge changes, and carrier on-time decline. Build an integration evaluation
output connecting shipment profile, rates, accessorials, utilization, carrier
performance, consolidation, scenario comparison, and improvement planning. Do
not approve carrier selection, rate acceptance, claim filing, demurrage payment,
customer chargeback, financial posting, or live TMS change.

Acceptance checks:

- Routes across transportation, freight analysis, performance analysis, and
  continuous-improvement skills.
- Separates rate, accessorial, detention, demurrage, utilization, mode mix,
  carrier performance, customer behavior, and volume-mix evidence.
- Compares improvement scenarios with assumptions, expected effect, risks,
  required data, and measurement plan.
- Blocks carrier, claim, payment, customer, finance, and live-system approvals.

Risk and review notes:

- Carrier awards, rate acceptance, claims, detention or demurrage payments,
  customer chargebacks, financial postings, regulatory decisions, and live TMS
  changes require qualified review.
