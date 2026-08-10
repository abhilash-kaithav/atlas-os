#!/usr/bin/env python3

import csv
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FAMILY_MAP_PATH = (
    REPO_ROOT
    / "opportunity-engine"
    / "opportunity-families"
    / "opportunity_family_map.csv"
)
OUTPUT_DIR = REPO_ROOT / "opportunity-engine" / "scoring"
SCORECARD_PATH = OUTPUT_DIR / "opportunity_family_scores.csv"
SUMMARY_PATH = OUTPUT_DIR / "opportunity_family_ranked_summary.md"


CRITERIA = [
    {
        "key": "size_of_opportunity",
        "label": "Size of Opportunity",
        "weight": 20,
        "description": (
            "How large and recurring the underlying problem space appears across "
            "budgets, domains, and strategic importance."
        ),
    },
    {
        "key": "ai_moat",
        "label": "AI Moat",
        "weight": 15,
        "description": (
            "How strongly the family can compound proprietary context, data, "
            "feedback loops, or model advantage into better performance."
        ),
    },
    {
        "key": "founder_fit",
        "label": "Founder Fit",
        "weight": 15,
        "description": (
            "How well the family matches the founder's capabilities, motivation, "
            "and right-to-win once a dedicated founder-fit artifact exists."
        ),
    },
    {
        "key": "speed_to_mvp",
        "label": "Speed to MVP",
        "weight": 10,
        "description": (
            "How quickly Atlas could ship a narrow wedge without requiring heavy "
            "market formation, institutional change, or large up-front integrations."
        ),
    },
    {
        "key": "defensibility",
        "label": "Defensibility",
        "weight": 15,
        "description": (
            "How likely the family is to become hard to replace through workflow "
            "embedment, data, networks, trust, or accumulated assets."
        ),
    },
    {
        "key": "platform_potential",
        "label": "Long-Term Platform Potential",
        "weight": 15,
        "description": (
            "How naturally a narrow wedge can expand into a broader operating "
            "system, network, or category-defining platform."
        ),
    },
    {
        "key": "revenue_potential",
        "label": "Revenue Potential",
        "weight": 10,
        "description": (
            "How clear the budget owner, willingness to pay, and value-capture "
            "path appear for an initial wedge."
        ),
    },
]


NEUTRAL_FOUNDER_FIT_RATIONALE = (
    "No founder-fit artifact exists in the canonical repository yet, so Atlas "
    "holds founder fit at a neutral 3/5 for every family until that input is "
    "made explicit in a durable repo artifact."
)


SCORE_INPUTS = {
    "OF-001": {
        "family": "Operational Execution Infrastructure",
        "shortlist_status": "Not shortlisted",
        "recommendation": "Do not prioritize for immediate research.",
        "overall_rationale": (
            "The family targets real operating pain and is fast to wedge, but it "
            "is also the most crowded and least defensible family in the current set."
        ),
        "research_angle": (
            "Only revisit if a sharply constrained workflow wedge reveals unusual "
            "distribution or proprietary context advantages."
        ),
        "scores": {
            "size_of_opportunity": {
                "score": 4,
                "rationale": (
                    "Workflow and memory pain is broad across operations, but the "
                    "breadth also reflects a generic problem space rather than a "
                    "single unusually leverageable category."
                ),
            },
            "ai_moat": {
                "score": 2,
                "rationale": (
                    "Execution copilots and memory layers are easy to copy unless "
                    "they capture unusually proprietary context or deep workflow lock-in."
                ),
            },
            "founder_fit": {
                "score": 3,
                "rationale": NEUTRAL_FOUNDER_FIT_RATIONALE,
            },
            "speed_to_mvp": {
                "score": 5,
                "rationale": (
                    "A narrow execution wedge can be shipped quickly because it "
                    "does not require market liquidity or heavy institutional change."
                ),
            },
            "defensibility": {
                "score": 2,
                "rationale": (
                    "Without a unique data exhaust or high switching cost, most "
                    "execution products in this family remain vulnerable to feature competition."
                ),
            },
            "platform_potential": {
                "score": 3,
                "rationale": (
                    "Some wedges could expand into an operating layer, but that "
                    "expansion path is crowded and often collapses into broad horizontal tooling."
                ),
            },
            "revenue_potential": {
                "score": 4,
                "rationale": (
                    "Operational efficiency budgets are real, but pricing power is "
                    "constrained when the wedge looks like generic automation."
                ),
            },
        },
    },
    "OF-002": {
        "family": "Decision and Foresight Infrastructure",
        "shortlist_status": "Primary",
        "recommendation": "Research first and use as the default build-candidate family.",
        "overall_rationale": (
            "This family combines high-value pain, clear budget logic, and a "
            "believable wedge path without requiring a full network or institutional platform on day one."
        ),
        "research_angle": (
            "Start with one painful recurring decision workflow where delay, bad "
            "tradeoffs, or low-confidence forecasting already destroy value."
        ),
        "scores": {
            "size_of_opportunity": {
                "score": 5,
                "rationale": (
                    "High-stakes decisions exist across product, operations, "
                    "commercial, policy, and physical systems, making this the "
                    "broadest high-value family in the current ranking."
                ),
            },
            "ai_moat": {
                "score": 4,
                "rationale": (
                    "The family can compound proprietary decision context, outcome "
                    "history, and simulation layers into better recommendations over time."
                ),
            },
            "founder_fit": {
                "score": 3,
                "rationale": NEUTRAL_FOUNDER_FIT_RATIONALE,
            },
            "speed_to_mvp": {
                "score": 4,
                "rationale": (
                    "A single decision workflow can be productized faster than a "
                    "network or governance system while still demonstrating measurable ROI."
                ),
            },
            "defensibility": {
                "score": 4,
                "rationale": (
                    "Once embedded in recurring decisions, the product can become "
                    "sticky through context history, workflow integration, and outcome tuning."
                ),
            },
            "platform_potential": {
                "score": 4,
                "rationale": (
                    "A strong wedge can expand from one decision surface into a "
                    "broader planning, simulation, and operating layer."
                ),
            },
            "revenue_potential": {
                "score": 5,
                "rationale": (
                    "The budget logic is unusually clear because bad decisions "
                    "destroy time, margin, trust, or strategic position directly."
                ),
            },
        },
    },
    "OF-003": {
        "family": "Trust and Adaptive Governance",
        "shortlist_status": "Reserve",
        "recommendation": "Keep as a strong reserve candidate, but not the first research lane.",
        "overall_rationale": (
            "The family is strategically strong and likely defensible, but it is "
            "slower to wedge because trust, compliance, and adaptive control usually require deeper adoption."
        ),
        "research_angle": (
            "Revisit in sectors where proof, readiness, or resilience budgets are "
            "already visible and switching costs can compound."
        ),
        "scores": {
            "size_of_opportunity": {
                "score": 4,
                "rationale": (
                    "Trust and governance pain is meaningful across infrastructure, "
                    "operations, healthcare, and public systems, though the category "
                    "is narrower than generic execution or decision tooling."
                ),
            },
            "ai_moat": {
                "score": 4,
                "rationale": (
                    "Verification and adaptation can become stronger with domain "
                    "data, policy context, and operating history."
                ),
            },
            "founder_fit": {
                "score": 3,
                "rationale": NEUTRAL_FOUNDER_FIT_RATIONALE,
            },
            "speed_to_mvp": {
                "score": 2,
                "rationale": (
                    "Most credible wedges need trust, compliance, or change-management "
                    "buy-in, which slows adoption compared with a simpler decision tool."
                ),
            },
            "defensibility": {
                "score": 5,
                "rationale": (
                    "If the system becomes part of governance, readiness, or risk "
                    "control, it can become unusually hard to replace."
                ),
            },
            "platform_potential": {
                "score": 4,
                "rationale": (
                    "A wedge can expand into a wider governance layer, but that "
                    "platform path usually requires slower institutional trust-building."
                ),
            },
            "revenue_potential": {
                "score": 4,
                "rationale": (
                    "Risk and compliance budgets exist, but the buying motion is "
                    "often slower and more conservative than direct efficiency tools."
                ),
            },
        },
    },
    "OF-004": {
        "family": "Discovery and Liquidity Networks",
        "shortlist_status": "Reserve",
        "recommendation": "Do not lead with this family until a wedge avoids early liquidity traps.",
        "overall_rationale": (
            "The upside is real, especially for platform expansion, but many wedges "
            "in this family struggle to turn discovery into durable monetized liquidity quickly."
        ),
        "research_angle": (
            "Only prioritize when the wedge can capture value before full two-sided "
            "network density is required."
        ),
        "scores": {
            "size_of_opportunity": {
                "score": 4,
                "rationale": (
                    "Search friction and poor matching create meaningful inefficiency, "
                    "but the family only becomes very large when discovery converts into allocation control."
                ),
            },
            "ai_moat": {
                "score": 3,
                "rationale": (
                    "Discovery features are easy to imitate early; the moat improves "
                    "only after proprietary data or liquidity density accumulates."
                ),
            },
            "founder_fit": {
                "score": 3,
                "rationale": NEUTRAL_FOUNDER_FIT_RATIONALE,
            },
            "speed_to_mvp": {
                "score": 2,
                "rationale": (
                    "A demo is easy, but a wedge that reliably produces better matches "
                    "or liquidity is slower to prove than a single-user decision product."
                ),
            },
            "defensibility": {
                "score": 4,
                "rationale": (
                    "If a real network or routing advantage forms, defensibility can "
                    "be strong, but it usually arrives later than the first product release."
                ),
            },
            "platform_potential": {
                "score": 5,
                "rationale": (
                    "This family has the strongest pure platform upside because the "
                    "best version becomes a network or market layer."
                ),
            },
            "revenue_potential": {
                "score": 3,
                "rationale": (
                    "Value capture is less direct until the product controls match quality, "
                    "deal flow, or transaction throughput in a durable way."
                ),
            },
        },
    },
    "OF-005": {
        "family": "Capability Capital Platforms",
        "shortlist_status": "Secondary",
        "recommendation": "Keep as the backup shortlist family behind OF-002.",
        "overall_rationale": (
            "This family has the strongest long-term compounding logic, but the "
            "first wedge must prove repeated-use behavior before the moat becomes real."
        ),
        "research_angle": (
            "Focus on one repeat workflow where retained learning or asset accumulation "
            "clearly improves the next cycle and creates visible willingness to pay."
        ),
        "scores": {
            "size_of_opportunity": {
                "score": 4,
                "rationale": (
                    "The family spans talent, learning, creator, and operating systems, "
                    "but the opportunity surface is more diffuse than the decision family."
                ),
            },
            "ai_moat": {
                "score": 5,
                "rationale": (
                    "Compounding loops, retained user data, and reusable assets map "
                    "especially well to durable AI-native advantage."
                ),
            },
            "founder_fit": {
                "score": 3,
                "rationale": NEUTRAL_FOUNDER_FIT_RATIONALE,
            },
            "speed_to_mvp": {
                "score": 3,
                "rationale": (
                    "A wedge is buildable, but the real value only shows up once "
                    "repetition and compounding behavior are visible."
                ),
            },
            "defensibility": {
                "score": 4,
                "rationale": (
                    "Skill graphs, retained context, and accumulated assets can "
                    "create strong stickiness after the product proves compounding gains."
                ),
            },
            "platform_potential": {
                "score": 5,
                "rationale": (
                    "A successful wedge can expand naturally into a broader capability "
                    "or intellectual-capital platform."
                ),
            },
            "revenue_potential": {
                "score": 4,
                "rationale": (
                    "Recurring subscription or marketplace economics are plausible, "
                    "but willingness to pay depends on sustained compounding value."
                ),
            },
        },
    },
}


def load_rows():
    with FAMILY_MAP_PATH.open(newline="") as handle:
        return list(csv.DictReader(handle))


def flag_list(review_flags):
    if not review_flags or review_flags == "None":
        return []
    return [flag.strip() for flag in review_flags.split(";") if flag.strip()]


def percent(value, total):
    if total == 0:
        return "0.0%"
    return f"{(value / total) * 100:.1f}%"


def metrics_for_rows(rows):
    confidences = [int(row["Confidence"]) for row in rows]
    evidence = Counter(row["Evidence"] for row in rows)
    flags = Counter()
    domains = Counter(row["Domain"] for row in rows)
    jobs = Counter(row["Canonical Job"] for row in rows)

    for row in rows:
        for flag in flag_list(row["Review Flags"]):
            flags[flag] += 1

    why_now_missing = flags["Why-now missing"]
    why_now_present = len(rows) - why_now_missing

    return {
        "concept_count": len(rows),
        "average_confidence": round(sum(confidences) / len(confidences), 2),
        "high_confidence": sum(value >= 4 for value in confidences),
        "low_confidence": sum(value <= 2 for value in confidences),
        "why_now_missing": why_now_missing,
        "why_now_present": why_now_present,
        "why_now_coverage": percent(why_now_present, len(rows)),
        "broad_initial_wedge": flags["Broad initial wedge"],
        "primitive_ambiguity": flags["Primitive ambiguity"],
        "revenue_evidence": evidence["Revenue Evidence"],
        "customer_voice": evidence["Customer Voice"],
        "behavioral_data": evidence["Behavioral Data"],
        "secondary_research": evidence["Secondary Research"],
        "pattern_evidence": evidence["Pattern Evidence"],
        "intuition": evidence["Intuition"],
        "top_domains": ", ".join(
            f"{name} ({count})" for name, count in domains.most_common(3)
        ),
        "top_jobs": ", ".join(
            f"{name} ({count})" for name, count in jobs.most_common(3)
        ),
    }


def points_for(score, weight):
    return int(score * weight / 5)


def build_ranked_rows(rows):
    by_family = defaultdict(list)
    for row in rows:
        by_family[row["Opportunity Family ID"]].append(row)

    ranked_rows = []
    for family_id, score_input in SCORE_INPUTS.items():
        family_rows = by_family[family_id]
        metrics = metrics_for_rows(family_rows)

        total_points = 0
        row = {
            "Opportunity Family ID": family_id,
            "Opportunity Family": score_input["family"],
            "Shortlist Status": score_input["shortlist_status"],
            "Recommendation": score_input["recommendation"],
            "Overall Rationale": score_input["overall_rationale"],
            "Primary Research Angle": score_input["research_angle"],
            "Concept Count": metrics["concept_count"],
            "Average Confidence": metrics["average_confidence"],
            "High Confidence Concepts": metrics["high_confidence"],
            "Low Confidence Concepts": metrics["low_confidence"],
            "Why-now Coverage": metrics["why_now_coverage"],
            "Why-now Missing Concepts": metrics["why_now_missing"],
            "Broad-Wedge Concepts": metrics["broad_initial_wedge"],
            "Primitive Ambiguity Concepts": metrics["primitive_ambiguity"],
            "Revenue Evidence Concepts": metrics["revenue_evidence"],
            "Customer Voice Concepts": metrics["customer_voice"],
            "Behavioral Data Concepts": metrics["behavioral_data"],
            "Secondary Research Concepts": metrics["secondary_research"],
            "Pattern Evidence Concepts": metrics["pattern_evidence"],
            "Intuition Concepts": metrics["intuition"],
            "Top Domains": metrics["top_domains"],
            "Top Jobs": metrics["top_jobs"],
        }

        for criterion in CRITERIA:
            criterion_data = score_input["scores"][criterion["key"]]
            points = points_for(criterion_data["score"], criterion["weight"])
            total_points += points

            prefix = criterion["label"]
            row[f"{prefix} Score"] = criterion_data["score"]
            row[f"{prefix} Weight"] = criterion["weight"]
            row[f"{prefix} Points"] = points
            row[f"{prefix} Rationale"] = criterion_data["rationale"]

        row["Weighted Total"] = total_points
        ranked_rows.append(row)

    ranked_rows.sort(
        key=lambda row: (
            -row["Weighted Total"],
            -row["Revenue Potential Score"],
            -row["Speed to MVP Score"],
            row["Opportunity Family ID"],
        )
    )

    for rank, row in enumerate(ranked_rows, start=1):
        row["Rank"] = rank

    return ranked_rows


def write_scorecard(rows):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "Rank",
        "Opportunity Family ID",
        "Opportunity Family",
        "Weighted Total",
        "Shortlist Status",
        "Recommendation",
        "Overall Rationale",
        "Primary Research Angle",
        "Concept Count",
        "Average Confidence",
        "High Confidence Concepts",
        "Low Confidence Concepts",
        "Why-now Coverage",
        "Why-now Missing Concepts",
        "Broad-Wedge Concepts",
        "Primitive Ambiguity Concepts",
        "Revenue Evidence Concepts",
        "Customer Voice Concepts",
        "Behavioral Data Concepts",
        "Secondary Research Concepts",
        "Pattern Evidence Concepts",
        "Intuition Concepts",
        "Top Domains",
        "Top Jobs",
    ]

    for criterion in CRITERIA:
        prefix = criterion["label"]
        fieldnames.extend(
            [
                f"{prefix} Score",
                f"{prefix} Weight",
                f"{prefix} Points",
                f"{prefix} Rationale",
            ]
        )

    with SCORECARD_PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_summary(rows):
    lines = []
    lines.append("# Opportunity Family Scorecard")
    lines.append("")
    lines.append("Generated: 2026-08-06")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This artifact ranks the approved Opportunity Families so Atlas can choose "
        "where deeper research should begin before committing to a build."
    )
    lines.append("")
    lines.append(
        "The score is a prioritization tool, not proof that the top family is already validated."
    )
    lines.append("")
    lines.append("## Scoring Rubric v1.0")
    lines.append("")
    lines.append("| Criterion | Weight | What It Measures |")
    lines.append("| --- | ---: | --- |")

    for criterion in CRITERIA:
        lines.append(
            f"| {criterion['label']} | {criterion['weight']} | {criterion['description']} |"
        )

    lines.append("")
    lines.append("### Founder Fit Handling")
    lines.append("")
    lines.append(
        "- Founder fit is held at a neutral `3/5` for every family because no dedicated founder-fit artifact exists in the canonical repository yet."
    )
    lines.append(
        "- This keeps the ranking honest: Atlas does not invent founder advantage from chat memory when the repo has not recorded it."
    )
    lines.append("")
    lines.append("## Ranking")
    lines.append("")
    lines.append(
        "| Rank | Opportunity Family | ID | Total | Shortlist | Avg Confidence | Why-now Coverage | Revenue Evidence Concepts |"
    )
    lines.append("| --- | --- | --- | ---: | --- | ---: | ---: | ---: |")

    for row in rows:
        lines.append(
            f"| {row['Rank']} | {row['Opportunity Family']} | {row['Opportunity Family ID']} | "
            f"{row['Weighted Total']} | {row['Shortlist Status']} | {row['Average Confidence']} | "
            f"{row['Why-now Coverage']} | {row['Revenue Evidence Concepts']} |"
        )

    lines.append("")
    lines.append("## Recommended Shortlist")
    lines.append("")
    lines.append(
        f"- Primary research candidate: `{rows[0]['Opportunity Family ID']} {rows[0]['Opportunity Family']}`"
    )
    lines.append(
        f"- Secondary backup candidate: `{rows[1]['Opportunity Family ID']} {rows[1]['Opportunity Family']}`"
    )
    lines.append(
        "- Default move: research the primary family first instead of splitting effort across all five families."
    )
    lines.append("")
    lines.append("## Family Notes")
    lines.append("")

    for row in rows:
        lines.append(f"### {row['Opportunity Family ID']} {row['Opportunity Family']}")
        lines.append("")
        lines.append(f"- Rank: {row['Rank']}")
        lines.append(f"- Weighted total: {row['Weighted Total']} / 100")
        lines.append(f"- Shortlist status: {row['Shortlist Status']}")
        lines.append(f"- Overall rationale: {row['Overall Rationale']}")
        lines.append(f"- Evidence posture: average confidence {row['Average Confidence']}, why-now coverage {row['Why-now Coverage']}, revenue evidence concepts {row['Revenue Evidence Concepts']}.")
        lines.append(f"- Top domains: {row['Top Domains']}")
        lines.append(f"- Top jobs: {row['Top Jobs']}")
        lines.append("- Criterion scores: " + ", ".join(
            f"{criterion['label']} {row[f'{criterion['label']} Score']}/5"
            for criterion in CRITERIA
        ))
        lines.append(f"- Research angle: {row['Primary Research Angle']}")
        lines.append(f"- Recommendation: {row['Recommendation']}")
        lines.append("")

    lines.append("## Current Limits")
    lines.append("")
    lines.append(
        "- The ranking is still constrained by weak why-now coverage and many low-confidence concepts in the underlying curated layer."
    )
    lines.append(
        "- Founder fit is neutralized until the repository contains a dedicated founder-fit artifact."
    )
    lines.append(
        "- The next step should test the top family with external market evidence before Atlas chooses a specific wedge to build."
    )

    with SUMMARY_PATH.open("w") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def main():
    rows = load_rows()
    ranked_rows = build_ranked_rows(rows)
    write_scorecard(ranked_rows)
    write_summary(ranked_rows)


if __name__ == "__main__":
    main()
