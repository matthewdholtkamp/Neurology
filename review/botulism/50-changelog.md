# Changelog — docs/nmj/botulism.md

**151 → 584 lines.** One agent. Third page through the pipeline, second through the
rebuilt version.

| Stage | Cost | Yield |
|---|---|---|
| **A — scripts** | 4 shell commands | 1 HIGH (BabyBIG undosed) — **label supplied the fix**; EPTS/LOD gap; **BAT proved absent from openFDA** |
| **B — OpenEvidence** | free, 127 sources | 3 outright corrections, ~20 additions, and the entire airway rewrite |
| **C — triage** | — | `page-safety` **not spawned** |
| **D — one agent** | 86,411 tokens, **13 tool calls** | 12 findings, 3 HIGH, wrote its own file |

---

## Three positions that were wrong, not merely thin

| Was | Now | Source |
|---|---|---|
| *(silent — older references mandate skin testing before equine antitoxin)* | **Skin testing must not delay BAT.** Predictive values were poor for older non-despeciated products; anaphylaxis with modern BAT is ~0.6–1.6% and **no fatal anaphylaxis has ever been reported with any botulinum antitoxin** | AAAAI/CDC workgroup |
| "Every hour of delay is more toxin bound" — implies a closing window | **No interval has been identified beyond which antitoxin stops being beneficial.** Toxin found in serum **11–12 days** after ingestion; benefit documented at day 15 in iatrogenic cases. **Give it while paralysis progresses** | O'Horo meta-analysis; Fagan 2009 |
| Iatrogenic botulism "usually mild/localized, **occasionally systemic**" | **195 cases at one Chinese centre in two months** — 26.2% severe, **16.4% ventilated**. England seized vials assaying **370 U against a 200 U label**. It is **product counterfeiting, not labelled dose** | An 2025; UKHSA 2025 |

## The airway section, rewritten around a fact it never stated

**Airway obstruction and aspiration precede hypoventilation** — the paralysis is bulbar-first, so
the airway fails before the bellows. Consequences the page now carries:

- **Intubate for loss of gag or cough regardless of numbers.** In infant botulism the principal
  indication was loss of protective reflexes, not gas exchange.
- **No botulism-specific threshold has ever been validated.** The 20/30/40 rule comes from a
  Guillain-Barré cohort; the JAMA consensus statement deliberately gives **no numeric cutoff**.
- **The vital capacity you measure may be falsely low** — facial diplegia breaks the mouthpiece
  seal (~200 mL even in normals). Use a facemask interface.
- **NIV should be actively discouraged** — a real reversal from the [MG page](../../docs/nmj/index.md),
  where a third of NIV trials succeed. Bulbar failure plus secretions is exactly where it fails.
- Botulism-specific predictors added: **postprandial hypotension aOR 8.33**, ptosis severity,
  pupillary dilation; **sporadic cases 85% intubated vs 42% in outbreaks**.

## The diagnosis caveat that matters most

**17% of patients report paresthesias, 13% have raised CSF protein, and 7% are frankly atypical** —
unilateral cranial findings, even ascending paralysis. Those are precisely the findings a clinician
uses to rule botulism *out*. Of 332 CDC cases the differential named **GBS in 99 and MG in 76**; in
one outbreak all 28 patients were initially misdiagnosed, four as psychiatric illness.

Also added: **a negative electrodiagnostic study cannot exclude botulism** — facilitation appears in
only 50–60%, is less dramatic than in LEMS, and **decays with time**.

## What the one agent found that nothing else could

- **There is no botulism vaccine, and the record may suggest otherwise.** The pentavalent (ABCDE)
  toxoid given under **IND 161** (CDC) and **IND 3723** (US Army) was **discontinued 30 Nov 2011**.
  **A documented series is not protection and must not delay antitoxin.** The agent then verified
  locally that **AR 40-562 contains zero botulinum entries** — 0 hits against 16 for anthrax and 26
  for smallpox — so there is no immunization requirement to enforce or waive.
- **`5.26.i` is the right DoD hook here — the opposite of the LEMS answer.** Its permanence
  qualifier worked *against* the LEMS page; in botulism, where the whole question is residual
  deficit at MRDP, "paralytic disorders resulting in permanent functional impairment" is exactly
  what is being asked. **The reviewer explicitly declined to copy its own prior advice across.**
- **The aeromedical chain must not be copied either.** `6.26.q` requires a **chronic** nervous
  system disorder and does not reach a resolved acute intoxication. The right hook is **`6.26.n`**
  (which names Guillain-Barré), framed on the **4-27g** model — *"until complete recovery"* —
  making this a **temporary medical suspension, not disqualification.**
- **The commonest correct MEB answer is "no board at all."** On MG and LEMS the risk is
  under-referral; here it is **over-referral** — boarding a recovering Soldier or writing a
  permanent profile before rehabilitation has plateaued.
- **Do not close the profile at extubation** — ventilation averages ~56 days in type A, and 68% of
  survivors report worse health at 4.3 years.
- **"CDC Category A select agent" conflated two regimes** — Category A is CDC bioterrorism tiering;
  **Tier 1 Select Agent is regulatory status under 42 CFR Part 73**, and it is the one that creates
  independent laboratory-exposure reporting obligations.
- A **TRICARE box that is an access-path box, not a formulary box**: BAT is never prescribed,
  ordered or purchased.

## Where the agent pushed back on its own tasking

I told it BAT and BabyBIG are both released through public health at no cost. **It agreed for BAT
and refused for BabyBIG** — the CDPH programme bills for the product, making it a coverage question
for a dependent infant. It could not confirm that within budget, **flagged it VERIFY, and declined
to state it as free.** The page is hedged accordingly. That is the correct behaviour and worth
recording.

## One thing deliberately NOT written

**BAT's paediatric dosing.** It is absent from the openFDA drug-label API, the paediatric schedule
is an age-band percentage table, and reproducing that from a secondary source is a realistic route
to a paediatric overdose. The page states the **one-vial adult rule** and points to the insert as
controlling — and says so in the footer rather than hiding it.

## Verification

- `python3 tools/lint_page.py docs/nmj/botulism.md` → **clean**
- `python3 tools/label_diff.py docs/nmj/botulism.md` → **0 flags**
- `mkdocs build --strict` → **exit 0**

## Tooling fixes this page earned

`label_diff.py` was reading `Population: Drug` bullets backwards — it invented a drug called
`infants` while **never checking BAT or BabyBIG at all**. Now it takes post-colon text (gated to
genuine population heads, after a first attempt invented a drug called `hbsag`), and harvests
**brand names from parentheses**, which is the only reason BabyBIG resolved. All three regression
checks pass: the pre-review MG page still fires both headline catches; reviewed MG and LEMS stay
quiet.

## Not done

- **`Last reviewed:` stamp not touched.**
- **DoDI 6200.03**, the *Armed Forces Reportable Medical Events Guidelines*, and **AR 600-8-4** were
  cited from doctrinal knowledge and not available locally — flagged in the ledger.
- `nerve-agent.md` remains the last unreviewed NMJ page.
