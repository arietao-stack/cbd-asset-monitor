"""Shared helpers for the CBD asset monitor."""
import json
import os
import re
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "docs", "data")

# Column indexes in the Google-Sheet CSV (0-based; col1 == index 0).
COL = {
    "asset_id": 4,       # E  Asset_ID
    "product": 6,        # G  Product
    "aired": 8,          # I  Aired Date
    "month_year": 9,     # J  Month & Year
    "funnel": 11,        # L  Funnel Stage (TOF/MOF/BOF)
    "angle": 12,         # M  Angle
    "concept": 13,       # N  Concept
    "campaign": 15,      # P  Campaign Type
    "source_type": 16,   # Q  Source Type (Inhouse / Social Boost / KOL-UGC)
    "creator_link": 18,  # S  Creator Link
    "creator_id": 19,    # T  Creator ID
    "summary": 20,       # U  Summary
    "instagram": 27,     # AB Instagram Link
    "tiktok": 29,        # AD TikTok Link
    "facebook": 31,      # AF Facebook Link
    "youtube": 32,       # AG YouTube Link
    "pic": 42,           # AQ PIC
}

# Source Type -> brand-channel bucket (mirrors the company's Owned/Earned framing).
def channel_of(source_type):
    s = (source_type or "").lower()
    if "kol" in s or "ugc" in s or "collab" in s:
        return "Earned"
    return "Owned"  # Inhouse, Social Boost

# Which Month & Year values to track. Add more strings to widen the scope.
TARGET_MONTHS = ["2026_06"]


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today():
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def normalize_date(v):
    """Return YYYY-MM-DD from the sheet's varied date formats, else ''."""
    s = str(v or "").strip()
    if not s:
        return ""
    for fmt in ("%Y-%m-%d", "%d-%b-%Y", "%d-%B-%Y", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s[:11], fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return s[:10]


def is_url(v):
    return bool(v) and str(v).strip().lower().startswith("http")


def clean_url(v):
    return str(v).strip() if v else ""


# Instagram permalink (a single post we can pull metrics for) vs a profile link.
IG_PERMALINK = re.compile(r"instagram\.com/(p|reel|tv)/", re.I)


def is_ig_permalink(v):
    return is_url(v) and bool(IG_PERMALINK.search(str(v)))


def merge_history(existing_item, point, max_len=180):
    """Append today's metric snapshot, replacing an earlier one from the same day."""
    history = (existing_item or {}).get("history", []) if existing_item else []
    history = [h for h in history if h.get("t") != point["t"]]
    history.append(point)
    history.sort(key=lambda h: h["t"])
    return history[-max_len:]
