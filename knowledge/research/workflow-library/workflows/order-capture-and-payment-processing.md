# Order Capture and Payment Processing

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Customer and Experience Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Other retail`
- Industry count: 1
- Systems-of-record categories: `Order Management System | Commerce Platform | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Capture the live transaction cleanly while keeping payment, loyalty, and service context synchronized.
- Trigger: A customer is ready to order, pay, check out, or complete a live in-person transaction.
- End outcome: The transaction is completed, tender is recorded, and any downstream fulfillment or settlement record is updated.
- Primary actors: frontline cashier or associate; customer; store or venue manager; finance or reconciliation staff
- Major decisions: What tender, adjustment, or loyalty treatment should apply?; How should an exception or mismatch be resolved in the moment?; What transaction should be held, voided, or escalated?
- Major handoffs: customer interaction -> POS and payment systems; completed transaction -> fulfillment, service, or inventory team; day close -> finance and reconciliation staff
- Systems of record involved: Order Management System | Commerce Platform | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Leakage appears through shrink, tender errors, bad overrides, abandoned carts, and loyalty mistakes.
- Where time is lost: Teams spend time on line delays, exception handling, and end-of-day balancing.
- Where human judgment dominates: Frontline staff still decide how to recover failures and apply judgment-based overrides.
- Where people leave the system of record: Exception handling moves into notes, supervisor conversations, and manual balancing sheets.

## Software Landscape

- What software exists today: Typical stacks combine Order Management System, Commerce Platform, Warehouse Management System, ERP; representative software in market today includes Manhattan ActiveOrder, Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail, Shopify, Blue Yonder.
- Representative vendors: Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail; Shopify; Blue Yonder; SAP; Acumatica Cloud ERP
- Why this has not been solved cleanly: Core POS is mature, but live edge cases and the downstream reconciliation burden remain stubbornly human. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
