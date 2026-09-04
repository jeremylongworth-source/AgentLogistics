# Integration Scenario D: Capacity Constraint

Category: `integration_capacity_constraint`

Expected routing:

- `classify-storage-requirements`
- `calculate-storage-capacity`
- `calculate-pallet-positions`
- `calculate-cube-utilization`
- `analyze-storage-utilization`
- `plan-reserve-storage`
- `plan-forward-pick-storage`
- `slot-warehouse-inventory`
- `analyze-slotting-efficiency`
- `optimize-storage-density`
- `evaluate-racking-strategy`
- `forecast-capacity-requirements`
- `analyze-space-utilization`
- `plan-warehouse-zones`
- `plan-dock-capacity`
- `analyze-warehouse-flow`
- `identify-warehouse-congestion`
- `design-conceptual-warehouse-layout`
- `compare-warehouse-layouts`
- `plan-warehouse-expansion`
- `classify-food-cold-chain-requirements`
- `plan-temperature-controlled-storage`

Prompt:

A food distribution center expects 22 percent inventory growth, has 91 percent
reserve occupancy, 74 percent cube utilization, blocked cross-aisles near
freezer staging, insufficient dock doors on Mondays, and rising travel time for
fast-moving chilled SKUs. Build an integration evaluation output connecting
inventory, pallet positions, storage utilization, slotting, throughput, dock
capacity, growth forecast, and capacity recommendation. Do not approve
structural rack changes, building expansion, food safety release, capital
spend, labor commitments, customer commitments, or live WMS changes.

Acceptance checks:

- Routes across storage, warehouse design and capacity, fulfillment planning,
  food cold-chain, and material handling boundaries where relevant.
- Separates storage requirement class, current capacity, utilization, slotting,
  congestion, dock capacity, forecast, alternatives, assumptions, and
  recommendation logic.
- Shows calculation inputs and unit checks where capacity, cube, utilization,
  growth, or dock capacity are used.
- Preserves structural, food safety, capital, labor, and system-change review
  boundaries.

Risk and review notes:

- Structural engineering, rack certification, food safety, capital approvals,
  labor commitments, customer promises, and live system changes require
  qualified review.
