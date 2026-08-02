# Changelog — docs/nmj/lems.md

**152 → 478 lines.** First run of the rebuilt cheapest-source-first pipeline.
**One agent instead of five.**

## What each stage cost and caught

| Stage | Cost | Caught |
|---|---|---|
| **A — scripts** | 4 shell commands, ~0 model tokens | 1 HIGH flag (amifampridine named with no dose) — **and the FDA label supplied the fix**; military box missing EPTS/LOD; RUZURGI absent from openFDA |
| **B — OpenEvidence** | free, 67 sources | 19 findings no script could reach, 6 corrections to existing text |
| **C — triage** | — | `page-safety` **not spawned**; `military-tricare` spawned |
| **D — one agent** | 71,812 tokens, **15 tool calls (on budget)**, wrote its own file | 11 findings, 4 HIGH |

For comparison, the MG page ran five agents at ~735k tokens.

---

## Factual corrections

| Was | Now | Caught by |
|---|---|---|
| "up to **80–100 mg/day**" as a single range | **Two different ceilings.** 100 mg/day is the US label maximum; **80 mg/day is the EMA ceiling *and* the expert practice cap** on seizure-risk grounds | OE |
| Cancer surveillance **every 3–6 months** | **Every 4–6 months** for 2 years (2021 **PNS-Care** criteria; the old figure came from the 2011 Titulaer paper) | OE |
| "CT chest first; **FDG-PET/CT if CT is negative**" | **CT *and* PET/CT for everyone** — CT sensitivity falls for central/mediastinal tumours (PET 100% vs CT 50%). CT-first is now labelled as the resource-constrained fallback it is | OE |
| Facilitation "**>60–100%**" | Resolve to **≥60%** — 97% sensitive, 99% specific | OE |
| RNS "2–3 Hz" | **2–5 Hz**, decrement ≥10%; plus the nadir-position discriminator (7th–10th vs 4th–5th in MG, AUC 0.90) | OE |
| Pyridostigmine "**adds little**" | Softened with the reason: the only RCT was **intravenous, single-dose, n=9**; chronic oral add-on has never been randomised and ~67% of a long-term cohort reported benefit | OE |
| VGCC "~85–95%" | **~90%**, near 100% in SCLC-associated disease | OE |
| **"AR 40-501 3-31"** (a heading, not a standard) | **3-31k, "Other neurologic conditions"**, closing on para 3-1 — with explicit warnings not to cite 3-31b (myopathies) or 3-31c (MG's carve-out doesn't transfer) | `military-tricare` |
| **"DoDI 6130.03 V2 5.26.i"** | **Lead with 5.26.e.** 5.26.i is the only subparagraph with its own **permanence qualifier**, so citing it *raises the bar against the page's own argument*. Kept as a secondary citation only. **5.26.n** added — a genuinely *named* standard the dysautonomia engages | `military-tricare` |
| "**MEB/DES: refer**" | The **MAR2-vs-DES fork**, MRDP condition, and "the profile *is* the referral." A well-controlled Soldier who can't perform their PMOS is a MAR2 — sending that to DES gets it bounced | `military-tricare` |

## Added

- **Full amifampridine dosing table** — weight bands, titration increments, max single dose, and
  the **NAT2 poor-metabolizer** adjustment (40–60% prevalence in White and African American
  populations; 3.5–4.5× Cmax). Plus: **divided 3–5× daily is mandatory**, because t½ is 1.8–2.5 h.
- **The malignancy standard, by paragraph** — **AR 40-501 3-34a** and **DoDI 6130.03 V2 5.29**.
  The page previously gestured at "malignancy governs retention" with nothing a provider could put
  in a memo. Key practical point: SCLC therapy meets 3-34a's *"prolonged, intensive medical
  supervision"* limb **without waiting for treatment to fail.**
- **The 5.26.a gate** — LEMS is not an "upon-diagnosis" condition; both prongs must be documented.
- **EPTS/LOD field** — the site-wide gap, and it bites hard here because symptoms precede diagnosis
  by months to years, so the 6-month accession/retention fork can turn on onset-dating.
- **PULHES, a temporary-profile phase, and functional Section 4 limits.**
- **Aeromedical** — absent entirely before. Runs by import (**4-27 → Vol 1 6.26.q / 6.26.n**) and,
  in a paraneoplastic case, **categorically via 4-30b, "history of any malignant tumor."**
- **A TRICARE box** — the page prescribes an orphan drug and said nothing about how a Service
  member obtains it. Pharmacy vs medical benefit split, hedged hard on tier and PA criteria.
- **Two exposures that catch LEMS patients out** — **NMBA hypersensitivity** (11% respiratory
  complications, concentrated in the undiagnosed) and **checkpoint inhibitors** triggering de novo
  LEMS, stated as vigilance rather than established causation.
- **Do not extrapolate the MG biologics** — complement inhibition is a **mechanistic** mismatch in
  LEMS, not merely untested.
- **DELTA-P components in full**, with the honest **prospective AUC 82.5%**.
- **SOX1** for cancer risk; **do not order N-type VGCC.**
- **Two findings that reverse common assumptions:** LEMS **does not reliably flare when the tumour
  recurs** (so it is not a recurrence sentinel), and **SCLC with LEMS survives materially longer
  than SCLC alone** (17 vs 7 months; NCCN says it does not imply incurability).

## The tooling caught its own author

After the new immunotherapy section was written, `lint_page.py` and `label_diff.py` flagged that
**prednisone + azathioprine and rituximab had been added with no doses**, and that the page had
crossed the threshold where a **TRICARE box becomes mandatory**. Both fixed. The scripts do not
care who wrote the defect.

## Verification

- `python3 tools/lint_page.py docs/nmj/lems.md` → **clean**
- `python3 tools/label_diff.py docs/nmj/lems.md` → **0 flags** (from 1 HIGH at intake)
- `mkdocs build --strict` → **exit 0**

## Not done

- **`Last reviewed:` stamp not touched** — awaiting the author's date.
- **DA Pam 40-502 PULHES attribution** carried from the MG page, not re-verified; flagged on the
  page and in the ledger.
- **AR 40-501 4-24 / 4-24a** deliberately not carried over — the reviewer declined to assert them
  without re-checking.
- **TRICARE tier and PA criteria** remain publicly unverifiable.
- `botulism.md` and `nerve-agent.md` still unreviewed.
