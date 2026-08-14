# Structural Failure Atlas (v1)

Last updated: 2026-08-14
Status: Active Phase 3 analytical layer

## Corpus Summary

- Evidence base: 198 canonical workflows and 250 workflow ↔ operating-system ↔ industry usage rows.
- Scope boundary: Phase 3 synthesis only. No startup ideas, solution recommendations, or Phase 4 opportunity classification are included here.
- Recurrence is measured at two levels: workflow incidence and expanded workflow-usage links from the Phase 1 index.

## Failure Register

| Code | Failure | Workflows | Usage links | Operating systems | Industries | Dominant root cause | Confidence |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| SF-03 | Decision Context Escapes the Record | 174 | 219 | 21 | 50 | Legacy Architecture | High |
| SF-04 | Human Judgment Under Incomplete Information | 116 | 149 | 21 | 50 | Technical | High |
| SF-01 | Exception-Path Breakdown | 77 | 99 | 20 | 48 | Legacy Architecture | Medium-High |
| SF-06 | Plan vs. Reality Divergence | 53 | 76 | 13 | 35 | Legacy Architecture | Medium-High |
| SF-02 | Cross-System Reconciliation | 42 | 47 | 17 | 35 | Legacy Architecture | Medium-High |
| SF-05 | Handoff and Approval Latency | 40 | 46 | 18 | 32 | Organizational | Medium-High |
| SF-07 | Compliance and Evidence Burden | 29 | 34 | 14 | 23 | Regulatory | Medium |
| SF-08 | Multi-Party Trust and Dependency Gaps | 28 | 39 | 12 | 27 | Technical | Medium |

## SF-03 Decision Context Escapes the Record

- Description: The decisive context for advancing work lives outside the formal system of record in email, calls, spreadsheets, decks, notes, or portals.
- Frequency: 174 of 198 workflows (87.9%); 219 failure-to-workflow-usage links across 21 operating systems and 50 industries.
- Root-cause mix: Legacy Architecture (74); Regulatory (38); Technical (27); Organizational (16); Behavioral (15); Economic (4)
- Operating systems affected: Product Manufacturing and Lifecycle Operations (30), Process Manufacturing and Throughput Control (23), Retail and Service Commerce (17), Professional Services and Matter Management (15), Transportation Network Operations (15), Care Delivery and Reimbursement (14), Asset Utilization and Lease Management (14), Workforce Coordination and Service Operations (10)
- Industries affected: Hospitals (5), Ambulatory health care services (5), Federal Reserve banks, credit intermediation, and related activities (5), Educational services (5), Machinery (5), Electrical equipment, appliances, and components (5), Utilities (5), Paper products (5)
- Typical systems of record involved: ERP (104); CRM (72); HCM / Workforce Management (35); Maintenance Management (33); Service Management (28); Supply Chain Planning (24)
- Common human judgment points: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item. (12); Materiality, root cause, and acceptable resolution still depend on experienced finance staff. (11); Inspectors still interpret severity, traceability gaps, and acceptable release decisions. (10)
- Common system-of-record escape points: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system. (12); Exception triage almost always moves into spreadsheets, email, and bank or partner portals. (11); Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record. (10)
- Common economic leakage: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points. (12); Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag. (11); Failures, recalls, rework, and excess inspection labor are the major leakage points. (10)
- Structural reason incumbents have not solved it: Systems of record optimize for structured state capture, while collaboration tools hold the narrative, negotiation, and exception context that operators actually need. Repeated Phase 2 evidence most often states: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. (12); Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. (11); Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. (10).
- Dominant root cause: Legacy Architecture
- Confidence: High
- Evidence references:
  - [Collections and Loss Mitigation](../workflow-library/workflows/collections-and-loss-mitigation.md): Core context moves into credit memos, committee notes, shared spreadsheets, and email threads outside the core record.
  - [Account and Loan Onboarding](../workflow-library/workflows/account-and-loan-onboarding.md): Onboarding packets, emails, shared checklists, and external verification portals carry the real process state.
  - [Customer Retention and Remarketing](../workflow-library/workflows/customer-retention-and-remarketing.md): The decisive conversations happen in calls, emails, and side planning decks outside the system of record.
  - [Delivery and Contract Milestone Management](../workflow-library/workflows/delivery-and-contract-milestone-management.md): The real state of the project lives in meetings, comments, decks, and side trackers beyond the PSA or project tool.
  - [Clinical Documentation](../workflow-library/workflows/clinical-documentation.md): Critical case context moves through phone calls, referrals, messages, and external portals.
  - [Supplier Scheduling and Procurement](../workflow-library/workflows/supplier-scheduling-and-procurement.md): Actual supplier coordination lives in calls, emails, and shared trackers beyond the formal procurement record.

## SF-04 Human Judgment Under Incomplete Information

- Description: Progress depends on experienced people interpreting incomplete, noisy, or conflicting signals and choosing tradeoffs.
- Frequency: 116 of 198 workflows (58.6%); 149 failure-to-workflow-usage links across 21 operating systems and 50 industries.
- Root-cause mix: Technical (34); Legacy Architecture (31); Regulatory (27); Behavioral (13); Organizational (11)
- Operating systems affected: Product Manufacturing and Lifecycle Operations (25), Retail and Service Commerce (18), Process Manufacturing and Throughput Control (15), Venue, Hospitality, and Attendance Operations (10), Care Delivery and Reimbursement (9), Asset Utilization and Lease Management (8), Capital Markets and Investment Management (7), Professional Services and Matter Management (7)
- Industries affected: Management of companies and enterprises (5), Federal Reserve banks, credit intermediation, and related activities (4), Other transportation equipment (4), Electrical equipment, appliances, and components (4), Nursing and residential care facilities (4), Amusements, gambling, and recreation industries (4), Insurance carriers and related activities (4), Motor vehicle and parts dealers (4)
- Typical systems of record involved: ERP (73); CRM (47); Supply Chain Planning (22); Manufacturing Execution System (21); Maintenance Management (21); HCM / Workforce Management (20)
- Common human judgment points: Planners still decide which signals to trust and when the model output does not fit local reality. (13); Inspectors still interpret severity, traceability gaps, and acceptable release decisions. (10); Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run. (9)
- Common system-of-record escape points: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations. (13); Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record. (10); Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields. (9)
- Common economic leakage: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting. (13); Failures, recalls, rework, and excess inspection labor are the major leakage points. (10); Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages. (9)
- Structural reason incumbents have not solved it: The important variables are contextual, dynamic, or politically negotiated, so rules engines and dashboards cannot safely absorb the full decision load. Repeated Phase 2 evidence most often states: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. (13); Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. (10); Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. (9).
- Dominant root cause: Technical
- Confidence: High
- Evidence references:
  - [Production Planning](../workflow-library/workflows/production-planning.md): Planners still decide which signals to trust and when the model output does not fit local reality.
  - [Account and Loan Onboarding](../workflow-library/workflows/account-and-loan-onboarding.md): Analysts still judge risk, beneficial ownership complexity, and what counts as a satisfactory exception path.
  - [Policy Administration](../workflow-library/workflows/policy-administration.md): Risk appetite and exposure interpretation remain highly judgment-driven even with scoring support.
  - [Aftermarket Service and Field Support](../workflow-library/workflows/aftermarket-service-and-field-support.md): Good service recovery depends on empathy, prioritization, and contextual interpretation.
  - [Asset Maintenance and Uptime Management](../workflow-library/workflows/asset-maintenance-and-uptime-management.md): Maintenance leaders still assess condition, risk, and repair tradeoffs beyond simple rules.
  - [Medication and Compliance Management](../workflow-library/workflows/medication-and-compliance-management.md): Medication decisions still depend on severity, tolerance, behavior, and contextual risk.

## SF-01 Exception-Path Breakdown

- Description: The core system handles the standard path, but economics and control break down when real-world exceptions enter the flow.
- Frequency: 77 of 198 workflows (38.9%); 99 failure-to-workflow-usage links across 20 operating systems and 48 industries.
- Root-cause mix: Legacy Architecture (41); Organizational (12); Regulatory (9); Technical (8); Economic (4); Behavioral (3)
- Operating systems affected: Retail and Service Commerce (13), Product Manufacturing and Lifecycle Operations (10), Process Manufacturing and Throughput Control (10), Venue, Hospitality, and Attendance Operations (10), Care Delivery and Reimbursement (7), Transportation Network Operations (7), Asset Utilization and Lease Management (6), Workforce Coordination and Service Operations (6)
- Industries affected: Food services and drinking places (5), Accommodation (4), Ambulatory health care services (3), Wholesale trade (3), Other services, except government (3), Publishing industries, except internet (includes software) (3), Administrative and support services (3), Chemical products (3)
- Typical systems of record involved: ERP (43); CRM (32); HCM / Workforce Management (15); Maintenance Management (13); Supply Chain Planning (12); POS and Payments (12)
- Common human judgment points: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item. (12); Materiality, root cause, and acceptable resolution still depend on experienced finance staff. (11); Operators still decide how to recover shortages, prioritize customers, and manage substitutions. (7)
- Common system-of-record escape points: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system. (12); Exception triage almost always moves into spreadsheets, email, and bank or partner portals. (11); Exception handling often happens through email, calls, and local trackers outside the formal order flow. (7)
- Common economic leakage: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points. (12); Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag. (11); Leakage shows up in split orders, mispicks, returns, expedites, and fulfillment promises that outrun actual capacity. (7)
- Structural reason incumbents have not solved it: Incumbents automate the happy path, but they rarely unify upstream data quality, policy nuance, and local exception handling well enough to remove manual orchestration. Repeated Phase 2 evidence most often states: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. (12); Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. (11); Order orchestration spans inventory, warehouse, transport, and customer systems with different clocks and constraints. (7).
- Dominant root cause: Legacy Architecture
- Confidence: Medium-High
- Evidence references:
  - [Billing and Renewals](../workflow-library/workflows/billing-and-renewals.md): Recurring billing is structurally automatable, but entitlement logic and exception-heavy account transitions remain messy. It typically spans 1 operating-sys...
  - [Order Capture and Payment Processing](../workflow-library/workflows/order-capture-and-payment-processing.md): Core POS is mature, but live edge cases and the downstream reconciliation burden remain stubbornly human. It typically spans 1 operating-system context and 4...
  - [Logistics and Channel Fulfillment](../workflow-library/workflows/logistics-and-channel-fulfillment.md): Order orchestration spans inventory, warehouse, transport, and customer systems with different clocks and constraints. It typically spans 2 operating-system...
  - [Access, Admissions, and Throughput Management](../workflow-library/workflows/access-admissions-and-throughput-management.md): Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration. It typically spans 1 operating-system...
  - [Exception Management](../workflow-library/workflows/exception-management.md): Visibility tools have improved, but cross-party event quality and actionability remain inconsistent. It typically spans 1 operating-system context and 3 syst...
  - [Material Sourcing](../workflow-library/workflows/material-sourcing.md): Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. It typically spans 2 operating-s...

## SF-06 Plan vs. Reality Divergence

- Description: A published plan or baseline becomes stale quickly as demand, capacity, field conditions, or network state change.
- Frequency: 53 of 198 workflows (26.8%); 76 failure-to-workflow-usage links across 13 operating systems and 35 industries.
- Root-cause mix: Legacy Architecture (28); Technical (25)
- Operating systems affected: Product Manufacturing and Lifecycle Operations (16), Process Manufacturing and Throughput Control (14), Retail and Service Commerce (10), Asset Utilization and Lease Management (8), Field Production and Resource Extraction (7), Transportation Network Operations (7), Network Infrastructure Operations (4), Venue, Hospitality, and Attendance Operations (3)
- Industries affected: Paper products (4), Oil and gas extraction (4), Rental and leasing services and lessors of intangible assets (3), Primary metals (3), Housing (3), Petroleum and coal products (3), Air transportation (3), Computer and electronic products (3)
- Typical systems of record involved: ERP (39); Maintenance Management (17); Supply Chain Planning (15); CRM (12); Manufacturing Execution System (10); Industrial Automation and SCADA (10)
- Common human judgment points: Planners still decide which signals to trust and when the model output does not fit local reality. (13); Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run. (9); Controllers interpret service priorities and real-world constraints faster than static optimization models. (8)
- Common system-of-record escape points: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations. (13); Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields. (9); Carrier calls, texts, and manual route notes remain central to live execution. (8)
- Common economic leakage: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting. (13); Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages. (9); The biggest leaks are empty capacity, bad routing, detention, and poor network utilization. (8)
- Structural reason incumbents have not solved it: Optimization engines depend on stable inputs and trusted constraints, but the operating environment changes faster than shared models can stay accurate. Repeated Phase 2 evidence most often states: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. (13); Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. (9); Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. (8).
- Dominant root cause: Legacy Architecture
- Confidence: Medium-High
- Evidence references:
  - [Capacity and Load Planning](../workflow-library/workflows/capacity-and-load-planning.md): Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. It typically spans 1 operating-system context and...
  - [Production Planning and Process Control](../workflow-library/workflows/production-planning-and-process-control.md): Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. It typically spans 1 operating-system context and 6...
  - [Production Planning](../workflow-library/workflows/production-planning.md): The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. It typically spans 2 operating-system contexts...
  - [Lease Acquisition and Pipeline Management](../workflow-library/workflows/lease-acquisition-and-pipeline-management.md): The workflow spans commercial negotiation, physical readiness, and revenue optimization rather than a single clean transaction. It typically spans 1 operatin...
  - [Content and Service Operations](../workflow-library/workflows/content-and-service-operations.md): The workflow changes minute to minute based on field conditions, dependencies, and incomplete telemetry across teams and vendors. It typically spans 1 operat...
  - [Carrier Coordination and Brokerage](../workflow-library/workflows/carrier-coordination-and-brokerage.md): Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. It typically spans 1 operating-system context and...

## SF-02 Cross-System Reconciliation

- Description: Teams must reconstruct truth by matching records, statuses, balances, or evidence across multiple systems, ledgers, and counterparties.
- Frequency: 42 of 198 workflows (21.2%); 47 failure-to-workflow-usage links across 17 operating systems and 35 industries.
- Root-cause mix: Legacy Architecture (32); Technical (6); Regulatory (4)
- Operating systems affected: IP, Subscription, and Rights Management (7), Capital Markets and Investment Management (6), Asset Utilization and Lease Management (4), Professional Services and Matter Management (4), Product Manufacturing and Lifecycle Operations (4), Venue, Hospitality, and Attendance Operations (3), Transportation Network Operations (3), Network Infrastructure Operations (2)
- Industries affected: Publishing industries, except internet (includes software) (4), Motion picture and sound recording industries (3), Funds, trusts, and other financial vehicles (3), Securities, commodity contracts, and investments (3), Other real estate (2), Miscellaneous professional, scientific, and technical services (2), Data processing, internet publishing, and other information services (2), Rental and leasing services and lessors of intangible assets (1)
- Typical systems of record involved: ERP (25); CRM (20); Service Management (9); Billing and Subscription Management (7); HCM / Workforce Management (7); Investor Reporting and Performance (6)
- Common human judgment points: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item. (12); Materiality, root cause, and acceptable resolution still depend on experienced finance staff. (11); Tradeoffs among quality, timing, and downstream disruption remain human-led. (7)
- Common system-of-record escape points: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system. (12); Exception triage almost always moves into spreadsheets, email, and bank or partner portals. (11); Critical rationale and version decisions live in reviews, comments, and docs outside the system of record. (7)
- Common economic leakage: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points. (12); Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag. (11); Master-data mistakes and release delays create rework, scrap, missed launch windows, and downstream confusion. (7)
- Structural reason incumbents have not solved it: Authoritative records are distributed across asynchronous systems with inconsistent identifiers, timing, and standards, so reconciliation remains a manual control layer. Repeated Phase 2 evidence most often states: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. (12); Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. (11); Structured data and collaborative work still sit in separate tools, so version truth remains hard to unify. (7).
- Dominant root cause: Legacy Architecture
- Confidence: Medium-High
- Evidence references:
  - [Billing and Reconciliation](../workflow-library/workflows/billing-and-reconciliation.md): Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
  - [Asset and Investor Reporting](../workflow-library/workflows/asset-and-investor-reporting.md): Teams reconcile books and records repeatedly across portfolio, accounting, and investor-reporting systems.
  - [Distribution and Release Management](../workflow-library/workflows/distribution-and-release-management.md): Teams manually synchronize definitions across PLM, ERP, support, and commercial systems.
  - [Billing, Collections, and Cash Application](../workflow-library/workflows/billing-collections-and-cash-application.md): Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
  - [Cash and Inventory Reconciliation](../workflow-library/workflows/cash-and-inventory-reconciliation.md): Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
  - [Event Settlement and Reporting](../workflow-library/workflows/event-settlement-and-reporting.md): Analysts spend time matching records manually, collecting support, and rebuilding audit trails.

## SF-05 Handoff and Approval Latency

- Description: Work slows or stalls when responsibility crosses functions, approvers, organizations, or service teams.
- Frequency: 40 of 198 workflows (20.2%); 46 failure-to-workflow-usage links across 18 operating systems and 32 industries.
- Root-cause mix: Organizational (17); Legacy Architecture (9); Regulatory (8); Technical (4); Behavioral (2)
- Operating systems affected: Enterprise Governance and Shared Services (5), Product Manufacturing and Lifecycle Operations (5), Care Delivery and Reimbursement (4), Deposit, Credit, and Payment Intermediation (4), Workforce Coordination and Service Operations (4), Professional Services and Matter Management (4), Asset Utilization and Lease Management (3), Project Delivery and Contracting (3)
- Industries affected: Management of companies and enterprises (5), Federal Reserve banks, credit intermediation, and related activities (4), Construction (3), Ambulatory health care services (2), Administrative and support services (2), Legal services (2), Other services, except government (2), Motor vehicle and parts dealers (2)
- Typical systems of record involved: ERP (22); CRM (21); HCM / Workforce Management (12); Service Management (12); Loan Origination and Servicing (6); EPM and Financial Consolidation (5)
- Common human judgment points: Leadership still decides tradeoffs among long-term return, local politics, and near-term operational reality. (7); Staff balance urgency, fit, and operational constraints under incomplete documentation. (6); Analysts still judge risk, beneficial ownership complexity, and what counts as a satisfactory exception path. (4)
- Common system-of-record escape points: Most decisive discussion happens in decks and meetings rather than the planning system itself. (7); Phone calls, scanned documents, and message threads still carry the real intake context. (6); Onboarding packets, emails, shared checklists, and external verification portals carry the real process state. (4)
- Common economic leakage: Capital and support resources drift into low-return uses when performance signals are late or noisy. (7); Leakage starts with avoidable denials, no-shows, unused capacity, and mis-routed participants. (6); Slow onboarding delays revenue start dates and increases abandonment, while weak controls raise risk and rework. (4)
- Structural reason incumbents have not solved it: The binding constraint is organizational coordination rather than a single task, and incumbents generally automate local steps instead of shared accountability across handoffs. Repeated Phase 2 evidence most often states: Shared-service and capital decisions remain cross-functional and politically negotiated rather than purely model-driven. (7); Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration. (6); Verification is partly automatable, but high-value or high-risk relationships still require context-heavy review and layered approvals. (4).
- Dominant root cause: Organizational
- Confidence: Medium-High
- Evidence references:
  - [Account and Loan Onboarding](../workflow-library/workflows/account-and-loan-onboarding.md): Teams chase documents, approvals, signatures, and duplicate data entry across systems.
  - [Capital Allocation and Planning](../workflow-library/workflows/capital-allocation-and-planning.md): Review cycles are slowed by manual aggregation and commentary collection.
  - [Customer Support and Success](../workflow-library/workflows/customer-support-and-success.md): Agents and operations teams waste time on status chasing and duplicate handoffs.
  - [Collections and Loss Mitigation](../workflow-library/workflows/collections-and-loss-mitigation.md): Banking teams chase documents, reconcile exposures, and move work across front, middle, and back office queues.
  - [Dispatch and Checkout](../workflow-library/workflows/dispatch-and-checkout.md): Crews lose time to waiting, missing parts, unclear scope, and back-and-forth approvals.
  - [Document and Knowledge Management](../workflow-library/workflows/document-and-knowledge-management.md): Teams search for the right version and reconcile obligations across disconnected repositories.

## SF-07 Compliance and Evidence Burden

- Description: A large share of work is spent collecting proof, documenting exceptions, and maintaining traceability for rules, audits, or formal reporting.
- Frequency: 29 of 198 workflows (14.6%); 34 failure-to-workflow-usage links across 14 operating systems and 23 industries.
- Root-cause mix: Regulatory (28); Behavioral (1)
- Operating systems affected: Care Delivery and Reimbursement (8), Case Management and Program Administration (4), Risk Underwriting and Claims Administration (4), Product Manufacturing and Lifecycle Operations (4), Process Manufacturing and Throughput Control (4), Capital Markets and Investment Management (2), Education Delivery and Administration (1), Professional Services and Matter Management (1)
- Industries affected: Social assistance (4), Insurance carriers and related activities (4), Hospitals (3), Nursing and residential care facilities (3), Ambulatory health care services (2), Educational services (1), Electrical equipment, appliances, and components (1), Funds, trusts, and other financial vehicles (1)
- Typical systems of record involved: CRM (14); ERP (13); Manufacturing Execution System (6); HCM / Workforce Management (5); EHR and Care Management (4); Revenue Cycle Management (4)
- Common human judgment points: Inspectors still interpret severity, traceability gaps, and acceptable release decisions. (10); Control owners still decide what is material, what is remediated, and what can be tolerated temporarily. (9); Care appropriateness, urgency, and readiness still depend on expert interpretation. (4)
- Common system-of-record escape points: Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record. (10); Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems. (9); Critical case context moves through phone calls, referrals, messages, and external portals. (4)
- Common economic leakage: Failures, recalls, rework, and excess inspection labor are the major leakage points. (10); Late or weak reporting creates fines, reserve exposure, rework, and management blind spots. (9); Leakage appears as duplicated work, missed follow-up, avoidable utilization, and incomplete billable documentation. (4)
- Structural reason incumbents have not solved it: Standards and forms can be codified, but evidence lineage, interpretation, and edge-case proofwork still cross people, documents, and external systems. Repeated Phase 2 evidence most often states: Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. (10); The form of the report may be standardized, but the data lineage and exception handling still are not. (9); Even strong systems of record do not remove the need for contextual coordination across people and organizations. (4).
- Dominant root cause: Regulatory
- Confidence: Medium
- Evidence references:
  - [Compliance and Service-Provider Oversight](../workflow-library/workflows/compliance-and-service-provider-oversight.md): Teams manually stitch files, request attestations, and chase evidence for every cycle.
  - [Billing, Aid, and Regulatory Reporting](../workflow-library/workflows/billing-aid-and-regulatory-reporting.md): Teams manually stitch files, request attestations, and chase evidence for every cycle.
  - [Medication and Compliance Management](../workflow-library/workflows/medication-and-compliance-management.md): Teams spend time on outreach, refill coordination, and manual follow-up loops.
  - [Documentation and Compliance Management](../workflow-library/workflows/documentation-and-compliance-management.md): Teams manually stitch files, request attestations, and chase evidence for every cycle.
  - [Outage and Regulatory Management](../workflow-library/workflows/outage-and-regulatory-management.md): Teams manually stitch files, request attestations, and chase evidence for every cycle.
  - [Regulatory and Reinsurance Reporting](../workflow-library/workflows/regulatory-and-reinsurance-reporting.md): Teams manually stitch files, request attestations, and chase evidence for every cycle.

## SF-08 Multi-Party Trust and Dependency Gaps

- Description: The workflow depends on outside parties whose data, incentives, timing, or standards do not align with the incumbent system.
- Frequency: 28 of 198 workflows (14.1%); 39 failure-to-workflow-usage links across 12 operating systems and 27 industries.
- Root-cause mix: Technical (21); Economic (4); Legacy Architecture (2); Organizational (1)
- Operating systems affected: Product Manufacturing and Lifecycle Operations (10), Transportation Network Operations (6), Process Manufacturing and Throughput Control (6), Field Production and Resource Extraction (5), Venue, Hospitality, and Attendance Operations (2), Distribution and Trade Operations (2), Network Infrastructure Operations (2), Project Delivery and Contracting (2)
- Industries affected: Oil and gas extraction (3), Truck transportation (2), Other transportation and support activities (2), Air transportation (2), Wholesale trade (2), Food and beverage and tobacco products (2), Farms (2), Plastics and rubber products (2)
- Typical systems of record involved: ERP (22); Supply Chain Planning (6); Manufacturing Execution System (6); PLM and Engineering Design (6); CRM (5); Maintenance Management (4)
- Common human judgment points: Planners still decide which signals to trust and when the model output does not fit local reality. (13); Controllers interpret service priorities and real-world constraints faster than static optimization models. (8); Source selection and expedites still rely on local knowledge and changing supplier behavior. (4)
- Common system-of-record escape points: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations. (13); Carrier calls, texts, and manual route notes remain central to live execution. (8); Exception discussions and commitments often move into email and supplier portals beyond the ERP trail. (4)
- Common economic leakage: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting. (13); The biggest leaks are empty capacity, bad routing, detention, and poor network utilization. (8); Leakage appears through rush buys, stockouts, overbuying, and weak term control. (4)
- Structural reason incumbents have not solved it: Automation stops at the enterprise boundary because counterparties, partners, payers, suppliers, and regulators do not share one operating model or one trusted data layer. Repeated Phase 2 evidence most often states: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. (13); Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. (8); Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. (4).
- Dominant root cause: Technical
- Confidence: Medium
- Evidence references:
  - [Supplier and Subcontractor Management](../workflow-library/workflows/supplier-and-subcontractor-management.md): Structured supplier master data is not the same as reliable day-to-day execution behavior. It typically spans 1 operating-system context and 3 systems-of-rec...
  - [Capacity and Load Planning](../workflow-library/workflows/capacity-and-load-planning.md): Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. It typically spans 1 operating-system context and...
  - [Production Planning](../workflow-library/workflows/production-planning.md): The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. It typically spans 2 operating-system contexts...
  - [Supplier Scheduling and Procurement](../workflow-library/workflows/supplier-scheduling-and-procurement.md): Structured supplier master data is not the same as reliable day-to-day execution behavior. It typically spans 1 operating-system context and 6 systems-of-rec...
  - [Supplier Coordination and Compliance](../workflow-library/workflows/supplier-coordination-and-compliance.md): Structured supplier master data is not the same as reliable day-to-day execution behavior. It typically spans 1 operating-system context and 3 systems-of-rec...
  - [Material Sourcing](../workflow-library/workflows/material-sourcing.md): Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. It typically spans 2 operating-s...
