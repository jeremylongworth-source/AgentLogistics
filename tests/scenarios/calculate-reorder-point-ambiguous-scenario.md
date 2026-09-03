# Calculate Reorder Point Ambiguous Scenario

Category: `ambiguous_scenario`

Expected routing:

- `calculate-reorder-point`

Prompt:

```text
We sell about 100 units a week for SKU F, but demand spikes during promotions and
the supplier lead time is usually around one or two weeks. What reorder point
should I use?
```

Acceptance checks:

- Identifies ambiguous lead time and non-representative demand.
- Requests a planning lead time and safety stock or approved assumptions.
- Avoids presenting a single precise threshold as final.
- Provides a partial structure for what can be calculated once inputs are fixed.

Risk and review notes:

- Tests uncertainty and assumption handling.
