#!/usr/bin/env python3
"""Normalize the Atlas Top 50 industry census into canonical Phase 1B taxonomies."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CENSUS_DIR = ROOT / "knowledge" / "research" / "industry-census"
SOURCE_CSV = CENSUS_DIR / "top-50-industry-census.csv"
NORMALIZED_CSV = CENSUS_DIR / "top-50-industry-census-normalized.csv"
OPERATING_SYSTEM_DOC = CENSUS_DIR / "operating-system-taxonomy.md"
WORKFLOW_DOC = CENSUS_DIR / "workflow-taxonomy.md"
SYSTEM_DOC = CENSUS_DIR / "systems-of-record-taxonomy.md"
SUMMARY_DOC = CENSUS_DIR / "phase-1b-normalization-summary.md"

GENERATED_DATE = "2026-08-13"


def escape_md(value: str) -> str:
    return value.replace("|", "\\|")


OPERATING_SYSTEM_DEFINITIONS = {
    "Asset Utilization and Lease Management": (
        "Monetizes owned or controlled assets through occupancy or utilization, "
        "contract terms, maintenance, turnover, and billing discipline."
    ),
    "Capital Markets and Investment Management": (
        "Manages portfolios, trades, valuation, reporting, and compliance for "
        "entrusted capital."
    ),
    "Care Delivery and Reimbursement": (
        "Delivers regulated care where access, documentation, staffing, "
        "reimbursement, and collections drive economics."
    ),
    "Case Management and Program Administration": (
        "Coordinates intake, service plans, documentation, referrals, and funding "
        "reporting across case-based programs."
    ),
    "Digital Platform and Subscription Operations": (
        "Monetizes digital products or infrastructure through release velocity, "
        "onboarding, billing, retention, and service reliability."
    ),
    "Deposit, Credit, and Payment Intermediation": (
        "Grows and services deposits and credit while managing payments, losses, "
        "exceptions, and regulation."
    ),
    "Distribution and Trade Operations": (
        "Coordinates suppliers, inventory, pricing, order flow, and receivables "
        "across trade networks."
    ),
    "Education Delivery and Administration": (
        "Recruits participants, staffs schedules, delivers instruction, supports "
        "outcomes, and administers funding or reporting."
    ),
    "Enterprise Governance and Shared Services": (
        "Allocates capital and coordinates governance, finance, shared services, "
        "and performance across business units."
    ),
    "Field Production and Resource Extraction": (
        "Converts land or reserves into output through field planning, operations, "
        "logistics, and revenue or regulatory management."
    ),
    "IP, Subscription, and Rights Management": (
        "Develops, licenses, distributes, and accounts for content or software "
        "portfolios governed by subscriptions, rights, and recurring usage."
    ),
    "Network Infrastructure Operations": (
        "Operates capital-intensive service networks through planning, "
        "provisioning, reliability, billing, and regulatory control."
    ),
    "Process Manufacturing and Throughput Control": (
        "Converts feedstocks into standardized output through planning, process "
        "control, quality, maintenance, and logistics."
    ),
    "Product Manufacturing and Lifecycle Operations": (
        "Designs, plans, manufactures, certifies, fulfills, and supports discrete "
        "products across supplier and channel networks."
    ),
    "Professional Services and Matter Management": (
        "Monetizes expert labor through pipeline management, staffing, delivery, "
        "work product, time capture, and client billing."
    ),
    "Project Delivery and Contracting": (
        "Delivers scoped projects through estimation, scheduling, subcontractor "
        "coordination, field execution, and progress billing."
    ),
    "Retail and Service Commerce": (
        "Monetizes traffic, assortment, transactions, service execution, labor, "
        "and repeat demand across commerce channels."
    ),
    "Risk Underwriting and Claims Administration": (
        "Prices risk, administers contracts, adjudicates claims, and satisfies "
        "reserving and regulatory obligations."
    ),
    "Transportation Network Operations": (
        "Plans capacity, routes assets, manages exceptions, and settles transport "
        "across operating networks."
    ),
    "Venue, Hospitality, and Attendance Operations": (
        "Monetizes capacity, reservations or ticketing, staffing, guest or "
        "attendee experience, and post-event settlement."
    ),
    "Workforce Coordination and Service Operations": (
        "Matches labor to demand, schedules execution, monitors service levels, "
        "and converts work into payroll and billing."
    ),
}

WORKFLOW_FAMILY_DEFINITIONS = {
    "Access, Intake, and Contracting": (
        "Work that acquires demand, qualifies participants, creates contracts, "
        "and admits work into the system."
    ),
    "Clinical and Case Operations": (
        "Care, case, and documentation workflows that govern ongoing service "
        "delivery in regulated human-service environments."
    ),
    "Customer and Experience Operations": (
        "Frontline workflows that shape order capture, service experience, "
        "retention, loyalty, and aftermarket relationships."
    ),
    "Delivery and Service Execution": (
        "Operational workflows that fulfill orders, deliver projects, perform "
        "fieldwork, or execute day-to-day service."
    ),
    "Finance and Revenue Operations": (
        "Billing, claims, accounting, settlement, reconciliation, and cash "
        "realization workflows."
    ),
    "Governance and Portfolio Operations": (
        "Capital allocation, investor reporting, consolidation, and oversight "
        "workflows."
    ),
    "Network and Transportation Operations": (
        "Routing, dispatch, provisioning, booking, visibility, and exception "
        "workflows for moving assets or service capacity."
    ),
    "Planning and Allocation": (
        "Demand, capacity, schedule, production, or portfolio planning workflows "
        "that allocate constrained resources."
    ),
    "Product, Content, and Engineering": (
        "Workflows that define products, content, rights, releases, engineering "
        "changes, or work-product management."
    ),
    "Production and Asset Operations": (
        "Workflows that operate plants, assets, equipment, inventory, or physical "
        "locations."
    ),
    "Risk, Compliance, and Reporting": (
        "Workflows that enforce rules, monitor risk, maintain quality, and produce "
        "regulatory or certification outputs."
    ),
    "Sourcing and Supply": (
        "Workflows that secure inputs, manage suppliers, and coordinate "
        "replenishment."
    ),
    "Workforce and Labor Operations": (
        "Recruiting, staffing, tasking, scheduling, and labor-deployment "
        "workflows."
    ),
}

SYSTEM_CATEGORY_DEFINITIONS = {
    "Airline Operations and Reservations": "Systems that manage airline schedules, reservations, and operating control.",
    "Billing and Subscription Management": "Systems that manage recurring billing, monetization, and contract revenue events.",
    "Case Management System": "Systems of record for social, human-service, or care-plan casework.",
    "Claims Management": "Systems that intake, triage, adjudicate, and settle insurance claims.",
    "Cloud Infrastructure and IT Operations": "Platforms that run core compute, hosting, identity, and operational reliability.",
    "Commerce Platform": "Systems that run digital storefronts, catalogs, and order-capture flows.",
    "Core Banking": "Deposit, payments, and account-ledger systems at the center of banking operations.",
    "CRM": "Systems that track pipeline, customer records, account activity, or relationship workflows.",
    "Dealership Management System": "Integrated sales, financing, parts, and service systems for auto dealers.",
    "Document Management": "Systems that store, version, and govern work product or regulated documents.",
    "EHR and Care Management": "Clinical systems of record for patient or resident documentation and care workflows.",
    "EPM and Financial Consolidation": "Planning and consolidation systems for enterprise finance and performance management.",
    "ERP": "Back-office systems that manage finance, operations, procurement, and core enterprise records.",
    "Event and Donor Management": "Systems that track sponsorships, donors, or event-specific revenue relationships.",
    "Farm Management Platform": "Systems that manage crop, livestock, field, and farm planning records.",
    "Fleet Telematics and Visibility": "Systems that provide location, telematics, status, and proof-of-service visibility.",
    "Fund Administration and Accounting": "Systems that maintain fund ledgers, administration records, and investor accounting.",
    "Geoscience and Reservoir Management": "Systems that model geology, reserves, and subsurface development plans.",
    "Grant and Program Reporting": "Systems that track program funding usage and required reporting outputs.",
    "HCM / Workforce Management": "Systems that manage recruiting, labor records, scheduling, payroll, and workforce capacity.",
    "Industrial Automation and SCADA": "Operational systems that monitor or control industrial equipment, plants, and infrastructure.",
    "Investor Reporting and Performance": "Systems that produce investor-facing statements, performance views, and portfolio reporting.",
    "Learning Management System": "Systems that deliver coursework, assignments, and instructional content.",
    "Loan Origination and Servicing": "Systems that originate, underwrite, service, and maintain loan records.",
    "Maintenance Management": "Systems that manage preventive maintenance, work orders, asset uptime, and service history.",
    "Manufacturing Execution System": "Systems that manage production execution, plant workflows, and manufacturing traceability.",
    "Network OSS/BSS": "Systems that run telecom or network service operations, fulfillment, and commercial support.",
    "Order Management System": "Systems that orchestrate orders, routing, allocations, and fulfillment status.",
    "Payments": "Systems that authorize, settle, and reconcile payment flows.",
    "PLM and Engineering Design": "Systems that manage product definitions, engineering changes, and lifecycle data.",
    "Policy Administration": "Systems that maintain insurance products, policies, endorsements, and policy transactions.",
    "Portfolio and Order Management": "Systems that manage positions, portfolios, orders, and investment workflows.",
    "POS and Payments": "Point-of-sale systems that capture transactions, in-location demand, and payment events.",
    "Practice Management": "Systems that manage provider schedules, visits, and operational records in ambulatory care.",
    "Practice Management and Billing": "Systems that manage legal or professional-service matters, billing, and firm operations.",
    "Precision Agriculture and Telematics": "Systems that track farm equipment, field telemetry, and precision operating data.",
    "Production Accounting and Regulatory": "Systems that account for field production and required regulatory submissions.",
    "Production Management": "Systems that plan and coordinate project-based media or content production.",
    "Professional Services Automation": "Systems that manage staffing, project delivery, utilization, and invoicing for service firms.",
    "Project and Construction Management": "Systems that manage project schedules, field coordination, document control, and delivery status.",
    "Property Management System": "Systems that manage tenants or guests, units or rooms, billing, and property operations.",
    "Real Estate Asset Management": "Systems that track real-estate portfolios, leasing pipelines, ownership reporting, and investor views.",
    "Reconciliation and Reporting": "Systems that reconcile balances across providers and generate formal reporting outputs.",
    "Referral Management": "Systems that coordinate referrals, handoffs, and partner-service routing.",
    "Reservation and Distribution System": "Systems that manage reservations, channel distribution, and booking inventory.",
    "Restaurant Back Office and Inventory": "Systems that manage restaurant inventory, prep, food cost, and store back office.",
    "Rental Operations Management": "Systems that manage rental inventory, reservations, checkout, utilization, and returns.",
    "Revenue Cycle Management": "Systems that manage coding, claims, patient billing, denials, and collections.",
    "Revenue Management Platform": "Systems that optimize pricing, yield, or occupancy against demand and capacity.",
    "Rights and Royalty Management": "Systems that manage IP rights, licensing terms, royalties, and participation accounting.",
    "Risk and Compliance": "Systems that monitor risk, exceptions, or regulatory obligations.",
    "Scheduling and Planning": "Systems that maintain operational schedules, milestones, or planning views.",
    "Service Management": "Systems that coordinate service requests, work queues, incidents, or internal delivery processes.",
    "Shop Floor Control and Quality": "Systems that manage fabrication work, shop routing, inspections, and quality records.",
    "Student Information System": "Systems that manage enrollment, student records, billing, and institutional administration.",
    "Supply Chain Planning": "Systems that plan demand, replenishment, inventory, and sourcing across supply networks.",
    "Ticketing and Venue Management": "Systems that manage ticket inventory, venue operations, attendance, and admission workflows.",
    "Trading and Market Data": "Systems that support trading workflows with execution, analytics, and market information.",
    "Transportation Management System": "Systems that manage shipment planning, dispatch, routing, and freight execution.",
    "Underwriting and Rating": "Systems that support insurance risk selection, pricing, and quote decisions.",
    "Upstream Energy Management": "Systems that manage drilling, production, lease, and field-development workflows.",
    "Utility Operations and Billing": "Systems that manage utility customer records, meters, field assets, and billing flows.",
    "Warehouse Management System": "Systems that manage inventory storage, warehouse execution, and distribution-center workflows.",
}

SYSTEM_CATEGORY_EXAMPLES = {
    "Airline Operations and Reservations": ["Sabre", "Amadeus", "Navitaire", "Lufthansa Systems"],
    "Billing and Subscription Management": ["Zuora", "Amdocs", "Oracle Communications", "NetSuite"],
    "Case Management System": ["Netsmart", "WellSky", "Eccovia", "Apricot"],
    "Claims Management": ["Guidewire", "Duck Creek", "Majesco", "Verisk"],
    "Cloud Infrastructure and IT Operations": ["AWS", "Microsoft Azure", "Google Cloud", "ServiceNow"],
    "Commerce Platform": ["Shopify", "Salesforce Commerce Cloud", "Oracle Retail"],
    "Core Banking": ["Fiserv", "FIS", "Jack Henry", "Temenos"],
    "CRM": ["Salesforce", "Microsoft Dynamics 365", "VTS", "Cox Automotive"],
    "Dealership Management System": ["CDK Global", "Reynolds and Reynolds", "Tekion", "Dealertrack"],
    "Document Management": ["iManage", "NetDocuments", "Litera"],
    "EHR and Care Management": ["Epic", "Oracle Health", "Meditech", "PointClickCare"],
    "EPM and Financial Consolidation": ["Oracle EPM", "Anaplan", "Workday", "SAP"],
    "ERP": ["SAP", "Oracle", "NetSuite", "Infor"],
    "Event and Donor Management": ["Tessitura", "Salesforce", "Eventbrite"],
    "Farm Management Platform": ["John Deere Operations Center", "Climate FieldView", "Granular"],
    "Fleet Telematics and Visibility": ["Samsara", "project44", "Trimble Transportation"],
    "Fund Administration and Accounting": ["SS&C", "SimCorp", "State Street Alpha", "Clearwater"],
    "Geoscience and Reservoir Management": ["SLB Delfi", "Halliburton Landmark"],
    "Grant and Program Reporting": ["Apricot", "Eccovia", "Salesforce"],
    "HCM / Workforce Management": ["Workday", "SAP SuccessFactors", "UKG"],
    "Industrial Automation and SCADA": ["AspenTech", "AVEVA", "Emerson", "Honeywell"],
    "Investor Reporting and Performance": ["SS&C Advent", "Clearwater", "State Street Alpha"],
    "Learning Management System": ["Canvas", "Blackboard"],
    "Loan Origination and Servicing": ["nCino", "Temenos", "Dealertrack"],
    "Maintenance Management": ["Yardi", "ServiceTitan", "Oracle Utilities", "IFS"],
    "Manufacturing Execution System": ["Siemens Opcenter", "Plex", "Epicor", "Rockwell FactoryTalk"],
    "Network OSS/BSS": ["Amdocs", "Oracle Communications", "Netcracker", "Ericsson"],
    "Order Management System": ["Manhattan Associates", "Salesforce Commerce Cloud", "Oracle Retail"],
    "Payments": ["Fiserv", "FIS", "Square", "NCR Voyix"],
    "PLM and Engineering Design": ["Siemens Teamcenter", "Dassault 3DEXPERIENCE", "PTC Windchill", "Cadence"],
    "Policy Administration": ["Guidewire", "Duck Creek", "Majesco"],
    "Portfolio and Order Management": ["Aladdin", "Charles River", "SimCorp", "State Street Alpha"],
    "POS and Payments": ["Toast", "Square", "Oracle MICROS", "NCR Voyix"],
    "Practice Management": ["athenahealth", "eClinicalWorks", "NextGen Healthcare"],
    "Practice Management and Billing": ["Thomson Reuters Elite", "Clio"],
    "Precision Agriculture and Telematics": ["John Deere Operations Center", "AgLeader", "Trimble Agriculture"],
    "Production Accounting and Regulatory": ["Quorum", "Enverus", "SAP"],
    "Production Management": ["Movie Magic", "Adobe Creative Cloud"],
    "Professional Services Automation": ["Deltek", "Workday", "ServiceNow"],
    "Project and Construction Management": ["Procore", "Autodesk Construction Cloud", "Oracle Primavera"],
    "Property Management System": ["Yardi", "RealPage", "AppFolio", "Entrata"],
    "Real Estate Asset Management": ["CoStar", "Juniper Square", "MRI Software"],
    "Reconciliation and Reporting": ["Clearwater", "State Street Alpha", "SS&C Advent"],
    "Referral Management": ["WellSky", "Netsmart"],
    "Reservation and Distribution System": ["Oracle OPERA", "Amadeus", "Mews", "Cloudbeds"],
    "Restaurant Back Office and Inventory": ["PAR Technology", "Toast"],
    "Rental Operations Management": ["AssetWorks", "LeaseQuery", "Oracle", "NetSuite"],
    "Revenue Cycle Management": ["Optum", "Epic", "athenahealth", "Oracle Health"],
    "Revenue Management Platform": ["Oracle OPERA", "Sabre", "Amadeus"],
    "Rights and Royalty Management": ["Rightsline", "Movie Magic", "Adobe Creative Cloud"],
    "Risk and Compliance": ["Temenos", "Verisk", "ServiceNow"],
    "Scheduling and Planning": ["Oracle Primavera", "Anaplan", "Blue Yonder"],
    "Service Management": ["ServiceNow", "Jira", "Salesforce"],
    "Shop Floor Control and Quality": ["JobBOSS", "Plex", "Epicor", "Infor"],
    "Student Information System": ["Ellucian", "PowerSchool", "Workday Student"],
    "Supply Chain Planning": ["Blue Yonder", "Manhattan Associates", "Infor"],
    "Ticketing and Venue Management": ["Ticketmaster/Live Nation", "Tessitura", "AudienceView", "Accesso"],
    "Trading and Market Data": ["Bloomberg", "Charles River", "SimCorp"],
    "Transportation Management System": ["McLeod", "Oracle Transportation Management", "Descartes", "CargoWise"],
    "Underwriting and Rating": ["Guidewire", "Duck Creek", "Verisk"],
    "Upstream Energy Management": ["Enverus", "SLB Delfi", "Halliburton Landmark", "Quorum"],
    "Utility Operations and Billing": ["Oracle Utilities", "SAP", "GE Vernova"],
    "Warehouse Management System": ["Manhattan Associates", "Blue Yonder", "SAP"],
}

INDUSTRY_NORMALIZATION = {
    "Housing": {
        "canonical_operating_system": "Asset Utilization and Lease Management",
        "canonical_workflows": [
            ("Lease Acquisition and Renewal", "Access, Intake, and Contracting"),
            ("Billing, Collections, and Cash Application", "Finance and Revenue Operations"),
            ("Asset Maintenance and Work Orders", "Production and Asset Operations"),
            ("Turnover and Readiness Management", "Production and Asset Operations"),
            ("Capital Planning and Compliance Reporting", "Governance and Portfolio Operations"),
        ],
        "systems_of_record_categories": [
            "Property Management System",
            "CRM",
            "Maintenance Management",
        ],
    },
    "Wholesale trade": {
        "canonical_operating_system": "Distribution and Trade Operations",
        "canonical_workflows": [
            ("Demand Planning", "Planning and Allocation"),
            ("Procurement and Replenishment", "Sourcing and Supply"),
            ("Pricing and Quoting", "Access, Intake, and Contracting"),
            ("Order Management and Fulfillment", "Delivery and Service Execution"),
            ("Billing and Collections", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Supply Chain Planning",
            "Warehouse Management System",
            "Order Management System",
        ],
    },
    "Construction": {
        "canonical_operating_system": "Project Delivery and Contracting",
        "canonical_workflows": [
            ("Estimating and Proposal Management", "Access, Intake, and Contracting"),
            ("Project Scheduling and Resource Planning", "Planning and Allocation"),
            ("Supplier and Subcontractor Management", "Sourcing and Supply"),
            ("Field Execution and Change Management", "Delivery and Service Execution"),
            ("Progress Billing and Compliance Administration", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Project and Construction Management",
            "Scheduling and Planning",
            "ERP",
        ],
    },
    "Miscellaneous professional, scientific, and technical services": {
        "canonical_operating_system": "Professional Services and Matter Management",
        "canonical_workflows": [
            ("Lead and Proposal Management", "Access, Intake, and Contracting"),
            ("Staffing and Capacity Planning", "Workforce and Labor Operations"),
            ("Project Delivery", "Delivery and Service Execution"),
            ("Time and Expense Capture", "Finance and Revenue Operations"),
            ("Billing and Collections", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "CRM",
            "HCM / Workforce Management",
            "Professional Services Automation",
            "ERP",
        ],
    },
    "Other real estate": {
        "canonical_operating_system": "Asset Utilization and Lease Management",
        "canonical_workflows": [
            ("Lease Acquisition and Pipeline Management", "Access, Intake, and Contracting"),
            ("Asset and Investor Reporting", "Governance and Portfolio Operations"),
            ("Asset Maintenance and Work Orders", "Production and Asset Operations"),
            ("Billing and Reconciliation", "Finance and Revenue Operations"),
            ("Capital Planning and Compliance Reporting", "Governance and Portfolio Operations"),
        ],
        "systems_of_record_categories": [
            "Property Management System",
            "Real Estate Asset Management",
            "CRM",
            "Fund Administration and Accounting",
        ],
    },
    "Ambulatory health care services": {
        "canonical_operating_system": "Care Delivery and Reimbursement",
        "canonical_workflows": [
            ("Access, Intake, and Scheduling", "Access, Intake, and Contracting"),
            ("Eligibility and Authorization", "Access, Intake, and Contracting"),
            ("Clinical Documentation", "Clinical and Case Operations"),
            ("Coding and Charge Capture", "Finance and Revenue Operations"),
            ("Billing, Claims, and Collections", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "EHR and Care Management",
            "Practice Management",
            "Revenue Cycle Management",
        ],
    },
    "Other retail": {
        "canonical_operating_system": "Retail and Service Commerce",
        "canonical_workflows": [
            ("Merchandising and Assortment Planning", "Planning and Allocation"),
            ("Inventory Allocation and Replenishment", "Planning and Allocation"),
            ("Order Capture and Payment Processing", "Customer and Experience Operations"),
            ("Fulfillment and Returns Management", "Delivery and Service Execution"),
            ("Pricing and Promotion Management", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "Commerce Platform",
            "ERP",
            "Order Management System",
            "Warehouse Management System",
        ],
    },
    "Insurance carriers and related activities": {
        "canonical_operating_system": "Risk Underwriting and Claims Administration",
        "canonical_workflows": [
            ("Distribution and Quote-to-Bind", "Access, Intake, and Contracting"),
            ("Underwriting and Pricing", "Risk, Compliance, and Reporting"),
            ("Policy Administration", "Risk, Compliance, and Reporting"),
            ("Claims Administration", "Finance and Revenue Operations"),
            ("Regulatory and Reinsurance Reporting", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "Policy Administration",
            "Claims Management",
            "Underwriting and Rating",
            "CRM",
        ],
    },
    "Federal Reserve banks, credit intermediation, and related activities": {
        "canonical_operating_system": "Deposit, Credit, and Payment Intermediation",
        "canonical_workflows": [
            ("Account and Loan Onboarding", "Access, Intake, and Contracting"),
            ("Deposit and Payment Operations", "Finance and Revenue Operations"),
            ("Credit Underwriting and Servicing", "Finance and Revenue Operations"),
            ("Risk and Compliance Monitoring", "Risk, Compliance, and Reporting"),
            ("Collections and Loss Mitigation", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Core Banking",
            "Loan Origination and Servicing",
            "Payments",
            "Risk and Compliance",
            "CRM",
        ],
    },
    "Food services and drinking places": {
        "canonical_operating_system": "Retail and Service Commerce",
        "canonical_workflows": [
            ("Workforce Scheduling", "Workforce and Labor Operations"),
            ("Procurement and Prep Management", "Sourcing and Supply"),
            ("Point-of-Sale and Order Flow", "Customer and Experience Operations"),
            ("Service Execution", "Delivery and Service Execution"),
            ("Cash and Inventory Reconciliation", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "POS and Payments",
            "Restaurant Back Office and Inventory",
            "HCM / Workforce Management",
        ],
    },
    "Administrative and support services": {
        "canonical_operating_system": "Workforce Coordination and Service Operations",
        "canonical_workflows": [
            ("Client Intake and Scope Definition", "Access, Intake, and Contracting"),
            ("Recruiting and Work Assignment", "Workforce and Labor Operations"),
            ("Workforce Scheduling", "Workforce and Labor Operations"),
            ("Service-Level Monitoring", "Governance and Portfolio Operations"),
            ("Payroll, Billing, and Reconciliation", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "HCM / Workforce Management",
            "CRM",
            "Service Management",
            "ERP",
        ],
    },
    "Hospitals": {
        "canonical_operating_system": "Care Delivery and Reimbursement",
        "canonical_workflows": [
            ("Access, Admissions, and Throughput Management", "Access, Intake, and Contracting"),
            ("Clinical Documentation", "Clinical and Case Operations"),
            ("Care Coordination and Order Management", "Clinical and Case Operations"),
            ("Billing, Claims, and Collections", "Finance and Revenue Operations"),
            ("Payer Contract Management", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "EHR and Care Management",
            "Revenue Cycle Management",
            "HCM / Workforce Management",
            "ERP",
        ],
    },
    "Food and beverage and tobacco products": {
        "canonical_operating_system": "Process Manufacturing and Throughput Control",
        "canonical_workflows": [
            ("Demand Planning", "Planning and Allocation"),
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning and Process Control", "Production and Asset Operations"),
            ("Regulatory Labeling and Compliance", "Risk, Compliance, and Reporting"),
            ("Distribution and Trade Promotion", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Supply Chain Planning",
            "Manufacturing Execution System",
            "Industrial Automation and SCADA",
        ],
    },
    "Other services, except government": {
        "canonical_operating_system": "Workforce Coordination and Service Operations",
        "canonical_workflows": [
            ("Lead Intake and Scheduling", "Access, Intake, and Contracting"),
            ("Workforce Scheduling and Dispatch", "Workforce and Labor Operations"),
            ("Field Service Execution", "Delivery and Service Execution"),
            ("Billing and Payment Processing", "Finance and Revenue Operations"),
            ("Customer Retention and Repeat Service", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "CRM",
            "POS and Payments",
            "HCM / Workforce Management",
            "Service Management",
        ],
    },
    "Securities, commodity contracts, and investments": {
        "canonical_operating_system": "Capital Markets and Investment Management",
        "canonical_workflows": [
            ("Client Onboarding and KYC", "Access, Intake, and Contracting"),
            ("Portfolio and Order Management", "Governance and Portfolio Operations"),
            ("Trade Execution and Settlement", "Finance and Revenue Operations"),
            ("Risk and Compliance Surveillance", "Risk, Compliance, and Reporting"),
            ("Investor Reporting and Performance", "Governance and Portfolio Operations"),
        ],
        "systems_of_record_categories": [
            "Portfolio and Order Management",
            "Trading and Market Data",
            "CRM",
            "Investor Reporting and Performance",
        ],
    },
    "Chemical products": {
        "canonical_operating_system": "Process Manufacturing and Throughput Control",
        "canonical_workflows": [
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning and Process Control", "Production and Asset Operations"),
            ("Quality, Safety, and Environmental Management", "Risk, Compliance, and Reporting"),
            ("Order Management and Fulfillment", "Delivery and Service Execution"),
            ("Contract and Margin Management", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Industrial Automation and SCADA",
            "Manufacturing Execution System",
            "Maintenance Management",
        ],
    },
    "Data processing, internet publishing, and other information services": {
        "canonical_operating_system": "Digital Platform and Subscription Operations",
        "canonical_workflows": [
            ("Infrastructure Capacity Planning", "Planning and Allocation"),
            ("Product and Content Release Management", "Product, Content, and Engineering"),
            ("Customer Acquisition and Onboarding", "Access, Intake, and Contracting"),
            ("Usage Billing and Monetization", "Finance and Revenue Operations"),
            ("Reliability and Security Operations", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "Cloud Infrastructure and IT Operations",
            "CRM",
            "Service Management",
            "Billing and Subscription Management",
        ],
    },
    "Broadcasting and telecommunications": {
        "canonical_operating_system": "Network Infrastructure Operations",
        "canonical_workflows": [
            ("Network Planning and Capital Management", "Planning and Allocation"),
            ("Service Provisioning and Activation", "Network and Transportation Operations"),
            ("Content and Service Operations", "Delivery and Service Execution"),
            ("Billing and Collections", "Finance and Revenue Operations"),
            ("Outage and Regulatory Management", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "Network OSS/BSS",
            "Billing and Subscription Management",
            "CRM",
        ],
    },
    "Management of companies and enterprises": {
        "canonical_operating_system": "Enterprise Governance and Shared Services",
        "canonical_workflows": [
            ("Capital Allocation and Planning", "Governance and Portfolio Operations"),
            ("Financial Consolidation", "Governance and Portfolio Operations"),
            ("Governance and Risk Review", "Governance and Portfolio Operations"),
            ("Shared Service Operations", "Governance and Portfolio Operations"),
            ("Performance Management", "Governance and Portfolio Operations"),
        ],
        "systems_of_record_categories": [
            "EPM and Financial Consolidation",
            "ERP",
            "HCM / Workforce Management",
            "Service Management",
        ],
    },
    "Computer systems design and related services": {
        "canonical_operating_system": "Professional Services and Matter Management",
        "canonical_workflows": [
            ("Lead and Proposal Management", "Access, Intake, and Contracting"),
            ("Staffing and Capacity Planning", "Workforce and Labor Operations"),
            ("Project Delivery", "Delivery and Service Execution"),
            ("Time and Expense Capture", "Finance and Revenue Operations"),
            ("Renewal and Account Expansion", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "CRM",
            "HCM / Workforce Management",
            "Professional Services Automation",
            "Service Management",
        ],
    },
    "Motor vehicles, bodies and trailers, and parts": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Program and Platform Planning", "Planning and Allocation"),
            ("Supplier Scheduling and Procurement", "Sourcing and Supply"),
            ("Shop Floor Execution and Quality Management", "Production and Asset Operations"),
            ("Logistics and Channel Fulfillment", "Delivery and Service Execution"),
            ("Aftermarket Service and Field Support", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "PLM and Engineering Design",
            "Manufacturing Execution System",
            "Supply Chain Planning",
        ],
    },
    "Publishing industries, except internet (includes software)": {
        "canonical_operating_system": "IP, Subscription, and Rights Management",
        "canonical_workflows": [
            ("Product and Content Development", "Product, Content, and Engineering"),
            ("Subscription and License Management", "Finance and Revenue Operations"),
            ("Distribution and Release Management", "Product, Content, and Engineering"),
            ("Customer Support and Success", "Customer and Experience Operations"),
            ("Billing and Renewals", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "CRM",
            "Billing and Subscription Management",
            "ERP",
            "Service Management",
        ],
    },
    "Rental and leasing services and lessors of intangible assets": {
        "canonical_operating_system": "Asset Utilization and Lease Management",
        "canonical_workflows": [
            ("Asset Acquisition and Setup", "Planning and Allocation"),
            ("Reservation and Contract Management", "Access, Intake, and Contracting"),
            ("Dispatch and Checkout", "Delivery and Service Execution"),
            ("Asset Maintenance and Turnover", "Production and Asset Operations"),
            ("Billing and Asset Recovery", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Rental Operations Management",
            "Maintenance Management",
            "ERP",
        ],
    },
    "Utilities": {
        "canonical_operating_system": "Network Infrastructure Operations",
        "canonical_workflows": [
            ("Load Forecasting and Dispatch", "Network and Transportation Operations"),
            ("Asset Maintenance and Outage Management", "Production and Asset Operations"),
            ("Meter-to-Cash", "Finance and Revenue Operations"),
            ("Capital Planning and Compliance Reporting", "Governance and Portfolio Operations"),
            ("Customer Service and Field Response", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "Utility Operations and Billing",
            "Maintenance Management",
            "Industrial Automation and SCADA",
            "ERP",
        ],
    },
    "Petroleum and coal products": {
        "canonical_operating_system": "Process Manufacturing and Throughput Control",
        "canonical_workflows": [
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning and Process Control", "Production and Asset Operations"),
            ("Maintenance and Turnaround Management", "Production and Asset Operations"),
            ("Blending, Logistics, and Distribution", "Delivery and Service Execution"),
            ("Margin, Safety, and Emissions Reporting", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Industrial Automation and SCADA",
            "Maintenance Management",
            "Supply Chain Planning",
        ],
    },
    "Farms": {
        "canonical_operating_system": "Field Production and Resource Extraction",
        "canonical_workflows": [
            ("Production Planning", "Planning and Allocation"),
            ("Input Sourcing and Procurement", "Sourcing and Supply"),
            ("Field Operations", "Production and Asset Operations"),
            ("Harvest and Logistics Management", "Delivery and Service Execution"),
            ("Marketing, Hedging, and Program Reporting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Farm Management Platform",
            "Precision Agriculture and Telematics",
        ],
    },
    "Motor vehicle and parts dealers": {
        "canonical_operating_system": "Retail and Service Commerce",
        "canonical_workflows": [
            ("Inventory Sourcing and Aging Management", "Planning and Allocation"),
            ("Lead Management and Sales", "Access, Intake, and Contracting"),
            ("Financing and Underwriting", "Finance and Revenue Operations"),
            ("Service Scheduling and Parts Management", "Customer and Experience Operations"),
            ("Customer Retention and Remarketing", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "Dealership Management System",
            "CRM",
            "Loan Origination and Servicing",
            "Maintenance Management",
        ],
    },
    "Truck transportation": {
        "canonical_operating_system": "Transportation Network Operations",
        "canonical_workflows": [
            ("Capacity and Load Planning", "Network and Transportation Operations"),
            ("Dispatch and Routing", "Network and Transportation Operations"),
            ("Driver Safety and Compliance", "Risk, Compliance, and Reporting"),
            ("In-Transit Visibility and Proof of Delivery", "Network and Transportation Operations"),
            ("Freight Audit and Billing", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Transportation Management System",
            "Fleet Telematics and Visibility",
            "ERP",
        ],
    },
    "Legal services": {
        "canonical_operating_system": "Professional Services and Matter Management",
        "canonical_workflows": [
            ("Matter Intake and Conflict Review", "Access, Intake, and Contracting"),
            ("Staffing and Task Management", "Workforce and Labor Operations"),
            ("Document and Knowledge Management", "Product, Content, and Engineering"),
            ("Time and Expense Capture", "Finance and Revenue Operations"),
            ("Docketing and Compliance Tracking", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "Document Management",
            "Practice Management and Billing",
            "CRM",
        ],
    },
    "Educational services": {
        "canonical_operating_system": "Education Delivery and Administration",
        "canonical_workflows": [
            ("Admissions and Enrollment", "Access, Intake, and Contracting"),
            ("Scheduling and Staffing", "Workforce and Labor Operations"),
            ("Instruction Delivery", "Delivery and Service Execution"),
            ("Student Service and Retention Management", "Customer and Experience Operations"),
            ("Billing, Aid, and Regulatory Reporting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Student Information System",
            "Learning Management System",
            "HCM / Workforce Management",
            "ERP",
        ],
    },
    "Fabricated metal products": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Estimating and Quotation", "Access, Intake, and Contracting"),
            ("Production Planning", "Planning and Allocation"),
            ("Shop Floor Execution and Quality Management", "Production and Asset Operations"),
            ("Quality Inspection and Certification", "Risk, Compliance, and Reporting"),
            ("Shipping and Invoice Reconciliation", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Manufacturing Execution System",
            "Shop Floor Control and Quality",
        ],
    },
    "Oil and gas extraction": {
        "canonical_operating_system": "Field Production and Resource Extraction",
        "canonical_workflows": [
            ("Asset and Reserve Evaluation", "Planning and Allocation"),
            ("Field Development Planning", "Planning and Allocation"),
            ("Production Operations", "Production and Asset Operations"),
            ("Midstream Coordination", "Network and Transportation Operations"),
            ("Revenue and Regulatory Reporting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Upstream Energy Management",
            "Production Accounting and Regulatory",
            "Geoscience and Reservoir Management",
            "ERP",
        ],
    },
    "Machinery": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Product and Engineering Configuration", "Product, Content, and Engineering"),
            ("Supplier Scheduling and Procurement", "Sourcing and Supply"),
            ("Assembly and Test", "Production and Asset Operations"),
            ("Logistics and Channel Fulfillment", "Delivery and Service Execution"),
            ("Aftermarket Service and Field Support", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "PLM and Engineering Design",
            "Manufacturing Execution System",
            "Maintenance Management",
        ],
    },
    "Other transportation equipment": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Program and Platform Planning", "Planning and Allocation"),
            ("Supplier Coordination and Compliance", "Sourcing and Supply"),
            ("Assembly, Test, and Certification", "Production and Asset Operations"),
            ("Delivery and Contract Milestone Management", "Delivery and Service Execution"),
            ("Aftermarket Service and Field Support", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "PLM and Engineering Design",
            "Project and Construction Management",
        ],
    },
    "Computer and electronic products": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Demand and Allocation Planning", "Planning and Allocation"),
            ("Engineering Change Management", "Product, Content, and Engineering"),
            ("Shop Floor Execution and Quality Management", "Production and Asset Operations"),
            ("Quality and Traceability Management", "Risk, Compliance, and Reporting"),
            ("Logistics and Channel Fulfillment", "Delivery and Service Execution"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "PLM and Engineering Design",
            "Manufacturing Execution System",
            "Supply Chain Planning",
        ],
    },
    "Accommodation": {
        "canonical_operating_system": "Venue, Hospitality, and Attendance Operations",
        "canonical_workflows": [
            ("Reservation and Distribution Management", "Access, Intake, and Contracting"),
            ("Revenue Management", "Planning and Allocation"),
            ("Front Desk and Housekeeping Operations", "Delivery and Service Execution"),
            ("Maintenance and Guest Service", "Customer and Experience Operations"),
            ("Night Audit and Owner Reporting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Property Management System",
            "Reservation and Distribution System",
            "Revenue Management Platform",
            "ERP",
        ],
    },
    "Nursing and residential care facilities": {
        "canonical_operating_system": "Care Delivery and Reimbursement",
        "canonical_workflows": [
            ("Access, Admissions, and Throughput Management", "Access, Intake, and Contracting"),
            ("Workforce Scheduling", "Workforce and Labor Operations"),
            ("Clinical Documentation", "Clinical and Case Operations"),
            ("Medication and Compliance Management", "Clinical and Case Operations"),
            ("Billing, Claims, and Collections", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "EHR and Care Management",
            "Revenue Cycle Management",
            "HCM / Workforce Management",
        ],
    },
    "Social assistance": {
        "canonical_operating_system": "Case Management and Program Administration",
        "canonical_workflows": [
            ("Intake and Eligibility Determination", "Access, Intake, and Contracting"),
            ("Case Planning", "Clinical and Case Operations"),
            ("Service Delivery and Referral Coordination", "Clinical and Case Operations"),
            ("Documentation and Compliance Management", "Risk, Compliance, and Reporting"),
            ("Billing, Grant Reporting, and Reimbursement", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Case Management System",
            "CRM",
            "Grant and Program Reporting",
            "Referral Management",
        ],
    },
    "Other transportation and support activities": {
        "canonical_operating_system": "Transportation Network Operations",
        "canonical_workflows": [
            ("Load Intake and Booking", "Access, Intake, and Contracting"),
            ("Carrier Coordination and Brokerage", "Network and Transportation Operations"),
            ("Terminal and Yard Operations", "Network and Transportation Operations"),
            ("Exception Management", "Network and Transportation Operations"),
            ("Freight Audit and Settlement", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Transportation Management System",
            "Fleet Telematics and Visibility",
            "ERP",
        ],
    },
    "Food and beverage stores": {
        "canonical_operating_system": "Retail and Service Commerce",
        "canonical_workflows": [
            ("Merchandising and Assortment Planning", "Planning and Allocation"),
            ("Inventory and Perishables Management", "Production and Asset Operations"),
            ("Point-of-Sale and Loyalty Operations", "Customer and Experience Operations"),
            ("Workforce Scheduling", "Workforce and Labor Operations"),
            ("Margin and Shrink Management", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "POS and Payments",
            "ERP",
            "Supply Chain Planning",
            "Warehouse Management System",
        ],
    },
    "Performing arts, spectator sports, museums, and related activities": {
        "canonical_operating_system": "Venue, Hospitality, and Attendance Operations",
        "canonical_workflows": [
            ("Programming and Event Planning", "Planning and Allocation"),
            ("Ticketing and Pricing", "Access, Intake, and Contracting"),
            ("Venue and Staff Operations", "Delivery and Service Execution"),
            ("Sponsorship and Donor Management", "Access, Intake, and Contracting"),
            ("Event Settlement and Reporting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Ticketing and Venue Management",
            "CRM",
            "Event and Donor Management",
        ],
    },
    "Air transportation": {
        "canonical_operating_system": "Transportation Network Operations",
        "canonical_workflows": [
            ("Network and Schedule Planning", "Network and Transportation Operations"),
            ("Crew and Fleet Assignment", "Network and Transportation Operations"),
            ("Revenue Management", "Planning and Allocation"),
            ("Operational Recovery and Disruption Management", "Network and Transportation Operations"),
            ("Loyalty and Settlement Accounting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Airline Operations and Reservations",
            "Revenue Management Platform",
            "ERP",
        ],
    },
    "General merchandise stores": {
        "canonical_operating_system": "Retail and Service Commerce",
        "canonical_workflows": [
            ("Merchandising and Assortment Planning", "Planning and Allocation"),
            ("Inventory Allocation and Replenishment", "Planning and Allocation"),
            ("Order Orchestration and Fulfillment", "Delivery and Service Execution"),
            ("Store Labor Execution", "Workforce and Labor Operations"),
            ("Returns and Markdown Management", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "Commerce Platform",
            "ERP",
            "Order Management System",
            "Warehouse Management System",
            "Supply Chain Planning",
        ],
    },
    "Primary metals": {
        "canonical_operating_system": "Process Manufacturing and Throughput Control",
        "canonical_workflows": [
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning and Process Control", "Production and Asset Operations"),
            ("Asset Maintenance and Uptime Management", "Production and Asset Operations"),
            ("Quality Inspection and Certification", "Risk, Compliance, and Reporting"),
            ("Order Management and Fulfillment", "Delivery and Service Execution"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Industrial Automation and SCADA",
            "Maintenance Management",
            "Shop Floor Control and Quality",
        ],
    },
    "Plastics and rubber products": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning", "Planning and Allocation"),
            ("Tooling and Machine Execution", "Production and Asset Operations"),
            ("Quality and Compliance Management", "Risk, Compliance, and Reporting"),
            ("Logistics and Channel Fulfillment", "Delivery and Service Execution"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Manufacturing Execution System",
            "PLM and Engineering Design",
            "Shop Floor Control and Quality",
        ],
    },
    "Funds, trusts, and other financial vehicles": {
        "canonical_operating_system": "Capital Markets and Investment Management",
        "canonical_workflows": [
            ("Fund Onboarding and Setup", "Access, Intake, and Contracting"),
            ("Fund Accounting", "Governance and Portfolio Operations"),
            ("Valuation, NAV, and Reconciliation", "Governance and Portfolio Operations"),
            ("Investor Reporting", "Governance and Portfolio Operations"),
            ("Compliance and Service-Provider Oversight", "Risk, Compliance, and Reporting"),
        ],
        "systems_of_record_categories": [
            "Fund Administration and Accounting",
            "Portfolio and Order Management",
            "Reconciliation and Reporting",
            "Investor Reporting and Performance",
        ],
    },
    "Amusements, gambling, and recreation industries": {
        "canonical_operating_system": "Venue, Hospitality, and Attendance Operations",
        "canonical_workflows": [
            ("Capacity and Event Planning", "Planning and Allocation"),
            ("Ticketing, POS, and Cage Operations", "Customer and Experience Operations"),
            ("Workforce Scheduling", "Workforce and Labor Operations"),
            ("Safety and Compliance Management", "Risk, Compliance, and Reporting"),
            ("Loyalty and Settlement Management", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Ticketing and Venue Management",
            "POS and Payments",
            "CRM",
            "Revenue Management Platform",
        ],
    },
    "Paper products": {
        "canonical_operating_system": "Process Manufacturing and Throughput Control",
        "canonical_workflows": [
            ("Material Sourcing", "Sourcing and Supply"),
            ("Production Planning and Process Control", "Production and Asset Operations"),
            ("Asset Maintenance and Uptime Management", "Production and Asset Operations"),
            ("Quality and Converting Management", "Production and Asset Operations"),
            ("Logistics and Channel Fulfillment", "Delivery and Service Execution"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "Industrial Automation and SCADA",
            "Maintenance Management",
            "Supply Chain Planning",
        ],
    },
    "Motion picture and sound recording industries": {
        "canonical_operating_system": "IP, Subscription, and Rights Management",
        "canonical_workflows": [
            ("Development and Greenlight Management", "Product, Content, and Engineering"),
            ("Production Scheduling", "Planning and Allocation"),
            ("Rights and Contract Management", "Product, Content, and Engineering"),
            ("Distribution and Release Management", "Product, Content, and Engineering"),
            ("Royalty and Participation Accounting", "Finance and Revenue Operations"),
        ],
        "systems_of_record_categories": [
            "Rights and Royalty Management",
            "Production Management",
            "CRM",
            "ERP",
        ],
    },
    "Electrical equipment, appliances, and components": {
        "canonical_operating_system": "Product Manufacturing and Lifecycle Operations",
        "canonical_workflows": [
            ("Product Lifecycle and Engineering Management", "Product, Content, and Engineering"),
            ("Supplier Scheduling and Procurement", "Sourcing and Supply"),
            ("Assembly and Test", "Production and Asset Operations"),
            ("Compliance and Certification Management", "Risk, Compliance, and Reporting"),
            ("Channel and Service Support", "Customer and Experience Operations"),
        ],
        "systems_of_record_categories": [
            "ERP",
            "PLM and Engineering Design",
            "Manufacturing Execution System",
            "Shop Floor Control and Quality",
        ],
    },
}


def build_normalized_rows(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, object]]:
    normalized_rows: list[dict[str, str]] = []
    workflow_examples: dict[str, set[str]] = defaultdict(set)
    workflow_industries: dict[str, set[str]] = defaultdict(set)
    workflow_families: dict[str, str] = {}
    family_assignments: Counter[str] = Counter()
    family_workflows: dict[str, set[str]] = defaultdict(set)
    category_industries: dict[str, set[str]] = defaultdict(set)
    operating_system_industries: dict[str, set[str]] = defaultdict(set)
    missing_by_industry: dict[str, list[str]] = {}

    source_industries = {row["industry_name"] for row in rows}
    mapping_industries = set(INDUSTRY_NORMALIZATION)
    if source_industries != mapping_industries:
        missing_mappings = sorted(source_industries - mapping_industries)
        extra_mappings = sorted(mapping_industries - source_industries)
        raise ValueError(
            f"Industry normalization mismatch. Missing={missing_mappings} extra={extra_mappings}"
        )

    for row in rows:
        industry = row["industry_name"]
        normalization = INDUSTRY_NORMALIZATION[industry]
        operating_system = normalization["canonical_operating_system"]
        workflows = normalization["canonical_workflows"]
        categories = normalization["systems_of_record_categories"]
        original_workflows = [value.strip() for value in row["core_workflows_observation"].split("|")]

        if operating_system not in OPERATING_SYSTEM_DEFINITIONS:
            raise ValueError(f"Unknown operating system for {industry}: {operating_system}")
        if len(workflows) != 5:
            raise ValueError(f"{industry} must have exactly 5 canonical workflows")
        if len(original_workflows) != 5:
            raise ValueError(f"{industry} source row does not contain exactly 5 workflows")

        missing_fields: list[str] = []
        if not row["gross_output_2025_usd_mn"] or not row["economic_size_summary"]:
            missing_fields.append("market_size")
        if not operating_system:
            missing_fields.append("canonical_operating_system")
        if not workflows or any(not name for name, _family in workflows):
            missing_fields.append("canonical_workflows")
        if not categories or any(not category for category in categories):
            missing_fields.append("systems_of_record_categories")

        for category in categories:
            if category not in SYSTEM_CATEGORY_DEFINITIONS:
                raise ValueError(f"Unknown system category for {industry}: {category}")
            category_industries[category].add(industry)

        operating_system_industries[operating_system].add(industry)
        missing_by_industry[industry] = missing_fields

        normalized_row = {
            "rank_2025_gross_output": row["rank_2025_gross_output"],
            "industry_name": industry,
            "bea_table_line": row["bea_table_line"],
            "gross_output_2025_usd_mn": row["gross_output_2025_usd_mn"],
            "value_added_2025_usd_mn": row["value_added_2025_usd_mn"],
            "q1_2026_real_go_change_pct_saar": row["q1_2026_real_go_change_pct_saar"],
            "economic_size_summary": row["economic_size_summary"],
            "canonical_operating_system": operating_system,
        }

        canonical_workflows: list[str] = []
        canonical_families: list[str] = []
        for index, ((workflow_name, family), source_phrase) in enumerate(
            zip(workflows, original_workflows),
            start=1,
        ):
            if family not in WORKFLOW_FAMILY_DEFINITIONS:
                raise ValueError(f"Unknown workflow family for {industry}: {family}")
            normalized_row[f"canonical_workflow_family_{index}"] = family
            normalized_row[f"canonical_workflow_{index}"] = workflow_name
            canonical_workflows.append(workflow_name)
            canonical_families.append(family)
            workflow_examples[workflow_name].add(source_phrase)
            workflow_industries[workflow_name].add(industry)
            workflow_families[workflow_name] = family
            family_assignments[family] += 1
            family_workflows[family].add(workflow_name)

        normalized_row["canonical_workflows"] = " | ".join(canonical_workflows)
        normalized_row["canonical_workflow_families"] = " | ".join(canonical_families)
        normalized_row["systems_of_record_categories"] = " | ".join(categories)
        normalized_row["phase_1b_validation_status"] = "Complete" if not missing_fields else "Missing Fields"
        normalized_row["phase_1b_missing_fields"] = ", ".join(missing_fields)
        normalized_row["operating_model_observation"] = row["operating_model_observation"]
        normalized_row["core_workflows_observation"] = row["core_workflows_observation"]
        normalized_row["systems_of_record_map"] = row["systems_of_record_map"]
        normalized_row["technology_maturity_assessment"] = row["technology_maturity_assessment"]
        normalized_row["structural_pressures_observation"] = row["structural_pressures_observation"]
        normalized_row["inefficiency_signals_observation"] = row["inefficiency_signals_observation"]
        normalized_row["evidence_quality_confidence"] = row["evidence_quality_confidence"]
        normalized_row["source_links"] = row["source_links"]
        normalized_row["hypothesis_notes"] = row["hypothesis_notes"]
        normalized_rows.append(normalized_row)

    metadata = {
        "workflow_examples": workflow_examples,
        "workflow_industries": workflow_industries,
        "workflow_families": workflow_families,
        "family_assignments": family_assignments,
        "family_workflows": family_workflows,
        "category_industries": category_industries,
        "operating_system_industries": operating_system_industries,
        "missing_by_industry": missing_by_industry,
    }
    return normalized_rows, metadata


def write_normalized_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "rank_2025_gross_output",
        "industry_name",
        "bea_table_line",
        "gross_output_2025_usd_mn",
        "value_added_2025_usd_mn",
        "q1_2026_real_go_change_pct_saar",
        "economic_size_summary",
        "canonical_operating_system",
        "canonical_workflow_family_1",
        "canonical_workflow_1",
        "canonical_workflow_family_2",
        "canonical_workflow_2",
        "canonical_workflow_family_3",
        "canonical_workflow_3",
        "canonical_workflow_family_4",
        "canonical_workflow_4",
        "canonical_workflow_family_5",
        "canonical_workflow_5",
        "canonical_workflows",
        "canonical_workflow_families",
        "systems_of_record_categories",
        "phase_1b_validation_status",
        "phase_1b_missing_fields",
        "operating_model_observation",
        "core_workflows_observation",
        "systems_of_record_map",
        "technology_maturity_assessment",
        "structural_pressures_observation",
        "inefficiency_signals_observation",
        "evidence_quality_confidence",
        "source_links",
        "hypothesis_notes",
    ]
    with NORMALIZED_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_operating_system_doc(
    rows: list[dict[str, str]],
    operating_system_industries: dict[str, set[str]],
) -> None:
    by_rank = sorted(rows, key=lambda row: int(row["rank_2025_gross_output"]))
    ranked_operating_systems = sorted(
        operating_system_industries.items(),
        key=lambda item: (-len(item[1]), item[0]),
    )

    lines = [
        "# Operating-System Taxonomy",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 1B taxonomy",
        "",
        "## Design Rules",
        "",
        "- Derived only from the existing Top 50 Industry Census.",
        "- One canonical operating system per industry.",
        "- Names describe reusable economic operating logic rather than raw industry labels.",
        "- Original operating-model observations remain preserved in both the raw and normalized CSVs.",
        "",
        "## Canonical Taxonomy",
        "",
        "| Canonical Operating System | Definition | Industry Count | Industries |",
        "| --- | --- | ---: | --- |",
    ]

    for operating_system, industries in ranked_operating_systems:
        industry_list = ", ".join(sorted(industries))
        definition = OPERATING_SYSTEM_DEFINITIONS[operating_system]
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(operating_system),
                    escape_md(definition),
                    str(len(industries)),
                    escape_md(industry_list),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Industry Map",
            "",
            "| Rank | Industry | Canonical Operating System |",
            "| ---: | --- | --- |",
        ]
    )
    for row in by_rank:
        lines.append(
            f"| {row['rank_2025_gross_output']} | {escape_md(row['industry_name'])} | "
            f"{escape_md(row['canonical_operating_system'])} |"
        )

    OPERATING_SYSTEM_DOC.write_text("\n".join(lines) + "\n")


def write_workflow_doc(
    workflow_examples: dict[str, set[str]],
    workflow_industries: dict[str, set[str]],
    workflow_families: dict[str, str],
    family_assignments: Counter[str],
    family_workflows: dict[str, set[str]],
) -> None:
    lines = [
        "# Workflow Taxonomy",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 1B taxonomy",
        "",
        "## Design Rules",
        "",
        "- Derived only from the 250 workflow slots already present in the existing census.",
        "- Each industry retains exactly five canonical workflows.",
        "- Workflow families improve comparison across industries without introducing Phase 2 analysis.",
        "- Original source phrases remain preserved in the raw and normalized CSVs.",
        "",
        "## Workflow Families",
        "",
        "| Family | Definition | Canonical Workflow Count | Industry Slots |",
        "| --- | --- | ---: | ---: |",
    ]

    family_items = sorted(
        family_workflows.items(),
        key=lambda item: (-family_assignments[item[0]], item[0]),
    )
    for family, workflows in family_items:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(family),
                    escape_md(WORKFLOW_FAMILY_DEFINITIONS[family]),
                    str(len(workflows)),
                    str(family_assignments[family]),
                ]
            )
            + " |"
        )

    for family, workflows in family_items:
        lines.extend(
            [
                "",
                f"## {family}",
                "",
                "| Canonical Workflow | Industry Count | Example Source Phrases |",
                "| --- | ---: | --- |",
            ]
        )
        ordered_workflows = sorted(
            workflows,
            key=lambda workflow_name: (-len(workflow_industries[workflow_name]), workflow_name),
        )
        for workflow_name in ordered_workflows:
            examples = "; ".join(sorted(workflow_examples[workflow_name])[:3])
            lines.append(
                "| "
                + " | ".join(
                    [
                        escape_md(workflow_name),
                        str(len(workflow_industries[workflow_name])),
                        escape_md(examples),
                    ]
                )
                + " |"
            )

    WORKFLOW_DOC.write_text("\n".join(lines) + "\n")


def write_system_doc(category_industries: dict[str, set[str]]) -> None:
    ranked_categories = sorted(
        category_industries.items(),
        key=lambda item: (-len(item[1]), item[0]),
    )
    lines = [
        "# Systems-of-Record Taxonomy",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 1B taxonomy",
        "",
        "## Design Rules",
        "",
        "- Categories normalize representative vendor stacks into comparable system types.",
        "- Categories are inferred only from the existing census vendor fields and workflow context.",
        "- Category labels are not market-share claims and do not add new research.",
        "- Original vendor strings remain preserved in both the raw and normalized CSVs.",
        "",
        "## Canonical Categories",
        "",
        "| Category | Definition | Example Vendors | Industry Count |",
        "| --- | --- | --- | ---: |",
    ]

    for category, industries in ranked_categories:
        vendor_examples = ", ".join(SYSTEM_CATEGORY_EXAMPLES.get(category, [])[:4])
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(category),
                    escape_md(SYSTEM_CATEGORY_DEFINITIONS[category]),
                    escape_md(vendor_examples),
                    str(len(industries)),
                ]
            )
            + " |"
        )

    SYSTEM_DOC.write_text("\n".join(lines) + "\n")


def write_summary(
    rows: list[dict[str, str]],
    operating_system_industries: dict[str, set[str]],
    workflow_industries: dict[str, set[str]],
    family_workflows: dict[str, set[str]],
    category_industries: dict[str, set[str]],
    missing_by_industry: dict[str, list[str]],
) -> None:
    complete_count = sum(1 for row in rows if row["phase_1b_validation_status"] == "Complete")
    top_operating_systems = sorted(
        operating_system_industries.items(),
        key=lambda item: (-len(item[1]), item[0]),
    )[:5]
    top_families = sorted(
        family_workflows.items(),
        key=lambda item: (-sum(1 for workflow in item[1] for _ in workflow_industries[workflow]), item[0]),
    )[:5]

    lines = [
        "# Phase 1B Normalization Summary",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Completed",
        "",
        "## Scope",
        "",
        "- Source input: `knowledge/research/industry-census/top-50-industry-census.csv` only.",
        "- No new industry research was added.",
        "- No Phase 2 workflow mapping was started.",
        "- No opportunity, gap, or startup analysis was introduced.",
        "",
        "## Deliverables Created",
        "",
        "- `knowledge/research/industry-census/top-50-industry-census-normalized.csv`",
        "- `knowledge/research/industry-census/operating-system-taxonomy.md`",
        "- `knowledge/research/industry-census/workflow-taxonomy.md`",
        "- `knowledge/research/industry-census/systems-of-record-taxonomy.md`",
        "- `knowledge/research/industry-census/phase-1b-normalization-summary.md`",
        "",
        "## Normalization Counts",
        "",
        f"- Industries normalized: {len(rows)}",
        f"- Canonical operating systems: {len(operating_system_industries)}",
        f"- Workflow-family vocabulary: {len(family_workflows)} reusable families across all {len(rows) * 5} workflow slots",
        f"- Systems-of-record category layer: generated for all {len(rows)} industries",
        "",
        "## Validation",
        "",
        f"- Complete rows: {complete_count} of {len(rows)}",
        f"- Rows with missing fields: {len(rows) - complete_count}",
    ]

    missing_items = [
        (industry, fields)
        for industry, fields in sorted(missing_by_industry.items())
        if fields
    ]
    if missing_items:
        lines.extend(["", "### Missing Fields", ""])
        for industry, fields in missing_items:
            lines.append(f"- {industry}: {', '.join(fields)}")
    else:
        lines.extend(["", "- Missing-field flags: none", ""])

    lines.extend(
        [
            "## Largest Operating-System Buckets",
            "",
        ]
    )
    for operating_system, industries in top_operating_systems:
        lines.append(f"- {operating_system}: {len(industries)} industries")

    lines.extend(["", "## Largest Workflow Families", ""])
    for family, workflows in top_families:
        slot_count = sum(
            1
            for workflow_name in workflows
            for _industry in workflow_industries[workflow_name]
        )
        lines.append(f"- {family}: {slot_count} industry workflow slots across {len(workflows)} canonical workflows")

    lines.extend(
        [
            "",
            "## Active Census Layer",
            "",
            "- Raw research snapshot remains preserved in `top-50-industry-census.csv`.",
            "- The active normalized Phase 1 layer is `top-50-industry-census-normalized.csv`.",
            "- Phase 2 should start from the normalized operating-system, workflow, and systems vocabulary rather than the raw labels.",
        ]
    )

    SUMMARY_DOC.write_text("\n".join(lines) + "\n")


def main() -> None:
    with SOURCE_CSV.open() as handle:
        rows = list(csv.DictReader(handle))

    normalized_rows, metadata = build_normalized_rows(rows)
    write_normalized_csv(normalized_rows)
    write_operating_system_doc(normalized_rows, metadata["operating_system_industries"])
    write_workflow_doc(
        metadata["workflow_examples"],
        metadata["workflow_industries"],
        metadata["workflow_families"],
        metadata["family_assignments"],
        metadata["family_workflows"],
    )
    write_system_doc(metadata["category_industries"])
    write_summary(
        normalized_rows,
        metadata["operating_system_industries"],
        metadata["workflow_industries"],
        metadata["family_workflows"],
        metadata["category_industries"],
        metadata["missing_by_industry"],
    )
    print("Wrote normalized census artifacts:")
    print(f"- {NORMALIZED_CSV}")
    print(f"- {OPERATING_SYSTEM_DOC}")
    print(f"- {WORKFLOW_DOC}")
    print(f"- {SYSTEM_DOC}")
    print(f"- {SUMMARY_DOC}")


if __name__ == "__main__":
    main()
