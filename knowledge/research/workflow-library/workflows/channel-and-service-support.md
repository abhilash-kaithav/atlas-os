# Channel and Service Support

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Customer and Experience Operations`
- Operating systems: `Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Electrical equipment, appliances, and components`
- Industry count: 1
- Systems-of-record categories: `Manufacturing Execution System | PLM and Engineering Design | Shop Floor Control and Quality | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Resolve customer issues quickly without sacrificing margin, service quality, or downstream operational clarity.
- Trigger: A customer asks for support, raises an issue, or requires live service intervention.
- End outcome: The issue is resolved or routed correctly and the account or service record reflects the outcome.
- Primary actors: support or service agent; customer; operations team; account owner
- Major decisions: What is the true root cause and who owns it?; Should the issue be fixed, compensated, escalated, or monitored?; What follow-up best protects future retention?
- Major handoffs: customer-facing channel -> support queue; support -> operations, field, or finance; resolution -> account owner or retention motion
- Systems of record involved: Manufacturing Execution System | PLM and Engineering Design | Shop Floor Control and Quality | ERP

## Current-State Friction

- Where money is lost: Repeat contacts, credits, field callbacks, and unresolved issues raise support cost and churn risk.
- Where time is lost: Agents and operations teams waste time on status chasing and duplicate handoffs.
- Where human judgment dominates: Good service recovery depends on empathy, prioritization, and contextual interpretation.
- Where people leave the system of record: The most important context often lives in conversations, notes, and side chats rather than system fields.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, PLM and Engineering Design, Shop Floor Control and Quality, ERP; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, Siemens Teamcenter.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; Siemens Teamcenter; Dassault 3DEXPERIENCE; PTC Windchill
- Why this has not been solved cleanly: Support flows cross channels and teams, and the edge cases that matter most remain unstructured. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
