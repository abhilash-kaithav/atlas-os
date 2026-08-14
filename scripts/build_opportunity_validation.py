#!/usr/bin/env python3
"""Build Phase 4 opportunity-validation artifacts from the Atlas evidence layers."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = ROOT / "knowledge" / "research"
PHASE1_CSV = RESEARCH_DIR / "industry-census" / "top-50-industry-census-normalized.csv"
PHASE2_CSV = RESEARCH_DIR / "workflow-library" / "canonical-workflow-library.csv"
PHASE3_CLASSIFICATION_CSV = (
    RESEARCH_DIR
    / "structural-failure-atlas"
    / "workflow-structural-failure-classification.csv"
)
PHASE3_FREQUENCY_MATRIX_CSV = (
    RESEARCH_DIR
    / "structural-failure-atlas"
    / "structural-failure-frequency-matrix.csv"
)
PHASE4_DIR = RESEARCH_DIR / "opportunity-validation"
KILL_SHEETS_DIR = PHASE4_DIR / "kill-sheets"

GENERATED_DATE = "2026-08-14"

README_DOC = PHASE4_DIR / "README.md"
EXEC_SUMMARY_DOC = PHASE4_DIR / "executive-summary.md"
VALIDATION_REPORT_DOC = PHASE4_DIR / "opportunity-validation-report.md"
CONSTRAINT_ATLAS_DOC = PHASE4_DIR / "structural-constraint-atlas.md"
INCUMBENT_MATRIX_DOC = PHASE4_DIR / "incumbent-handicap-matrix.md"
FOUNDER_MATRIX_DOC = PHASE4_DIR / "founder-advantage-matrix.md"
TIMING_REPORT_DOC = PHASE4_DIR / "timing-validation-report.md"
FINAL_MATRIX_DOC = PHASE4_DIR / "final-opportunity-matrix.md"
MATRIX_CSV = PHASE4_DIR / "opportunity-validation-matrix.csv"


FAILURE_NAMES = {
    "SF-01": "Exception-Path Breakdown",
    "SF-02": "Cross-System Reconciliation",
    "SF-03": "Decision Context Escapes the Record",
    "SF-04": "Human Judgment Under Incomplete Information",
    "SF-05": "Handoff and Approval Latency",
    "SF-06": "Plan vs. Reality Divergence",
    "SF-07": "Compliance and Evidence Burden",
    "SF-08": "Multi-Party Trust and Dependency Gaps",
}


TIMING_SIGNALS = {
    "ai_tools": {
        "label": "AI capability and workflow tools",
        "date": "retrieved August 14, 2026",
        "url": "https://platform.openai.com/docs/quickstart",
        "summary": (
            "Current OpenAI API docs show the Responses API, file inputs, built-in web "
            "search, file search, and MCP/connectors in the main workflow. That matters "
            "because the surviving theses all depend on parsing unstructured evidence and "
            "acting across tools without custom infrastructure from scratch."
        ),
    },
    "cms_prior_auth": {
        "label": "CMS prior authorization interoperability rule",
        "date": "January 17, 2024",
        "url": "https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f",
        "summary": (
            "CMS finalized payer operational requirements that generally begin January 1, "
            "2026, plus API requirements that generally begin January 1, 2027, including "
            "Provider Access, Payer-to-Payer, and Prior Authorization APIs. That shifts "
            "documentation, evidence, and exception workflows from optional modernization "
            "to dated compliance work."
        ),
    },
    "sec_t1": {
        "label": "SEC T+1 settlement cycle",
        "date": "May 21, 2024",
        "url": "https://www.sec.gov/newsroom/press-releases/2024-62",
        "summary": (
            "The SEC's move to T+1 took effect on May 28, 2024 and added tighter same-day "
            "processing requirements. That compresses reconciliation windows and raises the "
            "value of explainable straight-through exception handling."
        ),
    },
    "bls_costs": {
        "label": "BLS unit labor costs",
        "date": "August 6, 2026",
        "url": "https://www.bls.gov/news.release/prod2.htm",
        "summary": (
            "BLS reported second-quarter 2026 unit labor costs up 1.3% in nonfarm business. "
            "That reinforces the urgency to reduce manual exception handling, evidence chasing, "
            "and rework."
        ),
    },
    "bts_transport": {
        "label": "BTS transportation producer price indexes",
        "date": "June 11, 2026",
        "url": "https://www.bts.gov/newsroom/transportation-producer-price-index-may-2026",
        "summary": (
            "BTS reported May 2026 producer-price increases of 17.3% for truck, 5.7% for "
            "air, and 11.0% for water transportation services versus May 2025. That sharpens "
            "the ROI case for live replanning and exception recovery in network operations."
        ),
    },
    "fda_dscsa": {
        "label": "FDA DSCSA interoperability push",
        "date": "updated April 2026 page with 2023-2024 guidance history",
        "url": "https://www.fda.gov/drugs/drug-supply-chain-security-act-dscsa/drug-supply-chain-security-act-law-and-policies",
        "summary": (
            "FDA's DSCSA policy page shows 2023 final guidance on interoperable tracing plus "
            "2024 follow-on work on enhanced interoperable systems. That is direct evidence "
            "that compliance evidence and package-level lineage are moving from paperwork to "
            "electronic proof chains."
        ),
    },
    "atlas_vendor_layer": {
        "label": "Atlas Phase 2 vendor-stack maturity",
        "date": "Atlas Phase 2, August 14, 2026",
        "url": "../workflow-library/README.md",
        "summary": (
            "The workflow library already documents current cloud stacks across ERP, CRM, "
            "EHR, MES, TMS, fund accounting, service management, and planning categories. "
            "That means new entrants can integrate with existing systems rather than ask "
            "customers to replace their core records first."
        ),
    },
}


FAILURE_EVALUATIONS = {
    "SF-03": {
        "root_or_symptom": "Root cause",
        "economic_meaningfulness": "Very high",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Legacy Architecture",
        "constraint_strength": "High",
        "constraint_note": (
            "Structured systems capture state changes, but decisive narrative context stays "
            "in collaboration channels, attachments, and portals."
        ),
        "phase4_verdict": "Advance as standalone thesis",
        "linked_candidate_id": "OV-01",
        "standalone_comment": (
            "This is Atlas's strongest cross-industry invariant and the best candidate for "
            "a new system layer rather than another point tool."
        ),
    },
    "SF-04": {
        "root_or_symptom": "Symptom-leaning cross-cutting condition",
        "economic_meaningfulness": "Very high",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Technical",
        "constraint_strength": "Medium-High",
        "constraint_note": (
            "Judgment remains human because the underlying context is incomplete, noisy, and "
            "politically negotiated rather than because no dashboard exists."
        ),
        "phase4_verdict": "Reject as standalone thesis",
        "linked_candidate_id": "RJ-01",
        "standalone_comment": (
            "A generic AI judgment copilot is too horizontal and too easy for incumbents to "
            "add as a feature unless it is anchored in proprietary context capture or a "
            "closed-loop workflow system."
        ),
    },
    "SF-01": {
        "root_or_symptom": "Symptom cluster with concentrated economics",
        "economic_meaningfulness": "Very high",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Legacy Architecture",
        "constraint_strength": "Medium-High",
        "constraint_note": (
            "Incumbents automate the happy path but leave fragmented data, policy nuance, and "
            "local recovery work to humans once the flow deviates."
        ),
        "phase4_verdict": "Advance as standalone thesis",
        "linked_candidate_id": "OV-02",
        "standalone_comment": (
            "Exception work is not the deepest root cause, but it is where cash leakage and "
            "service failure are concentrated, which makes it venture-relevant."
        ),
    },
    "SF-06": {
        "root_or_symptom": "Root cause inside dynamic physical operations",
        "economic_meaningfulness": "High",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Legacy Architecture + Technical",
        "constraint_strength": "High",
        "constraint_note": (
            "Plans decay faster than incumbent planning suites can absorb new field conditions, "
            "partner data, and changing local constraints."
        ),
        "phase4_verdict": "Advance as standalone thesis",
        "linked_candidate_id": "OV-04",
        "standalone_comment": (
            "This is the cleanest path to a live control layer above existing planning and "
            "execution software in logistics, field, and industrial operations."
        ),
    },
    "SF-02": {
        "root_or_symptom": "Root cause",
        "economic_meaningfulness": "High",
        "pressure_trend": "Stable to increasing",
        "dominant_constraint": "Legacy Architecture",
        "constraint_strength": "High",
        "constraint_note": (
            "Authoritative truth is distributed across asynchronous systems and counterparties, "
            "so reconciliation remains a manual control layer rather than a solved background task."
        ),
        "phase4_verdict": "Advance as standalone thesis",
        "linked_candidate_id": "OV-03",
        "standalone_comment": (
            "The pressure is less universal than SF-03, but the workflows are economically dense "
            "and timing has improved because reconciliation windows are tightening."
        ),
    },
    "SF-05": {
        "root_or_symptom": "Mostly symptom of coordination design",
        "economic_meaningfulness": "Medium-High",
        "pressure_trend": "Stable",
        "dominant_constraint": "Organizational",
        "constraint_strength": "High",
        "constraint_note": (
            "The hard part is not task automation but changing accountability, approvals, and "
            "cross-functional behavior."
        ),
        "phase4_verdict": "Reject as standalone thesis",
        "linked_candidate_id": "RJ-02",
        "standalone_comment": (
            "The category is crowded with BPM, onboarding, and ticketing software, while the "
            "constraint itself is often political rather than technical."
        ),
    },
    "SF-07": {
        "root_or_symptom": "Root cause in regulated domains",
        "economic_meaningfulness": "High",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Regulatory",
        "constraint_strength": "High",
        "constraint_note": (
            "Reporting forms can be standardized, but evidence lineage, proof collection, and "
            "materiality judgments still cut across people, documents, and external systems."
        ),
        "phase4_verdict": "Advance as standalone thesis",
        "linked_candidate_id": "OV-05",
        "standalone_comment": (
            "This is narrower than SF-03, but the combination of regulatory timing and evidence "
            "collection pain creates a believable entry wedge."
        ),
    },
    "SF-08": {
        "root_or_symptom": "Root cause with adoption-friction ceiling",
        "economic_meaningfulness": "High",
        "pressure_trend": "Increasing",
        "dominant_constraint": "Network Effects + Market Fragmentation",
        "constraint_strength": "Very high",
        "constraint_note": (
            "The workflow fails at enterprise boundaries, but the same boundary also makes first "
            "deployment, data standardization, and network adoption slow."
        ),
        "phase4_verdict": "Reject as first-company thesis",
        "linked_candidate_id": "RJ-03",
        "standalone_comment": (
            "The opportunity may become attractive later, but as an initial wedge it asks a startup "
            "to solve trust, integration, and adoption on both sides of the network at once."
        ),
    },
}


CANDIDATES = [
    {
        "id": "OV-01",
        "name": "Decision-Memory Infrastructure",
        "slug": "ov-01-decision-memory-infrastructure",
        "status": "Survive",
        "classification": "Transformation",
        "conviction_rank": 1,
        "conviction": "Highest",
        "anchored_failure": "SF-03",
        "supporting_failures": ["SF-04", "SF-05", "SF-02"],
        "thesis": (
            "Build a cross-system decision-memory layer that converts calls, emails, attachments, "
            "portal activity, and side notes into structured rationale, obligations, and next-action "
            "context linked back to operational records."
        ),
        "initial_wedge": (
            "Regulated revenue and service workflows where narrative context directly affects cash, "
            "risk, or escalation speed: clinical documentation and claims, professional-services "
            "delivery, and subscription entitlement or release decisions."
        ),
        "constraint_translation": (
            "The deepest problem is not missing data. It is that the decisive reasoning never enters "
            "the system of record in a trustworthy, queryable form."
        ),
        "incumbent_handicap_tags": [
            "Technical debt",
            "Installed base",
            "Switching costs",
            "Organizational inertia",
        ],
        "incumbent_handicap": (
            "ERP, CRM, EHR, and service platforms optimize for structured fields and transactions, "
            "while collaboration suites optimize for conversation. Neither side is architected to own "
            "the full decision chain or write a reliable narrative back into shared workflow state."
        ),
        "founder_advantage": (
            "A startup can combine modern multimodal AI, file inputs, tool use, and workflow-native "
            "writeback to create a trusted context layer without replacing the system of record. The "
            "product advantage is not generic summarization; it is persistent memory tied to actions, "
            "owners, and evidence."
        ),
        "timing_signal_ids": ["ai_tools", "atlas_vendor_layer", "cms_prior_auth"],
        "timing_summary": (
            "This thesis becomes more credible now because modern AI can interpret documents and messages "
            "at operational quality, while regulated workflows increasingly require traceable digital state "
            "instead of informal handoffs."
        ),
        "why_customers_may_not_buy": (
            "Security, privacy, and internal politics may block access to email, messages, and call notes. "
            "Some teams may also view pervasive context capture as surveillance rather than enablement."
        ),
        "why_incumbents_may_win": (
            "Microsoft, Salesforce, ServiceNow, or category leaders could bundle context capture into suites "
            "customers already trust if the startup does not establish superior workflow writeback and domain "
            "specificity quickly."
        ),
        "too_early_or_too_late": (
            "Too early if buyers accept note-taking demos but will not operationalize writeback. Too late if "
            "suite vendors commoditize summarization before a startup owns the system-of-action layer."
        ),
        "critical_assumptions": (
            "Customers will authorize access to the unstructured channels that contain real state, and the "
            "product will measurably improve turn times, denial rates, rework, or accountability."
        ),
        "invalidating_evidence": (
            "Pilots show that teams only want passive summaries, not operational writeback; adoption stalls "
            "because legal or security policy blocks access to decisive context; or incumbents win simply by "
            "adding transcript summarization."
        ),
        "kill_sheet_verdict": "Survives. Best Atlas candidate.",
    },
    {
        "id": "OV-02",
        "name": "Exception-Resolution System of Action",
        "slug": "ov-02-exception-resolution-system-of-action",
        "status": "Survive",
        "classification": "Disruption",
        "conviction_rank": 2,
        "conviction": "High",
        "anchored_failure": "SF-01",
        "supporting_failures": ["SF-03", "SF-02"],
        "thesis": (
            "Build an exception-resolution operating layer that turns fragmented exception queues into "
            "structured work with evidence, ownership, SLAs, and machine-assisted resolution across "
            "revenue and service workflows."
        ),
        "initial_wedge": (
            "Revenue-cycle denials, billing and collections, cash application, fulfillment exceptions, "
            "and freight or service recovery flows where the economic value of each exception is visible."
        ),
        "constraint_translation": (
            "Happy-path automation already exists. The open space is the exception layer where policy nuance, "
            "data quality gaps, and cross-system handoffs create most of the leakage."
        ),
        "incumbent_handicap_tags": [
            "Business-model conflict",
            "Technical debt",
            "Installed base",
            "Services revenue dependence",
        ],
        "incumbent_handicap": (
            "Core vendors benefit from stable transaction processing and often rely on partners or services "
            "teams for exception-heavy work. They are poorly positioned to unify the messy long tail that "
            "cuts across systems, policies, and teams."
        ),
        "founder_advantage": (
            "A startup can treat exceptions as the primary object: capture them, classify them, assemble the "
            "supporting evidence, recommend actions, and escalate humans only where policy or materiality "
            "requires it."
        ),
        "timing_signal_ids": ["ai_tools", "bls_costs", "cms_prior_auth"],
        "timing_summary": (
            "The why-now is rising labor and compliance cost combined with AI's ability to gather evidence, "
            "draft responses, and route work without pretending the exception can be fully dark automated."
        ),
        "why_customers_may_not_buy": (
            "Some organizations will prefer offshore labor or BPO rather than software. Others may fear that "
            "exception logic is too bespoke to justify a new platform."
        ),
        "why_incumbents_may_win": (
            "ERP, RCM, or service vendors can add queue management and AI triage features, while BPO providers "
            "can attach automation to existing operations contracts."
        ),
        "too_early_or_too_late": (
            "Too early if customers still accept labor arbitrage as the default answer. Too late if incumbents "
            "turn exception management into a bundled workflow module before the startup proves outcome gains."
        ),
        "critical_assumptions": (
            "Exception categories are repetitive enough to productize, and buyers care more about faster "
            "resolution and recovered dollars than about preserving today's manual process."
        ),
        "invalidating_evidence": (
            "Exception categories turn out to be too custom for reusable playbooks, buyers continue to choose "
            "services instead of software, or pilot savings fail to beat low-cost labor alternatives."
        ),
        "kill_sheet_verdict": "Survives with a vertical-first entry strategy.",
    },
    {
        "id": "OV-03",
        "name": "Reconciliation Truth Layer",
        "slug": "ov-03-reconciliation-truth-layer",
        "status": "Survive",
        "classification": "Disruption",
        "conviction_rank": 3,
        "conviction": "High",
        "anchored_failure": "SF-02",
        "supporting_failures": ["SF-03", "SF-01"],
        "thesis": (
            "Build a continuous truth layer that matches records, evidence, and version state across distributed "
            "systems and counterparties, then produces explainable, audit-ready resolutions instead of "
            "spreadsheet bridges and month-end fire drills."
        ),
        "initial_wedge": (
            "High-value financial and settlement workflows such as asset and investor reporting, freight audit "
            "and settlement, billing and cash application, and rights or royalty accounting."
        ),
        "constraint_translation": (
            "Truth is fragmented across ledgers, parties, and timing conventions. The winning product is not "
            "another ledger but an explainable resolution layer above many ledgers."
        ),
        "incumbent_handicap_tags": [
            "Technical debt",
            "Installed base",
            "Regulatory exposure",
            "Services revenue dependence",
        ],
        "incumbent_handicap": (
            "Existing financial platforms and close tools are optimized for their own domain models. They still "
            "struggle when identifiers, documents, counterparties, and timing differ across systems."
        ),
        "founder_advantage": (
            "Now a startup can combine modern matching, document understanding, and evidence retrieval to make "
            "reconciliation explainable rather than only rules-based. That makes hard-edge cases productizable "
            "without claiming zero human review."
        ),
        "timing_signal_ids": ["sec_t1", "ai_tools", "atlas_vendor_layer"],
        "timing_summary": (
            "Tighter settlement and reporting windows increase the value of faster, explainable reconciliation, "
            "while current AI and integration maturity make cross-system evidence handling more feasible than it "
            "was five years ago."
        ),
        "why_customers_may_not_buy": (
            "The budget may sit with finance teams that already tolerate close-period heroics, or buyers may be "
            "nervous about inserting a new truth layer into audited processes."
        ),
        "why_incumbents_may_win": (
            "Accounting, fund-administration, or settlement vendors may add similar features inside their installed "
            "base, especially if the startup stays too horizontal."
        ),
        "too_early_or_too_late": (
            "Too early if buyers still treat reconciliation as acceptable back-office overhead. Too late if domain "
            "vendors absorb explainable matching before the startup owns a dense vertical wedge."
        ),
        "critical_assumptions": (
            "Cross-system evidence can be gathered with enough completeness to reduce close time, settlement risk, "
            "or unresolved breaks without creating new audit uncertainty."
        ),
        "invalidating_evidence": (
            "Users refuse automated suggestions for material breaks, domain-specific rules overwhelm reusable product "
            "logic, or incumbents already solve the problem cleanly in the target wedge."
        ),
        "kill_sheet_verdict": "Survives if the company starts in one dense settlement domain.",
    },
    {
        "id": "OV-04",
        "name": "Live Replanning and Recovery Control",
        "slug": "ov-04-live-replanning-and-recovery-control",
        "status": "Survive",
        "classification": "Transformation",
        "conviction_rank": 4,
        "conviction": "High",
        "anchored_failure": "SF-06",
        "supporting_failures": ["SF-04", "SF-08"],
        "thesis": (
            "Build a live control layer between planning systems and frontline execution that continuously "
            "reconciles plan, field conditions, and partner state, then recommends or triggers recovery actions."
        ),
        "initial_wedge": (
            "Transportation disruption and capacity recovery, process-manufacturing throughput control, and other "
            "high-frequency operations where the plan decays within hours, not weeks."
        ),
        "constraint_translation": (
            "Incumbent planning software assumes the world is knowable at planning time. The real gap is the "
            "operational recovery layer once the world moves faster than the baseline."
        ),
        "incumbent_handicap_tags": [
            "Technical debt",
            "Installed base",
            "Channel conflict",
            "Organizational inertia",
        ],
        "incumbent_handicap": (
            "Planning suites are sold as forecast and optimization systems, not as minute-by-minute operational "
            "recovery layers. Their implementations are slow, and their models depend on cleaner inputs than real "
            "operations provide."
        ),
        "founder_advantage": (
            "A startup can start from the messy signal layer: shift notes, telematics, exceptions, partner updates, "
            "and operator reasoning. Natural-language interaction and faster deployment make a live control layer more "
            "usable than another optimization workbench."
        ),
        "timing_signal_ids": ["ai_tools", "bts_transport", "bls_costs", "atlas_vendor_layer"],
        "timing_summary": (
            "This thesis is more credible now because transport and labor costs remain elevated while telemetry, cloud "
            "integration, and AI interpretation of messy operational state are materially better than in 2021."
        ),
        "why_customers_may_not_buy": (
            "Operational leaders may fear false recommendations, integration burden, or another control tower that "
            "looks good in demos but fails under live pressure."
        ),
        "why_incumbents_may_win": (
            "Planning and TMS/MES vendors could add recovery features, and customers may default to existing vendor "
            "roadmaps to avoid creating another layer in critical operations."
        ),
        "too_early_or_too_late": (
            "Too early if frontline systems are still too closed for fast deployment. Too late if incumbents pair "
            "their installed data position with agentic copilots before the startup proves superior live execution."
        ),
        "critical_assumptions": (
            "Buyers will trust a system that recommends recovery actions in real time, and the startup can show clear "
            "savings in capacity utilization, delay reduction, downtime, or yield."
        ),
        "invalidating_evidence": (
            "The signal layer is too noisy to support consistent recommendations, deployments become long SI projects, "
            "or customers insist the planner of record must own every decision."
        ),
        "kill_sheet_verdict": "Survives, but only with a narrow high-frequency wedge first.",
    },
    {
        "id": "OV-05",
        "name": "Compliance Evidence Graph",
        "slug": "ov-05-compliance-evidence-graph",
        "status": "Survive",
        "classification": "Disruption",
        "conviction_rank": 5,
        "conviction": "Medium-High",
        "anchored_failure": "SF-07",
        "supporting_failures": ["SF-03", "SF-04"],
        "thesis": (
            "Build a continuously assembled evidence and lineage graph that collects proof, attestations, exception "
            "rationale, and traceability from operational systems so compliance outputs are generated from living "
            "evidence rather than periodic chase cycles."
        ),
        "initial_wedge": (
            "Manufacturing quality and certification, provider oversight, regulated reporting, and similar domains "
            "where evidence collection is repeated and failure is expensive."
        ),
        "constraint_translation": (
            "The real workload is not filling the form. It is assembling the lineage, proof, and exception narrative "
            "needed to stand behind the form."
        ),
        "incumbent_handicap_tags": [
            "Regulatory exposure",
            "Technical debt",
            "Services revenue dependence",
            "Organizational inertia",
        ],
        "incumbent_handicap": (
            "GRC, quality, and reporting tools often own the checklist or the filing but not the live operational "
            "evidence chain. Much of the painful work is still delegated to manual attestations and spreadsheets."
        ),
        "founder_advantage": (
            "Modern multimodal AI can read attachments, certifications, images, and supporting documents, while a "
            "workflow-native graph can preserve the source trail and human judgment required for auditability."
        ),
        "timing_signal_ids": ["cms_prior_auth", "fda_dscsa", "ai_tools"],
        "timing_summary": (
            "Regulatory systems are becoming more electronic and more interoperable, which raises both the obligation "
            "and the possibility of automating evidence collection without weakening traceability."
        ),
        "why_customers_may_not_buy": (
            "Compliance buyers are conservative and may see new tooling as risky if it touches audited outputs. Some "
            "teams may prefer process labor over new software."
        ),
        "why_incumbents_may_win": (
            "Large GRC, quality, or domain vendors may extend into evidence collection once the startup proves demand, "
            "especially if the product does not build strong domain-specific workflows."
        ),
        "too_early_or_too_late": (
            "Too early if regulators still tolerate low-tech proofwork. Too late if compliance platforms shift into "
            "evidence-graph products before the startup establishes domain trust."
        ),
        "critical_assumptions": (
            "Evidence can be captured at the source with enough trust to reduce audit prep, fines, rework, or manual "
            "coordination burden."
        ),
        "invalidating_evidence": (
            "Customers keep the process manual because auditors distrust generated evidence trails, or compliance pain "
            "proves too episodic to support durable software budgets."
        ),
        "kill_sheet_verdict": "Survives with regulated vertical focus and strong auditability.",
    },
    {
        "id": "RJ-01",
        "name": "Generic Judgment Workbench",
        "slug": "rj-01-generic-judgment-workbench",
        "status": "Reject",
        "classification": "Rejected",
        "conviction_rank": "",
        "conviction": "Rejected",
        "anchored_failure": "SF-04",
        "supporting_failures": ["SF-03"],
        "thesis": (
            "A broad AI copilot for ambiguous decisions across planning, support, maintenance, and service workflows."
        ),
        "initial_wedge": "None retained.",
        "constraint_translation": (
            "Judgment is universal, but without proprietary context capture or a closed-loop action surface it is not "
            "a defensible standalone company."
        ),
        "incumbent_handicap_tags": ["Weak standalone handicap"],
        "incumbent_handicap": (
            "Every incumbent suite can add an AI assistant. The startup has no obvious structural reason incumbents "
            "cannot copy the surface area."
        ),
        "founder_advantage": (
            "AI helps, but AI alone is not enough. The advantage only becomes real when paired with a stronger system "
            "layer such as decision memory or live control."
        ),
        "timing_signal_ids": ["ai_tools"],
        "timing_summary": "Timing exists, but the company boundary is too weak.",
        "why_customers_may_not_buy": "Looks like generic copiloting rather than a system-of-action with measurable ROI.",
        "why_incumbents_may_win": "Incumbents already ship adjacent copilots.",
        "too_early_or_too_late": "Too generic, not too early or too late.",
        "critical_assumptions": "Would require proprietary workflow data or trust advantage that Atlas does not yet see.",
        "invalidating_evidence": "Already rejected.",
        "kill_sheet_verdict": "Rejected. Roll the insight into stronger theses.",
    },
    {
        "id": "RJ-02",
        "name": "Approval and Onboarding Coordination Layer",
        "slug": "rj-02-approval-and-onboarding-coordination-layer",
        "status": "Reject",
        "classification": "Rejected",
        "conviction_rank": "",
        "conviction": "Rejected",
        "anchored_failure": "SF-05",
        "supporting_failures": ["SF-03", "SF-04"],
        "thesis": (
            "A cross-functional platform for approvals, onboarding, and handoff coordination across regulated and "
            "shared-service workflows."
        ),
        "initial_wedge": "None retained.",
        "constraint_translation": (
            "The pain is real, but much of the constraint is political accountability rather than a missing software "
            "primitive."
        ),
        "incumbent_handicap_tags": ["Crowded category", "Weak timing shift"],
        "incumbent_handicap": (
            "BPM, CRM, service management, ticketing, and onboarding software already attack this surface area."
        ),
        "founder_advantage": (
            "The startup does not have a clean founder advantage unless it narrows into a richer exception or "
            "evidence-heavy wedge."
        ),
        "timing_signal_ids": ["ai_tools"],
        "timing_summary": "AI improves user experience, but the structural timing delta is weak.",
        "why_customers_may_not_buy": "They often believe the issue is internal process discipline, not missing software.",
        "why_incumbents_may_win": "Existing workflow suites already sell directly into this budget.",
        "too_early_or_too_late": "Late. The category is crowded and poorly differentiated.",
        "critical_assumptions": "Would require a domain where the handoff object is uniquely valuable.",
        "invalidating_evidence": "Already rejected.",
        "kill_sheet_verdict": "Rejected. Better as a feature inside other products.",
    },
    {
        "id": "RJ-03",
        "name": "Multi-Party Trust Network",
        "slug": "rj-03-multi-party-trust-network",
        "status": "Reject",
        "classification": "Rejected",
        "conviction_rank": "",
        "conviction": "Rejected",
        "anchored_failure": "SF-08",
        "supporting_failures": ["SF-06", "SF-03"],
        "thesis": (
            "A network operating layer for suppliers, carriers, subcontractors, payers, or other external parties "
            "whose data and incentives do not align."
        ),
        "initial_wedge": "None retained as a first company.",
        "constraint_translation": (
            "The external boundary is exactly where the pain lives, but also where adoption friction, standards drift, "
            "and network effects are hardest for a startup."
        ),
        "incumbent_handicap_tags": ["Network effects", "Adoption friction"],
        "incumbent_handicap": (
            "Incumbents are constrained, but that does not automatically mean a startup can win first. It may just "
            "mean the problem requires ecosystem power."
        ),
        "founder_advantage": (
            "A startup could eventually build this from a single-enterprise wedge, but Atlas does not yet see a strong "
            "reason to start here instead of earning one side of the network first."
        ),
        "timing_signal_ids": ["ai_tools", "bts_transport"],
        "timing_summary": "The pain is increasing, but adoption still looks harder than the technology gap.",
        "why_customers_may_not_buy": "One enterprise rarely wants to be first to normalize data and workflow for everyone else.",
        "why_incumbents_may_win": "Existing marketplaces, brokers, platforms, or dominant software suites may still control access.",
        "too_early_or_too_late": "Too early for a first-company wedge; better as a later expansion path.",
        "critical_assumptions": "Would require a single-sided entry point with immediate ROI before network adoption.",
        "invalidating_evidence": "Already rejected for Phase 4 ranking purposes.",
        "kill_sheet_verdict": "Rejected as a first thesis; revisit after a single-enterprise wedge exists.",
    },
]


def parse_pipe_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.split("|") if item.strip()]


def md_link(label: str, target: str) -> str:
    return f"[{label}]({target})"


def timing_signal_link(source_id: str, for_kill_sheet: bool = False) -> str:
    signal = TIMING_SIGNALS[source_id]
    url = signal["url"]
    if for_kill_sheet and url.startswith("../workflow-library/"):
        url = url.replace("../workflow-library/", "../../workflow-library/", 1)
    return md_link(signal["label"], url)


def money_trillions(value_usd_mn: int) -> str:
    return f"${value_usd_mn / 1_000_000:.2f}T"


def format_counter(counter: Counter, limit: int = 5) -> str:
    return "; ".join(f"{name} ({count})" for name, count in counter.most_common(limit))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open() as handle:
        return list(csv.DictReader(handle))


def build_failure_metrics(
    industries: list[dict[str, str]],
    workflows: list[dict[str, str]],
    classifications: list[dict[str, str]],
    frequency_rows: list[dict[str, str]],
) -> tuple[dict[str, dict[str, object]], dict[frozenset[str], int]]:
    industry_by_name = {row["industry_name"]: row for row in industries}
    workflow_by_name = {row["workflow_name"]: row for row in workflows}

    pair_counts: Counter[frozenset[str]] = Counter()
    workflows_with_failure: dict[str, list[dict[str, str]]] = defaultdict(list)
    primary_workflows: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in classifications:
        all_codes = parse_pipe_list(row["all_selected_failure_codes"])
        for code in all_codes:
            workflows_with_failure[code].append(row)
        for idx, code in enumerate(all_codes):
            for other in all_codes[idx + 1 :]:
                pair_counts[frozenset([code, other])] += 1
        primary_workflows[row["primary_structural_failure_code"]].append(row)

    freq_by_failure: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in frequency_rows:
        freq_by_failure[row["failure_code"]].append(row)

    metrics: dict[str, dict[str, object]] = {}
    for code in FAILURE_NAMES:
        workflow_rows = workflows_with_failure[code]
        primary_rows = primary_workflows[code]
        freq_rows = freq_by_failure[code]
        family_counts = Counter(row["workflow_family"] for row in primary_rows)
        os_counts = Counter(row["canonical_operating_system"] for row in freq_rows)
        industry_counts = Counter(row["industry_name"] for row in freq_rows)
        root_cause_counts = Counter(row["dominant_root_cause"] for row in workflow_rows)
        sor_counts: Counter[str] = Counter()
        for row in primary_rows:
            workflow_row = workflow_by_name[row["workflow_name"]]
            for category in parse_pipe_list(workflow_row["systems_of_record_involved"]):
                sor_counts[category] += 1

        unique_industries = sorted(industry_counts)
        gross_output_mn = 0
        value_added_mn = 0
        q1_changes: list[float] = []
        for industry in unique_industries:
            industry_row = industry_by_name[industry]
            gross_output_mn += int(industry_row["gross_output_2025_usd_mn"])
            value_added_mn += int(industry_row["value_added_2025_usd_mn"])
            q1_raw = industry_row["q1_2026_real_go_change_pct_saar"]
            if q1_raw:
                q1_changes.append(float(q1_raw))

        example_rows = sorted(
            primary_rows,
            key=lambda row: (-int(row["industry_count"]), row["workflow_name"]),
        )
        support_pair_counts = {
            other: pair_counts[frozenset([code, other])]
            for other in FAILURE_NAMES
            if other != code
        }
        metrics[code] = {
            "workflow_incidence": len(workflow_rows),
            "primary_workflow_count": len(primary_rows),
            "usage_link_count": len(freq_rows),
            "operating_system_count": len(os_counts),
            "industry_count": len(industry_counts),
            "gross_output_mn": gross_output_mn,
            "value_added_mn": value_added_mn,
            "avg_q1_change_pct": round(mean(q1_changes), 1) if q1_changes else 0.0,
            "top_workflow_families": family_counts,
            "top_operating_systems": os_counts,
            "top_industries": industry_counts,
            "top_root_causes": root_cause_counts,
            "top_systems_of_record": sor_counts,
            "example_rows": example_rows,
            "support_pair_counts": support_pair_counts,
        }

    return metrics, dict(pair_counts)


def candidate_rows(
    metrics_by_failure: dict[str, dict[str, object]]
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for candidate in CANDIDATES:
        metrics = metrics_by_failure[candidate["anchored_failure"]]
        support_counts = metrics["support_pair_counts"]
        support_summary = "; ".join(
            f"{FAILURE_NAMES[code]} ({support_counts.get(code, 0)})"
            for code in candidate["supporting_failures"]
        )
        example_rows: list[dict[str, str]] = metrics["example_rows"]  # type: ignore[assignment]
        example_summary = "; ".join(
            f"{row['workflow_name']} ({row['operating_systems']})"
            for row in example_rows[:3]
        )
        rows.append(
            {
                "candidate_id": candidate["id"],
                "candidate_name": candidate["name"],
                "status": candidate["status"],
                "classification": candidate["classification"],
                "conviction_rank": str(candidate["conviction_rank"]),
                "conviction": candidate["conviction"],
                "anchored_failure_code": candidate["anchored_failure"],
                "anchored_failure_name": FAILURE_NAMES[candidate["anchored_failure"]],
                "supporting_failure_codes": " | ".join(candidate["supporting_failures"]),
                "supporting_failure_names": " | ".join(
                    FAILURE_NAMES[code] for code in candidate["supporting_failures"]
                ),
                "workflow_incidence": str(metrics["workflow_incidence"]),
                "primary_workflow_count": str(metrics["primary_workflow_count"]),
                "usage_link_count": str(metrics["usage_link_count"]),
                "operating_system_count": str(metrics["operating_system_count"]),
                "industry_count": str(metrics["industry_count"]),
                "gross_output_2025_usd_mn": str(metrics["gross_output_mn"]),
                "value_added_2025_usd_mn": str(metrics["value_added_mn"]),
                "avg_q1_2026_real_go_change_pct_saar": str(metrics["avg_q1_change_pct"]),
                "top_workflow_families": format_counter(
                    metrics["top_workflow_families"], 4  # type: ignore[arg-type]
                ),
                "top_operating_systems": format_counter(
                    metrics["top_operating_systems"], 4  # type: ignore[arg-type]
                ),
                "top_systems_of_record": format_counter(
                    metrics["top_systems_of_record"], 4  # type: ignore[arg-type]
                ),
                "supporting_failure_overlap": support_summary,
                "example_workflows": example_summary,
                "thesis": candidate["thesis"],
                "initial_wedge": candidate["initial_wedge"],
                "constraint_translation": candidate["constraint_translation"],
                "incumbent_handicap": candidate["incumbent_handicap"],
                "founder_advantage": candidate["founder_advantage"],
                "timing_summary": candidate["timing_summary"],
                "why_customers_may_not_buy": candidate["why_customers_may_not_buy"],
                "why_incumbents_may_win": candidate["why_incumbents_may_win"],
                "too_early_or_too_late": candidate["too_early_or_too_late"],
                "critical_assumptions": candidate["critical_assumptions"],
                "invalidating_evidence": candidate["invalidating_evidence"],
                "kill_sheet_verdict": candidate["kill_sheet_verdict"],
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_readme(candidate_matrix_rows: list[dict[str, str]]) -> str:
    surviving = [row for row in candidate_matrix_rows if row["status"] == "Survive"]
    rejected = [row for row in candidate_matrix_rows if row["status"] == "Reject"]
    lines = [
        "# Opportunity Validation Framework",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 evidence layer",
        "",
        "## Scope",
        "",
        "- Source inputs: Phase 1 normalized census, Phase 2 workflow library, and Phase 3 Structural Failure Atlas as the primary evidence base.",
        "- Broad new opportunity discovery is intentionally out of scope.",
        "- Targeted current validation is used only for timing-sensitive claims in the timing report.",
        "",
        "## Deliverables",
        "",
        "- `opportunity-validation-report.md`: full Phase 4 validation report and candidate decisions.",
        "- `structural-constraint-atlas.md`: root-cause and persistence view across all eight structural failures.",
        "- `incumbent-handicap-matrix.md`: why incumbents still leave each candidate unsolved.",
        "- `founder-advantage-matrix.md`: why a startup could plausibly win now, and where AI is not enough.",
        "- `timing-validation-report.md`: shared and candidate-specific why-now evidence.",
        "- `kill-sheets/`: one skeptical kill sheet for each surviving opportunity.",
        "- `final-opportunity-matrix.md`: ranked Phase 4 output with Whitespace / Disruption / Transformation labels.",
        "- `executive-summary.md`: concise Phase 4 handoff summary for Phase 5.",
        "- `opportunity-validation-matrix.csv`: structured backing data for all candidates.",
        "- `scripts/build_opportunity_validation.py`: reproducible generator for the Phase 4 artifact set.",
        "",
        "## Outcome",
        "",
        f"- Surviving venture theses: {len(surviving)}",
        f"- Rejected standalone candidates: {len(rejected)}",
        "- Final output is intentionally small and skeptical. Atlas advances only the candidates that survived structural, incumbent, timing, and kill-sheet scrutiny.",
        "",
        "## Surviving Thesis Order",
        "",
    ]
    for row in surviving:
        lines.append(
            f"- `{row['candidate_id']}` {row['candidate_name']}: `{row['classification']}`"
        )
    return "\n".join(lines) + "\n"


def build_executive_summary(
    candidate_matrix_rows: list[dict[str, str]],
    failure_metrics: dict[str, dict[str, object]],
) -> str:
    surviving = sorted(
        (row for row in candidate_matrix_rows if row["status"] == "Survive"),
        key=lambda row: int(row["conviction_rank"]),
    )
    rejected = [row for row in candidate_matrix_rows if row["status"] == "Reject"]
    summary_lines = [
        "# Phase 4 Executive Summary",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Approved Phase 4 summary",
        "",
        "## Headline",
        "",
        "Atlas did not find eight venture-grade companies hiding inside eight structural failures. It found five.",
        "Three categories were rejected as standalone company theses because they are either symptoms (`SF-04`, `SF-05`) or they require too much ecosystem adoption too early (`SF-08`).",
        "",
        "## Highest-Conviction Theses",
        "",
        "| Rank | ID | Venture thesis | Opportunity type | Evidence anchor |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in surviving:
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    row["conviction_rank"],
                    row["candidate_id"],
                    row["candidate_name"],
                    row["classification"],
                    (
                        f"{row['anchored_failure_code']} across {row['workflow_incidence']} workflows, "
                        f"{row['industry_count']} industries, and {money_trillions(int(row['gross_output_2025_usd_mn']))} "
                        "of 2025 gross output surface"
                    ),
                ]
            )
            + " |"
        )
    summary_lines.extend(
        [
            "",
            "## Why The Top Thesis Won",
            "",
            (
                "`OV-01` Decision-Memory Infrastructure is the strongest thesis because it sits on the most "
                "universal structural failure in Atlas, crosses every major operating system, and benefits from "
                "a genuine platform shift in multimodal and tool-using AI. Unlike generic copilots, it can own "
                "the missing system layer between collaboration and the system of record."
            ),
            "",
            "## Rejections Matter",
            "",
            "Atlas explicitly rejected three attractive but weaker ideas:",
        ]
    )
    for row in rejected:
        summary_lines.append(
            f"- `{row['candidate_id']}` {row['candidate_name']}: {row['kill_sheet_verdict']}"
        )
    summary_lines.extend(
        [
            "",
            "## Phase Boundary",
            "",
            "Phase 4 is complete when Phase 5 begins from these five surviving theses only. The next step is not more opportunity discovery; it is choosing which thesis can become the strongest specific company wedge.",
        ]
    )
    return "\n".join(summary_lines) + "\n"


def build_validation_report(
    candidate_matrix_rows: list[dict[str, str]],
    failure_metrics: dict[str, dict[str, object]],
) -> str:
    lines = [
        "# Opportunity Validation Report",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 analytical layer",
        "",
        "## Mission",
        "",
        "Transform the Structural Failure Atlas into a small set of evidence-backed venture opportunities by eliminating weak candidates rather than generating a long list of ideas.",
        "",
        "## Method",
        "",
        "- Primary evidence base: Phase 1 normalized census, Phase 2 workflow library, and Phase 3 structural-failure outputs.",
        "- No broad new opportunity discovery was performed.",
        "- Timing-sensitive claims use a small set of current official sources documented in `timing-validation-report.md`.",
        "",
        "## Step 1 - Structural Failure Validation",
        "",
        "| Code | Failure | Root cause or symptom | Recurrence | Economic meaning | Pressure trend | Phase 4 verdict |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for code in FAILURE_NAMES:
        evaluation = FAILURE_EVALUATIONS[code]
        metrics = failure_metrics[code]
        lines.append(
            "| "
            + " | ".join(
                [
                    code,
                    FAILURE_NAMES[code],
                    evaluation["root_or_symptom"],
                    (
                        f"{metrics['workflow_incidence']} workflows, {metrics['industry_count']} industries, "
                        f"{metrics['operating_system_count']} operating systems"
                    ),
                    evaluation["economic_meaningfulness"],
                    evaluation["pressure_trend"],
                    evaluation["phase4_verdict"],
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Step 2-6 - Candidate Decisions",
            "",
            "| ID | Candidate | Anchored failure | Dominant constraint | Founder advantage now | Kill-sheet verdict | Status |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in candidate_matrix_rows:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        lines.append(
            "| "
            + " | ".join(
                [
                    row["candidate_id"],
                    row["candidate_name"],
                    row["anchored_failure_code"],
                    FAILURE_EVALUATIONS[row["anchored_failure_code"]]["dominant_constraint"],
                    candidate["founder_advantage"][:110].rstrip() + "...",
                    row["kill_sheet_verdict"],
                    row["status"],
                ]
            )
            + " |"
        )

    surviving = sorted(
        (row for row in candidate_matrix_rows if row["status"] == "Survive"),
        key=lambda row: int(row["conviction_rank"]),
    )
    rejected = [row for row in candidate_matrix_rows if row["status"] == "Reject"]

    lines.extend(["", "## Surviving Opportunities", ""])
    for row in surviving:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        lines.extend(
            [
                f"### {row['candidate_id']} {row['candidate_name']}",
                "",
                f"- Classification: `{row['classification']}`",
                f"- Thesis: {candidate['thesis']}",
                (
                    "- Evidence base: "
                    f"{row['workflow_incidence']} workflows, {row['usage_link_count']} usage links, "
                    f"{row['industry_count']} industries, and {money_trillions(int(row['gross_output_2025_usd_mn']))} "
                    "of 2025 gross-output surface from the Atlas corpus."
                ),
                f"- Supporting overlap: {row['supporting_failure_overlap']}",
                f"- Initial wedge: {candidate['initial_wedge']}",
                "",
            ]
        )

    lines.extend(["## Rejected Standalone Candidates", ""])
    for row in rejected:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        lines.extend(
            [
                f"### {row['candidate_id']} {row['candidate_name']}",
                "",
                f"- Why it failed: {candidate['kill_sheet_verdict']}",
                f"- Reasoning: {FAILURE_EVALUATIONS[row['anchored_failure_code']]['standalone_comment']}",
                "",
            ]
        )

    return "\n".join(lines) + "\n"


def build_constraint_atlas(failure_metrics: dict[str, dict[str, object]]) -> str:
    lines = [
        "# Structural Constraint Atlas",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 constraint layer",
        "",
        "## Constraint Register",
        "",
        "| Code | Failure | Root cause or symptom | Dominant constraint | Constraint strength | Market surface | Standalone verdict |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for code in FAILURE_NAMES:
        evaluation = FAILURE_EVALUATIONS[code]
        metrics = failure_metrics[code]
        lines.append(
            "| "
            + " | ".join(
                [
                    code,
                    FAILURE_NAMES[code],
                    evaluation["root_or_symptom"],
                    evaluation["dominant_constraint"],
                    evaluation["constraint_strength"],
                    f"{metrics['industry_count']} industries / {money_trillions(metrics['gross_output_mn'])}",
                    evaluation["phase4_verdict"],
                ]
            )
            + " |"
        )

    lines.append("")
    for code in FAILURE_NAMES:
        evaluation = FAILURE_EVALUATIONS[code]
        metrics = failure_metrics[code]
        top_families = format_counter(
            metrics["top_workflow_families"], 3  # type: ignore[arg-type]
        )
        top_systems = format_counter(
            metrics["top_systems_of_record"], 4  # type: ignore[arg-type]
        )
        lines.extend(
            [
                f"## {code} {FAILURE_NAMES[code]}",
                "",
                f"- Root cause or symptom: {evaluation['root_or_symptom']}",
                f"- Dominant constraint: {evaluation['dominant_constraint']}",
                f"- Constraint strength: {evaluation['constraint_strength']}",
                f"- Why it persists: {evaluation['constraint_note']}",
                (
                    "- Recurrence: "
                    f"{metrics['workflow_incidence']} workflows, {metrics['usage_link_count']} usage links, "
                    f"{metrics['operating_system_count']} operating systems, {metrics['industry_count']} industries."
                ),
                f"- Market surface in Atlas: {money_trillions(metrics['gross_output_mn'])} gross output; {money_trillions(metrics['value_added_mn'])} value added.",
                f"- Top workflow families where it is primary: {top_families}.",
                f"- Typical system categories when it is primary: {top_systems}.",
                f"- Phase 4 verdict: {evaluation['phase4_verdict']}.",
                f"- Commentary: {evaluation['standalone_comment']}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_incumbent_matrix(candidate_matrix_rows: list[dict[str, str]]) -> str:
    lines = [
        "# Incumbent Handicap Matrix",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 matrix",
        "",
        "| ID | Candidate | Handicap types | Why incumbents have not solved it |",
        "| --- | --- | --- | --- |",
    ]
    for row in candidate_matrix_rows:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        lines.append(
            "| "
            + " | ".join(
                [
                    row["candidate_id"],
                    row["candidate_name"],
                    ", ".join(candidate["incumbent_handicap_tags"]),
                    candidate["incumbent_handicap"],
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def build_founder_matrix(candidate_matrix_rows: list[dict[str, str]]) -> str:
    lines = [
        "# Founder Advantage Matrix",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 matrix",
        "",
        "| ID | Candidate | Founder advantage now | Why AI alone is not enough |",
        "| --- | --- | --- | --- |",
    ]
    for row in candidate_matrix_rows:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        ai_caveat = (
            "The moat must come from workflow control, trust, evidence, or deployment model rather than generic model access."
            if row["status"] == "Survive"
            else "The thesis was rejected partly because AI alone does not create a defensible company boundary."
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    row["candidate_id"],
                    row["candidate_name"],
                    candidate["founder_advantage"],
                    ai_caveat,
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def build_timing_report(candidate_matrix_rows: list[dict[str, str]]) -> str:
    lines = [
        "# Timing Validation Report",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 timing layer",
        "",
        "## Shared Why-Now Signals",
        "",
    ]
    for signal_id in [
        "ai_tools",
        "cms_prior_auth",
        "sec_t1",
        "bls_costs",
        "bts_transport",
        "fda_dscsa",
        "atlas_vendor_layer",
    ]:
        signal = TIMING_SIGNALS[signal_id]
        lines.append(f"- {timing_signal_link(signal_id)} ({signal['date']}): {signal['summary']}")

    lines.extend(
        [
            "",
            "## Candidate Timing Decisions",
            "",
            "| ID | Candidate | Why now is different from five years ago | Timing sources |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in candidate_matrix_rows:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        source_list = ", ".join(
            TIMING_SIGNALS[source_id]["label"] for source_id in candidate["timing_signal_ids"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    row["candidate_id"],
                    row["candidate_name"],
                    candidate["timing_summary"],
                    source_list,
                ]
            )
            + " |"
        )

    return "\n".join(lines) + "\n"


def build_final_matrix(candidate_matrix_rows: list[dict[str, str]]) -> str:
    surviving = sorted(
        (row for row in candidate_matrix_rows if row["status"] == "Survive"),
        key=lambda row: int(row["conviction_rank"]),
    )
    lines = [
        "# Final Opportunity Matrix",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 4 output",
        "",
        "| Rank | ID | Opportunity | Opportunity type | Anchored failure | Best initial wedge | Conviction |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in surviving:
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        lines.append(
            "| "
            + " | ".join(
                [
                    row["conviction_rank"],
                    row["candidate_id"],
                    row["candidate_name"],
                    row["classification"],
                    f"{row['anchored_failure_code']} {row['anchored_failure_name']}",
                    candidate["initial_wedge"],
                    row["conviction"],
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- No surviving candidate qualified as pure `Whitespace` because each space already contains serious incumbent software or services.",
            "- `Transformation` appears where a new system layer becomes possible because AI and integration maturity changed the category boundary (`OV-01`, `OV-04`).",
            "- `Disruption` appears where incumbents exist but are structurally misaligned with the real failure surface (`OV-02`, `OV-03`, `OV-05`).",
        ]
    )
    return "\n".join(lines) + "\n"


def build_kill_sheet(
    row: dict[str, str],
    candidate: dict[str, object],
) -> str:
    timing_sources = ", ".join(
        timing_signal_link(source_id, for_kill_sheet=True)
        for source_id in candidate["timing_signal_ids"]  # type: ignore[index]
    )
    return (
        dedent(
            f"""
            # {row["candidate_id"]} Kill Sheet

            Last updated: {GENERATED_DATE}
            Status: Surviving Phase 4 opportunity

            ## Thesis

            {candidate["thesis"]}

            ## Evidence Base

            - Anchored structural failure: `{row["anchored_failure_code"]}` {row["anchored_failure_name"]}
            - Atlas coverage: {row["workflow_incidence"]} workflows, {row["usage_link_count"]} usage links, {row["industry_count"]} industries, {money_trillions(int(row["gross_output_2025_usd_mn"]))} of 2025 gross-output surface
            - Supporting failure overlap: {row["supporting_failure_overlap"]}
            - Example workflows: {row["example_workflows"]}

            ## Why Customers May Not Buy

            {candidate["why_customers_may_not_buy"]}

            ## Why Incumbents May Still Win

            {candidate["why_incumbents_may_win"]}

            ## Why The Market May Be Too Early Or Too Late

            {candidate["too_early_or_too_late"]}

            ## Critical Assumptions

            {candidate["critical_assumptions"]}

            ## Evidence That Would Invalidate The Thesis

            {candidate["invalidating_evidence"]}

            ## Timing Validation

            {candidate["timing_summary"]}

            Sources: {timing_sources}

            ## Verdict

            {candidate["kill_sheet_verdict"]}
            """
        ).strip()
        + "\n"
    )


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    industries = load_csv(PHASE1_CSV)
    workflows = load_csv(PHASE2_CSV)
    classifications = load_csv(PHASE3_CLASSIFICATION_CSV)
    frequency_rows = load_csv(PHASE3_FREQUENCY_MATRIX_CSV)

    failure_metrics, _pair_counts = build_failure_metrics(
        industries, workflows, classifications, frequency_rows
    )
    candidate_matrix_rows = candidate_rows(failure_metrics)

    PHASE4_DIR.mkdir(parents=True, exist_ok=True)
    KILL_SHEETS_DIR.mkdir(parents=True, exist_ok=True)

    write_csv(MATRIX_CSV, candidate_matrix_rows)
    write_text(README_DOC, build_readme(candidate_matrix_rows))
    write_text(
        EXEC_SUMMARY_DOC,
        build_executive_summary(candidate_matrix_rows, failure_metrics),
    )
    write_text(
        VALIDATION_REPORT_DOC,
        build_validation_report(candidate_matrix_rows, failure_metrics),
    )
    write_text(CONSTRAINT_ATLAS_DOC, build_constraint_atlas(failure_metrics))
    write_text(INCUMBENT_MATRIX_DOC, build_incumbent_matrix(candidate_matrix_rows))
    write_text(FOUNDER_MATRIX_DOC, build_founder_matrix(candidate_matrix_rows))
    write_text(TIMING_REPORT_DOC, build_timing_report(candidate_matrix_rows))
    write_text(FINAL_MATRIX_DOC, build_final_matrix(candidate_matrix_rows))

    for row in candidate_matrix_rows:
        if row["status"] != "Survive":
            continue
        candidate = next(item for item in CANDIDATES if item["id"] == row["candidate_id"])
        kill_sheet_path = KILL_SHEETS_DIR / f"{candidate['slug']}.md"
        write_text(kill_sheet_path, build_kill_sheet(row, candidate))


if __name__ == "__main__":
    main()
