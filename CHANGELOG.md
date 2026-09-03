# Changelog

All notable changes to AgentLogistics will be documented in this file.

The format follows a lightweight, human-readable changelog style. This project
does not have public releases yet.

## Unreleased

### Added

- Initialized the AgentLogistics repository structure.
- Added the full development roadmap as the local execution authority.
- Completed Wave AL-00 baseline audit.
- Added Wave AL-01 domain contract and scope boundary documentation.
- Added lightweight repository validation scripts.
- Completed Wave AL-02 master taxonomy audit.
- Added the v1 taxonomy, taxonomy audit, dependency map, and AL-02 handoff.
- Added taxonomy validation for duplicate skill slugs and naming format.
- Completed Wave AL-03 skill specification standard.
- Added skill authoring, naming, evidence, calculation, and regulatory content
  standards.
- Added the `calculate-reorder-point` reference skill package.
- Added skill package validation and wired it into repository validation.
- Completed Wave AL-04 validation and evaluation framework.
- Added testing and evaluation standards, reference scenarios, deterministic
  reorder-point fixtures, and a before/after evaluation report.
- Added test framework validation and wired it into repository validation.
- Completed Wave AL-05 shared logistics foundations.
- Added shared units, inventory-state terms, reorder-point formula,
  calculation-output template, and reorder-point fixture schema.
- Added shared-foundation validation and wired the reference skill to consume
  shared materials.
- Completed Wave AL-06 warehouse core skillset.
- Added 22 warehouse-operation skill packages and composed them into
  `skillsets/warehouse-operator/`.
- Added warehouse-operator scenario, flow fixture, evaluation report, and
  skillset validation.
- Completed Wave AL-07 inventory control system.
- Added 19 inventory-control skill packages and composed them with
  `calculate-reorder-point` into `skillsets/inventory-control-specialist/`.
- Added the inventory discrepancy investigation scenario, fixture, evaluation
  report, and AL-07 handoff.
- Extended validation for separate warehouse-operator and
  inventory-control-specialist skillset gates.
- Completed Wave AL-08 storage, slotting, and facility planning.
- Added 20 storage, slotting, pick-path, and warehouse-planning skill packages
  and composed them into `skillsets/warehouse-planner/`.
- Added the warehouse-planner layout concept scenario, fixture, evaluation
  report, and AL-08 handoff.
- Extended validation for the warehouse-planner skillset gate.
- Completed Wave AL-09 replenishment and fulfillment optimization.
- Added 11 replenishment, picking, packing, loading, and shipping optimization
  skill packages and composed them with existing warehouse skills into
  `skillsets/fulfillment-optimizer/`.
- Added the fulfillment-optimizer order-profile scenario, fixture, evaluation
  report, and AL-09 handoff.
- Extended validation for the fulfillment-optimizer skillset gate.
- Completed Wave AL-10 material handling systems.
- Added 8 material-handling skill packages and composed them with existing
  warehouse context skills into `skillsets/material-handling-analyst/`.
- Added the material-handling selection-analysis scenario, fixture, evaluation
  report, and AL-10 handoff.
- Extended validation for the material-handling-analyst skillset gate.
