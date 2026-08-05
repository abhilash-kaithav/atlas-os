# Decision Log

Last updated: 2026-08-05
Status: Active

## Logging Rules

- Log every material decision that affects scope, prioritization, workflow, or strategy.
- Include the evidence or rationale behind the decision.
- If a decision is revised, add a new row instead of rewriting history.

## Decision Register

| Date | ID | Decision | Evidence or Rationale | Status | Next Review |
| --- | --- | --- | --- | --- | --- |
| 2026-08-03 | D-001 | Use a Git repository as the Atlas source of truth. | Versioning, traceability, and durable context are required from day one. | Active | Quarterly |
| 2026-08-03 | D-002 | Prioritize revenue impact over adjacent optimization. | The system is intended to support action on commercial opportunities first. | Active | Quarterly |
| 2026-08-03 | D-003 | Keep recommendations concise and decision-ready. | Long outputs slow execution and obscure the next action. | Active | Quarterly |
| 2026-08-03 | D-004 | Do not change strategy without new evidence. | Direction changes should be justified by observed signals, not novelty. | Active | Ongoing |
| 2026-08-03 | D-005 | Generate broadly, then cluster and validate before prioritizing. | Broad intake improves coverage; clustering and validation reduce noise. | Active | Monthly |
| 2026-08-03 | D-006 | Record decisions and document revisions explicitly. | The repo must preserve operational memory independent of chat history. | Active | Ongoing |
| 2026-08-03 | D-007 | Adopt a formal knowledge hierarchy with evidence thresholds and mandatory session closeout updates. | Separating observations, hypotheses, evidence, and principles preserves reasoning history and reduces premature certainty. | Active | Monthly |
| 2026-08-04 | D-008 | Establish a permanent Atlas source-of-truth set before clustering work begins. | Atlas is transitioning from broad ideation into structured exploitation; charter, operating manual, constitution, roadmap, knowledge index, and opportunity-engine design reduce strategic drift and preserve working context. | Active | Monthly |
| 2026-08-05 | D-009 | Adopt Concept Schema v1.0 as mandatory for every Atlas concept record. | Consistent clustering, cross-cutting analysis, prevention of schema drift, and future automation require one frozen eight-field concept format before the representative 100-concept pilot. | Active | Monthly |
| 2026-08-05 | D-010 | Preserve the concept repository as Atlas's gold source and primary intellectual property. | Protecting concept-level fidelity preserves Atlas's foundational asset, keeps every original concept individually addressable, and supports future recombination, re-analysis, and layered enrichment without destructive consolidation. | Active | Monthly |
| 2026-08-05 | D-011 | Adopt `docs/PRODUCT_BOUNDARY.md` as a permanent strategic artifact and update it after every meaningful competitor evaluation. | Competitive analysis should sharpen Atlas's boundary without turning the charter into a market-comparison document; a dedicated artifact preserves durable positioning and reduces drift toward startup execution. | Active | Monthly |
| 2026-08-05 | D-012 | Adopt `data/concepts.csv` as the canonical Atlas Concept Inventory and immutable raw concept source. | The full ideation history has now been recovered into a durable, ID-stable repository artifact. Freezing the raw concept layer preserves chronology and original wording, prevents chat-history loss, and lets classification, families, scoring, and ventures remain additive layers instead of destructive edits. | Active | Monthly |
| 2026-08-05 | D-013 | Split the concept inventory into `data/concepts_raw.csv` and `data/concepts_curated.csv` while keeping the raw layer immutable. | Atlas now needs a durable preservation layer and a separate analytical layer. Renaming the raw file preserves the gold source, while the curated derivative enables schema-based comparison, QA, and future versioned enrichment without overwriting original wording. | Active | Monthly |
| 2026-08-05 | D-014 | Adopt Atlas operating model v1.0 as the repository-first workflow for tasking, execution, review, and shared state. | Atlas now needs a durable handoff loop between Chat and Work before Opportunity Families begins. Standard task, result, review, and state artifacts make work traceable, reusable by future sessions, and independent of chat history. | Active | Monthly |
| 2026-08-05 | D-015 | Adopt Atlas Reasoning Model v1.0 as the governing methodology for Atlas. | Atlas now needs one concise constitutional artifact that defines its laws, standard reasoning pipeline, taxonomy tests, and Value Pattern standard before Value Pattern Discovery begins. This replaces the earlier constitution as the active methodological source of truth while preserving the evidence-first repository model. | Active | Monthly |
| 2026-08-05 | D-016 | Adopt `docs/BOOTSTRAP.md` as the first-read startup artifact for all future Atlas sessions. | Atlas now has stable constitutional documents, active state artifacts, and canonical data layers, but future sessions still need one repository-grounded entry point that prevents drift back to chat-memory reconstruction during the permanent Chat -> Work migration. | Active | Monthly |

## Revision Notes

- Use this file as the authoritative history for strategic and process decisions.
- When a document changes materially, reference the related decision ID in the commit message or update note.
