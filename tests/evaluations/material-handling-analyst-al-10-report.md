# Material Handling Analyst AL-10 Evaluation

Completion token:

```text
AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY
```

## Scenario And Target Artifact

- Scenario file: `tests/scenarios/material-handling-selection-analysis.md`
- Target skillset: `material-handling-analyst`
- Target artifact: review-ready material-handling selection analysis

## Compared Conditions

- Baseline condition: general logistics response without the AL-10 skillset.
- Skill-enabled condition: AL-10 material-handling-analyst skillset with requirements classification, equipment selection, sizing, utilization, material-flow, conveyor, AGV/AMR, and AS/RS application skills.

## Acceptance Criteria

- Correct routing: pass
- Required considerations: pass
- Calculation or method correct: pass for supported cycle-time, moves-per-equipment, requirement, utilization, and throughput checks; unsupported approvals are blocked
- Evidence and source handling: pass
- Safety boundary: pass
- Useful review artifact: pass

## Baseline Result Summary

A likely general answer can list common material handling equipment options and automation ideas, but it may jump directly to equipment recommendations, miss required load and aisle constraints, understate WMS and traffic risks, or imply that a forklift, conveyor, AGV/AMR, or AS/RS option is ready to buy or certify.

## Skill-Enabled Result Summary

The material-handling-analyst skillset routes the work through product flow, constraints, storage context, zoning context, handling requirements, equipment class comparison, equipment requirement estimates, utilization analysis, material-flow planning, conveyor applicability, AGV/AMR applicability, and AS/RS applicability. It keeps source constraints visible and marks equipment certification, operator certification, load rating, traffic safety, guarding, building, fire, electrical, structural, procurement, live configuration, and safety approvals as outside scope.

## Rubric Scores

| Criterion | Baseline | Skill-Enabled | Notes |
|---|---:|---:|---|
| Routing accuracy | 1 | 3 | Skillset covers the full AL-10 handling chain. |
| Completeness | 1 | 3 | All required considerations are explicitly required. |
| Calculation handling | 1 | 3 | Cycle-time, equipment-count, throughput, and utilization formulas are scoped to supplied facts. |
| Unit handling | 1 | 3 | Loads, inches, feet, minutes, hours, moves, totes, and percentages remain distinct. |
| Evidence handling | 1 | 3 | Source constraints are preserved instead of optimized away. |
| Safety boundary | 1 | 3 | Equipment certification, traffic, guarding, structural, fire, electrical, operator, procurement, and safety approvals are blocked. |
| Reviewer burden | 1 | 2 | The output still requires qualified site, vendor, safety, engineering, maintenance, IT, and finance review. |

Scale: 0 = absent, 1 = weak, 2 = usable, 3 = strong.

## Improvements And Regressions

Improvements:

- Forces requirement classification before equipment comparison.
- Covers conventional equipment, conveyor, AGV/AMR, and AS/RS without over-certifying any option.
- Uses supported cycle-time and uptime facts for equipment requirement estimates.
- Preserves safety, aisle, height, WMS integration, missing cube, and capital-intensity constraints.

Regressions:

- More structured output may be longer than a quick equipment list.

## Safety And Evidence Notes

The scenario includes equipment, automation, traffic, guarding, building, fire, electrical, structural, procurement, and safety risks. The skillset may provide planning support, evidence requests, option comparisons, and review packets, but not equipment certification or operational approval.

## Overhead Notes

The skillset adds one scenario, one fixture, one evaluation report, and a focused reference checklist per AL-10 skill. The added context is justified by high safety and capital-intensity risk.

## Decision

keep

## Follow-Up Changes

- Add deterministic equipment-sizing fixtures in a later validation wave if AL-10 formulas become regression-critical.
- Expand MHE maintenance, battery, charging, and traffic-safety workflows when later roadmap waves require them.
