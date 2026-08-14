# Ticketing and Pricing

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Venue, Hospitality, and Attendance Operations`
- Industries using this workflow: `Performing arts, spectator sports, museums, and related activities`
- Industry count: 1
- Systems-of-record categories: `Ticketing and Venue Management | Event and Donor Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Convert finite capacity into confirmed bookings or admissions while preserving pricing discipline and customer experience.
- Trigger: A guest, attendee, shipper, or customer requests access to a dated capacity slot.
- End outcome: Capacity is reserved, priced, and confirmed with downstream service or fulfillment teams informed.
- Primary actors: reservation or ticketing agent; customer; revenue or capacity manager; operations team
- Major decisions: What inventory should be offered at what price and under what rules?; How should holds, cancellations, and over-capacity risk be managed?; What exception needs approval or manual intervention?
- Major handoffs: customer request -> booking or ticketing system; confirmed reservation -> venue, hotel, or operations staff; completed stay or event -> settlement or service follow-up
- Systems of record involved: Ticketing and Venue Management | Event and Donor Management | CRM

## Current-State Friction

- Where money is lost: Leakage comes from spoilage, bad holds, channel mix mistakes, refunds, and poor yield control.
- Where time is lost: Teams burn time resolving inventory conflicts, special requests, and distribution-channel mismatches.
- Where human judgment dominates: Operators still decide how to recover service, override inventory, and handle edge-case customers.
- Where people leave the system of record: Special handling moves through calls, guest notes, and partner channels outside the clean reservation record.

## Software Landscape

- What software exists today: Typical stacks combine Ticketing and Venue Management, Event and Donor Management, CRM; representative software in market today includes Tessitura, Ticketmaster/Live Nation, AudienceView, Accesso, Salesforce, Eventbrite.
- Representative vendors: Tessitura; Ticketmaster/Live Nation; AudienceView; Accesso; Salesforce; Eventbrite; Microsoft Dynamics 365 Sales; HubSpot CRM
- Why this has not been solved cleanly: Inventory can be digitized, but exception-heavy capacity control and live service recovery still depend on people. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Tessitura](https://www.tessitura.com/en/Features/Ticketing-Admissions)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Venue, Hospitality, and Attendance Operations`: Monetizes capacity, reservations or ticketing, staffing, guest or attendee experience, and post-event settlement.
