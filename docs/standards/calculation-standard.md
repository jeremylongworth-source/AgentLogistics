# AgentLogistics Calculation Standard

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY
```

## Purpose

Calculation skills must produce numeric outputs that are transparent,
unit-aware, and reviewable by logistics operators.

## Required Calculation Contract

Every calculation skill must define:

- formula name;
- purpose of the formula;
- variables and units;
- required inputs;
- optional inputs that affect interpretation;
- allowed unit conversions;
- rounding rules;
- validation rules;
- intermediate values to show;
- final output format;
- worked examples;
- edge cases and exception behavior.

## Unit Handling

The skill must:

- preserve the user's original units in the output;
- normalize units before calculating;
- show the normalization step when units differ;
- reject incompatible units;
- avoid silent conversion between weight, volume, length, count, currency, and
  time;
- state when mixed units require item-master, case-pack, pallet, or dimensional
  conversion data.

## Formula Handling

The skill must:

- name the formula before applying it;
- define each variable before calculating;
- show intermediate values for review;
- separate the mathematical result from operational recommendations;
- avoid using hidden constants;
- state when a formula is a simplification and what it excludes.

## Rounding And Precision

Define rounding before returning the final answer:

- Use exact arithmetic or enough decimal precision for intermediate values.
- Round only the final operational threshold unless the formula requires
  stepwise rounding.
- Round countable inventory, orders, pallets, cartons, people, dock doors, and
  equipment to operationally valid whole quantities.
- Preserve fractional values for rates, utilization percentages, cost per unit,
  and durations unless a local policy requires a whole number.
- Name any rounding policy such as ceiling, nearest whole unit, order multiple,
  or minimum order quantity.

## Validation Rules

Calculation skills must check:

- missing required inputs;
- negative values where impossible;
- zero values where they change interpretation;
- mismatched units;
- stale or non-representative data periods;
- outlier values;
- contradictory source records;
- formulas applied outside their assumptions.

If validation fails, do not force a final numeric result. Return the partial
calculation that is valid and identify the missing or invalid input.

## Sensitivity

When a result depends heavily on an assumption, show the sensitivity or call it
out. Examples:

- a reorder point driven mostly by safety stock;
- capacity results constrained by aisle or clearance assumptions;
- labor requirements driven by unverified productivity rates;
- freight charges driven by disputed accessorial rules.

## Testing

Each calculation skill must include at least:

- one straightforward worked example;
- one unit-conversion example;
- one missing-input or invalid-input example;
- one rounding example when the output is operationally countable.

Expected outputs must include intermediate values, final values, and units.
