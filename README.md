# AgentLogistics

AgentLogistics is an open-source AI skill repository for commercial logistics,
warehousing, storage, inventory movement, transportation, distribution,
material handling, logistics systems, and operational improvement.

The project is intended to make general-purpose AI agents better at structured
logistics work: identifying constraints, tracing operational evidence,
performing unit-aware calculations, separating universal practice from
jurisdiction-specific rules, and producing practical outputs for logistics
operators and managers.

## Status

AgentLogistics is in initial repository development.

Current completed gates:

- `AGENTLOGISTICS_AL_00_BASELINE_READY`
- `AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY`

The next planned wave is AL-02: Master Taxonomy Audit.

## Scope

The core project covers 13 domain families:

1. Logistics Fundamentals
2. Receiving and Inbound
3. Storage and Warehousing
4. Inventory Control
5. Replenishment and Picking
6. Packing, Staging and Shipping
7. Material Handling
8. Transportation and Freight
9. Warehouse Design and Capacity
10. Logistics Systems and Data
11. Performance and Continuous Improvement
12. Labor and Operational Planning
13. Returns and Reverse Logistics

Specializations such as Canada, United States, food logistics, cold chain,
dangerous goods, ecommerce, manufacturing, retail distribution, automotive,
pharmaceuticals, and international logistics should remain isolated from the
universal core until their sources, jurisdiction, and safety boundaries are
clear.

## Repository Layout

Current real content:

```text
AgentLogistics/
|-- docs/
|   |-- architecture/
|   `-- development/
|-- scripts/
|-- AGENTS.md
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
`-- ROADMAP.md
```

Planned content will add `skills/`, `skillsets/`, `specializations/`, `shared/`,
`tests/`, and additional validation tooling when those directories have real
content.

## Development Model

AgentLogistics follows a wave-based roadmap. Each wave must close as:

- `READY`
- `PARTIALLY_READY`
- `BLOCKED`

Unresolved work must be recorded explicitly before the next wave starts.

Run local validation with:

```powershell
.\scripts\validate-all.ps1
```

## Safety Boundary

AgentLogistics may help with safety planning, hazard identification, procedure
analysis, compliance research, inspection preparation, equipment-selection
analysis, and operational risk analysis.

It must not present AI-generated guidance as professional engineering approval,
equipment certification, operator certification, regulatory approval, legally
binding compliance advice, or a substitute for qualified professional review.

## License

MIT
