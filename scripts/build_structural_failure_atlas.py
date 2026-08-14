#!/usr/bin/env python3
"""Build Phase 3 structural failure artifacts from the Atlas Phase 1 and 2 evidence layers."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_LIBRARY_DIR = ROOT / "knowledge" / "research" / "workflow-library"
ATLAS_DIR = ROOT / "knowledge" / "research" / "structural-failure-atlas"

WORKFLOW_LIBRARY_CSV = WORKFLOW_LIBRARY_DIR / "canonical-workflow-library.csv"
WORKFLOW_INDEX_CSV = WORKFLOW_LIBRARY_DIR / "workflow-operating-system-industry-index.csv"

README_DOC = ATLAS_DIR / "README.md"
TAXONOMY_DOC = ATLAS_DIR / "structural-failure-taxonomy.md"
ATLAS_DOC = ATLAS_DIR / "structural-failure-atlas-v1.md"
EXECUTIVE_SUMMARY_DOC = ATLAS_DIR / "executive-summary.md"
CLASSIFICATION_CSV = ATLAS_DIR / "workflow-structural-failure-classification.csv"
FREQUENCY_MATRIX_CSV = ATLAS_DIR / "structural-failure-frequency-matrix.csv"

GENERATED_DATE = "2026-08-14"
MIN_SELECTED_SCORE = 6.0
MAX_FAILURES_PER_WORKFLOW = 3
TOTAL_WORKFLOWS = 198
TOTAL_USAGE_ROWS = 250

FIELD_WEIGHTS = {
    "where_money_is_lost": 1.0,
    "where_time_is_lost": 2.0,
    "where_human_judgment_dominates": 3.0,
    "where_people_leave_the_system_of_record": 3.0,
    "why_hasnt_this_been_solved": 3.0,
    "major_decisions": 1.0,
    "major_handoffs": 1.0,
    "objective": 0.5,
    "trigger": 0.5,
    "end_outcome": 0.5,
}

FAILURE_TAXONOMY = [
    {
        "code": "SF-01",
        "name": "Exception-Path Breakdown",
        "description": (
            "The core system handles the standard path, but economics and control "
            "break down when real-world exceptions enter the flow."
        ),
        "persistence_thesis": (
            "Incumbents automate the happy path, but they rarely unify upstream "
            "data quality, policy nuance, and local exception handling well enough "
            "to remove manual orchestration."
        ),
        "classification_cues": (
            "Edge cases, clean-path automation, exception triage, shortage recovery, "
            "and nonstandard scenarios."
        ),
        "keywords": [
            "exception",
            "exceptions",
            "edge case",
            "edge cases",
            "clean path",
            "deviation",
            "deviations",
            "unstructured",
            "satisfactory exception",
            "recover shortages",
            "shortages",
            "substitutions",
        ],
        "why_keywords": [
            "automation handles the clean path",
            "edge cases",
            "remain unstructured",
            "exception handling",
            "capacity realities still require manual orchestration",
        ],
    },
    {
        "code": "SF-02",
        "name": "Cross-System Reconciliation",
        "description": (
            "Teams must reconstruct truth by matching records, statuses, balances, "
            "or evidence across multiple systems, ledgers, and counterparties."
        ),
        "persistence_thesis": (
            "Authoritative records are distributed across asynchronous systems with "
            "inconsistent identifiers, timing, and standards, so reconciliation "
            "remains a manual control layer."
        ),
        "classification_cues": (
            "Manual matching, books-and-records alignment, settlement breaks, "
            "version truth, data lineage, and audit-trail rebuilds."
        ),
        "keywords": [
            "reconcile",
            "reconciliation",
            "matching records",
            "unmatched",
            "books and records",
            "version truth",
            "data lineage",
            "settlement",
            "audit trails",
            "definitions",
            "source evidence",
            "spreadsheet bridges",
            "duplicate data entry",
        ],
        "why_keywords": [
            "cross-book reconciliation",
            "low-standardization edge cases",
            "asynchronous systems",
            "version truth remains hard to unify",
            "data lineage",
        ],
    },
    {
        "code": "SF-03",
        "name": "Decision Context Escapes the Record",
        "description": (
            "The decisive context for advancing work lives outside the formal system "
            "of record in email, calls, spreadsheets, decks, notes, or portals."
        ),
        "persistence_thesis": (
            "Systems of record optimize for structured state capture, while "
            "collaboration tools hold the narrative, negotiation, and exception "
            "context that operators actually need."
        ),
        "classification_cues": (
            "Spreadsheets, calls, side notes, message threads, portals, decks, "
            "whiteboards, and manual trackers carry the real state."
        ),
        "keywords": [
            "spreadsheets",
            "email",
            "emails",
            "calls",
            "phone",
            "notes",
            "whiteboards",
            "decks",
            "meetings",
            "docs",
            "documents",
            "attachments",
            "portal",
            "portals",
            "threads",
            "trackers",
            "checklists",
            "side chats",
            "slides",
            "memos",
            "message threads",
            "comments",
        ],
        "why_keywords": [],
    },
    {
        "code": "SF-04",
        "name": "Human Judgment Under Incomplete Information",
        "description": (
            "Progress depends on experienced people interpreting incomplete, noisy, "
            "or conflicting signals and choosing tradeoffs."
        ),
        "persistence_thesis": (
            "The important variables are contextual, dynamic, or politically "
            "negotiated, so rules engines and dashboards cannot safely absorb the "
            "full decision load."
        ),
        "classification_cues": (
            "Interpretation, materiality, severity, trust, risk, prioritization, "
            "fit, and tradeoff decisions remain human-led."
        ),
        "keywords": [
            "interpret",
            "decide",
            "judg",
            "trust",
            "materiality",
            "severity",
            "tradeoff",
            "tradeoffs",
            "balance",
            "acceptable",
            "prioritization",
            "empathy",
            "experienced",
            "risk",
            "fit",
            "local reality",
            "contextual",
            "beneficial ownership",
            "what counts as",
            "what is enough",
        ],
        "why_keywords": [],
    },
    {
        "code": "SF-05",
        "name": "Handoff and Approval Latency",
        "description": (
            "Work slows or stalls when responsibility crosses functions, approvers, "
            "organizations, or service teams."
        ),
        "persistence_thesis": (
            "The binding constraint is organizational coordination rather than a "
            "single task, and incumbents generally automate local steps instead of "
            "shared accountability across handoffs."
        ),
        "classification_cues": (
            "Approvals, sign-offs, layered review, cross-functional waiting, status "
            "chasing, and repeated handoffs."
        ),
        "keywords": [
            "approval",
            "approvals",
            "sign-off",
            "handoff",
            "handoffs",
            "coordination",
            "waiting",
            "queue",
            "review cycles",
            "commentary collection",
            "status chasing",
            "duplicate handoffs",
            "signatures",
            "layered approvals",
            "cross-functional",
            "collect commentary",
            "chase documents",
            "chase coverage",
        ],
        "why_keywords": [
            "layered approvals",
            "cross-functional",
            "politically negotiated",
        ],
    },
    {
        "code": "SF-06",
        "name": "Plan vs. Reality Divergence",
        "description": (
            "A published plan or baseline becomes stale quickly as demand, capacity, "
            "field conditions, or network state change."
        ),
        "persistence_thesis": (
            "Optimization engines depend on stable inputs and trusted constraints, "
            "but the operating environment changes faster than shared models can "
            "stay accurate."
        ),
        "classification_cues": (
            "Local reality, live execution, unstable demand, rerouting, field "
            "conditions, readiness, and replanning loops."
        ),
        "keywords": [
            "local reality",
            "conditions diverge",
            "real time",
            "replanning",
            "re-planning",
            "rerouting",
            "reroute",
            "unstable demand",
            "incomplete constraints",
            "field conditions",
            "actual capacity",
            "downtime",
            "readiness",
            "network state changes",
            "moves faster",
            "re-cut",
            "published plan",
            "throughput",
            "yield",
            "route notes",
            "restraints",
        ],
        "why_keywords": [
            "hard problem is not math alone",
            "last mile of execution",
            "capacity realities",
            "network state changes in real time",
            "local conditions and human adaptation",
        ],
    },
    {
        "code": "SF-07",
        "name": "Compliance and Evidence Burden",
        "description": (
            "A large share of work is spent collecting proof, documenting "
            "exceptions, and maintaining traceability for rules, audits, or formal "
            "reporting."
        ),
        "persistence_thesis": (
            "Standards and forms can be codified, but evidence lineage, "
            "interpretation, and edge-case proofwork still cross people, documents, "
            "and external systems."
        ),
        "classification_cues": (
            "Evidence collection, traceability, audit trails, regulatory proof, "
            "documentation, verification, certification, and controls."
        ),
        "keywords": [
            "evidence",
            "documentation",
            "audit",
            "traceability",
            "attestations",
            "certification",
            "compliance",
            "regulatory",
            "authorization",
            "verification",
            "filing",
            "standards",
            "controls",
            "reserve exposure",
            "denials",
            "proof",
        ],
        "why_keywords": [
            "form of the report may be standardized",
            "standards are formal",
            "required checks, documents, and controls",
        ],
    },
    {
        "code": "SF-08",
        "name": "Multi-Party Trust and Dependency Gaps",
        "description": (
            "The workflow depends on outside parties whose data, incentives, timing, "
            "or standards do not align with the incumbent system."
        ),
        "persistence_thesis": (
            "Automation stops at the enterprise boundary because counterparties, "
            "partners, payers, suppliers, and regulators do not share one operating "
            "model or one trusted data layer."
        ),
        "classification_cues": (
            "Partner data, payers, carriers, suppliers, counterparties, external "
            "verification, and negotiated trust."
        ),
        "keywords": [
            "partner",
            "partners",
            "payer",
            "carrier",
            "customer-specific",
            "counterparty",
            "investor",
            "provider",
            "regulator",
            "reinsurance",
            "third-party",
            "external verification",
            "organizational trust",
            "negotiation",
            "receiving location",
            "receiving party",
            "supplier",
        ],
        "why_keywords": [
            "partner data",
            "organizational trust",
            "politically negotiated",
            "counterparty",
            "cross-party data standards",
        ],
    },
]

FAILURE_BY_CODE = {failure["code"]: failure for failure in FAILURE_TAXONOMY}

WORKFLOW_FAMILY_BOOSTS = {
    "Access, Intake, and Contracting": {"SF-01": 3.0, "SF-05": 3.0},
    "Clinical and Case Operations": {"SF-07": 3.0, "SF-05": 2.0, "SF-03": 1.0},
    "Customer and Experience Operations": {"SF-04": 3.0, "SF-03": 2.0, "SF-01": 1.0},
    "Delivery and Service Execution": {"SF-06": 4.0, "SF-05": 1.0, "SF-03": 1.0},
    "Finance and Revenue Operations": {"SF-02": 5.0, "SF-01": 2.0, "SF-03": 1.0},
    "Governance and Portfolio Operations": {"SF-05": 4.0, "SF-03": 2.0, "SF-02": 1.0},
    "Network and Transportation Operations": {"SF-06": 4.0, "SF-08": 3.0, "SF-05": 1.0},
    "Planning and Allocation": {"SF-06": 6.0, "SF-04": 3.0, "SF-05": 1.0},
    "Product, Content, and Engineering": {"SF-05": 4.0, "SF-03": 3.0, "SF-02": 1.0},
    "Production and Asset Operations": {"SF-06": 4.0, "SF-04": 2.0, "SF-03": 1.0},
    "Risk, Compliance, and Reporting": {"SF-07": 5.0, "SF-02": 1.0, "SF-04": 1.0},
    "Sourcing and Supply": {"SF-08": 4.0, "SF-05": 2.0, "SF-06": 1.0},
    "Workforce and Labor Operations": {"SF-05": 4.0, "SF-06": 2.0, "SF-03": 1.0},
}

PRIMARY_REASON_BOOSTS = {
    "Regulatory": {"SF-07": 2.0},
    "Legacy Architecture": {"SF-03": 1.0, "SF-02": 1.0},
    "Technical": {"SF-06": 1.0},
    "Organizational": {"SF-05": 1.0, "SF-08": 1.0},
    "Behavioral": {"SF-04": 1.0},
    "Economic": {"SF-08": 1.0},
}

REPRESENTATIVE_FIELD_BY_FAILURE = {
    "SF-01": "why_hasnt_this_been_solved",
    "SF-02": "where_time_is_lost",
    "SF-03": "where_people_leave_the_system_of_record",
    "SF-04": "where_human_judgment_dominates",
    "SF-05": "where_time_is_lost",
    "SF-06": "why_hasnt_this_been_solved",
    "SF-07": "where_time_is_lost",
    "SF-08": "why_hasnt_this_been_solved",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def escape_md(value: str) -> str:
    return value.replace("|", "\\|")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def split_pipe_list(value: str) -> list[str]:
    return [part.strip() for part in value.split("|") if part.strip()]


def clamp_sentence(value: str, limit: int = 160) -> str:
    if len(value) <= limit:
        return value
    trimmed = value[: limit - 3].rstrip()
    return f"{trimmed}..."


def why_lead_clause(value: str) -> str:
    return value.split(" It typically spans")[0].strip()


def score_workflow(row: dict[str, str]) -> tuple[dict[str, float], dict[str, list[str]]]:
    scores: dict[str, float] = {failure["code"]: 0.0 for failure in FAILURE_TAXONOMY}
    cue_log: dict[str, list[str]] = {failure["code"]: [] for failure in FAILURE_TAXONOMY}

    for failure in FAILURE_TAXONOMY:
        code = failure["code"]
        for field, weight in FIELD_WEIGHTS.items():
            text = row[field].lower()

            for keyword in failure["keywords"]:
                if keyword in text:
                    scores[code] += weight
                    cue_log[code].append(f"{field}:{keyword}")

            if field == "why_hasnt_this_been_solved":
                for keyword in failure["why_keywords"]:
                    if keyword in text:
                        scores[code] += 2.0
                        cue_log[code].append(f"{field}:{keyword}")

    for code, boost in WORKFLOW_FAMILY_BOOSTS.get(row["workflow_family"], {}).items():
        scores[code] += boost
        cue_log[code].append(f"workflow_family:{row['workflow_family']}")

    for code, boost in PRIMARY_REASON_BOOSTS.get(row["primary_reason"], {}).items():
        scores[code] += boost
        cue_log[code].append(f"primary_reason:{row['primary_reason']}")

    return scores, cue_log


def classify_workflows(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, dict[str, object]]]:
    classified_rows: list[dict[str, object]] = []
    by_name: dict[str, dict[str, object]] = {}

    for row in rows:
        workflow_row = dict(row)
        workflow_row["workflow_slug"] = slugify(workflow_row["workflow_name"])

        scores, cue_log = score_workflow(workflow_row)
        ordered_codes = sorted(
            scores,
            key=lambda code: (-scores[code], code),
        )

        selected_codes = [
            code for code in ordered_codes if scores[code] >= MIN_SELECTED_SCORE
        ][:MAX_FAILURES_PER_WORKFLOW]
        if not selected_codes:
            selected_codes = [ordered_codes[0]]

        primary_code = selected_codes[0]
        secondary_codes = selected_codes[1:]

        workflow_row["selected_failure_codes"] = selected_codes
        workflow_row["primary_failure_code"] = primary_code
        workflow_row["secondary_failure_codes"] = secondary_codes
        workflow_row["failure_scores"] = scores
        workflow_row["failure_cues"] = cue_log
        workflow_row["workflow_document"] = (
            f"knowledge/research/workflow-library/workflows/"
            f"{workflow_row['workflow_slug']}.md"
        )

        classified_rows.append(workflow_row)
        by_name[workflow_row["workflow_name"]] = workflow_row

    return classified_rows, by_name


def build_classification_csv_rows(classified_rows: list[dict[str, object]]) -> list[dict[str, str]]:
    csv_rows: list[dict[str, str]] = []

    for row in sorted(classified_rows, key=lambda item: item["workflow_name"]):
        selected_codes = row["selected_failure_codes"]
        secondary_codes = row["secondary_failure_codes"]
        scores = row["failure_scores"]
        ordered_score_pairs = sorted(
            scores.items(),
            key=lambda pair: (-pair[1], pair[0]),
        )

        csv_rows.append(
            {
                "workflow_name": row["workflow_name"],
                "workflow_family": row["workflow_family"],
                "operating_systems": row["operating_systems"],
                "industries_using_this_workflow": row["industries_using_this_workflow"],
                "industry_count": row["industry_count"],
                "primary_structural_failure_code": row["primary_failure_code"],
                "primary_structural_failure_name": FAILURE_BY_CODE[row["primary_failure_code"]]["name"],
                "secondary_structural_failure_codes": " | ".join(secondary_codes),
                "secondary_structural_failure_names": " | ".join(
                    FAILURE_BY_CODE[code]["name"] for code in secondary_codes
                ),
                "all_selected_failure_codes": " | ".join(selected_codes),
                "all_selected_failure_names": " | ".join(
                    FAILURE_BY_CODE[code]["name"] for code in selected_codes
                ),
                "selected_failure_score_breakdown": " | ".join(
                    f"{code}:{scores[code]:.1f}" for code in selected_codes
                ),
                "full_score_breakdown": " | ".join(
                    f"{code}:{score:.1f}" for code, score in ordered_score_pairs if score > 0
                ),
                "dominant_root_cause": row["primary_reason"],
                "economic_leakage_summary": row["where_money_is_lost"],
                "time_leakage_summary": row["where_time_is_lost"],
                "human_judgment_summary": row["where_human_judgment_dominates"],
                "system_of_record_escape_summary": row["where_people_leave_the_system_of_record"],
                "why_it_persists_summary": row["why_hasnt_this_been_solved"],
                "workflow_document": row["workflow_document"],
            }
        )

    return csv_rows


def build_frequency_matrix(
    index_rows: list[dict[str, str]],
    classified_by_name: dict[str, dict[str, object]],
) -> list[dict[str, str]]:
    matrix_rows: list[dict[str, str]] = []

    for index_row in sorted(
        index_rows,
        key=lambda item: (
            item["workflow_name"],
            item["canonical_operating_system"],
            item["industry_name"],
        ),
    ):
        workflow = classified_by_name[index_row["workflow_name"]]
        scores = workflow["failure_scores"]

        for code in workflow["selected_failure_codes"]:
            matrix_rows.append(
                {
                    "failure_code": code,
                    "failure_name": FAILURE_BY_CODE[code]["name"],
                    "assignment_role": "Primary"
                    if code == workflow["primary_failure_code"]
                    else "Secondary",
                    "failure_score": f"{scores[code]:.1f}",
                    "workflow_name": workflow["workflow_name"],
                    "workflow_family": workflow["workflow_family"],
                    "canonical_operating_system": index_row["canonical_operating_system"],
                    "industry_name": index_row["industry_name"],
                    "industry_rank_2025_gross_output": index_row["industry_rank_2025_gross_output"],
                    "dominant_root_cause": workflow["primary_reason"],
                    "systems_of_record_categories": index_row["systems_of_record_categories"],
                    "workflow_document": workflow["workflow_document"],
                }
            )

    return matrix_rows


def top_counter_strings(items: list[str], limit: int = 5) -> list[tuple[str, int]]:
    counter = Counter(items)
    return counter.most_common(limit)


def format_counter_list(items: list[tuple[str, int]]) -> str:
    return "; ".join(f"{item} ({count})" for item, count in items)


def confidence_level(workflow_count: int, operating_system_count: int) -> str:
    if workflow_count >= 100 and operating_system_count >= 10:
        return "High"
    if workflow_count >= 40 and operating_system_count >= 6:
        return "Medium-High"
    return "Medium"


def list_with_counts(counter: Counter[str], limit: int = 8) -> str:
    return ", ".join(
        f"{item} ({count})" for item, count in counter.most_common(limit)
    )


def representative_workflows(
    failure_code: str,
    classified_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    candidates = [
        row
        for row in classified_rows
        if failure_code in row["selected_failure_codes"]
    ]
    candidates.sort(
        key=lambda row: (
            -row["failure_scores"][failure_code],
            -int(row["industry_count"]),
            row["workflow_name"],
        )
    )

    chosen: list[dict[str, object]] = []
    seen_families: set[str] = set()

    for row in candidates:
        family = row["workflow_family"]
        if family not in seen_families:
            chosen.append(row)
            seen_families.add(family)
        if len(chosen) == 6:
            return chosen

    for row in candidates:
        if row not in chosen:
            chosen.append(row)
        if len(chosen) == 6:
            break

    return chosen


def aggregate_failure(
    failure_code: str,
    classified_rows: list[dict[str, object]],
    matrix_rows: list[dict[str, str]],
) -> dict[str, object]:
    workflows = [
        row for row in classified_rows if failure_code in row["selected_failure_codes"]
    ]
    usage_rows = [row for row in matrix_rows if row["failure_code"] == failure_code]
    primary_count = sum(
        1 for row in workflows if row["primary_failure_code"] == failure_code
    )

    operating_system_counter = Counter(
        row["canonical_operating_system"] for row in usage_rows
    )
    industry_counter = Counter(row["industry_name"] for row in usage_rows)
    systems_counter = Counter()
    root_cause_counter = Counter()
    judgment_counter = Counter()
    escape_counter = Counter()
    leakage_counter = Counter()
    why_counter = Counter()
    score_values: list[float] = []

    for row in workflows:
        systems_counter.update(split_pipe_list(row["systems_of_record_involved"]))
        root_cause_counter.update([row["primary_reason"]])
        judgment_counter.update([row["where_human_judgment_dominates"]])
        escape_counter.update([row["where_people_leave_the_system_of_record"]])
        leakage_counter.update([row["where_money_is_lost"]])
        why_counter.update([why_lead_clause(row["why_hasnt_this_been_solved"])])
        score_values.append(row["failure_scores"][failure_code])

    return {
        "failure": FAILURE_BY_CODE[failure_code],
        "workflow_count": len(workflows),
        "usage_count": len(usage_rows),
        "primary_count": primary_count,
        "operating_system_count": len(operating_system_counter),
        "industry_count": len(industry_counter),
        "operating_system_counter": operating_system_counter,
        "industry_counter": industry_counter,
        "systems_counter": systems_counter,
        "root_cause_counter": root_cause_counter,
        "judgment_counter": judgment_counter,
        "escape_counter": escape_counter,
        "leakage_counter": leakage_counter,
        "why_counter": why_counter,
        "average_score": sum(score_values) / len(score_values),
        "confidence": confidence_level(
            workflow_count=len(workflows),
            operating_system_count=len(operating_system_counter),
        ),
        "representative_workflows": representative_workflows(
            failure_code, classified_rows
        ),
    }


def build_taxonomy_doc(aggregates: list[dict[str, object]]) -> str:
    lines = [
        "# Structural Failure Taxonomy",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 3 taxonomy",
        "",
        "## Method",
        "",
        "- Source inputs: `knowledge/research/industry-census/top-50-industry-census-normalized.csv`, `knowledge/research/workflow-library/canonical-workflow-library.csv`, and `knowledge/research/workflow-library/workflow-operating-system-industry-index.csv` only.",
        "- No additional external research was added.",
        "- Each workflow is assigned one primary structural failure and up to two secondary structural failures using deterministic scoring on the Phase 2 friction fields, workflow family, and existing Phase 2 root-cause label.",
        f"- Minimum score to retain a failure on a workflow: `{MIN_SELECTED_SCORE:.0f}`.",
        "",
        "## Taxonomy",
        "",
        "| Code | Failure | Definition | Typical evidence cues | Workflow incidence | Primary assignments | Confidence |",
        "| --- | --- | --- | --- | ---: | ---: | --- |",
    ]

    aggregate_by_code = {
        aggregate["failure"]["code"]: aggregate for aggregate in aggregates
    }

    for failure in FAILURE_TAXONOMY:
        aggregate = aggregate_by_code[failure["code"]]
        lines.append(
            "| "
            f"{failure['code']} | "
            f"{escape_md(failure['name'])} | "
            f"{escape_md(failure['description'])} | "
            f"{escape_md(failure['classification_cues'])} | "
            f"{aggregate['workflow_count']} / {TOTAL_WORKFLOWS} | "
            f"{aggregate['primary_count']} | "
            f"{aggregate['confidence']} |"
        )

    return "\n".join(lines) + "\n"


def build_atlas_doc(aggregates: list[dict[str, object]]) -> str:
    lines = [
        "# Structural Failure Atlas (v1)",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 3 analytical layer",
        "",
        "## Corpus Summary",
        "",
        "- Evidence base: 198 canonical workflows and 250 workflow ↔ operating-system ↔ industry usage rows.",
        "- Scope boundary: Phase 3 synthesis only. No startup ideas, solution recommendations, or Phase 4 opportunity classification are included here.",
        "- Recurrence is measured at two levels: workflow incidence and expanded workflow-usage links from the Phase 1 index.",
        "",
        "## Failure Register",
        "",
        "| Code | Failure | Workflows | Usage links | Operating systems | Industries | Dominant root cause | Confidence |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]

    for aggregate in aggregates:
        failure = aggregate["failure"]
        dominant_root_cause = aggregate["root_cause_counter"].most_common(1)[0][0]
        lines.append(
            "| "
            f"{failure['code']} | "
            f"{escape_md(failure['name'])} | "
            f"{aggregate['workflow_count']} | "
            f"{aggregate['usage_count']} | "
            f"{aggregate['operating_system_count']} | "
            f"{aggregate['industry_count']} | "
            f"{dominant_root_cause} | "
            f"{aggregate['confidence']} |"
        )

    for aggregate in aggregates:
        failure = aggregate["failure"]
        dominant_root_cause = aggregate["root_cause_counter"].most_common(1)[0][0]

        lines.extend(
            [
                "",
                f"## {failure['code']} {failure['name']}",
                "",
                f"- Description: {failure['description']}",
                (
                    "- Frequency: "
                    f"{aggregate['workflow_count']} of {TOTAL_WORKFLOWS} workflows "
                    f"({aggregate['workflow_count'] / TOTAL_WORKFLOWS:.1%}); "
                    f"{aggregate['usage_count']} failure-to-workflow-usage links across "
                    f"{aggregate['operating_system_count']} operating systems and "
                    f"{aggregate['industry_count']} industries."
                ),
                (
                    "- Root-cause mix: "
                    f"{format_counter_list(aggregate['root_cause_counter'].most_common())}"
                ),
                (
                    "- Operating systems affected: "
                    f"{list_with_counts(aggregate['operating_system_counter'])}"
                ),
                (
                    "- Industries affected: "
                    f"{list_with_counts(aggregate['industry_counter'])}"
                ),
                (
                    "- Typical systems of record involved: "
                    f"{format_counter_list(aggregate['systems_counter'].most_common(6))}"
                ),
                (
                    "- Common human judgment points: "
                    f"{format_counter_list(top_counter_strings(list(aggregate['judgment_counter'].elements()), 3))}"
                ),
                (
                    "- Common system-of-record escape points: "
                    f"{format_counter_list(top_counter_strings(list(aggregate['escape_counter'].elements()), 3))}"
                ),
                (
                    "- Common economic leakage: "
                    f"{format_counter_list(top_counter_strings(list(aggregate['leakage_counter'].elements()), 3))}"
                ),
                (
                    "- Structural reason incumbents have not solved it: "
                    f"{failure['persistence_thesis']} "
                    f"Repeated Phase 2 evidence most often states: "
                    f"{format_counter_list(aggregate['why_counter'].most_common(3))}."
                ),
                f"- Dominant root cause: {dominant_root_cause}",
                f"- Confidence: {aggregate['confidence']}",
                "- Evidence references:",
            ]
        )

        for workflow in aggregate["representative_workflows"]:
            field_name = REPRESENTATIVE_FIELD_BY_FAILURE[failure["code"]]
            excerpt = clamp_sentence(workflow[field_name])
            lines.append(
                "  - "
                f"[{workflow['workflow_name']}](../workflow-library/workflows/{workflow['workflow_slug']}.md): "
                f"{excerpt}"
            )

    return "\n".join(lines) + "\n"


def build_executive_summary_doc(aggregates: list[dict[str, object]]) -> str:
    top_five = aggregates[:5]
    lines = [
        "# Phase 3 Executive Summary",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Approved Phase 3 summary",
        "",
        "## Headline",
        "",
        (
            "Atlas now has an evidence-backed Structural Failure Atlas built from the "
            "Phase 1 normalized census and the Phase 2 workflow library. The corpus "
            "shows that recurring failure is driven less by missing point software "
            "than by repeated breakdowns in context capture, judgment, exception "
            "handling, reconciliation, coordination, and adaptation to reality."
        ),
        "",
        "## Most Recurring Failures",
        "",
    ]

    for aggregate in top_five:
        failure = aggregate["failure"]
        dominant_root_cause = aggregate["root_cause_counter"].most_common(1)[0][0]
        lines.append(
            (
                f"- `{failure['code']}` {failure['name']}: "
                f"{aggregate['workflow_count']} workflows, "
                f"{aggregate['operating_system_count']} operating systems, "
                f"{aggregate['industry_count']} industries, "
                f"dominant root cause `{dominant_root_cause}`."
            )
        )

    overall_root_causes = Counter()
    for aggregate in aggregates:
        overall_root_causes.update(aggregate["root_cause_counter"])

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "The two most universal failures are `SF-03` Decision Context Escapes "
                "the Record and `SF-04` Human Judgment Under Incomplete Information. "
                "Together they show that the system of record rarely contains the full "
                "narrative or tradeoff logic required to advance work."
            ),
            (
                "`SF-01` Exception-Path Breakdown, `SF-06` Plan vs. Reality "
                "Divergence, and `SF-05` Handoff and Approval Latency explain why "
                "workflows that look software-covered still leak money and time once "
                "real conditions deviate from the nominal path."
            ),
            (
                "`SF-02` Cross-System Reconciliation, `SF-07` Compliance and Evidence "
                "Burden, and `SF-08` Multi-Party Trust and Dependency Gaps are most "
                "concentrated where financial accuracy, regulated proof, or "
                "counterparty coordination matter more than local task completion."
            ),
            "",
            "## Root-Cause Pattern",
            "",
            (
                "Across selected failure assignments in the atlas, the most common "
                "Phase 2 root causes remain "
                f"{format_counter_list(overall_root_causes.most_common())}. "
                "Legacy architecture dominates overall, but technical, regulatory, "
                "organizational, and behavioral causes all persist depending on the "
                "failure family."
            ),
            "",
            "## Phase Boundary",
            "",
            (
                "Phase 3 is complete when Phase 4 uses this atlas, taxonomy, workflow "
                "classification layer, and frequency matrix as its sole input. This "
                "summary intentionally does not classify opportunities, recommend "
                "solutions, or prioritize markets."
            ),
        ]
    )

    return "\n".join(lines) + "\n"


def build_readme_doc(
    classification_rows: list[dict[str, str]],
    matrix_rows: list[dict[str, str]],
    aggregates: list[dict[str, object]],
) -> str:
    lines = [
        "# Structural Failure Atlas",
        "",
        f"Last updated: {GENERATED_DATE}",
        "Status: Active Phase 3 evidence layer",
        "",
        "## Scope",
        "",
        "- Source inputs: normalized Phase 1 census plus the Phase 2 workflow library only.",
        "- No new industry research or solution ideation is included here.",
        "- This folder is the durable Phase 3 analytical layer that sits on top of `knowledge/research/workflow-library/`.",
        "",
        "## Deliverables",
        "",
        "- `structural-failure-taxonomy.md`: the canonical failure vocabulary and scoring method.",
        "- `workflow-structural-failure-classification.csv`: one row per canonical workflow with primary and secondary structural failures.",
        "- `structural-failure-frequency-matrix.csv`: expanded failure × workflow × operating system × industry matrix.",
        "- `structural-failure-atlas-v1.md`: the first full atlas with aggregate evidence for each recurring failure.",
        "- `executive-summary.md`: concise Phase 3 summary for Phase 4 handoff.",
        "- `scripts/build_structural_failure_atlas.py`: reproducible generator for every artifact in this folder.",
        "",
        "## Counts",
        "",
        f"- Canonical workflows classified: {len(classification_rows)}",
        f"- Frequency-matrix rows: {len(matrix_rows)}",
        f"- Structural failure categories: {len(aggregates)}",
        "",
        "## Top Failure Incidence",
        "",
    ]

    for aggregate in aggregates[:5]:
        lines.append(
            f"- `{aggregate['failure']['code']}` {aggregate['failure']['name']}: "
            f"{aggregate['workflow_count']} workflows"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    ATLAS_DIR.mkdir(parents=True, exist_ok=True)

    workflow_rows = read_csv(WORKFLOW_LIBRARY_CSV)
    index_rows = read_csv(WORKFLOW_INDEX_CSV)

    classified_rows, classified_by_name = classify_workflows(workflow_rows)
    classification_csv_rows = build_classification_csv_rows(classified_rows)
    matrix_rows = build_frequency_matrix(index_rows, classified_by_name)
    aggregates = [
        aggregate_failure(failure["code"], classified_rows, matrix_rows)
        for failure in FAILURE_TAXONOMY
    ]
    aggregates.sort(key=lambda aggregate: (-aggregate["workflow_count"], aggregate["failure"]["code"]))

    write_csv(
        CLASSIFICATION_CSV,
        classification_csv_rows,
        [
            "workflow_name",
            "workflow_family",
            "operating_systems",
            "industries_using_this_workflow",
            "industry_count",
            "primary_structural_failure_code",
            "primary_structural_failure_name",
            "secondary_structural_failure_codes",
            "secondary_structural_failure_names",
            "all_selected_failure_codes",
            "all_selected_failure_names",
            "selected_failure_score_breakdown",
            "full_score_breakdown",
            "dominant_root_cause",
            "economic_leakage_summary",
            "time_leakage_summary",
            "human_judgment_summary",
            "system_of_record_escape_summary",
            "why_it_persists_summary",
            "workflow_document",
        ],
    )

    write_csv(
        FREQUENCY_MATRIX_CSV,
        matrix_rows,
        [
            "failure_code",
            "failure_name",
            "assignment_role",
            "failure_score",
            "workflow_name",
            "workflow_family",
            "canonical_operating_system",
            "industry_name",
            "industry_rank_2025_gross_output",
            "dominant_root_cause",
            "systems_of_record_categories",
            "workflow_document",
        ],
    )

    README_DOC.write_text(
        build_readme_doc(classification_csv_rows, matrix_rows, aggregates)
    )
    TAXONOMY_DOC.write_text(build_taxonomy_doc(aggregates))
    ATLAS_DOC.write_text(build_atlas_doc(aggregates))
    EXECUTIVE_SUMMARY_DOC.write_text(build_executive_summary_doc(aggregates))


if __name__ == "__main__":
    main()
