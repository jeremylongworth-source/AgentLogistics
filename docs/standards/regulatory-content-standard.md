# AgentLogistics Regulatory Content Standard

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY
```

## Purpose

AgentLogistics may support regulatory and safety research, but it must not claim
authority it does not have.

This standard applies to skills that touch laws, regulations, permits, safety
rules, customs, dangerous goods, food logistics, cold chain, pharmaceuticals,
employment requirements, vehicle rules, equipment use, facility compliance, or
other regulated operating areas.

## Allowed Outputs

Skills may produce:

- research briefs;
- source-backed obligation checklists;
- evidence requests;
- compliance-preparation checklists;
- inspection-preparation notes;
- operational risk registers;
- escalation packets for qualified reviewers;
- questions for counsel, regulators, engineers, safety professionals, brokers,
  carriers, insurers, or certified trainers.

## Disallowed Outputs

Skills must not produce:

- legal conclusions;
- regulatory approval;
- engineering signoff;
- operator certification;
- equipment certification;
- safety approval for a facility, rack, vehicle, machine, or process;
- declarations that a shipment, workplace, product, or process is compliant;
- instructions that bypass an employer safety program, competent-person review,
  regulator, carrier, customs broker, or qualified professional.

## Jurisdiction And Scope

Regulatory content must state:

- jurisdiction;
- mode or facility context;
- product or hazard context;
- time of source access or publication date when available;
- whether the output is a research brief, checklist, or final operational
  procedure;
- what must be reviewed by a qualified person before use.

If jurisdiction is missing, ask for it or provide only jurisdiction-neutral
questions and research steps.

## Source Requirements

Use current official sources for regulatory claims whenever possible:

- government statutes, regulations, and agency guidance;
- official regulator interpretation pages;
- recognized standards bodies when the applicable rule references a standard;
- carrier, customs, port, airport, or terminal rules for their own processes;
- user-provided contracts, permits, SOPs, or safety programs for local
  operating constraints.

Vendor blogs, forum posts, and AI output are not acceptable as final authority
for regulatory claims.

## Safety Requirements

For safety-sensitive work, skills must:

- identify hazards separately from controls;
- avoid prescribing equipment use beyond manufacturer instructions and employer
  programs;
- route structural, load-bearing, machine-guarding, electrical, hazardous
  material, and fire-code questions to qualified review;
- call out training, supervision, PPE, lockout, traffic, pedestrian, and
  emergency-response dependencies where relevant;
- distinguish practical observations from approved corrective actions.

## Output Labels

Use clear labels:

- `Research brief` for source-backed summaries that need review.
- `Preparation checklist` for evidence collection before review or inspection.
- `Operational draft` only when the user has provided local authority and the
  skill stays inside that authority.
- `Escalation required` when a qualified person must decide.

## Review Checklist

A regulatory or safety-sensitive skill is ready only when:

- it names the regulated scope and jurisdiction needs;
- it requires current official sources for rule claims;
- it keeps legal and certification boundaries explicit;
- it separates evidence, interpretation, and action;
- it tells the agent what to do when current sources are unavailable.
