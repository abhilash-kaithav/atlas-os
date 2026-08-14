# Client Intake and Scope Definition

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Workforce Coordination and Service Operations`
- Industries using this workflow: `Administrative and support services`
- Industry count: 1
- Systems-of-record categories: `CRM | ERP | HCM / Workforce Management | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Admit qualified demand into the operating system with the minimum information, approvals, and commercial terms required to proceed.
- Trigger: A new prospect, participant, counterparty, or service request enters the funnel.
- End outcome: A qualified record, schedule, or agreement is created and handed to downstream planning or delivery teams.
- Primary actors: frontline intake or sales team; customer or participant; operations coordinator; approver or risk owner
- Major decisions: Is the request qualified and in policy?; What terms, slot, or service level should be offered?; Can the work proceed now or does it require more data or approval?
- Major handoffs: frontline intake -> operations scheduling; sales or intake -> finance or risk review; approved request -> delivery owner
- Systems of record involved: CRM | ERP | HCM / Workforce Management | Service Management

## Current-State Friction

- Where money is lost: Poor qualification, pricing errors, avoidable no-shows, and weak contract hygiene create leakage before execution starts.
- Where time is lost: Teams chase missing information, approvals, and schedule availability across email, phone, and shared documents.
- Where human judgment dominates: Humans still arbitrate exceptions, fit, urgency, and risk tolerance when intake data is incomplete or context is changing.
- Where people leave the system of record: Critical context lives in inboxes, call notes, PDFs, and spreadsheets before the final system record is updated.

## Software Landscape

- What software exists today: Typical stacks combine CRM, ERP, HCM / Workforce Management, Service Management; representative software in market today includes Salesforce CRM, Microsoft Dynamics 365 Sales, HubSpot CRM, VTS, Cox Automotive, SAP Cloud ERP.
- Representative vendors: Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS; Cox Automotive; SAP Cloud ERP; Acumatica Cloud ERP; Oracle
- Why this has not been solved cleanly: Structured fields handle the routine path, but real intake varies by exception, policy nuance, and local operating context. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Organizational`

## Current Vendor Research

- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Workforce Coordination and Service Operations`: Matches labor to demand, schedules execution, monitors service levels, and converts work into payroll and billing.
