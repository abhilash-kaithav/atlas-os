# Systems-of-Record Taxonomy

Last updated: 2026-08-13
Status: Active Phase 1B taxonomy

## Design Rules

- Categories normalize representative vendor stacks into comparable system types.
- Categories are inferred only from the existing census vendor fields and workflow context.
- Category labels are not market-share claims and do not add new research.
- Original vendor strings remain preserved in both the raw and normalized CSVs.

## Canonical Categories

| Category | Definition | Example Vendors | Industry Count |
| --- | --- | --- | ---: |
| ERP | Back-office systems that manage finance, operations, procurement, and core enterprise records. | SAP, Oracle, NetSuite, Infor | 31 |
| CRM | Systems that track pipeline, customer records, account activity, or relationship workflows. | Salesforce, Microsoft Dynamics 365, VTS, Cox Automotive | 18 |
| HCM / Workforce Management | Systems that manage recruiting, labor records, scheduling, payroll, and workforce capacity. | Workday, SAP SuccessFactors, UKG | 9 |
| Maintenance Management | Systems that manage preventive maintenance, work orders, asset uptime, and service history. | Yardi, ServiceTitan, Oracle Utilities, IFS | 9 |
| Manufacturing Execution System | Systems that manage production execution, plant workflows, and manufacturing traceability. | Siemens Opcenter, Plex, Epicor, Rockwell FactoryTalk | 8 |
| Supply Chain Planning | Systems that plan demand, replenishment, inventory, and sourcing across supply networks. | Blue Yonder, Manhattan Associates, Infor | 8 |
| Industrial Automation and SCADA | Operational systems that monitor or control industrial equipment, plants, and infrastructure. | AspenTech, AVEVA, Emerson, Honeywell | 6 |
| PLM and Engineering Design | Systems that manage product definitions, engineering changes, and lifecycle data. | Siemens Teamcenter, Dassault 3DEXPERIENCE, PTC Windchill, Cadence | 6 |
| Service Management | Systems that coordinate service requests, work queues, incidents, or internal delivery processes. | ServiceNow, Jira, Salesforce | 6 |
| POS and Payments | Point-of-sale systems that capture transactions, in-location demand, and payment events. | Toast, Square, Oracle MICROS, NCR Voyix | 4 |
| Shop Floor Control and Quality | Systems that manage fabrication work, shop routing, inspections, and quality records. | JobBOSS, Plex, Epicor, Infor | 4 |
| Warehouse Management System | Systems that manage inventory storage, warehouse execution, and distribution-center workflows. | Manhattan Associates, Blue Yonder, SAP | 4 |
| Billing and Subscription Management | Systems that manage recurring billing, monetization, and contract revenue events. | Zuora, Amdocs, Oracle Communications, NetSuite | 3 |
| EHR and Care Management | Clinical systems of record for patient or resident documentation and care workflows. | Epic, Oracle Health, Meditech, PointClickCare | 3 |
| Order Management System | Systems that orchestrate orders, routing, allocations, and fulfillment status. | Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail | 3 |
| Property Management System | Systems that manage tenants or guests, units or rooms, billing, and property operations. | Yardi, RealPage, AppFolio, Entrata | 3 |
| Revenue Cycle Management | Systems that manage coding, claims, patient billing, denials, and collections. | Optum, Epic, athenahealth, Oracle Health | 3 |
| Revenue Management Platform | Systems that optimize pricing, yield, or occupancy against demand and capacity. | Oracle OPERA, Sabre, Amadeus | 3 |
| Commerce Platform | Systems that run digital storefronts, catalogs, and order-capture flows. | Shopify, Salesforce Commerce Cloud, Oracle Retail | 2 |
| Fleet Telematics and Visibility | Systems that provide location, telematics, status, and proof-of-service visibility. | Samsara, project44, Trimble Transportation | 2 |
| Fund Administration and Accounting | Systems that maintain fund ledgers, administration records, and investor accounting. | SS&C, SimCorp, State Street Alpha, Clearwater | 2 |
| Investor Reporting and Performance | Systems that produce investor-facing statements, performance views, and portfolio reporting. | SS&C Advent, Clearwater, State Street Alpha | 2 |
| Loan Origination and Servicing | Systems that originate, underwrite, service, and maintain loan records. | nCino, Temenos, Dealertrack | 2 |
| Portfolio and Order Management | Systems that manage positions, portfolios, orders, and investment workflows. | Aladdin, Charles River, SimCorp, State Street Alpha | 2 |
| Professional Services Automation | Systems that manage staffing, project delivery, utilization, and invoicing for service firms. | Deltek, Workday, ServiceNow | 2 |
| Project and Construction Management | Systems that manage project schedules, field coordination, document control, and delivery status. | Procore, Autodesk Construction Cloud, Oracle Primavera | 2 |
| Ticketing and Venue Management | Systems that manage ticket inventory, venue operations, attendance, and admission workflows. | Ticketmaster/Live Nation, Tessitura, AudienceView, Accesso | 2 |
| Transportation Management System | Systems that manage shipment planning, dispatch, routing, and freight execution. | McLeod, Oracle Transportation Management, Descartes, CargoWise | 2 |
| Airline Operations and Reservations | Systems that manage airline schedules, reservations, and operating control. | Sabre, Amadeus, Navitaire, Lufthansa Systems | 1 |
| Case Management System | Systems of record for social, human-service, or care-plan casework. | Netsmart, WellSky, Eccovia, Apricot | 1 |
| Claims Management | Systems that intake, triage, adjudicate, and settle insurance claims. | Guidewire, Duck Creek, Majesco, Verisk | 1 |
| Cloud Infrastructure and IT Operations | Platforms that run core compute, hosting, identity, and operational reliability. | AWS, Microsoft Azure, Google Cloud, ServiceNow | 1 |
| Core Banking | Deposit, payments, and account-ledger systems at the center of banking operations. | Fiserv, FIS, Jack Henry, Temenos | 1 |
| Dealership Management System | Integrated sales, financing, parts, and service systems for auto dealers. | CDK Global, Reynolds and Reynolds, Tekion, Dealertrack | 1 |
| Document Management | Systems that store, version, and govern work product or regulated documents. | iManage, NetDocuments, Litera | 1 |
| EPM and Financial Consolidation | Planning and consolidation systems for enterprise finance and performance management. | Oracle EPM, Anaplan, Workday, SAP | 1 |
| Event and Donor Management | Systems that track sponsorships, donors, or event-specific revenue relationships. | Tessitura, Salesforce, Eventbrite | 1 |
| Farm Management Platform | Systems that manage crop, livestock, field, and farm planning records. | John Deere Operations Center, Climate FieldView, Granular | 1 |
| Geoscience and Reservoir Management | Systems that model geology, reserves, and subsurface development plans. | SLB Delfi, Halliburton Landmark | 1 |
| Grant and Program Reporting | Systems that track program funding usage and required reporting outputs. | Apricot, Eccovia, Salesforce | 1 |
| Learning Management System | Systems that deliver coursework, assignments, and instructional content. | Canvas, Blackboard | 1 |
| Network OSS/BSS | Systems that run telecom or network service operations, fulfillment, and commercial support. | Amdocs, Oracle Communications, Netcracker, Ericsson | 1 |
| Payments | Systems that authorize, settle, and reconcile payment flows. | Fiserv, FIS, Square, NCR Voyix | 1 |
| Policy Administration | Systems that maintain insurance products, policies, endorsements, and policy transactions. | Guidewire, Duck Creek, Majesco | 1 |
| Practice Management | Systems that manage provider schedules, visits, and operational records in ambulatory care. | athenahealth, eClinicalWorks, NextGen Healthcare | 1 |
| Practice Management and Billing | Systems that manage legal or professional-service matters, billing, and firm operations. | Thomson Reuters Elite, Clio | 1 |
| Precision Agriculture and Telematics | Systems that track farm equipment, field telemetry, and precision operating data. | John Deere Operations Center, AgLeader, Trimble Agriculture | 1 |
| Production Accounting and Regulatory | Systems that account for field production and required regulatory submissions. | Quorum, Enverus, SAP | 1 |
| Production Management | Systems that plan and coordinate project-based media or content production. | Movie Magic, Adobe Creative Cloud | 1 |
| Real Estate Asset Management | Systems that track real-estate portfolios, leasing pipelines, ownership reporting, and investor views. | CoStar, Juniper Square, MRI Software | 1 |
| Reconciliation and Reporting | Systems that reconcile balances across providers and generate formal reporting outputs. | Clearwater, State Street Alpha, SS&C Advent | 1 |
| Referral Management | Systems that coordinate referrals, handoffs, and partner-service routing. | WellSky, Netsmart | 1 |
| Rental Operations Management | Systems that manage rental inventory, reservations, checkout, utilization, and returns. | AssetWorks, LeaseQuery, Oracle, NetSuite | 1 |
| Reservation and Distribution System | Systems that manage reservations, channel distribution, and booking inventory. | Oracle OPERA, Amadeus, Mews, Cloudbeds | 1 |
| Restaurant Back Office and Inventory | Systems that manage restaurant inventory, prep, food cost, and store back office. | PAR Technology, Toast | 1 |
| Rights and Royalty Management | Systems that manage IP rights, licensing terms, royalties, and participation accounting. | Rightsline, Movie Magic, Adobe Creative Cloud | 1 |
| Risk and Compliance | Systems that monitor risk, exceptions, or regulatory obligations. | Temenos, Verisk, ServiceNow | 1 |
| Scheduling and Planning | Systems that maintain operational schedules, milestones, or planning views. | Oracle Primavera, Anaplan, Blue Yonder | 1 |
| Student Information System | Systems that manage enrollment, student records, billing, and institutional administration. | Ellucian, PowerSchool, Workday Student | 1 |
| Trading and Market Data | Systems that support trading workflows with execution, analytics, and market information. | Bloomberg, Charles River, SimCorp | 1 |
| Underwriting and Rating | Systems that support insurance risk selection, pricing, and quote decisions. | Guidewire, Duck Creek, Verisk | 1 |
| Upstream Energy Management | Systems that manage drilling, production, lease, and field-development workflows. | Enverus, SLB Delfi, Halliburton Landmark, Quorum | 1 |
| Utility Operations and Billing | Systems that manage utility customer records, meters, field assets, and billing flows. | Oracle Utilities, SAP, GE Vernova | 1 |
