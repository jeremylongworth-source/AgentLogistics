# Calculate Reorder Point Correct Invocation

Category: `correct_invocation`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
For SKU A, average demand is 25 cases per day, supplier lead time is 8 days, and
approved safety stock is 60 cases. Calculate the reorder point and show the
calculation.
```

Acceptance checks:

- Uses the reorder point formula.
- Shows demand during lead time.
- Adds safety stock.
- Returns the result in cases.
- States the rounding policy.

Risk and review notes:

- Low-risk inventory planning example with no regulated product claim.
