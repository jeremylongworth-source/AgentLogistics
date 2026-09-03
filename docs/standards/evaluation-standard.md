# AgentLogistics Evaluation Standard

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY
```

## Purpose

This standard defines how AgentLogistics compares general model behavior against
skill-enabled behavior.

The goal is not to prove that a skill is perfect. The goal is to decide whether
the skill improves routing, correctness, validation, safety, and usefulness
enough to keep, revise, split, merge, defer, or retire it.

## Compared Conditions

Use the same scenario and target artifact under two conditions:

```text
general model without skill
vs.
general model with AgentLogistics skill
```

When a live baseline run is impractical, record a simulated baseline based on
the likely unspecialized answer pattern and label it as simulated.

Do not leak expected answers into either prompt.

## Required Evaluation Inputs

Each evaluation must define:

- scenario file;
- target skill or skillset;
- target artifact;
- baseline condition;
- skill-enabled condition;
- acceptance criteria;
- rubric version;
- reviewer and date when manually reviewed.

## Rubric

Score each dimension from 0 to 3:

| Score | Meaning |
|---:|---|
| 0 | Missing, wrong, unsafe, or unusable. |
| 1 | Partially useful but materially incomplete or risky. |
| 2 | Useful with minor gaps or review notes. |
| 3 | Correct, complete, clear, and ready for the stated scope. |

Required dimensions:

- trigger accuracy;
- calculation correctness;
- input validation;
- missing-input behavior;
- unit handling;
- output structure;
- evidence handling;
- safety boundary;
- operational usefulness;
- concision;
- reviewer edit burden.

For non-calculation skills, mark calculation-specific dimensions as not
applicable and explain the replacement criteria.

## Promotion Decisions

Use these decisions:

- `keep`: skill passes and can be used as written.
- `revise`: skill is useful but needs scoped changes.
- `split`: skill is too broad and should become multiple skills.
- `merge`: skill overlaps another skill and should be consolidated.
- `defer`: skill is valid but not ready for current authoring.
- `retire`: skill is not useful or unsafe for the repository.

Promotion to mass authoring requires:

- no score below 2 on required dimensions;
- no unsafe approval or compliance claim;
- passing structural validation;
- passing deterministic fixtures when calculations exist;
- a recorded evaluation report.

## Before/After Report

Use `docs/evaluation/before-after-report-template.md` for each comparison
report.

Each report must include:

- scenario and target artifact;
- baseline result summary;
- skill-enabled result summary;
- rubric scores;
- improvements;
- regressions;
- safety and evidence notes;
- overhead notes;
- promotion decision;
- follow-up changes.

## Safety And Evidence

Do not hide regressions because the skill improved another dimension.

If the skill-enabled output is more confident without better evidence, record
that as a regression.

If a scenario touches legal, regulatory, safety, finance, customer commitments,
dangerous goods, customs, food, cold chain, medical, or high-value inventory,
the evaluation must state the review boundary and the qualified reviewer role.

## Evaluation Re-Run Triggers

Re-run affected evaluations when:

- skill triggers or non-triggers change;
- required inputs or assumptions change;
- formula, rounding, or unit rules change;
- references change;
- validation scripts change;
- a new skillset composes the skill;
- a release candidate is prepared;
- a user report reveals a routing, calculation, evidence, or safety failure.
