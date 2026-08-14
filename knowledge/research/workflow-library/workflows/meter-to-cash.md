# Meter-to-Cash

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Utilities`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Turn completed work or contractual obligation into clean bills, timely collections, and accurate receivable records.
- Trigger: A billable event, service completion, or recurring obligation reaches the point of invoicing or follow-up.
- End outcome: The bill is issued, the receivable is updated, and collection or exception status is clear.
- Primary actors: billing specialist; collections or revenue-cycle staff; source operations team; customer or payer
- Major decisions: Is the billable record complete enough to issue or submit?; What denial, dispute, or delinquency path should be pursued next?; When should the item be escalated, adjusted, or written down?
- Major handoffs: source operations -> billing or coding team; billing -> customer, payer, or clearing partner; open item -> collections, finance, or account owner
- Systems of record involved: Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points.
- Where time is lost: Teams repeatedly reconcile source evidence, payer rules, and customer-specific exceptions.
- Where human judgment dominates: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item.
- Where people leave the system of record: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Utility Operations and Billing, Industrial Automation and SCADA, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Oracle Utilities Customer to Meter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Oracle Utilities Customer to Meter; SAP; GE Vernova
- Why this has not been solved cleanly: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Oracle Utilities Customer to Meter](https://docs.oracle.com/en/industries/energy-water/advanced-meter/index.html)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
