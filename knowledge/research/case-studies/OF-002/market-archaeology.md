# OF-002 Market Archaeology: Enterprise Software Renewal Decision System

Last updated: 2026-08-09
Status: Completed research artifact
Task ID: TASK-009

## Executive Summary

- Core thesis: enterprise software renewals are recurring capital-allocation and risk-governance decisions made under fragmented evidence, pricing opacity, and time pressure.
- Why this matters now: AI and SaaS spend are becoming more volatile while ownership, benchmarking, and procurement operating models remain immature.
- Current recommendation: Hold / Do Not Pursue as the current venture. Preserve `OF-002` as institutional knowledge because the problem is real, but the entry wedge is not sufficiently differentiated.
- Confidence: Medium-High. Problem validation is strong; the decisive weakness is entry defensibility rather than market existence.

## Question

What is the actual decision system behind enterprise software renewals, where does economic value leak away, and does the renewal wedge plausibly expand into Enterprise Decision Intelligence?

## Short Answer

The hard problem is not remembering that a contract expires.

The hard problem is assembling the right evidence early enough for finance, IT, procurement, security, legal, and the business owner to choose among renew, renegotiate, reduce, consolidate, replace, or cancel.

That makes the wedge more credible as a decision-intelligence problem than as a simple workflow or calendar problem.

The category is real and urgent, but it is not empty. Benchmark-led procurement vendors, SaaS management systems, procurement orchestration platforms, and converged SAM/SaaS vendors are already active. The open question is whether Atlas can create differentiated benchmark quality, shared decision memory, and enough trust to change customer behavior before the wedge collapses into a service-heavy market.

## Facts

These are evidence-backed observations reviewed on 2026-08-09.

- Spend volatility is rising. SpendHound's 2026 AI Spend Report says `46%` of organizations exceeded their AI budgets in 2025, `81%` expect AI budgets to increase in 2026, `57%` lack confidence they are paying a fair price, and `22%` say no single person owns the AI budget.
- AI use is widespread, but measurable procurement ROI is still rare. Zip says it surveyed `1,050` procurement, finance, IT, and operations leaders and found `62%` now use AI multiple times a day while only `17%` report clear measurable ROI from procurement technology and AI investments.
- Procurement AI remains early. The University of Mannheim / ISM 2026 State of the Procurement Profession reports that `80%` of organizations remain in exploration or pilot phase and none reported AI as fully scaled and embedded in core procurement processes.
- Renewal environments are large and repetitive. Zylo's 2026 SaaS Management Index says the average organization carries `305` SaaS applications, while Zylo's renewal-management guidance says the average organization experiences `211` SaaS renewals each year.
- AI is raising cost volatility inside software portfolios. Zylo says AI-native application spend rose `108%` overall and `393%` in large enterprises year over year, while broader AI-category application use grew `181%`.
- Renewal cycles are slow and renewal-specific friction is material. Vertice says that in June 2026 new software purchases averaged `36` days while renewals averaged `87` days, with pricing opacity, legal redlining, and sequential approvals as major causes.
- Contract and commercial fragmentation destroys value. WorldCC says average value erosion stands at `8.6%`, and attributes the problem to fragmented ownership, disconnected systems, and handoff-heavy operating models.
- The market is converging toward unified software-governance workflows. Forrester says SAM and SaaS management are converging because enterprises need one view across licenses, usage, contracts, and spend.

## Hypotheses

These are current working judgments, not validated facts.

- The economic center of gravity is not procurement alone. The renewal decision appears to be a shared finance, IT, and business-owner problem with procurement, security, and legal acting as gating functions.
- Mid-market companies without deeply staffed procurement teams remain the best initial wedge because fragmentation is likely high while incumbent platform lock-in is lower than in large enterprises.
- Benchmark quality plus reusable decision history could become more defensible than renewal reminders or generic workflow orchestration.
- The wedge expands into Enterprise Decision Intelligence only if customers value the system as a reusable cross-functional decision layer, not only as a lower-cost negotiation service.

## Unknowns

These questions remain unresolved and require direct customer evidence.

- Who is the true champion in the target ICP: finance, IT, operations, or procurement-adjacent leadership?
- How much proprietary benchmark depth is required before buyers trust the output enough to change behavior?
- Will customers pay for software-first decision support, or mostly for analyst-assisted negotiation services?
- Which renewal categories create the fastest proof of value: AI tools, horizontal SaaS, security, or systems of record?
- How often do customers change the final decision after seeing usage, benchmark, or contract-risk evidence?
- How much data-access friction appears before a useful decision brief can be produced?

## Decision Lifecycle

This lifecycle is synthesized from the current repo thesis plus Zylo, Vertice, ServiceNow, WorldCC, Forrester, BCG, and current procurement-platform workflows.

| Stage | Core question | Primary inputs | Main owners | Typical failure mode |
| --- | --- | --- | --- | --- |
| Trigger detection | What is renewing, and when does the notice window close? | Contract dates, notice terms, renewal calendar, purchase records | Contract owner, SAM / ITAM, procurement ops | Renewal discovered too late or not discovered at all |
| Portfolio triage | Which renewals deserve attention first? | Spend amount, criticality, upcoming dates, business ownership | Procurement, finance, SAM / ITAM | Teams treat all renewals the same or miss high-value contracts |
| Usage and dependency diagnosis | Is the current footprint justified? | Seat utilization, feature usage, adoption, workflow dependency, SSO data | Business owner, IT, SAM / ITAM | Rightsizing happens without real usage evidence |
| Budget and ROI framing | Is the current spend still justified? | Budget owner, prior spend, planned growth, expected ROI, savings targets | Finance, business owner | Budget decisions made without usage or business-context evidence |
| Market and benchmark formation | What is a fair price and realistic alternative set? | Benchmark data, vendor intelligence, competitor options, prior negotiations | Procurement, finance | No fair-price reference or weak alternative pressure |
| Contract and risk review | Which clauses, obligations, and exposures matter? | Contract paper, renewal terms, AI/data clauses, legal redlines, security review | Legal, security, procurement | Clause issues surface too late and extend cycle time |
| Cross-functional recommendation | What should we actually do? | Consolidated usage, cost, benchmark, risk, and alternative evidence | Procurement, finance, IT, business owner | Teams optimize locally and never reach a shared decision |
| Vendor engagement and negotiation | How do we improve terms or pressure alternatives? | Negotiation posture, desired terms, concession strategy, escalation paths | Procurement, business owner, executive sponsor | Vendor controls timing and anchors price before the buyer is ready |
| Governance and final sign-off | Who approves the tradeoff? | Final recommendation, budget impact, risk position, implementation plan | Finance, executive sponsor, CIO or delegate | Decision authority is unclear or enters too late |
| Execution and learning | Did the decision create value, and what should future renewals remember? | Final contract, realized savings, implementation outcome, stakeholder feedback | Procurement ops, finance, IT, business owner | No decision memory, so the next cycle restarts from zero |

## Stakeholder Map

The table below captures the minimum cross-functional anatomy of the renewal decision.

| Stakeholder | Primary objective | Needs to know | Typical output or authority | Common conflict |
| --- | --- | --- | --- | --- |
| CIO / IT leader | Keep the stack operable, secure, and rationalized | Architecture fit, overlap, roadmap, operational dependency | Standardization guardrails, platform preference, escalation input | Can prefer standardization even when a team wants local flexibility |
| Procurement | Improve commercial terms and process discipline | Fair-price context, contract dates, alternatives, negotiation levers | Runs sourcing and negotiation workflow | Can optimize for savings while the business optimizes for speed |
| SAM / ITAM | Control entitlements, waste, and audit exposure | License position, usage, renewals, compliance, reclamation candidates | Rightsizing recommendation, entitlement view, renewal alerts | May focus on license efficiency more than end-user impact |
| Business owner | Preserve or improve workflow outcomes | Adoption, team sentiment, must-haves, switching cost, timing | Business recommendation to renew, replace, reduce, or cancel | Often wants continuity and less disruption than finance prefers |
| Finance | Control budget, forecast accuracy, and ROI | Spend history, budget owner, savings range, price uplift, scenario cost | Budget approval, savings framing, escalation | Can cut cost without full context on operational criticality |
| Security | Reduce vendor and data risk | Security posture, data handling, AI clauses, control gaps | Security approval or escalation | Can slow decisions if brought in too late |
| Legal | Reduce contractual downside | Liability, termination rights, renewal language, AI/data terms | Clause approval, redlines, risk call | Protects downside but often extends timelines |
| Executive sponsor | Resolve high-stakes tradeoffs | Final recommendation, risk summary, budget impact, strategic fit | Tie-breaker or final approval on major contracts | Often enters late, after lower-level disagreement has hardened |
| Vendor account team | Maximize ACV and preserve expansion | Customer usage signals, budget pressure, timing, competitor threats | Quote, terms, concessions, renewal pressure | Incentives are structurally opposed to buyer savings and timing leverage |

## Decision Anatomy

| Decision layer | Practical question | Evidence required | Failure if evidence is weak | Economic consequence |
| --- | --- | --- | --- | --- |
| Need | Do we still need this tool at all? | Workflow dependency, end-user sentiment, replacement feasibility | Renew by habit | Pay for avoidable software |
| Utilization | Are we over-licensed or wrongly tiered? | Seat counts, activity, entitlement data, adoption trends | Renew the old footprint | Carry idle cost into the next term |
| Criticality | How painful is switching or downtime? | Integration depth, workflow centrality, historical reliance | Overestimate or underestimate switching cost | Either overpay from fear or accept risky disruption |
| Price fairness | Is the quoted price actually reasonable? | Benchmarks, prior deal terms, market alternatives, vendor behavior | Negotiate without leverage | Accept avoidable price inflation |
| Terms and timing | Do renewal mechanics help or trap us? | Notice window, auto-renewal terms, uplift clauses, coterms | Miss leverage windows | Lose renegotiation power and flexibility |
| Risk | What legal, security, and compliance exposure rides with the decision? | Legal terms, AI data clauses, security review, audit posture | Risk review happens late | Extra cycle time or forced acceptance |
| Alternatives | What else could replace or consolidate this? | Supplier landscape, overlap, migration path, category fit | Options remain invisible | Weak outside option means weak leverage |
| Ownership | Who can actually decide and who can block? | Budget authority, policy, workflow owner, executive coverage | Decision rights stay ambiguous | Delays, rework, and political escalation |
| Action | What should the organization do now? | Shared synthesis across cost, usage, risk, alternatives, timing | Functions optimize locally | Decision quality stays inconsistent |
| Memory | What should future renewals inherit from this cycle? | Final rationale, realized outcome, vendor behavior, concessions won | Learning stays trapped in email and memory | Future cycles repeat preventable mistakes |

## Economic Leakage Analysis

| Leakage source | Status | Mechanism | Why it matters |
| --- | --- | --- | --- |
| Renewal discovered too late | Fact | Notice windows are missed or surfaced only after options narrow. ServiceNow and Zylo both treat early renewal visibility and alerts as foundational. | Late discovery destroys leverage and increases auto-renewal risk. |
| Over-licensing and stale entitlements | Fact | Seats and tiers are renewed without current usage and entitlement evidence. Zylo, ServiceNow, and Forrester all emphasize reclamation and ongoing optimization. | Idle licenses become recurring committed spend. |
| Pricing opacity | Fact | Buyers often cannot tell whether a quote is fair before negotiations begin. Vertice calls out the information gap directly, while SpendHound says `57%` lack confidence they are paying a fair price. | Weak benchmarks reduce savings and invite vendor anchoring. |
| Fragmented ownership | Fact | Budget authority, tool ownership, and review responsibility are split. SpendHound says `22%` report no single AI budget owner, and WorldCC attributes `8.6%` average value erosion to fragmented ownership and disconnected systems. | Cross-functional drift slows decisions and leaks value between handoffs. |
| Sequential review bottlenecks | Fact | Vertice describes procurement as a relay race where finance, security, and legal often review in sequence. | Cycle time expands and vendor leverage improves. |
| Portfolio overlap and weak consolidation | Fact | Forrester and ServiceNow both frame overlap and software rationalization as active cost-control problems. | Redundant tools survive because no one sees the full option set early enough. |
| Renewal-only operating model | Fact | Forrester says optimization is shifting from periodic events toward a continuous operating model. | Annual fire drills prevent compounding learning and preparation. |
| Missing decision memory | Hypothesis | Most teams likely preserve rationale in email, spreadsheets, or individual memory rather than a durable shared layer. | The same evidence-assembly cost repeats every cycle and benchmark power compounds slowly. |

## Current Solution Landscape

The current market appears to cluster into four visible groups.

| Category | Representative examples | What they already cover | Implication for Atlas |
| --- | --- | --- | --- |
| Benchmark-led procurement and negotiation | Tropic, Vendr, Vertice | Pricing intelligence, renewal triage, negotiation tactics, supplier intelligence, savings workflows | The pain is real, but "fair price plus negotiation help" is not an empty lane. |
| SaaS management and system-of-record platforms | Zylo, ServiceNow SAM | Renewal calendars, usage visibility, entitlement tracking, reclamation, audit readiness | Visibility and renewal tracking are table stakes, not a durable wedge by themselves. |
| Procurement orchestration platforms | Zip and similar workflow layers | Intake, routing, approvals, workflow coordination across procurement, finance, IT, security, and legal | Workflow alone is already well-served in larger organizations. |
| Converged SAM / SaaS governance | Flexera, USU, Matrix42, Qinfinite, Asato | Unified software governance across licenses, contracts, usage, and spend | Large-enterprise convergence is underway, which raises the bar for head-on platform replacement. |

### What this landscape says

- The category is validated. Multiple vendors now sell explicit renewal visibility, benchmark, and negotiation outcomes.
- The market is converging. Pure SaaS management, procurement workflow, and traditional SAM are bleeding together.
- Benchmarking matters. The strongest commercial messaging in the category repeatedly centers on "know what fair looks like before you renew."
- Shared context still appears hard. The existence of many tools does not erase the evidence of ownership fragmentation, cycle-time drag, and weak measurable ROI.

## Opportunity Assessment

### Supporting evidence

- The decision surface is frequent enough to matter. Zylo's `211` annual renewals per average organization means this is not an edge workflow.
- The money is real. Zylo reports average SaaS spend of `$55.7M`, while AI-native spend is accelerating and budgets are increasingly volatile.
- The decision is evidence-hungry. Usage, contract, budget, benchmark, risk, and alternative data all matter, and no single function naturally owns the full picture.
- The process is measurably slow. Vertice's June 2026 gap between new purchases (`36` days) and renewals (`87` days) suggests renewals are operationally harder, not simpler.
- The business pain is broader than negotiation. WorldCC's value-leakage evidence and Forrester's convergence thesis both point to coordination and governance failures, not only bad price negotiation.

### Contradicting evidence

- The category is active and increasingly crowded. Tropic, Vertice, Zylo, ServiceNow, and procurement-orchestration vendors all occupy adjacent territory.
- Benchmark data may be the real moat. If Atlas cannot produce meaningfully credible pricing and alternative intelligence, the wedge weakens fast.
- Operational benefits likely appear before commercial outperformance. BCG says internal productivity and process gains typically arrive earlier than supplier-facing commercial gains.
- The organization may be the harder problem than the software. Mannheim / ISM and BCG both suggest procurement AI value depends on process redesign, data quality, governance, and adoption, not just tooling.
- Large enterprises may prefer incumbent stack extension. Forrester's convergence view suggests mature buyers may choose to extend existing SAM / SaaS platforms rather than adopt another system.

### Current verdict

The problem survives this archaeology pass.

The current venture does not.

The cross-functional renewal decision remains real, frequent, and economically meaningful, but the evidence now points to a more occupied and data-moat-dependent category than Atlas initially assumed.

The biggest risk is not chasing a fake pain point. It is entering a real category with insufficient differentiation, no benchmark moat, and a severe cold-start disadvantage.

## Expansion Analysis

The renewal wedge can expand into Enterprise Decision Intelligence only under specific conditions.

| Condition | If true | If false |
| --- | --- | --- |
| The customer values a reusable decision layer, not just cheaper negotiations | Renewal becomes the entry point into broader recurring spend and vendor decisions | The product collapses into a narrow procurement or services tool |
| Decision memory compounds across cycles | Each renewal improves the next and creates durable organizational leverage | Every renewal behaves like a one-off transaction |
| The primary buyer sits at a finance, IT, or operating coordination layer | The wedge can move into broader portfolio and capital-allocation decisions | The market stays trapped inside procurement tooling |
| Benchmark credibility can be established early | Atlas can influence action, not just reporting | Recommendations remain interesting but not decision-changing |
| Cross-functional synthesis is the hard problem | Atlas can widen from renewals into other fragmented enterprise choices | Existing systems of record will absorb the functionality |

### Working judgment

Expansion is plausible, but only if the wedge proves it can improve repeated, cross-functional, pre-commitment decisions.

If the customer mostly buys negotiation services, or if benchmark data alone does the heavy lifting, the expansion thesis weakens materially.

## Open Questions

- In the target ICP, who is the real tie-breaker when finance, IT, and the business owner disagree?
- Which evidence source changes behavior most: usage, benchmarks, contract risk, or consolidation alternatives?
- How much of the renewal delay is data fragmentation versus governance sequencing?
- Are AI-vendor renewals meaningfully different from traditional SaaS renewals in trust, pricing volatility, or stakeholder mix?
- How often do teams intentionally allow a low-value contract to auto-renew because the coordination cost of re-evaluation is too high?
- What minimum data package is sufficient for a decision brief that a buyer will trust?

## Next Validation Gates

- Test whether target buyers describe renewals as a cross-functional decision problem rather than only a procurement or negotiation problem.
- Test whether the most valuable artifact is a benchmark, a recommendation, or a shared decision brief.
- Test whether a finance, IT, or operations owner will champion this before a mature procurement team exists.
- Test whether benchmark-backed insight changes the customer's action, timing, or negotiation stance on a live renewal.
- Test whether customers want software-first support or still default to analyst-assisted help.

## Source Register

### Repository inputs

- `core/BOOTSTRAP.md`
- `core/STATE.md`
- `core/DECISION_LOG.md`
- `archive/discovery-v1/OF-002/research/of-002_decision_and_foresight_memo.md`
- `archive/discovery-v1/OF-002/validation/of-002_renewal_copilot_validation_plan.md`
- `archive/discovery-v1/taxonomies/value-patterns/value_pattern_summary.md`
- `archive/discovery-v1/taxonomies/opportunity-families/opportunity_family_summary.md`

### External sources reviewed on 2026-08-09

- [Zip: Introducing the State of AI in Spend, published 2026-07-22](https://zip.com/blog/introducing-the-state-of-ai-in-spend)
- [SpendHound: AI Spend Report, 2026 Edition](https://www.spendhound.com/ai-spend-report)
- [University of Mannheim / ISM: State of the Procurement Profession 2026, published 2026-04-28](https://www.bwl.uni-mannheim.de/en/details/state-of-the-procurement-profession-2026-results-presented-exclusively-at-ism-world/)
- [BCG: Scaling Agentic AI in Procurement Is an Organizational Challenge, published 2026-07-21](https://www.bcg.com/publications/2026/scaling-agentic-ai-in-tech-procurement)
- [Zylo: 2026 SaaS Management Index](https://zylo.com/2026-saas-management-index)
- [Zylo: A 3-Part Approach to Programmatic SaaS Renewal Management, updated 2026-04-03](https://zylo.com/blog/3-part-approach-saas-renewal-management)
- [Zylo: Turn Renewals into a Predictable Savings Engine](https://zylo.com/solutions/renewal-savings)
- [Vertice: Procurement cycle time, 2026 benchmarks](https://www.vertice.one/insights/procurement-cycle-time)
- [Vertice: SaaS spend management software for finance teams](https://www.vertice.one/solutions/saas-spend-management-software)
- [Tropic: SaaS renewal management](https://www.tropicapp.io/ai-procurement-software/saas-renewal-management)
- [Tropic: AI and SaaS procurement solution](https://www.tropicapp.io/)
- [WorldCC: From value leakage to better outcomes, published 2026-06-19](https://www.worldcc.com/resource/from-value-leakage-to-better-outcomes-why-contracting-needs-integration.html)
- [Forrester: The Convergence of Software Asset Management and SaaS Management, published 2026-05-26](https://www.forrester.com/blogs/the-convergence-of-software-asset-management-and-saas-management/)
- [ServiceNow: Software Asset Management product overview](https://www.servicenow.com/uk/products/software-asset-management.html)
- [ServiceNow: Software asset overview documentation](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/sam-workspace-landing.html)

## Investment Committee Outcome

### Decision

- Hold / Do Not Pursue as current venture.

### Outcome Summary

- `OF-002` advanced through Market Archaeology and produced a validated problem statement.
- The investment outcome is `Validated Problem / Unattractive Entry`.
- Atlas should preserve this artifact as institutional knowledge rather than delete or hide it.

### Evidence-backed conclusions

These points are supported by the archaeology artifact, companion research, and the subsequent investment review.

- Market is attractive. Renewal volume, pricing opacity, value leakage, AI-spend volatility, and fragmented ownership all point to a large recurring problem.
- Incumbents already possess significant benchmark and transaction-data moats. The current landscape and broader review show vendors such as Tropic, Vertice/Vendr, Zylo, and adjacent platforms already compounding proprietary spend, negotiation, contract, and license data at scale.
- The `system of reasoning` / decision-memory concept already has established vendors. The broader category test found that enterprise decision intelligence is not an unclaimed category simply because it is framed around decision memory.
- Cold-start data disadvantage is a major strategic risk. Benchmark credibility appears to be table stakes, while Atlas has no proven proprietary dataset, distribution channel, or live customer base that offsets the incumbent head start.
- The underlying Value Pattern remains valid even though this company formation is not recommended. `OF-002` still expresses real signal in `VP-002 Decision Advantage`, `VP-003 Memory Infrastructure`, and `VP-008 Pre-Commitment Foresight`; the failure is venture entry attractiveness, not pattern invalidity.

### Hypotheses and interpretations

These are forward-looking judgments, not closed facts.

- A differentiated entrant may still exist if it enters through a proprietary data source, a uniquely advantaged founder channel, or a narrower domain where incumbents are weaker.
- Atlas may revisit this opportunity family later if a future concept passes the moat and cold-start test before deep archaeology begins.
- The recommendation should change only if new evidence materially alters the benchmark, founder-advantage, or data-access picture.

### Lessons for Atlas methodology

- Separate `problem validation` from `venture attractiveness` earlier. A real and painful problem can still be an unattractive company entry.
- Test incumbent benchmark depth and data accumulation before spending heavily on workflow anatomy or category-legibility analysis.
- Run a structural moat and cold-start screen before assuming a recommendation layer or decision-memory layer is defensible.
- Preserve attractive rejected opportunities as institutional knowledge instead of keeping them artificially active.
- Revised evaluation order for future top-ranked opportunities:
  1. Market magnitude
  2. Incumbent map
  3. Structural moat and cold-start test
  4. Founder entry feasibility
  5. Deep market archaeology
  6. Customer discovery
