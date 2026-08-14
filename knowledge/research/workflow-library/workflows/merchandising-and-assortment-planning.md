# Merchandising and Assortment Planning

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Other retail | Food and beverage stores | General merchandise stores`
- Industry count: 3
- Systems-of-record categories: `Order Management System | Supply Chain Planning | POS and Payments | Warehouse Management System | Commerce Platform | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Place inventory and assortment into the right location, age bucket, or channel before demand crystallizes.
- Trigger: Inventory, assortment, or aging conditions require an allocation or reallocation decision.
- End outcome: Inventory is assigned to the right destination with downstream replenishment and commercial actions aligned.
- Primary actors: inventory planner; merchant or commercial lead; warehouse or store operations; finance partner
- Major decisions: Where should inventory sit given expected demand and margin?; What stock should be accelerated, protected, or marked down?; When is reallocation worth the operational disruption?
- Major handoffs: demand and stock signals -> inventory planning; allocation decision -> store, warehouse, or channel team; execution outcome -> pricing and finance review
- Systems of record involved: Order Management System | Supply Chain Planning | POS and Payments | Warehouse Management System | Commerce Platform | ERP

## Current-State Friction

- Where money is lost: Misallocation drives stockouts, markdowns, carrying cost, and lost working capital productivity.
- Where time is lost: Teams spend time reconciling stock truth and coordinating transfers or aged inventory action.
- Where human judgment dominates: Operators still judge local demand and whether aged stock can truly move through the planned channel.
- Where people leave the system of record: Inventory decisions are often managed in spreadsheets and store communications outside the planning system.

## Software Landscape

- What software exists today: Typical stacks combine Order Management System, Supply Chain Planning, POS and Payments, Warehouse Management System, and adjacent specialist systems; representative software in market today includes Manhattan ActiveOrder, Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail, Blue Yonder Integrated Business Planning, Kinaxis.
- Representative vendors: Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder
- Why this has not been solved cleanly: System optimization struggles when demand is local, seasonal, and only partly observable in real time. It typically spans 1 operating-system context and 6 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Toast POS](https://pos.toasttab.com/products/point-of-sale)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
