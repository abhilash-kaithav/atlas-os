#!/usr/bin/env python3

import csv
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CURATED_PATH = REPO_ROOT / "data" / "concepts_curated.csv"
OUTPUT_DIR = REPO_ROOT / "opportunity-engine" / "value-patterns"
MAP_PATH = OUTPUT_DIR / "value_pattern_map.csv"
SUMMARY_PATH = OUTPUT_DIR / "value_pattern_summary.md"


PATTERN_ORDER = [
    {
        "id": "VP-001",
        "name": "Workflow Compression",
        "primitives": ["Coordinate"],
        "definition": "Reduces handoffs and coordination drag so multi-step work moves faster across people, tools, or systems.",
        "mechanism": "Converts fragmented workflows into shorter cycle times, fewer stalls, and lower execution overhead.",
    },
    {
        "id": "VP-002",
        "name": "Decision Advantage",
        "primitives": ["Optimize"],
        "definition": "Turns noisy signals into better choices, tradeoffs, and negotiated outcomes before value leaks away.",
        "mechanism": "Improves the quality of prioritization and intervention decisions where mistakes or delays are expensive.",
    },
    {
        "id": "VP-003",
        "name": "Memory Infrastructure",
        "primitives": ["Remember"],
        "definition": "Makes prior context, rationale, and history reusable so future work does not restart from zero.",
        "mechanism": "Transforms past operating knowledge into future leverage by lowering search, reconstruction, and onboarding costs.",
    },
    {
        "id": "VP-004",
        "name": "Trust Infrastructure",
        "primitives": ["Verify"],
        "definition": "Produces proofs, checks, scores, or readiness signals that let people act with less uncertainty and lower error.",
        "mechanism": "Unlocks action by reducing the cost of validation, compliance, and quality assurance.",
    },
    {
        "id": "VP-005",
        "name": "Matching Liquidity",
        "primitives": ["Match"],
        "definition": "Connects the right people, assets, opportunities, or capacity at the right time.",
        "mechanism": "Creates value by lowering search friction and increasing utilization, fit, or fill-rate in a constrained network.",
    },
    {
        "id": "VP-006",
        "name": "Opportunity Surface Expansion",
        "primitives": ["Discover"],
        "definition": "Searches a wider option space than manual exploration and surfaces higher-value openings earlier.",
        "mechanism": "Creates upside by expanding the set of credible opportunities a team can see, compare, or pursue.",
    },
    {
        "id": "VP-007",
        "name": "Compounding Loops",
        "primitives": ["Compound", "Learn"],
        "definition": "Makes each cycle increase the value of the next through feedback, practice, retained gains, or cumulative capability.",
        "mechanism": "Creates durable value through repeated-use reinforcement rather than one-time task completion.",
    },
    {
        "id": "VP-008",
        "name": "Pre-Commitment Foresight",
        "primitives": ["Predict", "Simulate"],
        "definition": "Forecasts or tests outcomes before time, capital, or trust are committed in the real world.",
        "mechanism": "Creates value by reducing the cost of uncertainty before irreversible action is taken.",
    },
    {
        "id": "VP-009",
        "name": "Adaptive Control",
        "primitives": ["Adapt"],
        "definition": "Keeps plans, contracts, or operating systems aligned as conditions change.",
        "mechanism": "Preserves performance by continuously re-tuning decisions and structures instead of letting them drift out of date.",
    },
    {
        "id": "VP-010",
        "name": "Assetization Engines",
        "primitives": ["Create"],
        "definition": "Turns expertise, intent, or operating work into reusable assets that can be deployed repeatedly.",
        "mechanism": "Creates leverage by converting transient effort into reusable intellectual or operating capital.",
    },
]


PRIMITIVE_TO_PATTERN = {}
PATTERN_INDEX = {}
for pattern in PATTERN_ORDER:
    PATTERN_INDEX[pattern["name"]] = pattern
    for primitive in pattern["primitives"]:
        PRIMITIVE_TO_PATTERN[primitive] = pattern


def load_rows():
    with CURATED_PATH.open(newline="") as handle:
        return list(csv.DictReader(handle))


def flags_for_row(row):
    flags = []
    notes = row["Notes"] or ""

    try:
        if int(row["Confidence"]) <= 2:
            flags.append("Low concept confidence")
    except ValueError:
        flags.append("Missing confidence")

    if "Primitive required judgment" in notes:
        flags.append("Primitive ambiguity")
    if "Initial wedge remains broad" in notes:
        flags.append("Broad initial wedge")
    if "Why now was not explicit" in notes:
        flags.append("Why-now missing")
    if "description had to fall back" in notes:
        flags.append("Description fallback")

    return flags or ["None"]


def enrich_rows(rows):
    enriched = []
    for row in rows:
        pattern = PRIMITIVE_TO_PATTERN.get(row["Primitive"])
        if not pattern:
            raise ValueError(f"Unmapped primitive: {row['Primitive']}")

        flags = flags_for_row(row)
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
                "Value Pattern ID": pattern["id"],
                "Value Pattern": pattern["name"],
                "Rule Basis": f"Primary primitive {row['Primitive']} -> {pattern['name']}",
                "Pattern Mechanism": pattern["mechanism"],
                "Review Flags": "; ".join(flags),
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


def summarize_pattern(enriched_rows):
    by_pattern = defaultdict(list)
    for row in enriched_rows:
        by_pattern[row["Value Pattern"]].append(row)

    lines = []
    lines.append("# Value Pattern Summary")
    lines.append("")
    lines.append("Generated: 2026-08-06")
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Curated concepts classified: {len(enriched_rows)}")
    lines.append(f"- Unmapped concepts: 0")
    lines.append(f"- Value Pattern count: {len(PATTERN_ORDER)}")
    lines.append("- Classification anchor: primary primitive from `data/concepts_curated.csv`")
    lines.append("")
    lines.append("## Pattern Distribution")
    lines.append("")
    lines.append("| Value Pattern | ID | Concepts | Source Primitives | Top Domains | Top Jobs |")
    lines.append("| --- | --- | ---: | --- | --- | --- |")

    for pattern in PATTERN_ORDER:
        rows = by_pattern[pattern["name"]]
        domains = Counter(row["Domain"] for row in rows).most_common(3)
        jobs = Counter(row["Canonical Job"] for row in rows).most_common(3)
        domain_text = ", ".join(f"{name} ({count})" for name, count in domains)
        job_text = ", ".join(f"{name} ({count})" for name, count in jobs)
        primitive_text = ", ".join(pattern["primitives"])
        lines.append(
            f"| {pattern['name']} | {pattern['id']} | {len(rows)} | {primitive_text} | {domain_text} | {job_text} |"
        )

    lines.append("")
    lines.append("## Review Flag Counts")
    lines.append("")

    flag_counter = Counter()
    pattern_flag_counter = defaultdict(Counter)
    for row in enriched_rows:
        for flag in row["Review Flags"].split("; "):
            if flag == "None":
                continue
            flag_counter[flag] += 1
            pattern_flag_counter[row["Value Pattern"]][flag] += 1

    for flag, count in flag_counter.most_common():
        lines.append(f"- {flag}: {count}")

    lines.append("")
    lines.append("## Pattern Notes")
    lines.append("")

    for pattern in PATTERN_ORDER:
        rows = by_pattern[pattern["name"]]
        ranked = sorted(
            rows,
            key=lambda row: (-int(row["Confidence"]), row["Concept ID"]),
        )
        representatives = ", ".join(
            f"{row['Concept ID']} {row['Concept Title']}" for row in ranked[:3]
        )
        low_confidence = sum(int(row["Confidence"]) <= 2 for row in rows)
        broad_wedge = sum(
            "Broad initial wedge" in row["Review Flags"] for row in rows
        )
        lines.append(f"### {pattern['id']} {pattern['name']}")
        lines.append("")
        lines.append(f"- Definition: {pattern['definition']}")
        lines.append(f"- Economic mechanism: {pattern['mechanism']}")
        lines.append(f"- Representative concepts: {representatives}")
        lines.append(f"- Low-confidence concepts: {low_confidence}")
        lines.append(f"- Broad-wedge concepts: {broad_wedge}")
        lines.append("")

    with SUMMARY_PATH.open("w") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def main():
    rows = load_rows()
    enriched_rows = enrich_rows(rows)
    write_map(enriched_rows)
    summarize_pattern(enriched_rows)


if __name__ == "__main__":
    main()
