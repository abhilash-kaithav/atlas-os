# Reservation and Contract Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Rental and leasing services and lessors of intangible assets`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Rental Operations Management | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert finite capacity into confirmed bookings or admissions while preserving pricing discipline and customer experience.
- Trigger: A guest, attendee, shipper, or customer requests access to a dated capacity slot.
- End outcome: Capacity is reserved, priced, and confirmed with downstream service or fulfillment teams informed.
- Primary actors: reservation or ticketing agent; customer; revenue or capacity manager; operations team
- Major decisions: What inventory should be offered at what price and under what rules?; How should holds, cancellations, and over-capacity risk be managed?; What exception needs approval or manual intervention?
- Major handoffs: customer request -> booking or ticketing system; confirmed reservation -> venue, hotel, or operations staff; completed stay or event -> settlement or service follow-up
- Systems of record involved: Maintenance Management | Rental Operations Management | ERP

## Current-State Friction

- Where money is lost: Leakage comes from spoilage, bad holds, channel mix mistakes, refunds, and poor yield control.
- Where time is lost: Teams burn time resolving inventory conflicts, special requests, and distribution-channel mismatches.
- Where human judgment dominates: Operators still decide how to recover service, override inventory, and handle edge-case customers.
- Where people leave the system of record: Special handling moves through calls, guest notes, and partner channels outside the clean reservation record.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Rental Operations Management, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, AssetWorks.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; AssetWorks; LeaseQuery; Oracle
- Why this has not been solved cleanly: Inventory can be digitized, but exception-heavy capacity control and live service recovery still depend on people. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
