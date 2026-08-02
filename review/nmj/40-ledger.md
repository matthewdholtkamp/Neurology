# Citation ledger — docs/nmj/index.md

Every dose, threshold and trial claim on the page mapped to its source. This is what
makes the `*Verified*` footer honest rather than aspirational. Anything that could
not be pinned is marked **UNVERIFIED** here *and* stated as unverified on the page.

FDA label facts were pulled programmatically via openFDA (`tools/evidence.py`);
`effective_time` is given so each claim is re-checkable.

---

## Drug dosing — all from current FDA labels

| Claim on page | Source | Label effective |
|---|---|---|
| Pyridostigmine 30–60 mg PO q4–6h; ER 180 mg qHS; renal reduction | pyridostigmine bromide label | 2025-08-04 |
| Pyridostigmine "label average 600 mg/day is pre-immunotherapy-era practice"; operative threshold >450 mg/day | OE synthesis (Meriggioli & Sanders, *Lancet Neurol* 2009) + label | 2025-08-04 |
| Efgartigimod IV 10 mg/kg weekly ×4, cap 1,200 mg ≥120 kg | VYVGART | 2026-05-13 |
| Efgartigimod SC 1,000 mg/10,000 U weekly ×4 | VYVGART Hytrulo | 2026-07-15 |
| **Efgartigimod indication carries NO serostatus qualifier** | VYVGART §1 / Hytrulo §1 — verified directly by orchestrator | 2026-05-13 / 2026-07-15 |
| Rozanolixizumab weekly ×6; 420/560/840 mg bands; ≥63-day cycle interval; aseptic meningitis | RYSTIGGO §2, §5.2 | 2026-01-20 |
| **Nipocalimab 30 mg/kg → 15 mg/kg q2wk; IV ONLY** | IMAAVY §2.2 — single label, `route: INTRAVENOUS`, verified directly | 2025-05-07 |
| Eculizumab 900 mg weekly ×4 → 1,200 mg wk 5 → 1,200 mg q2wk | SOLIRIS §2.3 | 2026-07-08 |
| Eculizumab pediatric ≥6 y (AChR+) | Drugs@FDA BLA 125166 SUPPL-448, approved 2025-02-28 | — |
| Eculizumab biosimilars BKEMV / EPYSQLI carry gMG | BLA 761333 SUPPL-1; BLA 761340 SUPPL-3 | 2026-07-02 / 2026-07-06 |
| Ravulizumab weight-banded load → q8wk from wk 2; ≥40 kg | ULTOMIRIS §2.3 Table 1 | 2025-10-09 |
| Zilucoplan 16.6/23/32.4 mg SC daily; baseline amylase + lipase | ZILBRYSQ §2.2–2.3, §5.4 | 2026-02-03 |
| C5 supplemental dosing after PLEX/IVIG (300–600 mg; 1,200–1,800 mg) | SOLIRIS §2.5 Tables 2–3; ULTOMIRIS §2.4 Table 3 | 2026-07-08 / 2025-10-09 |
| MenACWY **+ MenB** ≥2 wk, urgent-start exception, REMS | boxed warnings, all three C5 labels | as above |
| Inebilizumab 300 mg → repeat at 2 wk → q6mo; HBV/IgG/TB pre-checks; premedication | UPLIZNA §2.1–2.3, §4, §5.4 | 2025-12-11 |
| Rituximab off-label, **no FDA MG indication**; 375 mg/m² ×4 or 1 g ×2 | RITUXAN §1 + boxed warning | 2025-01-06 |
| Prednisone 5–60 mg/day labelled range; contraindicated in systemic fungal infection | prednisone label | 2023-08-31 |
| Azathioprine 50 mg → 2.5 mg/kg/day max; **TPMT *and* NUDT15**; CBC schedule; allopurinol ⅓–¼ | azathioprine label | 2025-05-19 |
| Mycophenolate 1,000 mg BID; boxed embryofetal warning; 2 pregnancy tests; **OCP efficacy reduced** | mycophenolate mofetil label | 2026-05-14 |
| Methotrexate 7.5–20 mg **weekly**; pregnancy contraindicated (non-neoplastic) | methotrexate label + boxed warning | 2026-05-18 |
| Tacrolimus / cyclosporine doses | **UNVERIFIED as MG dosing** — off-label neurology practice, stated as such on the page | — |
| Glycopyrrolate 1 mg TID; **MG is a labelled contraindication** | glycopyrrolate (oral) §4 | 2026-05-05 |
| IVIG 2 g/kg over 2–5 days | **off-label** — no IGIV product carries an FDA MG indication (zero-result openFDA query). Dose is consensus practice; stated as such | — |
| IVIG boxed warning: thrombosis, renal failure | BIVIGAM boxed warning | 2025-05-05 |
| IV pyridostigmine 1–2 mg/h discouraged, fatal arrhythmia risk; 1 mg IV ≈ 30 mg PO | Claytor, *Muscle Nerve* 2023 (via OE) | — |

## Thresholds and clinical numbers

| Claim | Source |
|---|---|
| 20/30/40 rule (VC <20 mL/kg, NIF < −30, MEP <40); **not prospectively validated** | Claytor, *Muscle Nerve* 2023 |
| MEP fall ≥30% = high risk; low-risk VC >20 / MEP >40 / NIF better than −40 | Claytor 2023; Thieben, *Muscle Nerve* 2005 |
| Single-breath count ~30 normal / ≤20 significant, ~2 counts/sec, ~116 mL VC per count | Claytor 2023 (via OE) |
| *Competing figure: normal ≥25* — stated on the page as a footnote | Dishnica, *J Clin Neurosci* 2023 systematic review |
| PaCO₂ >45 mmHg predicts BiPAP failure | Seneviratne, *Arch Neurol* 2008 (n=60) |
| PaCO₂ >50, pneumonia, older age predict NIV failure; failure ~38% | Claytor 2023; Neumann, *Neurology* 2020 (n=250) |
| Succinylcholine resistance, ED95 ≈2.6× | Eisenkraft et al.; StatPearls anesthesia-in-MG |
| Steroid worsening ~day 5, lasts 1–7 days, up to 50%; predictors older age + bulbar | Farmakidis, *Muscle Nerve* 2020 (via OE); PMID 17074487 |
| IVIG 69% vs PLEX 65% — **moderate-to-severe worsening MG, not intubated crisis** | Barth, *Neurology* 2011 (n=84) |
| PLEX superior in crisis (7-day severity, 2-wk ventilation, 1-mo function) | Qureshi 1999 (n=54); Wang 2022 (n=40); Neumann 2020 (n=250) |
| IVIg may be less beneficial than PLEX (very low certainty) | Cochrane 2025 |
| AChR ~85%, MuSK ~5–8%, LRP4 ~1–3% | carried from prior review — **not re-verified this round** |
| Thymoma 10–15% | carried from prior review — **not re-verified this round** |
| Ocular generalization 50–80% untreated / ~28% treated / ~39% pooled | Menon, *Neurology* 2024; Hendricks, *Neurology* 2023 |
| Prednisone HR 0.43–0.46, any IS HR 0.30–0.35 for generalization | Menon, *Neurology* 2024 (n=154, propensity-matched + IPTW) |
| Ocular steroid dose ~15 mg/day; 5/6 vs 0/5 reaching MM at median 14 wk | ICG 2020 Update (small RCT) |
| RNS 10% decrement at 2–5 Hz; abnormal ~17% ocular vs ~85% generalized | AAEM/AANEM practice parameter |
| SFEMG ~92% overall, 95–99% generalized, ~79% ocular | AANEM parameter; PMID s00415-019-09631-3 |
| MGTX: 20% absolute increase in MM at 36 mo (95% CI 1.6–37%); no benefit ≥50 post hoc | Wolfe NEJM 2016; *Lancet Neurol* 2019; Gronseth AAN advisory 2020 |
| LOMG thymectomy 2.36× remission (48.9% vs 23.8% at 24 mo); HR 3.25 second cohort | Chen, *Ann Neurol* 2026; Latini, *J Neurol* 2025 (both observational) |
| Class equivalence FcRn / C5 / CD19; insufficient response 20–49% both arms | McLaren, *Neurology* 2026 (27 RCTs, n=2,318); Huntemann, *JNNP* 2025 (n=153) |
| MINT −1.9 MG-ADL / −2.5 QMG wk 26; AChR+ widens at wk 52; MuSK QMG NS | Nowak, *NEJM* 2025 |
| ICI-MG median onset ~21 days; triple-M in-hospital mortality ~38% | *Diagnostics* 2024 (PMID 39202282); *Crit Care* 2026 |
| MuSK series: 33.9% worsened on AChE-I, 7.3% cholinergic crisis | PMID 38759248 |
| Pyridostigmine Class I evidence; amifampridine adds nothing | IMPACT-MG, *Neurology* 2026 (PMIDs 41945881, 41945880) |
| Cemdisiran SC q12wk, FDA action Nov 2026; gefurulimab filed | *Lancet* 2026 (PMID 42030965); Regeneron/AstraZeneca releases |

## Military / regulatory — verified against source PDFs

| Claim | Source | Status |
|---|---|---|
| AR 40-501 3-31c *"Unless clinically restricted to extraocular muscles"* | AR 40-501 (27 Jun 2019) PDF p.32 | **verbatim, extracted and confirmed by orchestrator** |
| DoDI 6130.03 V2 5.26.l | Vol 2 (Chg 2, 6 Feb 2026) PDF p.35 | verbatim |
| 5.26.a gate applies to MG; only 5.26.d and 5.26.k are exempt | Vol 2 PDF pp.33–35 | confirmed |
| Aeromedical chain 4-27 → Vol 1 6.26.q, **no ocular exception** | AR 40-501 p.47, p.39; Vol 1 PDF p.49 | confirmed |
| 3-2 Note (6-month accession/retention fork); 3-3c waiver bar | AR 40-501 PDF pp.14–15 | confirmed |
| P factor for nervous system | DA Pam 40-502 4-3c(1) PDF p.17 | confirmed |
| 3-7b binocular diplopia standard | AR 40-501 PDF p.16 | confirmed |
| Non-Army aeromedical specifics | — | **UNVERIFIED** — stated as such on the page |
| TRICARE PA criteria, tiers, specialist-prescriber rule | — | **UNVERIFIED** — militaryrx PA path 404s; Formulary Search is dynamic. Page states this explicitly |
