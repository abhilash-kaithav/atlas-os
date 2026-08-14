# Document and Knowledge Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Product, Content, and Engineering`
- Operating systems: `Professional Services and Matter Management`
- Industries using this workflow: `Legal services`
- Industry count: 1
- Systems-of-record categories: `Document Management | Practice Management and Billing | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Protect the integrity of governed documents, rights, or knowledge while making the right version available to downstream users.
- Trigger: A document, rights position, or knowledge asset changes or is needed for downstream use.
- End outcome: The authoritative record is updated and downstream obligations or access rules are aligned.
- Primary actors: document or rights owner; legal or policy reviewer; operations user; finance or commercial partner
- Major decisions: What version or rights state is authoritative?; Who can use the asset and under what conditions?; What exception requires legal, billing, or operational review?
- Major handoffs: content or matter owner -> legal or document governance; approved asset -> downstream production, sales, or delivery team; rights or document exception -> finance or compliance review
- Systems of record involved: Document Management | Practice Management and Billing | CRM

## Current-State Friction

- Where money is lost: Leakage appears through rights misinterpretation, stale documents, missed obligations, and manual rework.
- Where time is lost: Teams search for the right version and reconcile obligations across disconnected repositories.
- Where human judgment dominates: People still interpret contractual nuance, usage rights, and which document version is good enough to act on.
- Where people leave the system of record: Key commentary and approval history sit in emails, redlines, and shared folders outside the formal index.

## Software Landscape

- What software exists today: Typical stacks combine Document Management, Practice Management and Billing, CRM; representative software in market today includes iManage, NetDocuments, Litera, Thomson Reuters Elite, Clio, Salesforce CRM.
- Representative vendors: iManage; NetDocuments; Litera; Thomson Reuters Elite; Clio; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM
- Why this has not been solved cleanly: The workflow combines unstructured content and structured obligations, which few systems model together well. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Professional Services and Matter Management`: Monetizes expert labor through pipeline management, staffing, delivery, work product, time capture, and client billing.
