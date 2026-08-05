#!/usr/bin/env python3
"""Build the curated Atlas concept inventory and QA report from the raw source."""

from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_PATH = DATA_DIR / "concepts_raw.csv"
CURATED_PATH = DATA_DIR / "concepts_curated.csv"
QA_PATH = DATA_DIR / "concepts_inventory_qa.md"
JOB_TAXONOMY_PATH = DATA_DIR / "job_taxonomy.csv"

UNKNOWN = "Unknown"
GENERATED_DATE = "2026-08-05"

CURATED_COLUMNS = [
    "Concept ID",
    "Concept Title",
    "Clear Description",
    "Track",
    "Batch",
    "Primitive",
    "Canonical Job",
    "Domain",
    "Customer",
    "Value Mechanism",
    "Initial Wedge",
    "Confidence",
    "Evidence",
    "Why Now",
    "Notes",
    "Raw Source ID",
    "Original Wording",
]

# Targeted curation decisions that should survive regeneration.
LEGACY_ROW_OVERRIDES = {
    "C-0064": {
        "Customer": "Educator",
        "Initial Wedge": "Classrooms or course teams managing repeated practice and feedback cycles outside live instruction.",
        "Notes": "Track not recoverable from the raw inventory; marked Unknown. Customer normalized from title or domain cues rather than an explicit raw persona. Why now was not explicit in the raw wording. Evidence level is based on concept framing rather than cited external validation. Confidence reduced because the concept remains broad or lightly specified.",
    },
    "C-0097": {
        "Clear Description": "Certification that an AI agent can safely operate within regulated environments.",
        "Primitive": "Verify",
        "Job": "Verify quality in commercial decisions.",
        "Customer": "Legal operations leader",
        "Value Mechanism": "Produces trustworthy certification and compliance proofs before autonomous agents are allowed into sensitive workflows.",
        "Initial Wedge": "Legal and compliance teams defining approval and certification gates for autonomous agents in regulated environments.",
        "Confidence": "2",
        "Evidence": "Intuition",
        "Why Now": UNKNOWN,
        "Notes": "Track not recoverable from the raw inventory; marked Unknown. Customer normalized from title or domain cues rather than an explicit raw persona. Why now was not explicit in the raw wording. Evidence level is based on concept framing rather than cited external validation. Confidence reduced because the concept remains broad or lightly specified. Likely near-duplicate of C-0190; this row appears to be the thinner or earlier restatement.",
    },
    "C-0190": {
        "Clear Description": "Companies will need certification before autonomous agents can execute sensitive workflows; the equivalent of SOC 2 for AI agents.",
        "Primitive": "Verify",
        "Job": "Verify quality in commercial decisions.",
        "Customer": "Legal operations leader",
        "Value Mechanism": "Produces trustworthy certification and compliance proofs before autonomous agents are allowed into sensitive workflows.",
        "Initial Wedge": "Legal and compliance teams defining approval and certification gates for autonomous agents in regulated environments.",
        "Confidence": "2",
        "Evidence": "Intuition",
        "Why Now": UNKNOWN,
        "Notes": "Track not recoverable from the raw inventory; marked Unknown. Customer normalized from title or domain cues rather than an explicit raw persona. Why now was not explicit in the raw wording. Evidence level is based on concept framing rather than cited external validation. Confidence reduced because the concept remains broad or lightly specified. Near-duplicate of C-0097, but this row preserves the fuller statement of the thesis.",
    },
    "C-0275": {
        "Customer": "Procurement leader",
        "Initial Wedge": "Procurement teams practicing recurring vendor and pricing negotiations without a structured feedback loop.",
        "Notes": "Original customer wording mixed multiple personas, so one primary role was selected. Why now was not explicit in the raw wording.",
    },
    "C-0283": {
        "Clear Description": "AI connects patents, startups, papers, acquisitions, hiring, regulations, and open-source signals to detect patterns before humans do.",
        "Job": "Find opportunities in research programs.",
        "Customer": "R&D leader",
        "Value Mechanism": "Surfaces earlier weak-signal patterns across research, market, and policy signals before teams would spot them manually.",
        "Initial Wedge": "Research and strategy teams scanning patents, papers, startups, and regulatory shifts for early pattern detection.",
        "Notes": "Customer normalized from title or domain cues rather than an explicit raw persona. Why now was not explicit in the raw wording.",
    },
    "C-0291": {
        "Job": "Coordinate venture decisions.",
        "Value Mechanism": "Reduces manual handoffs and keeps multi-step work moving across venture decisions.",
        "Initial Wedge": "Founder-led holding companies coordinating diligence, hiring, finance, and shared services across multiple businesses.",
        "Notes": "Primitive required judgment between nearby controlled taxonomy labels. Why now was not explicit in the raw wording. Confidence reduced because the concept remains broad or lightly specified.",
    },
    "C-0625": {
        "Clear Description": "Governments maintain an always-current map of critical skills that can be mobilized during emergencies.",
        "Primitive": "Match",
        "Job": "Match the right resources in public coordination.",
        "Customer": "Public sector strategist",
        "Value Mechanism": "Connects critical skills and surge capacity faster during public-sector emergency coordination.",
        "Initial Wedge": "Government emergency-preparedness teams mapping critical skills across agencies, contractors, and reserves before crisis response.",
        "Confidence": "2",
        "Evidence": "Intuition",
        "Why Now": UNKNOWN,
        "Notes": "Customer normalized from title or domain cues rather than an explicit raw persona. Primitive required judgment between nearby controlled taxonomy labels. Why now was not explicit in the raw wording. Evidence level is based on concept framing rather than cited external validation. Confidence reduced because the concept remains broad or lightly specified.",
    },
}

ARCHETYPE_RULES = [
    ("Negotiation Agent", ["negotiat", "procurement", "vendor contract", "vendor renewal", "commercial agreement"]),
    ("Trust Trial", ["trust", "credential", "reputation", "verify", "verification", "trial"]),
    ("Learning Loop", ["learning", "coach", "tutor", "companion", "skills", "practice", "feedback"]),
    ("Opportunity Queue", ["opportunity queue", "next best", "priorit", "queue"]),
    ("Compounding Loop", ["compound", "dividend", "flywheel", "loop", "compounding"]),
    ("Memory Layer", ["memory", "knowledge", "archive", "brain", "operating manual", "documentation", "history"]),
    ("Decision Draft", ["decision", "copilot", "board", "auditor", "strategy", "recommend", "roadmap"]),
    ("Simulation Twin", ["simulation", "simulator", "twin", "scenario", "what-if"]),
    ("Measurement Index", ["score", "index", "mri", "measure", "readiness", "health", "benchmark"]),
    ("Prediction Engine", ["predict", "prediction", "forecast", "forecasting", "risk engine", "anticipat"]),
    ("Discovery Engine", ["discover", "discovery", "research", "exploration", "insight", "scientific"]),
    ("Exchange Network", ["marketplace", "exchange", "network", "league"]),
    ("Workflow Orchestration", ["workflow", "operating system", "operating layer", "chief of staff", "navigator", "concierge", "manager", "planner", "coordinator", "coordinates", "orchestr"]),
]

TITLE_ARCHETYPE_OVERRIDES = {
    "decision drafts": "Decision Draft",
    "learning loops": "Learning Loop",
    "trust trials": "Trust Trial",
    "opportunity queue": "Opportunity Queue",
    "decision compounder": "Compounding Loop",
    "cognitive compounder": "Compounding Loop",
    "skill compounder": "Compounding Loop",
    "identity compounder": "Compounding Loop",
    "health compounder": "Compounding Loop",
    "play compounder": "Compounding Loop",
    "meaning compounder": "Compounding Loop",
    "exploration compounder": "Compounding Loop",
    "compound time": "Compounding Loop",
    "community compounding": "Compounding Loop",
    "relationship compounding": "Compounding Loop",
    "social compound interest": "Compounding Loop",
    "discovery compiler": "Discovery Engine",
    "discovery exchange": "Exchange Network",
    "prediction corporations": "Prediction Engine",
}

ARCHETYPE_TO_PRIMITIVE = {
    "Decision Draft": "Optimize",
    "Learning Loop": "Learn",
    "Trust Trial": "Verify",
    "Opportunity Queue": "Optimize",
    "Compounding Loop": "Compound",
    "Discovery Engine": "Discover",
    "Memory Layer": "Remember",
    "Simulation Twin": "Simulate",
    "Measurement Index": "Verify",
    "Prediction Engine": "Predict",
    "Exchange Network": "Match",
    "Workflow Orchestration": "Coordinate",
    "Negotiation Agent": "Optimize",
}

CONTROLLED_PRIMITIVE_ORDER = (
    "Discover",
    "Predict",
    "Verify",
    "Coordinate",
    "Compound",
    "Remember",
    "Adapt",
    "Create",
    "Simulate",
    "Optimize",
    "Match",
    "Learn",
)

CONTROLLED_PRIMITIVE_RULES = [
    ("Predict", ["predict", "prediction", "forecast", "forecasting", "anticipat", "early warning", "probabil", "risk engine"]),
    ("Simulate", ["simulation", "simulator", "twin", "scenario", "what-if"]),
    ("Remember", ["memory", "knowledge", "archive", "brain", "documentation", "history", "context"]),
    ("Learn", ["learn", "coach", "tutor", "feedback", "practice", "training", "onboarding", "curriculum"]),
    ("Match", ["marketplace", "exchange", "network", "match", "pair", "league"]),
    ("Verify", ["verify", "validation", "validate", "credential", "trust", "proof", "quality", "inspect", "audit", "benchmark", "measure", "readiness", "detector", "compliance"]),
    ("Discover", ["discover", "discovery", "research", "exploration", "explore", "breakthrough", "opportunity", "possibility"]),
    ("Adapt", ["adapt", "adaptive", "resilien", "evolv", "dynamic", "reconfig", "respond", "retires obsolete", "promotes emerging"]),
    ("Create", ["creator", "content", "author", "writer", "generator", "composer", "design", "publish", "licensing", "royalties", "builder", "studio"]),
    ("Compound", ["compound", "compounding", "flywheel", "cumulative"]),
    ("Coordinate", ["workflow", "orchestr", "coordinate", "scheduling", "scheduler", "dispatch", "chief of staff", "concierge", "operating system", "operating layer", "handoff", "automation"]),
    ("Optimize", ["optimiz", "decision", "recommend", "priorit", "next best", "negotiat", "pricing", "allocation", "root-cause", "roadmap"]),
]

DIRECT_EVIDENCE_VALUES = {
    "Interview Evidence",
    "Customer Voice",
    "Behavioral Data",
    "Revenue Evidence",
}


@dataclass(frozen=True)
class DomainProfile:
    name: str
    keywords: tuple[str, ...]
    customer: str
    object_label: str
    wedge: str


DOMAIN_PROFILES = [
    DomainProfile(
        "product",
        ("product manager", "roadmap", "jira", "support ticket", "customer call", "product team"),
        "Product manager",
        "roadmap decisions",
        "Mid-market SaaS product teams triaging weekly roadmap tradeoffs across Jira, support, and usage analytics.",
    ),
    DomainProfile(
        "org-ops",
        ("company", "enterprise", "organiz", "executive", "ceo", "board", "operating manual", "decision"),
        "Operations executive",
        "operating decisions",
        "Mid-market leadership teams reconciling decisions across meetings, chat, docs, and dashboards.",
    ),
    DomainProfile(
        "workflow",
        ("workflow", "automation", "sop", "process", "back office", "operations", "chief of staff"),
        "Operations manager",
        "workflow execution",
        "Back-office teams running repetitive approvals, service handoffs, or exception workflows across disconnected tools.",
    ),
    DomainProfile(
        "gtm",
        ("customer", "sales", "revenue", "support", "renewal", "interview", "go-to-market", "account"),
        "Revenue operations leader",
        "account decisions",
        "Customer-facing teams consolidating calls, tickets, and account signals before weekly decisions.",
    ),
    DomainProfile(
        "finance-legal",
        ("finance", "procurement", "vendor", "contract", "legal", "accounting", "wealth", "tax", "audit"),
        "Procurement leader",
        "commercial decisions",
        "Procurement and finance teams handling recurring vendor renewals, contract reviews, or compliance packets.",
    ),
    DomainProfile(
        "talent-learning",
        ("recruit", "talent", "hr", "hiring", "employee", "learning", "school", "student", "teacher"),
        "Learning and development leader",
        "skill development",
        "Teams running onboarding, recruiting, or coaching programs with limited manager bandwidth.",
    ),
    DomainProfile(
        "family-home",
        ("family", "home", "household", "calendar", "travel", "bill", "chore", "parent"),
        "Parent",
        "household coordination",
        "Dual-income households coordinating calendars, school logistics, finances, and home tasks.",
    ),
    DomainProfile(
        "health-care",
        ("health", "patient", "clinic", "medical", "medication", "caregiver", "senior", "aging", "hospital", "nurse", "doctor"),
        "Care coordinator",
        "care coordination",
        "Care teams managing appointments, medications, follow-ups, and family communication across settings.",
    ),
    DomainProfile(
        "ops-infra",
        ("supply chain", "logistics", "warehouse", "quality", "manufacturing", "factory", "rail", "port", "water"),
        "Operations manager",
        "physical operations",
        "Operators managing plants, fleets, or infrastructure with manual exception handling.",
    ),
    DomainProfile(
        "science",
        ("science", "scientific", "research", "lab", "materials", "hypothesis", "patent", "commercialization"),
        "R&D leader",
        "research programs",
        "Applied research teams moving experiments from hypothesis to validation with fragmented evidence trails.",
    ),
    DomainProfile(
        "climate-energy",
        ("climate", "energy", "grid", "urban", "city", "infrastructure", "migration", "resilience"),
        "Infrastructure planner",
        "adaptation planning",
        "Cities, utilities, or asset owners planning capital decisions under climate or grid volatility.",
    ),
    DomainProfile(
        "creator-ip",
        ("creator", "content", "media", "course", "book", "patent", "intellectual property", "ip"),
        "Creator",
        "content production",
        "Creators or expert-led teams turning repeated knowledge work into reusable content or IP.",
    ),
    DomainProfile(
        "founder-investor",
        ("founder", "startup", "venture", "entrepreneur", "investor", "acquisition", "vc"),
        "Founder",
        "venture decisions",
        "Founder-led teams or early-stage investors evaluating repeated opportunities with lean analyst support.",
    ),
    DomainProfile(
        "social-community",
        ("community", "social", "relationship", "belonging", "contribution", "conversation", "network"),
        "Community manager",
        "community participation",
        "Communities where retention depends on repeated contribution, matching, and moderation.",
    ),
    DomainProfile(
        "personal-growth",
        ("cognitive", "memory", "identity", "meaning", "play", "thinking", "reasoning", "opinion", "self", "possibility", "listening", "understand", "future self"),
        "Individual professional",
        "personal development",
        "Self-directed professionals already using journals, notes, or coaching tools without continuity between sessions.",
    ),
    DomainProfile(
        "robotics",
        ("robot", "robotics", "autonomous vehicle", "physical workforce", "microgravity", "manufacturing scheduler"),
        "Automation operations leader",
        "automation deployment",
        "Operations teams deploying physical automation in labor-constrained environments.",
    ),
    DomainProfile(
        "institutions",
        ("institution", "country", "nation", "civilization", "society", "government", "public", "future", "futures", "possibility", "progress"),
        "Public sector strategist",
        "public coordination",
        "Policy and strategy teams working on multi-year public coordination problems.",
    ),
]

JOB_PREFIXES = (
    "Match the right resources in ",
    "Create reusable outputs for ",
    "Preserve context for ",
    "Find opportunities in ",
    "Predict outcomes in ",
    "Verify quality in ",
    "Test scenarios in ",
    "Compound gains in ",
    "Improve ",
    "Coordinate ",
    "Accelerate ",
    "Adapt ",
)

DECISION_CONTEXTS = {
    "roadmap decisions",
    "operating decisions",
    "account decisions",
    "commercial decisions",
    "venture decisions",
}

DEVELOPMENT_CONTEXTS = {
    "skill development",
    "personal development",
}

PLANNING_CONTEXTS = {
    "adaptation planning",
}

CREATION_CONTEXTS = {
    "content production",
}

CANONICAL_JOB_DESCRIPTIONS = {
    "Improve decisions": "Help the customer make better choices, prioritization calls, and tradeoffs.",
    "Improve execution": "Help the customer run ongoing work and coordination more effectively.",
    "Improve capability": "Increase skill, expertise, or personal effectiveness over time.",
    "Improve planning": "Make plans more robust, adaptive, or better informed before action.",
    "Improve creation": "Increase the quality or leverage of created outputs and intellectual assets.",
    "Preserve context": "Capture and recall knowledge, history, rationale, and prior decisions.",
    "Find opportunities": "Surface unmet needs, openings, patterns, or high-upside possibilities.",
    "Accelerate learning": "Help people or systems learn, onboard, or improve faster.",
    "Accelerate execution": "Shorten time-to-progress in coordinated work or multi-step action.",
    "Coordinate work": "Move multi-step work across people, tools, or systems with fewer handoffs.",
    "Match resources": "Connect the right people, assets, opportunities, or support at the right time.",
    "Verify quality": "Establish quality, trust, readiness, or compliance before proceeding.",
    "Predict outcomes": "Forecast likely outcomes early enough for the customer to act.",
    "Test scenarios": "Explore alternatives before committing time, capital, or trust.",
    "Create reusable outputs": "Turn work into repeatable assets, reusable outputs, or durable IP.",
    "Compound capability": "Make learning, self-improvement, or expertise accumulate across cycles.",
    "Compound gains": "Make each cycle increase the value of the next instead of resetting.",
    "Adapt continuously": "Keep plans, systems, or behavior aligned as conditions change.",
}

DOMAIN_DESCRIPTIONS = {
    "Product": "Product planning, roadmap, launch, and product strategy work.",
    "Operations": "Company-level management, planning, and operating decisions.",
    "Workflow": "Repeated business processes, approvals, handoffs, and operational execution.",
    "Commercial": "Revenue, customer, account, procurement, negotiation, and growth activity.",
    "Finance": "Finance, accounting, audit, tax, wealth, and capital allocation workflows.",
    "Legal": "Contracts, compliance, legal reasoning, rights, and legal process work.",
    "Talent": "Recruiting, onboarding, workforce design, and employee capability development.",
    "Education": "Teaching, schooling, structured learning, and formal capability building.",
    "Household": "Family logistics, home management, and household coordination.",
    "Healthcare": "Clinical care, caregiving, patient support, and health management.",
    "Physical Operations": "Manufacturing, logistics, supply chain, field operations, and asset operations.",
    "Research": "Scientific research, experimentation, interviews, and discovery programs.",
    "Infrastructure": "Utilities, resilience, long-horizon assets, and shared technical or civic infrastructure.",
    "Content & IP": "Content creation, publishing, knowledge products, and intellectual property.",
    "Venture": "Startups, acquisitions, venture building, and investment-oriented company creation.",
    "Community": "Community participation, belonging, reputation, and social coordination.",
    "Personal Development": "Individual growth, identity, memory, habits, and personal leverage.",
    "Automation": "Robotics, autonomous fleets, and physical automation deployment.",
    "Public Sector": "Government, grants, policy execution, and public administration.",
    "Institutions": "Society-scale systems, governance models, and long-horizon collective capability.",
}

JOB_CONTEXT_DOMAIN_BASES = {
    "roadmap decisions": {"Product": 6},
    "operating decisions": {"Operations": 6},
    "workflow execution": {"Workflow": 6},
    "account decisions": {"Commercial": 4, "Research": 1, "Venture": 1},
    "commercial decisions": {"Commercial": 3, "Finance": 2, "Legal": 2},
    "skill development": {"Talent": 3, "Education": 2, "Personal Development": 1},
    "personal development": {"Personal Development": 6},
    "household coordination": {"Household": 6},
    "care coordination": {"Healthcare": 6},
    "physical operations": {"Physical Operations": 6},
    "research programs": {"Research": 6},
    "adaptation planning": {"Infrastructure": 6},
    "content production": {"Content & IP": 6},
    "venture decisions": {"Venture": 6},
    "community participation": {"Community": 6},
    "automation deployment": {"Automation": 6},
    "public coordination": {"Institutions": 4, "Public Sector": 2},
}

CUSTOMER_DOMAIN_BASES = {
    "Product manager": {"Product": 4},
    "Product leader": {"Product": 4},
    "Chief of staff": {"Operations": 3},
    "Operations executive": {"Operations": 4},
    "Operations manager": {"Workflow": 2, "Operations": 2, "Physical Operations": 1},
    "User researcher": {"Research": 4},
    "Support leader": {"Commercial": 3},
    "Customer success manager": {"Commercial": 3},
    "Revenue operations leader": {"Commercial": 4},
    "Procurement leader": {"Commercial": 4},
    "Legal operations leader": {"Legal": 4},
    "Finance manager": {"Finance": 4},
    "Recruiter": {"Talent": 4},
    "Learning and development leader": {"Talent": 3, "Education": 1, "Personal Development": 1},
    "Educator": {"Education": 4},
    "Learner": {"Education": 2, "Personal Development": 2},
    "Parent": {"Household": 4},
    "Patient": {"Healthcare": 4},
    "Family caregiver": {"Healthcare": 4},
    "Care coordinator": {"Healthcare": 4},
    "Quality manager": {"Physical Operations": 4},
    "Supply chain manager": {"Physical Operations": 4},
    "Plant manager": {"Physical Operations": 4},
    "Infrastructure operator": {"Physical Operations": 4},
    "Research scientist": {"Research": 4},
    "R&D leader": {"Research": 4},
    "City planner": {"Infrastructure": 4, "Public Sector": 1},
    "Utility planner": {"Infrastructure": 4},
    "Infrastructure planner": {"Infrastructure": 4},
    "Creator": {"Content & IP": 4},
    "Investor": {"Venture": 4, "Finance": 1},
    "Founder": {"Venture": 4},
    "Community manager": {"Community": 4},
    "Individual professional": {"Personal Development": 4},
    "Automation operations leader": {"Automation": 4},
    "Public sector strategist": {"Institutions": 3, "Public Sector": 2},
}

DOMAIN_KEYWORDS = {
    "Product": (
        "product manager",
        "roadmap",
        "jira",
        "product launch",
        "requirements",
        "product studio",
    ),
    "Operations": (
        "operating manual",
        "organizational",
        "organization",
        "executive action",
        "board meeting",
        "company memory",
        "leadership team",
    ),
    "Workflow": (
        "workflow",
        "approval",
        "handoff",
        "back-office",
        "process",
        "service desk",
        "automation studio",
    ),
    "Commercial": (
        "sales",
        "account",
        "client",
        "customer success",
        "lead",
        "pipeline",
        "pricing",
        "procurement",
        "vendor",
        "renewal",
        "negotiation",
        "practice",
        "go-to-market",
    ),
    "Finance": (
        "finance",
        "financial",
        "accounting",
        "tax",
        "audit",
        "wealth",
        "credit",
        "bookkeeping",
        "spend",
        "capital allocation",
    ),
    "Legal": (
        "legal",
        "contract",
        "compliance",
        "lawyer",
        "case",
        "rights",
        "evidence",
        "divorce",
        "obligation",
        "permit",
    ),
    "Talent": (
        "recruit",
        "hiring",
        "talent",
        "employee",
        "onboarding",
        "workforce",
        "human capital",
        "expertise",
        "career pivot",
    ),
    "Education": (
        "student",
        "teacher",
        "school",
        "classroom",
        "course",
        "curriculum",
        "learns",
        "learning companion",
        "lifelong model",
        "retention",
    ),
    "Household": (
        "family",
        "household",
        "home",
        "parent",
        "chore",
        "school logistics",
        "travel",
        "bill",
    ),
    "Healthcare": (
        "health",
        "patient",
        "medical",
        "care",
        "clinic",
        "medication",
        "elder",
        "hospital",
        "therapy",
        "nutrition",
        "longevity",
    ),
    "Physical Operations": (
        "supply chain",
        "logistics",
        "warehouse",
        "factory",
        "plant",
        "manufacturing",
        "maintenance",
        "defect",
        "rail",
        "port",
        "throughput",
        "fleet",
    ),
    "Research": (
        "research",
        "scientific",
        "scientist",
        "experiment",
        "hypothesis",
        "discovery",
        "lab",
        "customer interview",
        "user research",
        "feedback",
        "patent",
    ),
    "Infrastructure": (
        "infrastructure",
        "utility",
        "grid",
        "climate",
        "resilience",
        "property",
        "city",
        "water",
        "telecom",
        "transportation",
        "critical infrastructure",
        "dependency",
        "planetary",
        "orbit",
        "moon",
    ),
    "Content & IP": (
        "creator",
        "content",
        "publish",
        "podcast",
        "subscriber",
        "intellectual property",
        "licens",
        "whiteboard",
        "media",
    ),
    "Venture": (
        "venture",
        "startup",
        "founder",
        "investor",
        "acquisition",
        "private equity",
        "hedge fund",
        "vc",
        "thesis",
        "deal",
    ),
    "Community": (
        "community",
        "belonging",
        "volunteer",
        "neighborhood",
        "social",
        "moderation",
        "collective",
    ),
    "Personal Development": (
        "identity",
        "future self",
        "journal",
        "memory",
        "meaning",
        "curiosity",
        "play",
        "self-directed",
        "personal leverage",
        "future regret",
    ),
    "Automation": (
        "robot",
        "robotics",
        "autonomous machine",
        "physical workforce",
        "microgravity",
        "embodied",
    ),
    "Public Sector": (
        "government",
        "grant",
        "policy",
        "policymaker",
        "public comment",
        "public administration",
        "city permit",
    ),
    "Institutions": (
        "institution",
        "civilization",
        "society",
        "nation",
        "humanity",
        "gdp",
        "progress",
        "valuable futures",
        "future readiness",
    ),
}


def clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"`+", "", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"^\s*>\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_label(text: str) -> str:
    cleaned = clean_markdown(text).lower().strip(" :-")
    cleaned = re.sub(r"[^a-z0-9 ]+", "", cleaned)
    return cleaned


def clean_title(title: str) -> str:
    title = clean_markdown(title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def clean_line(line: str) -> str:
    line = clean_markdown(line)
    line = re.sub(r"^\d+\.\s+", "", line)
    line = re.sub(r"^[-*]\s+", "", line)
    line = line.strip(" -")
    return line.strip()


def parse_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    alias_map = {
        "customer": "customer",
        "problem": "problem",
        "product": "product",
        "current behavior": "current_behavior",
        "new behavior": "new_behavior",
        "core value": "core_value",
        "dna": "dna",
        "combines": "combines",
    }

    for raw_line in text.replace("\r\n", "\n").split("\n"):
        line = raw_line.strip()
        if not line:
            continue
        normalized = normalize_label(line)
        if normalized in alias_map:
            current = alias_map[normalized]
            sections.setdefault(current, [])
            continue
        if normalized in {"top 3", "my favorite", "this is my favorite", "the top 3"}:
            current = None
            continue
        if line.strip("- ") == "":
            current = None
            continue
        if current:
            cleaned = clean_line(line)
            if cleaned:
                sections[current].append(cleaned)
    return sections


def extract_why_now(text: str) -> str:
    match = re.search(r"Why Now:\s*(.+)", text, flags=re.IGNORECASE)
    if match:
        return clean_line(match.group(1))
    collision = re.search(r"Collision:\s*(.+)", text, flags=re.IGNORECASE)
    if collision:
        return clean_line(collision.group(1))
    return UNKNOWN


def is_meta_line(line: str, title: str) -> bool:
    cleaned = clean_line(line)
    normalized = normalize_label(cleaned)
    title_norm = normalize_label(title)
    if not cleaned:
        return True
    if normalized == title_norm:
        return True
    if normalized in {
        "customer",
        "problem",
        "product",
        "current behavior",
        "new behavior",
        "core value",
        "top 3",
        "dna",
        "combines",
    }:
        return True
    if cleaned.lower().startswith(("why now:", "initial rating:", "my favorite", "this is my favorite", "favorite of", "not startup ideas")):
        return cleaned.lower().startswith(("why now:", "initial rating:", "my favorite", "this is my favorite", "favorite of"))
    if re.match(r"^\d+\.\s+", cleaned):
        return True
    return False


def trim_sentence(text: str, limit: int = 220) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    sentence_end = text.rfind(".", 0, limit)
    if sentence_end >= 80:
        return text[: sentence_end + 1]
    return text[: limit - 3].rstrip() + "..."


def extract_description(title: str, wording: str, sections: dict[str, list[str]]) -> tuple[str, bool]:
    for prefix in ("One-Line Pitch:", "Core value:"):
        match = re.search(re.escape(prefix) + r"\s*(.+)", wording, flags=re.IGNORECASE)
        if match:
            description = trim_sentence(clean_line(match.group(1)))
            return ensure_period(description), False

    if sections.get("product"):
        description = trim_sentence(" ".join(sections["product"][:3]))
        return ensure_period(description), False

    if sections.get("core_value"):
        description = trim_sentence(" ".join(sections["core_value"][:3]))
        return ensure_period(description), False

    lines: list[str] = []
    for raw_line in wording.replace("\r\n", "\n").split("\n"):
        if is_meta_line(raw_line, title):
            continue
        cleaned = clean_line(raw_line)
        if cleaned:
            lines.append(cleaned)
        if len(" ".join(lines)) >= 220 or len(lines) >= 3:
            break

    if lines:
        description = trim_sentence(" ".join(lines))
        return ensure_period(description), False

    fallback = f"Concept centered on {title.lower()}."
    return ensure_period(fallback), True


def ensure_period(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text.endswith(":"):
        text = text[:-1].rstrip()
    if text[-1] not in ".!?":
        return text + "."
    return text


PROFILE_SUBSTRING_KEYWORDS = {
    "organiz",
    "resilience",
}


def profile_keyword_match(keyword: str, haystack: str) -> bool:
    if keyword in PROFILE_SUBSTRING_KEYWORDS:
        return keyword in haystack
    if " " in keyword:
        return keyword in haystack
    return re.search(rf"\b{re.escape(keyword)}\b", haystack) is not None


def infer_profile(title: str, description: str, wording: str, track: str) -> DomainProfile:
    haystack = f"{title} {description} {wording}".lower()
    if track == "Behavior":
        best = next(profile for profile in DOMAIN_PROFILES if profile.name == "personal-growth")
    elif track == "Fusion":
        best = next(profile for profile in DOMAIN_PROFILES if profile.name == "institutions")
    else:
        best = next(profile for profile in DOMAIN_PROFILES if profile.name == "org-ops")
    best_score = 0
    for profile in DOMAIN_PROFILES:
        score = sum(1 for keyword in profile.keywords if profile_keyword_match(keyword, haystack))
        if score > best_score:
            best = profile
            best_score = score
    return best


def extract_customer_from_title(title: str) -> str | None:
    match = re.search(r"\bfor ([A-Za-z0-9/& -]{3,60})$", title)
    if match:
        customer = clean_line(match.group(1))
        if customer:
            return customer
    return None


def normalize_explicit_customer(customer: str) -> tuple[str | None, bool]:
    candidate = clean_line(customer).rstrip(".")
    lower = candidate.lower()
    if not candidate:
        return None, False
    if any(separator in lower for separator in (",", " and ", "/", ";")):
        return None, True

    rules = [
        (r"product manager", "Product manager"),
        (r"product leader|head of product|vp product", "Product leader"),
        (r"chief of staff", "Chief of staff"),
        (r"executive|ceo|founder mode", "Operations executive"),
        (r"operations", "Operations manager"),
        (r"customer success", "Customer success manager"),
        (r"support", "Support leader"),
        (r"user research|researcher", "User researcher"),
        (r"sales|revenue", "Revenue operations leader"),
        (r"procurement|vendor", "Procurement leader"),
        (r"legal|compliance|law firm", "Legal operations leader"),
        (r"finance|accounting|wealth|tax", "Finance manager"),
        (r"recruit", "Recruiter"),
        (r"teacher|educator|professor", "Educator"),
        (r"student|learner", "Learner"),
        (r"learning|training|onboarding|coach", "Learning and development leader"),
        (r"parent|family|household", "Parent"),
        (r"patient", "Patient"),
        (r"caregiver", "Family caregiver"),
        (r"care|clinic|medical|hospital|nurse|doctor", "Care coordinator"),
        (r"quality", "Quality manager"),
        (r"supply chain|logistics|warehouse", "Supply chain manager"),
        (r"manufacturing|factory|plant", "Plant manager"),
        (r"rail|port|water|infrastructure", "Infrastructure operator"),
        (r"scientist|lab|research", "Research scientist"),
        (r"city planner|urban planner", "City planner"),
        (r"utility", "Utility planner"),
        (r"creator|author|youtuber|consultant", "Creator"),
        (r"investor|vc|private equity|hedge fund", "Investor"),
        (r"founder|entrepreneur", "Founder"),
        (r"community", "Community manager"),
        (r"individual|professional", "Individual professional"),
        (r"robot|automation", "Automation operations leader"),
        (r"government|public", "Public sector strategist"),
    ]
    for pattern, normalized in rules:
        if re.search(pattern, lower):
            return normalized, False
    return None, False


def infer_customer_from_keywords(profile: DomainProfile, haystack: str) -> str:
    if profile.name == "product":
        if re.search(r"head of product|vp product|product leader", haystack):
            return "Product leader"
        return "Product manager"
    if profile.name == "org-ops":
        if re.search(r"chief of staff", haystack):
            return "Chief of staff"
        return "Operations executive"
    if profile.name == "workflow":
        return "Operations manager"
    if profile.name == "gtm":
        if re.search(r"user research|customer interview|interview synthesis", haystack):
            return "User researcher"
        if re.search(r"support ticket|support\b|help desk|service desk", haystack):
            return "Support leader"
        if re.search(r"customer success|renewal|account\b", haystack):
            return "Customer success manager"
        return "Revenue operations leader"
    if profile.name == "finance-legal":
        if re.search(r"legal|compliance|law firm|evidence collection", haystack):
            return "Legal operations leader"
        if re.search(r"finance|accounting|wealth|tax|bookkeeping", haystack):
            return "Finance manager"
        return "Procurement leader"
    if profile.name == "talent-learning":
        if re.search(r"teacher|educator|classroom|school|professor", haystack):
            return "Educator"
        if re.search(r"student|learner", haystack):
            return "Learner"
        if re.search(r"recruit|hiring|talent acquisition", haystack):
            return "Recruiter"
        return "Learning and development leader"
    if profile.name == "family-home":
        return "Parent"
    if profile.name == "health-care":
        if re.search(r"family caregiver|caregiver", haystack):
            return "Family caregiver"
        if re.search(r"patient\b", haystack):
            return "Patient"
        return "Care coordinator"
    if profile.name == "ops-infra":
        if re.search(r"quality|defect|inspection", haystack):
            return "Quality manager"
        if re.search(r"supply chain|logistics|warehouse", haystack):
            return "Supply chain manager"
        if re.search(r"manufacturing|factory|plant", haystack):
            return "Plant manager"
        if re.search(r"rail|port|water|utility asset|infrastructure operator", haystack):
            return "Infrastructure operator"
        return "Operations manager"
    if profile.name == "science":
        if re.search(r"scientist|lab|experiment", haystack):
            return "Research scientist"
        return "R&D leader"
    if profile.name == "climate-energy":
        if re.search(r"city|urban", haystack):
            return "City planner"
        if re.search(r"grid|utility|energy", haystack):
            return "Utility planner"
        return "Infrastructure planner"
    if profile.name == "creator-ip":
        return "Creator"
    if profile.name == "founder-investor":
        if re.search(r"investor|vc|private equity|hedge fund", haystack):
            return "Investor"
        return "Founder"
    if profile.name == "social-community":
        return "Community manager"
    if profile.name == "personal-growth":
        return "Individual professional"
    if profile.name == "robotics":
        return "Automation operations leader"
    if profile.name == "institutions":
        return "Public sector strategist"
    return profile.customer


def infer_customer(title: str, wording: str, sections: dict[str, list[str]], profile: DomainProfile) -> tuple[str, bool, bool]:
    explicit_candidates: list[str] = []
    if sections.get("customer"):
        explicit_candidates.append(trim_sentence(" ".join(sections["customer"][:2]), limit=120))

    title_customer = extract_customer_from_title(title)
    if title_customer:
        explicit_candidates.append(title_customer)

    mixed_source = False
    for candidate in explicit_candidates:
        normalized, mixed = normalize_explicit_customer(candidate)
        mixed_source = mixed_source or mixed
        if normalized:
            return normalized, False, mixed_source

    haystack = f"{title} {wording}".lower()
    return infer_customer_from_keywords(profile, haystack), True, mixed_source


def infer_archetype(title: str, description: str, wording: str, track: str) -> tuple[str, bool]:
    title_key = normalize_label(title)
    if title_key in TITLE_ARCHETYPE_OVERRIDES:
        return TITLE_ARCHETYPE_OVERRIDES[title_key], False

    haystack = f"{title} {description} {wording}".lower()
    scored: list[tuple[int, str]] = []
    for primitive, keywords in ARCHETYPE_RULES:
        score = sum(1 for keyword in keywords if keyword in haystack)
        if score:
            scored.append((score, primitive))

    if scored:
        scored.sort(key=lambda item: (-item[0], item[1]))
        best_score, best_primitive = scored[0]
        uncertain = best_score == 1 and best_primitive in {
            "Workflow Orchestration",
            "Exchange Network",
            "Compounding Loop",
        }
        return best_primitive, uncertain

    if track == "Behavior":
        return "Compounding Loop", True
    if track == "Fusion":
        return "Workflow Orchestration", True
    return "Workflow Orchestration", True


def infer_primitive(title: str, description: str, wording: str, track: str) -> tuple[str, bool]:
    archetype, archetype_uncertain = infer_archetype(title, description, wording, track)
    haystack = f"{title} {description} {wording}".lower()
    title_lower = title.lower()
    scores: Counter[str] = Counter()
    scores[ARCHETYPE_TO_PRIMITIVE[archetype]] += 3

    for primitive, keywords in CONTROLLED_PRIMITIVE_RULES:
        for keyword in keywords:
            if keyword in haystack:
                weight = 2 if keyword in title_lower else 1
                scores[primitive] += weight * haystack.count(keyword)

    if "quality inspector" in haystack or "defect detection" in haystack:
        scores["Verify"] += 3
    if "root-cause" in haystack and "quality" in haystack:
        scores["Verify"] += 2
    if "adaptive" in title_lower or "adaptation" in title_lower:
        scores["Adapt"] += 4
    if "valuable futures" in haystack or "possibility network" in haystack:
        scores["Discover"] += 2
    if "continuously optimizes" in haystack or "next highest-value" in haystack:
        scores["Optimize"] += 2
    if "adaptive knowledge" in haystack or "promotes emerging knowledge" in haystack:
        scores["Adapt"] += 3
    if track == "Behavior":
        scores["Compound"] += 1
        scores["Learn"] += 1
    if track == "Fusion":
        scores["Adapt"] += 1
        scores["Discover"] += 1

    ranked = sorted(
        scores.items(),
        key=lambda item: (-item[1], CONTROLLED_PRIMITIVE_ORDER.index(item[0])),
    )
    best_primitive = ranked[0][0]
    best_score = ranked[0][1]
    second_score = ranked[1][1] if len(ranked) > 1 else 0
    uncertain = archetype_uncertain or best_score <= 3 or second_score >= best_score - 1
    return best_primitive, uncertain


def count_signal_lines(title: str, wording: str) -> int:
    count = 0
    for raw_line in wording.replace("\r\n", "\n").split("\n"):
        if is_meta_line(raw_line, title):
            continue
        if clean_line(raw_line):
            count += 1
    return count


def infer_evidence(title: str, wording: str, sections: dict[str, list[str]], description_fallback: bool) -> str:
    lower = wording.lower()
    signal_lines = count_signal_lines(title, wording)
    has_sections = bool(sections)

    if re.search(r"\b(arr|mrr|gmv|revenue|royalties|pricing experiment|retention|conversion|margin)\b", lower):
        return "Revenue Evidence"
    if re.search(r"\b(from|based on|trained from|using)\s+(real interactions|usage data|telemetry|sensor data|logs?)\b", lower):
        return "Behavioral Data"
    if re.search(r"\b(from|based on|after)\s+interviews?\b", lower) or re.search(r"\binterviews?\s+(show|revealed|suggest)\b", lower):
        return "Interview Evidence"
    if re.search(r"customer complaint|customers say|users say|customer quote|support complaint", lower):
        return "Customer Voice"
    if re.search(r"\b(study|report|paper|benchmark|survey|patent|academic)\b", lower) or "memcite" in wording:
        return "Secondary Research"
    if has_sections or any(marker in lower for marker in ("why now:", "collision:", "current behavior", "new behavior", "top 3", "candidate observation")):
        return "Pattern Evidence"
    if description_fallback:
        return "None"
    if signal_lines >= 3:
        return "Pattern Evidence"
    return "Intuition"


def count_stars(wording: str) -> int | None:
    match = re.search(r"Initial Rating:\s*([⭐☆]+)", wording)
    if not match:
        return None
    return match.group(1).count("⭐")


def infer_confidence(
    title: str,
    wording: str,
    why_now: str,
    evidence: str,
    description_fallback: bool,
    primitive_uncertain: bool,
    customer_inferred: bool,
    wedge_review: bool,
    track: str,
) -> int:
    lower = wording.lower()
    stars = count_stars(wording)
    signal_lines = count_signal_lines(title, wording)
    score = 3

    if stars is not None:
        if stars >= 4:
            score += 1
        elif stars <= 2:
            score -= 1

    if why_now != UNKNOWN:
        score += 1
    if evidence in DIRECT_EVIDENCE_VALUES or evidence == "Secondary Research":
        score += 1
    if "my favorite idea of the entire exercise" in lower:
        score += 1
    elif "my favorite" in lower or "favorite of the" in lower or "top 3" in lower:
        score += 1

    if description_fallback or signal_lines <= 1:
        score -= 1
    if primitive_uncertain:
        score -= 1
    if track == "Fusion" or any(marker in lower for marker in ("civilization", "society layer", "not a product")):
        score -= 1

    score = max(1, min(5, score))
    if signal_lines <= 2 and why_now == UNKNOWN and evidence == "None":
        score = min(score, 2)
    if score == 5 and evidence not in DIRECT_EVIDENCE_VALUES and "my favorite idea of the entire exercise" not in lower:
        score = 4
    if score < 2 and evidence in {"Pattern Evidence", "Intuition"} and not description_fallback:
        score = 2
    return score


def infer_job(primitive: str, profile: DomainProfile) -> str:
    templates = {
        "Discover": "Find opportunities in {obj}.",
        "Predict": "Predict outcomes in {obj}.",
        "Verify": "Verify quality in {obj}.",
        "Coordinate": "Coordinate {obj}.",
        "Compound": "Compound gains in {obj}.",
        "Remember": "Preserve context for {obj}.",
        "Adapt": "Adapt {obj}.",
        "Create": "Create reusable outputs for {obj}.",
        "Simulate": "Test scenarios in {obj}.",
        "Optimize": "Improve {obj}.",
        "Match": "Match the right resources in {obj}.",
        "Learn": "Accelerate {obj}.",
    }
    return templates[primitive].format(obj=profile.object_label)


def extract_job_context(job: str) -> tuple[str, str]:
    trimmed = job.rstrip(".")
    for prefix in JOB_PREFIXES:
        if trimmed.startswith(prefix):
            return prefix, trimmed[len(prefix) :]
    return trimmed, trimmed


def infer_canonical_job(legacy_job: str) -> str:
    prefix, context = extract_job_context(legacy_job)

    if prefix == "Improve ":
        if context in DECISION_CONTEXTS:
            return "Improve decisions"
        if context in DEVELOPMENT_CONTEXTS:
            return "Improve capability"
        if context in PLANNING_CONTEXTS:
            return "Improve planning"
        if context in CREATION_CONTEXTS:
            return "Improve creation"
        return "Improve execution"
    if prefix == "Accelerate ":
        if context in DEVELOPMENT_CONTEXTS:
            return "Accelerate learning"
        return "Accelerate execution"
    if prefix == "Coordinate ":
        return "Coordinate work"
    if prefix == "Preserve context for ":
        return "Preserve context"
    if prefix == "Find opportunities in ":
        return "Find opportunities"
    if prefix == "Match the right resources in ":
        return "Match resources"
    if prefix == "Verify quality in ":
        return "Verify quality"
    if prefix == "Predict outcomes in ":
        return "Predict outcomes"
    if prefix == "Test scenarios in ":
        return "Test scenarios"
    if prefix == "Create reusable outputs for ":
        return "Create reusable outputs"
    if prefix == "Compound gains in ":
        if context in DEVELOPMENT_CONTEXTS:
            return "Compound capability"
        return "Compound gains"
    if prefix == "Adapt ":
        return "Adapt continuously"
    raise ValueError(f"Unexpected legacy job format: {legacy_job}")


def add_scores(scores: Counter[str], additions: dict[str, int]) -> None:
    for label, weight in additions.items():
        scores[label] += weight


def score_keyword_matches(text: str, title_lower: str, scores: Counter[str]) -> None:
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                weight = 3 if keyword in title_lower else 1
                scores[domain] += weight


def infer_domain(row: dict[str, str]) -> tuple[str, bool]:
    legacy_job = row["Job"]
    customer = row["Customer"]
    title_lower = row["Concept Title"].lower()
    text = " ".join(
        [
            row["Concept Title"],
            row["Clear Description"],
            legacy_job,
            customer,
            row["Initial Wedge"],
            row["Original Wording"],
        ]
    ).lower()

    _, context = extract_job_context(legacy_job)
    scores: Counter[str] = Counter()
    add_scores(scores, JOB_CONTEXT_DOMAIN_BASES.get(context, {}))
    add_scores(scores, CUSTOMER_DOMAIN_BASES.get(customer, {}))
    score_keyword_matches(text, title_lower, scores)

    if "user research" in text or "customer feedback" in text or "interview" in text:
        scores["Research"] += 3
    if "career pivot" in text or "career changes" in text:
        scores["Talent"] += 2
        scores["Personal Development"] += 2
    if "trust infrastructure" in text or "critical infrastructure" in text:
        scores["Infrastructure"] += 3
    if any(keyword in text for keyword in ("public comment", "policy", "government", "regulation", "grant", "laws")):
        scores["Public Sector"] += 8
    if any(keyword in text for keyword in ("civilization", "society", "humanity", "civilizational", "institutions", "collective intelligence")):
        scores["Institutions"] += 8
    if any(keyword in title_lower for keyword in ("civilization", "society", "institution")):
        scores["Institutions"] += 5
    if any(keyword in title_lower for keyword in ("policy", "regulation", "grant", "public comment")):
        scores["Public Sector"] += 5
    if "play " in text or title_lower.startswith("play "):
        scores["Personal Development"] += 4

    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    if not ranked:
        return "Operations", True

    best_domain, best_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else 0
    uncertain = best_score < 4 or best_score - second_score <= 1
    return best_domain, uncertain


def append_note(notes: str, new_note: str) -> str:
    notes = notes.strip()
    if not notes:
        return new_note
    if new_note in notes:
        return notes
    return f"{notes} {new_note}"


def finalize_row(base_row: dict[str, str]) -> dict[str, str]:
    legacy_job = base_row["Job"]
    canonical_job = infer_canonical_job(legacy_job)
    domain, domain_uncertain = infer_domain(base_row)
    notes = base_row["Notes"]
    if domain_uncertain:
        notes = append_note(notes, "Domain required judgment between nearby controlled vocabulary labels.")

    return {
        "Concept ID": base_row["Concept ID"],
        "Concept Title": base_row["Concept Title"],
        "Clear Description": base_row["Clear Description"],
        "Track": base_row["Track"],
        "Batch": base_row["Batch"],
        "Primitive": base_row["Primitive"],
        "Canonical Job": canonical_job,
        "Domain": domain,
        "Customer": base_row["Customer"],
        "Value Mechanism": base_row["Value Mechanism"],
        "Initial Wedge": base_row["Initial Wedge"],
        "Confidence": base_row["Confidence"],
        "Evidence": base_row["Evidence"],
        "Why Now": base_row["Why Now"],
        "Notes": notes,
        "Raw Source ID": base_row["Raw Source ID"],
        "Original Wording": base_row["Original Wording"],
    }


def infer_value_mechanism(primitive: str, profile: DomainProfile) -> str:
    templates = {
        "Discover": "Searches a wider option space and surfaces higher-value openings in {obj} before teams would find them manually.",
        "Predict": "Turns leading signals into earlier forecasts so teams can change outcomes in {obj}.",
        "Verify": "Produces trustworthy checks, measurements, or proofs so teams can reduce errors in {obj}.",
        "Coordinate": "Reduces manual handoffs and keeps multi-step work moving across {obj}.",
        "Compound": "Carries gains from one cycle into the next so value in {obj} accumulates instead of resetting.",
        "Remember": "Makes prior decisions, context, and history reusable during {obj}.",
        "Adapt": "Keeps plans and systems aligned with changing conditions during {obj}.",
        "Create": "Converts expertise or intent into reusable outputs that accelerate {obj}.",
        "Simulate": "Lets teams explore scenarios in {obj} before spending time, capital, or trust.",
        "Optimize": "Improves prioritization, tradeoffs, or negotiated outcomes in {obj}.",
        "Match": "Connects the right people, assets, or opportunities faster in {obj}.",
        "Learn": "Improves performance through repeated feedback and practice in {obj}.",
    }
    return templates[primitive].format(obj=profile.object_label)


def infer_wedge(title: str, wording: str, profile: DomainProfile, customer: str) -> tuple[str, bool]:
    start_match = re.search(r"Start in ([^.]+)\.?", wording, flags=re.IGNORECASE)
    if start_match:
        start_value = clean_line(start_match.group(1))
        if start_value.lower() == "one vertical":
            return "One vertical where the workflow is repetitive enough to keep expert review in the loop.", True
        return ensure_period(start_value), False

    one_vertical = re.search(r"one vertical", wording, flags=re.IGNORECASE)
    if one_vertical:
        return "One vertical with repetitive, high-value workflows where expert review can stay in the loop.", True

    wedge_by_customer = {
        "Product manager": "Mid-market SaaS product teams triaging weekly roadmap tradeoffs across Jira, support, and usage analytics.",
        "Product leader": "Mid-market SaaS product teams triaging weekly roadmap tradeoffs across Jira, support, and usage analytics.",
        "Chief of staff": "Leadership teams coordinating recurring planning and execution handoffs across meetings, chat, docs, and dashboards.",
        "Operations executive": "Mid-market leadership teams reconciling decisions across meetings, chat, docs, and dashboards.",
        "Operations manager": "Back-office teams running repetitive approvals, service handoffs, or exception workflows across disconnected tools.",
        "Customer success manager": "B2B SaaS customer-success teams preparing renewal and risk reviews from fragmented notes and product signals.",
        "Support leader": "Support teams triaging recurring tickets and escalations across chat, email, and help desk systems.",
        "User researcher": "Research teams synthesizing recurring interviews, calls, and feedback without dedicated research operations support.",
        "Revenue operations leader": "Revenue teams consolidating account, pipeline, and customer signals before weekly decisions.",
        "Procurement leader": "Procurement teams handling recurring SaaS renewals and vendor negotiations without a dedicated analyst.",
        "Legal operations leader": "Legal and compliance teams assembling contract or evidence packets across fragmented systems.",
        "Finance manager": "Finance teams reconciling repetitive close, audit, or spend workflows across spreadsheets and source systems.",
        "Recruiter": "Recruiting teams screening high applicant volumes without enough recruiter capacity.",
        "Learning and development leader": "People teams running onboarding or coaching programs with limited manager bandwidth.",
        "Educator": "Classrooms or course teams managing repeated practice and feedback cycles outside live instruction.",
        "Learner": "Self-directed learners seeking repeated practice, feedback, or coaching between formal sessions.",
        "Parent": "Dual-income households coordinating calendars, school logistics, finances, and home tasks.",
        "Patient": "Patients with ongoing care plans coordinating appointments, medications, and follow-ups across providers.",
        "Family caregiver": "Family caregivers managing multi-party care updates, appointments, and medication schedules.",
        "Care coordinator": "Care coordination teams managing appointments, medications, follow-ups, and family communication across settings.",
        "Quality manager": "Manufacturers monitoring high-volume lines where defect detection and root-cause analysis are still manual.",
        "Supply chain manager": "Supply chain teams scheduling constrained inventory, vendors, or routes under volatile demand.",
        "Plant manager": "Plant teams coordinating maintenance, staffing, and throughput decisions across fragmented systems.",
        "Infrastructure operator": "Infrastructure operators managing rail, port, water, or utility assets with manual exception handling.",
        "Research scientist": "Research teams moving experiments from hypothesis to validation with fragmented evidence trails.",
        "R&D leader": "Applied R&D teams moving experiments from hypothesis to validation with fragmented evidence trails.",
        "City planner": "Cities planning long-horizon resilience or infrastructure investments under climate pressure.",
        "Utility planner": "Utilities planning reliability or capital decisions under grid volatility.",
        "Infrastructure planner": "Cities, utilities, or asset owners planning capital decisions under climate or grid volatility.",
        "Creator": "Creators and small media teams turning repeated research into publishable content without a reusable system.",
        "Investor": "Early-stage investors evaluating repeated deals, diligence, and portfolio decisions with lean teams.",
        "Founder": "Founder-led teams evaluating repeated product, hiring, or expansion decisions without analyst support.",
        "Community manager": "Communities where retention depends on repeated contribution, matching, and moderation.",
        "Individual professional": "Self-directed professionals already using journals, notes, or coaching tools without continuity between sessions.",
        "Automation operations leader": "Operations teams deploying physical automation in labor-constrained environments.",
        "Public sector strategist": "Policy and strategy teams working on multi-year public coordination problems.",
    }

    lower = f"{title} {wording}".lower()
    wedge = wedge_by_customer.get(customer, profile.wedge)
    needs_review = customer in {"Operations executive", "Public sector strategist", "Individual professional"} and not any(
        keyword in lower for keyword in ("mid-market", "saaS", "policy", "coach", "journal", "roadmap", "provider")
    )
    if "mid-market" in lower and customer == "Operations executive":
        wedge = "Mid-market leadership teams reconciling decisions across meetings, chat, docs, and dashboards."
    return wedge, needs_review


def build_notes(
    track_known: bool,
    customer_inferred: bool,
    customer_mixed: bool,
    primitive_uncertain: bool,
    wedge_review: bool,
    description_fallback: bool,
    why_now: str,
    track: str,
    evidence: str,
    confidence: int,
) -> str:
    notes: list[str] = []
    if not track_known:
        notes.append("Track not recoverable from the raw inventory; marked Unknown.")
    if customer_inferred:
        notes.append("Customer normalized from title or domain cues rather than an explicit raw persona.")
    if customer_mixed:
        notes.append("Original customer wording mixed multiple personas, so one primary role was selected.")
    if primitive_uncertain:
        notes.append("Primitive required judgment between nearby controlled taxonomy labels.")
    if wedge_review:
        notes.append("Initial wedge remains broad and should be narrowed manually before external use.")
    if description_fallback:
        notes.append("Raw wording was minimal, so the description relies on title-level interpretation.")
    if why_now == UNKNOWN:
        notes.append("Why now was not explicit in the raw wording.")
    if evidence in {"Intuition", "None"}:
        notes.append("Evidence level is based on concept framing rather than cited external validation.")
    if confidence <= 2:
        notes.append("Confidence reduced because the concept remains broad or lightly specified.")
    if track == "Fusion":
        notes.append("Fusion concept combines multiple motifs; one primary primitive was selected for one-to-one schema coverage.")
    return " ".join(notes)


def derive_row(raw_row: dict[str, str]) -> dict[str, str]:
    title = clean_title(raw_row["Concept"])
    wording = raw_row["Original Wording"]
    sections = parse_sections(wording)
    description, description_fallback = extract_description(title, wording, sections)

    raw_track = raw_row["Track"].strip()
    track = raw_track or UNKNOWN
    batch = raw_row["Batch"].strip() or UNKNOWN
    track_known = bool(raw_track)

    profile = infer_profile(title, description, wording, track)
    customer, customer_inferred, customer_mixed = infer_customer(title, wording, sections, profile)
    primitive, primitive_uncertain = infer_primitive(title, description, wording, track)
    why_now = extract_why_now(wording)
    evidence = infer_evidence(title, wording, sections, description_fallback)
    wedge, wedge_review = infer_wedge(title, wording, profile, customer)
    confidence = infer_confidence(
        title,
        wording,
        why_now,
        evidence,
        description_fallback,
        primitive_uncertain,
        customer_inferred,
        wedge_review,
        track,
    )
    notes = build_notes(
        track_known,
        customer_inferred,
        customer_mixed,
        primitive_uncertain,
        wedge_review,
        description_fallback,
        why_now,
        track,
        evidence,
        confidence,
    )

    return {
        "Concept ID": raw_row["Concept ID"],
        "Concept Title": title,
        "Clear Description": description,
        "Track": track,
        "Batch": batch,
        "Primitive": primitive,
        "Job": infer_job(primitive, profile),
        "Customer": customer,
        "Value Mechanism": infer_value_mechanism(primitive, profile),
        "Initial Wedge": wedge,
        "Confidence": str(confidence),
        "Evidence": evidence,
        "Why Now": why_now,
        "Notes": notes,
        "Raw Source ID": raw_row["Concept ID"],
        "Original Wording": wording,
    }


def write_csv(path: Path, rows: Iterable[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def apply_legacy_overrides(row: dict[str, str]) -> dict[str, str]:
    override = LEGACY_ROW_OVERRIDES.get(row["Concept ID"])
    if not override:
        return row
    updated = row.copy()
    updated.update(override)
    return updated


def format_counts(counter: Counter[str]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in sorted(counter.items(), key=lambda item: item[0]))


def markdown_frequency_table(counter: Counter[str], first_col: str) -> list[str]:
    lines = [
        f"| {first_col} | Count |",
        "| --- | ---: |",
    ]
    for label, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {label} | {count} |")
    return lines


def build_job_taxonomy_rows(
    legacy_rows: list[dict[str, str]],
    curated_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    canonical_to_variants: dict[str, Counter[str]] = {}
    canonical_to_count: Counter[str] = Counter()

    for legacy_row, curated_row in zip(legacy_rows, curated_rows):
        canonical_job = curated_row["Canonical Job"]
        canonical_to_count[canonical_job] += 1
        canonical_to_variants.setdefault(canonical_job, Counter())[legacy_row["Job"]] += 1

    rows: list[dict[str, str]] = []
    for canonical_job, concept_count in sorted(
        canonical_to_count.items(),
        key=lambda item: (-item[1], item[0]),
    ):
        variants = canonical_to_variants[canonical_job]
        rows.append(
            {
                "Canonical Job": canonical_job,
                "Description": CANONICAL_JOB_DESCRIPTIONS[canonical_job],
                "Example Variants": "; ".join(job for job, _count in variants.most_common(5)),
                "Concept Count": str(concept_count),
            }
        )
    return rows


def qa_report(
    raw_rows: list[dict[str, str]],
    legacy_rows: list[dict[str, str]],
    curated_rows: list[dict[str, str]],
) -> str:
    raw_ids = [row["Concept ID"] for row in raw_rows]
    curated_ids = [row["Concept ID"] for row in curated_rows]
    raw_counter = Counter(raw_ids)
    curated_counter = Counter(curated_ids)
    duplicate_raw = sorted(concept_id for concept_id, count in raw_counter.items() if count > 1)
    duplicate_curated = sorted(concept_id for concept_id, count in curated_counter.items() if count > 1)
    missing_raw = sorted(set(raw_ids) - set(curated_ids))
    extra_curated = sorted(set(curated_ids) - set(raw_ids))

    required_fields = [
        "Concept ID",
        "Concept Title",
        "Clear Description",
        "Track",
        "Batch",
        "Primitive",
        "Canonical Job",
        "Domain",
        "Customer",
        "Value Mechanism",
        "Initial Wedge",
        "Confidence",
        "Evidence",
        "Why Now",
        "Raw Source ID",
        "Original Wording",
    ]
    missing_field_counts = {
        field: sum(1 for row in curated_rows if not str(row[field]).strip()) for field in required_fields
    }

    unknown_track_count = sum(1 for row in curated_rows if row["Track"] == UNKNOWN)
    unknown_batch_count = sum(1 for row in curated_rows if row["Batch"] == UNKNOWN)
    unknown_why_now_count = sum(1 for row in curated_rows if row["Why Now"] == UNKNOWN)
    legacy_job_count = len({row["Job"] for row in legacy_rows})
    canonical_job_count = len({row["Canonical Job"] for row in curated_rows})
    distinct_domain_count = len({row["Domain"] for row in curated_rows})
    changed_concepts = sum(
        1
        for legacy_row, curated_row in zip(legacy_rows, curated_rows)
        if legacy_row["Job"].rstrip(".") != curated_row["Canonical Job"]
    )

    review_buckets: dict[str, list[str]] = {
        "Minimal raw detail / description fallback": [],
        "Primitive assignments needing judgment": [],
        "Domain mappings needing judgment": [],
        "Broad initial wedges needing manual narrowing": [],
        "Low-confidence concepts (1-2)": [],
        "Fusion concepts with multi-primitive overlap": [],
    }
    for row in curated_rows:
        notes = row["Notes"]
        concept_id = row["Concept ID"]
        if "description relies on title-level interpretation" in notes:
            review_buckets["Minimal raw detail / description fallback"].append(concept_id)
        if "Primitive required judgment between nearby controlled taxonomy labels." in notes:
            review_buckets["Primitive assignments needing judgment"].append(concept_id)
        if "Domain required judgment between nearby controlled vocabulary labels." in notes:
            review_buckets["Domain mappings needing judgment"].append(concept_id)
        if "Initial wedge remains broad and should be narrowed manually before external use." in notes:
            review_buckets["Broad initial wedges needing manual narrowing"].append(concept_id)
        if row["Confidence"] in {"1", "2"}:
            review_buckets["Low-confidence concepts (1-2)"].append(concept_id)
        if "Fusion concept combines multiple motifs" in notes:
            review_buckets["Fusion concepts with multi-primitive overlap"].append(concept_id)

    evidence_counts = Counter(row["Evidence"] for row in curated_rows)
    confidence_counts = Counter(row["Confidence"] for row in curated_rows)
    canonical_job_counts = Counter(row["Canonical Job"] for row in curated_rows)
    domain_counts = Counter(row["Domain"] for row in curated_rows)

    lines = [
        "# Atlas Concept Inventory QA",
        "",
        f"Generated: {GENERATED_DATE}",
        "",
        "## Summary",
        "",
        f"- Raw row count: {len(raw_rows)}",
        f"- Curated row count: {len(curated_rows)}",
        f"- Original distinct Job count: {legacy_job_count}",
        f"- Canonical Job count: {canonical_job_count}",
        f"- Distinct Domain count: {distinct_domain_count}",
        f"- Concepts changed: {changed_concepts}",
        f"- One-to-one ID coverage: {'PASS' if not missing_raw and not extra_curated and len(raw_rows) == len(curated_rows) else 'FAIL'}",
        f"- Duplicate raw IDs: {len(duplicate_raw)}",
        f"- Duplicate curated IDs: {len(duplicate_curated)}",
        "",
        "## Coverage Detail",
        "",
        f"- Missing curated IDs from raw: {', '.join(missing_raw) if missing_raw else 'None'}",
        f"- Extra curated IDs not found in raw: {', '.join(extra_curated) if extra_curated else 'None'}",
        f"- Duplicate raw ID list: {', '.join(duplicate_raw) if duplicate_raw else 'None'}",
        f"- Duplicate curated ID list: {', '.join(duplicate_curated) if duplicate_curated else 'None'}",
        "",
        "## Missing Required Fields",
        "",
    ]

    for field in required_fields:
        lines.append(f"- {field}: {missing_field_counts[field]}")

    lines.extend(
        [
            "",
            "## Unknown Normalization Counts",
            "",
            f"- Unknown Track count: {unknown_track_count}",
            f"- Unknown Batch count: {unknown_batch_count}",
            f"- Unknown Why Now count: {unknown_why_now_count}",
            "",
            "## Distribution Checks",
            "",
            f"- Evidence distribution: {format_counts(evidence_counts)}",
            f"- Confidence distribution: {format_counts(confidence_counts)}",
            "",
            "## Canonical Job Frequency",
            "",
        ]
    )
    lines.extend(markdown_frequency_table(canonical_job_counts, "Canonical Job"))
    lines.extend(
        [
            "",
            "## Domain Frequency",
            "",
        ]
    )
    lines.extend(markdown_frequency_table(domain_counts, "Domain"))
    lines.extend(
        [
            "",
            "## Ambiguous Rows Requiring Review",
            "",
        ]
    )

    for label, concept_ids in review_buckets.items():
        lines.append(f"- {label}: {len(concept_ids)}")
        if concept_ids:
            lines.append(f"  IDs: {', '.join(concept_ids)}")

    return "\n".join(lines) + "\n"


def main() -> None:
    if not RAW_PATH.exists():
        raise SystemExit(f"Missing raw source: {RAW_PATH}")

    raw_rows = load_rows(RAW_PATH)
    legacy_rows = [apply_legacy_overrides(derive_row(row)) for row in raw_rows]
    curated_rows = [finalize_row(row) for row in legacy_rows]
    write_csv(CURATED_PATH, curated_rows, CURATED_COLUMNS)
    write_csv(
        JOB_TAXONOMY_PATH,
        build_job_taxonomy_rows(legacy_rows, curated_rows),
        ["Canonical Job", "Description", "Example Variants", "Concept Count"],
    )
    QA_PATH.write_text(qa_report(raw_rows, legacy_rows, curated_rows), encoding="utf-8")


if __name__ == "__main__":
    main()
