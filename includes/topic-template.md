# <Topic name>

<!--
  CANONICAL FORMAT = the "Headache" style. Every write-up follows this.
  The hallmarks (don't drop them):
    • A "The prescriptive flow (what I want done, in order)" numbered block.
    • Tiered `!!! orderset` boxes — Step 1 → 2 → 3 — WITH DOSES on every drug.
    • Decision tables (comorbidity → agent, situation → target, etc.).
    • A `!!! tip "TRICARE — ..."` box wherever drugs are prescribed
      (verified product, benefit, indication, PA/MN and source date; use Formulary Search).
    • The standardized `!!! military` box (fixed 5 fields).
    • A "📚 Discover" evidence brief + linked References + a "*Evidence/policy audit: DD Month YYYY. ...*" footer.
  Prescriptive > comprehensive: the reader should know EXACTLY what to do at each step.
  See docs/headache/migraine.md as the reference implementation.
-->

<span class="reviewed-stamp">Last reviewed: MON YYYY</span>

**One-liner:** <one-sentence gestalt — what this is and who this page is for (the on-call neuro /
PCP seeing this in the ER, on admit, or in clinic).>

!!! danger "🚩 Red flags — <what must not be missed / when to image now>"
    | Pattern | Worry | Do now |
    |---|---|---|
    | <finding> | <dangerous cause> | <immediate action / imaging> |

## Diagnosis / classification

<Criteria or phenotype buckets, stated precisely. Cite the actual criterion (ICHD-3 / ILAE /
McDonald / AHA-ASA / etc.) — quote thresholds exactly, don't paraphrase loosely.>

## Rapid approach

1. <exclude the dangerous thing first>
2. <classify / localize>
3. <route to the tiered management below>

---

## The prescriptive flow (what I want done, in order)

1. <confirm / work up>
2. <Step 1 treatment, matched to the patient>
3. <what to do if that's inadequate → Step 2>
4. <escalation → Step 3 / refractory>
5. <disposition + follow-up>

## Workup

<Labs / imaging / LP / other. State clearly when NO work-up is needed. Use an `!!! orderset`
box if there's a mandatory test set to order.>

## Management

!!! orderset "Step 1 — first-line (start here for most)"
    - **<Drug>** — **<dose, route, titration>**; <monitoring / key caution>.
    - → <what defines failure / when to move on> → **Step 2**.

!!! orderset "Step 2 — <second-line / if Step 1 fails or is contraindicated>"
    - **<Drug>** — **<dose>**; <note>.

!!! orderset "Step 3 — <refractory / escalation / procedural>"
    - **<Option>** — <dose / referral>; <trade-offs>.

<Use decision tables and `=== "tabs"` for parallel option sets keyed to comorbidity, e.g.:>

| Patient / comorbidity | Preferred agent | Target dose | Watch for |
|---|---|---|---|
| <comorbidity> | **<drug>** | <dose> | <caution> |

!!! warning "Avoid"
    - **<agent/approach>** — <why it's wrong here>.

!!! tip "TRICARE — <topic> prescribing"
    <Give product-specific coverage details supported by the current form. State which criteria
    are unavailable and link the TRICARE access guide and live Formulary Search.>

## Disposition

<Admit vs discharge criteria; follow-up interval.>

!!! military "Military medicine — <topic>"
    *Framework — verify against current **AR 40-501**, **DoDI 6130.03**, **DoDI 1332.18**, service
    deployment/aeromedical policy (and any relevant JTS CPG) before counseling.*

    - **Deployability:** <condition and medication effects under the current destination’s policy>
    - **Profile (DA Form 3349):** <temporary vs permanent; functional limits>
    - **EPTS / LOD:** <onset / pre-service considerations>
    - **Retention (AR 40-501 / DoDI 6130.03):** <threshold that triggers review — cite the para>
    - **MEB / IDES:** <when to refer; documentation that carries a board>
    - **Aeromedical / special duty:** <flight-status / waiver considerations>

---

## 📚 Discover — evidence brief

*Written from primary guidelines and trials; source articles are a reading list, not copied.*

- <what's current / what changed and why it matters>
- <key practice-changing points>

**Key sources:** <guideline(s); landmark trial(s)>.

## References

1. <Author et al. [*Title.* Journal. Year](https://doi-or-url) — one-line note on what it anchors.>
2. **TRICARE / DoD Uniform Formulary:** <preferred/PA status of the drugs on this page>. *Verify at
   the TRICARE Formulary Search.*

*Evidence/policy audit: DD Month YYYY. <Describe what was checked, the primary sources, and remaining limitations.>*
