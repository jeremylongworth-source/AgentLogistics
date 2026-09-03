# Continuous Improvement Specialist Performance Review

Category: `continuous_improvement_analysis`

Expected routing:

- `select-logistics-kpis`
- `build-logistics-scorecard`
- `analyze-warehouse-kpis`
- `analyze-throughput`
- `diagnose-throughput-loss`
- `identify-logistics-bottleneck`
- `perform-logistics-root-cause-analysis`
- `perform-logistics-pareto-analysis`
- `map-warehouse-process`
- `analyze-logistics-waste`
- `compare-logistics-scenarios`
- `build-logistics-improvement-plan`
- `measure-improvement-result`

Prompt:

```text
We need a continuous-improvement specialist brief for DC-04. Build a logistics
performance review that selects the right KPIs, designs a weekly scorecard,
analyzes current warehouse KPIs, calculates throughput, diagnoses throughput
loss, identifies the bottleneck, performs root-cause and Pareto analysis, maps
the warehouse process, identifies waste, compares improvement scenarios, builds
an improvement plan, and defines how to measure the result.

Scope and data:
- Outbound current-state process is wave release, pick, replenishment exception,
  pack, label print, staging, trailer load, ship confirm.
- Week 35 output was 41,600 order lines over 400 paid labor hours. Productive
  picking time was 352 hours after breaks and downtime. Target is 130 lines per
  productive labor hour; baseline from weeks 31-34 is 118.
- Pack produced 18,900 cartons over 188 productive pack hours. Target is 110
  cartons per productive hour; baseline is 104. WIP before pack grew from 220
  cartons at 10:00 to 760 cartons at 15:00.
- On-time ship was 92.1% against a 98.0% target. Pick accuracy was 99.2%
  against a 99.7% target. Putaway aging over 24 hours was 18.4% against a 10.0%
  target. Overtime was 15.2% of labor hours against a 9.0% target.
- Issue counts for Week 35: label reprint errors 48, replenishment stockouts 31,
  dock-door waits 27, scanner outages 12, location exceptions 8, cartonization
  errors 7.
- Observations from supervisor walks: pickers wait for replenishment in Zone B,
  packers walk to a shared label printer, staged pallets block two outbound
  lanes after 14:00, and ship confirms are batch-posted near shift end.
- Candidate scenarios: move label printing to each pack bench, start Zone B
  replenishment two hours earlier, rebalance two workers from pick to pack after
  12:00, or add a temporary overflow staging lane.
- A pilot moved label printing to two pack benches for three days in Week 36.
  Pack rate rose from 100 to 112 cartons per productive hour, label reprints
  fell from 48 per week to a projected 19 per week, overtime stayed at 15.0%,
  and on-time ship rose to 94.0%. Order mix and volume were similar, but Zone B
  replenishment was not changed.

For every improvement recommendation, distinguish observation, evidence,
inference, root cause, recommendation, expected effect, and measurement plan.
Do not approve staffing changes, discipline, capital spend, layout changes,
customer commitments, financial postings, safety controls, labor standards, or
live WMS/LMS/WCS/WES/TMS/ERP/BI configuration.
```

Acceptance checks:

- Output invokes all thirteen AL-13 priority skills.
- KPI set maps metrics to decisions, definitions, units, sources, owners, cadence, targets, and action thresholds.
- Scorecard design separates leading, lagging, diagnostic, and balancing metrics.
- Warehouse KPI analysis calculates variance to target and baseline movement without treating KPI movement alone as root cause.
- Throughput analysis uses output quantity divided by elapsed or productive time with units, timeframe, exclusions, and source notes.
- Throughput-loss diagnosis identifies lost output drivers and labels source gaps.
- Bottleneck finding distinguishes the limiting process step from symptoms, temporary disruptions, and downstream effects.
- Root-cause analysis distinguishes observation, evidence, inference, root cause, recommendation, expected effect, and measurement plan.
- Pareto analysis sorts issue categories, calculates share and cumulative share, and does not claim cause from ranking alone.
- Warehouse process map identifies physical steps, systems, queues, handoffs, controls, rework, and exceptions.
- Waste analysis identifies waiting, walking, blocked lanes, rework, defects, excess WIP, and manual batch posting where supported.
- Scenario comparison uses a common baseline, compatible assumptions, expected KPI effects, risks, and measurement plan.
- Improvement plan includes owners or owner gaps, dependencies, controls, risks, approvals, expected effect, and measurement plan.
- Result measurement separates observed before-after change from causal proof and checks guardrails such as overtime, order mix, and volume.
- Recommendations are planning support and do not approve staffing, discipline, capital spend, layout changes, customer commitments, financial postings, safety controls, labor standards, or live system configuration.

Risk and review notes:

- KPI and throughput claims require source definitions, units, timeframe, and baseline visibility.
- Causal claims require process evidence and must not be inferred from correlation, trend movement, or Pareto ranking alone.
- Financially material, customer-critical, labor-sensitive, safety-relevant, regulated, audit, or production-system decisions require qualified review.
