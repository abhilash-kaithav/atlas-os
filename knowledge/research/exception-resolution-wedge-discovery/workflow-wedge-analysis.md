# Workflow Wedge Analysis

Last updated: 2026-08-14
Status: Active wedge layer

## Workflow Decisions

| Workflow | Exact exception still underserved | Why it persists | Primary constraint | Wedge verdict |
| --- | --- | --- | --- | --- |
| Access, Admissions, and Throughput Management | Edge-case intake and scheduling handoffs after eligibility uncertainty | Real-time capacity and payer complexity still require human coordination | Organizational | Roll into provider denial wedge |
| Eligibility and Authorization | Payer-specific authorization exception handling | Payer rules, portal fragmentation, and incomplete patient documentation | Regulatory | Roll into provider denial wedge |
| Coding and Charge Capture | Denial and documentation appeal packet assembly | Clinical nuance and payer logic remain case-specific | Regulatory | Roll into provider denial wedge |
| Payer Contract Management | Underpayment and carve-out dispute resolution | Contract interpretation still crosses legal, payer, and rev-cycle data | Economic | Roll into provider denial wedge |
| Billing and Collections | Contract-specific short-pay and dispute work | Exceptions span customer context, account history, and payment ops | Economic | Kill |
| Billing and Payment Processing | Service-business billing corrections and dispute follow-up | Too many SMB variants and weak willingness to add net-new workflow software | Economic | Kill |
| Usage Billing and Monetization | Usage corrections, one-off invoice edge cases, entitlement drift | Modern billing stacks still optimize planned pricing over custom edge behavior | Architectural | Advance to SaaS monetization wedge |
| Time and Expense Capture | Complex project-billing exceptions after time capture | Billing logic still escapes into reporting, pivots, and local policy workarounds | Architectural | Watch, but not Top 3 |
| Progress Billing and Compliance Administration | Pay-app rejections driven by waiver, SOV, change-order, and backup mismatches | Current tools serve GC or owner control better than trade-contractor AR execution | Business model | Advance to construction wedge |
| Meter-to-Cash | Field-to-billing exception follow-up on problematic bills | Entrenched utility stacks and long deployment cycles blunt startup entry | Architectural | Watch, but not Top 3 |
| Freight Audit and Billing | POD and accessorial disputes tied to invoice evidence | TMS data and invoice documents still diverge, but freight-audit vendors already sell into it | Architectural | Watch, but not Top 3 |
| Freight Audit and Settlement | Counterparty settlement breaks and dispute routing | Existing audit and settlement tools already own much of the buyer budget | Economic | Kill |
| Order Management and Fulfillment | Customer-specific split-order and substitution recovery | OMS and planning systems already own the control point; exceptions are execution-heavy | Strategic choice | Kill |
| Logistics and Channel Fulfillment | Cross-system fulfillment recovery after inventory truth breaks | Strong planning and fulfillment incumbents already attack this layer | Strategic choice | Kill |
| Aftermarket Service and Field Support | High-cost service recovery exceptions across parts, field, and customer history | Hard, but already partially owned by service platforms and field-service stacks | Architectural | Kill |
| Service Provisioning and Activation | Dependency-driven activation exception resolution | Telecom and service-delivery stacks are deeply embedded and integration-heavy | Architectural | Kill |
| Order Capture and Payment Processing | POS and refund exceptions in real time | Too operationally fragmented and already embedded in payment/POS vendors | Strategic choice | Kill |
| Margin and Shrink Management | Store-level vendor or markdown exception handling | The problem is real but buyer separation from merchandising and ERP tools is weak | Organizational | Kill |
| Billing and Asset Recovery | Asset-status and rental-billing disputes | Strong overlap with incumbent rental and asset platforms | Business model | Kill |
| Procurement and Replenishment | Supplier shortage and substitution exception routing | Buyer pain is real, but the wedge looks more like planning and supplier collaboration than a clean exception company | Strategic choice | Kill |

## Surviving Wedge Themes

### 1. Construction pay-app exception resolution

Workflows:

- `Progress Billing and Compliance Administration`

### 2. Provider denial and recoupment exception resolution

Workflows:

- `Access, Admissions, and Throughput Management`
- `Eligibility and Authorization`
- `Coding and Charge Capture`
- `Payer Contract Management`

### 3. SaaS monetization exception resolution

Workflows:

- `Usage Billing and Monetization`

## Why Most Workflows Failed

- Some had clear pain but weak buyer separation from incumbent systems.
- Some had clear buyers but already had strong direct vendors.
- Some still looked horizontal even after narrowing.
- Some were more planning, reconciliation, or service recovery problems than clean exception-resolution company boundaries.
