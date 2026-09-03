# Common Units

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## Purpose

Use this glossary to normalize unit language across AgentLogistics skills.

Skills must preserve the user's original units, convert only compatible units,
and state the conversion basis before calculating.

## Unit Families

| Family | Examples | Conversion Boundary |
|---|---|---|
| Count | each, unit, case, inner, pack, carton, pallet, roll, kit | Convert only with item-master or user-supplied pack hierarchy. |
| Time | hour, day, week, month, quarter, year | Convert only when the planning calendar is clear. |
| Weight | ounce, pound, gram, kilogram, ton, tonne | Convert within weight units after confirming system of measure. |
| Volume | cubic inch, cubic foot, cubic meter, liter | Convert within volume units after confirming dimensions or cube basis. |
| Length | inch, foot, millimeter, centimeter, meter | Convert within length units after confirming measurement orientation. |
| Currency | USD, CAD, EUR, GBP, local currency | Do not convert without a dated exchange-rate source. |

## Count Unit Hierarchy

Use these terms consistently:

- `each`: the smallest normally stocked or sold inventory unit.
- `inner`: a sub-pack inside a case or carton.
- `case`: a shipping or handling pack containing one or more eaches or inners.
- `carton`: a package used for shipping or storage; confirm whether it equals a
  case before converting.
- `pallet`: a logistics handling unit that may contain cases, cartons, eaches,
  or mixed goods.
- `kit`: a grouped item that may contain multiple components; do not assume one
  kit equals one each unless the user states that policy.

## Time Basis

Use explicit time bases for rates:

- `per hour`
- `per day`
- `per week`
- `per month`
- `per year`

Do not silently convert months or years to days when calendar basis matters.
Ask whether to use calendar days, working days, fiscal periods, or a fixed
planning period.

## Rounding Terms

- `raw result`: numeric output before operational rounding.
- `whole-unit result`: raw result rounded up when the inventory unit is
  countable.
- `operating threshold`: result rounded to a stated case pack, pallet multiple,
  order multiple, minimum order quantity, or local policy.
- `ceil`: round up to avoid falling below the calculated threshold.
- `nearest`: round to the nearest unit only when local policy allows it.

## Validation Rules

Before calculation, check:

- unit family compatibility;
- pack hierarchy when converting between eaches, inners, cases, cartons, kits,
  and pallets;
- time basis for demand, lead time, throughput, and labor rates;
- whether fractional outputs are operationally valid;
- whether the user supplied enough data to convert units safely.
