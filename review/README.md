# Review pipeline — working directory

One folder per page under review, created by `/page <slug>`. **Almost everything in
here is gitignored on purpose.**

## Why most of this stays local

`30-openevidence.md` holds pasted OpenEvidence output — their copyrighted text,
under terms that restrict reuse. This repo is public. So `.gitignore` keeps
`review/*` out of git, with four exceptions, all of them our own work:

- `review/README.md` (this file)
- `review/_scorecard.md` — the accumulated OE-vs-panel learning
- `review/<slug>/40-ledger.md` and `review/<slug>/50-changelog.md` — the audit trail
  standing behind a page's `*Verified MON YYYY*` footer, so they ship with the page

The `.gitignore` enforces this **per file, by name**, so a new review folder gets the
same treatment automatically — the OpenEvidence paste can never be committed by
accident. Verify any time with:

```bash
git check-ignore -v review/<slug>/30-openevidence.md
```

## Files in a review folder

| File | What it is |
|---|---|
| `10-baseline.md` | the page as it was before the review — the diff's before-picture |
| `15-machine.md` | **free, scripted:** every drug diffed against its current FDA label — route conflicts, missing doses, missing induction, unmentioned boxed warnings, serostatus drift, labels revised since the stamp |
| `30-openevidence.md` | question pack + the paste zone. **Never committed.** |
| `35-oe-intake.md` | three-way diff of the OE response against `15-machine.md` and the page |
| `20-findings.md` | everything adjudicated and ranked |
| `22-panel-*.md` | agent findings — **written by the agents themselves**, and only when a page needs them |
| `40-ledger.md` | every dose/threshold/trial → its source, or `UNVERIFIED` |
| `50-changelog.md` | what changed, why, and who caught it |

## Cheapest source first

The pipeline runs **scripts → OpenEvidence → agents**, in that order, and stops as
early as it can. Scripts and OpenEvidence are free; agents are not. The first full
run cost ~735k tokens with five agents, and `tools/label_diff.py` now reproduces the
two most expensive findings from that run — efgartigimod's removed serostatus
restriction and nipocalimab's IV-only route — deterministically and for nothing.

Many pages should finish without an agent ever running. That is the design working,
not a corner being cut.

Stage is inferred from which files exist, which is what lets `/page <slug>` resume
in a chat that has never seen the earlier work.

## Manual use

The scripts are useful on their own, outside the pipeline:

```bash
python3 tools/label_diff.py docs/nmj/index.md   # page drug claims vs current FDA labels
python3 tools/lint_page.py --all                # format audit, whole site
python3 tools/lint_page.py --all --no-baseline  # ...including known debt
python3 tools/evidence.py label --drug efgartigimod --section dosage boxed
python3 tools/evidence.py trials --cond "myasthenia gravis" --phase 3 --since 2024
```

`label_diff.py` is worth running on its own against any page you suspect has drifted
— it needs no model and no review folder.
