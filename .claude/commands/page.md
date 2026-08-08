---
description: Run the review pipeline on a Neuro Scutbook page or a whole section — free scripted checks and OpenEvidence first, paid reviewers only if there is signal
argument-hint: "<slug, docs/ path, or section dir> [quick|standard|deep]  — blank lists in-flight reviews"
---

# /page — the page review pipeline

Target: **$ARGUMENTS**

You are the orchestrator. **All state lives in files under `review/<slug>/`, never in
conversation** — that is what lets this resume in a chat that has never seen the
earlier work.

## The economics, because they drive the design

The first full run of this pipeline cost ~735k tokens, ~80% of it in five parallel
reviewer agents. Rebuilt to put the **free** work first:

| Source | Cost | What only it can do |
|---|---|---|
| `tools/*.py` | free | FDA label facts, format conformance, trial pulls. **Deterministic comparisons, which a model should never be paid to do.** |
| **OpenEvidence** | **free** | Current practice, guideline conformance, quantitative claim-checking, sequencing. Catches things labels don't contain. |
| `page-safety`, `military-tricare` | expensive | Reading *this page* as a clinician; AR 40-501 / TRICARE |

**Agents are the exception, not the default.** Many pages will finish without one.

## Section mode — the default when a slug names a directory

**If `$ARGUMENTS` resolves to a `docs/` directory with more than one page, review the WHOLE
SECTION as ONE cycle.** Do not loop the pipeline once per page. This is the single largest
cost lever in the system and it costs nothing in evidence, because the sources are identical
across a section:

- **One** machine pass — run `lint_page.py` and `label_diff.py` over every page in the
  directory and put the combined result in `15-machine.md`.
- **One** OpenEvidence round. Build the pack to cover the section: Part 1 draws its practice
  questions from whichever pages are weakest, and **Part 2's claim check lists every number
  across every page.** One paste, one gate.
- **One** `military-tricare` pass, run against the **hub**, instructed to establish the
  **section-wide framing** that the sub-pages will inherit.
- **`page-safety` only on the specific pages that warrant it** — usually one, sometimes none.
  Name which and why.
- **One** `40-ledger.md`, **one** `50-changelog.md`, **one** Gate 2, **one** commit.

**Write the military box once.** The hub carries the full framing; each sub-page carries only
what genuinely differs for that disease. Six near-identical military boxes is six times the
text to write, verify and drift.

## Depth

Read the last word of `$ARGUMENTS`:

- **`quick`** — Stages A–B only. Never spawns an agent. Right for hub pages, short
  pages, and re-checks.
- **`standard`** (default) — agents spawn **only if Stage A or B produced HIGH
  signal.**
- **`deep`** — both agents always.

## Where are we?

Empty `$ARGUMENTS` → list every `review/*/` with its stage, then stop. Otherwise
resolve to a page path (`nmj` → `docs/nmj/index.md`), derive `<slug>`, and read the
stage off disk:

| Present in `review/<slug>/` | Stage |
|---|---|
| nothing | **A — machine pass** |
| `15-machine.md`, no `30-openevidence.md` | **B — OE pack** |
| `30-openevidence.md`, paste zone empty | **GATE 1** — waiting on the user |
| `30-openevidence.md`, paste zone filled | **C — OE intake, then triage** |
| `20-findings.md` | **E — apply** |
| `50-changelog.md`, page uncommitted | **GATE 2** — waiting on approval |

Announce the stage in one line, then run it.

---

## Stage A — machine pass (free)

1. If the page does not exist, this is a **new page**: write it from
   `includes/topic-template.md` following `ROADMAP.md`, using
   `docs/headache/migraine.md` as the reference. Then continue.
2. `git checkout -b review/<slug>`; `mkdir -p review/<slug>`; copy the page to
   `10-baseline.md`.
3. Run all three and put the output in `15-machine.md`:

```bash
python3 tools/lint_page.py <page> --no-baseline
python3 tools/label_diff.py <page> --out review/<slug>/15-machine.md
python3 tools/evidence.py trials --cond "<condition>" --phase 3 --since <stamp year - 2>
```

`label_diff.py` is the important one. It flags route conflicts, missing doses,
missing induction phases, unmentioned boxed warnings, **serostatus drift**, and
labels revised since the review stamp. On the MG page it reproduced, for free, the
two findings that cost the most: efgartigimod's removed AChR+ restriction and
nipocalimab's IV-only route.

**These are mechanical comparisons, not verdicts.** Adjudicate each; some are false
positives by design, because the alternative is a filter that hides real drift.

> **Do not stop the review to make the tool perfect.** A false positive costs one line of
> prose to dismiss; a fix-test-fix cycle costs far more than that. **Collect every false
> positive in one pass, dismiss them in `15-machine.md`, and only change the script when it
> is HIDING findings rather than adding noise.** (A real example worth the fix: `increas\b`
> could never match "increasing", so correctly-titrated pages were silently flagged as
> missing an induction phase.)

## Stage B — OpenEvidence, then **GATE 1**

Write `30-openevidence.md` with **three blocks in one copyable fence**:

1. **Practice questions** (5–8) — the page's weakest management claims, each stating
   the page's current position in one line so the answer is comparable.
2. **Quantitative claim check** — a bulleted list of *every number on the page*
   (percentages, thresholds, intervals, sensitivities, response rates) asking which
   are out of date and what the current figure is. **This block replaces the retired
   guideline-auditor agent.**
3. **What changed** — approvals, label changes, practice-changing readouts **and
   abandonments** in this topic over the last 24 months. Ask explicitly about drugs
   that *failed or were dropped*, not just approvals. **This block replaces the
   retired recency-scout agent.**

Then, exactly:

```
<!-- PASTE OPENEVIDENCE RESPONSE BELOW THIS LINE -->

<!-- END PASTE -->
```

**STOP.** Tell the user to paste in, paste back, save, re-run `/page <slug>`.

> **Never attempt to access OpenEvidence yourself** — no public API, terms bar
> automated access, the account is NPI-bound to the user. Manual by design, forever.

## Stage C — OE intake, then triage

Parse the paste and three-way diff against `15-machine.md` and the page:
OE-caught/machine-missed, machine-caught/OE-missed, corroborated, and **direct
conflicts — surface to the user, never silently overwrite.** Write `35-oe-intake.md`.

**Then decide whether to spend money.** Spawn agents only if:

- depth is `deep`, **or**
- Stage A produced a HIGH flag that needs page-level judgment, **or**
- OE raised a safety concern the page does not address, **or**
- the page has a military box and has never had a `military-tricare` pass.

Otherwise **skip to Stage E and say so explicitly** — "no agent needed, here's why."
That is a successful outcome, not a shortcut.

## Stage D — agents, at most two

Launch only those justified above, in one message:

- **`page-safety`** — internal contradictions, dangerous omissions, missed mimics,
  the 3 a.m. read. The one thing no script or OE can do.
- **`military-tricare`** — AR 40-501 / DoDI / TRICARE. Nothing else covers it.

Each **writes its own findings file** (`22-panel-*.md`) and returns a ≤15-line
summary. **Do not transcribe their reports** — that cost real money last time. Tell
each agent that `15-machine.md` and `35-oe-intake.md` already exist and must not be
redone.

## Stage E — adjudicate and apply

**Keep four files, not six.** `15-machine.md` (script-generated), `30-openevidence.md`
(the paste), `35-oe-intake.md` (the adjudicated three-way diff — **findings live here; do
not also write a separate `20-findings.md`**), plus the two that ship:

- **`40-ledger.md`** — every dose, threshold and trial claim → a source URL or `UNVERIFIED`.
  This is what makes the `*Verified*` footer defensible. **Never drop it.**
- **`50-changelog.md`** — what changed, why, who caught it.

Agent findings stay in their own `22-panel-*.md` files, written by the agents. **Do not
restate agent output anywhere** — reference the file.

Then edit the page(s) and update the `*Verified*` footer audit trail.

## Stage F — verify, then **GATE 2**

```bash
python3 tools/lint_page.py <page>
python3 -m mkdocs build --strict
```

Both must pass. Show the diff summary, the HIGH findings applied, anything
unresolved — then **STOP for approval.**

**Never set the `Last reviewed:` stamp yourself.** Ask; apply the date given.

## Stage G — ship

Only after explicit approval:

1. Apply the authorized stamp; match the `*Verified*` footer.
2. Append a row to `review/_scorecard.md` — **and record what each source cost and
   caught.** The column that matters is what OE caught that the machine pass missed;
   when a pattern repeats, encode it in a script.
3. Update `ROADMAP.md`.
4. `git status` first, then commit. **`30-openevidence.md` must never be staged** —
   `.gitignore` handles it; verify anyway. **Keep the commit message short — a subject line
   and a few sentences.** `50-changelog.md` already carries the detail and ships in the same
   commit; writing it twice is pure duplication.
5. Merge to `main` fast-forward, push, delete the review branch. Do not leave
   branches lying around.

---

## Standing rules

- **Never invent a citation.** Unverifiable → `UNVERIFIED` in the ledger and stated
  in the footer.
- **Never write a dose from memory.** `label_diff.py` already pulled it.
- **Never stamp a page as reviewed without the user's say-so.**
- **Distinguish approval status precisely** — FDA vs EMA vs phase 3 positive vs CRL
  vs *positive but never filed* (batoclimab).
- **Prefer the cheapest source that can answer the question.** Script > OpenEvidence
  > agent. Reach for an agent only when the two below it structurally cannot answer.
- **Report honestly.** A quiet review is a real outcome; a padded one wastes trust.
