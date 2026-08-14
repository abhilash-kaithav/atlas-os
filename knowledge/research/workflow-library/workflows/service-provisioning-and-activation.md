# Service Provisioning and Activation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Network and Transportation Operations`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Broadcasting and telecommunications`
- Industry count: 1
- Systems-of-record categories: `Billing and Subscription Management | Network OSS/BSS | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Translate a sold network or platform service into an activated, billable, and supportable live service state.
- Trigger: A service order or change request is approved and ready for technical fulfillment.
- End outcome: The service is provisioned, activated, and synchronized across support and billing records.
- Primary actors: provisioning team; engineering or platform operations; customer-facing account owner; billing or assurance staff
- Major decisions: What design or activation path best fits the order and current capacity?; What dependency or exception blocks go-live?; When is the service stable enough to bill and hand to support?
- Major handoffs: commercial order -> technical provisioning; provisioned service -> assurance or support team; activated service -> billing and customer success
- Systems of record involved: Billing and Subscription Management | Network OSS/BSS | CRM

## Current-State Friction

- Where money is lost: Delayed activations and bad service-order hygiene push revenue start dates and increase fallout.
- Where time is lost: Provisioning teams reconcile commercial orders with technical reality and chase cross-system updates.
- Where human judgment dominates: Engineers and provisioning staff still judge edge-case feasibility and recovery steps.
- Where people leave the system of record: Actual root-cause context often lives in tickets, chat threads, and engineering notes outside the order record.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, Network OSS/BSS, CRM; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, Netcracker, Ericsson.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; Netcracker; Ericsson; Salesforce CRM; Microsoft Dynamics 365 Sales
- Why this has not been solved cleanly: Commercial, technical, and billing systems still do not share one reliable activation truth in many stacks. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
