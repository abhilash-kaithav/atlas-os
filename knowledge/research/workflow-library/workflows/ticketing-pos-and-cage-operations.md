# Ticketing, POS, and Cage Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Customer and Experience Operations`
- Operating systems: `Venue, Hospitality, and Attendance Operations`
- Industries using this workflow: `Amusements, gambling, and recreation industries`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | Ticketing and Venue Management | Revenue Management Platform | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Capture the live transaction cleanly while keeping payment, loyalty, and service context synchronized.
- Trigger: A customer is ready to order, pay, check out, or complete a live in-person transaction.
- End outcome: The transaction is completed, tender is recorded, and any downstream fulfillment or settlement record is updated.
- Primary actors: frontline cashier or associate; customer; store or venue manager; finance or reconciliation staff
- Major decisions: What tender, adjustment, or loyalty treatment should apply?; How should an exception or mismatch be resolved in the moment?; What transaction should be held, voided, or escalated?
- Major handoffs: customer interaction -> POS and payment systems; completed transaction -> fulfillment, service, or inventory team; day close -> finance and reconciliation staff
- Systems of record involved: POS and Payments | Ticketing and Venue Management | Revenue Management Platform | CRM

## Current-State Friction

- Where money is lost: Leakage appears through shrink, tender errors, bad overrides, abandoned carts, and loyalty mistakes.
- Where time is lost: Teams spend time on line delays, exception handling, and end-of-day balancing.
- Where human judgment dominates: Frontline staff still decide how to recover failures and apply judgment-based overrides.
- Where people leave the system of record: Exception handling moves into notes, supervisor conversations, and manual balancing sheets.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, Ticketing and Venue Management, Revenue Management Platform, CRM; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, Tessitura, Ticketmaster/Live Nation.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; Tessitura; Ticketmaster/Live Nation; AudienceView; Accesso
- Why this has not been solved cleanly: Core POS is mature, but live edge cases and the downstream reconciliation burden remain stubbornly human. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Toast POS](https://pos.toasttab.com/products/point-of-sale)
- [Tessitura](https://www.tessitura.com/en/Features/Ticketing-Admissions)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Venue, Hospitality, and Attendance Operations`: Monetizes capacity, reservations or ticketing, staffing, guest or attendee experience, and post-event settlement.
