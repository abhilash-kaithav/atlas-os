# Regulatory and Reinsurance Reporting

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Risk Underwriting and Claims Administration`
- Industries using this workflow: `Insurance carriers and related activities`
- Industry count: 1
- Systems-of-record categories: `Claims Management | Policy Administration | Underwriting and Rating | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Produce a compliant, decision-useful record of activity while ensuring the supporting evidence can stand up to review.
- Trigger: A formal period close, audit, regulatory filing, or quality checkpoint requires documented output.
- End outcome: The report or compliance record is submitted with evidence, exceptions, and ownership clearly documented.
- Primary actors: reporting or compliance analyst; source operations owner; manager or approver; external reviewer
- Major decisions: What source should be treated as authoritative for this report?; Which exception is material enough to disclose or remediate?; What evidence is sufficient to sign off the output?
- Major handoffs: source teams -> reporting or compliance owner; prepared output -> reviewer, auditor, or regulator; findings -> remediation owner
- Systems of record involved: Claims Management | Policy Administration | Underwriting and Rating | CRM

## Current-State Friction

- Where money is lost: Late or weak reporting creates fines, reserve exposure, rework, and management blind spots.
- Where time is lost: Teams manually stitch files, request attestations, and chase evidence for every cycle.
- Where human judgment dominates: Control owners still decide what is material, what is remediated, and what can be tolerated temporarily.
- Where people leave the system of record: Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems.

## Software Landscape

- What software exists today: Typical stacks combine Claims Management, Policy Administration, Underwriting and Rating, CRM; representative software in market today includes Guidewire ClaimCenter, Duck Creek Claims, Guidewire, Duck Creek, Majesco, Verisk.
- Representative vendors: Guidewire ClaimCenter; Duck Creek Claims; Guidewire; Duck Creek; Majesco; Verisk; Guidewire PolicyCenter; Salesforce CRM
- Why this has not been solved cleanly: The form of the report may be standardized, but the data lineage and exception handling still are not. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Guidewire ClaimCenter](https://www.guidewire.com/products/core-products/insurancesuite/claimcenter-claims-management-software)
- [Duck Creek Claims](https://www.duckcreek.com/product/claims-management-software/)
- [Guidewire PolicyCenter](https://www.guidewire.com/products/core-products/insurancesuite/policycenter-insurance-policy-administration)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Risk Underwriting and Claims Administration`: Prices risk, administers contracts, adjudicates claims, and satisfies reserving and regulatory obligations.
