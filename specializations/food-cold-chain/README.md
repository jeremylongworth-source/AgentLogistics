# Food Cold-Chain Specialization

Completion token: `AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY`

The food-cold-chain specialization provides source-backed logistics planning
support for food and temperature-sensitive food workflows. It is isolated from
the universal core because food and cold-chain requirements are product-specific
and jurisdiction-specific, and may involve qualified food safety, quality,
legal, regulatory, customer, carrier, equipment, or facility review.
AgentLogistics and ChefSkills independent boundaries are preserved; this
specialization creates no hard dependency on ChefSkills or any cross-project
artifact.

## Packages

- `classify-food-cold-chain-requirements`
- `plan-temperature-controlled-storage`
- `monitor-cold-chain-temperature`
- `triage-temperature-excursion`
- `plan-fefo-inventory-rotation`
- `manage-expiry-controlled-food-inventory`
- `trace-food-lot-movement`
- `plan-sanitation-sensitive-logistics`
- `plan-food-segregation`
- `support-food-recall-logistics`
- `plan-cold-chain-transportation`
- `plan-cold-chain-handoff`

## Source Rule

Use current official sources for regulatory claims. The source starting points
in `references/food-cold-chain-source-map.md` were verified on 2026-09-03 and
must be refreshed before operational use.

## Boundary

This specialization may produce research briefs, preparation checklists,
evidence requests, routing briefs, trace packets, temperature-monitoring
summaries, recall logistics packets, and qualified-review handoffs. It must not
provide legal advice, compliance declarations, food safety approvals, product
release approvals, temperature excursion disposition approvals, recall
initiation approvals, sanitation approvals, equipment certifications, carrier
approvals, customer commitment approvals, financial approvals, or live system
changes.
