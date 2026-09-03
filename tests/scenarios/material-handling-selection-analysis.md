# Material Handling Selection Analysis

Category: `material_handling_selection_analysis`

Expected routing:

- `analyze-product-flow`
- `identify-logistics-constraints`
- `select-storage-system`
- `plan-warehouse-zones`
- `classify-material-handling-requirements`
- `select-material-handling-equipment`
- `calculate-equipment-requirements`
- `analyze-equipment-utilization`
- `plan-material-flow`
- `evaluate-conveyor-application`
- `evaluate-agv-amr-application`
- `evaluate-asrs-application`

Prompt:

```text
We need a review-ready material-handling selection analysis for a dry ambient distribution center. Do not approve a purchase, certify equipment, certify operators, certify load ratings, approve traffic safety, approve guarding, approve building/fire/electrical/structural compliance, or configure any live WMS, WES, ERP, MHE, or automation system.

Facility and flow context:

- The building has 28 feet clear height. Reserve rack top beam is 22 feet. Current reserve aisles are 11 feet wide and the pick-module aisles are 7 feet wide.
- Product flow is inbound receiving to reserve, reserve to forward pick, forward pick to pack, and pallet staging to five outbound doors. The main cross aisle has repeated congestion near the battery charging area.
- Operating environment is dry ambient. The dock apron has uneven spots noted by supervisors, but the automation review scope is inside the building only.

Load, dimension, volume, and throughput facts:

- Pallet loads are 48 x 40 inches, average 1,200 lb, reported maximum 2,200 lb, and average 64 inches high. Pallet moves are 180 receiving putaway moves per day and 420 reserve-to-dock or reserve-to-forward-pick moves per day.
- Case and tote flow is 3,600 totes per day, standard tote size 18 x 24 x 12 inches, maximum tote weight 35 lb. Peak pack induction demand is 430 totes per hour for two hours.
- Reach-truck movement averages 420 feet loaded and 380 feet return. A representative observed cycle is 1.5 minutes load, 1.3 minutes unload, 250 feet per minute loaded travel, 280 feet per minute return travel, and a 15 percent delay allowance.
- Current equipment is 3 reach trucks, 2 counterbalance lift trucks, 8 manual pallet jacks, and 12 carts. Reach-truck availability is estimated at 88 percent after charging and downtime. Two 7-hour shifts are available for this flow.

Decision context:

- Leadership wants options across manual/powered equipment, conveyor for tote flow, AGV/AMR for repeatable pallet or cart movement, and AS/RS for future storage density.
- Capital intensity should be grouped as low, medium, or high only; there are no vendor quotes yet.
- WMS integration readiness is uncertain, the safety team flagged a pedestrian near-miss at the blind cross-aisle corner, and item master cube is missing for 9 percent of tote SKUs.

Build an analysis that covers handling requirements, equipment class comparison, equipment requirement estimates, utilization implications, material-flow planning, conveyor applicability, AGV/AMR applicability, AS/RS applicability, missing evidence, and review-required actions. Show calculations only where the facts support them and separate selection analysis from certification.
```

Acceptance checks:

- Covers load, dimensions, volume, travel distance, throughput, storage height, aisle requirements, operating environment, automation level, safety, and capital intensity.
- Classifies material-handling requirements before comparing equipment classes.
- Calculates supported cycle time, moves per equipment unit, equipment requirement, or utilization implications only from supplied facts.
- Evaluates manual/powered equipment, conveyor, AGV/AMR, and AS/RS at applicability level without vendor selection or certification.
- Treats WMS integration uncertainty, pedestrian near-miss, missing cube data, aisle widths, storage height, and dock-apron note as constraints.
- Distinguishes selection analysis from equipment capacity certification, operator certification, traffic-safety approval, guarding approval, and building/fire/electrical/structural compliance.

Risk and review notes:

- Synthetic scenario only. The case includes no private customer data or live system requirement. Site owner, safety, engineering, maintenance, IT, finance, vendor, and qualified operations review may be required before operational use.
