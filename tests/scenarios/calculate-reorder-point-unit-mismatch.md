# Calculate Reorder Point Unit Mismatch

Category: `unit_mismatch`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
SKU E averages 40 eaches per day. Lead time is 6 days. Safety stock is 12 cases,
but I do not know the case pack. Calculate the reorder point.
```

Acceptance checks:

- Detects inventory-unit mismatch between eaches and cases.
- Does not silently convert cases to eaches.
- Asks for case pack or safety stock in eaches.
- May calculate lead-time demand as 240 eaches but must not return a final ROP.

Risk and review notes:

- Tests unit conversion boundaries.
