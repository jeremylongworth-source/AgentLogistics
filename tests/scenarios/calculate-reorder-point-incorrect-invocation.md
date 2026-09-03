# Calculate Reorder Point Incorrect Invocation

Category: `incorrect_invocation`

Expected routing:

No AgentLogistics skill should route directly.

Prompt:

```text
Build me a full min-max replenishment policy for every item in my warehouse,
including economic order quantity and service-level safety stock targets.
```

Acceptance checks:

- Does not treat reorder point calculation as sufficient for the whole request.
- Identifies that safety stock, EOQ, and min-max policy require other skills or
  broader analysis.
- Offers a scoped handoff instead of forcing a reorder point answer.

Risk and review notes:

- Prevents over-triggering when a request contains adjacent inventory concepts.
