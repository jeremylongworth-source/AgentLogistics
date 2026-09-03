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

Coverage includes:

- routing scenarios for the AL-04 required categories;
- deterministic reorder-point calculation fixtures;
- missing-input, bad-input, unit-mismatch, ambiguity, safety, jurisdiction, and
  unsupported-assumption checks;
- a reference evaluation report;
- the AL-06 warehouse-operator receive-to-ship scenario and flow fixture.

Run:

```powershell
.\scripts\validate-all.ps1
```
