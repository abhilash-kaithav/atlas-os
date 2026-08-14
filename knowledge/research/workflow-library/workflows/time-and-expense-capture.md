# Time and Expense Capture

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Professional Services and Matter Management`
- Industries using this workflow: `Miscellaneous professional, scientific, and technical services | Computer systems design and related services | Legal services`
- Industry count: 3
- Systems-of-record categories: `Professional Services Automation | Document Management | Practice Management and Billing | CRM | HCM / Workforce Management | ERP | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Turn completed work or contractual obligation into clean bills, timely collections, and accurate receivable records.
- Trigger: A billable event, service completion, or recurring obligation reaches the point of invoicing or follow-up.
- End outcome: The bill is issued, the receivable is updated, and collection or exception status is clear.
- Primary actors: billing specialist; collections or revenue-cycle staff; source operations team; customer or payer
- Major decisions: Is the billable record complete enough to issue or submit?; What denial, dispute, or delinquency path should be pursued next?; When should the item be escalated, adjusted, or written down?
- Major handoffs: source operations -> billing or coding team; billing -> customer, payer, or clearing partner; open item -> collections, finance, or account owner
- Systems of record involved: Professional Services Automation | Document Management | Practice Management and Billing | CRM | HCM / Workforce Management | ERP | Service Management

## Current-State Friction

- Where money is lost: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points.
- Where time is lost: Teams repeatedly reconcile source evidence, payer rules, and customer-specific exceptions.
- Where human judgment dominates: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item.
- Where people leave the system of record: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system.

## Software Landscape

- What software exists today: Typical stacks combine Professional Services Automation, Document Management, Practice Management and Billing, CRM, and adjacent specialist systems; representative software in market today includes Deltek Polaris, Deltek, Workday, ServiceNow, iManage, NetDocuments.
- Representative vendors: Deltek Polaris; Deltek; Workday; ServiceNow; iManage; NetDocuments; Litera; Thomson Reuters Elite
- Why this has not been solved cleanly: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. It typically spans 1 operating-system context and 7 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Deltek Polaris](https://www.deltek.com/products/polaris/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Professional Services and Matter Management`: Monetizes expert labor through pipeline management, staffing, delivery, work product, time capture, and client billing.
