# Billing, Claims, and Collections

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Care Delivery and Reimbursement`
- Industries using this workflow: `Ambulatory health care services | Hospitals | Nursing and residential care facilities`
- Industry count: 3
- Systems-of-record categories: `EHR and Care Management | Revenue Cycle Management | Practice Management | HCM / Workforce Management | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert covered service or insured loss into adjudicated reimbursement with accurate reserves, documentation, and follow-through.
- Trigger: A claim, billable care event, or reimbursable program expense is submitted for external payment.
- End outcome: The claim is paid, denied, reserved, or escalated with a clear financial and operational status.
- Primary actors: claims or revenue-cycle specialist; payer or insurer; operations source owner; supervisor
- Major decisions: Is the submission complete and coded correctly?; What denial, reserve, or escalation path applies?; When should the issue be appealed, corrected, or closed?
- Major handoffs: service or loss record -> claims submission team; claim response -> operations, provider, or adjuster; final outcome -> finance and reporting
- Systems of record involved: EHR and Care Management | Revenue Cycle Management | Practice Management | HCM / Workforce Management | ERP

## Current-State Friction

- Where money is lost: Leakage comes from denials, undercoding, reserve drift, slow cycle times, and missed recovery opportunities.
- Where time is lost: Teams rework submissions, chase evidence, and manage payer or carrier correspondence repeatedly.
- Where human judgment dominates: Experienced staff interpret coverage, coding, severity, and the most effective appeal or settlement path.
- Where people leave the system of record: Supporting evidence and negotiation history live in portals, attachments, calls, and external correspondence.

## Software Landscape

- What software exists today: Typical stacks combine EHR and Care Management, Revenue Cycle Management, Practice Management, HCM / Workforce Management, and adjacent specialist systems; representative software in market today includes Epic, Oracle Health EHR, Meditech, PointClickCare, athenahealth RCM, R1 RCM.
- Representative vendors: Epic; Oracle Health EHR; Meditech; PointClickCare; athenahealth RCM; R1 RCM; Optum; eClinicalWorks
- Why this has not been solved cleanly: The workflow is document-heavy, regulated, and exception-driven, with too much nuance for complete straight-through adjudication. It typically spans 1 operating-system context and 5 systems-of-record categories.
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
