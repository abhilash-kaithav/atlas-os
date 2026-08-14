# Clinical Documentation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Clinical and Case Operations`
- Operating systems: `Care Delivery and Reimbursement`
- Industries using this workflow: `Ambulatory health care services | Hospitals | Nursing and residential care facilities`
- Industry count: 3
- Systems-of-record categories: `EHR and Care Management | Revenue Cycle Management | Practice Management | HCM / Workforce Management | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Advance the active care or case plan safely while documenting enough context for the next accountable action.
- Trigger: An open care episode or case requires intervention, documentation, or referral follow-through.
- End outcome: The next action, service step, or referral status is updated and visible to the right owner.
- Primary actors: clinician or case worker; patient or beneficiary; care coordinator; referral or specialist partner
- Major decisions: What intervention or next step is most appropriate now?; Does the current record support safe continuation or escalation?; What coordination gap puts outcome or reimbursement at risk?
- Major handoffs: primary record owner -> specialist or downstream service provider; active service -> billing, claims, or reporting team; ongoing case -> supervisor or escalation path
- Systems of record involved: EHR and Care Management | Revenue Cycle Management | Practice Management | HCM / Workforce Management | ERP

## Current-State Friction

- Where money is lost: Leakage appears as duplicated work, missed follow-up, avoidable utilization, and incomplete billable documentation.
- Where time is lost: Teams repeatedly reconcile status and chase missing clinical, referral, or plan information.
- Where human judgment dominates: Care appropriateness, urgency, and readiness still depend on expert interpretation.
- Where people leave the system of record: Critical case context moves through phone calls, referrals, messages, and external portals.

## Software Landscape

- What software exists today: Typical stacks combine EHR and Care Management, Revenue Cycle Management, Practice Management, HCM / Workforce Management, and adjacent specialist systems; representative software in market today includes Epic, Oracle Health EHR, Meditech, PointClickCare, athenahealth RCM, R1 RCM.
- Representative vendors: Epic; Oracle Health EHR; Meditech; PointClickCare; athenahealth RCM; R1 RCM; Optum; eClinicalWorks
- Why this has not been solved cleanly: Even strong systems of record do not remove the need for contextual coordination across people and organizations. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Epic](https://www.epic.com/)
- [Oracle Health EHR](https://www.oracle.com/health/clinical-suite/electronic-health-record/)
- [athenahealth RCM](https://www.athenahealth.com/solutions/revenue-cycle-management)
- [R1 RCM](https://www.r1rcm.com/enterprise-partnerships)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Care Delivery and Reimbursement`: Delivers regulated care where access, documentation, staffing, reimbursement, and collections drive economics.
