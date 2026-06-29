"""Scrape Instagram metrics and write docs/data/instagram.json.

Runs LOCALLY on your Mac (not in the cloud): Instagram blocks datacenter IPs and
needs a logged-in session, so we use your Chrome cookies. Pass the cookie source
via env IG_COOKIES_FROM_BROWSER (default "chrome") or IG_COOKIES_FILE.
"""
import json
import os
import subprocess
import sys
import time

from common import (DATA_DIR, load_json, save_json, merge_history, now_iso, today,
                    is_ig_permalink)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
YTDLP = os.environ.get("YTDLP_BIN", os.path.expanduser("~/.tiktok_monitor_venv/bin/yt-dlp"))
COOKIES_FROM_BROWSER = os.environ.get("IG_COOKIES_FROM_BROWSER", "chrome")
COOKIES_FILE = os.environ.get("IG_COOKIES_FILE", "")
# Pause between requests so Instagram doesn't rate-limit us (blocked responses).
SLEEP = float(os.environ.get("IG_SLEEP", "4"))


def cookie_args():
    if COOKIES_FILE:
        return ["--cookies", COOKIES_FILE]
    return ["--cookies-from-browser", COOKIES_FROM_BROWSER]


def scrape(url):
    cmd = [YTDLP, "--dump-single-json", "--skip-download", "--no-warnings",
           "--user-agent", UA, "--socket-timeout", "30", "--retries", "2"]
    cmd += cookie_args()
    cmd.append(url)
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return "error", {}
    if p.returncode != 0:
        err = (p.stderr or "").lower()
        if "empty media response" in err or "login" in err or "rate" in err:
            return "blocked", {}
        if "not available" in err or "removed" in err or "404" in err:
            return "dead", {}
        if "private" in err:
            return "private", {}
        return "error", {}
    try:
        d = json.loads(p.stdout)
    except json.JSONDecodeError:
        return "error", {}
    return "ok", {
        "uploader": d.get("uploader") or d.get("channel") or "",
        "title": (d.get("title") or d.get("description") or "")[:160],
        "views": d.get("view_count"),
        "likes": d.get("like_count"),
        "comments": d.get("comment_count"),
        "url": d.get("webpage_url") or url,
    }


def main():
    links = load_json(os.path.join(DATA_DIR, "links.json"), {"assets": []})
    prev = load_json(os.path.join(DATA_DIR, "instagram.json"), {"items": []})
    prev_by_key = {it["key"]: it for it in prev.get("items", [])}

    # One row per (asset, ig-url). The `instagram` column is primary; a creator_link
    # is included only when it is a distinct post permalink.
    targets = []
    for a in links["assets"]:
        urls = []
        if a.get("instagram"):
            urls.append(a["instagram"])
        if a.get("creator_link") and a["creator_link"] not in urls and is_ig_permalink(a["creator_link"]):
            urls.append(a["creator_link"])
        for u in urls:
            targets.append((a, u))

    items = []
    t = today()
    for idx, (a, url) in enumerate(targets):
        if idx:
            time.sleep(SLEEP)
        key = f"{a['asset_id']}|{url}"
        status, f = scrape(url)
        existing = prev_by_key.get(key, {})
        item = {
            "key": key,
            "asset_id": a["asset_id"],
            "platform": "instagram",
            "product": a.get("product", ""),
            "aired": a.get("aired", ""),
            "pic": a.get("pic", ""),
            "url": url,
            "uploader": f.get("uploader") or existing.get("uploader", ""),
            "title": f.get("title") or existing.get("title", ""),
            "status": status,
            "views": f.get("views"),
            "likes": f.get("likes"),
            "comments": f.get("comments"),
            "shares": None,
            "last_checked": now_iso(),
        }
        if status == "ok":
            point = {"t": t, "views": f.get("views"), "likes": f.get("likes"),
                     "comments": f.get("comments")}
            item["history"] = merge_history(existing, point)
        else:
            item["history"] = existing.get("history", [])
            for k in ("views", "likes", "comments"):
                if item[k] is None:
                    item[k] = existing.get(k)
        items.append(item)
        print(f"[ig] {a['asset_id']:24} {status:8} likes={item['likes']} comments={item['comments']}", file=sys.stderr)

    save_json(os.path.join(DATA_DIR, "instagram.json"),
              {"updated": now_iso(), "source": "instagram", "count": len(items), "items": items})
    ok = sum(1 for i in items if i["status"] == "ok")
    print(f"instagram.json: {ok}/{len(items)} ok", file=sys.stderr)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
