# Changelog — dementia section (6 pages)

**First section-level review.** One machine pass, one OpenEvidence round, two agents, one gate —
instead of six separate cycles. **1,574 → 1,750 lines** across six pages.

| Stage | Cost | Yield |
|---|---|---|
| A — scripts, all 6 pages | shell only | trazodone's missing boxed warning; every dose label-verified |
| B — OpenEvidence, section-wide | free, 54 sources | 3 conflicts, 18 findings, and the Part 2 claim check covered all six pages at once |
| D — `military-tricare` | 78,349 tokens, 17 calls | primary claim **verified verbatim**; profile factor wrong on every page |
| D — `page-safety` (RPD only) | 70,422 tokens, 9 calls | **4 HIGH, including a cross-page dose contradiction** |

---

## The finding of the review

**`docs/seizure/index.md` prescribed `thiamine 100 mg IV` — the exact maintenance dose the
rapidly-progressive page warned against, two clicks away, on the acute page a tired reader
actually checks.** The RPD page said "use your local Wernicke protocol"; at a Role 2, afloat, or
a critical-access hospital there is no local protocol, so the reader falls back on the site's own
number. **Both pages fixed in the same pass** — RPD now carries **500 mg IV q8h**, and the seizure
page now distinguishes prophylaxis from treatment.

No script and no evidence tool could find this. It required reading two pages against each other.

## Other HIGH safety findings

- **Aciclovir** — "empirically **while PCR is pending**" reads as a stop condition. **A negative CSF
  HSV PCR in the first 72 hours does not exclude HSV encephalitis**, and that is exactly the window
  a page urging speed produces. Now dosed (**10 mg/kg IV q8h**), with the repeat-LP instruction.
- **Pre-steroid checklist added.** The page's own differential includes primary CNS lymphoma, and
  its Avoid box was pushing readers toward steroid-before-tissue. **Steroids melt PCNSL**; the
  biopsy becomes non-diagnostic for months.
- **The hub routed RPD patients off the pathway.** Its delirium red flag said *"find the cause; do
  not diagnose dementia in a delirious patient"* and its flow said *"Stop here."* Encephalitis
  presents exactly that way. Both rewritten as a **fork, not a stop.**

## Military — verified verbatim, and one error on every page

**The load-bearing claim holds.** `DoDI 6130.03 Vol 2 5.26.d` reads *"permanent or progressive
cognitive impairment… **Paragraph 5.26.a. does not apply**"* — and that sentence appears **exactly
twice in all of para 5.26**, at dementia and epilepsy. The inverse-posture framing stands.

Corrections:

- **Profile factor was S on every page; it should be P.** DA Pam 40-502 assigns the nervous system
  to P and confines S to personality and emotional stability. Six pages fixed.
- **`3-31k` carries its own "after adequate treatment" gate that 5.26.d waives** — so citing it as
  the lead invites the reviewer to ask what treatment was tried. **5.26.d is now cited as operative.**
- **Named subparagraphs beat the catch-all** on three pages: **3-31d** (DLB), **3-31f** (vascular),
  **3-31j** (TBI substrate).
- **Aeromedical: `AR 40-501 4-27i` names dementia and Alzheimer's outright** — the drafts cited 4-27
  generically. The accession paragraph is **6.26.d**, **not 6.26.q**, which the botulism page used
  and which does not fit.
- **`MAR2` is affirmatively not the pathway** for established dementia — no page said so.
- **The trigger is "permanent or progressive," not the word "dementia."** No page quoted it, and it
  is the doctrinal basis for the RPD page's argument that 5.26.d **does not engage at all** until
  permanence is established.

**Structure changed:** the hub now carries the full framing; the five disease pages carry **only
their deltas**. That removed roughly five near-identical boxes.

## Clinical corrections from OpenEvidence

**The 2024 Alzheimer's Association Revised Criteria** replace the NIA-AA framework — AD is now
defined **biologically**, diagnosable on a Core 1 biomarker **without symptoms**. Applied to the
amyloid prevalence figures (**33% of cognitively normal 80-year-olds**), that is contested, and the
pages now take a position: **characterise the symptomatic, do not diagnose the asymptomatic.**

- **A second FDA-approved agent for agitation in AD exists** — **dextromethorphan/bupropion
  (Auvelity, 2026), the first non-antipsychotic.** The page called brexpiprazole "the" agent.
- **Full ARIA management protocol** added, plus numeric exclusions (**>4 microhaemorrhages, ≥1
  macrohaemorrhage**) and real effect sizes in place of adjectives.
- **Reversible dementia corrected downward** — 9–23% potentially reversible, **only ~11% actually
  resolve.** The screen is still mandatory; the honest reason is contributors, not reversal.
- **Hearing loss reframed** — **ACHIEVE was negative overall.** Risk-modifying, not treatment.
- **Driving thresholds by CDR stage**, with the note that **DLB and FTD impair driving at milder
  stages** so the AD thresholds do not transfer.
- **DLB neuroleptic sensitivity softened** — the consensus criteria list it as **supportive with no
  percentage**; **cholinesterase inhibitors go first.**
- **RT-QuIC given its real numbers**, including that sensitivity falls to **44–78% in MM2**, so a
  negative does not exclude.

## Where the machine pass beat OpenEvidence

**First time in five reviews.** OE listed **subcutaneous lecanemab as investigational**; the current
label (eff. 2026-07-21) carries the **LEQEMBI IQLIK autoinjector** with full dosing. A script that
reads the label is simply more current on regulatory fact than a literature-retrieval tool. **The
two sources fail in opposite directions, which is the argument for running both.**

## Tooling

`label_diff.py` — stoplisted seven more phrase classes openFDA fuzzy-matched as drugs (including
`enhanced clinical`, which returned a **hand-sanitizer label**), and fixed a real bug: **`increas\\b`
can never match "increasing"**, so correctly-titrated pages were being silently flagged as missing
an induction phase.

`lint_page.py` — added the **delta-box rule**: a military box that explicitly defers its framing to
a hub page is no longer held to the five-field requirement. Verified this does not mask real gaps —
17 MIL-FIELDS warnings still fire site-wide.

`page.md` — now supports **section mode**, consolidated artifacts, and a standing instruction not to
stop a review to perfect the tooling.

## Not done

- **`Last reviewed:` stamps still say August 2026** from drafting — they were never author-approved
  and need confirming at the gate.
- **TRICARE tier and PA criteria** unverified across all six pages (stated on each).
- **USAAMA practice, non-Army service standards, Reserve/Guard pathways** — all flagged.
- **Auvelity's agitation dosing was not label-pulled** — named without a dose, and said so.
- TRICARE boxes on `lewy-body`, `frontotemporal` and `vascular` could still be reduced to pointers
  (military reviewer's F-12); left as-is this pass.
