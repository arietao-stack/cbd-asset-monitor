"""Scrape TikTok metrics for the tracked assets and write docs/data/tiktok.json.

Runs in the cloud (GitHub Actions): TikTok does not require login. Uses yt-dlp.
"""
import json
import os
import subprocess
import sys

from common import DATA_DIR, load_json, save_json, merge_history, now_iso, today

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
YTDLP = os.environ.get("YTDLP_BIN", "yt-dlp")


def scrape(url):
    """Return (status, fields) for one TikTok URL."""
    cmd = [
        YTDLP, "--dump-single-json", "--skip-download", "--no-warnings",
        "--user-agent", UA, "--socket-timeout", "30", "--retries", "2", url,
    ]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return "error", {}
    if p.returncode != 0:
        err = (p.stderr or "").lower()
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
        "title": (d.get("title") or "")[:160],
        "views": d.get("view_count"),
        "likes": d.get("like_count"),
        "comments": d.get("comment_count"),
        "shares": d.get("repost_count"),
        "url": d.get("webpage_url") or url,
    }


def main():
    links = load_json(os.path.join(DATA_DIR, "links.json"), {"assets": []})
    prev = load_json(os.path.join(DATA_DIR, "tiktok.json"), {"items": []})
    prev_by_id = {it["asset_id"]: it for it in prev.get("items", [])}

    targets = [a for a in links["assets"] if a.get("tiktok")]
    items = []
    t = today()
    for a in targets:
        status, f = scrape(a["tiktok"])
        existing = prev_by_id.get(a["asset_id"], {})
        item = {
            "asset_id": a["asset_id"],
            "platform": "tiktok",
            "product": a.get("product", ""),
            "aired": a.get("aired", ""),
            "pic": a.get("pic", ""),
            "url": a["tiktok"],
            "uploader": f.get("uploader") or existing.get("uploader", ""),
            "title": f.get("title") or existing.get("title", ""),
            "status": status,
            "views": f.get("views"),
            "likes": f.get("likes"),
            "comments": f.get("comments"),
            "shares": f.get("shares"),
            "last_checked": now_iso(),
        }
        if status == "ok":
            point = {"t": t, "views": f.get("views"), "likes": f.get("likes"),
                     "comments": f.get("comments"), "shares": f.get("shares")}
            item["history"] = merge_history(existing, point)
        else:
            item["history"] = existing.get("history", [])
            # keep last known numbers visible if this run failed
            for k in ("views", "likes", "comments", "shares"):
                if item[k] is None:
                    item[k] = existing.get(k)
        items.append(item)
        print(f"[tiktok] {a['asset_id']:24} {status:8} views={item['views']}", file=sys.stderr)

    save_json(os.path.join(DATA_DIR, "tiktok.json"),
              {"updated": now_iso(), "source": "tiktok", "count": len(items), "items": items})
    ok = sum(1 for i in items if i["status"] == "ok")
    print(f"tiktok.json: {ok}/{len(items)} ok", file=sys.stderr)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
