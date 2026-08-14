# Exception Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Network and Transportation Operations`
- Operating systems: `Transportation Network Operations`
- Industries using this workflow: `Other transportation and support activities`
- Industry count: 1
- Systems-of-record categories: `Transportation Management System | Fleet Telematics and Visibility | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain a current view of in-flight network health so downstream teams can respond before service failure compounds.
- Trigger: Movement, service, or asset status becomes uncertain, delayed, or exception-prone.
- End outcome: The exception is visible, prioritized, and owned with the next corrective action underway.
- Primary actors: control tower or exception team; carrier or field operator; customer service; operations manager
- Major decisions: Which exceptions are truly material?; What customer or downstream impact will happen if nothing changes?; Should the response be reroute, recover, reschedule, or communicate?
- Major handoffs: telemetry or event feed -> control tower; exception review -> carrier, field, or customer team; resolution -> billing, claims, or performance review
- Systems of record involved: Transportation Management System | Fleet Telematics and Visibility | ERP

## Current-State Friction

- Where money is lost: Poor visibility turns small exceptions into claims, missed commitments, and expensive recoveries.
- Where time is lost: Teams spend time validating whether the exception signal is real and who is best positioned to act.
- Where human judgment dominates: Exception severity and customer impact still require contextual interpretation.
- Where people leave the system of record: Teams fall back to calls, partner portals, and spreadsheets when telemetry is incomplete or late.

## Software Landscape

- What software exists today: Typical stacks combine Transportation Management System, Fleet Telematics and Visibility, ERP; representative software in market today includes project44, McLeod, Oracle Transportation Management, Descartes, CargoWise, Samsara.
- Representative vendors: project44; McLeod; Oracle Transportation Management; Descartes; CargoWise; Samsara; Trimble Transportation; SAP Cloud ERP
- Why this has not been solved cleanly: Visibility tools have improved, but cross-party event quality and actionability remain inconsistent. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [project44](https://www.project44.com/platform/tms/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Transportation Network Operations`: Plans capacity, routes assets, manages exceptions, and settles transport across operating networks.
