# Contributing

AgentLogistics welcomes focused contributions that improve commercial logistics
reasoning, skill quality, source discipline, validation, and public
documentation.

Before proposing large changes, read:

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/master-taxonomy-v1.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/calculation-standard.md`
- `docs/standards/testing-standard.md`

## Contribution Priorities

- Prefer atomic logistics skills over broad textbook-style content.
- Map every new skill to one primary domain family.
- Compose professional roles in `skillsets/`; do not duplicate atomic skill
  procedures inside role packages.
- Keep universal logistics guidance separate from jurisdiction-specific,
  industry-specific, or mode-specific content.
- Include authoritative sources for standards, regulations, safety-sensitive
  claims, and quantitative methods.
- Add or update scenarios, fixtures, evaluations, and validators when behavior
  changes.
- Preserve AgentLogistics independence from AgentSkills, ChefSkills, and any
  other repository unless an explicit architecture decision creates a boundary.

## Skill Contributions

New skill packages should follow this shape when supporting files are needed:

```text
skills/<domain>/<skill-name>/
|-- SKILL.md
|-- agents/openai.yaml
`-- references/
```

Every skill must define:

- trigger and non-trigger boundaries;
- required and optional inputs;
- assumptions and missing-input behavior;
- procedure;
- calculation requirements when applicable;
- validation expectations;
- source usage expectations;
- output contract;
- safety, regulatory, approval, and escalation boundaries.

Do not create empty folders to reserve future structure. Add directories only
when they contain real content.

## Evidence And Sources

Use primary and authoritative sources whenever possible. For regulatory or
safety-sensitive material, record:

- authority;
- jurisdiction;
- applicability;
- source URL;
- access or verification date;
- whether the requirement may change over time;
- what skill, specialization, or reference uses the source.

Do not copy large blocks of source text. Summarize the operational requirement,
preserve provenance, and keep jurisdiction-specific rules isolated in
`specializations/`.

## Calculations

Calculation-oriented skills must show the math. Include:

- variables;
- units;
- formula;
- assumptions;
- required inputs;
- missing-input behavior;
- edge cases;
- output interpretation;
- at least one worked test case.

Validate unit compatibility explicitly.

## Safety Boundaries

AgentLogistics may support planning, research, analysis, and operational
decision preparation. It must not claim to provide:

- legal advice;
- engineering approval;
- equipment certification;
- operator certification;
- regulatory approval;
- dangerous-goods classification approval;
- food safety release;
- customs entry approval;
- financial approval;
- customer commitment approval;
- live system authorization.

Safety-sensitive changes require qualified review by the appropriate
professional, authority, owner, or accountable operator.

## Local Checks

Run the full validation wrapper before submitting a pull request:

```powershell
.\scripts\validate-all.ps1
```

Expected result:

```text
All AgentLogistics validation checks passed.
```

For targeted checks, use the scripts in `scripts/`:

```powershell
python scripts\validate-docs.py
python scripts\validate-skills.py
python scripts\validate-skillsets.py
python scripts\validate-specializations.py
python scripts\validate-tests.py
```

## Pull Request Checklist

A useful pull request should state:

- which roadmap wave it advances;
- which domain family, skillset, specialization, or public document it touches;
- which artifacts changed;
- what source material was used;
- what validation was run;
- any known limitations, assumptions, unresolved risks, or follow-up work.

For public-readiness work, include whether `README.md`, `CONTRIBUTING.md`,
`CHANGELOG.md`, `SECURITY.md`, issue templates, pull request templates, and
release notes need updates.

## Issues

Open an issue when:

- a skill trigger is unclear;
- a logistics procedure is incomplete or too broad;
- a calculation is missing inputs, units, edge cases, or a worked example;
- a source is stale, weak, jurisdiction-mixed, or missing;
- a safety or approval boundary is too broad;
- a scenario, fixture, or validator does not cover expected behavior.

Do not include secrets, credentials, customer data, shipment data, facility
layouts, personnel records, or other sensitive operational details in public
issues.
