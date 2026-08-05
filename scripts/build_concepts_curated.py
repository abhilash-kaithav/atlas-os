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

UNKNOWN = "Unknown"

CURATED_COLUMNS = [
    "Concept ID",
    "Concept Title",
    "Clear Description",
    "Track",
    "Batch",
    "Primitive",
    "Job",
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

RECURRING_PRIMITIVES = {
    "Decision Draft",
    "Learning Loop",
    "Trust Trial",
    "Opportunity Queue",
    "Compounding Loop",
    "Discovery Engine",
}

PRIMITIVE_RULES = [
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

TITLE_PRIMITIVE_OVERRIDES = {
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
        "Product managers and product leaders",
        "product planning and roadmap execution",
        "Product teams already coordinating work across Jira, Slack, analytics, support, and customer feedback",
    ),
    DomainProfile(
        "org-ops",
        ("company", "enterprise", "organiz", "executive", "ceo", "board", "operating manual", "decision"),
        "Executives and operating leaders",
        "organizational operations and strategic choices",
        "Mid-market teams whose operating context is fragmented across meetings, chat, docs, and dashboards",
    ),
    DomainProfile(
        "workflow",
        ("workflow", "automation", "sop", "process", "back office", "operations", "chief of staff"),
        "Operations teams and functional operators",
        "repeatable workflows and operating processes",
        "Teams running high-friction, multi-step workflows without reliable automation coverage",
    ),
    DomainProfile(
        "gtm",
        ("customer", "sales", "revenue", "support", "renewal", "interview", "go-to-market", "account"),
        "Go-to-market, support, and research teams",
        "customer-facing workflows and account decisions",
        "Revenue and support teams handling recurring customer research, service, or renewal work",
    ),
    DomainProfile(
        "finance-legal",
        ("finance", "procurement", "vendor", "contract", "legal", "accounting", "wealth", "tax", "audit"),
        "Finance, procurement, and legal operators",
        "financial, commercial, and compliance work",
        "Teams managing recurring contracts, renewals, compliance work, or high-stakes financial workflows",
    ),
    DomainProfile(
        "talent-learning",
        ("recruit", "talent", "hr", "hiring", "employee", "learning", "school", "student", "teacher"),
        "People teams, educators, and learners",
        "learning and talent development",
        "Organizations or households already investing time in recruiting, onboarding, or learning support",
    ),
    DomainProfile(
        "family-home",
        ("family", "home", "household", "calendar", "travel", "bill", "chore", "parent"),
        "Busy households and family coordinators",
        "household logistics and family coordination",
        "Dual-income or high-coordination households juggling calendars, school, travel, finances, and home tasks",
    ),
    DomainProfile(
        "health-care",
        ("health", "care", "patient", "clinic", "medical", "medication", "caregiver", "senior", "aging"),
        "Care teams, patients, and family caregivers",
        "care coordination and health management",
        "Care settings where appointments, medications, follow-ups, and family communication regularly break down",
    ),
    DomainProfile(
        "ops-infra",
        ("supply chain", "logistics", "warehouse", "quality", "manufacturing", "factory", "rail", "port", "water"),
        "Operations, logistics, and infrastructure leaders",
        "industrial operations and infrastructure workflows",
        "Operators managing physical systems with high coordination cost, downtime risk, or defect pressure",
    ),
    DomainProfile(
        "science",
        ("science", "scientific", "research", "lab", "materials", "experiment", "discovery", "patent"),
        "Research teams, labs, and discovery organizations",
        "scientific discovery and R&D execution",
        "Research organizations trying to shorten the gap between discovery, validation, and commercialization",
    ),
    DomainProfile(
        "climate-energy",
        ("climate", "energy", "grid", "urban", "city", "infrastructure", "migration", "resilience"),
        "Public-sector, climate, and infrastructure planners",
        "climate adaptation and infrastructure planning",
        "Cities, utilities, and infrastructure owners facing rising volatility and capital-allocation pressure",
    ),
    DomainProfile(
        "creator-ip",
        ("creator", "content", "media", "course", "book", "patent", "intellectual property", "ip"),
        "Creators and IP-heavy teams",
        "content creation and intellectual-property development",
        "Teams whose most valuable assets are created repeatedly but captured inconsistently today",
    ),
    DomainProfile(
        "founder-investor",
        ("founder", "startup", "venture", "entrepreneur", "investor", "acquisition", "vc"),
        "Founders, operators, and investors",
        "venture creation and capital-allocation decisions",
        "Founder-led teams or investment groups making repeated opportunity, diligence, or company-building decisions",
    ),
    DomainProfile(
        "social-community",
        ("community", "social", "relationship", "belonging", "contribution", "conversation", "network"),
        "Communities, network builders, and socially active individuals",
        "community behavior and relationship formation",
        "Groups where repeated participation and contribution determine whether the system gets stronger over time",
    ),
    DomainProfile(
        "personal-growth",
        ("cognitive", "memory", "identity", "meaning", "play", "thinking", "reasoning", "opinion", "self", "possibility", "listening", "understand", "future self"),
        "Individuals improving how they think, learn, and act",
        "personal cognition and self-development",
        "People already using reflective, learning, or self-improvement tools but lacking compounding support",
    ),
    DomainProfile(
        "robotics",
        ("robot", "robotics", "autonomous vehicle", "physical workforce", "microgravity", "manufacturing scheduler"),
        "Operators deploying physical automation",
        "physical capability deployment and automation planning",
        "Teams integrating physical automation where labor shortages or scheduling complexity already justify new systems",
    ),
    DomainProfile(
        "institutions",
        ("institution", "country", "nation", "civilization", "society", "government", "public", "future", "futures", "possibility", "progress"),
        "Institutional and public-sector leaders",
        "institutional adaptation and societal coordination",
        "Institutions facing long-horizon adaptation problems that current quarterly systems handle poorly",
    ),
]


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
        score = sum(1 for keyword in profile.keywords if keyword in haystack)
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


def infer_customer(title: str, sections: dict[str, list[str]], profile: DomainProfile) -> tuple[str, bool]:
    if sections.get("customer"):
        customer = trim_sentence(" ".join(sections["customer"][:2]), limit=120)
        return customer.rstrip("."), False

    title_customer = extract_customer_from_title(title)
    if title_customer:
        return title_customer, True

    return profile.customer, True


def infer_primitive(title: str, description: str, wording: str, track: str) -> tuple[str, bool]:
    title_key = normalize_label(title)
    if title_key in TITLE_PRIMITIVE_OVERRIDES:
        return TITLE_PRIMITIVE_OVERRIDES[title_key], False

    haystack = f"{title} {description} {wording}".lower()
    scored: list[tuple[int, str]] = []
    for primitive, keywords in PRIMITIVE_RULES:
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


def infer_evidence(wording: str, primitive: str, track: str) -> str:
    lower = wording.lower()
    if primitive in RECURRING_PRIMITIVES:
        return "Pattern"
    if track in {"Behavior", "Fusion"}:
        return "Pattern"
    if any(marker in lower for marker in ("why now:", "collision:", "**problem**", "**current behavior**", "current behavior")):
        return "Pattern"
    return "Intuition"


def count_stars(wording: str) -> int | None:
    match = re.search(r"Initial Rating:\s*([⭐☆]+)", wording)
    if not match:
        return None
    return match.group(1).count("⭐")


def infer_confidence(wording: str, primitive: str, description_fallback: bool, track: str) -> int:
    lower = wording.lower()
    stars = count_stars(wording)
    if stars is not None:
        score = max(3, min(5, stars))
    else:
        score = 3

    if "my favorite idea of the entire exercise" in lower:
        score = 5
    elif "my favorite" in lower or "favorite of the" in lower or "top 3" in lower:
        score = max(score, 4)

    if primitive in RECURRING_PRIMITIVES and track == "Behavior":
        score = max(score, 4)

    if "civilization" in lower or "society layer" in lower:
        score = min(score, 4)

    if description_fallback:
        score = max(2, score - 1)

    return max(1, min(5, score))


def infer_job(primitive: str, profile: DomainProfile) -> str:
    templates = {
        "Workflow Orchestration": "Coordinate {obj} with fewer manual handoffs.",
        "Memory Layer": "Recall and reuse context for {obj} at the moment of work.",
        "Decision Draft": "Make better decisions about {obj} with less manual synthesis.",
        "Learning Loop": "Improve performance in {obj} through repeated feedback in context.",
        "Trust Trial": "Reduce commitment risk in {obj} before full adoption.",
        "Opportunity Queue": "See the next highest-value action in {obj}.",
        "Compounding Loop": "Make each action in {obj} increase the value of the next one.",
        "Prediction Engine": "Anticipate outcomes in {obj} early enough to act.",
        "Simulation Twin": "Test changes in {obj} before committing resources.",
        "Discovery Engine": "Discover new opportunities or breakthroughs in {obj} earlier.",
        "Exchange Network": "Match the right participants, assets, or knowledge within {obj}.",
        "Measurement Index": "Measure the health, readiness, or progress of {obj} consistently.",
        "Negotiation Agent": "Negotiate better terms in {obj} with less manual effort.",
    }
    return templates[primitive].format(obj=profile.object_label)


def infer_value_mechanism(primitive: str, profile: DomainProfile) -> str:
    templates = {
        "Workflow Orchestration": "Creates a shared operating layer that automates coordination and reduces overhead across {obj}.",
        "Memory Layer": "Turns fragmented history into reusable memory so teams spend less time searching and less often repeat mistakes in {obj}.",
        "Decision Draft": "Surfaces signals, tradeoffs, and recommended next moves before decisions about {obj} stall or degrade.",
        "Learning Loop": "Captures feedback from each cycle so capability in {obj} improves with continued use.",
        "Trust Trial": "Makes adoption or partnership safer by introducing reversible tests and stronger trust signals around {obj}.",
        "Opportunity Queue": "Concentrates attention on the next highest-leverage move in {obj} instead of leaving prioritization implicit.",
        "Compounding Loop": "Stores gains from each cycle so value in {obj} accumulates instead of resetting after every action.",
        "Prediction Engine": "Uses pattern recognition to surface future states, shortages, or risks early enough to change the outcome in {obj}.",
        "Simulation Twin": "Models scenarios or digital twins so operators can explore tradeoffs in {obj} before spending time or capital.",
        "Discovery Engine": "Searches a broader solution space and turns weak signals into actionable discoveries in {obj}.",
        "Exchange Network": "Creates liquidity and coordination across fragmented participants involved in {obj}.",
        "Measurement Index": "Turns hard-to-see system quality into a comparable signal that can guide action in {obj}.",
        "Negotiation Agent": "Automates preparation and execution so teams can capture better outcomes in {obj} without proportional labor growth.",
    }
    return templates[primitive].format(obj=profile.object_label)


def infer_wedge(wording: str, profile: DomainProfile, customer: str) -> str:
    start_match = re.search(r"Start in ([^.]+)\.?", wording, flags=re.IGNORECASE)
    if start_match:
        start_value = clean_line(start_match.group(1))
        if start_value.lower() == "one vertical":
            return "One vertical where the workflow is repetitive enough to keep expert review in the loop."
        return ensure_period(start_value)

    one_vertical = re.search(r"one vertical", wording, flags=re.IGNORECASE)
    if one_vertical:
        return "One vertical with repetitive, high-value workflows where expert review can stay in the loop."

    if "mid-market" in wording.lower():
        return "Mid-market teams with enough process complexity to justify a shared operating layer but not enough specialists to build one internally."

    return profile.wedge


def build_notes(
    track_known: bool,
    customer_inferred: bool,
    primitive_uncertain: bool,
    description_fallback: bool,
    why_now: str,
    track: str,
) -> str:
    notes: list[str] = []
    if not track_known:
        notes.append("Track not recoverable from the raw inventory; marked Unknown.")
    if customer_inferred:
        notes.append("Customer inferred from title or surrounding wording.")
    if primitive_uncertain:
        notes.append("Primitive chosen from the nearest matching controlled taxonomy label.")
    if description_fallback:
        notes.append("Raw wording was minimal, so the description relies on title-level interpretation.")
    if why_now == UNKNOWN:
        notes.append("Why now was not explicit in the raw wording.")
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
    customer, customer_inferred = infer_customer(title, sections, profile)
    primitive, primitive_uncertain = infer_primitive(title, description, wording, track)
    why_now = extract_why_now(wording)
    evidence = infer_evidence(wording, primitive, track)
    confidence = infer_confidence(wording, primitive, description_fallback, track)
    notes = build_notes(track_known, customer_inferred, primitive_uncertain, description_fallback, why_now, track)

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
        "Initial Wedge": infer_wedge(wording, profile, customer),
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


def format_counts(counter: Counter[str]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in sorted(counter.items(), key=lambda item: item[0]))


def qa_report(raw_rows: list[dict[str, str]], curated_rows: list[dict[str, str]]) -> str:
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
        "Job",
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

    review_buckets: dict[str, list[str]] = {
        "Minimal raw detail / description fallback": [],
        "Low-confidence primitive assignment": [],
        "Fusion concepts with multi-primitive overlap": [],
    }
    for row in curated_rows:
        notes = row["Notes"]
        concept_id = row["Concept ID"]
        if "description relies on title-level interpretation" in notes:
            review_buckets["Minimal raw detail / description fallback"].append(concept_id)
        if "nearest matching controlled taxonomy label" in notes:
            review_buckets["Low-confidence primitive assignment"].append(concept_id)
        if "Fusion concept combines multiple motifs" in notes:
            review_buckets["Fusion concepts with multi-primitive overlap"].append(concept_id)

    evidence_counts = Counter(row["Evidence"] for row in curated_rows)
    confidence_counts = Counter(row["Confidence"] for row in curated_rows)

    lines = [
        "# Atlas Concept Inventory QA",
        "",
        "Generated: 2026-08-05",
        "",
        "## Summary",
        "",
        f"- Raw row count: {len(raw_rows)}",
        f"- Curated row count: {len(curated_rows)}",
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
    curated_rows = [derive_row(row) for row in raw_rows]
    write_csv(CURATED_PATH, curated_rows, CURATED_COLUMNS)
    QA_PATH.write_text(qa_report(raw_rows, curated_rows), encoding="utf-8")


if __name__ == "__main__":
    main()
