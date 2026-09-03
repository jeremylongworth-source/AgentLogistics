# Calculate Reorder Point Calculation Correctness

Category: `calculation_correctness`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
Replacement part SKU B averages 140 units per week. The supplier lead time is
10 days and our approved safety stock is 90 units. Calculate the reorder point.
```

Acceptance checks:

- Converts 10 days to 10/7 weeks.
- Calculates demand during lead time as 200 units.
- Calculates raw reorder point as 290 units.
- Returns the final reorder point as 290 units.

Risk and review notes:

- Tests time-unit conversion and arithmetic correctness.
