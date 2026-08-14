# Order Orchestration and Fulfillment

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `General merchandise stores`
- Industry count: 1
- Systems-of-record categories: `Order Management System | Supply Chain Planning | Commerce Platform | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Route and fulfill demand from the right inventory or capacity source with accurate status and exception control.
- Trigger: An order is confirmed and needs allocation, release, shipment, or return handling.
- End outcome: The order is fulfilled or closed with any exception documented for downstream billing or service teams.
- Primary actors: order management team; warehouse or operations staff; customer or channel partner; transport or service partner
- Major decisions: Which inventory, facility, or path should fulfill the order?; What exception requires split shipment, reroute, substitution, or hold?; When is the order complete enough to invoice or close?
- Major handoffs: order capture -> allocation or warehouse team; warehouse or operations -> transportation or customer; completed order -> billing, returns, or support team
- Systems of record involved: Order Management System | Supply Chain Planning | Commerce Platform | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Leakage shows up in split orders, mispicks, returns, expedites, and fulfillment promises that outrun actual capacity.
- Where time is lost: Teams chase inventory truth, release status, and downstream transport updates across systems.
- Where human judgment dominates: Operators still decide how to recover shortages, prioritize customers, and manage substitutions.
- Where people leave the system of record: Exception handling often happens through email, calls, and local trackers outside the formal order flow.

## Software Landscape

- What software exists today: Typical stacks combine Order Management System, Supply Chain Planning, Commerce Platform, Warehouse Management System, and adjacent specialist systems; representative software in market today includes Manhattan ActiveOrder, Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail, Blue Yonder Integrated Business Planning, Kinaxis.
- Representative vendors: Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder
- Why this has not been solved cleanly: Order orchestration spans inventory, warehouse, transport, and customer systems with different clocks and constraints. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
