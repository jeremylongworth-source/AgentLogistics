# Inventory State Terms

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## Purpose

Use this glossary to keep inventory-control skills consistent when they discuss
stock state, demand, lead time, and replenishment policy.

## Core Terms

| Term | Meaning |
|---|---|
| `SKU` | Stock keeping unit. A specific inventory identifier controlled by the operation. |
| `item group` | A set of SKUs treated together for analysis, policy, or planning. |
| `inventory unit` | The unit in which stock is counted for the calculation or decision. |
| `average demand` | Representative demand rate for a selected planning period. |
| `lead time` | Elapsed time from replenishment trigger or order release to usable inventory availability. |
| `demand during lead time` | Expected demand over the replenishment lead-time window. |
| `safety stock` | Extra inventory held above expected lead-time demand to buffer uncertainty or service risk. |
| `reorder point` | Inventory-position threshold that signals replenishment should be considered or triggered. |
| `on hand` | Inventory physically or systemically available at the operation before reservations. |
| `on order` | Inventory already ordered or replenishment already released but not yet available. |
| `allocated` | Inventory reserved for known demand and not freely available. |
| `backordered` | Demand already due or committed when inventory is not available. |
| `inventory position` | Planning quantity calculated as on hand plus on order minus allocated or backordered quantity. |
| `minimum order quantity` | Smallest order quantity allowed by supplier, system, or policy. |
| `order multiple` | Required ordering increment such as case, layer, pallet, or pack multiple. |

## Replenishment Distinctions

The reorder point is a trigger level. It is not the same as:

- safety stock;
- order quantity;
- economic order quantity;
- minimum order quantity;
- maximum stock level;
- forecast demand;
- service-level target.

When the user asks for a complete replenishment policy, route beyond a single
reorder point calculation.

## Inventory Position Formula

Use this planning convention when all fields are available:

```text
inventory position = on hand + on order - allocated/backordered
```

If the local operation distinguishes allocated and backordered separately, state
the exact fields used.

If open replenishment is uncertain, delayed, blocked, or not confirmed, label
the inventory-position comparison as approximate.

## Evidence Checks

Before relying on an inventory-state input, ask whether:

- the quantity came from a WMS, ERP, count, spreadsheet, or estimate;
- the unit of measure matches the item master;
- open orders are confirmed and expected within lead time;
- allocated and backordered quantities are included or excluded;
- demand history includes abnormal events such as promotions, shutdowns, stockouts,
  substitutions, or launches.
