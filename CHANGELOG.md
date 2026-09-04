# Changelog

All notable changes to AgentLogistics will be documented in this file.

The format follows a lightweight, human-readable changelog style. The first
public preview release is `v0.1.0-public-preview`.

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
- Completed Wave AL-11 transportation and freight core.
- Added 16 transportation-freight skill packages and composed them into
  `skillsets/transportation-coordinator/`.
- Added the transportation-coordinator multimode scenario, fixture, evaluation
  report, and AL-11 handoff.
- Extended validation for the transportation-coordinator skillset gate.
- Completed Wave AL-12 logistics systems and data.
- Added 13 logistics-systems-data skill packages and composed them into
  `skillsets/logistics-systems-analyst/`.
- Added the logistics-systems-analyst integration data-quality scenario,
  fixture, evaluation report, and AL-12 handoff.
- Extended validation for the logistics-systems-analyst skillset gate, including
  GS1 source-boundary checks.
- Completed Wave AL-13 performance and continuous improvement.
- Added 13 performance-continuous-improvement skill packages and composed them
  into `skillsets/continuous-improvement-specialist/`.
- Added the continuous-improvement-specialist performance review scenario,
  fixture, evaluation report, and AL-13 handoff.
- Extended validation for the continuous-improvement-specialist skillset gate,
  including recommendation-gate checks.
- Completed Wave AL-14 labor and operating planning.
- Added 8 labor-operating-planning skill packages and composed them into
  `skillsets/warehouse-supervisor/` and `skillsets/warehouse-manager/`.
- Added warehouse-supervisor and warehouse-manager labor-planning scenarios,
  fixtures, evaluation report, and AL-14 handoff.
- Extended validation for both AL-14 skillset gates, including labor-time,
  planning-component, and labor-approval boundary checks.
- Completed Wave AL-15 returns and reverse logistics.
- Added 12 reverse-logistics skill packages under `skills/reverse-logistics/`.
- Added the reverse-logistics return lifecycle scenario, fixture, evaluation
  report, and AL-15 handoff.
- Extended validation for the AL-15 reverse-logistics test gate, including
  lifecycle, quantity-state, and approval-boundary checks.
- Completed Wave AL-16 Canadian logistics safety and compliance.
- Added the Canada specialization under `specializations/canada/` with 11
  source-backed research packages.
- Added the Canada compliance source-triage scenario, fixture, evaluation
  report, shared authority map, and AL-16 handoff.
- Added specialization validation and extended test validation for Canada
  jurisdiction, official-source, and compliance-boundary checks.
- Completed Wave AL-17 United States logistics safety and compliance.
- Added the United States specialization under `specializations/united-states/`
  with 11 source-backed research packages.
- Added the US compliance source-triage scenario, fixture, evaluation report,
  shared authority map, and AL-17 handoff.
- Extended specialization and test validation for US jurisdiction,
  official-source, OSHA state-plan, hazmat, and compliance-boundary checks.
- Completed Wave AL-18 professional skillset composition.
- Added receiving-specialist, logistics-coordinator, distribution-manager, and
  logistics-operations-manager skillsets that compose existing atomic skills.
- Added the professional skillset composition index, scenario, fixture,
  evaluation report, and AL-18 handoff.
- Extended skillset and test validation for AL-18 role-component,
  composition-gate, routing, escalation, dependency, and boundary checks.
- Completed Wave AL-19 specialized logistics framework.
- Added the specialization roadmap architecture artifact for cold-chain,
  food-logistics, dangerous-goods, ecommerce, manufacturing,
  retail-distribution, automotive, pharmaceuticals, and
  international-logistics.
- Added the AL-19 specialization framework scenario, fixture, evaluation
  report, and handoff.
- Extended docs and test validation for AL-19 candidate fields, priorities,
  extension rules, and specialization-boundary checks.
- Completed Wave AL-20 food and cold-chain logistics.
- Added the `specializations/food-cold-chain/` industry specialization with
  twelve source-backed planning packages.
- Added the food cold-chain source map, source-triage scenario, fixture,
  evaluation report, and AL-20 handoff.
- Extended specialization, docs, and test validation for AL-20 package coverage,
  official source URLs, roadmap capabilities, blocked claims, and
  AgentLogistics/ChefSkills independence.
- Completed Wave AL-21 dangerous goods logistics.
- Added the `specializations/dangerous-goods/` source-backed specialization
  with four research and planning packages.
- Added the dangerous-goods source map, source-triage scenario, fixture,
  evaluation report, and AL-21 handoff.
- Extended specialization, docs, and test validation for AL-21 package coverage,
  official source URLs, roadmap requirements, blocked claims, mode-specific
  research, jurisdiction-specific research, and personnel qualification
  boundaries.
- Completed Wave AL-22 international logistics.
- Added the `specializations/international-logistics/` source-backed
  specialization with four research and handoff packages.
- Added the international-logistics source map, source-triage scenario, fixture,
  evaluation report, and AL-22 handoff.
- Extended specialization, docs, and test validation for AL-22 package coverage,
  official source URLs, roadmap areas, blocked claims, lane-specific research,
  jurisdiction-specific research, mode-specific research, customs broker
  handoffs, freight forwarder handoffs, and trade-compliance boundaries.
- Completed Wave AL-23 repository-wide integration evaluation.
- Added five integration scenarios covering inbound shortage, warehouse
  throughput collapse, inventory accuracy deterioration, capacity constraint,
  and transportation cost increase.
- Added the repository-wide integration fixture, AL-23 evaluation report, and
  AL-23 handoff.
- Extended docs and test validation for AL-23 scenario coverage, cross-domain
  route groups, output invariants, blocked approval classes, and evaluation
  report coverage.
- Completed Wave AL-24 documentation and public readiness.
- Reworked `README.md` for public users with audience, capabilities, quick
  start, skill examples, structure, limitations, contribution process, safety
  boundaries, security, license, completed gates, and next wave.
- Expanded `CONTRIBUTING.md` with contributor priorities, skill standards,
  evidence rules, calculation requirements, safety boundaries, validation
  commands, pull request expectations, and issue guidance.
- Added GitHub issue templates, a pull request template, the AL-24 public
  readiness audit, and the AL-24 handoff.
- Extended documentation validation for AL-24 public-readiness files, README
  sections, contribution sections, templates, audit coverage, and completion
  token checks.
- Completed Wave AL-25 v1 release candidate audit.
- Added the AL-25 v1 release candidate audit and AL-25 handoff with a
  `V1_PARTIALLY_READY` verdict.
- Recorded v1 blockers for live model scoring, external source freshness and
  reachability checks, expanded calculation verification, CI visibility, release
  notes, release tagging, and repository-setting review.
- Updated `README.md` with the AL-25 completion token and current v1 audit
  verdict.
- Extended documentation validation for AL-25 audit and handoff coverage.
- Built the GitHub wiki with public orientation pages for getting started,
  scope, repository structure, skill usage, skill authoring, validation,
  skillsets, specializations, safety boundaries, roadmap status, v1 audit
  status, and contributing.
- Added the GitHub wiki link to `README.md`.
- Added GitHub Actions validation for pushes, pull requests, and manual
  dispatches.
- Added the v1 hardening CI validation note.
- Added a manual source-link audit script for specialization source maps.
- Added a scheduled and manual GitHub Actions source-link audit workflow.
- Added remote verification evidence for the GitHub Actions validation and
  source-link audit workflows.
- Added GitHub Copilot and `gh skill` setup documentation for AgentLogistics
  skill preview, install, pinning, and maintainer publish checks.
- Added `v0.1.0-public-preview` release notes for GitHub CLI agent-skills
  publishing.
- Published AgentLogistics to GitHub CLI agent skills as
  `v0.1.0-public-preview`.

### Changed

- Hardened the source-link audit to retry `GET` after failing `HEAD` requests
  and report transient network or TLS failures without failing scheduled CI by
  default.
