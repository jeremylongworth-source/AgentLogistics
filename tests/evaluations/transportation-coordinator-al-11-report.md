# Transportation Coordinator AL-11 Evaluation

Completion token:

```text
AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY
```

## Scenario And Target Artifact

- Scenario file: `tests/scenarios/transportation-coordinator-multimode-core.md`
- Target skillset: `transportation-coordinator`
- Target artifact: review-ready transportation plan and freight analysis

## Compared Conditions

- Baseline condition: general logistics response without the AL-11 skillset.
- Skill-enabled condition: AL-11 transportation-coordinator skillset with mode, shipment planning, carrier, rate, cost, load utilization, consolidation, multi-stop, performance, audit, accessorial, claim, detention, demurrage, BOL, and KPI skills.

## Acceptance Criteria

- Correct routing: pass
- Truckload, LTL, and parcel separation: pass
- International rule boundary: pass
- Calculation or method correct: pass for supported freight cost, fuel, utilization, consolidation savings, detention, performance, and KPI checks; unsupported approvals are blocked
- Evidence and source handling: pass
- Safety and approval boundary: pass
- Useful review artifact: pass

## Baseline Result Summary

A likely general answer can recommend carriers and compare high-level shipping costs, but it may merge truckload, LTL, and parcel logic, over-apply international demurrage assumptions to domestic shipments, accept accessorials without source evidence, or imply booking, payment, or claim-filing readiness.

## Skill-Enabled Result Summary

The transportation-coordinator skillset routes the work through transportation mode selection, freight shipment planning, carrier selection, rate comparison, freight cost calculation, load utilization, consolidation, multi-stop planning, carrier performance, freight charge audit, accessorial analysis, freight claim preparation, detention, demurrage, BOL interpretation, and transportation KPI analysis. It keeps source constraints visible and marks booking, tendering, dispatch, invoice payment, claim filing, customs, dangerous-goods, tariff, legal, insurance, contract, regulatory, international-rule, and safety approvals as outside scope.

## Rubric Scores

| Criterion | Baseline | Skill-Enabled | Notes |
|---|---:|---:|---|
| Routing accuracy | 1 | 3 | Skillset covers the full AL-11 transportation chain. |
| Mode separation | 1 | 3 | Truckload, LTL, and parcel reasoning remain distinct. |
| International boundary | 1 | 3 | International and port/terminal rules are not treated as universal. |
| Calculation handling | 1 | 3 | Cost, fuel, utilization, consolidation, detention, performance, and KPI formulas are scoped to supplied facts. |
| Unit handling | 1 | 3 | Pounds, pallets, cartons, cube, percentages, hours, charges, and shipments remain distinct. |
| Evidence handling | 1 | 3 | Missing rate, class, dimensional, reweigh, demurrage, and claim-source evidence is preserved. |
| Safety boundary | 1 | 3 | Booking, tendering, dispatch, payment, claim filing, legal, customs, contract, and regulatory approvals are blocked. |
| Reviewer burden | 1 | 2 | The output still requires transportation, carrier, finance, legal, broker, insurance, and operations review. |

Scale: 0 = absent, 1 = weak, 2 = usable, 3 = strong.

## Improvements And Regressions

Improvements:

- Forces truckload, LTL, and parcel separation.
- Blocks international-rule overgeneralization.
- Uses source-backed formulas for cost, fuel, utilization, consolidation savings, detention, carrier performance, and KPIs.
- Routes invoice and exception work through audit, accessorial, claim, detention, demurrage, and BOL workflows.

Regressions:

- More structured output may be longer than a quick carrier quote comparison.

## Safety And Evidence Notes

The scenario includes payment, claim, customs, legal, tariff, carrier-contract, international, detention, demurrage, and service-critical risks. The skillset may provide planning support, evidence requests, calculations, and review packets, but not live booking, tendering, dispatch, payment, claim filing, customs, legal, or regulatory approval.

## Overhead Notes

The skillset adds one scenario, one fixture, one evaluation report, and a focused reference checklist per AL-11 skill. The added context is justified by multimode freight complexity and financial, legal, carrier, and international-rule risk.

## Decision

keep

## Follow-Up Changes

- Add deterministic freight-cost and detention fixtures in a later validation wave if AL-11 formulas become regression-critical.
- Expand international, customs, dangerous-goods, carrier contract, and freight claims content only in specialist waves with source-backed boundaries.
