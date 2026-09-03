# AgentLogistics Professional Skillsets

Completion token: `AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY`

AL-18 composes existing atomic AgentLogistics skills into professional logistics roles. These skillsets provide role-level routing, dependencies, excluded responsibilities, escalation conditions, and expected outputs without duplicating the underlying skill instructions.

## Required Roles

- `warehouse-operator`
- `receiving-specialist`
- `inventory-control-specialist`
- `warehouse-supervisor`
- `warehouse-manager`
- `logistics-coordinator`
- `transportation-coordinator`
- `warehouse-planner`
- `distribution-manager`
- `logistics-systems-analyst`
- `continuous-improvement-specialist`
- `logistics-operations-manager`

## Composition Gate

- Professional skillsets must compose existing atomic skills from `skills/`.
- Role packages must not add hidden procedures, hidden approvals, or new regulatory conclusions.
- Role outputs must preserve evidence boundaries, source gaps, owner handoffs, escalation conditions, and qualified-review requirements.
- Existing specialist skillsets remain valid and are referenced by the AL-18 composition fixture when they already satisfy a professional role.

## Validation

Run:

```powershell
.\scripts\validate-all.ps1
```
