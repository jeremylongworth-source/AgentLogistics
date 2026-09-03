# Warehouse Manager Labor Operating Plan

Category: `labor_operating_planning`

Expected routing:

- `forecast-warehouse-workload`
- `calculate-labor-requirements`
- `plan-warehouse-staffing`
- `balance-warehouse-workload`
- `analyze-labor-productivity`
- `analyze-overtime-requirements`
- `plan-shift-handoff`
- `build-daily-warehouse-plan`

Prompt:

```text
Prepare a warehouse manager labor and operating plan for next Monday at DC-07.
Use the provided planning evidence to forecast workload, calculate labor
requirements, propose staffing coverage, balance work across areas, analyze
labor productivity, analyze overtime risk, define shift handoff content, and
build the daily operating plan.

Evidence:
- Next Monday has 26 inbound POs, 18 inbound trailers, 710 pallets to receive,
  540 pallets to put away, 4,100 ecommerce orders, 980 wholesale cases, 21,800
  pick lines, 5,400 pack cartons, 115 replenishment moves, and 140 cycle counts.
- Service windows: ecommerce cutoff is 15:30, wholesale staging cutoff is 16:45,
  inbound detention risk begins after 13:00, and inventory count results must
  be reviewed before 20:00.
- Productivity standards supplied by operations: receiving 45 pallets per
  productive hour, putaway 32 pallets per productive hour, replenishment 20
  moves per productive hour, ecommerce picking 115 lines per productive hour,
  wholesale picking 82 lines per productive hour, packing 95 cartons per
  productive hour, shipping 60 pallets per productive hour, and cycle counting
  15 counts per productive hour.
- Available labor is 44 associates on day shift and 30 associates on evening
  shift. Day shift has 12 pick-only associates, 7 pack-only associates, 8
  receiving/putaway associates, 5 shipping associates, 4 cycle-count associates,
  and 8 flexible associates. Evening shift has 8 pick-only, 6 pack-only, 4
  receiving/putaway, 4 shipping, 2 cycle-count, and 6 flexible associates.
- Constraints: two pack benches are offline until maintenance clears them,
  three forklift operators are unavailable, the LMS report uses paid hours
  while the productivity standards use productive hours, and HR has not
  approved any overtime plan.
- The manager wants a review-ready plan with options and handoff content. Do
  not approve overtime, payroll, staffing changes, hiring, discipline, labor
  standards, wage-hour compliance, union interpretation, safety staffing,
  customer commitments, or live WMS/LMS/ERP/TMS/scheduling system changes.
```

Acceptance checks:

- Output invokes all eight AL-14 priority skills.
- Forecast, labor requirement, staffing, balancing, productivity, overtime, handoff, and daily operating plan outputs are all present.
- Calculations distinguish workload units, productivity rates, productive hours, paid hours, scheduled hours, break assumptions, and headcount rounding.
- Staffing and balancing logic account for skill mix, flexible labor, missing forklift operators, offline pack benches, service windows, and inventory-count deadline.
- Overtime analysis labels HR/payroll approval gaps and proposes review options without approval.
- Shift handoff content includes open work, exception owners, risks, next actions, and escalation triggers.
- Daily operating plan includes manager review cadence, communication points, constraints, priorities, and source gaps.
- Output blocks wage-hour, union, HR, safety, payroll, customer, financial, and live system approvals.

Risk and review notes:

- Labor-sensitive and production-impacting recommendations are planning support only.
- Scenario data is synthetic and must not require private employee records, credentials, or live connectors.
