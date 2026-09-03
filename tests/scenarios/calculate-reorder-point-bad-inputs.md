# Calculate Reorder Point Bad Inputs

Category: `bad_inputs`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
Calculate the reorder point with average demand of -5 units per day, lead time
of 4 days, and safety stock of 20 units.
```

Acceptance checks:

- Rejects negative average demand.
- Does not return a final reorder point.
- Asks for corrected demand input.

Risk and review notes:

- Tests invalid numeric input rejection.
