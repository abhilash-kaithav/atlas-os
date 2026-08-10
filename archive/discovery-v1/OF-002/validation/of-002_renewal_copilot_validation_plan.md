# Validation Plan: Benchmark-Backed SaaS and AI Renewal Decision Copilot

Last updated: 2026-08-06
Status: Active validation plan
Task ID: TASK-005

## Purpose

This artifact defines the cheapest credible validation sequence for the recommended `OF-002` wedge.

Its job is to decide whether Atlas should move toward a product build, stay in validation, or fall back to the backup family if the wedge weakens materially.

## Validation Goal

Test whether mid-market finance, IT, and operations teams without dedicated procurement have painful enough SaaS and AI renewal decisions that they will:

1. change behavior based on a renewal decision brief
2. trust benchmark-backed guidance
3. pay for a software-first product instead of only buying a service

## Recommended ICP

Start with companies that meet most of these conditions:

- `150` to `1,000` employees
- material SaaS and AI spend
- no deeply staffed procurement team
- finance, IT, and operations all touch vendor-renewal decisions
- at least `3` meaningful software or AI renewals in the next `120` days
- current workflow still depends on spreadsheets, shared drives, email, or ad hoc broker help

## Exclusion Criteria

Do not start with:

- very large enterprises already running a mature procurement stack
- companies focused mainly on direct-material sourcing
- teams with no upcoming renewal pressure
- founders or operators who cannot share any contract, spend, or usage signals even manually

## Core Hypotheses

| ID | Hypothesis | Why it matters | Pass signal | Fail signal |
| --- | --- | --- | --- | --- |
| `H-001` | Renewal decisions are painful, recurring, and under-instrumented for the target ICP. | If the pain is weak, the wedge is not strong enough. | Most target buyers describe recent avoidable waste, late renewals, or weak leverage. | Buyers describe renewals as low pain or already solved. |
| `H-002` | A part-time procurement owner exists and can buy or champion this wedge. | Atlas needs a real buyer before building. | Finance, IT, or operations owners clearly own the problem and can move budget. | Ownership is too fragmented or always pushed to consultants or centralized procurement. |
| `H-003` | Benchmark-backed decision guidance materially changes customer behavior. | Benchmarks are the core differentiator in the wedge thesis. | Buyers say the brief would change timing, negotiation stance, or renewal choice. | Buyers treat the brief as interesting but non-actionable. |
| `H-004` | Atlas can create enough benchmark value before owning a giant proprietary dataset. | The wedge fails if the moat is impossible to start. | Atlas can produce useful price and leverage ranges for live renewals using a scrappy initial data strategy. | Atlas cannot produce differentiated insight beyond obvious public pricing. |
| `H-005` | Customers will pay for a software-first or hybrid product, not only a service-heavy negotiation shop. | The business model changes drastically if this is only consulting. | Buyers accept recurring software or hybrid pricing tied to decision support. | Buyers only want done-for-you services or savings-share negotiation help. |
| `H-006` | A low-integration MVP is good enough for the first wedge. | Atlas should avoid overbuilding too early. | Buyers are willing to start with uploads, manual data pulls, or lightweight integrations. | Buyers require deep procurement-system integration before the product is useful. |

## Validation Sequence

### Phase 1: Problem and workflow interviews

Goal:

Confirm pain, workflow reality, buyer ownership, and renewal timing pressure.

Target sample:

- `12` interviews
- at least `8` companies
- mix of finance, IT, and operations owners

Pass threshold:

- at least `8/12` describe renewals as painful, recurring, and currently under-instrumented
- at least `6/12` name a recent overpayment, late renewal, or weak negotiation outcome
- at least `4/12` agree to share one live or recent renewal for a manual teardown

Fail threshold:

- fewer than `5/12` see renewal decisions as acute
- most say current broker, procurement stack, or finance workflow already solves the problem

### Phase 2: Concierge renewal decision briefs

Goal:

Test whether a manual benchmark-backed decision brief actually changes behavior.

Method:

- run `5` concierge teardowns on real or near-term renewals
- create a brief with contract timing, spend, usage, pricing context, savings ideas, and negotiation posture

Pass threshold:

- at least `3/5` buyers say the brief would change their action, negotiation stance, or renewal timing
- at least `2/5` ask to use the product again for another renewal
- at least `3/5` reveal a believable savings or risk-reduction opportunity large enough to justify future spend

Fail threshold:

- buyers say the brief adds little beyond existing broker or finance review
- benchmark context is not trusted enough to influence action

### Phase 3: Pricing and packaging test

Goal:

Test whether customers want software, hybrid support, or only managed service.

Test offers:

1. recurring software subscription for renewal watchlists and decision briefs
2. hybrid software plus analyst support
3. service-heavy negotiation support

Pass threshold:

- at least `3/8` qualified buyers prefer a software-first or hybrid model over pure service
- at least `2/8` accept a believable recurring budget range without requiring a guaranteed savings-only model

Fail threshold:

- most buyers only want done-for-you negotiation help
- willingness to pay only appears when Atlas behaves like a consultancy

### Phase 4: Data-access feasibility test

Goal:

Confirm that a low-integration MVP can ingest enough information to be useful.

Minimum data package:

- contract or order form
- current spend or invoice history
- renewal date and notice terms
- basic usage or seat counts when available

Pass threshold:

- at least `4/5` concierge customers can provide the minimum package within one week
- the resulting brief is still actionable without a deep procurement-system rollout

Fail threshold:

- access friction is so high that every pilot becomes enterprise integration work

### Phase 5: Benchmark moat feasibility

Goal:

Test whether Atlas can create a differentiated benchmark layer early enough to matter.

Method:

- build an initial source matrix for `10` target vendors
- compare public pricing, package structure, contract terms, seat utilization heuristics, and any anonymized advisory intelligence available during concierge work

Pass threshold:

- Atlas can produce useful pricing bands, leverage flags, or downgrade signals for most target vendors
- buyers say the benchmark layer is one of the most valuable parts of the brief

Fail threshold:

- Atlas cannot say anything materially stronger than "ask for a discount"
- benchmark quality is too weak to defend the wedge

## Prioritized Test Order

1. Problem and workflow interviews
2. Concierge renewal decision briefs
3. Pricing and packaging test
4. Data-access feasibility test
5. Benchmark moat feasibility

## Kill Criteria

Deactivate this wedge and reconsider `OF-005` if any of these conditions hold:

- renewal pain is not consistently urgent in the target ICP
- buyers mostly want a service business, not a product
- benchmark insight is not differentiated enough to change decisions
- data access is too hard for a low-integration MVP

## Recommended First Sprint

### Sprint objective

Decide whether the wedge is strong enough to survive past customer discovery.

### Sprint scope

- recruit `12` qualified interviews
- secure `4` to `5` live or recent renewal teardowns
- manually produce the first renewal decision briefs
- test at least `2` pricing shapes during follow-up calls

### Required output

- interview notes
- renewal teardown notes
- decision brief reactions
- one go / hold / kill recommendation

## Next Action

Run a customer-facing validation sprint instead of designing product flows.

The first customer-facing step should be:

`12 targeted interviews with finance, IT, and operations owners, each ending with an ask for one live renewal teardown`
