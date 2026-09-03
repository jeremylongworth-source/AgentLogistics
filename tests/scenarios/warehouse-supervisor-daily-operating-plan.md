# Warehouse Supervisor Daily Operating Plan

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
Build tomorrow's warehouse supervisor daily operating plan for DC-05 first and
second shift. Use the supplied evidence to forecast workload, calculate labor
requirements, plan staffing, balance workload by area, analyze labor
productivity, analyze overtime exposure, plan the shift handoff, and build the
daily warehouse plan.

Evidence:
- Planning date is 2026-09-04. First shift runs 06:00-14:30 with two 15-minute
  breaks and one 30-minute lunch. Second shift runs 14:30-23:00 with the same
  break pattern.
- Forecast inbound work is 14 trailers, 620 pallets, and 2,400 received cases.
  Outbound work is 3,200 orders, 18,600 order lines, 24,500 picked units, and
  4,850 cartons. Inventory work is 95 cycle counts and 180 replenishment moves.
- Backlog carryover is 620 order lines, 220 cartons waiting at pack, and 38
  putaway pallets over 24 hours old.
- Productivity evidence: receiving 42 pallets per productive labor hour,
  putaway 34 pallets per productive labor hour, replenishment 18 moves per
  productive labor hour, picking 105 lines per productive labor hour, packing
  92 cartons per productive labor hour, shipping 58 pallets per productive
  labor hour, and cycle count 16 counts per productive labor hour.
- Available staffing is 32 associates on first shift and 24 associates on
  second shift. Four associates are cross-trained for receiving and putaway,
  six for pick and pack, two for cycle count, and only one shipping lead is
  available after 18:00.
- Constraints: carrier cutoff at 17:00 for priority customer ORD-RED, two dock
  doors are reserved for inbound until 11:00, one forklift is down, printer P3
  has intermittent failures, and Zone C replenishment must complete before the
  12:00 wave.
- Management wants options if overtime is required, but do not approve
  overtime, payroll, staffing changes, hiring, discipline, labor standards,
  wage-hour compliance, union interpretation, safety staffing, or live WMS/LMS/
  scheduling system changes.
```

Acceptance checks:

- Output invokes all eight AL-14 priority skills.
- Workload forecast separates inbound, outbound, inventory work, backlog, exceptions, units, planning date, and shift windows.
- Labor requirement calculation converts workload into productive labor hours with productivity-rate units and visible assumptions.
- Staffing plan separates required labor from available labor by shift, skill, area, supervisor coverage, breaks, and indirect time.
- Workload balancing addresses receiving, putaway, replenishment, picking, packing, shipping, cycle counting, dock doors, forklift constraint, printer risk, and priority customer cutoff.
- Labor productivity analysis keeps paid time, scheduled time, productive time, output unit, standard, target, baseline, and source records distinct.
- Overtime analysis calculates exposure as required hours minus available scheduled hours and labels approval boundaries.
- Shift handoff includes open work, exceptions, owners, risks, timestamps, and next actions.
- Daily plan integrates inbound, outbound, inventory, labor, constraints, priorities, escalation triggers, communication points, and handoffs.
- Output blocks staffing approval, payroll approval, labor discipline, wage-hour or union-contract interpretation, safety or regulatory approval, and live system changes.

Risk and review notes:

- Labor, wage-hour, union, payroll, HR, staffing, safety, customer, and production-system decisions require qualified review.
- Scenario data is synthetic and must not require live systems, credentials, or private employee records.
