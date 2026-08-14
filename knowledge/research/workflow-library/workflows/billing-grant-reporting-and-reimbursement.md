# Billing, Grant Reporting, and Reimbursement

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Case Management and Program Administration`
- Industries using this workflow: `Social assistance`
- Industry count: 1
- Systems-of-record categories: `Case Management System | Grant and Program Reporting | Referral Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert covered service or insured loss into adjudicated reimbursement with accurate reserves, documentation, and follow-through.
- Trigger: A claim, billable care event, or reimbursable program expense is submitted for external payment.
- End outcome: The claim is paid, denied, reserved, or escalated with a clear financial and operational status.
- Primary actors: claims or revenue-cycle specialist; payer or insurer; operations source owner; supervisor
- Major decisions: Is the submission complete and coded correctly?; What denial, reserve, or escalation path applies?; When should the issue be appealed, corrected, or closed?
- Major handoffs: service or loss record -> claims submission team; claim response -> operations, provider, or adjuster; final outcome -> finance and reporting
- Systems of record involved: Case Management System | Grant and Program Reporting | Referral Management | CRM

## Current-State Friction

- Where money is lost: Leakage comes from denials, undercoding, reserve drift, slow cycle times, and missed recovery opportunities.
- Where time is lost: Teams rework submissions, chase evidence, and manage payer or carrier correspondence repeatedly.
- Where human judgment dominates: Experienced staff interpret coverage, coding, severity, and the most effective appeal or settlement path.
- Where people leave the system of record: Supporting evidence and negotiation history live in portals, attachments, calls, and external correspondence.

## Software Landscape

- What software exists today: Typical stacks combine Case Management System, Grant and Program Reporting, Referral Management, CRM; representative software in market today includes Netsmart, WellSky, Eccovia, Apricot, Salesforce, Microsoft Dynamics 365 Sales.
- Representative vendors: Netsmart; WellSky; Eccovia; Apricot; Salesforce; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: The workflow is document-heavy, regulated, and exception-driven, with too much nuance for complete straight-through adjudication. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Case Management and Program Administration`: Coordinates intake, service plans, documentation, referrals, and funding reporting across case-based programs.
