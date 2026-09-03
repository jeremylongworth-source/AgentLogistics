# Specialization Framework Roadmap

Category: `specialization_framework`

Expected routing: []

Prompt:

Create an extension framework for AgentLogistics specializations without
building the specialization packages yet. Evaluate cold-chain, food-logistics,
dangerous-goods, ecommerce, manufacturing, retail-distribution, automotive,
pharmaceuticals, and international-logistics by domain need, unique knowledge,
unique regulations, unique workflows, shared core skills, new atomic skills
required, and priority.

Acceptance checks:

- Produces `docs/architecture/specialization-roadmap.md`.
- Evaluates all nine AL-19 candidate specializations.
- Keeps universal core skills independent from specialization packages.
- Identifies shared core skills before proposing new atomic specialized skills.
- Prioritizes food-logistics and cold-chain as the AL-20 entry point.
- Blocks regulatory, safety, customs, HR, financial, certification, and live
  system decisions pending qualified review and source maps.

Risk and review notes:

- This is architecture planning, not specialization implementation.
- Candidate skill names are proposals until a later wave creates and validates
  real packages.
