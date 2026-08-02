# Authoring pipeline — design + local setup

How a page gets written, gap-checked, and shipped. Replaces the ad-hoc
"draft → paste through OpenEvidence → paste feedback back" loop with a repeatable
pipeline, while keeping the OpenEvidence step where it has to stay: manual.

> **Status: DESIGN ONLY.** Nothing in `.claude/skills/` or `tools/` is built yet.
> This file is the spec to build from.

---

## Where this runs

**Primary: locally**, in `~/Desktop/Research AI/Neurology`. Three reasons, all
structural:

1. **`/_source/` is gitignored** — the SCUTBOOK drafts and reference PDFs that carry
   the voice and skeleton exist only on the local machine. A cloud session cannot see
   them, so it drafts without the source material.
2. **Network egress.** Scripted literature pulls (PubMed E-utilities, ClinicalTrials.gov,
   openFDA) work from a normal machine. In the sandboxed web environment they are
   blocked at the proxy.
3. **`mkdocs serve`** live preview is only useful where you can see it, and the
   OpenEvidence paste loop already happens in the browser on that machine.

**Secondary: web/remote sessions** are still worth using for unattended batch work that
touches no source material — e.g. "run the gap panel across all existing pages, file the
findings, open a PR." That job needs no `/_source/` and is a good fit for running while
you do something else.

The pipeline itself is committed to the repo, so it runs the same in both places.

### Starting a local session

```bash
cd ~/Desktop/"Research AI"/Neurology     # quotes: the folder name has a space
git pull origin main
claude
```

### Local preview

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve                              # http://127.0.0.1:8000
```

---

## The pipeline

### Pass 1 — Draft
From `includes/topic-template.md`, in the canonical tiered-prescriptive style
(reference implementation: `docs/headache/migraine.md`). Reads `/_source/` for voice
and skeleton where material exists.

### Pass 2 — The gap panel
Independent reviewers over the draft, each blind to the others, each with its own
literature-search budget. This is the part that substitutes for the OpenEvidence
"did we miss anything" pass.

| Reviewer | Hunts for |
|---|---|
| Guideline auditor | Does every recommendation trace to a *current* named guideline (AHS / AAN / AHA-ASA / ILAE / ICHD-3 / MGFA)? Superseded editions cited as current. |
| Trials & new-drug scout | Approvals, label changes, and practice-changing trials in the last 24 months that the draft omits. Highest-yield reviewer. |
| Dose & safety pharmacist | Dose + route + titration on every drug; renal/hepatic adjustment; monitoring; pregnancy; major interactions. |
| Failure-mode clinician | What harms the patient if the reader follows the page literally — missing contraindications, unlisted mimics, wrong escalation trigger. |
| Military / TRICARE layer | The fixed 5 fields correct and current; formulary and PA status; AR 40-501 paragraph citations that actually exist. |
| Format linter (deterministic) | Section order, dose present on every drug line, TRICARE box present whenever drugs appear, military box has exactly 5 fields, `Last reviewed` stamp, linked references, `Verified MON YYYY` footer. |

### Pass 3 — Adjudicate
Merge the panel into one ranked delta list: `ADD` / `CORRECT` / `REMOVE` /
`CANNOT-CONFIRM`. Deduplicate, resolve conflicts between reviewers, drop anything
without a citation. Without this step, six reviewers produce six times the noise
rather than six times the coverage.

### Pass 4 — OpenEvidence handoff (manual, by design)
Emits `review/<topic>-openevidence.md`: one batched, copy-paste-ready block of 5–10
specific questions targeting the draft's weakest claims, each stating the draft's
current position. One round trip per page, not one per section.

**Why this stays manual:** OpenEvidence publishes no self-serve developer API (docs are
gated), its terms prohibit automated access and reverse engineering, it has litigated
over unauthorized access, and it blocks automated requests outright. The account is
NPI-verified to an individual clinician — driving it with a bot puts that account and
license at risk. Do not script it, and do not hand session credentials to a tool.

### Pass 5 — Intake
Paste the OpenEvidence response back into the marked block, unedited — no cleanup
needed. Intake diffs it against both the draft and the panel findings and reports three
buckets:

- what OpenEvidence caught that the panel missed,
- what the panel caught that OpenEvidence missed,
- direct conflicts needing adjudication.

Each intake appends to `review/panel-scorecard.md`. After ~10 pages that log shows
exactly what OpenEvidence systematically catches that the panel does not — fold those
into the panel prompts and the manual hop shrinks toward spot-check.

### Pass 6 — Ship
`mkdocs build --strict` + format linter + `nav:` entry in `mkdocs.yml` + commit + PR.

---

## To build

| Path | What |
|---|---|
| `.claude/skills/scutbook-draft/` | Pass 1 |
| `.claude/skills/scutbook-panel/` | Passes 2–3 |
| `.claude/skills/scutbook-intake/` | Pass 5 |
| `tools/lint_page.py` | Deterministic template conformance; also runs in CI |
| `review/queue/<topic>.yml` | Work order: topic, sections needed, special asks |
| `review/panel-scorecard.md` | Panel-vs-OpenEvidence delta log |
| `.github/workflows/deploy.yml` | Add the linter as a gate before deploy |

Build order: `tools/lint_page.py` first (it is the only deterministic piece and the
panel depends on it), then prove passes 1–5 end-to-end on a single drug-heavy topic
before generalizing.

## Cost

A page goes from one long session to roughly three: draft → panel + adjudicate →
intake + ship. Worth it for pages with drugs and doses; overkill for hub and index
pages, which should skip straight to Pass 6.
