# AL-23 Repository-Wide Integration Evaluation

Completion token: `AGENTLOGISTICS_AL_23_INTEGRATION_VALIDATED`

## Baseline Result Summary

Before AL-23, AgentLogistics had validated atomic skills, professional
skillsets, compliance specializations, food cold-chain, dangerous-goods, and
international-logistics packages. Prior evaluations proved individual waves,
but the repository had not yet recorded a cross-domain integration gate for
realistic scenarios that move through multiple domains and preserve consistent
evidence, assumptions, calculations, routing, and approval boundaries.

## Skill-Enabled Result Summary

AL-23 adds five repository-wide integration scenarios and one deterministic
fixture covering inbound shortage, warehouse throughput collapse, inventory
accuracy deterioration, capacity constraint, and transportation cost increase.
The scenarios require cross-skill routing through receiving, storage,
inventory, replenishment, picking, packing, shipping, freight, systems data,
KPIs, labor, warehouse capacity, performance improvement, and relevant
specializations while blocking inventory, financial, customer, carrier, safety,
structural, food safety, staffing, and live-system approvals.

## Rubric Scores

| Criterion | Score | Notes |
| --- | ---: | --- |
| Scenario coverage | 5 | All five AL-23 roadmap scenarios are represented. |
| Cross-skill routing | 5 | Expected routes span the relevant domains and reference existing packages. |
| Evidence discipline | 5 | Fixtures require source-by-source evidence, chronology, missing evidence, and source conflict handling. |
| Calculation and unit handling | 5 | Capacity, utilization, quantity, and cost scenarios require visible inputs and unit checks. |
| Boundary handling | 5 | Operational, financial, safety, customer, carrier, and live-system approvals are blocked. |
| Verification | 5 | Test validation checks scenario files, route groups, fixture invariants, and report token. |

## Decision

keep

The AL-23 integration evaluation is ready to keep because it validates that
AgentLogistics operates as a coherent system across realistic multi-domain
logistics workflows rather than only as isolated prompt packages.
