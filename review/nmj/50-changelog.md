# Changelog — docs/nmj/index.md

**365 → 953 lines.** Structure and voice unchanged; the canonical format is intact and
the page lints clean. Every change below traces to a named reviewer or to the
OpenEvidence pass.

---

## Factual errors corrected

| What was wrong | Now | Caught by |
|---|---|---|
| **Efgartigimod listed as `AChR+`** | FDA removed the serostatus restriction **8 May 2026** (ADAPT SERON). It is the **only approved agent with no serostatus gate** and the only approved option for the seronegative patient. Fixed in the FcRn bullet, the routing table, Discover, and the footer | `recency-scout` **and** `guideline-auditor` independently; verified against the label by the orchestrator |
| **Nipocalimab "IV or SC"** | **IV only** — one label, route INTRAVENOUS | `dose-pharmacist`, corroborated by `recency-scout` (no supplements to the BLA); verified |
| **Nipocalimab "approved 30 Apr 2025"** | **29 Apr 2025** (FDA action date; the 30th was the press release) | `recency-scout` |
| **AR 40-501 quoted as "to *the* extraocular muscles"** | Quotation corrected to the regulation's actual text; the inserted article removed | `military-tricare`; verified by extracting the source PDF |
| **Aeromedical grounded in "fatigable diplopia"** | Chapter 4 never names MG. Chain is **4-27 → DoDI 6130.03 Vol 1 6.26.q**, which has **no ocular carve-out** — so a Soldier *retained* under 3-31c is **still grounded on history alone** | `military-tricare` |
| **Succinylcholine: "MG patients are exquisitely sensitive… reduced-dose"** | MG patients are **resistant** to succinylcholine (ED95 ≈2.6×) — **dose UP, 1.5–2 mg/kg.** Sensitivity applies to non-depolarizers. Rocuronium + sugammadex named as preferred | `failure-mode` |
| **Eculizumab "IV every 2 weeks"** | 900 mg weekly ×4 → 1,200 mg wk 5 → q2wk. The old text **skipped the entire induction month** | `dose-pharmacist` |
| **Two conflicting intubation thresholds** (<15 vs <15–20 mL/kg) | Single harmonized 20/30/40 rule with NIF and MEP numbers, plus the honest caveat that none is prospectively validated | `failure-mode` + `guideline-auditor` |
| **`batoclimab — not yet approved`** | Phase 3 **succeeded**, then the sponsor **declined to file in MG.** Moved out of the prescribing list — it is not prescribable | `recency-scout` |
| **Thymectomy "yes" / thymoma "always"** | AAN **Level B — *discuss***; thymoma resection has stated exceptions and an elective-timing rule | `guideline-auditor` |

## Safety content added

- **Cholinergic vs myasthenic crisis** — the page had none, while `nerve-agent.md:151` already
  linked here for it. Framed per OE as **rare but not excludable**, not a coin-flip: muscarinic
  signs, **timing (peak 30–60 min post-dose)**, the **>450 mg/day** threshold, and the warning that
  **glycopyrrolate cover masks the signs.** *(`failure-mode` + `dose-pharmacist`; reframed by OE.)*
- **C5 supplemental dosing after PLEX/IVIG** — this page's own crisis pathway creates the sequence
  that strips the drug. *(`dose-pharmacist`.)*
- **IVIG boxed warning** — thrombosis and acute renal failure, with estrogen use and immobilization
  named as risk factors present in this readership. *(`dose-pharmacist`.)*
- **Checkpoint-inhibitor MG promoted** from a line in the cautionary list to its own danger box —
  triple-M overlap, **~38% in-hospital mortality**, *send a troponin.* *(`failure-mode`.)*
- **IV magnesium / eclampsia / pregnancy** — the page previously gave magnesium two contradictory
  verdicts and never mentioned pregnancy. *(`failure-mode`.)*
- **Far-forward / MEDEVAC box** — the crisis section assumed a hospital while the audience includes
  medics afloat. *(`failure-mode`.)*
- **Steroid danger box moved to the point of prescribing**, with OE's corrected timing (**~day 5**,
  1–7 days, up to 50%), named outpatient regimens, and the rule to **maintain the dose through
  worsening rather than withdraw.** *(`failure-mode`; timing corrected by OE.)*
- **Crisis branch inserted into both numbered flows** — they previously placed serology and chest CT
  ahead of rapid immunotherapy with no "skip ahead." *(`failure-mode`.)*

## Clinical content updated

- **PLEX is now first-line in crisis**, with the honest note that randomized equivalence data come
  from *exacerbation, not intubated crisis*. **(OE caught this; no reviewer did.)**
- **Clustered-AChR cell-based assay before labeling anyone seronegative** — most "seronegative"
  patients are assay-negative. **(OE only.)**
- **Seronegative row added** to the routing table; there was previously no guidance for these
  patients at all.
- **MGFA classification, treatment target (minimal manifestation status), and a definition of
  "refractory"** — the page used "refractory" as a gate to biologics without defining it.
  *(`guideline-auditor`.)*
- **Thymectomy age** — best randomized evidence **18–50**, with the LOMG observational data that
  argue against a hard cutoff. **(OE prevented an over-correction here — the panel wanted to narrow
  to 18–50 and delete the late-onset signal.)**
- **Surgical route caveat** — MGTX used extended transsternal; AAN Level B counseling; both sides of
  the minimally-invasive dispute presented rather than harmonized.
- **Ocular MG** — "debated" replaced with the positive recommendation and the Menon 2024
  propensity-matched data; generalization rate given as a **range keyed to treatment status**
  (50–80% untreated / ~28% treated / ~39% pooled) rather than a bare 50%.
- **Full dosing for every biologic and every conventional agent**, plus boxed warnings, pre-treatment
  screening, monitoring, and pregnancy/contraception. **NUDT15 added alongside TPMT.**
- **Eculizumab pediatric ≥6, agent-by-agent age floors, and the eculizumab biosimilar market.**
- **Pyridostigmine now carries Class I evidence** (IMPACT-MG); **amifampridine adds nothing.**
- **Precipitant list rewritten** — reordered so fluoroquinolones lead instead of a drug withdrawn in
  2016, retitled for findability, addressed to the covering provider, and **given safe alternatives
  plus the warning not to withhold antibiotics from a septic MG patient.**
- **Discover brief** — the serostatus wall coming down, the **failed** classes (satralizumab,
  vemircopan, tolebrutinib), class equivalence, and cemdisiran/gefurulimab at the FDA door.

## Panel finding REJECTED

**`dose-pharmacist F-13` — raise the pyridostigmine ceiling toward the label's 600 mg/day.**
OE: that label figure **"reflects pre-immunotherapy-era practice and is not a modern target"**; the
operative threshold is **>450 mg/day**, and a patient symptomatic at 300–480 mg/day is
**inadequately controlled, not under-titrated.** The page's original 360–480 mg/day **stands
unchanged.** Applying the finding would have pushed readers toward the depolarizing block that
`failure-mode F-1` warns about — the panel was internally inconsistent and did not notice.

## Author decision applied

**Single-breath count** — two 2023 sources disagree. Author chose to keep **~30 normal / ≤20
significant** (OE's crisis-specific source), **add the missing counting rate (~2/second)**, footnote
the competing ≥25 figure, and state that it is a **correlate of VC/NIF, not a validated independent
intubation trigger.**

## Verification

- `python3 tools/lint_page.py docs/nmj/index.md` → **clean**
- `mkdocs build --strict` → **exit 0**
- Citation ledger: `40-ledger.md`. Unverifiable items are marked UNVERIFIED there *and* stated as
  unverified in the page footer.

## Not done

- **`Last reviewed:` stamp not touched** — still July 2026, awaiting the author's date.
- Tacrolimus/cyclosporine MG doses are off-label practice, flagged on the page, not label-verified.
- AChR/MuSK/LRP4 frequencies and the 10–15% thymoma figure were carried from the prior review and
  **not re-verified this round.**
- Sibling pages (`lems.md`, `botulism.md`, `nerve-agent.md`) not reviewed — `nerve-agent.md`'s
  cross-reference to the cholinergic-crisis content now resolves correctly.
