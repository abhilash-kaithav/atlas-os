#!/usr/bin/env python3
"""Build Phase 2 workflow mapping artifacts from the normalized Atlas census."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from build_industry_census_normalized import (
    OPERATING_SYSTEM_DEFINITIONS,
    SYSTEM_CATEGORY_DEFINITIONS,
    SYSTEM_CATEGORY_EXAMPLES,
    WORKFLOW_FAMILY_DEFINITIONS,
    escape_md,
)


ROOT = Path(__file__).resolve().parents[1]
INDUSTRY_CENSUS_DIR = ROOT / "knowledge" / "research" / "industry-census"
WORKFLOW_LIBRARY_DIR = ROOT / "knowledge" / "research" / "workflow-library"
WORKFLOW_DOCS_DIR = WORKFLOW_LIBRARY_DIR / "workflows"
SOURCE_CSV = INDUSTRY_CENSUS_DIR / "top-50-industry-census-normalized.csv"
LIBRARY_CSV = WORKFLOW_LIBRARY_DIR / "canonical-workflow-library.csv"
INDEX_CSV = WORKFLOW_LIBRARY_DIR / "workflow-operating-system-industry-index.csv"
README_DOC = WORKFLOW_LIBRARY_DIR / "README.md"
SOFTWARE_RESEARCH_DOC = WORKFLOW_LIBRARY_DIR / "software-research.md"

GENERATED_DATE = "2026-08-14"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def profile(
    objective: str,
    trigger: str,
    end_outcome: str,
    primary_actors: list[str],
    major_decisions: list[str],
    major_handoffs: list[str],
    money_lost: str,
    time_lost: str,
    human_judgment: str,
    system_escape: str,
    why_unsolved: str,
    primary_reason: str,
) -> dict[str, object]:
    return {
        "objective": objective,
        "trigger": trigger,
        "end_outcome": end_outcome,
        "primary_actors": primary_actors,
        "major_decisions": major_decisions,
        "major_handoffs": major_handoffs,
        "money_lost": money_lost,
        "time_lost": time_lost,
        "human_judgment": human_judgment,
        "system_escape": system_escape,
        "why_unsolved": why_unsolved,
        "primary_reason": primary_reason,
    }


FAMILY_DEFAULT_PROFILES: dict[str, dict[str, object]] = {
    "Access, Intake, and Contracting": profile(
        objective="Admit qualified demand into the operating system with the minimum information, approvals, and commercial terms required to proceed.",
        trigger="A new prospect, participant, counterparty, or service request enters the funnel.",
        end_outcome="A qualified record, schedule, or agreement is created and handed to downstream planning or delivery teams.",
        primary_actors=["frontline intake or sales team", "customer or participant", "operations coordinator", "approver or risk owner"],
        major_decisions=[
            "Is the request qualified and in policy?",
            "What terms, slot, or service level should be offered?",
            "Can the work proceed now or does it require more data or approval?",
        ],
        major_handoffs=[
            "frontline intake -> operations scheduling",
            "sales or intake -> finance or risk review",
            "approved request -> delivery owner",
        ],
        money_lost="Poor qualification, pricing errors, avoidable no-shows, and weak contract hygiene create leakage before execution starts.",
        time_lost="Teams chase missing information, approvals, and schedule availability across email, phone, and shared documents.",
        human_judgment="Humans still arbitrate exceptions, fit, urgency, and risk tolerance when intake data is incomplete or context is changing.",
        system_escape="Critical context lives in inboxes, call notes, PDFs, and spreadsheets before the final system record is updated.",
        why_unsolved="Structured fields handle the routine path, but real intake varies by exception, policy nuance, and local operating context.",
        primary_reason="Organizational",
    ),
    "Clinical and Case Operations": profile(
        objective="Coordinate ongoing service delivery, documentation, and next actions around an active person, patient, or case record.",
        trigger="A patient, resident, or beneficiary has an open episode of care or case plan that requires active management.",
        end_outcome="The active record is updated, required interventions are completed, and the next accountable owner is clear.",
        primary_actors=["clinician or case worker", "patient or beneficiary", "supervisor", "adjacent care or referral partner"],
        major_decisions=[
            "What is the next best intervention or service step?",
            "Does the record support the required clinical or program action?",
            "What exception needs escalation or coordination across teams?",
        ],
        major_handoffs=[
            "intake or scheduling -> care or case team",
            "primary service owner -> specialist or referral partner",
            "service team -> billing, reporting, or compliance staff",
        ],
        money_lost="Missing documentation, avoidable rework, failed authorizations, and unclosed loops reduce reimbursement and increase cost-to-serve.",
        time_lost="Care and case teams spend time reconciling status across calls, messages, paper forms, and incomplete records.",
        human_judgment="The hardest decisions depend on severity, appropriateness, readiness, and contextual knowledge that structured data rarely captures fully.",
        system_escape="Teams leave the record for phone calls, texts, shared notes, and external provider portals to coordinate actual work.",
        why_unsolved="These workflows cross regulated documentation, real-world human variability, and inter-organizational coordination that software alone cannot standardize end to end.",
        primary_reason="Regulatory",
    ),
    "Customer and Experience Operations": profile(
        objective="Protect the customer relationship during the live transaction or service experience while preserving revenue, retention, and service quality.",
        trigger="A customer needs to buy, be served, be retained, or receive follow-up support.",
        end_outcome="The customer interaction is resolved, the account is updated, and the next commercial or service action is clear.",
        primary_actors=["customer-facing staff", "customer", "operations manager", "support or fulfillment partner"],
        major_decisions=[
            "How should the request be prioritized and resolved?",
            "What exception requires compensation, override, or escalation?",
            "What next action best protects retention or margin?",
        ],
        major_handoffs=[
            "customer-facing team -> operations or fulfillment",
            "support agent -> finance or billing",
            "service resolution -> retention or account owner",
        ],
        money_lost="Leakage appears through discounts, giveaway behavior, missed upsell, churn, re-service, and preventable service failure.",
        time_lost="Time is lost to channel switching, queue triage, manual status checks, and repeated customer explanation.",
        human_judgment="Frontline workers constantly balance policy, empathy, urgency, and commercial context under incomplete information.",
        system_escape="Teams use chat, calls, email, and side logs when the system cannot capture the nuance of a live customer situation.",
        why_unsolved="Experience workflows combine soft judgment, fragmented channel data, and fast-moving exception handling that resists rigid automation.",
        primary_reason="Behavioral",
    ),
    "Delivery and Service Execution": profile(
        objective="Convert a committed order, project, or service promise into completed work that meets scope, timing, and quality expectations.",
        trigger="Demand has been accepted and operational work is ready to be performed.",
        end_outcome="The work is completed, status is recorded, and downstream billing or follow-up can proceed.",
        primary_actors=["operations lead", "frontline delivery team", "customer or receiving party", "scheduler or dispatcher"],
        major_decisions=[
            "What work should be done first and by whom?",
            "How should exceptions or changes in scope be handled?",
            "What completion threshold is enough to close or advance the job?",
        ],
        major_handoffs=[
            "planning or scheduling -> execution team",
            "execution team -> customer or receiver",
            "completed work -> finance, reporting, or support team",
        ],
        money_lost="Leakage comes from rework, poor sequencing, missed milestones, overtime, spoilage, and avoidable service failures.",
        time_lost="Execution teams lose time on missing inputs, waiting, field coordination, status chasing, and exception resolution.",
        human_judgment="Supervisors and frontline operators continually rebalance priorities, constraints, and real-world conditions.",
        system_escape="Actual execution is coordinated through calls, whiteboards, texts, and local spreadsheets when reality moves faster than the system.",
        why_unsolved="The workflow changes minute to minute based on field conditions, dependencies, and incomplete telemetry across teams and vendors.",
        primary_reason="Legacy Architecture",
    ),
    "Finance and Revenue Operations": profile(
        objective="Translate completed economic activity into accurate revenue recognition, cash realization, and controlled financial records.",
        trigger="A billable, payable, reportable, or collectible financial event occurs.",
        end_outcome="The transaction is posted, reconciled, or collected with a defensible audit trail.",
        primary_actors=["finance operations staff", "billing or collections team", "operations source owner", "customer, payer, or counterparty"],
        major_decisions=[
            "Is the transaction valid, complete, and supported by source evidence?",
            "What exception requires adjustment, escalation, or reserve treatment?",
            "When can the item be closed versus left open for follow-up?",
        ],
        major_handoffs=[
            "operations source system -> billing or accounting team",
            "billing or claims team -> payer, customer, or counterparty",
            "open exceptions -> collections, audit, or management review",
        ],
        money_lost="Leakage comes from missed charges, denial or dispute cycles, slow collections, weak controls, and exception handling errors.",
        time_lost="Teams burn time on reconciliation, documentation requests, approval loops, and manual follow-up across systems.",
        human_judgment="Experienced operators interpret contract nuance, exceptions, materiality, and the most efficient path to close.",
        system_escape="Finance teams export data to spreadsheets, email threads, bank portals, and customer communications to close open items.",
        why_unsolved="The workflow is only partly rules-based; the rest depends on upstream data quality, contract interpretation, and fragmented evidence trails.",
        primary_reason="Legacy Architecture",
    ),
    "Governance and Portfolio Operations": profile(
        objective="Provide management, investors, or leadership with accurate oversight of performance, capital, obligations, and risk.",
        trigger="A planning cycle, reporting period, governance checkpoint, or exception review requires updated oversight.",
        end_outcome="Leadership receives a current view of exposure and performance with decisions or actions documented.",
        primary_actors=["finance or portfolio team", "executive sponsor", "operations leaders", "external stakeholders or investors"],
        major_decisions=[
            "Which metrics or exceptions matter enough to escalate?",
            "How should capital, resources, or follow-up actions be reallocated?",
            "What is the authoritative number when sources disagree?",
        ],
        major_handoffs=[
            "line operations -> finance or portfolio team",
            "portfolio team -> leadership or investors",
            "governance review -> operating owners for action",
        ],
        money_lost="Poor visibility delays corrective action, misallocates capital, and hides underperformance or controllable risk.",
        time_lost="Teams reconcile inconsistent definitions, rebuild reports, and collect commentary manually before every review.",
        human_judgment="Leadership and portfolio teams interpret signal quality, risk appetite, and materiality rather than trusting raw dashboards blindly.",
        system_escape="The decisive conversation happens in slide decks, emails, committee notes, and spreadsheet bridges between systems.",
        why_unsolved="Oversight work spans multiple systems of record, changing definitions, and stakeholder-specific views that are hard to fully normalize.",
        primary_reason="Organizational",
    ),
    "Network and Transportation Operations": profile(
        objective="Move capacity, assets, or service commitments across a network while controlling utilization, timing, and exceptions.",
        trigger="Demand must be routed, assigned, monitored, or recovered across a transport or service network.",
        end_outcome="Capacity is allocated, movement is tracked, and network exceptions are resolved or escalated.",
        primary_actors=["planner or dispatcher", "carrier or field crew", "operations control team", "customer or receiving location"],
        major_decisions=[
            "Which route, carrier, or asset should handle the work?",
            "How should the network respond to delay, disruption, or overload?",
            "When is it better to expedite, reroute, or reschedule?",
        ],
        major_handoffs=[
            "planning -> dispatch or carrier operations",
            "in-motion network -> customer service or exception desk",
            "completed movement -> billing, proof, or settlement team",
        ],
        money_lost="Empty miles, poor utilization, detention, disruption costs, and missed commitments drive preventable margin loss.",
        time_lost="Planners lose time on status chasing, manual re-planning, phone coordination, and exception triage.",
        human_judgment="Network operators weigh tradeoffs among cost, service, safety, and downstream disruption under imperfect visibility.",
        system_escape="Critical updates travel by call, text, EDI exception, and shared trackers before systems catch up.",
        why_unsolved="Even with better telemetry, network state changes faster than shared planning models and cross-party data standards can absorb.",
        primary_reason="Technical",
    ),
    "Planning and Allocation": profile(
        objective="Allocate constrained capacity, inventory, labor, or capital against expected demand and operating constraints.",
        trigger="A planning horizon opens or conditions change enough to require a refreshed allocation decision.",
        end_outcome="A plan is published, assumptions are documented, and downstream execution teams have a working baseline.",
        primary_actors=["planner or analyst", "operations manager", "commercial owner", "finance or supply partner"],
        major_decisions=[
            "What demand or capacity assumptions are credible enough to plan against?",
            "How should scarce resources be allocated across competing needs?",
            "When should the plan be re-cut versus allowed to stand?",
        ],
        major_handoffs=[
            "commercial or demand signals -> planning team",
            "planning team -> operations or procurement",
            "published plan -> execution teams and finance",
        ],
        money_lost="Weak planning causes overstocks, stockouts, underutilization, missed revenue, overtime, and poor capital deployment.",
        time_lost="Analysts spend time stitching data, rebuilding assumptions, and socializing revised plans across functions.",
        human_judgment="Planners must decide what demand signals to trust and how to balance conflicting objectives when data is noisy.",
        system_escape="Scenario work often happens outside the system in spreadsheets, side models, and ad hoc meetings.",
        why_unsolved="Optimization engines exist, but the hard part is unstable demand, incomplete constraints, and low trust in the shared assumptions.",
        primary_reason="Technical",
    ),
    "Product, Content, and Engineering": profile(
        objective="Define, change, package, and release the product, content, or engineering record that downstream teams will execute against.",
        trigger="A new offering, change request, release milestone, or content requirement needs controlled execution.",
        end_outcome="The authoritative product or content record is updated and handed to downstream commercial or operational teams.",
        primary_actors=["product, engineering, or content owner", "operations partner", "commercial owner", "governance or legal reviewer"],
        major_decisions=[
            "What should change and what should stay frozen?",
            "What dependency, approval, or downstream impact blocks release?",
            "When is the record complete enough to publish or promote?",
        ],
        major_handoffs=[
            "product or engineering owner -> operations or release team",
            "creative or technical team -> legal, finance, or commercial review",
            "approved release -> downstream sales, production, or service teams",
        ],
        money_lost="Poor change control, slow release cycles, and inconsistent master data create rework, delays, and margin erosion downstream.",
        time_lost="Teams wait on approvals, version alignment, and manual propagation of changes across systems.",
        human_judgment="The hardest calls involve priority, tradeoff, quality threshold, and cross-functional impact rather than deterministic rules.",
        system_escape="Decisions live in docs, chats, slide decks, and design artifacts that are not synchronized cleanly with production records.",
        why_unsolved="The workflow spans structured master data and unstructured collaborative work, so no single system cleanly owns the whole process.",
        primary_reason="Legacy Architecture",
    ),
    "Production and Asset Operations": profile(
        objective="Operate physical assets, sites, or production lines safely and predictably while preserving throughput, uptime, and quality.",
        trigger="A physical operation must run, be maintained, or be restored to readiness.",
        end_outcome="The asset or process reaches the required operating state with status and exceptions recorded.",
        primary_actors=["operations supervisor", "frontline operator or technician", "maintenance or quality staff", "planner"],
        major_decisions=[
            "What operating mode or work sequence best fits current constraints?",
            "Which issue requires intervention now versus later?",
            "When is output or asset condition good enough to continue or release?",
        ],
        major_handoffs=[
            "planning -> plant, field, or facility team",
            "operations -> maintenance or quality team",
            "completed work -> logistics, billing, or governance team",
        ],
        money_lost="Downtime, scrap, overtime, poor turns, and underutilized assets create immediate economic leakage.",
        time_lost="Teams lose time to waiting, manual coordination, unavailable parts, and inconsistent shift handoffs.",
        human_judgment="Frontline supervisors and technicians constantly interpret operating signals, trade off risk, and sequence recovery actions.",
        system_escape="Real work is often coordinated through radios, whiteboards, paper logs, and tribal knowledge alongside the formal system.",
        why_unsolved="Operational technology, enterprise systems, and local work practices remain only partially integrated in most environments.",
        primary_reason="Legacy Architecture",
    ),
    "Risk, Compliance, and Reporting": profile(
        objective="Keep the organization inside policy, quality, and regulatory boundaries while proving that control through evidence.",
        trigger="A control point, audit requirement, product or service exception, or formal reporting cycle requires review.",
        end_outcome="The exception is resolved or documented and the required evidence is available for internal or external review.",
        primary_actors=["risk, compliance, or quality owner", "operations manager", "frontline record owner", "external regulator, auditor, or partner"],
        major_decisions=[
            "What exception is material enough to escalate?",
            "What evidence satisfies the control or reporting requirement?",
            "Can the process continue, or does it need remediation first?",
        ],
        major_handoffs=[
            "operations -> quality, risk, or compliance team",
            "compliance team -> regulator, customer, or auditor",
            "findings -> operating owner for remediation",
        ],
        money_lost="Leakage appears through fines, rejected output, reserve impacts, rework, and the drag of over-control where trust is low.",
        time_lost="Teams repeatedly compile evidence, chase signatures, and reconstruct context after the fact.",
        human_judgment="Materiality, root cause, and acceptable corrective action are still judged by experienced operators and control owners.",
        system_escape="Evidence leaves the system in attachments, spreadsheets, audit binders, email approvals, and external portals.",
        why_unsolved="Controls are explicit, but the evidence trail is fragmented and each exception still requires context-rich interpretation.",
        primary_reason="Regulatory",
    ),
    "Sourcing and Supply": profile(
        objective="Secure the inputs, supplier commitments, and replenishment actions needed to keep downstream operations moving.",
        trigger="Inventory, materials, supplier capacity, or subcontractor commitment is needed for future execution.",
        end_outcome="A supply commitment is placed, confirmed, and handed to receiving, planning, or execution teams.",
        primary_actors=["buyer or procurement lead", "supplier or subcontractor", "planner", "receiving or operations manager"],
        major_decisions=[
            "Which supplier or source is best under current constraints?",
            "What quantity, timing, and terms should be committed?",
            "What exception needs escalation because supply no longer matches plan?",
        ],
        major_handoffs=[
            "planning -> procurement",
            "procurement -> supplier or subcontractor",
            "confirmed supply -> receiving, planning, or field teams",
        ],
        money_lost="Expedites, weak terms, maverick buying, shortages, and supplier misses create direct margin pressure.",
        time_lost="Buyers spend time on follow-up, quote comparison, exception handling, and schedule recovery across fragmented channels.",
        human_judgment="Source selection, tradeoff decisions, and supplier negotiations still depend on local knowledge and changing market context.",
        system_escape="Negotiation, exception handling, and commitment tracking often happen in email, calls, and supplier portals outside the ERP trail.",
        why_unsolved="Structured purchasing tools exist, but upstream demand volatility and heterogeneous supplier behavior keep the workflow only partly standardized.",
        primary_reason="Economic",
    ),
    "Workforce and Labor Operations": profile(
        objective="Match available labor to near-term demand while preserving productivity, compliance, and labor economics.",
        trigger="Demand changes, shifts open, or work needs to be assigned to a finite labor pool.",
        end_outcome="Labor is scheduled or assigned and the responsible team has a clear execution plan.",
        primary_actors=["scheduler or staffing lead", "frontline manager", "worker", "HR or payroll partner"],
        major_decisions=[
            "Who should work, when, and on what task?",
            "How should labor constraints, skills, and policy rules be balanced?",
            "When should the schedule be rewritten versus managed in place?",
        ],
        major_handoffs=[
            "forecast or service demand -> scheduler",
            "scheduler -> frontline manager and worker",
            "actual hours and outcomes -> payroll, billing, or performance review",
        ],
        money_lost="Leakage shows up as overtime, idle labor, poor utilization, attrition, service misses, and payroll corrections.",
        time_lost="Schedulers spend time juggling availability, callouts, compliance rules, and last-minute changes.",
        human_judgment="Managers still rely on trust, skill familiarity, customer context, and fairness judgments that do not fit neatly into rules.",
        system_escape="Live staffing changes move through calls, texts, messaging apps, and paper rosters faster than the workforce system updates.",
        why_unsolved="Workforce tools optimize the baseline, but actual labor coordination depends on fast exceptions and local human context.",
        primary_reason="Behavioral",
    ),
}


THEME_OVERRIDES: dict[str, dict[str, object]] = {
    "access_admission": profile(
        objective="Move a person into service with the right eligibility, timing, and required intake information captured up front.",
        trigger="A person requests entry into care, education, or a case-based program.",
        end_outcome="The person is cleared for service, scheduled or enrolled, and visible to downstream service teams.",
        primary_actors=["intake coordinator", "participant or patient", "authorization or eligibility staff", "service scheduler"],
        major_decisions=[
            "Is the person eligible and appropriately prioritized?",
            "What slot, program, or service path should they enter?",
            "What information gap blocks progression into service?",
        ],
        major_handoffs=[
            "front-door intake -> authorization or scheduling",
            "eligibility review -> service owner",
            "admitted participant -> ongoing service team",
        ],
        money_lost="Leakage starts with avoidable denials, no-shows, unused capacity, and mis-routed participants.",
        time_lost="Teams repeatedly collect the same history and chase coverage, paperwork, and schedule coordination.",
        human_judgment="Staff balance urgency, fit, and operational constraints under incomplete documentation.",
        system_escape="Phone calls, scanned documents, and message threads still carry the real intake context.",
        why_unsolved="Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration.",
        primary_reason="Organizational",
    ),
    "lead_sales": profile(
        objective="Convert demand into qualified commercial opportunities with enough context to price, commit, and forecast reliably.",
        trigger="A prospect, inbound inquiry, or account expansion signal enters the pipeline.",
        end_outcome="A qualified opportunity is advanced, disqualified, or handed to the next commercial owner with clear next steps.",
        primary_actors=["sales or business development owner", "prospect or account", "solution or operations partner", "commercial approver"],
        major_decisions=[
            "Is the opportunity real, winnable, and worth pursuing?",
            "What next step best advances conversion without overcommitting capacity?",
            "What level of customization or executive attention is justified?",
        ],
        major_handoffs=[
            "marketing or inbound lead -> account owner",
            "account owner -> pricing, proposal, or operations review",
            "qualified opportunity -> implementation or delivery team",
        ],
        money_lost="Poor qualification, weak follow-up, and over-discounting waste selling capacity and suppress win rates.",
        time_lost="Commercial teams lose time assembling context, chasing stakeholders, and rebuilding proposals from prior deals.",
        human_judgment="Win probability, account politics, and deal strategy still sit heavily in human judgment.",
        system_escape="Critical context lives in email, notes, calls, and ad hoc documents outside the CRM fields.",
        why_unsolved="CRM structures pipeline data, but deal progression still depends on relationship context and bespoke coordination.",
        primary_reason="Behavioral",
    ),
    "quote_estimate": profile(
        objective="Translate demand into a priced, scoped, and approvable commercial commitment that the business can actually deliver.",
        trigger="A qualified request needs pricing, scope definition, or a formal quote, estimate, or proposal.",
        end_outcome="The quote or proposal is issued with approved assumptions, margins, and delivery commitments.",
        primary_actors=["estimator or pricing analyst", "sales owner", "operations or supply partner", "approver"],
        major_decisions=[
            "What price, scope, or configuration best fits the request and margin target?",
            "Which assumptions need approval because they materially change risk or delivery feasibility?",
            "When should the opportunity be declined rather than priced?",
        ],
        major_handoffs=[
            "qualified demand -> pricing or estimating",
            "estimating -> operations, engineering, or supply review",
            "approved quote -> customer or contracting team",
        ],
        money_lost="Leakage comes from underpricing, scope misses, inaccurate assumptions, and change orders that were predictable at quote time.",
        time_lost="Estimators wait on inputs, rebuild historical assumptions, and route approvals repeatedly.",
        human_judgment="Estimators must judge risk, uncertainty, and customer-specific nuance that raw historical data rarely captures cleanly.",
        system_escape="The actual pricing narrative often sits in spreadsheets, markups, and offline review threads.",
        why_unsolved="Rules can price the simple path, but profitable quoting still depends on tacit knowledge and cross-functional review.",
        primary_reason="Technical",
    ),
    "onboarding_kyc": profile(
        objective="Stand up a new account, relationship, or fund record while satisfying verification, risk, and setup requirements.",
        trigger="A new customer, borrower, investor, or fund relationship is approved for activation.",
        end_outcome="The relationship is activated in the necessary systems with required checks, documents, and controls completed.",
        primary_actors=["onboarding specialist", "customer or counterparty", "risk or compliance reviewer", "operations setup team"],
        major_decisions=[
            "Is the relationship verified enough to activate?",
            "What documentation or control gap still blocks go-live?",
            "Which setup path fits the relationship complexity and risk level?",
        ],
        major_handoffs=[
            "sales or relationship owner -> onboarding team",
            "onboarding -> risk, compliance, or legal review",
            "approved setup -> servicing or operations team",
        ],
        money_lost="Slow onboarding delays revenue start dates and increases abandonment, while weak controls raise risk and rework.",
        time_lost="Teams chase documents, approvals, signatures, and duplicate data entry across systems.",
        human_judgment="Analysts still judge risk, beneficial ownership complexity, and what counts as a satisfactory exception path.",
        system_escape="Onboarding packets, emails, shared checklists, and external verification portals carry the real process state.",
        why_unsolved="Verification is partly automatable, but high-value or high-risk relationships still require context-heavy review and layered approvals.",
        primary_reason="Regulatory",
    ),
    "lease_acquisition": profile(
        objective="Keep monetizable capacity occupied by winning the right tenants or reservations and preserving renewal continuity.",
        trigger="A unit, asset, or capacity block must be leased, renewed, or moved through the reservation pipeline.",
        end_outcome="Capacity is committed on acceptable terms and downstream readiness or billing actions are triggered.",
        primary_actors=["leasing or reservations staff", "prospect or tenant", "property or asset manager", "operations support"],
        major_decisions=[
            "What terms, concessions, or pricing are acceptable for this capacity?",
            "Should the existing relationship be renewed, repriced, or replaced?",
            "What readiness or turnover work must occur before commitment?",
        ],
        major_handoffs=[
            "prospect management -> approval or contracting",
            "signed commitment -> property or operations team",
            "live lease or reservation -> billing and service teams",
        ],
        money_lost="Vacancy, poor renewal timing, weak concessions discipline, and slow readiness cycles directly reduce yield.",
        time_lost="Leasing teams spend time coordinating tours, approvals, readiness updates, and status checks across systems.",
        human_judgment="Staff balance occupancy goals, asset condition, pricing power, and relationship context when deciding terms.",
        system_escape="Negotiation details, readiness notes, and exceptions live in email, call logs, and side trackers.",
        why_unsolved="The workflow spans commercial negotiation, physical readiness, and revenue optimization rather than a single clean transaction.",
        primary_reason="Legacy Architecture",
    ),
    "reservation_ticketing": profile(
        objective="Convert finite capacity into confirmed bookings or admissions while preserving pricing discipline and customer experience.",
        trigger="A guest, attendee, shipper, or customer requests access to a dated capacity slot.",
        end_outcome="Capacity is reserved, priced, and confirmed with downstream service or fulfillment teams informed.",
        primary_actors=["reservation or ticketing agent", "customer", "revenue or capacity manager", "operations team"],
        major_decisions=[
            "What inventory should be offered at what price and under what rules?",
            "How should holds, cancellations, and over-capacity risk be managed?",
            "What exception needs approval or manual intervention?",
        ],
        major_handoffs=[
            "customer request -> booking or ticketing system",
            "confirmed reservation -> venue, hotel, or operations staff",
            "completed stay or event -> settlement or service follow-up",
        ],
        money_lost="Leakage comes from spoilage, bad holds, channel mix mistakes, refunds, and poor yield control.",
        time_lost="Teams burn time resolving inventory conflicts, special requests, and distribution-channel mismatches.",
        human_judgment="Operators still decide how to recover service, override inventory, and handle edge-case customers.",
        system_escape="Special handling moves through calls, guest notes, and partner channels outside the clean reservation record.",
        why_unsolved="Inventory can be digitized, but exception-heavy capacity control and live service recovery still depend on people.",
        primary_reason="Technical",
    ),
    "donor_sponsorship": profile(
        objective="Convert sponsors, donors, or patrons into committed revenue and managed relationships around an event or institution.",
        trigger="A sponsorship, patronage, or donor opportunity is created or renewed.",
        end_outcome="The commitment is secured, benefits are tracked, and fulfillment or stewardship actions are handed off.",
        primary_actors=["development or partnerships team", "donor or sponsor", "finance staff", "event or program owner"],
        major_decisions=[
            "Which relationship deserves active cultivation now?",
            "What package, recognition, or benefit structure should be offered?",
            "What follow-up is required to protect renewal likelihood?",
        ],
        major_handoffs=[
            "relationship owner -> finance or contracting",
            "secured commitment -> program or event operations",
            "post-event outcome -> stewardship and renewal owner",
        ],
        money_lost="Revenue is lost through weak follow-up, inconsistent fulfillment, and poor visibility into renewal risk.",
        time_lost="Teams manually coordinate donor history, package details, and fulfillment status across systems and documents.",
        human_judgment="Relationship strength, timing, and ask strategy are still judged person to person.",
        system_escape="Stewardship context lives in notes, conversations, and one-off trackers rather than a complete shared record.",
        why_unsolved="The workflow depends heavily on relationship nuance and bespoke package management rather than purely transactional logic.",
        primary_reason="Behavioral",
    ),
    "clinical_case": profile(
        objective="Advance the active care or case plan safely while documenting enough context for the next accountable action.",
        trigger="An open care episode or case requires intervention, documentation, or referral follow-through.",
        end_outcome="The next action, service step, or referral status is updated and visible to the right owner.",
        primary_actors=["clinician or case worker", "patient or beneficiary", "care coordinator", "referral or specialist partner"],
        major_decisions=[
            "What intervention or next step is most appropriate now?",
            "Does the current record support safe continuation or escalation?",
            "What coordination gap puts outcome or reimbursement at risk?",
        ],
        major_handoffs=[
            "primary record owner -> specialist or downstream service provider",
            "active service -> billing, claims, or reporting team",
            "ongoing case -> supervisor or escalation path",
        ],
        money_lost="Leakage appears as duplicated work, missed follow-up, avoidable utilization, and incomplete billable documentation.",
        time_lost="Teams repeatedly reconcile status and chase missing clinical, referral, or plan information.",
        human_judgment="Care appropriateness, urgency, and readiness still depend on expert interpretation.",
        system_escape="Critical case context moves through phone calls, referrals, messages, and external portals.",
        why_unsolved="Even strong systems of record do not remove the need for contextual coordination across people and organizations.",
        primary_reason="Regulatory",
    ),
    "medication_management": profile(
        objective="Maintain safe medication, compliance, and follow-up status while keeping the longitudinal record current.",
        trigger="Medication adherence, refill, or compliance status requires active review or intervention.",
        end_outcome="Medication status is updated, the next required action is completed, and exceptions are escalated appropriately.",
        primary_actors=["clinician or care manager", "patient or resident", "pharmacy partner", "compliance or quality reviewer"],
        major_decisions=[
            "Is the patient or resident compliant enough to stay on the current plan?",
            "What issue requires outreach, refill, or escalation?",
            "What documentation is required to support the action taken?",
        ],
        major_handoffs=[
            "care team -> pharmacy or medication partner",
            "medication issue -> supervising clinician",
            "resolved status -> billing, quality, or record team",
        ],
        money_lost="Leakage appears through avoidable readmissions, failed adherence, and unbillable documentation gaps.",
        time_lost="Teams spend time on outreach, refill coordination, and manual follow-up loops.",
        human_judgment="Medication decisions still depend on severity, tolerance, behavior, and contextual risk.",
        system_escape="Call logs, refill messages, and compliance notes often live outside the structured medication record.",
        why_unsolved="Medication management is highly regulated and behavior-heavy, so closed-loop automation remains incomplete.",
        primary_reason="Behavioral",
    ),
    "customer_support": profile(
        objective="Resolve customer issues quickly without sacrificing margin, service quality, or downstream operational clarity.",
        trigger="A customer asks for support, raises an issue, or requires live service intervention.",
        end_outcome="The issue is resolved or routed correctly and the account or service record reflects the outcome.",
        primary_actors=["support or service agent", "customer", "operations team", "account owner"],
        major_decisions=[
            "What is the true root cause and who owns it?",
            "Should the issue be fixed, compensated, escalated, or monitored?",
            "What follow-up best protects future retention?",
        ],
        major_handoffs=[
            "customer-facing channel -> support queue",
            "support -> operations, field, or finance",
            "resolution -> account owner or retention motion",
        ],
        money_lost="Repeat contacts, credits, field callbacks, and unresolved issues raise support cost and churn risk.",
        time_lost="Agents and operations teams waste time on status chasing and duplicate handoffs.",
        human_judgment="Good service recovery depends on empathy, prioritization, and contextual interpretation.",
        system_escape="The most important context often lives in conversations, notes, and side chats rather than system fields.",
        why_unsolved="Support flows cross channels and teams, and the edge cases that matter most remain unstructured.",
        primary_reason="Organizational",
    ),
    "retention_renewal": profile(
        objective="Preserve profitable relationships by identifying risk early and executing the right renewal, retention, or remarketing action.",
        trigger="A contract, account, subscriber, or customer relationship shows renewal timing or churn risk.",
        end_outcome="The relationship is renewed, recovered, remarketed, or exited with a clear ownership path.",
        primary_actors=["account owner", "customer success or retention team", "customer", "commercial approver"],
        major_decisions=[
            "Is the relationship healthy enough to renew as is?",
            "What price, package, or intervention is worth offering?",
            "When should the account be saved, reshaped, or allowed to churn?",
        ],
        major_handoffs=[
            "usage or performance signals -> account owner",
            "retention motion -> pricing or finance review",
            "renewed account -> delivery, support, or billing team",
        ],
        money_lost="Late risk detection, weak expansion discipline, and reactive renewal handling erode retention economics.",
        time_lost="Teams assemble context manually across service records, invoices, and relationship notes before every renewal conversation.",
        human_judgment="Renewal strategy depends on relationship strength, future potential, and nuanced commercial tradeoffs.",
        system_escape="The decisive conversations happen in calls, emails, and side planning decks outside the system of record.",
        why_unsolved="Signals are fragmented and the most important retention decisions are strategic rather than purely operational.",
        primary_reason="Behavioral",
    ),
    "point_of_sale": profile(
        objective="Capture the live transaction cleanly while keeping payment, loyalty, and service context synchronized.",
        trigger="A customer is ready to order, pay, check out, or complete a live in-person transaction.",
        end_outcome="The transaction is completed, tender is recorded, and any downstream fulfillment or settlement record is updated.",
        primary_actors=["frontline cashier or associate", "customer", "store or venue manager", "finance or reconciliation staff"],
        major_decisions=[
            "What tender, adjustment, or loyalty treatment should apply?",
            "How should an exception or mismatch be resolved in the moment?",
            "What transaction should be held, voided, or escalated?",
        ],
        major_handoffs=[
            "customer interaction -> POS and payment systems",
            "completed transaction -> fulfillment, service, or inventory team",
            "day close -> finance and reconciliation staff",
        ],
        money_lost="Leakage appears through shrink, tender errors, bad overrides, abandoned carts, and loyalty mistakes.",
        time_lost="Teams spend time on line delays, exception handling, and end-of-day balancing.",
        human_judgment="Frontline staff still decide how to recover failures and apply judgment-based overrides.",
        system_escape="Exception handling moves into notes, supervisor conversations, and manual balancing sheets.",
        why_unsolved="Core POS is mature, but live edge cases and the downstream reconciliation burden remain stubbornly human.",
        primary_reason="Legacy Architecture",
    ),
    "promotion_pricing": profile(
        objective="Use pricing, assortment, and promotional levers to protect margin while matching demand and channel realities.",
        trigger="A pricing, inventory age, channel, or campaign change requires a new commercial decision.",
        end_outcome="The updated commercial rule is published and downstream sales or replenishment teams can act on it.",
        primary_actors=["merchandising or revenue manager", "commercial analyst", "operations or inventory partner", "finance reviewer"],
        major_decisions=[
            "What price or promotional action best fits demand and margin goals?",
            "Which inventory should be pushed, protected, or marked down?",
            "When does local judgment override the standard rule?",
        ],
        major_handoffs=[
            "demand and inventory signals -> commercial team",
            "approved pricing action -> channel or store operators",
            "executed campaign -> finance and performance review",
        ],
        money_lost="Leakage comes from blunt discounts, poor markdown timing, and channel decisions that shift volume without improving contribution.",
        time_lost="Analysts and operators waste time aligning price files, inventory context, and execution timing.",
        human_judgment="Merchants still interpret local demand, competitor behavior, and brand considerations.",
        system_escape="The rationale for overrides often lives in spreadsheets, chats, and field communications.",
        why_unsolved="Optimization helps, but demand signals remain noisy and commercial teams still distrust fully automated rules.",
        primary_reason="Technical",
    ),
    "service_scheduling": profile(
        objective="Match a customer need to the right appointment, technician, or part-supported service slot.",
        trigger="A customer requests service or a follow-up intervention must be scheduled.",
        end_outcome="The appointment or work slot is booked with the right resources and dependencies prepared.",
        primary_actors=["scheduler", "customer", "field or service team", "parts or operations support"],
        major_decisions=[
            "What slot, technician, or resource best fits the request?",
            "Which dependency such as parts or authorization must be secured first?",
            "What issue should be escalated because the standard schedule will fail?",
        ],
        major_handoffs=[
            "customer request -> scheduler",
            "scheduled job -> field or service team",
            "completed service -> billing, support, or account owner",
        ],
        money_lost="Leakage appears through low first-time fix, no-shows, deadhead travel, and rescheduling churn.",
        time_lost="Schedulers spend time on calendar juggling, parts checks, and customer callbacks.",
        human_judgment="Experienced schedulers still know which combinations of customer, asset, and worker will actually succeed.",
        system_escape="Real-world exceptions are coordinated through calls, texts, and side notes outside the scheduler.",
        why_unsolved="The slotting problem is only half the challenge; the other half is local exception management with incomplete visibility.",
        primary_reason="Technical",
    ),
    "order_fulfillment": profile(
        objective="Route and fulfill demand from the right inventory or capacity source with accurate status and exception control.",
        trigger="An order is confirmed and needs allocation, release, shipment, or return handling.",
        end_outcome="The order is fulfilled or closed with any exception documented for downstream billing or service teams.",
        primary_actors=["order management team", "warehouse or operations staff", "customer or channel partner", "transport or service partner"],
        major_decisions=[
            "Which inventory, facility, or path should fulfill the order?",
            "What exception requires split shipment, reroute, substitution, or hold?",
            "When is the order complete enough to invoice or close?",
        ],
        major_handoffs=[
            "order capture -> allocation or warehouse team",
            "warehouse or operations -> transportation or customer",
            "completed order -> billing, returns, or support team",
        ],
        money_lost="Leakage shows up in split orders, mispicks, returns, expedites, and fulfillment promises that outrun actual capacity.",
        time_lost="Teams chase inventory truth, release status, and downstream transport updates across systems.",
        human_judgment="Operators still decide how to recover shortages, prioritize customers, and manage substitutions.",
        system_escape="Exception handling often happens through email, calls, and local trackers outside the formal order flow.",
        why_unsolved="Order orchestration spans inventory, warehouse, transport, and customer systems with different clocks and constraints.",
        primary_reason="Legacy Architecture",
    ),
    "project_delivery": profile(
        objective="Execute a scoped engagement or project while controlling milestones, changes, utilization, and cash realization.",
        trigger="A project, matter, or contracted work package is ready for execution.",
        end_outcome="The deliverable or milestone is completed, status is updated, and commercial closeout can progress.",
        primary_actors=["project manager", "delivery team", "customer or stakeholder", "commercial or finance partner"],
        major_decisions=[
            "What work should be prioritized to protect schedule and margin?",
            "Which scope change requires repricing or approval?",
            "When is the milestone complete enough to bill or accept?",
        ],
        major_handoffs=[
            "sales or planning -> project manager",
            "delivery team -> customer review or acceptance",
            "accepted milestone -> billing and portfolio reporting",
        ],
        money_lost="Leakage comes from scope creep, underutilization, write-offs, and late recognition of delivery risk.",
        time_lost="Project teams spend time aligning resources, updating status manually, and reconciling effort with customer expectations.",
        human_judgment="Project health still depends on leadership judgment around sequencing, risk, and stakeholder management.",
        system_escape="The real state of the project lives in meetings, comments, decks, and side trackers beyond the PSA or project tool.",
        why_unsolved="Project work is inherently exception-heavy and relationship-driven, which prevents full straight-through execution.",
        primary_reason="Organizational",
    ),
    "field_execution": profile(
        objective="Execute work in the field while adapting safely to site conditions, change requests, and incomplete information.",
        trigger="A field team is dispatched or mobilized to perform work at a site, customer, or operating location.",
        end_outcome="The field task is completed, deferred, or escalated with actual conditions captured for downstream use.",
        primary_actors=["field supervisor", "technician or crew", "customer or site contact", "back-office coordinator"],
        major_decisions=[
            "What can actually be completed given current site conditions?",
            "What change requires new approval, scope, or documentation?",
            "What issue should be solved locally versus escalated?",
        ],
        major_handoffs=[
            "dispatch or planning -> field crew",
            "field crew -> back office, customer, or inspector",
            "completed work -> billing, maintenance history, or reporting",
        ],
        money_lost="Travel waste, revisit rates, change-order misses, and field rework are the main economic leaks.",
        time_lost="Crews lose time to waiting, missing parts, unclear scope, and back-and-forth approvals.",
        human_judgment="Field leads interpret site reality, safety, and customer context in ways that no template fully captures.",
        system_escape="Actual field decisions are coordinated over calls, text, and paper notes before systems are updated later.",
        why_unsolved="Field conditions mutate faster than central systems, making local judgment indispensable.",
        primary_reason="Legacy Architecture",
    ),
    "hospitality_ops": profile(
        objective="Turn booked capacity into an on-site service experience while keeping turnover, staffing, and guest needs coordinated.",
        trigger="A guest, room, venue, or event day reaches the active service window.",
        end_outcome="The guest or attendee is served, the operating area is reset, and the financial record is ready for closeout.",
        primary_actors=["front desk or venue operations staff", "housekeeping or service staff", "guest or attendee", "manager"],
        major_decisions=[
            "How should arrivals, room readiness, or guest requests be prioritized?",
            "What issue requires compensation, maintenance, or escalation?",
            "When is the unit or venue area ready for the next use?",
        ],
        major_handoffs=[
            "reservation or ticketing -> on-site operations",
            "operations -> housekeeping, maintenance, or finance",
            "completed stay or event -> settlement and service recovery",
        ],
        money_lost="Leakage comes from unready inventory, labor mismatch, service recovery costs, and poor turnover discipline.",
        time_lost="Teams lose time on room-status reconciliation, guest issue triage, and manual cross-shift communication.",
        human_judgment="On-site teams continually arbitrate service tradeoffs, prioritization, and recovery.",
        system_escape="The true operating picture often lives in shift notes, radios, texts, and verbal coordination.",
        why_unsolved="Hospitality operations mix fixed capacity, live human service, and fast exceptions that spill beyond the PMS.",
        primary_reason="Organizational",
    ),
    "instruction_delivery": profile(
        objective="Deliver scheduled instruction or learning services while keeping attendance, progress, and support needs aligned.",
        trigger="A course, lesson, or instructional block reaches delivery time.",
        end_outcome="Instruction is delivered, participation is recorded, and follow-up actions are visible for students and staff.",
        primary_actors=["instructor", "student", "academic or program coordinator", "support staff"],
        major_decisions=[
            "How should pacing or support be adjusted for current student needs?",
            "What absence, issue, or escalation requires intervention?",
            "What evidence is required to confirm participation or completion?",
        ],
        major_handoffs=[
            "enrollment and scheduling -> instructional staff",
            "instruction -> student support or administration",
            "course outcomes -> billing, reporting, or retention workflows",
        ],
        money_lost="Leakage appears through attrition, underfilled capacity, compliance misses, and avoidable remediation cost.",
        time_lost="Faculty and administrators spend time on attendance tracking, follow-up, and reconciling systems with actual class activity.",
        human_judgment="Instruction quality and intervention timing still depend on educator judgment.",
        system_escape="Critical context lives in conversations, notes, side messages, and informal support channels outside SIS and LMS records.",
        why_unsolved="Learning delivery is partly standardized, but student variance and faculty autonomy keep the workflow human-led.",
        primary_reason="Behavioral",
    ),
    "billing_collections": profile(
        objective="Turn completed work or contractual obligation into clean bills, timely collections, and accurate receivable records.",
        trigger="A billable event, service completion, or recurring obligation reaches the point of invoicing or follow-up.",
        end_outcome="The bill is issued, the receivable is updated, and collection or exception status is clear.",
        primary_actors=["billing specialist", "collections or revenue-cycle staff", "source operations team", "customer or payer"],
        major_decisions=[
            "Is the billable record complete enough to issue or submit?",
            "What denial, dispute, or delinquency path should be pursued next?",
            "When should the item be escalated, adjusted, or written down?",
        ],
        major_handoffs=[
            "source operations -> billing or coding team",
            "billing -> customer, payer, or clearing partner",
            "open item -> collections, finance, or account owner",
        ],
        money_lost="Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points.",
        time_lost="Teams repeatedly reconcile source evidence, payer rules, and customer-specific exceptions.",
        human_judgment="Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item.",
        system_escape="Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system.",
        why_unsolved="Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation.",
        primary_reason="Legacy Architecture",
    ),
    "reconciliation_settlement": profile(
        objective="Close the loop between source activity, cash movement, and the official financial record with defensible reconciliation.",
        trigger="Transactions from multiple sources must be balanced, settled, or closed for a period or event.",
        end_outcome="Balances are reconciled, exceptions are documented, and the official close or settlement state is updated.",
        primary_actors=["accounting or settlement analyst", "operations source owner", "treasury or payments partner", "manager or reviewer"],
        major_decisions=[
            "What is the authoritative source when records disagree?",
            "Which exception can be auto-cleared versus requiring investigation?",
            "What threshold is material enough to escalate before close?",
        ],
        major_handoffs=[
            "source system -> reconciliation or settlement team",
            "unmatched item -> operations, treasury, or counterparty",
            "resolved balance -> reporting and management review",
        ],
        money_lost="Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag.",
        time_lost="Analysts spend time matching records manually, collecting support, and rebuilding audit trails.",
        human_judgment="Materiality, root cause, and acceptable resolution still depend on experienced finance staff.",
        system_escape="Exception triage almost always moves into spreadsheets, email, and bank or partner portals.",
        why_unsolved="Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation.",
        primary_reason="Legacy Architecture",
    ),
    "claims_reimbursement": profile(
        objective="Convert covered service or insured loss into adjudicated reimbursement with accurate reserves, documentation, and follow-through.",
        trigger="A claim, billable care event, or reimbursable program expense is submitted for external payment.",
        end_outcome="The claim is paid, denied, reserved, or escalated with a clear financial and operational status.",
        primary_actors=["claims or revenue-cycle specialist", "payer or insurer", "operations source owner", "supervisor"],
        major_decisions=[
            "Is the submission complete and coded correctly?",
            "What denial, reserve, or escalation path applies?",
            "When should the issue be appealed, corrected, or closed?",
        ],
        major_handoffs=[
            "service or loss record -> claims submission team",
            "claim response -> operations, provider, or adjuster",
            "final outcome -> finance and reporting",
        ],
        money_lost="Leakage comes from denials, undercoding, reserve drift, slow cycle times, and missed recovery opportunities.",
        time_lost="Teams rework submissions, chase evidence, and manage payer or carrier correspondence repeatedly.",
        human_judgment="Experienced staff interpret coverage, coding, severity, and the most effective appeal or settlement path.",
        system_escape="Supporting evidence and negotiation history live in portals, attachments, calls, and external correspondence.",
        why_unsolved="The workflow is document-heavy, regulated, and exception-driven, with too much nuance for complete straight-through adjudication.",
        primary_reason="Regulatory",
    ),
    "lending_credit": profile(
        objective="Advance credit, account, or financing decisions while balancing growth, risk, documentation, and servicing control.",
        trigger="A borrower or account relationship requires onboarding, underwriting, servicing, collections, or payment handling.",
        end_outcome="The credit or servicing action is completed with the record, controls, and next follow-up updated.",
        primary_actors=["relationship manager or lender", "underwriter or analyst", "borrower or account holder", "servicing or collections team"],
        major_decisions=[
            "Is the customer or credit request acceptable under current policy and risk appetite?",
            "What servicing, payment, or workout action is most appropriate now?",
            "What exception deserves manual review despite automation rules?",
        ],
        major_handoffs=[
            "relationship owner -> credit or onboarding review",
            "approved account or loan -> servicing operations",
            "risk signal -> collections, workout, or compliance team",
        ],
        money_lost="Leakage appears through slow decisioning, avoidable losses, poor collections, and high manual servicing cost.",
        time_lost="Banking teams chase documents, reconcile exposures, and move work across front, middle, and back office queues.",
        human_judgment="Risk appetite, borrower quality, and workout strategy still rely heavily on expert human judgment.",
        system_escape="Core context moves into credit memos, committee notes, shared spreadsheets, and email threads outside the core record.",
        why_unsolved="Core systems are mature, but cross-functional credit work remains document-heavy and policy-sensitive.",
        primary_reason="Regulatory",
    ),
    "subscription_billing": profile(
        objective="Translate recurring usage, entitlements, or contracted service into accurate recurring bills and renewal-ready account records.",
        trigger="A subscription period closes, usage accrues, or a contract event changes what should be billed.",
        end_outcome="The account reflects the correct bill, entitlement state, and next renewal or support action.",
        primary_actors=["billing operations team", "customer success or account owner", "finance partner", "customer"],
        major_decisions=[
            "What contract, usage, or entitlement state should drive the bill?",
            "Which exception requires manual correction or customer communication?",
            "What change should flow into renewal or expansion planning?",
        ],
        major_handoffs=[
            "product or usage systems -> billing operations",
            "billing issue -> support or account owner",
            "finalized bill -> finance close and renewal tracking",
        ],
        money_lost="Leakage comes from usage mismatch, wrong entitlements, stale contract data, and manual credits.",
        time_lost="Teams spend time reconciling subscription state across CRM, billing, and service systems.",
        human_judgment="Operators still decide how to resolve exceptions, bundle edge cases, and preserve the relationship during disputes.",
        system_escape="Important contract and exception context lives in tickets, email, and account notes outside the billing platform.",
        why_unsolved="Recurring billing is structurally automatable, but entitlement logic and exception-heavy account transitions remain messy.",
        primary_reason="Legacy Architecture",
    ),
    "reporting_compliance": profile(
        objective="Produce a compliant, decision-useful record of activity while ensuring the supporting evidence can stand up to review.",
        trigger="A formal period close, audit, regulatory filing, or quality checkpoint requires documented output.",
        end_outcome="The report or compliance record is submitted with evidence, exceptions, and ownership clearly documented.",
        primary_actors=["reporting or compliance analyst", "source operations owner", "manager or approver", "external reviewer"],
        major_decisions=[
            "What source should be treated as authoritative for this report?",
            "Which exception is material enough to disclose or remediate?",
            "What evidence is sufficient to sign off the output?",
        ],
        major_handoffs=[
            "source teams -> reporting or compliance owner",
            "prepared output -> reviewer, auditor, or regulator",
            "findings -> remediation owner",
        ],
        money_lost="Late or weak reporting creates fines, reserve exposure, rework, and management blind spots.",
        time_lost="Teams manually stitch files, request attestations, and chase evidence for every cycle.",
        human_judgment="Control owners still decide what is material, what is remediated, and what can be tolerated temporarily.",
        system_escape="Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems.",
        why_unsolved="The form of the report may be standardized, but the data lineage and exception handling still are not.",
        primary_reason="Regulatory",
    ),
    "investor_portfolio": profile(
        objective="Maintain an accurate investment, fund, or investor record across accounting, performance, portfolio, and client-facing views.",
        trigger="A trade, valuation change, investor event, or reporting cycle requires the portfolio record to be refreshed.",
        end_outcome="Positions, valuations, reporting views, and investor outputs align closely enough to support action and oversight.",
        primary_actors=["portfolio or fund operations team", "investment professional", "accounting partner", "investor relations or client service"],
        major_decisions=[
            "What portfolio, fund, or investor state is authoritative for the current action?",
            "Which break, exception, or exposure deserves escalation?",
            "What action should be taken before downstream reporting or client communication proceeds?",
        ],
        major_handoffs=[
            "front-office activity -> middle or back office",
            "accounting and valuation outputs -> investor reporting",
            "exception review -> portfolio manager or leadership",
        ],
        money_lost="Leakage comes from stale positions, NAV breaks, manual reporting overhead, and slow exception closure.",
        time_lost="Teams reconcile books and records repeatedly across portfolio, accounting, and investor-reporting systems.",
        human_judgment="Materiality, valuation challenge, and client communication still depend on experienced professionals.",
        system_escape="Exception narratives and investor context move through emails, memos, and spreadsheet bridges.",
        why_unsolved="Even sophisticated platforms still depend on cross-book reconciliation and human review to maintain trust.",
        primary_reason="Technical",
    ),
    "capital_performance": profile(
        objective="Allocate capital or shared resources and monitor performance with enough fidelity to drive corrective action.",
        trigger="A planning cycle, performance review, or governance checkpoint requires an updated view of resource deployment.",
        end_outcome="Leaders have a current performance view and documented actions for the next operating cycle.",
        primary_actors=["finance or strategy team", "business leader", "shared-service owner", "executive sponsor"],
        major_decisions=[
            "Where should capital or scarce support capacity move next?",
            "What underperformance deserves intervention now?",
            "Which metric should guide the next management action?",
        ],
        major_handoffs=[
            "business-unit data -> central finance or strategy team",
            "management review -> operating owners",
            "approved action -> execution teams and finance tracking",
        ],
        money_lost="Capital and support resources drift into low-return uses when performance signals are late or noisy.",
        time_lost="Review cycles are slowed by manual aggregation and commentary collection.",
        human_judgment="Leadership still decides tradeoffs among long-term return, local politics, and near-term operational reality.",
        system_escape="Most decisive discussion happens in decks and meetings rather than the planning system itself.",
        why_unsolved="Shared-service and capital decisions remain cross-functional and politically negotiated rather than purely model-driven.",
        primary_reason="Organizational",
    ),
    "dispatch_routing": profile(
        objective="Assign the right asset, route, crew, or carrier to the job while balancing service, utilization, and cost.",
        trigger="Demand is ready to be moved or serviced across a network and requires a dispatch decision.",
        end_outcome="The movement or service plan is issued with owners, route, and timing visible to the network.",
        primary_actors=["dispatcher or planner", "carrier, crew, or field operator", "operations control", "customer or receiving party"],
        major_decisions=[
            "Which asset, route, or partner should carry the work?",
            "What tradeoff between service, cost, and utilization is acceptable?",
            "What exception requires re-plan or escalation now?",
        ],
        major_handoffs=[
            "demand intake -> dispatch control",
            "dispatch plan -> driver, crew, or carrier",
            "movement status -> customer service, billing, or recovery desk",
        ],
        money_lost="The biggest leaks are empty capacity, bad routing, detention, and poor network utilization.",
        time_lost="Dispatchers lose time chasing status, making call-based updates, and rerouting around late disruptions.",
        human_judgment="Controllers interpret service priorities and real-world constraints faster than static optimization models.",
        system_escape="Carrier calls, texts, and manual route notes remain central to live execution.",
        why_unsolved="Network state changes in real time and often depends on partner data that is late, partial, or nonstandard.",
        primary_reason="Technical",
    ),
    "network_visibility": profile(
        objective="Maintain a current view of in-flight network health so downstream teams can respond before service failure compounds.",
        trigger="Movement, service, or asset status becomes uncertain, delayed, or exception-prone.",
        end_outcome="The exception is visible, prioritized, and owned with the next corrective action underway.",
        primary_actors=["control tower or exception team", "carrier or field operator", "customer service", "operations manager"],
        major_decisions=[
            "Which exceptions are truly material?",
            "What customer or downstream impact will happen if nothing changes?",
            "Should the response be reroute, recover, reschedule, or communicate?",
        ],
        major_handoffs=[
            "telemetry or event feed -> control tower",
            "exception review -> carrier, field, or customer team",
            "resolution -> billing, claims, or performance review",
        ],
        money_lost="Poor visibility turns small exceptions into claims, missed commitments, and expensive recoveries.",
        time_lost="Teams spend time validating whether the exception signal is real and who is best positioned to act.",
        human_judgment="Exception severity and customer impact still require contextual interpretation.",
        system_escape="Teams fall back to calls, partner portals, and spreadsheets when telemetry is incomplete or late.",
        why_unsolved="Visibility tools have improved, but cross-party event quality and actionability remain inconsistent.",
        primary_reason="Technical",
    ),
    "service_provisioning": profile(
        objective="Translate a sold network or platform service into an activated, billable, and supportable live service state.",
        trigger="A service order or change request is approved and ready for technical fulfillment.",
        end_outcome="The service is provisioned, activated, and synchronized across support and billing records.",
        primary_actors=["provisioning team", "engineering or platform operations", "customer-facing account owner", "billing or assurance staff"],
        major_decisions=[
            "What design or activation path best fits the order and current capacity?",
            "What dependency or exception blocks go-live?",
            "When is the service stable enough to bill and hand to support?",
        ],
        major_handoffs=[
            "commercial order -> technical provisioning",
            "provisioned service -> assurance or support team",
            "activated service -> billing and customer success",
        ],
        money_lost="Delayed activations and bad service-order hygiene push revenue start dates and increase fallout.",
        time_lost="Provisioning teams reconcile commercial orders with technical reality and chase cross-system updates.",
        human_judgment="Engineers and provisioning staff still judge edge-case feasibility and recovery steps.",
        system_escape="Actual root-cause context often lives in tickets, chat threads, and engineering notes outside the order record.",
        why_unsolved="Commercial, technical, and billing systems still do not share one reliable activation truth in many stacks.",
        primary_reason="Legacy Architecture",
    ),
    "planning": profile(
        objective="Set the next operating baseline for capacity, demand, production, or resource use under uncertain conditions.",
        trigger="A planning horizon opens or enough signal changes that the current plan no longer fits reality.",
        end_outcome="A practical baseline plan is published with assumptions and accountable owners documented.",
        primary_actors=["planner", "operations leader", "commercial or finance partner", "downstream execution owner"],
        major_decisions=[
            "What demand and capacity assumptions should the organization trust right now?",
            "Which tradeoff between service, cost, and utilization is acceptable?",
            "When should the baseline be changed rather than managed through exceptions?",
        ],
        major_handoffs=[
            "market or operating signals -> planning team",
            "published plan -> procurement, labor, or execution teams",
            "plan variance -> management review",
        ],
        money_lost="Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting.",
        time_lost="Planning teams spend time rebuilding assumptions and chasing sign-off across functions.",
        human_judgment="Planners still decide which signals to trust and when the model output does not fit local reality.",
        system_escape="Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations.",
        why_unsolved="The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust.",
        primary_reason="Technical",
    ),
    "inventory_allocation": profile(
        objective="Place inventory and assortment into the right location, age bucket, or channel before demand crystallizes.",
        trigger="Inventory, assortment, or aging conditions require an allocation or reallocation decision.",
        end_outcome="Inventory is assigned to the right destination with downstream replenishment and commercial actions aligned.",
        primary_actors=["inventory planner", "merchant or commercial lead", "warehouse or store operations", "finance partner"],
        major_decisions=[
            "Where should inventory sit given expected demand and margin?",
            "What stock should be accelerated, protected, or marked down?",
            "When is reallocation worth the operational disruption?",
        ],
        major_handoffs=[
            "demand and stock signals -> inventory planning",
            "allocation decision -> store, warehouse, or channel team",
            "execution outcome -> pricing and finance review",
        ],
        money_lost="Misallocation drives stockouts, markdowns, carrying cost, and lost working capital productivity.",
        time_lost="Teams spend time reconciling stock truth and coordinating transfers or aged inventory action.",
        human_judgment="Operators still judge local demand and whether aged stock can truly move through the planned channel.",
        system_escape="Inventory decisions are often managed in spreadsheets and store communications outside the planning system.",
        why_unsolved="System optimization struggles when demand is local, seasonal, and only partly observable in real time.",
        primary_reason="Technical",
    ),
    "revenue_management": profile(
        objective="Monetize fixed or perishable capacity by setting prices and controls that balance yield with occupancy or load.",
        trigger="Capacity is approaching sale or use and pricing must respond to demand, mix, and remaining availability.",
        end_outcome="Price, restrictions, and allocation logic are updated and visible to selling channels or operators.",
        primary_actors=["revenue manager", "commercial analyst", "sales or reservations team", "operations manager"],
        major_decisions=[
            "What price and inventory controls maximize expected contribution?",
            "How should channel, segment, or timing tradeoffs be handled?",
            "When should manual overrides replace the model recommendation?",
        ],
        major_handoffs=[
            "demand signals -> revenue management",
            "pricing decision -> selling channels and frontline teams",
            "realized performance -> finance and commercial review",
        ],
        money_lost="Yield is lost through blunt pricing, poor segment control, and late response to demand shifts.",
        time_lost="Teams spend time validating model output and coordinating overrides with selling channels.",
        human_judgment="Managers still incorporate local knowledge, events, and customer behavior that are only partly visible in the data.",
        system_escape="Override rationales and special-event plans often live in spreadsheets and meetings outside the pricing engine.",
        why_unsolved="Optimization is strong, but last-mile trust and local exception handling keep humans in the loop.",
        primary_reason="Technical",
    ),
    "engineering_product": profile(
        objective="Maintain the authoritative product, engineering, or release record so downstream execution runs against the correct definition.",
        trigger="A new product, change request, or release milestone requires controlled updates to the master record.",
        end_outcome="The approved version is published with dependencies and downstream impact clearly communicated.",
        primary_actors=["product or engineering owner", "change or release manager", "operations partner", "commercial or legal reviewer"],
        major_decisions=[
            "Which change set is safe and worth promoting now?",
            "What dependency or downstream effect blocks release?",
            "What version should be treated as authoritative for execution?",
        ],
        major_handoffs=[
            "product or design work -> engineering or release control",
            "approved record -> manufacturing, platform, or commercial teams",
            "released version -> support, billing, or customer-facing teams",
        ],
        money_lost="Master-data mistakes and release delays create rework, scrap, missed launch windows, and downstream confusion.",
        time_lost="Teams manually synchronize definitions across PLM, ERP, support, and commercial systems.",
        human_judgment="Tradeoffs among quality, timing, and downstream disruption remain human-led.",
        system_escape="Critical rationale and version decisions live in reviews, comments, and docs outside the system of record.",
        why_unsolved="Structured data and collaborative work still sit in separate tools, so version truth remains hard to unify.",
        primary_reason="Legacy Architecture",
    ),
    "document_rights": profile(
        objective="Protect the integrity of governed documents, rights, or knowledge while making the right version available to downstream users.",
        trigger="A document, rights position, or knowledge asset changes or is needed for downstream use.",
        end_outcome="The authoritative record is updated and downstream obligations or access rules are aligned.",
        primary_actors=["document or rights owner", "legal or policy reviewer", "operations user", "finance or commercial partner"],
        major_decisions=[
            "What version or rights state is authoritative?",
            "Who can use the asset and under what conditions?",
            "What exception requires legal, billing, or operational review?",
        ],
        major_handoffs=[
            "content or matter owner -> legal or document governance",
            "approved asset -> downstream production, sales, or delivery team",
            "rights or document exception -> finance or compliance review",
        ],
        money_lost="Leakage appears through rights misinterpretation, stale documents, missed obligations, and manual rework.",
        time_lost="Teams search for the right version and reconcile obligations across disconnected repositories.",
        human_judgment="People still interpret contractual nuance, usage rights, and which document version is good enough to act on.",
        system_escape="Key commentary and approval history sit in emails, redlines, and shared folders outside the formal index.",
        why_unsolved="The workflow combines unstructured content and structured obligations, which few systems model together well.",
        primary_reason="Legacy Architecture",
    ),
    "production_execution": profile(
        objective="Run the physical process or line at the required throughput and quality with clear status and escalation control.",
        trigger="A production run, asset cycle, or operating shift is ready to execute.",
        end_outcome="Output is produced, status is recorded, and any exception is handed to the right follow-up owner.",
        primary_actors=["operations supervisor", "machine or process operator", "quality or maintenance staff", "planner"],
        major_decisions=[
            "What run order or operating mode best fits current conditions?",
            "What issue should stop the line versus be worked around?",
            "When is output acceptable enough to release or continue?",
        ],
        major_handoffs=[
            "plan -> line or field operators",
            "execution -> quality or maintenance team",
            "completed output -> logistics, inventory, or finance",
        ],
        money_lost="Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages.",
        time_lost="Operators lose time to waiting, restarts, manual data capture, and coordination across shifts.",
        human_judgment="Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run.",
        system_escape="Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields.",
        why_unsolved="Even with modern MES, the last mile of execution still depends on local conditions and human adaptation.",
        primary_reason="Legacy Architecture",
    ),
    "maintenance_turnaround": profile(
        objective="Restore or preserve asset readiness with the right work orders, parts, sequencing, and outage discipline.",
        trigger="An asset reaches a maintenance threshold, fails, turns over, or must be prepared for the next use.",
        end_outcome="The asset returns to service or readiness with maintenance history and follow-up actions captured.",
        primary_actors=["maintenance planner", "technician", "operations owner", "parts or contractor support"],
        major_decisions=[
            "What work is urgent now versus deferrable?",
            "What outage, turnover, or turnaround scope is required to restore readiness?",
            "What issue should be repaired, monitored, or replaced entirely?",
        ],
        major_handoffs=[
            "operations signal -> maintenance planning",
            "planned work -> technicians or contractors",
            "returned asset -> operations and finance history",
        ],
        money_lost="Leakage comes from downtime, repeat failures, poor work scope, and weak turnover discipline.",
        time_lost="Teams chase parts, permits, technician availability, and asset-history context.",
        human_judgment="Maintenance leaders still assess condition, risk, and repair tradeoffs beyond simple rules.",
        system_escape="Readiness and outage details are frequently tracked in calls, notes, and local sheets outside the CMMS.",
        why_unsolved="Maintenance systems track work orders, but true readiness still depends on fragmented context and field judgment.",
        primary_reason="Legacy Architecture",
    ),
    "quality_compliance": profile(
        objective="Prove that output, operations, or service meet required standards before release or continued execution.",
        trigger="A production step, service checkpoint, or formal control requirement calls for inspection or compliance review.",
        end_outcome="The item is passed, failed, quarantined, or escalated with evidence attached to the record.",
        primary_actors=["quality or compliance owner", "operator or frontline staff", "manager", "external customer or regulator"],
        major_decisions=[
            "Does the item meet the release threshold?",
            "What deviation is acceptable versus requiring stop-work or escalation?",
            "What corrective action and evidence are necessary?",
        ],
        major_handoffs=[
            "operations -> quality or compliance team",
            "quality finding -> rework or management action",
            "released item -> downstream fulfillment or reporting",
        ],
        money_lost="Failures, recalls, rework, and excess inspection labor are the major leakage points.",
        time_lost="Teams repeat data entry, collect evidence manually, and wait on disposition decisions.",
        human_judgment="Inspectors still interpret severity, traceability gaps, and acceptable release decisions.",
        system_escape="Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record.",
        why_unsolved="Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy.",
        primary_reason="Regulatory",
    ),
    "underwriting_policy": profile(
        objective="Apply policy, pricing, and risk selection logic to create or maintain a defendable risk-bearing commitment.",
        trigger="A policy, quote, or underwriting action requires decision, pricing, or downstream administration.",
        end_outcome="The policy or underwriting decision is bound, adjusted, declined, or referred with full traceability.",
        primary_actors=["underwriter", "distribution or account partner", "policy administration staff", "risk or actuarial reviewer"],
        major_decisions=[
            "Should the risk be written, repriced, referred, or declined?",
            "What policy terms or endorsements best fit the exposure?",
            "What exception requires senior review or reinsurance consideration?",
        ],
        major_handoffs=[
            "distribution intake -> underwriting",
            "approved decision -> policy administration or claims context",
            "risk issue -> actuarial, reinsurance, or compliance review",
        ],
        money_lost="Leakage appears through poor risk selection, slow cycle times, mispriced endorsements, and admin rework.",
        time_lost="Teams spend time on document collection, exception referral, and back-and-forth across policy, claims, and rating tools.",
        human_judgment="Risk appetite and exposure interpretation remain highly judgment-driven even with scoring support.",
        system_escape="Key rationale lives in underwriter notes, referrals, broker calls, and exception memos outside the core flow.",
        why_unsolved="Insurance software is mature, but complex cases still require layered human judgment and fragmented evidence.",
        primary_reason="Regulatory",
    ),
    "procurement": profile(
        objective="Secure the right materials or supplies at the right time and cost without destabilizing downstream operations.",
        trigger="Planned or reactive demand requires a purchase, replenishment, or sourcing action.",
        end_outcome="A committed supply action is placed and visible to receiving, planning, and operating teams.",
        primary_actors=["buyer", "planner", "supplier", "operations or inventory owner"],
        major_decisions=[
            "What quantity and timing should be ordered now?",
            "Which source best fits the current cost, quality, and service tradeoff?",
            "What shortage or exception requires escalation?",
        ],
        major_handoffs=[
            "demand plan -> procurement",
            "purchase action -> supplier",
            "confirmed supply -> receiving or execution teams",
        ],
        money_lost="Leakage appears through rush buys, stockouts, overbuying, and weak term control.",
        time_lost="Buyers spend time chasing confirmations, comparing suppliers, and repairing plan mismatches.",
        human_judgment="Source selection and expedites still rely on local knowledge and changing supplier behavior.",
        system_escape="Exception discussions and commitments often move into email and supplier portals beyond the ERP trail.",
        why_unsolved="Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn.",
        primary_reason="Economic",
    ),
    "supplier_management": profile(
        objective="Maintain supplier or subcontractor performance, readiness, and compliance so upstream plans can translate into reliable execution.",
        trigger="A supplier relationship must be scheduled, coordinated, or reviewed against active operating requirements.",
        end_outcome="The external partner is committed, compliant, and visible in the delivery plan.",
        primary_actors=["supplier manager or buyer", "supplier or subcontractor", "operations or project owner", "quality or compliance staff"],
        major_decisions=[
            "Which external partner should be trusted with this scope now?",
            "What compliance or readiness gap must be closed before work starts?",
            "When is a partner issue severe enough to replace or escalate?",
        ],
        major_handoffs=[
            "project or production demand -> supplier manager",
            "supplier commitment -> field, plant, or project team",
            "performance issue -> quality, finance, or leadership review",
        ],
        money_lost="Leakage comes from supplier misses, poor coordination, and weak compliance discipline that forces recovery work.",
        time_lost="Teams spend time on follow-up, document checks, and schedule alignment across organizational boundaries.",
        human_judgment="Partner selection and intervention strategy remain experience-heavy and relationship-driven.",
        system_escape="Actual supplier coordination lives in calls, emails, and shared trackers beyond the formal procurement record.",
        why_unsolved="Structured supplier master data is not the same as reliable day-to-day execution behavior.",
        primary_reason="Organizational",
    ),
    "workforce_scheduling": profile(
        objective="Publish and maintain a near-term labor schedule that covers demand, skills, and compliance constraints.",
        trigger="A shift pattern, service forecast, or operational change requires schedule creation or adjustment.",
        end_outcome="Workers know where to be, managers know coverage, and actual changes can flow into payroll and performance systems.",
        primary_actors=["scheduler", "frontline manager", "worker", "HR or payroll partner"],
        major_decisions=[
            "Who should work which shift or route?",
            "How should shortages, absences, or overtime risk be handled?",
            "When is a local override justified despite the planning rule?",
        ],
        major_handoffs=[
            "forecast -> scheduler",
            "published schedule -> workers and managers",
            "actual changes -> payroll, billing, or service review",
        ],
        money_lost="Overtime, uncovered demand, idle time, and payroll corrections are the core leaks.",
        time_lost="Schedulers constantly rework the plan around callouts, fairness concerns, and compliance rules.",
        human_judgment="Managers know who can actually handle the work and what informal tradeoffs will hold the operation together.",
        system_escape="The live schedule lives in texts, calls, and local shift notes once the day starts moving.",
        why_unsolved="Workforce systems solve the baseline but not the velocity of same-day human exceptions.",
        primary_reason="Behavioral",
    ),
    "staffing_assignment": profile(
        objective="Assign the right person or team to work based on skill, availability, utilization, and current priority.",
        trigger="A new job, matter, project, or shift gap requires labor assignment or reallocation.",
        end_outcome="Work is assigned to accountable people with utilization and downstream operational implications visible.",
        primary_actors=["staffing manager", "team lead", "worker", "project or service owner"],
        major_decisions=[
            "Who is the best fit for this work now?",
            "What tradeoff between utilization, continuity, and skill depth is acceptable?",
            "When should the work be reassigned or escalated?",
        ],
        major_handoffs=[
            "demand owner -> staffing function",
            "assignment decision -> worker and manager",
            "work outcome -> billing, payroll, or performance review",
        ],
        money_lost="Leakage comes from misstaffing, poor utilization, overqualified labor, and late reassignment.",
        time_lost="Managers spend time matching people to work and rebalancing load when priorities shift.",
        human_judgment="People assignment depends on context, trust, and tacit knowledge about who can truly handle the work.",
        system_escape="Assignment rationale is often managed in calls, chats, and local trackers outside the HCM tool.",
        why_unsolved="Skills models help, but actual staffing decisions remain social and context-sensitive.",
        primary_reason="Behavioral",
    ),
}


RESEARCHED_VENDORS: dict[str, list[dict[str, str]]] = {
    "Billing and Subscription Management": [
        {"vendor": "Zuora", "url": "https://www.zuora.com/products/billing/"},
    ],
    "Claims Management": [
        {"vendor": "Guidewire ClaimCenter", "url": "https://www.guidewire.com/products/core-products/insurancesuite/claimcenter-claims-management-software"},
        {"vendor": "Duck Creek Claims", "url": "https://www.duckcreek.com/product/claims-management-software/"},
    ],
    "Cloud Infrastructure and IT Operations": [
        {"vendor": "ServiceNow IT Operations Management", "url": "https://www.servicenow.com/docs/r/it-operations-management/r_ITOMApplications.html"},
    ],
    "Core Banking": [
        {"vendor": "Temenos", "url": "https://www.temenos.com/"},
        {"vendor": "Finastra Phoenix", "url": "https://www.finastra.com/us-mid-market/solutions/phoenix-banking-core"},
    ],
    "CRM": [
        {"vendor": "Salesforce CRM", "url": "https://www.salesforce.com/crm/"},
        {"vendor": "Microsoft Dynamics 365 Sales", "url": "https://www.microsoft.com/en-us/dynamics-365/products/sales"},
        {"vendor": "HubSpot CRM", "url": "https://www.hubspot.com/products/crm?gh_jid=5988617"},
    ],
    "EHR and Care Management": [
        {"vendor": "Epic", "url": "https://www.epic.com/"},
        {"vendor": "Oracle Health EHR", "url": "https://www.oracle.com/health/clinical-suite/electronic-health-record/"},
    ],
    "ERP": [
        {"vendor": "SAP Cloud ERP", "url": "https://www.sap.com/products/erp.html?dfa=1&gad=1"},
        {"vendor": "Acumatica Cloud ERP", "url": "https://www.acumatica.com/cloud-erp-software/"},
    ],
    "Fund Administration and Accounting": [
        {"vendor": "Allvue Fund Accounting", "url": "https://www.allvuesystems.com/solutions/fund-accounting/"},
        {"vendor": "Aladdin Accounting", "url": "https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting"},
    ],
    "HCM / Workforce Management": [
        {"vendor": "Workday Workforce Management", "url": "https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default"},
        {"vendor": "Deputy", "url": "https://www.deputy.com/"},
        {"vendor": "Legion", "url": "https://legion.co/en-gb/products/"},
    ],
    "Investor Reporting and Performance": [
        {"vendor": "Aladdin", "url": "https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software"},
    ],
    "Learning Management System": [
        {"vendor": "Canvas LMS", "url": "https://www.instructure.com/canvas"},
        {"vendor": "D2L Brightspace", "url": "https://www.d2l.com/brightspace/"},
    ],
    "Loan Origination and Servicing": [
        {"vendor": "nCino Commercial Lending", "url": "https://www.ncino.com/solutions/commercial-lending?nxtPslug=commercial-loan-origination-system"},
    ],
    "Maintenance Management": [
        {"vendor": "IFS Enterprise Asset Management", "url": "https://www.ifs.com/en/products/alm/eam"},
    ],
    "Manufacturing Execution System": [
        {"vendor": "Siemens Opcenter", "url": "https://www.siemens.com/en-us/products/opcenter/"},
        {"vendor": "Rockwell FactoryTalk MES", "url": "https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html"},
    ],
    "Order Management System": [
        {"vendor": "Manhattan ActiveOrder", "url": "https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system"},
    ],
    "POS and Payments": [
        {"vendor": "Toast POS", "url": "https://pos.toasttab.com/products/point-of-sale"},
    ],
    "Policy Administration": [
        {"vendor": "Guidewire PolicyCenter", "url": "https://www.guidewire.com/products/core-products/insurancesuite/policycenter-insurance-policy-administration"},
    ],
    "Portfolio and Order Management": [
        {"vendor": "Aladdin", "url": "https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software"},
    ],
    "Professional Services Automation": [
        {"vendor": "Deltek Polaris", "url": "https://www.deltek.com/products/polaris/"},
    ],
    "Project and Construction Management": [
        {"vendor": "Procore", "url": "https://www.procore.com/what-is-procore"},
        {"vendor": "Procore Financial Management", "url": "https://www.procore.com/financial-management"},
    ],
    "Property Management System": [
        {"vendor": "Yardi", "url": "https://www.yardi.com/solution/property-management-software/"},
    ],
    "Reservation and Distribution System": [
        {"vendor": "Mews", "url": "https://www.mews.com/en/hospitality-management-software"},
        {"vendor": "Cloudbeds", "url": "https://www.cloudbeds.com/property-management-system/"},
    ],
    "Revenue Cycle Management": [
        {"vendor": "athenahealth RCM", "url": "https://www.athenahealth.com/solutions/revenue-cycle-management"},
        {"vendor": "R1 RCM", "url": "https://www.r1rcm.com/enterprise-partnerships"},
    ],
    "Student Information System": [
        {"vendor": "Ellucian Student", "url": "https://www.ellucian.com/student"},
    ],
    "Supply Chain Planning": [
        {"vendor": "Blue Yonder Integrated Business Planning", "url": "https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning"},
        {"vendor": "Kinaxis", "url": "https://www.kinaxis.com/en"},
        {"vendor": "o9 Solutions", "url": "https://o9solutions.com/"},
    ],
    "Ticketing and Venue Management": [
        {"vendor": "Tessitura", "url": "https://www.tessitura.com/en/Features/Ticketing-Admissions"},
    ],
    "Transportation Management System": [
        {"vendor": "project44", "url": "https://www.project44.com/platform/tms/"},
    ],
    "Utility Operations and Billing": [
        {"vendor": "Oracle Utilities Customer to Meter", "url": "https://docs.oracle.com/en/industries/energy-water/advanced-meter/index.html"},
    ],
}

GENERIC_SYSTEM_CATEGORIES = {
    "CRM",
    "ERP",
    "HCM / Workforce Management",
    "Service Management",
}


def load_rows() -> list[dict[str, str]]:
    with SOURCE_CSV.open() as handle:
        return list(csv.DictReader(handle))


def pick_theme(workflow_name: str, family: str) -> str | None:
    name = workflow_name.lower()

    if family == "Access, Intake, and Contracting":
        if any(term in name for term in ["admissions", "access", "authorization", "eligibility"]) or "intake and scheduling" in name:
            return "access_admission"
        if any(term in name for term in ["lead ", "lead and", "sales"]) or name == "lead intake and scheduling":
            return "lead_sales"
        if any(term in name for term in ["quotation", "quoting", "estimate", "proposal", "quote-to-bind"]):
            return "quote_estimate"
        if "onboarding" in name or "kyc" in name or "fund onboarding" in name or "account and loan" in name:
            return "onboarding_kyc"
        if "lease acquisition" in name:
            return "lease_acquisition"
        if "reservation" in name or "ticketing and pricing" in name or "load intake and booking" in name:
            return "reservation_ticketing"
        if "donor" in name or "sponsorship" in name:
            return "donor_sponsorship"
    elif family == "Clinical and Case Operations":
        if "medication" in name:
            return "medication_management"
        return "clinical_case"
    elif family == "Customer and Experience Operations":
        if "retention" in name or "renewal" in name or "remarketing" in name:
            return "retention_renewal"
        if "point-of-sale" in name or "pos" in name or "order capture" in name:
            return "point_of_sale"
        if "pricing" in name or "promotion" in name or "markdown" in name or "trade promotion" in name:
            return "promotion_pricing"
        if "scheduling" in name or "parts management" in name:
            return "service_scheduling"
        return "customer_support"
    elif family == "Delivery and Service Execution":
        if "project delivery" in name or "contract milestone" in name:
            return "project_delivery"
        if "field" in name or "dispatch and checkout" in name:
            return "field_execution"
        if "front desk" in name or "housekeeping" in name or "venue and staff" in name:
            return "hospitality_ops"
        if "instruction delivery" in name:
            return "instruction_delivery"
        if any(term in name for term in ["fulfillment", "orchestration", "distribution", "logistics", "harvest", "service execution", "blending"]):
            return "order_fulfillment"
    elif family == "Finance and Revenue Operations":
        if any(term in name for term in ["reconciliation", "settlement", "cash application", "night audit", "cash and inventory"]):
            return "reconciliation_settlement"
        if "claims" in name or "reimbursement" in name:
            return "claims_reimbursement"
        if any(term in name for term in ["credit underwriting", "loss mitigation", "financing", "deposit and payment"]):
            return "lending_credit"
        if any(term in name for term in ["subscription", "license", "usage billing", "billing and renewals"]):
            return "subscription_billing"
        if "royalty" in name or "participation" in name:
            return "document_rights"
        if "reporting" in name and any(term in name for term in ["regulatory", "grant", "owner"]):
            return "reporting_compliance"
        return "billing_collections"
    elif family == "Governance and Portfolio Operations":
        if any(term in name for term in ["fund accounting", "investor reporting", "valuation", "portfolio and order", "asset and investor"]):
            return "investor_portfolio"
        return "capital_performance"
    elif family == "Network and Transportation Operations":
        if any(term in name for term in ["dispatch", "routing", "yard", "carrier", "load planning", "terminal"]):
            return "dispatch_routing"
        if any(term in name for term in ["visibility", "exception", "recovery", "disruption"]):
            return "network_visibility"
        if "provisioning" in name or "activation" in name:
            return "service_provisioning"
        return "dispatch_routing"
    elif family == "Planning and Allocation":
        if "inventory" in name or "assortment" in name or "merchandising" in name:
            return "inventory_allocation"
        if "revenue management" in name:
            return "revenue_management"
        return "planning"
    elif family == "Product, Content, and Engineering":
        if "document" in name or "rights" in name:
            return "document_rights"
        return "engineering_product"
    elif family == "Production and Asset Operations":
        if any(term in name for term in ["maintenance", "turnover", "readiness", "outage"]):
            return "maintenance_turnaround"
        return "production_execution"
    elif family == "Risk, Compliance, and Reporting":
        if "policy administration" in name or "underwriting" in name:
            return "underwriting_policy"
        if any(term in name for term in ["quality", "safety", "certification", "traceability", "labeling", "docketing"]):
            return "quality_compliance"
        return "reporting_compliance"
    elif family == "Sourcing and Supply":
        if "supplier" in name or "subcontractor" in name:
            return "supplier_management"
        return "procurement"
    elif family == "Workforce and Labor Operations":
        if "recruiting" in name or "staffing" in name or "assignment" in name or "task management" in name:
            return "staffing_assignment"
        return "workforce_scheduling"

    return None


def build_profile(workflow_name: str, family: str, operating_systems: list[str], categories: list[str]) -> dict[str, object]:
    merged = dict(FAMILY_DEFAULT_PROFILES[family])
    theme = pick_theme(workflow_name, family)
    if theme and theme in THEME_OVERRIDES:
        merged.update(THEME_OVERRIDES[theme])

    category_set = set(categories)
    if merged["primary_reason"] == "Legacy Architecture" and {
        "Policy Administration",
        "Claims Management",
        "Underwriting and Rating",
        "Core Banking",
        "Loan Origination and Servicing",
        "EHR and Care Management",
        "Revenue Cycle Management",
    } & category_set:
        merged["primary_reason"] = "Regulatory"
    elif merged["primary_reason"] == "Organizational" and {
        "Manufacturing Execution System",
        "Industrial Automation and SCADA",
        "PLM and Engineering Design",
        "Network OSS/BSS",
    } & category_set:
        merged["primary_reason"] = "Legacy Architecture"

    merged["why_unsolved"] = (
        f"{merged['why_unsolved']} "
        f"It typically spans {len(operating_systems)} operating-system context"
        f"{'' if len(operating_systems) == 1 else 's'} and {len(categories)} systems-of-record categories."
    )
    return merged


def join_pipe(values: list[str]) -> str:
    return " | ".join(values)


def join_semicolon(values: list[str]) -> str:
    return "; ".join(values)


def vendor_key(name: str) -> str:
    key = name.lower().strip()
    for suffix in (
        " crm",
        " sales",
        " cloud erp",
        " workforce management",
        " ehr",
        " rcm",
        " lms",
        " student",
        " pos",
    ):
        if key.endswith(suffix):
            key = key[: -len(suffix)]
    return re.sub(r"[^a-z0-9]+", "", key)


def category_sort_key(item: tuple[str, int]) -> tuple[int, int, int, str]:
    category, count = item
    generic_rank = 1 if category in GENERIC_SYSTEM_CATEGORIES else 0
    research_rank = 0 if category in RESEARCHED_VENDORS else 1
    return (generic_rank, research_rank, -count, category)


def rank_sort_key(industry_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(industry_rows, key=lambda row: int(row["rank_2025_gross_output"]))


def vendor_landscape(categories: list[str]) -> tuple[list[str], list[str], list[str]]:
    vendor_names: list[str] = []
    vendor_links: list[str] = []
    coverage_categories: list[str] = []
    seen: set[str] = set()

    for category in categories:
        current_entries = RESEARCHED_VENDORS.get(category, [])
        if current_entries:
            coverage_categories.append(category)
        for entry in current_entries:
            dedupe_key = vendor_key(entry["vendor"])
            if dedupe_key not in seen:
                seen.add(dedupe_key)
                vendor_names.append(entry["vendor"])
                vendor_links.append(f"{entry['vendor']}: {entry['url']}")
        for vendor in SYSTEM_CATEGORY_EXAMPLES.get(category, []):
            dedupe_key = vendor_key(vendor)
            if dedupe_key not in seen:
                seen.add(dedupe_key)
                vendor_names.append(vendor)

    return vendor_names[:8], vendor_links, coverage_categories


def software_landscape_text(categories: list[str], vendor_names: list[str]) -> str:
    category_phrase = ", ".join(categories[:4])
    vendor_phrase = ", ".join(vendor_names[:6]) if vendor_names else "representative category incumbents"
    if not category_phrase:
        return "Phase 1B did not provide systems-of-record categories for this workflow, so software coverage should be treated as incomplete."
    return (
        f"Typical stacks combine {category_phrase}"
        f"{'' if len(categories) <= 4 else ', and adjacent specialist systems'}; "
        f"representative software in market today includes {vendor_phrase}."
    )


def build_workflow_records(
    rows: list[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, list[str]]]:
    workflow_meta: dict[str, dict[str, object]] = {}
    index_rows: list[dict[str, str]] = []
    category_coverage: dict[str, list[str]] = defaultdict(list)

    for row in rank_sort_key(rows):
        industry_categories = [item.strip() for item in row["systems_of_record_categories"].split("|") if item.strip()]
        for i in range(1, 6):
            workflow_name = row[f"canonical_workflow_{i}"]
            workflow_family = row[f"canonical_workflow_family_{i}"]
            if workflow_name not in workflow_meta:
                workflow_meta[workflow_name] = {
                    "workflow_name": workflow_name,
                    "workflow_family": workflow_family,
                    "operating_systems": Counter(),
                    "industry_rows": [],
                    "categories": Counter(),
                }
            record = workflow_meta[workflow_name]
            record["operating_systems"][row["canonical_operating_system"]] += 1
            record["industry_rows"].append(row)
            record["categories"].update(industry_categories)
            index_rows.append(
                {
                    "workflow_name": workflow_name,
                    "workflow_family": workflow_family,
                    "canonical_operating_system": row["canonical_operating_system"],
                    "industry_name": row["industry_name"],
                    "industry_rank_2025_gross_output": row["rank_2025_gross_output"],
                    "systems_of_record_categories": join_pipe(industry_categories),
                }
            )

    library_rows: list[dict[str, str]] = []
    for workflow_name in sorted(workflow_meta):
        record = workflow_meta[workflow_name]
        family = record["workflow_family"]
        operating_systems = [
            os_name
            for os_name, _count in sorted(
                record["operating_systems"].items(),
                key=lambda item: (-item[1], item[0]),
            )
        ]
        industry_rows = record["industry_rows"]
        industries = [row["industry_name"] for row in industry_rows]
        categories = [
            category
            for category, _count in sorted(
                record["categories"].items(),
                key=category_sort_key,
            )
        ]
        vendor_names, vendor_links, coverage_categories = vendor_landscape(categories)
        for category in coverage_categories:
            category_coverage[category] = vendor_links

        anatomy = build_profile(workflow_name, family, operating_systems, categories)
        missing_fields: list[str] = []
        if not operating_systems:
            missing_fields.append("operating_systems")
        if not industries:
            missing_fields.append("industries")
        if not categories:
            missing_fields.append("systems_of_record_categories")

        library_rows.append(
            {
                "workflow_name": workflow_name,
                "workflow_family": family,
                "operating_systems": join_pipe(operating_systems),
                "industries_using_this_workflow": join_pipe(industries),
                "industry_count": str(len(industries)),
                "objective": anatomy["objective"],
                "trigger": anatomy["trigger"],
                "end_outcome": anatomy["end_outcome"],
                "primary_actors": join_semicolon(anatomy["primary_actors"]),
                "major_decisions": join_semicolon(anatomy["major_decisions"]),
                "major_handoffs": join_semicolon(anatomy["major_handoffs"]),
                "systems_of_record_involved": join_pipe(categories),
                "where_money_is_lost": anatomy["money_lost"],
                "where_time_is_lost": anatomy["time_lost"],
                "where_human_judgment_dominates": anatomy["human_judgment"],
                "where_people_leave_the_system_of_record": anatomy["system_escape"],
                "what_software_exists_today": software_landscape_text(categories, vendor_names),
                "why_hasnt_this_been_solved": anatomy["why_unsolved"],
                "primary_reason": anatomy["primary_reason"],
                "representative_vendors": join_semicolon(vendor_names),
                "researched_vendor_links": join_semicolon(vendor_links),
                "validation_status": "Complete" if not missing_fields else "Missing Fields",
                "missing_fields": join_semicolon(missing_fields),
            }
        )

    return library_rows, index_rows, category_coverage


def write_library_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "workflow_name",
        "workflow_family",
        "operating_systems",
        "industries_using_this_workflow",
        "industry_count",
        "objective",
        "trigger",
        "end_outcome",
        "primary_actors",
        "major_decisions",
        "major_handoffs",
        "systems_of_record_involved",
        "where_money_is_lost",
        "where_time_is_lost",
        "where_human_judgment_dominates",
        "where_people_leave_the_system_of_record",
        "what_software_exists_today",
        "why_hasnt_this_been_solved",
        "primary_reason",
        "representative_vendors",
        "researched_vendor_links",
        "validation_status",
        "missing_fields",
    ]
    with LIBRARY_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_index_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "workflow_name",
        "workflow_family",
        "canonical_operating_system",
        "industry_name",
        "industry_rank_2025_gross_output",
        "systems_of_record_categories",
    ]
    with INDEX_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_workflow_docs(rows: list[dict[str, str]]) -> None:
    WORKFLOW_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for row in rows:
        operating_systems = row["operating_systems"].split(" | ")
        industries = row["industries_using_this_workflow"].split(" | ")
        categories = row["systems_of_record_involved"].split(" | ") if row["systems_of_record_involved"] else []
        vendor_links = [item for item in row["researched_vendor_links"].split("; ") if item]
        lines = [
            f"# {row['workflow_name']}",
            "",
            f"Last updated: {GENERATED_DATE}",
            "Status: Active Phase 2 workflow record",
            "",
            "## Metadata",
            "",
            f"- Workflow family: `{row['workflow_family']}`",
            f"- Operating systems: `{row['operating_systems']}`",
            f"- Industries using this workflow: `{row['industries_using_this_workflow']}`",
            f"- Industry count: {row['industry_count']}",
            f"- Systems-of-record categories: `{row['systems_of_record_involved']}`",
            f"- Validation status: `{row['validation_status']}`",
            "",
            "## Current-State Mapping",
            "",
            f"- Objective: {row['objective']}",
            f"- Trigger: {row['trigger']}",
            f"- End outcome: {row['end_outcome']}",
            f"- Primary actors: {row['primary_actors']}",
            f"- Major decisions: {row['major_decisions']}",
            f"- Major handoffs: {row['major_handoffs']}",
            f"- Systems of record involved: {row['systems_of_record_involved']}",
            "",
            "## Current-State Friction",
            "",
            f"- Where money is lost: {row['where_money_is_lost']}",
            f"- Where time is lost: {row['where_time_is_lost']}",
            f"- Where human judgment dominates: {row['where_human_judgment_dominates']}",
            f"- Where people leave the system of record: {row['where_people_leave_the_system_of_record']}",
            "",
            "## Software Landscape",
            "",
            f"- What software exists today: {row['what_software_exists_today']}",
            f"- Representative vendors: {row['representative_vendors']}",
            f"- Why this has not been solved cleanly: {row['why_hasnt_this_been_solved']}",
            f"- Primary reason: `{row['primary_reason']}`",
        ]

        if vendor_links:
            lines.extend(["", "## Current Vendor Research", ""])
            for item in vendor_links:
                vendor, url = item.split(": ", 1)
                lines.append(f"- [{vendor}]({url})")

        if categories:
            lines.extend(["", "## Atlas Context", ""])
            for operating_system in operating_systems:
                definition = OPERATING_SYSTEM_DEFINITIONS.get(operating_system)
                if definition:
                    lines.append(f"- `{operating_system}`: {definition}")

        if row["missing_fields"]:
            lines.extend(
                [
                    "",
                    "## Open Validation Flags",
                    "",
                    f"- Missing fields: {row['missing_fields']}",
                ]
            )

        file_path = WORKFLOW_DOCS_DIR / f"{slugify(row['workflow_name'])}.md"
        file_path.write_text("\n".join(lines) + "\n")


def write_readme(
    library_rows: list[dict[str, str]],
    index_rows: list[dict[str, str]],
) -> None:
    operating_systems = sorted(
        {
            operating_system
            for row in library_rows
            for operating_system in row["operating_systems"].split(" | ")
        }
    )
    families = sorted({row["workflow_family"] for row in library_rows})
    coverage_count = sum(1 for row in library_rows if row["researched_vendor_links"])
    lines = [
        "# Workflow Library",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 2 evidence layer",
        "",
        "## Scope",
        "",
        "- Source workflow universe: `knowledge/research/industry-census/top-50-industry-census-normalized.csv` only.",
        "- Additional software research: official vendor and product pages reviewed to enrich the `What software exists today?` field without changing the workflow universe.",
        "- Current-state mapping only. No opportunity analysis, solution design, or Phase 3 classification appears in this folder.",
        "",
        "## Deliverables",
        "",
        "- `canonical-workflow-library.csv`: one row per canonical workflow with the full Phase 2 anatomy.",
        "- `workflow-operating-system-industry-index.csv`: one row per workflow-to-operating-system-to-industry linkage from Phase 1.",
        "- `workflows/`: one document per canonical workflow.",
        "- `software-research.md`: reusable current vendor-category support artifact.",
        "",
        "## Counts",
        "",
        f"- Canonical workflows documented: {len(library_rows)}",
        f"- Workflow usage index rows: {len(index_rows)}",
        f"- Operating systems represented: {len(operating_systems)}",
        f"- Workflow families represented: {len(families)}",
        f"- Workflow records with additional vendor-research links: {coverage_count}",
        "",
        "## Notes",
        "",
        "- The normalized Phase 1 census remains the source of truth for workflow names, operating systems, and industry mappings.",
        "- The software layer is intentionally representative rather than exhaustive. It exists to keep Phase 2 grounded in the current market landscape without drifting into opportunity analysis.",
    ]
    README_DOC.write_text("\n".join(lines) + "\n")


def write_software_research_doc(category_coverage: dict[str, list[str]]) -> None:
    lines = [
        "# Workflow Software Research",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 2 support artifact",
        "",
        "## Scope",
        "",
        "- Purpose: supplement Phase 1 vendor strings with current category-level vendor research for Phase 2 workflow mapping.",
        "- Source type: official vendor and product pages only.",
        "- This file is not a market-share ranking, opportunity analysis, or vendor recommendation layer.",
        "",
        "## Category Coverage",
        "",
        "| Systems-of-Record Category | Current Vendor Pages Used |",
        "| --- | --- |",
    ]

    for category in sorted(RESEARCHED_VENDORS):
        vendors = [f"[{entry['vendor']}]({entry['url']})" for entry in RESEARCHED_VENDORS[category]]
        lines.append(f"| {escape_md(category)} | {escape_md('; '.join(vendors))} |")

    lines.extend(
        [
            "",
            "## Reuse Rule",
            "",
            "- Use this artifact only to answer `What software exists today?` within the approved Phase 2 workflow charter.",
            "- Do not use it to score gaps, identify startups, or classify opportunities before Phase 3.",
        ]
    )
    SOFTWARE_RESEARCH_DOC.write_text("\n".join(lines) + "\n")


def validate_outputs(library_rows: list[dict[str, str]], index_rows: list[dict[str, str]]) -> None:
    if len(library_rows) != 198:
        raise ValueError(f"Expected 198 canonical workflows, found {len(library_rows)}")
    if len(index_rows) != 250:
        raise ValueError(f"Expected 250 workflow usage rows, found {len(index_rows)}")
    missing_docs = []
    for row in library_rows:
        doc_path = WORKFLOW_DOCS_DIR / f"{slugify(row['workflow_name'])}.md"
        if not doc_path.exists():
            missing_docs.append(doc_path.name)
    if missing_docs:
        raise ValueError(f"Missing workflow docs: {', '.join(missing_docs[:10])}")
    invalid_rows = [row["workflow_name"] for row in library_rows if row["validation_status"] != "Complete"]
    if invalid_rows:
        raise ValueError(f"Validation flags remain on: {', '.join(invalid_rows[:10])}")


def main() -> None:
    WORKFLOW_LIBRARY_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    library_rows, index_rows, category_coverage = build_workflow_records(rows)
    write_library_csv(library_rows)
    write_index_csv(index_rows)
    write_workflow_docs(library_rows)
    write_readme(library_rows, index_rows)
    write_software_research_doc(category_coverage)
    validate_outputs(library_rows, index_rows)
    print("Wrote Phase 2 workflow-library artifacts:")
    print(f"- {LIBRARY_CSV}")
    print(f"- {INDEX_CSV}")
    print(f"- {WORKFLOW_DOCS_DIR}")
    print(f"- {README_DOC}")
    print(f"- {SOFTWARE_RESEARCH_DOC}")


if __name__ == "__main__":
    main()
