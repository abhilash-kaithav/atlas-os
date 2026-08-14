# Blending, Logistics, and Distribution

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Process Manufacturing and Throughput Control`
- Industries using this workflow: `Petroleum and coal products`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Supply Chain Planning | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Route and fulfill demand from the right inventory or capacity source with accurate status and exception control.
- Trigger: An order is confirmed and needs allocation, release, shipment, or return handling.
- End outcome: The order is fulfilled or closed with any exception documented for downstream billing or service teams.
- Primary actors: order management team; warehouse or operations staff; customer or channel partner; transport or service partner
- Major decisions: Which inventory, facility, or path should fulfill the order?; What exception requires split shipment, reroute, substitution, or hold?; When is the order complete enough to invoice or close?
- Major handoffs: order capture -> allocation or warehouse team; warehouse or operations -> transportation or customer; completed order -> billing, returns, or support team
- Systems of record involved: Maintenance Management | Supply Chain Planning | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: Leakage shows up in split orders, mispicks, returns, expedites, and fulfillment promises that outrun actual capacity.
- Where time is lost: Teams chase inventory truth, release status, and downstream transport updates across systems.
- Where human judgment dominates: Operators still decide how to recover shortages, prioritize customers, and manage substitutions.
- Where people leave the system of record: Exception handling often happens through email, calls, and local trackers outside the formal order flow.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Supply Chain Planning, Industrial Automation and SCADA, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Blue Yonder Integrated Business Planning.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions
- Why this has not been solved cleanly: Order orchestration spans inventory, warehouse, transport, and customer systems with different clocks and constraints. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
