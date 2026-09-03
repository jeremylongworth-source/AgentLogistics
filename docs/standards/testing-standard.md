# AgentLogistics Testing Standard

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY
```

## Purpose

This standard defines the minimum tests required before AgentLogistics scales
skill production.

Tests must prove that a skill routes correctly, handles incomplete or unsafe
inputs, preserves calculation correctness, and returns a predictable output.

## Test Layers

AgentLogistics uses four test layers:

| Layer | Purpose | Artifact |
|---|---|---|
| Structural validation | Check repository, skill, metadata, and reference shape. | `scripts/validate-*.py` |
| Scenario routing | Check whether realistic prompts should trigger a skill. | `tests/scenarios/*.md`, `tests/expected-routing.yaml` |
| Deterministic fixtures | Check calculations, missing inputs, unit handling, and output invariants. | `tests/fixtures/*.json` |
| Evaluation reports | Compare baseline and skill-enabled output quality. | `tests/evaluations/*.md` |

## Required Scenario Categories

Each implemented calculation or safety-sensitive skill must have scenario
coverage for:

- correct invocation;
- incorrect invocation;
- missing inputs;
- bad inputs;
- calculation correctness;
- unit mismatch;
- ambiguous scenario;
- expected output structure;
- safety boundary;
- jurisdiction conflicts;
- unsupported assumptions.

Non-calculation skills may mark `calculation correctness` and `unit mismatch` as
not applicable, but the test artifact must state why.

## Scenario Files

Scenario files live in `tests/scenarios/`.

Each file must include:

- scenario title;
- `Category:`;
- `Expected routing:`;
- `Prompt:`;
- `Acceptance checks:`;
- `Risk and review notes:`.

Prompts must be realistic and must not name the expected skill unless the test
is explicitly about direct invocation wording.

Scenarios must not contain private customer, employee, credential, production,
or regulated shipment data.

## Expected Routing

`tests/expected-routing.yaml` is the routing manifest. It maps each scenario to:

- prompt file;
- category;
- expected skill routes.

Expected routes must reference existing skill folders unless the scenario is
explicitly marked as future coverage.

Empty `expected_routes: []` means the skill must not trigger.

## Deterministic Fixtures

Fixture files live in `tests/fixtures/` and use JSON so they can be validated by
the standard Python library.

Calculation fixtures must define:

- case ID;
- category;
- target skill;
- input values and units;
- expected status;
- expected intermediate values when calculation should proceed;
- expected final values when a final answer is valid;
- expected missing inputs, error fields, or review flags when calculation should
  not proceed.

Fixture validation must check numeric outputs with tolerances and must fail on
silent unit mismatches, invented assumptions, or unsafe final answers.

## Output Invariants

Expected output structure tests should check invariants rather than exact prose.
For reorder point calculations, required fields include:

- item scope;
- input values;
- normalized lead time;
- demand during lead time;
- safety stock;
- raw reorder point;
- rounded reorder point;
- assumptions;
- validation notes.

## Pass And Fail Rules

A skill test set passes only when:

- all required categories are represented;
- expected routes point to existing skills;
- calculation fixtures match expected numeric results;
- missing or invalid inputs produce partial outputs or clear clarification
  requests;
- safety and regulatory scenarios avoid approval claims;
- validation scripts pass without warnings that require action.

A single unsafe approval claim, hidden assumption, or wrong calculation fails the
skill.

## Commands

Run the full local validation gate with:

```powershell
.\scripts\validate-all.ps1
```

Run test validation directly with:

```powershell
python .\scripts\validate-tests.py --repo-root D:\AgentLogistics
```

## Review Cadence

Run tests:

- before committing new skills;
- after editing skill frontmatter, triggers, workflow, calculations, references,
  or output contracts;
- before release-candidate audits;
- after incidents or user reports that expose routing, calculation, evidence, or
  safety failures.
