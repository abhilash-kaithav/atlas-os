# Underwriting and Pricing

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

- Objective: Apply policy, pricing, and risk selection logic to create or maintain a defendable risk-bearing commitment.
- Trigger: A policy, quote, or underwriting action requires decision, pricing, or downstream administration.
- End outcome: The policy or underwriting decision is bound, adjusted, declined, or referred with full traceability.
- Primary actors: underwriter; distribution or account partner; policy administration staff; risk or actuarial reviewer
- Major decisions: Should the risk be written, repriced, referred, or declined?; What policy terms or endorsements best fit the exposure?; What exception requires senior review or reinsurance consideration?
- Major handoffs: distribution intake -> underwriting; approved decision -> policy administration or claims context; risk issue -> actuarial, reinsurance, or compliance review
- Systems of record involved: Claims Management | Policy Administration | Underwriting and Rating | CRM

## Current-State Friction

- Where money is lost: Leakage appears through poor risk selection, slow cycle times, mispriced endorsements, and admin rework.
- Where time is lost: Teams spend time on document collection, exception referral, and back-and-forth across policy, claims, and rating tools.
- Where human judgment dominates: Risk appetite and exposure interpretation remain highly judgment-driven even with scoring support.
- Where people leave the system of record: Key rationale lives in underwriter notes, referrals, broker calls, and exception memos outside the core flow.

## Software Landscape

- What software exists today: Typical stacks combine Claims Management, Policy Administration, Underwriting and Rating, CRM; representative software in market today includes Guidewire ClaimCenter, Duck Creek Claims, Guidewire, Duck Creek, Majesco, Verisk.
- Representative vendors: Guidewire ClaimCenter; Duck Creek Claims; Guidewire; Duck Creek; Majesco; Verisk; Guidewire PolicyCenter; Salesforce CRM
- Why this has not been solved cleanly: Insurance software is mature, but complex cases still require layered human judgment and fragmented evidence. It typically spans 1 operating-system context and 4 systems-of-record categories.
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
