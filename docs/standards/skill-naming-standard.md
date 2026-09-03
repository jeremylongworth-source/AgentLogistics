# AgentLogistics Skill Naming Standard

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY
```

## Purpose

Skill names must be predictable, searchable, and stable enough for routing,
testing, documentation, and skillset composition.

## Format

Use lowercase hyphen-case:

```text
<verb>-<logistics-object>
```

Examples:

- `calculate-reorder-point`
- `plan-inbound-receiving`
- `verify-outbound-shipment`
- `analyze-pick-accuracy`

Requirements:

- Use ASCII lowercase letters and numbers.
- Use hyphens as separators.
- Do not use spaces, underscores, punctuation, camelCase, or version suffixes.
- Match the `name` frontmatter value exactly to the skill directory.
- Keep names short enough to read but specific enough to route.

## Approved Verb Families

Use the narrowest verb that matches the skill output:

| Verb | Use when the skill primarily |
|---|---|
| `analyze` | Interprets evidence, trends, causes, or performance. |
| `audit` | Checks a document, charge, record, or configuration against a rule set. |
| `build` | Produces an operating artifact such as a scorecard or daily plan. |
| `calculate` | Produces a numeric result from explicit formulas. |
| `classify` | Assigns an item, process, operation, or exception to a category. |
| `compare` | Evaluates alternatives against consistent criteria. |
| `define` | Establishes requirements, terms, or operating criteria. |
| `design` | Produces a policy, program, flow, layout, or control structure. |
| `diagnose` | Identifies likely causes of an observed operational problem. |
| `identify` | Finds constraints, risks, exceptions, waste, or candidate items. |
| `interpret` | Explains a document, identifier, code, or logistics record. |
| `investigate` | Walks through evidence to resolve an exception or discrepancy. |
| `manage` | Defines control actions for an ongoing exception, process, or asset. |
| `map` | Converts a process, flow, handoff, or integration into a structured map. |
| `optimize` | Improves a constrained objective using explicit tradeoffs. |
| `perform` | Executes a named method such as root-cause analysis or Pareto analysis. |
| `plan` | Produces a practical operating plan, handoff, schedule, or action set. |
| `prioritize` | Orders work, exceptions, or actions by criteria. |
| `process` | Guides execution of a bounded operational workflow. |
| `reconcile` | Resolves expected-versus-actual records. |
| `schedule` | Produces a time-slot or appointment assignment. |
| `select` | Chooses a method, mode, equipment class, policy, or carrier from options. |
| `validate` | Checks data quality, completeness, units, or master-data readiness. |
| `verify` | Confirms shipment, order, inventory, or document facts before a handoff. |

## Object Rules

- Name the operational object, not the internal method.
- Use common logistics terms from the domain contract.
- Avoid vague objects such as `operation`, `issue`, or `strategy` unless the
  taxonomy already approves the exact skill.
- Use singular nouns for formulas and named outputs when the result is one
  artifact: `calculate-reorder-point`, not `calculate-reorder-points`.
- Use plural nouns when the task naturally operates on a set:
  `compare-freight-rates`, `manage-freight-claims` only if the skill handles
  multiple claims.
- Do not include vendor names, WMS names, countries, provinces, states, or
  industries in a universal core skill.

## Specialization Names

Specialized skills must make the boundary visible in the path or name:

```text
specializations/<jurisdiction-or-industry>/<domain>/<skill-name>/
```

If the name itself must include the specialization, put the specialization after
the object:

```text
classify-dangerous-goods-logistics-requirements
plan-customs-broker-handoff
```

## Disallowed Patterns

Do not create skill names that:

- promise certification, approval, legal conclusions, or engineering signoff;
- combine unrelated actions with `and`;
- use broad labels such as `full-warehouse-optimization`;
- duplicate an existing taxonomy row under a slightly different phrase;
- use internal implementation names such as `run-python-solver`;
- use brand-specific naming for universal capabilities.

## Naming Review

Before accepting a new skill name, confirm:

- the name exists in the AL-02 taxonomy or has a recorded taxonomy-change note;
- the verb matches the expected output;
- the object has one clear logistics meaning;
- the name does not hide a jurisdiction, equipment, or regulatory dependency;
- nearby skills have been checked for overlap.
