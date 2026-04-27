#!/usr/bin/env python3
"""
OMX30 Evening Updater
Runs at 18:30 CET every weekday. Fetches actual OMX30 close
and updates today's scorecard entry with result.
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import date

SCORECARD = os.path.join(os.path.dirname(__file__), "..", "data", "scorecard.json")


def fetch_omx30_close():
    for symbol in ["^OMX", "^OMXS30"]:
        enc = urllib.parse.quote(symbol)
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{enc}?interval=1d&range=5d"
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read())
            q      = data["chart"]["result"][0]["indicators"]["quote"][0]
            closes = [c for c in q["close"] if c is not None]
            if len(closes) >= 2:
                pct = round((closes[-1] - closes[-2]) / closes[-2] * 100, 3)
                return round(closes[-1], 2), pct
        except Exception as e:
            print(f"  [warn] {symbol}: {e}")
    return None, None


def main():
    today     = date.today()
    today_iso = today.strftime("%Y-%m-%d")
    print(f"OMX30 Evening Update — {today_iso}")

    if today.weekday() >= 5:
        print("Weekend — nothing to do.")
        sys.exit(0)

    try:
        with open(SCORECARD) as f:
            scorecard = json.load(f)
    except Exception:
        print("No scorecard found — skipping.")
        sys.exit(0)

    entry = next((e for e in scorecard if e["date"] == today_iso), None)
    if not entry:
        print(f"No entry for {today_iso} — skipping.")
        sys.exit(0)

    if entry.get("actual") is not None:
        print(f"Already updated for {today_iso}.")
        sys.exit(0)

    print("Fetching OMX30 close...")
    close_price, pct = fetch_omx30_close()

    if pct is None:
        print("Could not fetch close price — will retry next run.")
        sys.exit(1)

    predicted = entry.get("predicted", 0)

    # Determine result
    if abs(pct) < 0.05:
        result = "correct" if abs(predicted) < 0.20 else "partial"
    elif (predicted < 0) == (pct < 0):
        result = "correct"
    else:
        result = "miss"

    entry["actual"]        = pct
    entry["omxClose"]      = close_price
    entry["result"]        = result
    entry["magnitudeError"] = round(abs(predicted - pct), 3)

    with open(SCORECARD, "w") as f:
        json.dump(scorecard, f, indent=2, default=str)

    icons = {"correct": "CORRECT", "partial": "PARTIAL", "miss": "MISS"}
    print(f"{icons.get(result,'?')} | predicted {predicted:+.2f}% | actual {pct:+.2f}% | error {entry['magnitudeError']:.3f}%")
    print(f"OMX30 close: {close_price}")


if __name__ == "__main__":
    main()
