# AgentLogistics Tests

Completion token:

```text
AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY
```

## Layout

```text
tests/
|-- expected-routing.yaml
|-- evaluations/
|-- fixtures/
`-- scenarios/
```

## Current Coverage

The first test target is the AL-03 reference skill:

- `skills/inventory-control/calculate-reorder-point/`

The first end-to-end skillset target is:

- `skillsets/warehouse-operator/`

The inventory-control skillset target is:

- `skillsets/inventory-control-specialist/`

The warehouse-planning skillset target is:

- `skillsets/warehouse-planner/`

The fulfillment-optimization skillset target is:

- `skillsets/fulfillment-optimizer/`

The material-handling skillset target is:

- `skillsets/material-handling-analyst/`

The transportation skillset target is:

- `skillsets/transportation-coordinator/`

Coverage includes:

- routing scenarios for the AL-04 required categories;
- deterministic reorder-point calculation fixtures;
- missing-input, bad-input, unit-mismatch, ambiguity, safety, jurisdiction, and
  unsupported-assumption checks;
- a reference evaluation report;
- the AL-06 warehouse-operator receive-to-ship scenario and flow fixture.
- the AL-07 inventory discrepancy investigation scenario and fixture.
- the AL-08 warehouse-planner layout concept scenario and fixture.
- the AL-09 fulfillment-optimizer order-profile scenario and fixture.
- the AL-10 material-handling selection-analysis scenario and fixture.
- the AL-11 transportation-coordinator multimode scenario and fixture.

Run:

```powershell
.\scripts\validate-all.ps1
```
