# Reorder Point Formula

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## Purpose

This is the canonical AgentLogistics formula reference for basic reorder point
calculations.

## Formula

```text
ROP = (D * L) + SS
```

Variables:

- `ROP`: reorder point in inventory units.
- `D`: average demand rate in inventory units per time unit.
- `L`: replenishment lead time converted to the same time unit as `D`.
- `SS`: safety stock in inventory units.

Expanded:

```text
demand during lead time = average demand rate * normalized lead time
reorder point = demand during lead time + safety stock
```

## Inventory Position Comparison

When current inventory facts are available:

```text
inventory position = on hand + on order - allocated/backordered
reorder signal = inventory position <= reorder point
```

This comparison is optional. A reorder point can be calculated without current
inventory position.

## Required Inputs

For a final reorder point:

- average demand rate;
- demand inventory unit;
- demand time unit;
- replenishment lead time;
- lead-time unit;
- safety stock quantity;
- safety-stock inventory unit.

For an inventory-position comparison:

- on-hand quantity;
- on-order quantity;
- allocated or backordered quantity.

## Validation Rules

- Demand, lead time, and safety stock must be numeric.
- Negative demand, lead time, or safety stock invalidates the calculation.
- Demand unit and safety-stock unit must match or have an explicit pack
  conversion.
- Lead-time unit must convert to the demand time unit.
- Missing safety stock blocks a final reorder point unless the user explicitly
  approves a zero safety-stock assumption.
- Seasonal, sparse, promotional, or disrupted demand should be flagged as a
  representativeness risk.

## Rounding

Report both raw and rounded results when rounding changes the value.

For countable inventory, use ceiling rounding unless the user supplies another
approved policy.

If a case pack, order multiple, or minimum order quantity is supplied, separate
the reorder point from any rounded operating threshold or order-quantity
recommendation.

## Limits

This formula does not calculate safety stock, economic order quantity, forecast
demand, min-max levels, supplier reliability, expiry risk, substitution logic, or
regulated availability requirements.

Use it as a planning calculation, not as a service guarantee.
