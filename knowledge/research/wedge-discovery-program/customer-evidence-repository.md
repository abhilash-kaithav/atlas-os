# Customer Evidence Repository

Last updated: 2026-08-14
Status: Canonical practitioner evidence layer

## Rules

- Customer and practitioner evidence outrank vendor positioning.
- Every row should be reusable by later research objectives.
- Evidence strength reflects the quality of the evidence for the wedge question, not the general quality of the source.

## Evidence Log

| Evidence ID | Industry | Related wedge or candidate | Evidence strength | Source type | Date reviewed | Source link | Paraphrased signal | Reusable implication |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CE-001 | Construction | `W-001` | High | G2 review set | 2026-08-14 | [GCPay Reviews | G2](https://www.g2.com/products/gcpay/reviews) | Users report manual SOV entry, awkward waiver flow, unclear error states, and no easy subcontractor-side self-correction path. | GC-side payment software still leaves the sub-side correction loop manual. |
| CE-002 | Construction | `W-001` | High | G2 review | 2026-08-14 | [Procore Reviews | G2](https://www.g2.com/products/procore/reviews) | Advanced tracking across commitments and change orders still involves repeated Excel uploads. | Modern project systems still leak billing exception work into spreadsheets. |
| CE-003 | Construction | `W-001` | High | Practitioner podcast | 2026-08-14 | [Tara Cristel podcast transcript](https://podscan.fm/podcasts/bred-to-build-construction-podcast/episodes/ep-53-a-200-day-pay-app-nightmare-amp-financing-gcs-w-tara-cristel) | A commercial sub describes a 200-day pay-app delay and being forced to finance materials while waiting. | The correction loop carries real working-capital pain, not just admin annoyance. |
| CE-004 | Housing | `W-002` | High | Practitioner forum | 2026-08-14 | [How do you handle maintenance coordination for a small PM portfolio?](https://www.biggerpockets.com/forums/899/topics/1283438-how-do-you-handle-maintenance-coordination-for-a-small-pm-portfolio?page=1) | A small PM operator says triage, owner approvals, aging work orders, and update chasing are the main headache; spreadsheets and texts stop working as the portfolio grows. | Maintenance coordination pain is operationally central and not solved by generic PMS alone. |
| CE-005 | Housing | `W-002` | High | Practitioner forum | 2026-08-14 | [For those managing maintenance in-house: how do you track vendor communications?](https://www.biggerpockets.com/forums/899/topics/1283143-for-those-managing-maintenance-in-house-how-do-you-track-vendor-communications) | Operators describe stale threads, missing follow-ups, and tenant update chasing after a work order is assigned. | The failure is often after assignment, not at intake. |
| CE-006 | Housing | `W-002` | Medium | Practitioner forum | 2026-08-14 | [5 things that nearly broke our maintenance operation](https://www.biggerpockets.com/forums/899/topics/1278925-5-things-that-nearly-broke-our-maintenance-operation-4-years-as-a-coordinator) | A coordinator says owner approvals, COI chasing, and spreadsheet/text workflows become brittle around 40-50 doors. | A blocker-resolution layer may be more valuable than another broad PMS module. |
| CE-007 | Housing | `W-002` | High | G2 review | 2026-08-14 | [ResMan Reviews | G2](https://www.g2.com/products/resman/reviews) | A user says one work order cannot cover multiple units and the make-ready board is still tricky to use. | Even purpose-built property systems do not fully remove turn coordination friction. |
| CE-008 | Housing | `W-002` | Medium | G2 review | 2026-08-14 | [Entrata Reviews | G2](https://www.g2.com/products/entrata/reviews) | A user asks for queueing and in-context tagging instead of sending screenshots by email. | Exception coordination still leaves the system and loses accountability. |
| CE-009 | Administrative and support services | `W-003` | Medium | G2 review | 2026-08-14 | [Bullhorn Reviews | G2](https://www.g2.com/products/bullhorn/reviews) | A staffing operations user says vendor-specific onboarding still requires email plus downloading and re-uploading records. | Staffing back-office truth still fragments across vendor- and client-specific workflows. |
| CE-010 | Administrative and support services | `W-003` | Medium | G2 review | 2026-08-14 | [Avionté Reviews | G2](https://www.g2.com/products/avionte-avionte/reviews) | A current user says a weekly time report produced zero data after an upgrade and had to be turned off, delaying operational use. | Staffing teams still depend on fragile reporting and exception handling even inside specialized platforms. |
| CE-011 | Administrative and support services | `W-003` | Medium | Job posting | 2026-08-14 | [OnCall Solutions Billing Operations Coordinator](https://www.linkedin.com/jobs/view/billing-operations-coordinator-at-oncall-solutions-4405554634) | The role exists to validate timesheets, review approvals, identify discrepancies, and resolve them before payroll and invoicing. | The mismatch-resolution job is explicit enough to have a dedicated owner. |
| CE-012 | Administrative and support services | `W-003` | Medium | Job posting | 2026-08-14 | [WorldWide Medical Staffing Payroll/Billing Specialist](https://www.simplyhired.com/job/JcFijGynFMbh9z433tIFxyVEUgZojUlMYQQIt9_rk5dMkZSaXLELqg) | The role revolves around verifying weekly timecards, generating invoices from approved timecards, and reconciling discrepancies. | Buyers already fund labor to do this manually, which supports willingness to pay if software can narrow the task. |
| CE-013 | Food services and drinking places | Killed candidate | High | Practitioner article | 2026-08-14 | [A Necessary Evil? Independent Operators Speak Out on Third-Party Delivery](https://www.restaurantowner.com/public/A-Necessary-Evil-Independent-Operators-Speak-Out-on-ThirdParty-Delivery.cfm) | Operators say each delivery partner requires hours of weekly auditing to verify deposits, credits, and fees. | Restaurant marketplace settlement pain is real and recurring. |
| CE-014 | Food services and drinking places | Killed candidate | Medium | G2 review | 2026-08-14 | [Restaurant365 Reviews | G2](https://www.g2.com/products/restaurant365/reviews) | An accounting user says payroll integrations and DSS re-polls still create issues despite the broad suite. | Back-office suites improve the workflow but do not eliminate exceptions. |
| CE-015 | Food services and drinking places | Killed candidate | Medium | G2 review | 2026-08-14 | [Otter Restaurant Operating System Reviews | G2](https://www.g2.com/products/otter-restaurant-operating-system-ros/reviews) | Users value order aggregation and CSV exports, but support and workflow gaps remain. | Order aggregation alone does not fully solve settlement and exception recovery. |

## Usage Notes

- `High` evidence requires multiple current practitioner sources plus current product verification.
- `Medium` evidence usually combines practitioner evidence with job-posting, review, or operational-detail support but lacks deeper repetition.
- `Low` evidence should not be enough by itself to preserve a wedge.
