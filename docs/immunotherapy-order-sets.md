# IVIG / PLEX / Rituximab order sets

<span class="reviewed-stamp">Last reviewed: November 2026</span>

**One-liner:** the prescriptive order sets for the three workhorse immunotherapies in acute neuroimmunology — IVIG, plasma exchange (PLEX/TPE), and rituximab — across Guillain-Barré syndrome, CIDP, myasthenic crisis, NMOSD relapse, and autoimmune encephalitis: which rescue to start, the exact doses and rates, how to sequence them without washing one out with the next, and when rituximab belongs. For the neurologist or intensivist admitting an acute antibody-mediated attack, and for the clinician writing the orders at 2 a.m.
Educational clinical decision-support, not medical advice — verify doses and eligibility against current labeling and guidelines before ordering.

!!! danger "🚩 Red flags — don't start immunotherapy before you check these"
    | Pattern | Worry | Do now |
    |---|---|---|
    | **Respiratory or bulbar weakness (MG crisis, GBS)** | Ventilatory failure — the clock is the airway, not the antibody | Admit to ICU/step-down, forced vital capacity + negative inspiratory force, secure the airway before debating IVIG vs PLEX |
    | **Rapidly progressive weakness with autonomic instability (GBS)** | Dysautonomia, arrhythmia, labile blood pressure | Continuous monitoring; IVIG is preferred over PLEX here — PLEX volume shifts worsen instability |
    | **Fever, untreated infection, or sepsis before rituximab** | B-cell depletion during active infection; HBV reactivation | Hold rituximab, treat the infection, screen HBsAg + anti-HBc first — see Step 3 |
    | **IgA deficiency with prior anaphylaxis, CKD, or thrombotic history before IVIG** | Anaphylaxis, acute kidney injury, thrombosis — the IVIG boxed warnings | For prior severe hypersensitivity/anaphylaxis, obtain specialist/pharmacy review of the exact product’s contraindications before any rechallenge. Low-IgA product selection alone does not make it safe. Address renal/thrombotic risks separately |
    | **Severe NMOSD attack (optic neuritis, myelitis, brainstem) and the clock is running** | Every day of delay costs vision and cord — complete recovery ~40% if PLEX starts within 2 days vs 3.7% if ≥7 days | Steroids + PLEX essentially simultaneously; do not finish a full steroid course first |

## Diagnosis / classification — which syndromes this page covers

This page is **therapeutics, not diagnosis**. It assumes the syndrome is already named. The five presentations it covers, with the rescue logic for each:

| Syndrome | Rescue principle | Durable control |
|---|---|---|
| **Myasthenic crisis** (impending or manifest) | PLEX **or** IVIG — equal efficacy in trials; expert consensus holds PLEX works faster | Rituximab once stable — especially MuSK+ or refractory disease |
| **Guillain-Barré syndrome** (unable to walk, GBS-DS ≥3, within 4 weeks of onset; or ambulatory but rapidly progressing / bulbar / respiratory risk) | IVIG **or** PLEX — equal efficacy; **never both routinely** | None — rituximab has no role in routine acute GBS; steroids alone are ineffective |
| **NMOSD relapse** (AQP4+ or seronegative) | High-dose steroids **plus early PLEX** — PLEX is primary therapy alongside steroids, not a salvage after steroid failure | Rituximab (or an approved mAb) after the PLEX course ends; oral steroid taper 3–6 months |
| **Autoimmune encephalitis** (esp. neuronal-surface antibody: NMDAR, LGI1, CASPR2) | Steroids **± IVIG or PLEX**, started early and empirically once infection is reasonably excluded | Rituximab as preferred second line; refractory → tocilizumab or bortezomib within ~1 month |
| **CIDP** (induction / maintenance) | IVIG first line in most; PLEX an induction alternative (5–10 sessions alternate days) | IVIG maintenance 1 g/kg q3wk, or rituximab for nodopathy / refractory disease — see [CIDP & IVIG order set](cidp.md) for the full CIDP workup |

**The one rule that governs the whole page:** IVIG and PLEX are the **rescue** therapies; rituximab is **not** a rescue drug. B-cell depletion takes weeks and does not lower existing antibody, because plasma cells are CD20-negative. Rituximab cannot replace PLEX in an acute attack — it is the bridge into maintenance, and it goes in **after** the rescue course ends.

## Rapid approach

1. **Secure the airway and the circulation first** — respiratory/bulbar status, dysautonomia, hemodynamics, venous access. That triage decides IVIG vs PLEX as much as the diagnosis does.
2. **Name the syndrome and the tempo** — fulminant/rapid (intubation, rising ventilation risk, NMOSD attack within 48 h, severe myelitis) favors PLEX for speed; autonomic instability, sepsis, poor access, or children favor IVIG.
3. **Order the rescue today, the durable control after** — pick IVIG or PLEX from the table below, run its order set, and plan rituximab (when indicated) only after the PLEX course is finished.

---

## The prescriptive flow (what I want done, in order)

1. **Confirm the syndrome and grade severity** — respiratory/bulbar exam, GBS disability scale, NMOSD attack severity (optic nerve / cord / brainstem), AE severity (ICU, status epilepticus/NORSE, dysautonomia, depressed consciousness).
2. **Run the shared pre-immunotherapy workup** (orderset below) — labs, serologies **before** IVIG (it causes false-positive antibody results for weeks), HBV screen before rituximab, infection screen, pregnancy test where applicable.
3. **Pick the rescue from the decision table** — IVIG or PLEX, matched to syndrome and tempo. Start it the same day; do not wait for antibody results in a fulminant attack.
4. **If the rescue is inadequate, switch by the rules, not by reflex** — GBS is the exception: routine IVIG→PLEX, PLEX→IVIG, or a second IVIG course for simple poor response is **not** recommended. MG crisis, NMOSD, and AE *do* allow sequential/escalating therapy — see the sequencing rules.
5. **Start durable control after rescue** — rituximab (when indicated) after the final PLEX session, never before or between sessions. Cover NMOSD with an oral steroid taper for 3–6 months, because early relapses after the first rituximab dose are described.
6. **Monitor for the therapy-specific harms** — IVIG: thrombosis and AKI (boxed warnings), hemolysis at 5–10 days; PLEX: hypotension, citrate toxicity, fibrinogen fall; rituximab: infusion reactions, infection, hypogammaglobulinemia, late-onset neutropenia. Disposition and follow-up below.

## Workup — shared pre-immunotherapy checklist

!!! orderset "Order before any of the three — do this first"
    - **CBC with differential, CMP (creatinine, LFTs), Na/K, Mg, ionized Ca** — baseline for IVIG (renal, hemolysis), PLEX (citrate, fibrinogen), and rituximab (neutropenia).
    - **Coagulation: PT/INR, aPTT, fibrinogen; blood type + antibody screen** — before PLEX, and before IVIG if plasma support could be needed.
    - **Draw clinically indicated antibody/infectious serologies before IVIG or PLEX when feasible**. Select AChR/MuSK, ganglioside, nodal/paranodal, AQP4/MOG, or neuronal panels by phenotype; do not send every panel for every syndrome or delay emergency rescue for send-outs. IVIG causes false positives that persist for weeks.
    - **Infection screen** — active infection review, fever workup; HCV, HIV, IGRA for TB (rituximab); do not give rituximab during a severe active infection.
    - **HBV screen before rituximab: HBsAg + anti-HBc in everyone** (add anti-HBs to characterize immunity). If either is positive: HBV DNA + hepatology, antiviral prophylaxis (entecavir or tenofovir) — see Step 3.
    - **Quantitative IgG / IgA / IgM before rituximab** — baseline IgG <3 g/L predicts infection risk; IgA status matters before IVIG if there is a history of severe/selective IgA deficiency or prior anaphylaxis.
    - **Pregnancy: β-hCG** before rituximab in patients of reproductive potential; contraception during treatment and for 12 months after the last dose per current product labeling, with individualized specialist counseling.
    - **Vaccines before rituximab** — pneumococcal, influenza, COVID-19, recombinant zoster ≥2–4 weeks before the first dose; if not VZV-immune, live varicella vaccine >4 weeks before. No live vaccines during B-cell depletion.
    - **Volume / cardiac / thrombotic risk assessment before IVIG** — age, immobility, prior VTE or arterial events, CAD, estrogens, central lines, hyperviscosity (cryoglobulins, marked hypertriglyceridemia, monoclonal gammopathy); ensure DVT prophylaxis in immobilized inpatients and hydration.
    - **Baseline brain MRI in MS** (rituximab) and **CD19+ B-cell count** (baseline; useful later if B-cell-guided redosing is planned).

## Management

### Choosing the rescue — decision table

| Syndrome | First rescue | Favor PLEX when | Favor IVIG when |
|---|---|---|---|
| **Myasthenic crisis** | PLEX **or** IVIG + ICU/step-down monitoring | Intubated, rapidly worsening, marked bulbar disease, need for fastest response — particularly MuSK-MG | Difficult vascular access, hemodynamic instability, sepsis, logistical preference |
| **GBS** | IVIG **or** PLEX (not both) | Either is effective; useful when IVIG unsuitable | Autonomic instability, children, PLEX access limited — often the simplest practical default |
| **NMOSD relapse** | IVMP 1 g/day × 3–5 days **+ very early PLEX** | Severe optic neuritis, longitudinal/extensive myelitis, major motor deficit, brainstem attack, rapid tempo, prior steroid-refractory attacks — start PLEX concurrently, don't wait for steroid failure | IVIG is **not** routine rescue in AQP4-NMOSD — the 2025 consensus recommends against it; use only if PLEX is contraindicated |
| **Autoimmune encephalitis** | IVMP ± IVIG or PLEX, started early | Fulminant antibody-mediated phenotype, severe dysautonomia/status epilepticus, concomitant demyelination, high thrombotic risk | Agitation/behavioral disease making line safety difficult, bleeding/coagulopathy concerns, easier logistics; IVIG has the best safety profile |
| **CIDP** | IVIG (see [CIDP page](cidp.md)) | Induction alternative when IVIG is unsuitable or has failed; 5–10 sessions alternate days | First line in most; maintenance 1 g/kg q3wk |

!!! orderset "Step 1 — IVIG order set (start here for most GBS / MG crisis / AE)"
    - **GBS: IVIG 0.4 g/kg/day × 5 days (total 2 g/kg)**, preferably begun within 2 weeks of weakness onset. **MG crisis / exacerbation: total 2 g/kg over 2–5 days** (1 g/kg/day × 2 days is acceptable in selected exacerbations; benefit begins in days to weeks, lasts 4–8 weeks). **CIDP induction: 2 g/kg over 2–5 days**, then maintenance **1 g/kg every 3 weeks** (practical range 0.4–1 g/kg q2–6wk, individualized to the lowest effective dose and longest interval; use objective response and an adequate trial before declaring failure; the ICE trial’s maintained week-24 INCAT response was **54% vs 21%** with placebo). **Severe AE: total 2 g/kg over 2–5 days.**
    - **Dosing weight:** dose on actual body weight in most patients; in obesity many centers use adjusted body weight to limit volume, viscosity, and thrombotic load.
    - **Infusion rates are product-specific — follow that product's label, never transplant a rate table between products.** 10% examples: Gammagard Liquid — start **0.5 mL/kg/h**, increase gradually as tolerated to max **5.4 mL/kg/h**; other 10% labels — start **0.5 mg/kg/min** for 15 min, increase every 15 min to max **8 mg/kg/min** (Gamunex-C starts 2 mg/kg/min → max 8 mg/kg/min; Privigen 0.5 → 8 mg/kg/min). Escalate stepwise ~every 15–30 min, checking vitals before each step. Use the slowest practicable rate for first-ever infusions, renal/thrombotic risk, IgA deficiency, or a product change.
    - **Premedication is NOT routinely required** — reserve acetaminophen + antihistamine (± hydrocortisone) for patients with prior infusion reactions.
    - **Monitoring:** vitals at baseline, each rate change, and end of infusion. BUN/creatinine before the first infusion and at intervals after. CBC/Hb, LDH, haptoglobin, DAT if symptomatic or high risk for hemolysis (~5–10 days post-infusion; non-O blood groups, high dose). Watch for aseptic meningitis (hours–2 days, worse with high dose or rapid rate), TRALI (within 6 h), and volume overload in heart failure.
    - **Boxed warnings: thrombosis and acute kidney injury.** Thrombosis ~1% per infusion in a neuropathy cohort (reported range 1–13%), mostly within 14 days — hydrate, use the minimum rate, split dosing, DVT prophylaxis. AKI risk is higher with CKD, diabetes, age >65, and sucrose-stabilized products — hydrate first and avoid sucrose products.
    - **Mild reactions:** slow or pause the infusion, restart at the last tolerated rate. **Anaphylaxis:** stop, give epinephrine; use a low-IgA product next time.
    - → **No routine second course in GBS** (SID-GBS: no benefit, more thrombosis). If no response, switch by the sequencing rules below — do not reflexively repeat IVIG. → **Step 2 if PLEX is the pick instead, or Step 3 for durable control.**

!!! orderset "Step 2 — PLEX order set (when PLEX is the pick)"
    - **Default prescription: 1.0–1.5 total plasma volumes (TPV) per session, ~5 exchanges over 7–14 days** (range 4–7; up to 10 in NMOSD). **GBS: 4–5 exchanges, 12–15 L total**, within 4 weeks of onset (best in the first week). **MG crisis: 5 sessions over 7–10 days** (no benefit to routinely extending beyond 5). **NMOSD: ~5 exchanges, daily or every other day, up to 10** — start within 2 days when severe. **AE: 5–7 exchanges every other day over ~10 days** (5 exchanges qod is the Canadian consensus regimen for severe AE). **CIDP induction: 5–10 sessions on alternate days.**
    - **Plasma volume:** Kaplan formula — **0.07 × weight (kg) × (1 − hematocrit)**. Removal is exponential: 1.0 PV removes ~63%, 1.5 PV ~78%.
    - **Replacement fluid: 5% (4.5–5%) albumin** as standard. **FFP only** for bleeding, low fibrinogen, or an impending procedure. Check fibrinogen serially — it falls ~60–70% per 1 PV albumin exchange; for hemorrhagic risk, maintain fibrinogen >1.0 g/L (100 mg/dL) with partial FFP replacement or post-PLEX cryoprecipitate (BSH target).
    - **Vascular access:** peripheral first whenever technically adequate — a **16–17 G apheresis/dialysis needle** is ideal (16–18 G cannulas at lower flows); centrifugal TPE runs ~50–120 mL/min. If central access is needed, use a short, rigid, large-bore dual-lumen apheresis/hemodialysis catheter (**11.5–12 Fr, internal jugular preferred**); ultrasound-guided, sterile placement, heparin or 4% citrate locks, tPA for occlusion, remove promptly after the course. Membrane TPE needs substantially higher flow and more often requires a dialysis-type catheter.
    - **Pre-PLEX checks:** CBC; Na/K/creatinine; ionized Ca, Mg; PT/INR, aPTT, fibrinogen; blood type/antibody screen. **Hold ACE inhibitors 24–48 h before PLEX** (bradykinin-mediated hypotension). Monitor vitals, BP/HR, symptoms, fluid balance, and access function during each session; reassess fibrinogen and ionized Ca serially during intensive (daily) courses.
    - **Hypotension (most common complication, ~12% of patients / 2.4% of sessions):** slow or pause PLEX, supine/Trendelenburg, restore intravascular volume — BSH gives **250 mL 0.9% saline** as the initial maneuver for vasovagal/hypovolemic events; assess for bleeding, anaphylaxis, arrhythmia. GBS with severe dysautonomia deserves especially conservative flow and volume management.
    - **Citrate toxicity / hypocalcemia:** progression is perioral/acral paresthesias → cramps/tetany → QT prolongation/arrhythmia. Slow citrate delivery, give oral or IV calcium by severity; prophylactic calcium is reasonable with prior citrate reactions, baseline hypoCa/hypoMg, liver/renal dysfunction, or high citrate exposure. Target ionized Ca >0.9 mmol/L. Plasma replacement adds substantial citrate — another reason albumin is preferred.
    - **Other complications:** catheter-related (pneumothorax, arterial puncture, bleeding, thrombosis, fibrin sheath, CLABSI — prevent with ultrasound guidance, proper locking, early removal); allergic reactions to albumin or FFP (~9.5%); infections between sessions (~12% in one cohort); removal of protein-bound drugs — give IV medications **after** the day's exchange.
    - **Steroids can run concurrently** — give after the session on PLEX days. **IgG replacement** if IgG falls below **150 mg/dL** after repeated courses (German MG guideline), given after PLEX is finished.
    - → **PLEX is the rescue, not the maintenance.** Plan the durable control (Step 3) while the course runs. → **Step 3.**

!!! orderset "Step 3 — rituximab order set (durable control — after rescue, never as the rescue)"
    - **Common adult schedule: rituximab 1,000 mg IV on days 1 and 15**, then maintenance every ~6 months — fixed schedule, or redosed when CD19 B cells return (common trigger CD19 >1% of lymphocytes; CD27+ memory B cells are an alternative and may need fewer infusions). Disease-specific regimens:
        - **Relapsing MS:** 1,000 mg days 1 and 15 (HERMES — 91% fewer Gd+ lesions vs placebo), or 1,000 mg × 1 then **500 mg q6mo** (RIFUND-MS — 3% relapses vs 16% on dimethyl fumarate over 24 months). OLYMPUS (primary progressive MS, 1,000 mg × 2 q24wk) missed its primary endpoint.
        - **AQP4+ NMOSD:** 1,000 mg days 1 and 15 (alternative 375 mg/m² weekly × 4); maintenance **1,000 mg × 2 (2 g/cycle) q6mo**, or redose when CD19 >1%. Lower-dose regimens (500 mg q6mo; 100 mg-based) come from observational studies only. Hopkins cohort: 2 g q6mo in most patients. MENACTRIMS 2026: extending the interval by CD19 return worked as well as fixed q6mo dosing.
        - **Generalized MG:** new-onset AChR+ — **500 mg × 1** (RINOMAX — 71% vs 29% reached minimal manifestations at week 16). Refractory / MuSK+ — **375 mg/m² weekly × 4**, or 1,000 mg × 2; redose at relapse or B-cell return (~6 months). BeatMG (375 mg/m² × 4, repeated at 6 months, established AChR+) showed **no steroid-sparing benefit** — best results are in MuSK+. In one MuSK cohort, 375 mg/m² weekly × 4 followed by 2 monthly doses had fewer relapses than 1 g × 2 (18% vs 80%).
        - **Autoimmune encephalitis (second line: NMDAR, LGI1, CASPR2):** 1,000 mg × 2, 2 weeks apart, or 375 mg/m² weekly × 4. Pediatric: 750 mg/m² × 2 (max 1 g/dose). Usually no maintenance; consider redosing at 6 months in selected relapsing NMDAR disease. Escalate after 2–4 weeks without response to first-line therapy — rituximab was the preferred second line of ~80% of experts.
    - **Infusion rates (label): first infusion start 50 mg/h, increase by 50 mg/h every 30 min to a maximum of 400 mg/h. Later infusions start 100 mg/h, increase by 100 mg/h every 30 min to 400 mg/h.** Dilute to 1–4 mg/mL. Do **not** import the accelerated 90-minute protocol as the default neurologic protocol — it is supported in selected lymphoma/chemotherapy circumstances only. SC rituximab (Rituxan Hycela) is not interchangeable, is not indicated for autoimmune disease, and must never be given IV.
    - **Premedication, 30 min before every infusion: acetaminophen + an antihistamine (e.g. diphenhydramine 50 mg) + methylprednisolone 100 mg IV.** Some centers add an H2 antagonist — institutional, not a universal evidence-based requirement.
    - **Infusion reactions** (most common adverse event, mostly the first dose, typically 30–120 min in): fever/chills, flushing, pruritus/urticaria, nausea, dyspnea, bronchospasm, hypoxia, angioedema, hypotension. **Mild–moderate:** stop the infusion, give antihistamine/acetaminophen ± steroid, then restart at **≥50% lower rate** once symptoms resolve. **Anaphylaxis, bronchospasm, or hypotension:** epinephrine, fluids, bronchodilators, steroids, oxygen. Recurrent or severe reactions: desensitization is preferred, or switch to a humanized anti-CD20. **Stop permanently after a life-threatening reaction.**
    - **HBV prophylaxis (if HBsAg+ or anti-HBc+): entecavir or tenofovir** with hepatology involvement — duration is **hepatology/guideline-directed**, commonly **at least 12 months after anti-CD20 therapy**, with longer follow-up or prophylaxis in selected settings. The FDA label warns of reactivation up to 24 months; it does not set a universal prophylaxis duration.
    - **Monitoring:** CD19 count about every 6 months, or before each dose if redosing is CD19-guided. IgG/IgM/IgA every 6 months or before each course — IgG falls progressively with cumulative dose; if IgG stays **<3–4 g/L with recurrent serious infections**, consider extending the dosing interval and starting Ig replacement. CBC with differential every 6 months, **plus whenever there is fever or infection**, to catch late-onset neutropenia. Ask about infections at each visit. Consider PJP prophylaxis if steroids or other immunosuppressants are given at the same time. Watch for HBV reactivation in patients with past infection.
    - **Risks to counsel on:** serious infections in 12.7% of an MS/NMOSD cohort; in RINOMAX follow-up, 12.5–18.8% had a severe infection — risk higher with age >65 and low IgG; IgG <500 mg/dL was associated with nearly a 3-fold adjusted risk of serious infection vs IgG ≥700 mg/dL (aHR 2.98). Hypogammaglobulinemia rises with cumulative exposure — reported in up to 44% of children treated for autoimmune CNS disease, where it can be severe. **Late-onset neutropenia:** in 2,686 Swedish MS patients, 6.2% had any episode, grade 3–4 in 1.0%, often with infection, at a median of 360 days after starting. **PML: very rare, but carries an FDA boxed warning** — new subacute cognitive, visual, motor, or coordination symptoms or suspicious MRI lesions should trigger withholding therapy; note that the serum JCV antibody index is **not** validated for rituximab PML risk stratification, so serial index testing does not reproduce the natalizumab algorithm. Other: HBV reactivation (can be fatal), impaired vaccine response, colitis/IBD-like illness, serum sickness; PRES and cardiac events reported.

### Sequencing rules — the part that gets people in trouble

| Sequence | Verdict | Why |
|---|---|---|
| **PLEX → IVIG** | Pharmacologically correct order | PLEX removes IVIG — always give IVIG **after** the PLEX course. In GBS it adds no benefit and is not recommended; in MG/AE it is acceptable as a bridge once PLEX is finished |
| **IVIG → PLEX** | Avoid, especially within 2 weeks of IVIG | PLEX washes out the infused immunoglobulin. If PLEX is truly needed (IVIG failure in crisis), accept the IVIG investment is lost — **there is no required two-week waiting interval for necessary rescue**. **Exception:** a life-threatening crisis deteriorating after IVIG — do not withhold necessary PLEX to preserve the IVIG dose |
| **PLEX → rituximab** | Correct — rituximab **after the last PLEX session** | PLEX 24–72 h after rituximab removes ~47–54% of the dose and cuts AUC by 26%. If rituximab cannot wait until PLEX is finished: dose at least 4–6 h after a session and leave ≥48 h before the next exchange; consider a supplemental dose if exchanges follow closely. No universal "safe 24-hour interval" or supplemental dose is validated — coordinate with pharmacy/apheresis |
| **Rituximab → PLEX** | Avoid | Same washout — hold biologics during PLEX: satralizumab, tocilizumab, inebilizumab, and natalizumab are large intravascular IgGs that PLEX removes efficiently; re-dose after the course |
| **IVIG + PLEX together (GBS)** | Do not combine routinely | No benefit over either alone (Hughes 1997, n=383); EAN/PNS explicitly does not recommend PE immediately followed by IVIG |
| **Second IVIG course (GBS)** | Not routine | SID-GBS: no benefit, more thrombosis. Lack of rapid improvement 5–10 days after IVIG in a ventilated GBS patient is **not** by itself an indication to wash out IVIG and try PLEX — axonal injury and delayed recovery explain persistent weakness |
| **Complement inhibitors + PLEX** | Supplemental dose required | PLEX substantially removes C5 inhibitors: **eculizumab — supplemental dose within 60 min after each session** (300 mg if the last dose was 300 mg, 600 mg if ≥600 mg); **ravulizumab — supplemental dose within 4 h**. FcRn blockers (efgartigimod, rozanolixizumab, nipocalimab) are also removed by PLEX and speed clearance of IVIG and other IgG monoclonals — reconcile every biologic with apheresis before the first exchange |

**Switching, by syndrome:**

- **MG crisis:** no response to IVIG → PLEX helped in retrospective series (do not delay necessary rescue to preserve the prior IVIG dose). In a prolonged severe crisis with inadequate response, sequential rescue is reasonable — and when both are planned, PLEX followed by IVIG is the favored order. Start steroids/immunosuppression after PLEX/IVIG; delay steroids a few days because they can cause transient worsening.
- **GBS:** treatment-related fluctuation (initial improvement/stabilization, then clear worsening) is different from poor response — retreatment with the **same** modality can be considered. ≥3 fluctuations or progression beyond ~8 weeks should trigger reconsideration of acute-onset CIDP or an autoimmune nodopathy rather than repeated empirical GBS treatment.
- **NMOSD:** insufficient recovery → repeat the apheresis course and/or steroids; immunoadsorption is an alternative to PLEX. Breakthrough relapse on rituximab: check CD19/CD27 repopulation and anti-drug antibodies, and switch to a monoclonal with a different mechanism (e.g. complement inhibitor or satralizumab). Prior poor response to steroids, or a good response to PLEX, in past attacks → PLEX first line next time.
- **AE:** unlike GBS, switching between first-line modalities is reasonable in refractory AE — if a steroid/IVIG strategy has clearly failed, PLEX can be added. First-line failure is defined as no improvement or worsening after **5–10 days in severe AE** vs ~2–4 weeks in mild/moderate disease (Canadian consensus 2024) — deliberately earlier in severe disease so second-line rituximab is not delayed. Refractory disease → tocilizumab or bortezomib within ~1 month.

!!! warning "Avoid"
    - **Rituximab as acute rescue** — it takes weeks to deplete B cells and does not touch existing antibody; it cannot rescue a respiratory, spinal-cord, optic-nerve, or encephalitic emergency.
    - **Routine IVIG for acute AQP4-NMOSD attacks** — the 2025 NMOSD consensus recommends against it; steroids + early PLEX is the rescue. (MOG-IgG-associated disease is different — the calculus changes.)
    - **Sequential PLEX + IVIG in GBS, or a second IVIG course for simple poor response** — no benefit, more harm.
    - **Transplanting infusion rates between IVIG products** — rates are product-specific; use the label for the product actually hanging.
    - **The 90-minute accelerated rituximab protocol as a neurologic default** — supported in selected lymphoma/chemotherapy settings, not as the neuroimmunology standard.
    - **Serial JCV antibody-index monitoring to stratify rituximab PML risk** — not validated; it does not reproduce the natalizumab algorithm.

!!! tip "TRICARE — verified rules and the current form"
    Confirm medical versus pharmacy benefit, exact product, indication, dose and site. IVIG brands do not share every approved indication; an infusion order does not establish insurance coverage. Current diagnosis-specific PA and continuation forms were not all obtainable in this review. Submit objective diagnostic evidence, prior therapy and safety/monitoring records rather than an invented universal failure threshold.

    [Current PA/MN details, benefit routing and packet](military/tricare.md) · [Live Formulary Search](https://www.express-scripts.com/frontend/open-enrollment/tricare/fst). Check the exact product, beneficiary and venue on the prescribing date.

## Disposition

- **Admit** every patient in this page's scope: MG crisis, GBS unable to walk or rapidly progressing, severe NMOSD relapse, severe AE — ICU or step-down with respiratory/bulbar monitoring, and apheresis + pharmacy coordinated before the first exchange.
- **Discharge only after** the rescue course is complete, the patient is stable off respiratory support, the durable-control plan is written (rituximab date, HBV/IgG/CD19 baselines drawn, vaccine plan), and the PLEX/IVIG washout rules are documented in the handoff so the next team does not undo the rescue.
- **Follow-up:** CIDP maintenance — INCAT / I-RODS / grip strength at each infusion to confirm response and guide tapering; try reducing dose every 6–12 months for the first 2–3 years. Rituximab — CD19 and IgG every ~6 months, CBC with any fever/infection, infection review at every visit. NMOSD — relapse-prevention therapy started before discharge; do not leave the patient on steroids alone.

!!! military "Military medicine — duty, retention and deployment"
    - **Profile / function:** Assess the underlying disease and treatment effects; record infection, infusion and monitoring risks in functional terms.
    - **Retention / MEB–MAR2:** Retention follows the underlying condition and Service standard. Receiving an infusion alone is not the same as a PEB finding. Use the [retention framework](military/deployability.md); permanent P3/4 does not by itself select DES versus MAR2.
    - **Deployment / medications:** CENTCOM lists injectable and immunosuppressive/immune-modifying treatments. Self-injection does not bypass waiver review; describe vaccine, lab, cold-chain and missed-dose requirements. See [the disease AND drug screen](military/deployment-medications.md) for the current CENTCOM rules and waiver packet.
    - **Special duty:** flight, diving and other special assignments have separate standards and waiver authorities; a general duty profile does not clear them.
    - **LOD / EPTS:** document onset, duty status, exposures and aggravation objectively. The designated authority determines LOD/EPTS; neither in-service diagnosis nor a genetic finding settles it automatically.

---

## 📚 Discover — evidence brief

*Written from primary guidelines and trials; source articles are a reading list, not copied.*

- **Rescue first, durable control second** is the organizing principle: IVIG and PLEX work in days; rituximab works in weeks and cannot rescue an acute attack. Every sequencing error on this page — PLEX after IVIG, rituximab before PLEX — is a washout error.
- **GBS is the exception to "switch if it didn't work."** IVIG and PLEX are equally effective, combining them adds nothing, a second IVIG course adds harm (SID-GBS), and persistent weakness 5–10 days after IVIG is usually axonal injury and slow recovery, not a failed drug. Treatment-related fluctuation is the one pattern where retreatment makes sense.
- **NMOSD is the opposite: move PLEX early.** The 2025 NMOSD consensus and current NMOSD attack-management guidance put apheresis alongside high-dose steroids as primary therapy, with 5–7 alternate-day exchanges preferably within ~5 days of onset, and explicitly recommend against routine IVIG for acute AQP4-NMOSD attacks.
- **Rituximab's evidence is trial-anchored but off-label in all four conditions.** RIFUND-MS (1 g → 500 mg q6mo), RINOMAX (single 500 mg in new-onset MG), and the Hopkins NMOSD cohort (2 g q6mo) give the dosing; the label still governs infusion rates, premedication, and HBV screening. The 2026 OVERLORD-MS data and the Swedish late-onset-neutropenia cohort (n=2,686) are the newest safety/efficacy signals.
- **What changed recently:** NEMOS attack-management recommendations and subsequent NMOSD consensus reposition PLEX from salvage to primary therapy; the 2024 Canadian AE consensus formalizes earlier second-line escalation in severe disease (5–10 days, not 2–4 weeks).

**Key sources:** 2023 EAN/PNS GBS and **2021 EAN/PNS CIDP** guidelines; AANEM IVIG consensus (Muscle & Nerve 2023, Tavee et al.); ASFA guidelines on therapeutic apheresis; ICE trial (CIDP); HERMES and RIFUND-MS (rituximab in MS); RINOMAX (rituximab in new-onset MG); NEMOS / 2025 NMOSD consensus; Canadian consensus on autoimmune encephalitis (2024); 2024 Nordic MG guidance.

## References

1. Shahrizaila N et al. [*Guillain-Barré syndrome.* Lancet. 2021](https://doi.org/10.1016/S0140-6736(21)00517-1) — GBS presentation, IVIG vs PLEX equivalence, treatment-related fluctuation.
2. van Doorn PA, Van den Bergh PYK, Hadden RDM, et al. [*European Academy of Neurology/Peripheral Nerve Society guideline on diagnosis and treatment of Guillain-Barré syndrome.* Eur J Neurol. 2023](https://doi.org/10.1111/ene.16073) — GBS: IVIG 0.4 g/kg/day × 5 days or PLEX 4–5 exchanges/12–15 L; do not combine; no routine second course.
3. Van den Bergh PYK et al. [*European Academy of Neurology/Peripheral Nerve Society guideline on diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy.* Eur J Neurol. 2021](https://doi.org/10.1111/ene.14959) — CIDP induction 2 g/kg, maintenance individualized from 1 g/kg q3wk; PLEX 5 exchanges over 2 weeks.
4. Tavee J et al. [*Updated consensus statement on IVIG in neuromuscular disorders (AANEM).* Muscle & Nerve. 2023](https://doi.org/10.1002/mus.27922) — IVIG dosing, pre-infusion screening, thrombotic/renal risk, product-specific rates.
5. Narayanaswami P, Sanders DB, Wolfe G, et al. [*International Consensus Guidance for Management of Myasthenia Gravis: 2020 Update.* Neurology. 2021](https://doi.org/10.1212/WNL.0000000000011124). See also [the 2016 consensus](https://pmc.ncbi.nlm.nih.gov/articles/PMC4977114/) for IVIG/PLEX rescue principles.
6. Kümpfel et al. [NEMOS revised NMOSD recommendations, Part II — attack therapy and long-term management](https://pmc.ncbi.nlm.nih.gov/articles/PMC10770020/).
   Severe attacks may need early combined steroid/apheresis treatment; the claimed 2026 ASFA edition/category upgrade was not verified and is not relied upon here.

7. Svenningsson A et al. [*Safety and efficacy of rituximab versus dimethyl fumarate in relapsing-remitting multiple sclerosis (RIFUND-MS).* Lancet Neurol. 2022](https://doi.org/10.1016/S1474-4422(22)00209-5) — rituximab 1,000 mg × 1 then 500 mg q6mo; 3% vs 16% relapses.
8. Hauser SL et al. [*B-cell depletion with rituximab in relapsing-remitting multiple sclerosis (HERMES).* N Engl J Med. 2008](https://doi.org/10.1056/NEJMoa0706383) — rituximab 1,000 mg × 2; 91% fewer Gd+ lesions.
9. Wu J et al. [*Rituximab in new-onset generalized myasthenia gravis: long-term follow-up of the RINOMAX clinical trial.* Eur J Neurol. 2025](https://doi.org/10.1111/ene.70418) — long-term follow-up. The **71% vs 29% week-16 result** comes from the [2022 RINOMAX randomized report](https://doi.org/10.1001/jamaneurol.2022.2887).
10. Hahn C, Budhram A, Alikhani K, et al. [*Canadian consensus guidelines for the diagnosis and treatment of autoimmune encephalitis.* 2024](https://doi.org/10.1017/cjn.2024.16) — severe AE: steroids + IVIG or PLEX from the outset; first-line failure 5–10 days (severe) vs 2–4 weeks (mild/moderate); rituximab preferred second line.
11. **Rituxan (rituximab) US prescribing information** (Genentech; DailyMed) — infusion rates (first 50 mg/h → max 400 mg/h; subsequent 100 mg/h → 400 mg/h), premedication (acetaminophen + antihistamine + methylprednisolone 100 mg IV), HBV boxed warning, PML boxed warning, contraception 12 months.
12. **Gammagard Liquid (immune globulin intravenous) US prescribing information** (FDA label, updated 2025-12-10) — CIDP dosing and infusion-rate titration (start 0.5 mL/kg/h → max 5.4 mL/kg/h); thrombosis and AKI boxed warnings.
- [Official TRICARE sources, retrieved forms and access limits](military/tricare.md).

*Evidence/policy audit: 21 November 2026. Material changes were checked against the linked primary sources; this is an AI-assisted review, not certification of every dose or claim. [Review scope and source limits](evidence-review.md).*
