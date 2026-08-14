# Network Planning and Capital Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Broadcasting and telecommunications`
- Industry count: 1
- Systems-of-record categories: `Billing and Subscription Management | Network OSS/BSS | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Set the next operating baseline for capacity, demand, production, or resource use under uncertain conditions.
- Trigger: A planning horizon opens or enough signal changes that the current plan no longer fits reality.
- End outcome: A practical baseline plan is published with assumptions and accountable owners documented.
- Primary actors: planner; operations leader; commercial or finance partner; downstream execution owner
- Major decisions: What demand and capacity assumptions should the organization trust right now?; Which tradeoff between service, cost, and utilization is acceptable?; When should the baseline be changed rather than managed through exceptions?
- Major handoffs: market or operating signals -> planning team; published plan -> procurement, labor, or execution teams; plan variance -> management review
- Systems of record involved: Billing and Subscription Management | Network OSS/BSS | CRM

## Current-State Friction

- Where money is lost: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting.
- Where time is lost: Planning teams spend time rebuilding assumptions and chasing sign-off across functions.
- Where human judgment dominates: Planners still decide which signals to trust and when the model output does not fit local reality.
- Where people leave the system of record: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, Network OSS/BSS, CRM; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, Netcracker, Ericsson.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; Netcracker; Ericsson; Salesforce CRM; Microsoft Dynamics 365 Sales
- Why this has not been solved cleanly: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
