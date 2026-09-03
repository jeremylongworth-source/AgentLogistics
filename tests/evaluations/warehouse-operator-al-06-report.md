# Warehouse Operator AL-06 Evaluation

Completion token:

```text
AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY
```

## Scenario

- Scenario file: `tests/scenarios/warehouse-operator-end-to-end.md`
- Target skillset: `warehouse-operator`
- Target artifact: receive-to-ship operating response
- Evaluation date: 2026-09-03
- Reviewer: repository maintainer review required before public release

## Compared Conditions

- Baseline condition: simulated general model without AgentLogistics skills.
- Skill-enabled condition: AL-06 warehouse-operator skillset with 22 atomic
  warehouse-operation skills.

## Acceptance Criteria

- Correct routing: pass
- Required inputs handled: pass
- Calculation or method correct: pass for available method checks; unsupported
  calculations request missing inputs
- Output structure complete: pass
- Evidence and source handling: pass
- Safety boundary respected: pass

## Baseline Result Summary

A likely general answer can produce a reasonable warehouse checklist but may
skip formal flow ordering, blur receiving verification with inspection, infer
missing capacity or productivity values, and understate safety or compliance
review boundaries.

## Skill-Enabled Result Summary

The warehouse-operator skillset decomposes the operating response into atomic
skills, preserves the receive-to-ship sequence, asks for missing calculation
inputs, and keeps approval-sensitive claims out of the universal core.

## Rubric Scores

| Dimension | Baseline | Skill-Enabled | Notes |
|---|---:|---:|---|
| Trigger accuracy | 1 | 3 | Skillset routes through explicit warehouse steps. |
| Calculation correctness | 1 | 2 | Skillset blocks unsupported capacity and productivity calculations. |
| Input validation | 1 | 3 | Skills require source records, units, and status checks. |
| Missing-input behavior | 1 | 3 | Skillset asks for missing capacity, labor, and productivity inputs. |
| Unit handling | 1 | 2 | Shared unit boundaries apply, but more formulas are deferred. |
| Output structure | 1 | 3 | Skillset README and scenario define expected handoffs. |
| Evidence handling | 1 | 3 | User records are evidence only. |
| Safety boundary | 1 | 3 | Safety, rack, carrier, and regulatory approval claims are blocked. |
| Operational usefulness | 2 | 3 | Produces an end-to-end warehouse operating plan. |
| Concision | 2 | 2 | More structure is needed for the multi-step flow. |
| Reviewer edit burden | 1 | 2 | Reviewer still needs site-specific SOP and data checks. |

## Improvements

- Splits the work into atomic skills instead of one broad warehouse answer.
- Keeps receiving verification, inspection, discrepancy handling, and putaway
  distinct.
- Routes storage decisions through capacity and utilization checks.
- Preserves replenishment, picking, packing, staging, and shipping handoffs.
- Blocks unsupported safety, compliance, rack-load, and carrier approval claims.

## Regressions

- The skillset adds routing overhead for simple one-step requests.

## Safety And Evidence Notes

The scenario includes storage capacity, inspection, carrier cutoff, and shipment
handoff risks. The skillset may provide planning support, evidence requests, and
review packets, but not site safety, rack, regulatory, or carrier compliance
approval.

## Overhead Notes

The skillset adds 22 concise skill packages and one flow fixture. This overhead
is justified by the first end-to-end warehouse capability.

## Decision

keep

## Follow-Up Changes

- Add deeper calculation fixtures for storage capacity, pallet positions, and
  pick productivity in later waves.
- Add live model scenario execution when a broader runner exists.
