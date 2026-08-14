# Revenue Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Transportation Network Operations | Venue, Hospitality, and Attendance Operations`
- Industries using this workflow: `Accommodation | Air transportation`
- Industry count: 2
- Systems-of-record categories: `Property Management System | Reservation and Distribution System | Revenue Management Platform | Airline Operations and Reservations | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Monetize fixed or perishable capacity by setting prices and controls that balance yield with occupancy or load.
- Trigger: Capacity is approaching sale or use and pricing must respond to demand, mix, and remaining availability.
- End outcome: Price, restrictions, and allocation logic are updated and visible to selling channels or operators.
- Primary actors: revenue manager; commercial analyst; sales or reservations team; operations manager
- Major decisions: What price and inventory controls maximize expected contribution?; How should channel, segment, or timing tradeoffs be handled?; When should manual overrides replace the model recommendation?
- Major handoffs: demand signals -> revenue management; pricing decision -> selling channels and frontline teams; realized performance -> finance and commercial review
- Systems of record involved: Property Management System | Reservation and Distribution System | Revenue Management Platform | Airline Operations and Reservations | ERP

## Current-State Friction

- Where money is lost: Yield is lost through blunt pricing, poor segment control, and late response to demand shifts.
- Where time is lost: Teams spend time validating model output and coordinating overrides with selling channels.
- Where human judgment dominates: Managers still incorporate local knowledge, events, and customer behavior that are only partly visible in the data.
- Where people leave the system of record: Override rationales and special-event plans often live in spreadsheets and meetings outside the pricing engine.

## Software Landscape

- What software exists today: Typical stacks combine Property Management System, Reservation and Distribution System, Revenue Management Platform, Airline Operations and Reservations, and adjacent specialist systems; representative software in market today includes Yardi, RealPage, AppFolio, Entrata, Mews, Cloudbeds.
- Representative vendors: Yardi; RealPage; AppFolio; Entrata; Mews; Cloudbeds; Oracle OPERA; Amadeus
- Why this has not been solved cleanly: Optimization is strong, but last-mile trust and local exception handling keep humans in the loop. It typically spans 2 operating-system contexts and 5 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Yardi](https://www.yardi.com/solution/property-management-software/)
- [Mews](https://www.mews.com/en/hospitality-management-software)
- [Cloudbeds](https://www.cloudbeds.com/property-management-system/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Transportation Network Operations`: Plans capacity, routes assets, manages exceptions, and settles transport across operating networks.
- `Venue, Hospitality, and Attendance Operations`: Monetizes capacity, reservations or ticketing, staffing, guest or attendee experience, and post-event settlement.
