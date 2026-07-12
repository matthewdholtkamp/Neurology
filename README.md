# Neuro Scutbook

A bedside neurology consult reference + evidence briefs for MDs, NPs, PAs, and medics, with a
military-medicine layer (deployability, profiles, EPTS/LOD, retention, MEB/IDES). Built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages.

> **Educational clinical decision-support — not a substitute for professional judgment or
> individual medical advice.** Verify everything against current guidelines and the governing
> regulation.

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # live preview at http://127.0.0.1:8000
```

## Add a topic

See [docs/contributing.md](docs/contributing.md) and copy [includes/topic-template.md](includes/topic-template.md).

## Deploy

Pushing to `main` triggers `.github/workflows/deploy.yml`, which runs `mkdocs gh-deploy` and
publishes to the `gh-pages` branch. Before the first deploy:

1. Set `site_url` and `repo_url` in `mkdocs.yml` to your real GitHub username/repo.
2. Create the GitHub repo (start **private**), push this folder to `main`.
3. In repo **Settings → Pages**, set the source to the **`gh-pages`** branch.

## Project layout

```
mkdocs.yml            # site config + nav
docs/                 # published content (Markdown)
  index.md            # landing + disclaimer
  headache/           # pilot topic
  military/           # deployability / MEB-IDES primer
  contributing.md
  stylesheets/        # custom callout styling
includes/             # abbreviations (auto-appended) + copy-paste topic template
.github/workflows/    # auto-deploy
ROADMAP.md            # build plan + 2016→2026 currency triage
Headache/ SCUTBOOK/   # local source material (gitignored — not published)
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full build plan and the per-topic content-currency triage.
