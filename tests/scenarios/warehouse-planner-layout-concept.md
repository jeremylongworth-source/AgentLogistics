# Warehouse Planner Layout Concept

Category: `warehouse_planning_layout`

Expected routing:

- `analyze-product-flow`
- `analyze-order-profile`
- `classify-inventory`
- `calculate-inventory-turns`
- `classify-storage-requirements`
- `select-storage-system`
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
- `analyze-product-affinity`
- `optimize-pick-path`
- `calculate-warehouse-capacity`
- `forecast-capacity-requirements`
- `analyze-space-utilization`
- `plan-warehouse-zones`
- `plan-dock-capacity`
- `analyze-warehouse-flow`
- `identify-warehouse-congestion`
- `design-conceptual-warehouse-layout`
- `compare-warehouse-layouts`
- `plan-warehouse-expansion`

Prompt:

```text
We need a review-ready warehouse planning concept for a lease renewal decision. Do not present this as structural engineering, rack, fire, floor-load, egress, permit, or safety approval.

Facility and operating facts:

- The building is 80,000 square feet with 28 feet clear height. Current usable storage footprint is estimated at 52,000 square feet after offices, battery charging, damaged-goods cage, and dock staging are excluded.
- Current storage includes 3,800 pallet positions, 3,250 occupied positions, 420 bulk floor positions, and 260 shelf/bin locations. The location master says 180 pallet positions are blocked, but the floor walk says only 95 are blocked.
- The operation handles 8,500 SKUs. About 2,100 SKUs move weekly. Ecommerce each-pick orders are 62 percent of order lines, wholesale case or pallet orders are 38 percent, and peak season adds about 35 percent more order lines for 10 weeks.
- Fast movers are currently slotted in the back third of the building. Packing is near shipping docks, but replenishment from reserve crosses the main outbound staging lane.
- Order history shows SKUs AL-BOLT-02 and AL-WASHER-02 are co-picked on 31 percent of ecommerce orders, but they are 470 travel feet apart. Heavy cases are stored in upper bin shelving near the forward pick area.
- Inbound averages 24 trailers per day with 70 minutes dock time. Outbound averages 31 trailers per day with 52 minutes dock time. There are 18 dock doors, but 4 are frequently used for staged overflow.
- The owner is considering three options: keep selective rack and reslot, add denser reserve storage, or redesign zones with a larger forward pick module and separate replenishment path.

Build a planning response that covers storage-system selection, pallet positions, cube utilization, storage density, forward versus reserve allocation, slotting, SKU velocity, product affinity, travel-distance considerations, warehouse capacity, dock capacity, congestion, zoning, conceptual layout reasoning, layout comparison, expansion triggers, missing evidence, and review boundaries.
```

Acceptance checks:

- Covers storage-system selection, pallet positions, cube utilization, density, forward and reserve allocation, slotting, SKU velocity, product affinity, travel distance, capacity, dock capacity, congestion, zoning, and conceptual layout reasoning.
- Uses the conflicting blocked-position records as source conflicts instead of averaging them without explanation.
- Calculates only values supported by the prompt and asks for missing dimensions, cube, rack, aisle, and cost data before unsupported outputs.
- Separates fast-mover, affinity, heavy-item, replenishment-crossing, and dock-overflow issues into traceable planning findings.
- Compares the three owner options without hiding structural, rack, fire, floor-load, egress, permit, lease, capital, or safety review boundaries.
- Produces a review-ready conceptual planning artifact, not a final engineered layout.

Risk and review notes:

- Synthetic scenario only. The case includes no private customer data or live system requirement. Site owner, safety, engineering, rack vendor, fire, finance, legal, and facility review may be required before operational use.
