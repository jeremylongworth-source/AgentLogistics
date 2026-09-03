# Calculation Output Template

Status: `READY`

Completion token:

```text
AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY
```

## Purpose

Use this template when an AgentLogistics skill returns a numeric logistics
calculation.

The template keeps calculation outputs reviewable without forcing exact prose.

## Template

```text
<Result label>: <rounded or final value> <unit>

Calculation:
- Formula: <formula name or expression>
- Inputs: <input values with original units>
- Normalization: <unit conversions or "none">
- Intermediate values: <values needed to audit the result>
- Raw result: <raw value and unit>
- Rounding: <rounding policy and rounded value>

Decision:
- <optional operational comparison or signal>

Notes:
- Assumptions: <explicit assumptions>
- Validation: <input and reasonableness checks>
- Missing inputs: <if any>
- Review required: <if safety, regulatory, financial, or policy boundary applies>
```

## Required Fields

A calculation output must include:

- result label;
- formula;
- inputs with original units;
- unit normalization;
- intermediate values;
- raw result;
- rounding policy;
- assumptions;
- validation notes;
- missing inputs or review requirements when applicable.

## Use Rules

- Use exact numbers where the calculation is deterministic.
- Use approximate labels only when the data or assumptions are approximate.
- Do not hide unit conversions.
- Do not bury missing required inputs after a final-looking result.
- Keep operational recommendations separate from mathematical results.
