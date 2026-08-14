# Estimating and Quotation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Fabricated metal products`
- Industry count: 1
- Systems-of-record categories: `Manufacturing Execution System | Shop Floor Control and Quality | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Translate demand into a priced, scoped, and approvable commercial commitment that the business can actually deliver.
- Trigger: A qualified request needs pricing, scope definition, or a formal quote, estimate, or proposal.
- End outcome: The quote or proposal is issued with approved assumptions, margins, and delivery commitments.
- Primary actors: estimator or pricing analyst; sales owner; operations or supply partner; approver
- Major decisions: What price, scope, or configuration best fits the request and margin target?; Which assumptions need approval because they materially change risk or delivery feasibility?; When should the opportunity be declined rather than priced?
- Major handoffs: qualified demand -> pricing or estimating; estimating -> operations, engineering, or supply review; approved quote -> customer or contracting team
- Systems of record involved: Manufacturing Execution System | Shop Floor Control and Quality | ERP

## Current-State Friction

- Where money is lost: Leakage comes from underpricing, scope misses, inaccurate assumptions, and change orders that were predictable at quote time.
- Where time is lost: Estimators wait on inputs, rebuild historical assumptions, and route approvals repeatedly.
- Where human judgment dominates: Estimators must judge risk, uncertainty, and customer-specific nuance that raw historical data rarely captures cleanly.
- Where people leave the system of record: The actual pricing narrative often sits in spreadsheets, markups, and offline review threads.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, Shop Floor Control and Quality, ERP; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, JobBOSS.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; JobBOSS; Infor; SAP Cloud ERP
- Why this has not been solved cleanly: Rules can price the simple path, but profitable quoting still depends on tacit knowledge and cross-functional review. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
