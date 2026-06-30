#!/bin/bash
# Deploy a deck to GitHub Pages → live link.
#   bash deploy-deck.sh docs/my-deck.html
# (or pass any .html; it'll be copied into docs/)
set -e
GH="$HOME/cbd-asset-monitor/.tools/gh_2.95.0_macOS_arm64/bin/gh"
REPO="$HOME/cbd-asset-monitor"
SRC="$1"
[ -z "$SRC" ] && { echo "Usage: bash deploy-deck.sh <deck.html>"; exit 1; }
[ -f "$SRC" ] || { echo "Not found: $SRC"; exit 1; }
BASE="$(basename "$SRC")"
cd "$REPO"
# copy into docs/ if it isn't already there
if [ "$(cd "$(dirname "$SRC")" && pwd)" != "$REPO/docs" ]; then cp "$SRC" "docs/$BASE"; fi
git pull --rebase --autostash -q origin main 2>/dev/null || true
git add "docs/$BASE"
if git diff --cached --quiet; then
  echo "No changes to deploy."
else
  git commit -q -m "deck: deploy/update $BASE"
  git push -q origin main
  echo "Pushed."
fi
echo "Live in ~1 min →  https://arietao-stack.github.io/cbd-asset-monitor/$BASE"
