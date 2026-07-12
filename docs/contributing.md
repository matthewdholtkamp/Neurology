# How to add a topic

Every clinical page follows the same skeleton so users build muscle memory. To add one:

1. Copy `includes/topic-template.md` to `docs/<area>/<topic>.md`.
2. Fill in each section. Delete sections that truly don't apply, but keep the **order**.
3. Add the page to the `nav:` list in `mkdocs.yml`.
4. Preview locally (`mkdocs serve`), then commit and push — the site redeploys automatically.

## The standard sections

1. Title + `Last reviewed: MON YYYY` stamp
2. One-liner + who it's for
3. 🚩 Red flags / when to image now (`!!! danger`)
4. Rapid approach (numbered algorithm)
5. Focused H&P + exam
6. Workup (labs / imaging / LP)
7. Management by diagnosis
8. Order set (`!!! orderset`)
9. Disposition
10. Military box (`!!! military`)
11. 📚 Discover — evidence brief
12. References

## Custom callout boxes

This site defines two custom admonitions in addition to the Material defaults:

```markdown
!!! danger "🚩 Red flags"
    Emergent / must-not-miss items.

!!! orderset "Order set"
    Copy-pasteable orders.

!!! military "Military medicine — <topic>"
    The five questions: deployability, profile, EPTS/LOD, retention, MEB/IDES.
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
