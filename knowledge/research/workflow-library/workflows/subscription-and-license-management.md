# Subscription and License Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `IP, Subscription, and Rights Management`
- Industries using this workflow: `Publishing industries, except internet (includes software)`
- Industry count: 1
- Systems-of-record categories: `Billing and Subscription Management | CRM | ERP | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Translate recurring usage, entitlements, or contracted service into accurate recurring bills and renewal-ready account records.
- Trigger: A subscription period closes, usage accrues, or a contract event changes what should be billed.
- End outcome: The account reflects the correct bill, entitlement state, and next renewal or support action.
- Primary actors: billing operations team; customer success or account owner; finance partner; customer
- Major decisions: What contract, usage, or entitlement state should drive the bill?; Which exception requires manual correction or customer communication?; What change should flow into renewal or expansion planning?
- Major handoffs: product or usage systems -> billing operations; billing issue -> support or account owner; finalized bill -> finance close and renewal tracking
- Systems of record involved: Billing and Subscription Management | CRM | ERP | Service Management

## Current-State Friction

- Where money is lost: Leakage comes from usage mismatch, wrong entitlements, stale contract data, and manual credits.
- Where time is lost: Teams spend time reconciling subscription state across CRM, billing, and service systems.
- Where human judgment dominates: Operators still decide how to resolve exceptions, bundle edge cases, and preserve the relationship during disputes.
- Where people leave the system of record: Important contract and exception context lives in tickets, email, and account notes outside the billing platform.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, CRM, ERP, Service Management; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, Salesforce CRM, Microsoft Dynamics 365 Sales.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Recurring billing is structurally automatable, but entitlement logic and exception-heavy account transitions remain messy. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `IP, Subscription, and Rights Management`: Develops, licenses, distributes, and accounts for content or software portfolios governed by subscriptions, rights, and recurring usage.
