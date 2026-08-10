#!/usr/bin/env python3

import csv
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALUE_PATTERN_MAP_PATH = (
    REPO_ROOT / "opportunity-engine" / "value-patterns" / "value_pattern_map.csv"
)
OUTPUT_DIR = REPO_ROOT / "opportunity-engine" / "opportunity-families"
MAP_PATH = OUTPUT_DIR / "opportunity_family_map.csv"
SUMMARY_PATH = OUTPUT_DIR / "opportunity_family_summary.md"


FAMILY_ORDER = [
    {
        "id": "OF-001",
        "name": "Operational Execution Infrastructure",
        "patterns": [
            {"id": "VP-001", "name": "Workflow Compression"},
            {"id": "VP-003", "name": "Memory Infrastructure"},
        ],
        "primitives": ["Coordinate", "Remember"],
        "definition": (
            "Systems that reduce recurring operating drag by compressing handoffs "
            "and preserving reusable context across multi-step work."
        ),
        "engine": (
            "Convert fragmented execution and lost context into faster cycle "
            "times, lower coordination overhead, and more repeatable operating "
            "throughput."
        ),
        "boundary": (
            "Use this family when the core wedge is smoother recurring execution. "
            "If the primary value is better pre-commitment judgment, market "
            "matching, or capability compounding, use a different family."
        ),
        "revenue_thesis": (
            "Best wedges monetize as workflow systems, operating copilots, or "
            "memory layers priced against time saved, throughput gained, or "
            "avoided coordination headcount."
        ),
        "next_validation": (
            "Identify one high-frequency multi-step workflow where coordination "
            "and context loss create measurable cycle-time drag, then compare "
            "incumbent tooling and switching pain."
        ),
    },
    {
        "id": "OF-002",
        "name": "Decision and Foresight Infrastructure",
        "patterns": [
            {"id": "VP-002", "name": "Decision Advantage"},
            {"id": "VP-008", "name": "Pre-Commitment Foresight"},
        ],
        "primitives": ["Optimize", "Predict", "Simulate"],
        "definition": (
            "Systems that improve high-stakes decisions before time, capital, or "
            "trust are committed."
        ),
        "engine": (
            "Raise judgment quality and reduce irreversible mistakes by turning "
            "weak signals, tradeoffs, and scenario uncertainty into clearer "
            "pre-commitment choices."
        ),
        "boundary": (
            "Use this family when the primary value comes from better choices "
            "before action. If the wedge is ongoing execution throughput or "
            "post-decision adaptation, use a different family."
        ),
        "revenue_thesis": (
            "Best wedges monetize where wrong decisions are expensive, via "
            "decision support, simulation, and planning systems priced against "
            "margin preservation, risk reduction, or faster strategic cycles."
        ),
        "next_validation": (
            "Pick one decision workflow with clear downside from delay or error, "
            "then quantify the current cost of missed tradeoffs, manual analysis, "
            "and low-confidence forecasting."
        ),
    },
    {
        "id": "OF-003",
        "name": "Trust and Adaptive Governance",
        "patterns": [
            {"id": "VP-004", "name": "Trust Infrastructure"},
            {"id": "VP-009", "name": "Adaptive Control"},
        ],
        "primitives": ["Verify", "Adapt"],
        "definition": (
            "Systems that keep organizations, networks, or institutions credible "
            "and aligned as conditions change."
        ),
        "engine": (
            "Lower the cost of action under uncertainty by combining verification, "
            "readiness, and continuous re-alignment instead of static governance."
        ),
        "boundary": (
            "Use this family when the wedge depends on proof, compliance, "
            "readiness, or re-tuning under change. If value mainly comes from "
            "discovery, matching, or capability accumulation, use a different family."
        ),
        "revenue_thesis": (
            "Best wedges monetize through risk, compliance, readiness, or "
            "resilience budgets where customers already pay to avoid failure, "
            "regulatory pain, or system drift."
        ),
        "next_validation": (
            "Find one domain where trust or governance friction blocks action, "
            "then test whether verification alone is insufficient without a "
            "continuous adaptation layer."
        ),
    },
    {
        "id": "OF-004",
        "name": "Discovery and Liquidity Networks",
        "patterns": [
            {"id": "VP-005", "name": "Matching Liquidity"},
            {"id": "VP-006", "name": "Opportunity Surface Expansion"},
        ],
        "primitives": ["Match", "Discover"],
        "definition": (
            "Systems that widen the visible option set and route scarce resources "
            "toward better matches."
        ),
        "engine": (
            "Create upside by increasing what the user can see and lowering the "
            "search friction required to turn discovery into allocation."
        ),
        "boundary": (
            "Use this family when value comes from search breadth, routing, or "
            "match quality. If the wedge depends mainly on operational throughput "
            "or post-match compounding, use a different family."
        ),
        "revenue_thesis": (
            "Best wedges monetize through access fees, transaction take rates, "
            "or workflow subscriptions tied to higher fill-rate, better deal flow, "
            "or improved utilization."
        ),
        "next_validation": (
            "Choose one constrained market or workflow where search friction is "
            "visible, then test whether better discovery actually improves match "
            "quality and conversion, not just lead volume."
        ),
    },
    {
        "id": "OF-005",
        "name": "Capability Capital Platforms",
        "patterns": [
            {"id": "VP-007", "name": "Compounding Loops"},
            {"id": "VP-010", "name": "Assetization Engines"},
        ],
        "primitives": ["Compound", "Learn", "Create"],
        "definition": (
            "Systems that turn repeated use, learning, and creation into reusable "
            "capability or intellectual capital."
        ),
        "engine": (
            "Build durable leverage by ensuring each cycle leaves behind skills, "
            "assets, or operating capital that makes the next cycle stronger."
        ),
        "boundary": (
            "Use this family when the wedge gets stronger with repeated use or "
            "asset accumulation. If value is mostly one-time execution, a different "
            "family is a better fit."
        ),
        "revenue_thesis": (
            "Best wedges monetize through recurring subscriptions, asset-marketplace "
            "economics, or productivity capture where retained gains compound for "
            "the customer over time."
        ),
        "next_validation": (
            "Find one workflow where repeated use clearly improves outcomes, then "
            "test whether the system retains reusable knowledge or assets that "
            "customers would pay to keep compounding."
        ),
    },
]


FAMILY_BY_PATTERN_ID = {}
for family in FAMILY_ORDER:
    for pattern in family["patterns"]:
        FAMILY_BY_PATTERN_ID[pattern["id"]] = family


def load_rows():
    with VALUE_PATTERN_MAP_PATH.open(newline="") as handle:
        return list(csv.DictReader(handle))


def flag_list(review_flags):
    if not review_flags or review_flags == "None":
        return []
    return [flag.strip() for flag in review_flags.split(";") if flag.strip()]


def enrich_rows(rows):
    enriched = []
    for row in rows:
        family = FAMILY_BY_PATTERN_ID.get(row["Value Pattern ID"])
        if not family:
            raise ValueError(f"Unmapped value pattern: {row['Value Pattern ID']}")

        enriched.append(
            {
                "Concept ID": row["Concept ID"],
                "Concept Title": row["Concept Title"],
                "Primitive": row["Primitive"],
                "Canonical Job": row["Canonical Job"],
                "Domain": row["Domain"],
                "Customer": row["Customer"],
                "Confidence": row["Confidence"],
                "Evidence": row["Evidence"],
                "Value Pattern ID": row["Value Pattern ID"],
                "Value Pattern": row["Value Pattern"],
                "Pattern Mechanism": row["Pattern Mechanism"],
                "Opportunity Family ID": family["id"],
                "Opportunity Family": family["name"],
                "Family Rule Basis": (
                    f"Value Pattern {row['Value Pattern ID']} {row['Value Pattern']} "
                    f"-> {family['name']}"
                ),
                "Family Value Engine": family["engine"],
                "Related Value Patterns": ", ".join(
                    f"{pattern['id']} {pattern['name']}"
                    for pattern in family["patterns"]
                ),
                "Review Flags": row["Review Flags"],
            }
        )
    return enriched


def write_map(enriched_rows):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = list(enriched_rows[0].keys())
    with MAP_PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_rows)


def sort_key(row):
    return (
        -int(row["Confidence"]),
        len(flag_list(row["Review Flags"])),
        row["Concept ID"],
    )


def representative_concepts(rows, family):
    by_pattern = defaultdict(list)
    for row in rows:
        by_pattern[row["Value Pattern ID"]].append(row)

    selected = []
    seen = set()

    for pattern in family["patterns"]:
        ranked = sorted(by_pattern[pattern["id"]], key=sort_key)
        for row in ranked[:2]:
            if row["Concept ID"] not in seen:
                selected.append(f"{row['Concept ID']} {row['Concept Title']}")
                seen.add(row["Concept ID"])

    if len(selected) < 4:
        ranked = sorted(rows, key=sort_key)
        for row in ranked:
            if row["Concept ID"] in seen:
                continue
            selected.append(f"{row['Concept ID']} {row['Concept Title']}")
            seen.add(row["Concept ID"])
            if len(selected) >= 4:
                break

    return selected[:4]


def summarize_families(enriched_rows):
    by_family = defaultdict(list)
    flag_counter = Counter()

    for row in enriched_rows:
        by_family[row["Opportunity Family ID"]].append(row)
        for flag in flag_list(row["Review Flags"]):
            flag_counter[flag] += 1

    lines = []
    lines.append("# Opportunity Family Summary")
    lines.append("")
    lines.append("Generated: 2026-08-06")
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Value-pattern rows classified: {len(enriched_rows)}")
    lines.append("- Unmapped rows: 0")
    lines.append(f"- Opportunity Family count: {len(FAMILY_ORDER)}")
    lines.append(
        "- Classification anchor: Value Pattern IDs from "
        "`opportunity-engine/value-patterns/value_pattern_map.csv`"
    )
    lines.append("")
    lines.append("## Family Distribution")
    lines.append("")
    lines.append(
        "| Opportunity Family | ID | Concepts | Related Value Patterns | Top Domains | Top Jobs |"
    )
    lines.append("| --- | --- | ---: | --- | --- | --- |")

    for family in FAMILY_ORDER:
        rows = by_family[family["id"]]
        domains = Counter(row["Domain"] for row in rows).most_common(3)
        jobs = Counter(row["Canonical Job"] for row in rows).most_common(3)
        domain_text = ", ".join(f"{name} ({count})" for name, count in domains)
        job_text = ", ".join(f"{name} ({count})" for name, count in jobs)
        pattern_text = ", ".join(
            f"{pattern['id']} {pattern['name']}" for pattern in family["patterns"]
        )
        lines.append(
            f"| {family['name']} | {family['id']} | {len(rows)} | {pattern_text} | "
            f"{domain_text} | {job_text} |"
        )

    lines.append("")
    lines.append("## Review Flag Counts")
    lines.append("")
    for flag, count in flag_counter.most_common():
        lines.append(f"- {flag}: {count}")

    lines.append("")
    lines.append("## Family Notes")
    lines.append("")

    for family in FAMILY_ORDER:
        rows = by_family[family["id"]]
        family_flags = Counter()
        for row in rows:
            for flag in flag_list(row["Review Flags"]):
                family_flags[flag] += 1

        representatives = ", ".join(representative_concepts(rows, family))
        lines.append(f"### {family['id']} {family['name']}")
        lines.append("")
        lines.append(f"- Definition: {family['definition']}")
        lines.append(f"- Value engine: {family['engine']}")
        lines.append(
            "- Related Value Patterns: "
            + ", ".join(
                f"{pattern['id']} {pattern['name']}" for pattern in family["patterns"]
            )
        )
        lines.append(f"- Revenue thesis: {family['revenue_thesis']}")
        lines.append(f"- Representative concepts: {representatives}")
        lines.append(
            "- Evidence gaps: "
            f"Why-now missing ({family_flags['Why-now missing']}), "
            f"low concept confidence ({family_flags['Low concept confidence']}), "
            f"broad initial wedge ({family_flags['Broad initial wedge']}), "
            f"primitive ambiguity ({family_flags['Primitive ambiguity']})."
        )
        lines.append(f"- Next validation step: {family['next_validation']}")
        lines.append("")

    with SUMMARY_PATH.open("w") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def main():
    rows = load_rows()
    enriched_rows = enrich_rows(rows)
    write_map(enriched_rows)
    summarize_families(enriched_rows)


if __name__ == "__main__":
    main()
