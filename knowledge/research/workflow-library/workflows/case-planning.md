# Case Planning

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Clinical and Case Operations`
- Operating systems: `Case Management and Program Administration`
- Industries using this workflow: `Social assistance`
- Industry count: 1
- Systems-of-record categories: `Case Management System | Grant and Program Reporting | Referral Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Advance the active care or case plan safely while documenting enough context for the next accountable action.
- Trigger: An open care episode or case requires intervention, documentation, or referral follow-through.
- End outcome: The next action, service step, or referral status is updated and visible to the right owner.
- Primary actors: clinician or case worker; patient or beneficiary; care coordinator; referral or specialist partner
- Major decisions: What intervention or next step is most appropriate now?; Does the current record support safe continuation or escalation?; What coordination gap puts outcome or reimbursement at risk?
- Major handoffs: primary record owner -> specialist or downstream service provider; active service -> billing, claims, or reporting team; ongoing case -> supervisor or escalation path
- Systems of record involved: Case Management System | Grant and Program Reporting | Referral Management | CRM

## Current-State Friction

- Where money is lost: Leakage appears as duplicated work, missed follow-up, avoidable utilization, and incomplete billable documentation.
- Where time is lost: Teams repeatedly reconcile status and chase missing clinical, referral, or plan information.
- Where human judgment dominates: Care appropriateness, urgency, and readiness still depend on expert interpretation.
- Where people leave the system of record: Critical case context moves through phone calls, referrals, messages, and external portals.

## Software Landscape

- What software exists today: Typical stacks combine Case Management System, Grant and Program Reporting, Referral Management, CRM; representative software in market today includes Netsmart, WellSky, Eccovia, Apricot, Salesforce, Microsoft Dynamics 365 Sales.
- Representative vendors: Netsmart; WellSky; Eccovia; Apricot; Salesforce; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Even strong systems of record do not remove the need for contextual coordination across people and organizations. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Case Management and Program Administration`: Coordinates intake, service plans, documentation, referrals, and funding reporting across case-based programs.
