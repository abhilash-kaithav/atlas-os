# Content and Service Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Broadcasting and telecommunications`
- Industry count: 1
- Systems-of-record categories: `Billing and Subscription Management | Network OSS/BSS | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert a committed order, project, or service promise into completed work that meets scope, timing, and quality expectations.
- Trigger: Demand has been accepted and operational work is ready to be performed.
- End outcome: The work is completed, status is recorded, and downstream billing or follow-up can proceed.
- Primary actors: operations lead; frontline delivery team; customer or receiving party; scheduler or dispatcher
- Major decisions: What work should be done first and by whom?; How should exceptions or changes in scope be handled?; What completion threshold is enough to close or advance the job?
- Major handoffs: planning or scheduling -> execution team; execution team -> customer or receiver; completed work -> finance, reporting, or support team
- Systems of record involved: Billing and Subscription Management | Network OSS/BSS | CRM

## Current-State Friction

- Where money is lost: Leakage comes from rework, poor sequencing, missed milestones, overtime, spoilage, and avoidable service failures.
- Where time is lost: Execution teams lose time on missing inputs, waiting, field coordination, status chasing, and exception resolution.
- Where human judgment dominates: Supervisors and frontline operators continually rebalance priorities, constraints, and real-world conditions.
- Where people leave the system of record: Actual execution is coordinated through calls, whiteboards, texts, and local spreadsheets when reality moves faster than the system.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, Network OSS/BSS, CRM; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, Netcracker, Ericsson.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; Netcracker; Ericsson; Salesforce CRM; Microsoft Dynamics 365 Sales
- Why this has not been solved cleanly: The workflow changes minute to minute based on field conditions, dependencies, and incomplete telemetry across teams and vendors. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
