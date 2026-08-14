# Billing and Collections

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Distribution and Trade Operations | Network Infrastructure Operations | Professional Services and Matter Management`
- Industries using this workflow: `Wholesale trade | Miscellaneous professional, scientific, and technical services | Broadcasting and telecommunications`
- Industry count: 3
- Systems-of-record categories: `Billing and Subscription Management | Order Management System | Professional Services Automation | Supply Chain Planning | Network OSS/BSS | Warehouse Management System | CRM | ERP | HCM / Workforce Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Turn completed work or contractual obligation into clean bills, timely collections, and accurate receivable records.
- Trigger: A billable event, service completion, or recurring obligation reaches the point of invoicing or follow-up.
- End outcome: The bill is issued, the receivable is updated, and collection or exception status is clear.
- Primary actors: billing specialist; collections or revenue-cycle staff; source operations team; customer or payer
- Major decisions: Is the billable record complete enough to issue or submit?; What denial, dispute, or delinquency path should be pursued next?; When should the item be escalated, adjusted, or written down?
- Major handoffs: source operations -> billing or coding team; billing -> customer, payer, or clearing partner; open item -> collections, finance, or account owner
- Systems of record involved: Billing and Subscription Management | Order Management System | Professional Services Automation | Supply Chain Planning | Network OSS/BSS | Warehouse Management System | CRM | ERP | HCM / Workforce Management

## Current-State Friction

- Where money is lost: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points.
- Where time is lost: Teams repeatedly reconcile source evidence, payer rules, and customer-specific exceptions.
- Where human judgment dominates: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item.
- Where people leave the system of record: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system.

## Software Landscape

- What software exists today: Typical stacks combine Billing and Subscription Management, Order Management System, Professional Services Automation, Supply Chain Planning, and adjacent specialist systems; representative software in market today includes Zuora, Amdocs, Oracle Communications, NetSuite, Manhattan ActiveOrder, Manhattan Associates.
- Representative vendors: Zuora; Amdocs; Oracle Communications; NetSuite; Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail
- Why this has not been solved cleanly: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. It typically spans 3 operating-system contexts and 9 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Zuora](https://www.zuora.com/products/billing/)
- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Deltek Polaris](https://www.deltek.com/products/polaris/)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Distribution and Trade Operations`: Coordinates suppliers, inventory, pricing, order flow, and receivables across trade networks.
- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
- `Professional Services and Matter Management`: Monetizes expert labor through pipeline management, staffing, delivery, work product, time capture, and client billing.
