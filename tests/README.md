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

The logistics-systems skillset target is:

- `skillsets/logistics-systems-analyst/`

The continuous-improvement skillset target is:

- `skillsets/continuous-improvement-specialist/`

The warehouse-supervisor skillset target is:

- `skillsets/warehouse-supervisor/`

The warehouse-manager skillset target is:

- `skillsets/warehouse-manager/`

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
- the AL-12 logistics-systems-analyst integration data-quality scenario and
  fixture.
- the AL-13 continuous-improvement-specialist performance review scenario and
  fixture.
- the AL-14 warehouse-supervisor daily operating plan scenario and fixture.
- the AL-14 warehouse-manager labor operating plan scenario and fixture.

Run:

```powershell
.\scripts\validate-all.ps1
```
