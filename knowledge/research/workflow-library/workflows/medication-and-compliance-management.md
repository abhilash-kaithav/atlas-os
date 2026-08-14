# Medication and Compliance Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Clinical and Case Operations`
- Operating systems: `Care Delivery and Reimbursement`
- Industries using this workflow: `Nursing and residential care facilities`
- Industry count: 1
- Systems-of-record categories: `EHR and Care Management | Revenue Cycle Management | HCM / Workforce Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain safe medication, compliance, and follow-up status while keeping the longitudinal record current.
- Trigger: Medication adherence, refill, or compliance status requires active review or intervention.
- End outcome: Medication status is updated, the next required action is completed, and exceptions are escalated appropriately.
- Primary actors: clinician or care manager; patient or resident; pharmacy partner; compliance or quality reviewer
- Major decisions: Is the patient or resident compliant enough to stay on the current plan?; What issue requires outreach, refill, or escalation?; What documentation is required to support the action taken?
- Major handoffs: care team -> pharmacy or medication partner; medication issue -> supervising clinician; resolved status -> billing, quality, or record team
- Systems of record involved: EHR and Care Management | Revenue Cycle Management | HCM / Workforce Management

## Current-State Friction

- Where money is lost: Leakage appears through avoidable readmissions, failed adherence, and unbillable documentation gaps.
- Where time is lost: Teams spend time on outreach, refill coordination, and manual follow-up loops.
- Where human judgment dominates: Medication decisions still depend on severity, tolerance, behavior, and contextual risk.
- Where people leave the system of record: Call logs, refill messages, and compliance notes often live outside the structured medication record.

## Software Landscape

- What software exists today: Typical stacks combine EHR and Care Management, Revenue Cycle Management, HCM / Workforce Management; representative software in market today includes Epic, Oracle Health EHR, Meditech, PointClickCare, athenahealth RCM, R1 RCM.
- Representative vendors: Epic; Oracle Health EHR; Meditech; PointClickCare; athenahealth RCM; R1 RCM; Optum; Workday Workforce Management
- Why this has not been solved cleanly: Medication management is highly regulated and behavior-heavy, so closed-loop automation remains incomplete. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Behavioral`

## Current Vendor Research

- [Epic](https://www.epic.com/)
- [Oracle Health EHR](https://www.oracle.com/health/clinical-suite/electronic-health-record/)
- [athenahealth RCM](https://www.athenahealth.com/solutions/revenue-cycle-management)
- [R1 RCM](https://www.r1rcm.com/enterprise-partnerships)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Care Delivery and Reimbursement`: Delivers regulated care where access, documentation, staffing, reimbursement, and collections drive economics.
