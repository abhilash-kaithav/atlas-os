# RO-002 Executive Summary

Last updated: 2026-08-14
Status: Approved research summary

## Headline

Commercial trade-contractor AR does not support a broad software thesis.

One narrow wedge does survive:

> subcontractor-side pay-application rejection diagnosis and resubmission orchestration

This is the workflow where a trade contractor learns that the current pay app cannot move forward because a GC-specific packet rule, schedule-of-values mismatch, change-order gap, waiver issue, compliance problem, or portal rule blocked approval. The team then has to figure out what actually failed, fix it, rebuild the packet, and resubmit before the monthly cutoff slips.

## Why This Won

- It is recurring. The same trade contractor can hit this failure mode every billing cycle across many GCs.
- It is buyer-visible. Controllers, AR leads, and billing managers feel the delay directly in aging and cash forecasting.
- It is measurable. A rejected pay app can push an otherwise collectible receivable into the next payment cycle.
- Existing software is present, but the subcontractor still does meaningful work outside the software.
- The strongest current platforms are still mostly oriented around the payor or GC workflow, not a neutral sub-side exception desk.

## What Lost

### Change-order-to-billing synchronization

Pain is real, but [Clearstory](https://www.g2.com/products/clearstory/reviews), Procore, Autodesk Cost Management, and Siteline all already recognize and productize much of the workflow.

### Retainage release tracking

Pain is severe, but the workflow is broader, slower-moving, and already a visible product surface for sub-AR tools such as [Siteline](https://www.g2.com/sellers/siteline), [Cotillo](https://cotillo.io/), and ERP-layer retainage features in [Vista](https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/retainage) and [Sage 300 CRE](https://us-kb.sage.com/portal/app/portlets/results/viewsolution.jsp?solutionid=223924250029938).

### Lien-waiver and notary orchestration

Pain is obvious, but it is already explicitly addressed by GCPay, Procore Pay, Textura-class workflows, and waiver-specific add-ons. The remaining gap is real, but not clean enough to be the first monopoly wedge.

### SOV setup and billing-template normalization

This remains painful, but direct sub-AR products already market "custom pay applications" and GC-specific form handling. The gap is narrower than it first appears.

## Final Recommendation

The surviving monopoly wedge is:

> the exception desk that receives rejected or at-risk pay apps, identifies the exact blocker, maps the fix to the right SOV, change-order, waiver, compliance, or portal requirement, and drives the corrected resubmission before the billing window closes

The next step is not product build.

The next step is direct controller and AR validation that this rejection-and-resubmission loop is painful enough, frequent enough, and budgetable enough to buy as a standalone workflow layer.
