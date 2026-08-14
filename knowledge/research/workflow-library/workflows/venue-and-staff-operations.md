# Venue and Staff Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Venue, Hospitality, and Attendance Operations`
- Industries using this workflow: `Performing arts, spectator sports, museums, and related activities`
- Industry count: 1
- Systems-of-record categories: `Ticketing and Venue Management | Event and Donor Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Turn booked capacity into an on-site service experience while keeping turnover, staffing, and guest needs coordinated.
- Trigger: A guest, room, venue, or event day reaches the active service window.
- End outcome: The guest or attendee is served, the operating area is reset, and the financial record is ready for closeout.
- Primary actors: front desk or venue operations staff; housekeeping or service staff; guest or attendee; manager
- Major decisions: How should arrivals, room readiness, or guest requests be prioritized?; What issue requires compensation, maintenance, or escalation?; When is the unit or venue area ready for the next use?
- Major handoffs: reservation or ticketing -> on-site operations; operations -> housekeeping, maintenance, or finance; completed stay or event -> settlement and service recovery
- Systems of record involved: Ticketing and Venue Management | Event and Donor Management | CRM

## Current-State Friction

- Where money is lost: Leakage comes from unready inventory, labor mismatch, service recovery costs, and poor turnover discipline.
- Where time is lost: Teams lose time on room-status reconciliation, guest issue triage, and manual cross-shift communication.
- Where human judgment dominates: On-site teams continually arbitrate service tradeoffs, prioritization, and recovery.
- Where people leave the system of record: The true operating picture often lives in shift notes, radios, texts, and verbal coordination.

## Software Landscape

- What software exists today: Typical stacks combine Ticketing and Venue Management, Event and Donor Management, CRM; representative software in market today includes Tessitura, Ticketmaster/Live Nation, AudienceView, Accesso, Salesforce, Eventbrite.
- Representative vendors: Tessitura; Ticketmaster/Live Nation; AudienceView; Accesso; Salesforce; Eventbrite; Microsoft Dynamics 365 Sales; HubSpot CRM
- Why this has not been solved cleanly: Hospitality operations mix fixed capacity, live human service, and fast exceptions that spill beyond the PMS. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Organizational`

## Current Vendor Research

- [Tessitura](https://www.tessitura.com/en/Features/Ticketing-Admissions)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Venue, Hospitality, and Attendance Operations`: Monetizes capacity, reservations or ticketing, staffing, guest or attendee experience, and post-event settlement.
