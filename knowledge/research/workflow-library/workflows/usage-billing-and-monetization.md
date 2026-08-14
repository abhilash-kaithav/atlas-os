# Usage Billing and Monetization

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Digital Platform and Subscription Operations`
- Industries using this workflow: `Data processing, internet publishing, and other information services`
- Industry count: 1
- Systems-of-record categories: `Billing and Subscription Management | Cloud Infrastructure and IT Operations | CRM | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Translate recurring usage, entitlements, or contracted service into accurate recurring bills and renewal-ready account records.
- Trigger: A subscription period closes, usage accrues, or a contract event changes what should be billed.
- End outcome: The account reflects the correct bill, entitlement state, and next renewal or support action.
- Primary actors: billing operations team; customer success or account owner; finance partner; customer
- Major decisions: What contract, usage, or entitlement state should drive the bill?; Which exception requires manual correction or customer communication?; What change should flow into renewal or expansion planning?
- Major handoffs: product or usage systems -> billing operations; billing issue -> support or account owner; finalized bill -> finance close and renewal tracking
- Systems of record involved: Billing and Subscription Management | Cloud Infrastructure and IT Operations | CRM | Service Management

## Current-State Friction

- Where money is lost: Leakage comes from usage mismatch, wrong entitlements, stale contract data, and manual credits.
- Where time is lost: Teams spend time reconciling subscription state across CRM, billing, and service systems.
- Where human judgment dominates: Operators still decide how to resolve exceptions, bundle edge cases, and preserve the relationship during disputes.
- Where people leave the system of record: Important contract and exception context lives in tickets, email, and account notes outside the billing platform.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, Cloud Infrastructure and IT Operations, CRM, Service Management; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, ServiceNow IT Operations Management, AWS.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; ServiceNow IT Operations Management; AWS; Microsoft Azure; Google Cloud
- Why this has not been solved cleanly: Recurring billing is structurally automatable, but entitlement logic and exception-heavy account transitions remain messy. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [ServiceNow IT Operations Management](https://www.servicenow.com/docs/r/it-operations-management/r_ITOMApplications.html)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Digital Platform and Subscription Operations`: Monetizes digital products or infrastructure through release velocity, onboarding, billing, retention, and service reliability.
