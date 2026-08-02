# Review scorecard

One row per completed page review. **This file is the point of the whole system.**

The five-reviewer panel and OpenEvidence are different retrieval stacks with
different blind spots. Tracking what OE catches that the panel misses turns the
manual paste step from a gap check into a spot check: after enough rows, the
recurring misses go back into `.claude/agents/*.md` and the panel stops making them.

Read the **"OE caught, panel missed"** column as the backlog for improving the panel.

| Date | Page | Panel HIGH | Panel total | OE caught, panel missed | Panel caught, OE missed | Lesson → which agent |
|---|---|---|---|---|---|---|
| 2026-08-02 | `docs/nmj/index.md` (MG) | 25 | 71 | **10** — PLEX first-line in crisis; clustered-AChR CBA before labeling seronegative; LOMG thymectomy data; timing as the cholinergic discriminator; IV pyridostigmine arrhythmia risk; 2nd BiPAP threshold; steroid worsening peaks ~day 5; MEP-fall/de-escalation criteria; cholinergic crisis is *rare*; real-world C5-vs-FcRn | ~45 — every label fact (efgartigimod all-serotype, nipocalimab IV-only, eculizumab pediatric, biosimilars, batoclimab), all dosing/boxed warnings, succinylcholine, ICI triple-M, all military/TRICARE | 4 lessons, all applied ↓ |

| 2026-08-02 | `docs/nmj/lems.md` | 4 | 11 (1 agent) | **19** — PLEX-era practice aside, the big ones: surveillance interval 3–6 → **4–6 months** (2021 PNS-Care); `80–100 mg/day` conflates the **US max (100)** with the **EMA/expert cap (80)**; facilitation resolves to **≥60%**; **LEMS does not flare when the tumour recurs**; **SCLC+LEMS survives longer** than SCLC alone; don't order N-type VGCC; anaesthesia NMBA hazard; checkpoint-inhibitor de novo LEMS | The **scripted** pass caught the missing dose *and supplied the fix from the label* (incl. NAT2). The **agent** caught what nothing else could: **5.26.i was working against the page**, the malignancy standard by paragraph (3-34a / 5.29), and aeromedical 4-30b | Cheapest-source-first works ↓ |

**Run notes (2026-08-02, LEMS) — first run of the rebuilt pipeline.**
**1 agent instead of 5. 71,812 agent tokens vs ~735,000. 15 tool calls vs 191.** The agent wrote
its own findings file, so there was no transcription tax. The free stages did the entire clinical
review; `page-safety` was never spawned because the machine pass found no contradictions and OE had
already surfaced both safety gaps.

**Two things worth keeping:**

1. **`tools/label_diff.py` reproduced the MG page's two most expensive findings for free** —
   efgartigimod's removed serostatus restriction and nipocalimab's IV-only route — when re-run
   against the pre-review baseline. Those cost five agents the first time.
2. **The tooling caught its own author.** After the new LEMS immunotherapy section was written, the
   linter flagged that prednisone+azathioprine and rituximab had been added with no doses, and that
   the page now needed a TRICARE box. The scripts do not care who wrote the defect.

**Run notes (2026-08-02, MG):** first end-to-end run. Two reviewers died on a session
limit and were rerun — no findings lost, because state lives in files. **OE overturned
one panel finding that would have made the page worse** (`dose-pharmacist F-13`,
pyridostigmine ceiling) and **reframed two more** (cholinergic-crisis framing;
thymectomy over-narrowing). The page's own linter passed it clean while 8 biologics
sat there undosed — the dose check only inspected `!!! orderset` blocks, not
`=== "tabs"`. Fixed in `tools/lint_page.py`.

## Standing lessons

Patterns confirmed across more than one review. Each one should already be written
into the named agent definition.

| Lesson | Agent | Status |
|---|---|---|
| Verify approval status, never assume — tolebrutinib got an FDA CRL in Dec 2025 after being written as approved | `recency-scout` | in agent |
| Pull the FDA label rather than recalling a dose | `dose-pharmacist` | in agent |
| EPTS/LOD is the military-box field most often missing site-wide | `military-tricare` | in agent |
| Distinguish FDA vs EMA vs "phase 3 positive, not approved" explicitly | `recency-scout` | in agent |
| **A label's dosing may predate the modern treatment era.** Before calling a page's ceiling wrong, ask whether the label still reflects current practice. *(Pyridostigmine, 2026-08-02 — this one nearly caused harm.)* | `dose-pharmacist` | in agent |
| **A positive phase 3 is not a coming approval.** Check whether the sponsor actually filed. *(Batoclimab, 2026-08-02 — the mirror of the tolebrutinib error.)* | `recency-scout` | in agent |
| **When a pooled estimate contradicts a page, check whether the cohorts differ in treatment status before proposing the number.** *(Ocular generalization 39% vs 50–80% vs 28%.)* | `guideline-auditor` | in agent |
| **Do not narrow a recommendation to a trial's positive subgroup without checking for observational evidence in the excluded group.** *(Thymectomy ≥50.)* | `guideline-auditor` | in agent |
| **Distinguish "no randomized difference" from "no difference"** — practice-changing signals can live in non-randomized data. *(PLEX in crisis.)* | all reviewers | in `guideline-auditor`, `recency-scout` |
