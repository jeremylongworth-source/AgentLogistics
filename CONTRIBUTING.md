# Contributing

AgentLogistics is built in roadmap waves. Before proposing large new content,
read `ROADMAP.md`, `docs/architecture/domain-contract.md`, and
`docs/architecture/scope-boundaries.md`.

## Contribution Priorities

- Prefer atomic logistics skills over broad textbook-style content.
- Map every new skill to one primary domain family.
- Keep jurisdiction-specific regulatory material isolated under the relevant
  specialization.
- Include sources for standards, regulations, safety-sensitive claims, and
  quantitative methods.
- Add tests or evaluation scenarios when behavior changes.

## Local Checks

Run:

```powershell
.\scripts\validate-all.ps1
```

The current validation is intentionally small because this repository is in its
initial architecture stage. It will expand as skills, skillsets, fixtures, and
evaluation reports are added.

## Pull Request Expectations

A useful pull request should state:

- which roadmap wave it advances;
- which domain family it touches;
- which artifacts changed;
- what evidence or source material was used;
- what validation was run;
- any unresolved risks, assumptions, or follow-up work.
