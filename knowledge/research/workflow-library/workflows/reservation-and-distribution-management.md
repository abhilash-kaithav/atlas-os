# Reservation and Distribution Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Venue, Hospitality, and Attendance Operations`
- Industries using this workflow: `Accommodation`
- Industry count: 1
- Systems-of-record categories: `Property Management System | Reservation and Distribution System | Revenue Management Platform | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert finite capacity into confirmed bookings or admissions while preserving pricing discipline and customer experience.
- Trigger: A guest, attendee, shipper, or customer requests access to a dated capacity slot.
- End outcome: Capacity is reserved, priced, and confirmed with downstream service or fulfillment teams informed.
- Primary actors: reservation or ticketing agent; customer; revenue or capacity manager; operations team
- Major decisions: What inventory should be offered at what price and under what rules?; How should holds, cancellations, and over-capacity risk be managed?; What exception needs approval or manual intervention?
- Major handoffs: customer request -> booking or ticketing system; confirmed reservation -> venue, hotel, or operations staff; completed stay or event -> settlement or service follow-up
- Systems of record involved: Property Management System | Reservation and Distribution System | Revenue Management Platform | ERP

## Current-State Friction

- Where money is lost: Leakage comes from spoilage, bad holds, channel mix mistakes, refunds, and poor yield control.
- Where time is lost: Teams burn time resolving inventory conflicts, special requests, and distribution-channel mismatches.
- Where human judgment dominates: Operators still decide how to recover service, override inventory, and handle edge-case customers.
- Where people leave the system of record: Special handling moves through calls, guest notes, and partner channels outside the clean reservation record.

## Software Landscape

- What software exists today: Typical stacks combine Property Management System, Reservation and Distribution System, Revenue Management Platform, ERP; representative software in market today includes Yardi, RealPage, AppFolio, Entrata, Mews, Cloudbeds.
- Representative vendors: Yardi; RealPage; AppFolio; Entrata; Mews; Cloudbeds; Oracle OPERA; Amadeus
- Why this has not been solved cleanly: Inventory can be digitized, but exception-heavy capacity control and live service recovery still depend on people. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Yardi](https://www.yardi.com/solution/property-management-software/)
- [Mews](https://www.mews.com/en/hospitality-management-software)
- [Cloudbeds](https://www.cloudbeds.com/property-management-system/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Venue, Hospitality, and Attendance Operations`: Monetizes capacity, reservations or ticketing, staffing, guest or attendee experience, and post-event settlement.
