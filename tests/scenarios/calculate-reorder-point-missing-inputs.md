# Calculate Reorder Point Missing Inputs

Category: `missing_inputs`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
SKU C averages 12 units per day and lead time is 5 days. What reorder point
should I use?
```

Acceptance checks:

- Calculates lead-time demand as 60 units.
- Does not invent safety stock.
- Asks for safety stock, service-policy inputs, or approval to assume zero
  safety stock.
- Labels the result as partial until safety stock is supplied.

Risk and review notes:

- Tests missing required input handling.
