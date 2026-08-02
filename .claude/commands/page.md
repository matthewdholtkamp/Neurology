---
description: Run the multi-reviewer evidence pipeline on a Neuro Scutbook page (draft → 5-reviewer panel → verification → OpenEvidence handoff → merge → ship)
argument-hint: "<topic slug or docs/ path>  — e.g. nmj, docs/nmj/index.md, or blank to list in-flight reviews"
---

# /page — the page review pipeline

Target: **$ARGUMENTS**

You are the orchestrator. Your job is to run the stages below, adjudicate what the
reviewers return, and stop at the two human gates. **All state lives in files under
`review/<slug>/`, never in conversation** — that is what lets this resume in a chat
that has never seen the earlier work.

## First: work out where we are

If `$ARGUMENTS` is empty, list every `review/*/` directory with its current stage
and stop. Otherwise resolve the target to a real page path (a slug like `nmj` →
`docs/nmj/index.md`; ask only if genuinely ambiguous), derive `<slug>` from the
path, then determine the stage from what exists on disk:

| Files present in `review/<slug>/` | Stage to run |
|---|---|
| nothing | **1 — Intake** |
| `00-workorder.md` only | **2 — Panel** |
| `20-findings.md`, no `30-openevidence.md` | **4 — OE pack** |
| `30-openevidence.md`, paste zone empty | **GATE 1** — waiting on the user |
| `30-openevidence.md`, paste zone filled | **5 — Intake OE** |
| `50-changelog.md` present, page uncommitted | **GATE 2** — waiting on approval |

Announce the stage you're entering in one line, then run it. Never re-run a
completed stage without saying so.

---

## Stage 1 — Intake

1. Confirm the page exists. If it does not, this is a **new page**: write it first
   from `includes/topic-template.md`, following the canonical format described in
   `ROADMAP.md` ("Standard topic template"), using `docs/headache/migraine.md` as
   the reference implementation. Then continue.
2. `git checkout -b review/<slug>` (branch off `main`; never work on `main`).
3. `mkdir -p review/<slug>` and copy the current page to `10-baseline.md` — this is
   the before-picture the changelog diffs against.
4. Run `python3 tools/lint_page.py <page>` and save the output.
5. Write `00-workorder.md`: page path, date, `Last reviewed` stamp currently on the
   page, the drugs named on it, the guidelines it cites, and the lint findings.

## Stage 2 — Panel

Pull the deterministic evidence **first**, so the reviewers argue against facts:

```bash
python3 tools/evidence.py trials --cond "<condition>" --phase 3 --since <stamp year - 2>
python3 tools/evidence.py pubmed --query "<condition>" --since <stamp year - 2> \
    --types "Randomized Controlled Trial" "Practice Guideline" "Meta-Analysis"
python3 tools/evidence.py label --drug <each drug on the page>
```

Save to `25-evidence.md`.

Then launch **all five reviewers in parallel, in one message** — they must not see
each other's findings, because independent misses are the whole point of a panel:

`guideline-auditor`, `recency-scout`, `dose-pharmacist`, `failure-mode`,
`military-tricare`

Give each: the page path, the path to `25-evidence.md`, and the page's current
`Last reviewed` date. Each returns findings in the schema its own definition
specifies.

## Stage 3 — Adjudicate

You do this yourself; do not spawn an agent for it. Merge the five reports into
`20-findings.md`, ranked:

- **Dedupe.** Two reviewers finding the same thing is corroboration — merge into
  one finding, note both, raise confidence.
- **Drop the unsourced.** A finding whose `Source:` is `NONE` becomes `VERIFY` and
  drops to the bottom. Do not apply it.
- **Resolve conflicts.** If two reviewers disagree, check it yourself and say who
  was right and why.
- **Discard the out-of-lane noise** unless it is HIGH severity.

Rank HIGH → MED → LOW. Keep every finding's `Source:` line intact.

## Stage 4 — OpenEvidence pack, then **GATE 1**

Write `30-openevidence.md` containing 5–10 questions aimed at the page's weakest
claims — the `VERIFY` findings, the unsourced ones, and anything the panel split
on. Rules for the questions:

- **Specific, not "did we miss anything."** OpenEvidence answers a pointed clinical
  question far better than an open audit.
- Each question states the page's current position in one line, so the answer is
  directly comparable.
- Ask about *management decisions*, not formatting or military policy — OE has no
  view on AR 40-501.

Put them in one fenced block the user can copy in a single action, then this,
exactly:

```
<!-- PASTE OPENEVIDENCE RESPONSE BELOW THIS LINE -->

<!-- END PASTE -->
```

Then **STOP.** Tell the user: paste the block into OpenEvidence, paste the whole
response back between those two markers, save, and re-run `/page <slug>`.

> **Do not attempt to access OpenEvidence yourself** — not by WebFetch, not by
> browser tools, not by asking for credentials. It has no public API, its terms bar
> automated access, and the account is NPI-bound to the user personally. This gate
> is manual by design, permanently.

## Stage 5 — Intake OE

Parse whatever prose is in the paste zone (no fixed format — OE output varies) and
three-way diff it against `20-findings.md` and the page:

1. **OE caught, panel missed** → the highest-value bucket. Verify each against a
   primary source before applying.
2. **Panel caught, OE missed** → keep; note it in the scorecard.
3. **Both** → corroborated, apply with confidence.
4. **Direct conflict** with a guideline the page cites → **surface to the user, do
   not silently overwrite.** Show both positions and your read.

Anything OE asserts without a citation gets verified before it goes on the page.

## Stage 6 — Apply

Edit the page. Then write:

- `40-ledger.md` — every dose, threshold, and trial claim on the page mapped to a
  source URL, or explicitly marked `UNVERIFIED`. This is what makes the
  `*Verified MON YYYY*` footer honest.
- `50-changelog.md` — what changed, why, and which reviewer or OE prompted it.

Update the page's `*Verified MON YYYY:*` footer audit trail to name what was
checked and what could not be pinned.

## Stage 7 — Verify, then **GATE 2**

```bash
python3 tools/lint_page.py <page>
python3 -m mkdocs build --strict
```

Both must pass. Then show the user: the diff summary, the HIGH findings applied,
anything unresolved — and **STOP for approval.**

**Do not set the `Last reviewed:` stamp yourself.** That is the user's signature on
clinical content. Ask; apply the date they give.

## Stage 8 — Ship

Only after explicit approval:

1. Apply the `Last reviewed:` stamp they authorised (and match the `*Verified*` footer).
2. Append a row to `review/_scorecard.md`: date, page, panel findings applied, OE
   findings the panel missed, notable misses. **This is how the panel gets better —
   patterns here go back into the agent definitions.**
3. Update the relevant `ROADMAP.md` line.
4. Commit `docs/`, `review/_scorecard.md`, `ROADMAP.md`, `40-ledger.md`,
   `50-changelog.md`. **Never commit `30-openevidence.md`** — it holds OpenEvidence's
   copyrighted output and `.gitignore` is set to keep it local. Verify with
   `git status` before committing.
5. Push and offer to open a PR.

---

## Standing rules

- **Never invent a citation.** Unverifiable → `UNVERIFIED` in the ledger and stated
  in the footer. This site's credibility is the whole product.
- **Never write a dose from memory.** Pull the label.
- **Never stamp a page as reviewed without the user's say-so.**
- **Distinguish approval status precisely** — FDA-approved vs EMA-only vs phase 3
  positive vs CRL. The repo has been wrong here before (tolebrutinib, Dec 2025 CRL).
- **Report honestly.** If a stage found nothing, say it found nothing. A quiet
  review is a real outcome; a padded one wastes the user's trust.
