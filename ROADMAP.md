# Neuro Scutbook — Project Roadmap

A neurology reference for MDs, NPs, PAs, and medics: a bedside consult "scutbook"
(what to do in clinic / ER / inpatient) paired with plain-language evidence briefs,
with a standardized military-medicine layer (deployability, profiles, EPTS/LOD,
retention, MEB/IDES). Hosted free on GitHub Pages.

> **Status: LIVE** at https://matthewdholtkamp.github.io/Neurology/ (public repo
> github.com/matthewdholtkamp/Neurology). 11 pages across Headache (6), Dizziness,
> Diplopia + military primer. Auto-deploys on push to main via strict-build CI.
> This file is the living build checklist.
> Last updated: 2026-07-12
>
> **Headache vertical now rebuilt in a "tiered prescriptive" style** — every treatment
> section is a numbered "what I want done, in order" flow + `Step 1→2→3` order-set boxes
> with doses, plus a **TRICARE formulary layer** (preferred/no-PA vs PA-gated agents,
> neurologist requirements). Source-verified against current guidelines (AHS/EAN/ICHD-3)
> with linked references. This is the **new canonical template** — propagate the tiered
> flow + TRICARE box to all future drug/protocol pages.

---

## Locked decisions

- **Stack:** MkDocs + Material theme → GitHub Pages, auto-deployed via GitHub Action.
  Author in plain Markdown; `git push` publishes in ~1 min.
- **Page model:** One page per topic. Bedside "Consult" content top-to-bottom,
  then a "Discover" evidence brief near the bottom. Single URL, single search hit.
  (Not a split /consult/ + /discover/ tree.)
- **Every clinical page carries a standardized Military box** (reusable snippet).
- **Every page shows a visible "Last reviewed: MON YYYY" line.**
- **Pilot topic:** Headache (only topic with both source workflow + source articles).
- **Start the repo private;** flip to public once disclaimer + PII scrub + first pages
  are solid. (Public repo required for free GitHub Pages.)

## Open decisions (not blocking)

- [ ] Repo name.
- [ ] Add a "quick reference" landing grid (tap symptom → topic), mirroring
      `Quick reference.docx`? (High utility on mobile.)

---

## Standard topic template

Every clinical page follows this skeleton so users build muscle memory:

1. One-liner + who this is for
2. RED FLAGS / when to image now
3. Rapid approach (numbered algorithm)
4. Focused H&P + exam
5. Workup (labs / imaging / LP)
6. Management by diagnosis
7. Order set (copy-pasteable)
8. Disposition (admit vs discharge)
9. Military box (standardized snippet)
10. Discover: evidence summary + key trials
11. References

### Military box — fixed 5 fields
1. **Deployability** — deployment-limiting per MOD/CENTCOM standards?
2. **Profile** — temporary vs permanent, DA Form 3349, functional limits.
3. **EPTS / LOD** — existed-prior-to-service vs line-of-duty.
4. **Retention** — AR 40-501 thresholds that trigger review.
5. **MEB/IDES** — when to refer, DoDI 1332.18 framing, aeromedical/flight-status.

---

## Guardrails

- **Copyright:** SCUTBOOK docx = your own writing, OK to publish. Headache PDFs
  (Continuum/AAN, UpToDate) are copyrighted — they are a *reading list*, never
  copied. Discover briefs are written from scratch and cited (AHS/AAN guidelines,
  ICHD-3, landmark trials).
- **Disclaimer:** every page framed as educational clinical decision-support —
  not a substitute for professional judgment or individual medical advice.
- **De-identify before publish:** scrub PII, real Botox lot #/exp, patient specifics.
- **OPSEC:** military content stays at published-doctrine level (AR 40-501,
  DoDI 1332.18, DA 3349). Nothing unit-specific or sensitive.
- **Currency:** the 2016 scutbook is skeleton + voice only. Each page is updated to
  current evidence *before* it gets a "reviewed 2026" stamp. No hand-waved dates.

---

## Content currency triage (2016 → 2026)

Planning estimate from model knowledge (through Jan 2026), **not verified currency**.
Each page's specifics get checked against current sources at build time.

### Substantial rewrite (do LAST, after template is proven)
- [ ] **Stroke** — thrombectomy to 24h (DAWN/DEFUSE-3); tenecteplase; large-core
      (SELECT2, ANGEL-ASPECT) & basilar (ATTENTION, BAOCHE) thrombectomy.
- [ ] **Major Stroke Trials Cliffs (2018-19)** — append 2020–2025 trials.
- [ ] **Demyelinating / MS** — 2017/2024 McDonald; new DMT era; NMOSD split off
      (eculizumab/satralizumab/inebilizumab); MOGAD as distinct disease.
- [ ] **NMJ / Myasthenia** — complement inhibitors (eculizumab, ravulizumab) &
      FcRn inhibitors (efgartigimod, rozanolixizumab); MGTX thymectomy.
- [ ] **Dementia** — anti-amyloid mAbs (lecanemab, donanemab) + ARIA; plasma/CSF
      biomarkers (p-tau217); RT-QuIC replaces 14-3-3 for CJD.
- [ ] **Seizure** — status epilepticus rewritten by ESETT; new ASMs; ILAE 2017.

### Drug/protocol update (skeleton holds, add what's new)
- [x] **Headache** *(PILOT — vertical complete + source-verified)* — triage hub + 6 pages
      (migraine, cluster/TACs, trigeminal neuralgia, MOH, NDPH, post-traumatic), rebuilt in
      the tiered prescriptive style with a TRICARE layer; drug details source-verified against
      current AHS/EAN guidelines + ICHD-3 (2026). Remaining: overview/triage hub (index.md)
      still in the older format — reformat into a tap-to-topic decision grid if desired.
- [ ] **Intracranial Hemorrhage** — andexanet/idarucizumab reversal; INTERACT3;
      ENRICH minimally-invasive surgery.
- [ ] **Movement Disorder** — VMAT2 inhibitors for TD; newer PD adjuncts.
- [ ] **Motor Neuron Disease** — edaravone; tofersen (SOD1); Relyvrio saga.
- [ ] **Acute Myelopathy** — fold in AQP4/MOG + NMOSD/MOGAD.
- [ ] **Myopathy** — modern myositis antibody panels; IMNM (anti-HMGCR/SRP).
- [ ] **Peripheral Neuropathy + IVIG** — CIDP efgartigimod; order set fine.
- [ ] **Brain Death** — update to 2023 AAN/consensus BD/DNC guideline.
- [ ] **Neuroinfections** — integrate autoimmune encephalitis workup.
- [ ] **Quick Reference** — drop MTHFR; add autoimmune/MOG panels.

### Light touch (date it, keep the voice)
- [ ] Increased ICP Management (nudge toward hypertonic saline)
- [ ] Hypercoag workup (drop MTHFR)
- [ ] Coma workup
- [x] Dizziness — built; reframed to timing-and-triggers (TiTrATE/ATTEST) + HINTS.
- [x] Diplopia — built as its own page (monocular-vs-binocular, CN III/IV/VI, Parks 3-step).
- [ ] Radiculopathy & Plexopathy
- [ ] AMS workup
- [ ] IVIG / PLEX / Rituximab order sets

---

## Phased build order

- **Phase 0 — Foundation:** ✅ DONE — MkDocs Material scaffold, mobile nav + search,
  landing page + disclaimer, custom Military/Order-set/Red-flag callouts, auto-expanding
  abbreviations, GitHub Action, contributing guide + copy-paste template, and the
  **fully-built Migraine page (updated to 2026 evidence) as the canonical template.**
  Remaining before public: set real GitHub username/repo in `mkdocs.yml`, `git init` +
  push to a private repo, enable Pages on the `gh-pages` branch, then PII scrub + flip public.
- **Phase 1 — Headache vertical:** ✅ DONE — triage hub + 6 sub-pages, each with a
  Discover brief and military box. **Live and pushed** to github.com/matthewdholtkamp/Neurology;
  all 6 treatment pages rebuilt in the tiered prescriptive + TRICARE style and source-verified.
- **Phase 2 — Military layer:** standalone deployability/MEB/IDES primer;
  wire military box into headache (post-traumatic HA is the bridge).
- **Phase 3 — Green pile:** fast-follow the 7 light-touch topics for early breadth.
- **Phase 4 — Yellow pile:** the 10 drug/protocol updates.
- **Phase 5 — Red pile:** the 6 substantial rewrites (Stroke first among them).
