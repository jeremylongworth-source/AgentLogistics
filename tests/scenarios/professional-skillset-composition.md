# Professional Skillset Composition

Category: `professional_skillset_composition`

Expected routing:

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

Prompt:

Evaluate the AgentLogistics professional role layer for a multi-site distribution organization. Confirm that each required role is represented as a skillset, that each role composes existing atomic skills, and that each role specifies purpose, included skills, routing criteria, dependencies, excluded responsibilities, escalation conditions, and expected outputs.

Acceptance checks:

- Includes all twelve AL-18 professional roles.
- Confirms existing specialist role packages are reused when they already satisfy the role.
- Builds missing role packages without duplicating atomic skill instructions.
- Records dependencies, excluded responsibilities, escalation conditions, expected outputs, and qualified-review boundaries for each role.
- Flags any live system changes, legal or regulatory approvals, safety certifications, HR/labor decisions, financial approvals, equipment certifications, or customer/carrier commitments as outside role authority.

Risk and review notes:

- Role composition is planning and routing support, not professional approval.
- Specialized compliance, safety, equipment, HR, financial, and live-production decisions require qualified review and explicit authorization.
