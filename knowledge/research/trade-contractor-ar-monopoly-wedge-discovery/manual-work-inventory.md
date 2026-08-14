# Manual Work Inventory

Last updated: 2026-08-14
Status: Active workflow leakage layer

## What Customers Still Do Outside Software

| Workflow | Manual work still performed | Tools or channels used | Evidence |
| --- | --- | --- | --- |
| SOV line setup | Enter or reshape SOV lines differently for each GC and project | Excel, portal forms, PDF markups | GCPay reviewer says some clients want line-by-line while others want milestone billing, forcing manual SOV entry and adaptation. |
| Advanced change-order and billing tracking | Re-upload the same support file into several modules | Excel, Office 365 attachments | Procore reviewer reports re-uploading the same Excel file across commitments, change orders, and bill-of-material tools. |
| Multi-project billing control | Maintain master draw, change-order, invoicing, and waiver tracker | Smartsheet / Excel | Smartsheet community users describe VLOOKUP-heavy grids for COs, draw status, invoicing, and lien waivers. |
| Waiver corrections | Recreate or edit lien waivers when system logic does not reflect the transaction properly | Manual edits, custom reports | Sage users report manually recreating waivers after every check run when credit memo amounts are missing. |
| Waiver delivery | Add separate automation to send waivers to counterparties | MyAssistant, third-party tools | Sage users ask for automated waiver transmission because the standard flow does not cover it. |
| Notary timing | Wait for a notary or physical stamp, then return later to finish billing | Print, physical sign, remote notary, portal relogin | GCPay users describe needing to finish billing only after the waiver has been uploaded or notarized. |
| Self-correction after discovering an error | Call the GC so the sub can fix its own bill instead of rejecting it directly | Phone, email | A GCPay AR user explicitly asks for a subcontractor-side reject button with a reason field. |
| Report shaping for AR visibility | Export and heavily manipulate reports outside the ERP | Excel, ODBC, Crystal Reports | Sage 300 CRE and Vista users describe significant Excel manipulation, custom reporting, and consultant help. |
| Retainage cleanup and release prep | Use special reports or database tools to clear or adjust old retainage records | Custom reports, ODBC, Access | Sage support responses point users to special procedures and external tools for bulk cleanup or retainage adjustments. |
| Collections memory | Track who said what, what is blocked, and what is due next | Email threads, call notes, spreadsheets | Practitioner posts and G2 reviews repeatedly describe chasing, follow-up, and lack of visibility after submission. |

## Implication

The most durable signal is not "people still use spreadsheets" in the abstract.

It is:

- spreadsheets hold the exception memory,
- phone calls resolve the ambiguity,
- and the software stack still loses the subcontractor when the billing packet falls off the clean path.
