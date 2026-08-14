# Incumbent Gap Analysis

Last updated: 2026-08-14
Status: Active incumbent layer

## Standard

This document answers:

- Why has Procore not solved this?
- Why has Autodesk not solved this?
- Why has Sage not solved this?
- Why has Vista not solved this?

The analysis relies on product scope evidence plus practitioner evidence. When a conclusion is inferred from both, that inference is stated directly.

## Workflow Under Test

Subcontractor-side pay-app rejection diagnosis and resubmission orchestration.

## Procore

### Evidence

- [Procore Pay](https://support.procore.com/products/online/procore-pay) is explicitly designed for general contractors and owner-builders, with subcontractors onboarded as payees.
- [Procore's payment page](https://www.procore.com/pay) focuses on streamlining subcontractor payment, payment readiness, and lien waiver exchange inside the Procore platform.
- [Procore financial management](https://www.procore.com/financial-management) emphasizes all-in-one financial clarity and invoice management.
- Practitioner evidence from [G2](https://www.g2.com/products/procore/reviews) still shows external logs or spreadsheets, and one reviewer says advanced tracking across commitments, change orders, and bill-of-material tools still requires re-uploading the same Excel file in multiple places.

### Conclusion

Procore has materially improved the GC-side workflow.

It has not eliminated the subcontractor-side exception desk because:

- the workflow is still anchored inside the GC's system,
- the sub is still adapting to each GC's configuration,
- and exception recovery still escapes into Excel, email, and duplicate uploads.

## Autodesk

### Evidence

- [Autodesk Build + GCPay integration](https://www.autodesk.com/blogs/construction/autodesk-forma-build-gcpay-a-new-integration-connecting-field-and-finance-is-here/) says Build already covers cost management, but teams needing deeper compliance, lien-waiver, and electronic-payment capabilities should use GCPay.
- [Autodesk's GCPay integration help](https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/setup-cost/cost-integrations/Cost_GCPay_Integration.html) states that subcontractors create and submit pay apps directly in GCPay while GCs review and approve there.
- [Autodesk/GCPay product news](https://www.autodesk.com/blogs/construction/transforming-construction-payments-autodesks-strategic-move-with-payapps-acquisition/) highlights broad visibility and payments between project stakeholders.
- Practitioner evidence from [G2](https://www.g2.com/products/autodesk-forma-formerly-autodesk-construction-cloud/reviews) says subcontractors still must learn the process of each different GC to use the system correctly.

### Conclusion

Autodesk has acknowledged the payment workflow as important enough to buy GCPay.

But the evidence still points to a GC-configured process, not a neutral subcontractor exception layer. The surviving gap is not that Autodesk ignores payments. The gap is that the sub still does not control the cross-GC correction loop.

## Sage

### Evidence

- [Sage 300 CRE](https://www.sage.com/en-us/products/sage-300-construction-and-real-estate/) emphasizes accounting, reporting, document control, and integrations.
- [Sage's construction page](https://www.sage.com/en-us/sage-construction/) emphasizes AIA-style billing, compliance, job costing, reporting, and integrated operations.
- [Sage KB guidance](https://us-kb.sage.com/portal/app/portlets/results/viewsolution.jsp?solutionid=223924250029938) shows retainage release is a defined accounting procedure inside the system.
- Practitioner evidence from [Sage community](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/124514/ap-lien-waivers-to-include-credit-memos) and [G2](https://www.g2.com/products/sage-300-construction-and-real-estate/reviews) shows manual waiver fixes, custom reporting, Excel manipulation, and reliance on add-ons like MyAssistant.

### Conclusion

Sage handles accounting storage and many construction mechanics.

It does not own the operational recovery loop when the billing packet is wrong or blocked. The evidence shows users still rely on custom reports, manual waiver handling, and add-ons rather than a native subcontractor-side exception workflow.

## Vista

### Evidence

- [Vista retainage help](https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/retainage) shows strong retainage mechanics at the AR item level.
- [Vista AP retainage help](https://help.trimble.com/doc/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage) shows the system can hold and later release retainage through defined accounting steps.
- Practitioner evidence from [Vista G2 reviews](https://www.g2.com/products/trimble-vista/reviews) shows complicated processes, messy reporting, and one user explicitly pairing Vista with GCPay for the payment workflow.
- Another [Viewpoint review](https://www.g2.com/products/dxo-viewpoint/reviews) says the change-order module does not flow well and can be difficult to learn.

### Conclusion

Vista is strong as a construction ERP and retainage/accounting engine.

The evidence does not show it owning the trade-contractor correction workflow. Instead, users supplement it with GCPay, custom reporting, and external process knowledge.

## Incumbent Reality

None of the four incumbents are absent.

All four participate in the construction financial stack.

The surviving gap remains because:

- Procore and Autodesk are strongest when the GC controls the workflow.
- Sage and Vista are strongest when the accounting system is the source of record.
- The subcontractor-side exception desk sits between those two layers and is still patched together by people.
