#!/bin/bash
# Update Instagram metrics from THIS Mac (uses your logged-in Chrome session),
# then push the result so the live dashboard shows fresh IG numbers.
#
# Instagram blocks cloud/datacenter IPs, so this part can't run on GitHub.
# Run it whenever your machine is on — manually, or via the launchd job.
#
#   bash ~/cbd-asset-monitor/local/update_instagram.sh
set -euo pipefail

REPO="$HOME/cbd-asset-monitor"
export YTDLP_BIN="$HOME/.tiktok_monitor_venv/bin/yt-dlp"
export IG_COOKIES_FROM_BROWSER="chrome"   # reads your logged-in Chrome cookies

cd "$REPO"

echo "[1/4] Pull latest from GitHub…"
git pull --rebase --autostash --quiet || true

echo "[2/4] Refresh links from sheet…"
/usr/bin/python3 scripts/fetch_sheet.py

echo "[3/4] Scrape Instagram…"
/usr/bin/python3 scripts/track_instagram.py 2>&1 | grep -v -i "urllib\|openssl\|deprecat\|warnings.warn" || true

echo "[4/4] Commit & push…"
git add docs/data/instagram.json docs/data/links.json
if git diff --cached --quiet; then
  echo "No changes."
else
  git commit -m "data: refresh Instagram $(date -u +%FT%TZ)" --quiet
  git push --quiet
  echo "Pushed. Dashboard will update within a minute."
fi
