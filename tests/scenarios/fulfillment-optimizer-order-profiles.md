# Fulfillment Optimizer Order Profiles

Category: `fulfillment_optimization_order_profiles`

Expected routing:

- `analyze-order-profile`
- `plan-forward-pick-storage`
- `plan-replenishment`
- `calculate-replenishment-demand`
- `prioritize-replenishment`
- `select-picking-strategy`
- `plan-picking-wave`
- `plan-batch-picking`
- `plan-zone-picking`
- `optimize-pick-path`
- `calculate-pick-productivity`
- `analyze-pick-accuracy`
- `diagnose-picking-bottleneck`
- `investigate-picking-error`
- `plan-packing-operation`
- `plan-cartonization`
- `plan-shipping-stage`
- `plan-trailer-loading`
- `verify-outbound-shipment`
- `investigate-shipping-error`

Prompt:

```text
We need a review-ready fulfillment optimization plan for tomorrow's outbound work. Do not change any live WMS, OMS, TMS, inventory, carrier, labor, or financial records. Do not present load securement, carrier, legal, dangerous-goods, equipment, traffic, or safety approval.

Order profile mix:

- Low-volume/high-SKU: 42 wholesale orders, 690 unique SKUs, mostly one line each, due by 16:00.
- High-volume/low-SKU: 18 promotional orders for 6 SKUs, 9,800 eaches total, due by 13:00.
- Ecommerce each-pick: 1,240 orders, 1.7 lines per order, mostly each-pick, carrier cutoff at 15:30.
- Case pick: 96 orders, 1,480 cases, replenishment from reserve is needed before the second wave.
- Pallet movement: 22 outbound pallet orders, 64 pallets total, staged by route and stop sequence.
- Mixed orders: 37 orders contain eaches, cases, and pallet lines with pack and stage split risk.

Operating facts:

- Forward pick has 14 SKUs projected to stock out before the ecommerce cutoff. Reserve has stock for 11 of them, but two reserve locations require reach equipment and one has a hold status in the WMS export.
- Pick productivity yesterday was 82 lines per labor hour for each-pick, 46 cases per labor hour for case pick, and 18 pallets per labor hour for pallet movement. Today has 9 pickers for 6.5 available hours, two case-pick drivers, and one loader after 14:00.
- The current pick strategy is single-order picking for ecommerce and route picking for wholesale. Travel observations show fast promo SKUs are split across three aisles, and batch opportunities exist for the ecommerce orders.
- The pack area has six stations. Carton data exists for small, medium, large, and bulk cartons, but item dimensions are missing for 11 percent of each-pick lines.
- Outbound staging has five route lanes. Two lanes are already holding delayed freight from today, so pallet movement and mixed orders may interfere with ecommerce parcel flow.
- Shipping has one reported issue from yesterday: order SO-9912 was picked complete, packed as two cartons, but the carrier scan shows only one carton accepted.

Build an optimization response that covers replenishment demand, replenishment priority, wave planning, batch picking, zone picking, pick-path considerations, pick productivity, pick accuracy, bottleneck diagnosis, picking-error investigation handoff, cartonization, packing/staging constraints, trailer loading, outbound verification, shipping-error investigation, and the six order profiles above. Show calculations only where the facts support them, list missing evidence, and separate review-required actions.
```

Acceptance checks:

- Covers all six required order profiles: low-volume/high-SKU, high-volume/low-SKU, ecommerce each-pick, case pick, pallet movement, and mixed orders.
- Calculates supported workload, labor, replenishment, carton, staging, loading, or productivity checks only from supplied facts.
- Routes stockout risk through replenishment demand and replenishment prioritization before wave release.
- Differentiates wave, batch, zone, and pick-path recommendations by order profile.
- Identifies pack, staging, trailer-loading, outbound-verification, and shipping-error handoffs.
- Treats the WMS hold status and missing item dimensions as constraints, not assumptions to override.
- Preserves carrier, load-securement, legal, regulatory, equipment, traffic, financial, labor, and safety review boundaries.

Risk and review notes:

- Synthetic scenario only. The case includes no private customer data or live system requirement. Site owner, supervisor, safety, carrier, finance, and qualified operations review may be required before operational use.
