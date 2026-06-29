"""Download the public Google Sheet as CSV and extract the tracked-month asset links.

Writes docs/data/links.json. Runs in the cloud (no auth needed: the sheet is
published/viewable, so the CSV-export endpoint returns data).
"""
import csv
import io
import os
import sys
import urllib.request

from common import (COL, TARGET_MONTHS, DATA_DIR, channel_of, clean_url, is_url,
                    is_ig_permalink, normalize_date, now_iso, save_json)

SHEET_ID = "1pjY79ldEs08y1Yict2XUWMi2X9r4d7Y8WWQJGmAueWs"
GID = "1941056735"  # Creative Asset Tracker (Official)
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def fetch_csv():
    req = urllib.request.Request(CSV_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def cell(row, key):
    i = COL[key]
    return row[i] if i < len(row) else ""


def main():
    text = fetch_csv()
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)

    assets = []
    for row in rows:
        if cell(row, "month_year") not in TARGET_MONTHS:
            continue
        asset_id = clean_url(cell(row, "asset_id"))
        if not asset_id:
            continue
        ig = clean_url(cell(row, "instagram"))
        cl = clean_url(cell(row, "creator_link"))
        source_type = clean_url(cell(row, "source_type"))
        concept = clean_url(cell(row, "concept"))
        angle = clean_url(cell(row, "angle"))
        # "What" = a human descriptor of the asset, like the reference dashboard.
        what = " · ".join([x for x in (concept, angle) if x]) or clean_url(cell(row, "summary"))
        assets.append({
            "asset_id": asset_id,
            "product": clean_url(cell(row, "product")),
            "aired": normalize_date(cell(row, "aired")),
            "pic": clean_url(cell(row, "pic")),
            "creator_id": clean_url(cell(row, "creator_id")),
            "source_type": source_type,
            "channel": channel_of(source_type),
            "funnel": clean_url(cell(row, "funnel")),
            "campaign": clean_url(cell(row, "campaign")),
            "angle": angle,
            "concept": concept,
            "what": what,
            "tiktok": clean_url(cell(row, "tiktok")) if is_url(cell(row, "tiktok")) else "",
            "instagram": ig if is_url(ig) else "",
            # creator_link is used as an extra IG source only when it is a post permalink
            "creator_link": cl if is_ig_permalink(cl) else "",
            "facebook": clean_url(cell(row, "facebook")) if is_url(cell(row, "facebook")) else "",
        })

    out = {"updated": now_iso(), "months": TARGET_MONTHS, "count": len(assets), "assets": assets}
    save_json(os.path.join(DATA_DIR, "links.json"), out)

    tk = sum(1 for a in assets if a["tiktok"])
    ig = sum(1 for a in assets if a["instagram"] or a["creator_link"])
    print(f"links.json: {len(assets)} assets  | TikTok={tk}  Instagram={ig}", file=sys.stderr)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
