# How to add a topic

**Every clinical page follows the "Headache" format** — the tiered, prescriptive style used across
the Headache and Stroke pages. The canonical reference implementation is
[`docs/headache/migraine.md`](headache/migraine.md); the fill-in skeleton is
`includes/topic-template.md`. To add a page:

1. Copy `includes/topic-template.md` to `docs/<area>/<topic>.md`.
2. Fill in each section. Delete sections that truly don't apply, but keep the **order** and the
   **format hallmarks** below.
3. Add the page to the `nav:` list in `mkdocs.yml`.
4. Preview locally (`mkdocs serve`), build with `mkdocs build --strict`, then commit and push — the
   site redeploys automatically.

## Format hallmarks (the "Headache" style — don't drop these)

- **Prescriptive, not just comprehensive.** The reader should know **exactly what to do at each
  step** — this is "what the neurologist wants you to do first, second, third."
- **A "The prescriptive flow (what I want done, in order)" numbered block** near the top of
  management.
- **Tiered `!!! orderset` boxes — Step 1 → 2 → 3 — with a DOSE on every drug** and an explicit
  "what defines failure / when to escalate" between tiers.
- **Decision tables** (comorbidity → agent, situation → target) and `=== "tabs"` for parallel
  option sets.
- **A `!!! tip "TRICARE — …"` box wherever drugs are prescribed** — name the preferred/no-PA go-to
  vs the PA-gated agents (and what the PA requires); always tell the reader to verify at the TRICARE
  Formulary Search.
- **The standardized `!!! military` box** (fixed 5 fields).
- **A "📚 Discover" evidence brief, linked References, and a `*Verified MON YYYY: …*` footer** that
  states what was source-checked and flags anything that could not be confirmed.

## The standard sections (in order)

1. Title + `Last reviewed: MON YYYY` stamp
2. One-liner + who it's for
3. 🚩 Red flags / when to image now (`!!! danger`)
4. Diagnosis / classification (quote criteria exactly)
5. Rapid approach (numbered)
6. **The prescriptive flow (what I want done, in order)**
7. Workup (labs / imaging / LP — an `!!! orderset` if there's a mandatory set)
8. Management — **tiered `!!! orderset` Step 1→2→3 with doses**, decision tables, `Avoid` box
9. **TRICARE prescribing box** (`!!! tip`) wherever drugs appear
10. Disposition
11. Military box (`!!! military`)
12. 📚 Discover — evidence brief
13. References + `*Verified MON YYYY*` footer

## Custom callout boxes

This site defines two custom admonitions in addition to the Material defaults:

```markdown
!!! danger "🚩 Red flags"
    Emergent / must-not-miss items.

!!! orderset "Step 1 — first-line"
    Copy-pasteable, dosed orders. Tier as Step 1 → 2 → 3.

!!! tip "TRICARE — <topic> prescribing"
    Preferred/no-PA go-to vs PA-gated agents; verify at the TRICARE Formulary Search.

!!! military "Military medicine — <topic>"
    The five fields: deployability, profile, EPTS/LOD, retention, MEB/IDES.
```

## Ground rules

- **Copyright:** write Discover briefs **in your own words** and cite. Source PDFs are a reading
  list — never paste from Continuum, UpToDate, or similar.
- **Currency:** update content to current evidence **before** stamping a review date. No
  hand-waved dates.
- **De-identify:** no PII, no real lot numbers, no patient specifics.
- **Military content:** published-doctrine level only; verify against current AR 40-501 / DoDI
  1332.18 / aeromedical policy; nothing sensitive.
- **Disclaimer:** the site-wide educational-use disclaimer applies to every page.

## Abbreviations

Common acronyms are defined once in `includes/abbreviations.md` and auto-expand on hover across
every page. Add new ones there rather than redefining them per page.
