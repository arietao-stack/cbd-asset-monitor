# CBD Creative Asset Tracker

Tracks **views + engagement** for June 2026 aired creative links from the
`Creative Asset Tracker (Official)` tab of the CBD International tracking sheet,
and shows them on a live dashboard hosted on **GitHub Pages**.

## How it works (hybrid)

| Part | Where it runs | Why |
|------|---------------|-----|
| Read links from the Google Sheet | GitHub Actions (cloud) | Sheet is published → CSV export needs no login |
| **TikTok** metrics | GitHub Actions (cloud), daily 08:00 VN | TikTok needs no login → works from cloud |
| **Instagram** metrics | **Your Mac** (`local/update_instagram.sh`) | IG blocks cloud IPs + needs a logged-in session → uses your Chrome cookies |
| Dashboard | GitHub Pages (`docs/`) | Static site, auto-updates when data is committed |

The cloud job and the local job write **separate** data files, so they never
conflict:
- `docs/data/links.json` — current asset list pulled from the sheet
- `docs/data/tiktok.json` — TikTok metrics + daily history (written by GitHub Actions)
- `docs/data/instagram.json` — Instagram metrics + daily history (pushed from your Mac)

The dashboard (`docs/index.html`) merges all three in the browser, auto-refreshing
every 5 minutes.

## Daily flow
1. **08:00 VN** — GitHub Actions runs automatically: pulls the sheet, scrapes
   TikTok, commits data. Dashboard updates. *No machine needed.*
2. **When your Mac is on** — run `bash ~/cbd-asset-monitor/local/update_instagram.sh`
   (or let the launchd job at 08:05 do it) to refresh Instagram.

## Run things manually
```bash
# Instagram (from your Mac, uses Chrome login):
bash ~/cbd-asset-monitor/local/update_instagram.sh

# TikTok + sheet (also runs in cloud, but you can run locally too):
cd ~/cbd-asset-monitor
YTDLP_BIN=~/.tiktok_monitor_venv/bin/yt-dlp python3 scripts/fetch_sheet.py
YTDLP_BIN=~/.tiktok_monitor_venv/bin/yt-dlp python3 scripts/track_tiktok.py
```

## Auto-run Instagram daily (optional)
```bash
cp local/com.cbd.igmonitor.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.cbd.igmonitor.plist
```

## Add more months
Edit `TARGET_MONTHS` in `scripts/common.py`, e.g. `["2026_06", "2026_07"]`.

## Notes / limits
- **Instagram** is gated. Even with Chrome cookies, some posts return `blocked`
  (IG rate-limiting). Re-running later usually fills the gaps. Last-known numbers
  are kept on screen when a refresh fails.
- TikTok **photo** posts (`/photo/`) often can't be read by yt-dlp → shown as `error`.
- "Real-time" here means **once a day** (chosen cadence). The schedule is in
  `.github/workflows/track.yml` (`cron`) and `local/com.cbd.igmonitor.plist`.
