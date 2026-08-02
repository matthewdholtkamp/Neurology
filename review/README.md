# Review pipeline — working directory

One folder per page under review, created by `/page <slug>`. **Almost everything in
here is gitignored on purpose.**

## Why most of this stays local

`30-openevidence.md` holds pasted OpenEvidence output — their copyrighted text,
under terms that restrict reuse. This repo is public. So `.gitignore` keeps
`review/*` out of git, with two exceptions that are our own work:

- `review/README.md` (this file)
- `review/_scorecard.md`

`40-ledger.md` and `50-changelog.md` get committed alongside the page they belong
to, not from here.

## Files in a review folder

| File | What it is |
|---|---|
| `00-workorder.md` | target page, current stamp, drugs, guidelines, opening lint |
| `10-baseline.md` | the page as it was before the review — the diff's before-picture |
| `20-findings.md` | the five reviewers' findings, adjudicated and ranked |
| `25-evidence.md` | deterministic pulls: PubMed, ClinicalTrials.gov, FDA labels |
| `30-openevidence.md` | question pack + the paste zone. **Never committed.** |
| `40-ledger.md` | every dose/threshold/trial → its source, or `UNVERIFIED` |
| `50-changelog.md` | what changed, why, and who caught it |

Stage is inferred from which files exist, which is what lets `/page <slug>` resume
in a chat that has never seen the earlier work.

## Manual use

The scripts are useful on their own, outside the pipeline:

```bash
python3 tools/lint_page.py --all              # format audit, whole site
python3 tools/lint_page.py --all --no-baseline # ...including known debt
python3 tools/evidence.py label --drug efgartigimod --section dosage boxed
python3 tools/evidence.py trials --cond "myasthenia gravis" --phase 3 --since 2024
```
