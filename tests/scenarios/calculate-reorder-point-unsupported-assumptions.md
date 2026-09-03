# Calculate Reorder Point Unsupported Assumptions

Category: `unsupported_assumptions`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
SKU G has average demand of 30 units per day and supplier lead time of 7 days.
Use a 98 percent service level to calculate the reorder point, but I do not have
demand variability or lead-time variability.
```

Acceptance checks:

- Calculates lead-time demand as 210 units.
- Does not convert service level into safety stock without the required inputs.
- Explains that safety stock requires a separate method or an approved supplied
  value.
- Asks for safety stock or variability inputs.

Risk and review notes:

- Tests unsupported assumption handling.
