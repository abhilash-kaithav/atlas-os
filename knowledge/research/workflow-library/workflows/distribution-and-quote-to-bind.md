# Distribution and Quote-to-Bind

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Risk Underwriting and Claims Administration`
- Industries using this workflow: `Insurance carriers and related activities`
- Industry count: 1
- Systems-of-record categories: `Claims Management | Policy Administration | Underwriting and Rating | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Translate demand into a priced, scoped, and approvable commercial commitment that the business can actually deliver.
- Trigger: A qualified request needs pricing, scope definition, or a formal quote, estimate, or proposal.
- End outcome: The quote or proposal is issued with approved assumptions, margins, and delivery commitments.
- Primary actors: estimator or pricing analyst; sales owner; operations or supply partner; approver
- Major decisions: What price, scope, or configuration best fits the request and margin target?; Which assumptions need approval because they materially change risk or delivery feasibility?; When should the opportunity be declined rather than priced?
- Major handoffs: qualified demand -> pricing or estimating; estimating -> operations, engineering, or supply review; approved quote -> customer or contracting team
- Systems of record involved: Claims Management | Policy Administration | Underwriting and Rating | CRM

## Current-State Friction

- Where money is lost: Leakage comes from underpricing, scope misses, inaccurate assumptions, and change orders that were predictable at quote time.
- Where time is lost: Estimators wait on inputs, rebuild historical assumptions, and route approvals repeatedly.
- Where human judgment dominates: Estimators must judge risk, uncertainty, and customer-specific nuance that raw historical data rarely captures cleanly.
- Where people leave the system of record: The actual pricing narrative often sits in spreadsheets, markups, and offline review threads.

## Software Landscape

- What software exists today: Typical stacks combine Claims Management, Policy Administration, Underwriting and Rating, CRM; representative software in market today includes Guidewire ClaimCenter, Duck Creek Claims, Guidewire, Duck Creek, Majesco, Verisk.
- Representative vendors: Guidewire ClaimCenter; Duck Creek Claims; Guidewire; Duck Creek; Majesco; Verisk; Guidewire PolicyCenter; Salesforce CRM
- Why this has not been solved cleanly: Rules can price the simple path, but profitable quoting still depends on tacit knowledge and cross-functional review. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Guidewire ClaimCenter](https://www.guidewire.com/products/core-products/insurancesuite/claimcenter-claims-management-software)
- [Duck Creek Claims](https://www.duckcreek.com/product/claims-management-software/)
- [Guidewire PolicyCenter](https://www.guidewire.com/products/core-products/insurancesuite/policycenter-insurance-policy-administration)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Risk Underwriting and Claims Administration`: Prices risk, administers contracts, adjudicates claims, and satisfies reserving and regulatory obligations.
