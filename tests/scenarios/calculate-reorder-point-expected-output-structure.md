# Calculate Reorder Point Expected Output Structure

Category: `expected_output_structure`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
For label roll SKU D, average demand is 18 rolls per day, lead time is 6 days,
safety stock is 40 rolls, on hand is 120 rolls, on order is 20 rolls, and 10
rolls are allocated. Calculate the reorder point and tell me whether to reorder.
```

Acceptance checks:

- Includes item scope, input values, normalized lead time, demand during lead
  time, safety stock, raw reorder point, rounded reorder point, assumptions, and
  validation notes.
- Calculates reorder point as 148 rolls.
- Calculates inventory position as 130 rolls.
- Returns reorder signal as yes.

Risk and review notes:

- Tests predictable output structure and optional inventory-position comparison.
