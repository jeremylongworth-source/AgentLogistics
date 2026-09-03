# Receiving Specialist Professional Role Scenario

Category: `professional_skillset_composition`

Expected routing:

- `receiving-specialist`

Prompt:

You are given a mixed logistics request that belongs to the receiving specialist role. Compose the existing AgentLogistics atomic skills for the role, identify source records and missing evidence, separate planning support from approvals, and return the expected role outputs with escalation conditions.

Acceptance checks:

- Routes to `receiving-specialist` as a professional skillset.
- Uses only existing AgentLogistics atomic skills from the skillset manifest.
- States purpose, included skills, routing criteria, dependencies, excluded responsibilities, escalation conditions, and expected outputs.
- Labels live system changes, approvals, certifications, compliance determinations, financial commitments, and labor decisions as outside the role authority.
- Produces source-backed handoffs, evidence gaps, metrics or calculations, and qualified-review boundaries.

Risk and review notes:

- Professional role composition must not create new atomic procedures or bypass specialist packages.
- Qualified review is required for legal, regulatory, safety, HR, financial, equipment, engineering, carrier-contract, customer-commitment, or live-system decisions.
