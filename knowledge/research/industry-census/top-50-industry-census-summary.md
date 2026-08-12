# Top 50 Industry Census Summary

Last updated: 2026-08-12
Status: Completed research snapshot

## Scope

- Geography: United States
- Universe: BEA GDP-by-industry summary-table leaf industries, excluding aggregate rollups and government-only lines
- Ranking metric: 2025 current-dollar gross output from BEA table `TGO105-A`
- Context metrics: 2025 current-dollar value added from `TVA105-A`; 2026 Q1 real gross-output change (SAAR) from `TGO101-Q`
- Non-goals: no opportunity ranking, no product ideas, no company theses, no hypotheses recorded in the CSV

## Methodology

1. Start from the current BEA GDP-by-industry summary workbooks because they are current through annual 2025 and quarterly 2026 Q1.
2. Remove aggregate lines such as `All industries`, `Private industries`, `Private goods-producing industries`, `Private services-producing industries`, and government-only rollups.
3. Rank the remaining leaf industries by 2025 current-dollar gross output.
4. Capture the top 50 industries in a structured CSV with:
   - size fields
   - operating-model observations
   - workflow observations
   - representative systems-of-record maps
   - maturity, pressure, and inefficiency observations
   - row-level source bundles
5. Leave `hypothesis_notes` blank to preserve a clean separation between evidence collection and later interpretation.

## Source Stack

- BEA gross output workbook: [GrossOutput.xlsx](https://apps.bea.gov/industry/Release/XLS/GDPxInd/GrossOutput.xlsx)
- BEA value added workbook: [ValueAdded.xlsx](https://apps.bea.gov/industry/Release/XLS/GDPxInd/ValueAdded.xlsx)
- BEA current product page: [GDP by Industry](https://www.bea.gov/data/gdp/gdp-industry)
- Official sector context pages from Census, CMS, FDIC/Federal Reserve, SEC, NAIC, EIA, USDA, BTS, NCES, NTIA, and FCC as cited in the CSV `source_links` field

## Caveats

- This census uses BEA summary-table leaf industries instead of the 138-industry underlying-detail tables because the summary tables are current through 2025 annual data and 2026 Q1 quarterly data, while the underlying detail still lags at 2024.
- BEA gross output is not the same as end-market revenue or TAM. For margin industries such as wholesale and retail trade, BEA measures gross output on a margin basis rather than gross merchandise value.
- Workflow and systems fields are representative operating observations, not exhaustive market-share claims.
- Evidence quality varies by industry. Regulated sectors and sectors with strong official reporting coverage tend to be higher-confidence than heterogeneous service categories.

## Ten Notable Cross-Industry Observations

1. The top 10 industries account for about 47.3% of 2025 gross output across the full top-50 set, so Atlas should expect concentration rather than a flat landscape.
2. Real-estate-adjacent sectors (`Housing`, `Other real estate`, `Construction`) represent about $7.95T of 2025 gross output before counting upstream suppliers.
3. Care-delivery sectors (`Ambulatory health care services`, `Hospitals`, `Nursing and residential care facilities`, `Social assistance`) represent about $3.84T of gross output, making health operations a major workflow surface independent of drug or biotech bets.
4. Core finance layers (`Credit intermediation`, `Insurance`, `Securities`, `Funds`) total about $4.43T, but their bottlenecks are dominated by regulation, risk, and reporting workflows rather than raw transaction demand.
5. The digitally native information stack (`Data processing`, `Broadcasting/telecommunications`, `Publishing/software`, `Computer systems design`) totals about $3.43T and includes several of the strongest 2026 Q1 real growth readings.
6. Consumer-facing physical sectors were mixed to weak in 2026 Q1. `General merchandise stores`, `Food and beverage stores`, and `Food services and drinking places` were among the weakest near-term movers in the census.
7. Value-added share varies sharply by industry. `Housing` and `Legal services` retain unusually high value-added shares, while `Motor vehicles`, `Primary metals`, and `Petroleum refining` are far more input-intensive.
8. Many of the largest sectors are coordination-limited rather than invention-limited. Scheduling, billing, procurement, compliance, exception handling, and documentation recur across the list.
9. Systems of record are usually mature at the core but fragmented at the edges. ERP, EHR, core-banking, claims, PMS, and TMS layers exist; the recurring breakdown is handoff, interoperability, and exception resolution.
10. Labor-constrained, regulation-heavy sectors dominate the census. Construction, health care, housing operations, utilities, education, administrative services, and transportation all show simultaneous workforce and compliance pressure.

## Facts vs. Hypotheses

- Facts and observations are stored in `top-50-industry-census.csv`.
- No hypotheses, opportunity rankings, or company theses were recorded in this sprint.

## Recommended Next Move

Define a follow-on task that selects 5-10 industries from this census for deeper operating-system and core-workflow mapping based on size, structural pressure, and visible inefficiency, without ranking venture opportunities yet.
