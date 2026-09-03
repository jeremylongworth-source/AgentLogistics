# Warehouse Planner AL-08 Evaluation

Completion token:

```text
AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY
```

## Scenario

- Scenario file: `tests/scenarios/warehouse-planner-layout-concept.md`
- Target skillset: `warehouse-planner`
- Target artifact: review-ready warehouse planning concept
- Evaluation date: 2026-09-03
- Reviewer: repository maintainer review required before public release

## Compared Conditions

- Baseline condition: simulated general model without AgentLogistics warehouse-planning skills.
- Skill-enabled condition: AL-08 warehouse-planner skillset with storage, slotting, travel, capacity, congestion, zoning, and conceptual-layout skills.

## Acceptance Criteria

- Correct routing: pass
- Required inputs handled: pass
- Calculation or method correct: pass for supported capacity, utilization, dock, travel, and planning checks; unsupported values request missing inputs
- Output structure complete: pass
- Evidence and source handling: pass
- Safety boundary respected: pass

## Baseline Result Summary

A likely general answer can suggest common warehouse layout ideas, but it may combine capacity, slotting, dock, congestion, and structural considerations into one recommendation. It can also average conflicting blocked-location records or imply that a conceptual layout is ready for implementation.

## Skill-Enabled Result Summary

The warehouse-planner skillset decomposes the request into product and order context, storage requirements, capacity, cube, density, reserve and forward pick allocation, slotting, affinity, travel, dock capacity, flow, congestion, zoning, layout comparison, conceptual layout, and expansion triggers. It preserves source conflicts and marks engineering, rack, fire, floor-load, egress, permit, lease, capital, and safety approvals as outside scope.

## Rubric Scores

| Dimension | Baseline | Skill-Enabled | Notes |
|---|---:|---:|---|
| Trigger accuracy | 1 | 3 | Skillset routes to storage, slotting, travel, capacity, and facility planning. |
| Calculation correctness | 1 | 3 | Supported calculations expose inputs, units, exclusions, and missing values. |
| Input validation | 1 | 3 | Conflicting blocked-location evidence and missing cube/rack details are visible. |
| Missing-input behavior | 1 | 3 | Unsupported engineering, rack, aisle, cube, and cost outputs ask for source data. |
| Unit handling | 1 | 3 | Area, cube, positions, trailer time, and travel distance use explicit bases. |
| Output structure | 1 | 3 | Scenario and fixture define a review-ready planning artifact. |
| Evidence handling | 1 | 3 | Source conflicts are preserved instead of averaged away. |
| Safety boundary | 1 | 3 | Conceptual planning is not structural, fire, rack, permit, or safety approval. |
| Operational usefulness | 2 | 3 | Produces option comparison and planning handoffs. |
| Concision | 2 | 2 | The multi-domain planning case needs structured output. |
| Reviewer edit burden | 1 | 2 | Reviewer still needs site measurements, drawings, vendor data, and owner review. |

## Improvements

- Adds storage-system, cube, density, reserve, forward-pick, slotting, affinity, travel, capacity, zoning, congestion, layout, comparison, and expansion planning coverage.
- Reuses AL-06 and AL-07 context skills for product, order, storage, and SKU velocity evidence.
- Extends validation with a warehouse-planner fixture and AL-08 evaluation gate.
- Keeps conceptual planning separate from structural and approval-sensitive decisions.

## Regressions

- The skillset adds routing overhead for simple one-metric capacity questions.

## Safety And Evidence Notes

The scenario includes building, rack, traffic, dock, congestion, lease, capital, and conceptual layout risks. The skillset may provide planning support, evidence requests, option comparisons, and review packets, but not engineering, code, fire, rack, floor-load, egress, permit, lease, capital, or safety approval.

## Overhead Notes

The skillset adds 20 new skill packages and composes them with existing warehouse, storage, order, product, and inventory skills. The overhead is justified by the roadmap objective for physical storage and warehouse-planning intelligence.

## Decision

keep

## Follow-Up Changes

- Add deterministic formula fixtures for cube utilization, dock capacity, warehouse capacity, and layout comparison in later waves.
- Reuse `optimize-pick-path` during AL-09 fulfillment optimization.
