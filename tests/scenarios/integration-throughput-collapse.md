# Integration Scenario B: Warehouse Throughput Collapse

Category: `integration_throughput_collapse`

Expected routing:

- `analyze-order-profile`
- `calculate-replenishment-demand`
- `prioritize-replenishment`
- `plan-picking-wave`
- `plan-zone-picking`
- `optimize-pick-path`
- `diagnose-picking-bottleneck`
- `calculate-pick-productivity`
- `forecast-warehouse-workload`
- `calculate-labor-requirements`
- `balance-warehouse-workload`
- `analyze-labor-productivity`
- `analyze-warehouse-kpis`
- `analyze-throughput`
- `diagnose-throughput-loss`
- `identify-logistics-bottleneck`
- `perform-logistics-root-cause-analysis`
- `build-logistics-improvement-plan`
- `measure-improvement-result`

Prompt:

Over three days, outbound throughput fell from 16,000 order lines per day to
9,400 while ecommerce each-pick orders increased, replenishment queues doubled,
two zones ran out of forward pick slots, overtime rose 28 percent, and staging
missed carrier cutoffs. Build an integration evaluation output connecting order
profile, replenishment, picking, labor, congestion, KPI analysis, root cause,
and improvement planning. Do not approve staffing spend, overtime policy,
equipment purchase, slotting release, customer commitment, or live WMS/LMS
change.

Acceptance checks:

- Routes across fulfillment optimization, labor planning, warehouse planning,
  performance, and continuous-improvement skills.
- Separates demand mix, replenishment constraints, pick-path effects, staffing
  capacity, congestion, carrier cutoff misses, KPI baseline, root-cause
  hypotheses, recommendations, and measurement plan.
- Distinguishes observation, evidence, inference, root cause, recommendation,
  expected effect, and measurement plan.
- Labels missing order, labor, location, replenishment, and cutoff evidence.

Risk and review notes:

- Staffing commitments, overtime decisions, equipment approvals, system
  changes, safety decisions, customer promises, and financial approvals require
  qualified review.
