# Shared Logistics Foundations

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## Purpose

The `shared/` tree stores reusable logistics references that would otherwise be
duplicated across skills.

Shared files are accepted only when they have an active consumer. A consumer can
be a skill, test fixture, standard, validator, or implementation handoff that
references the shared file directly.

## Current Foundations

| File | Purpose | Active Consumer |
|---|---|---|
| `shared/glossaries/common-units.md` | Common unit families, conversion boundaries, and rounding terms. | `skills/inventory-control/calculate-reorder-point/SKILL.md` |
| `shared/glossaries/inventory-state-terms.md` | Inventory control terms used by reorder-point and future inventory skills. | `skills/inventory-control/calculate-reorder-point/SKILL.md` |
| `shared/formulas/reorder-point.md` | Canonical reorder-point formula and inventory-position comparison. | `skills/inventory-control/calculate-reorder-point/references/reorder-point-formula.md` |
| `shared/schemas/reorder-point-calculation.schema.json` | Structured fixture schema for reorder-point calculation cases. | `tests/fixtures/calculate-reorder-point-cases.json` |
| `shared/templates/calculation-output.md` | Reusable calculation answer shape for skill output contracts. | `skills/inventory-control/calculate-reorder-point/SKILL.md` |

## Authoring Rules

- Add shared content only when at least one current artifact references it.
- Keep shared material domain-neutral enough for reuse.
- Keep skill-specific procedures inside the skill package.
- Keep jurisdiction-specific rules out of shared universal foundations.
- Prefer small shared files with clear ownership over large catch-all documents.
- Update `scripts/validate-shared.py` when a new shared file becomes required.
