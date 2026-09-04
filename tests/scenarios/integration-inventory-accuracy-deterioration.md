# Integration Scenario C: Inventory Accuracy Deterioration

Category: `integration_inventory_accuracy_deterioration`

Expected routing:

- `design-cycle-count-program`
- `plan-physical-inventory`
- `calculate-inventory-accuracy`
- `reconcile-inventory`
- `investigate-inventory-discrepancy`
- `analyze-inventory-shrinkage`
- `analyze-stockout`
- `analyze-wms-transaction-history`
- `analyze-logistics-scan-events`
- `perform-logistics-pareto-analysis`
- `perform-logistics-root-cause-analysis`
- `build-logistics-improvement-plan`
- `measure-improvement-result`

Prompt:

Cycle count accuracy dropped from 98.6 percent to 94.1 percent in six weeks.
The largest errors involve case-pick SKUs with mixed pallets, short picks,
manual moves, missing scan events, and unexplained adjustments on night shift.
Build an integration evaluation output connecting cycle count evidence, WMS
transactions, scan events, discrepancy investigation, Pareto analysis, root
cause, corrective action, and measurement. Do not approve shrinkage write-offs,
disciplinary action, inventory adjustments, customer commitments, financial
postings, or live system changes.

Acceptance checks:

- Routes across inventory control, systems data, performance analysis, and
  continuous improvement skills.
- Preserves cycle count, physical count, WMS balance, scan-event, adjustment,
  picking, shift, and SKU evidence separately.
- Uses Pareto and root-cause structure without blaming personnel from
  incomplete evidence.
- Defines corrective-action candidates and retest metrics without approving
  inventory or financial changes.

Risk and review notes:

- Inventory adjustments, shrinkage write-offs, HR decisions, financial postings,
  customer promises, regulated product decisions, and live system changes
  require qualified review.
