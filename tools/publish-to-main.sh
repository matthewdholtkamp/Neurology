#!/usr/bin/env bash
# Copies a built MkDocs site into the repo root so GitHub Pages can serve it
# straight from the main branch. Removes pages that no longer exist, using
# .site-manifest (the list of top-level entries the last build put here).
# Usage: tools/publish-to-main.sh <built-site-dir>
set -euo pipefail
SITE="${1:?usage: publish-to-main.sh <built-site-dir>}"
cd "$(git rev-parse --show-toplevel)"

if [ -f .site-manifest ]; then
  while IFS= read -r entry; do
    [ -n "$entry" ] && rm -rf -- "./$entry"
  done < .site-manifest
fi

cp -R "$SITE"/. .
ls -A "$SITE" > .site-manifest
touch .nojekyll   # serve files as-is; stops GitHub's Jekyll from rendering the Markdown sources
