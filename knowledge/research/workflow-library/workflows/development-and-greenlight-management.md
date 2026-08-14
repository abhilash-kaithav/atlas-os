# Development and Greenlight Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Product, Content, and Engineering`
- Operating systems: `IP, Subscription, and Rights Management`
- Industries using this workflow: `Motion picture and sound recording industries`
- Industry count: 1
- Systems-of-record categories: `Production Management | Rights and Royalty Management | CRM | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain the authoritative product, engineering, or release record so downstream execution runs against the correct definition.
- Trigger: A new product, change request, or release milestone requires controlled updates to the master record.
- End outcome: The approved version is published with dependencies and downstream impact clearly communicated.
- Primary actors: product or engineering owner; change or release manager; operations partner; commercial or legal reviewer
- Major decisions: Which change set is safe and worth promoting now?; What dependency or downstream effect blocks release?; What version should be treated as authoritative for execution?
- Major handoffs: product or design work -> engineering or release control; approved record -> manufacturing, platform, or commercial teams; released version -> support, billing, or customer-facing teams
- Systems of record involved: Production Management | Rights and Royalty Management | CRM | ERP

## Current-State Friction

- Where money is lost: Master-data mistakes and release delays create rework, scrap, missed launch windows, and downstream confusion.
- Where time is lost: Teams manually synchronize definitions across PLM, ERP, support, and commercial systems.
- Where human judgment dominates: Tradeoffs among quality, timing, and downstream disruption remain human-led.
- Where people leave the system of record: Critical rationale and version decisions live in reviews, comments, and docs outside the system of record.

## Software Landscape

- What software exists today: Typical stacks combine Production Management, Rights and Royalty Management, CRM, ERP; representative software in market today includes Movie Magic, Adobe Creative Cloud, Rightsline, Salesforce CRM, Microsoft Dynamics 365 Sales, HubSpot CRM.
- Representative vendors: Movie Magic; Adobe Creative Cloud; Rightsline; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS; Cox Automotive
- Why this has not been solved cleanly: Structured data and collaborative work still sit in separate tools, so version truth remains hard to unify. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `IP, Subscription, and Rights Management`: Develops, licenses, distributes, and accounts for content or software portfolios governed by subscriptions, rights, and recurring usage.
