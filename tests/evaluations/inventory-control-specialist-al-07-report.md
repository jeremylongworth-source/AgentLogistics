# Inventory Control Specialist AL-07 Evaluation

Completion token:

```text
AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY
```

## Scenario

- Scenario file: `tests/scenarios/inventory-discrepancy-investigation.md`
- Target skillset: `inventory-control-specialist`
- Target artifact: review-ready inventory discrepancy investigation
- Evaluation date: 2026-09-03
- Reviewer: repository maintainer review required before public release

## Compared Conditions

- Baseline condition: simulated general model without AgentLogistics
  inventory-control skills.
- Skill-enabled condition: AL-07 inventory-control-specialist skillset
  with 20 inventory-control skills and warehouse receiving handoffs.

## Acceptance Criteria

- Correct routing: pass
- Required inputs handled: pass
- Calculation or method correct: pass for supported quantity bridge and
  inventory metrics; unsupported values request missing inputs
- Output structure complete: pass
- Evidence and source handling: pass
- Safety boundary respected: pass

## Baseline Result Summary

A likely general answer can summarize the discrepancy and may propose a
plausible cause, but it can blur receiving, WMS, physical count, picking,
and adjustment evidence. It may also treat the -4 adjustment or picker
note as enough to conclude root cause without building a chronology.

## Skill-Enabled Result Summary

The inventory-control-specialist skillset routes the case through
classification, count accuracy, reconciliation, discrepancy
investigation, stockout, lot-control, shrinkage, and receiving handoffs.
It requires a source-by-source evidence table, transaction chronology,
quantity reconciliation, conflict list, evidence-ranked candidate causes,
missing evidence, and adjustment-review boundary.

## Rubric Scores

| Dimension | Baseline | Skill-Enabled | Notes |
|---|---:|---:|---|
| Trigger accuracy | 1 | 3 | Skillset routes to inventory evidence and supporting receiving skills. |
| Calculation correctness | 1 | 3 | Balance bridge uses only compatible transaction evidence. |
| Input validation | 1 | 3 | Requires the five discrepancy evidence categories or marks gaps. |
| Missing-input behavior | 1 | 3 | Missing approver, transaction signs, and unlabeled lot evidence remain open. |
| Unit handling | 2 | 3 | Quantity basis is eaches; case label conflict remains evidence, not conversion. |
| Output structure | 1 | 3 | Scenario and fixture define the investigation artifact. |
| Evidence handling | 1 | 3 | Source conflicts are preserved instead of collapsed into one story. |
| Safety boundary | 1 | 3 | No adjustment approval or accusation is allowed. |
| Operational usefulness | 2 | 3 | Produces a review-ready investigation packet. |
| Concision | 2 | 2 | The multi-source case needs more structure than a short answer. |
| Reviewer edit burden | 1 | 2 | Reviewer still needs site records and owner approval before action. |

## Improvements

- Adds a complete general-purpose inventory-control foundation.
- Makes discrepancy investigation evidence-led instead of conclusion-led.
- Preserves controlled-inventory, stockout, shrinkage, and receiving
  boundaries.
- Extends validation so AL-06 and AL-07 skillsets are checked separately.

## Regressions

- The skillset adds routing overhead for simple one-metric inventory
  questions.

## Safety And Evidence Notes

The scenario includes adjustment, shrinkage, lot-control, and stockout
risks. The skillset may provide planning support, evidence requests, and
review packets, but not adjustment approval, financial write-off, quality
release, or accusation.

## Overhead Notes

The skillset adds 19 new inventory-control skill packages, composes them
with the existing reorder-point skill, and adds one discrepancy fixture.
The overhead is justified by the roadmap objective for a complete
inventory foundation.

## Decision

keep

## Follow-Up Changes

- Add deterministic formula fixtures for safety stock, EOQ, turns, days
  on hand, and accuracy in later waves.
- Add live model scenario execution when a broader runner exists.
