#!/usr/bin/env python3
"""
OMX30 Morning Brief — main script
Runs at 07:55 CET every weekday via GitHub Actions.
Fetches market data, computes technicals, calls Claude,
writes data/morning_brief.json and data/scorecard.json
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, datetime

import anthropic
import numpy as np
from indicators import compute_all

# ─── Configuration ────────────────────────────────────────────────────────────
API_KEY      = os.environ["ANTHROPIC_API_KEY"]
SCORECARD    = os.path.join(os.path.dirname(__file__), "..", "data", "scorecard.json")
BRIEF        = os.path.join(os.path.dirname(__file__), "..", "data", "morning_brief.json")
MAX_DAYS     = 30
HISTORY_DAYS = 260

# ─── Market universe ──────────────────────────────────────────────────────────
MARKETS = {
    "DAX 40":      {"symbol": "^GDAXI",    "corr": 0.89, "region": "Europe"},
    "CAC 40":      {"symbol": "^FCHI",     "corr": 0.85, "region": "Europe"},
    "FTSE 100":    {"symbol": "^FTSE",     "corr": 0.78, "region": "Europe"},
    "S&P 500":     {"symbol": "^GSPC",     "corr": 0.52, "region": "Americas"},
    "Dow Jones":   {"symbol": "^DJI",      "corr": 0.51, "region": "Americas"},
    "NASDAQ":      {"symbol": "^IXIC",     "corr": 0.49, "region": "Americas"},
    "Nikkei 225":  {"symbol": "^N225",     "corr": 0.38, "region": "Asia"},
    "Hang Seng":   {"symbol": "^HSI",      "corr": 0.31, "region": "Asia"},
    "Shanghai":    {"symbol": "000001.SS", "corr": 0.22, "region": "Asia"},
}

OTHER = {
    "Brent Oil":    "BZ=F",
    "Gold":         "GC=F",
    "Copper":       "HG=F",
    "US 10Y Yield": "^TNX",
    "VIX":          "^VIX",
    "EUR/SEK":      "EURSEK=X",
    "USD/SEK":      "USDSEK=X",
    "EUR/USD":      "EURUSD=X",
    "DXY":          "DX-Y.NYB",
}

NEWS_FEEDS = [
    ("FT Markets",    "https://www.ft.com/rss/home/uk"),
    ("Reuters Biz",   "https://feeds.reuters.com/reuters/businessNews"),
]

SECTORS = {
    "Industrials (28%)":       ["Atlas Copco A", "Volvo B", "Sandvik", "SKF B", "Epiroc A"],
    "Banks (18%)":             ["SEB A", "Handelsbanken A", "Swedbank A", "Nordea"],
    "Pharma (12%)":            ["AstraZeneca", "Essity B"],
    "Tech & Telecom (12%)":    ["Ericsson B", "Hexagon B", "Sinch"],
    "Mining & Materials (8%)": ["Boliden", "SSAB A"],
    "Consumer & Retail (8%)":  ["H&M B", "EVO Gaming"],
    "Vehicles & Auto (8%)":    ["Volvo Cars B", "Volvo B"],
    "Real Estate (6%)":        ["Fastighets AB Balder", "Castellum"],
}

# ─── Data fetching ────────────────────────────────────────────────────────────
def yf(symbol, days=5):
    enc  = urllib.parse.quote(symbol)
    rang = f"{days}d" if days <= 30 else f"{max(2, days // 252 + 1)}y"
    url  = f"https://query1.finance.yahoo.com/v8/finance/chart/{enc}?interval=1d&range={rang}"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"    [warn] {symbol}: {e}")
        return None


def pct_and_last(symbol):
    data = yf(symbol, 5)
    if not data:
        return None, None
    try:
        q  = data["chart"]["result"][0]["indicators"]["quote"][0]
        cl = [c for c in q["close"] if c is not None]
        if len(cl) >= 2:
            return round((cl[-1] - cl[-2]) / cl[-2] * 100, 3), round(cl[-1], 4)
    except Exception:
        pass
    return None, None


def omx_history():
    data = yf("^OMX", HISTORY_DAYS)
    if not data:
        return None
    try:
        q = data["chart"]["result"][0]["indicators"]["quote"][0]
        rows = [(c, h, l) for c, h, l in zip(q["close"], q["high"], q["low"])
                if c and h and l]
        if len(rows) < 50:
            return None
        c, h, l = zip(*rows)
        return list(c), list(h), list(l)
    except Exception:
        return None


def fetch_news():
    items = []
    for source, url in NEWS_FEEDS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                root = ET.fromstring(r.read())
            for item in root.findall(".//item")[:4]:
                title = (item.findtext("title") or "").strip()
                if title:
                    items.append({
                        "source":      source,
                        "title":       title,
                        "description": (item.findtext("description") or "").strip()[:180],
                    })
        except Exception as e:
            print(f"    [warn] RSS {source}: {e}")
        time.sleep(0.3)
    return items[:10]


# ─── Claude synthesis ─────────────────────────────────────────────────────────
def call_claude(mkt, signal, ind, other, news, day_label):

    def fmt(d):
        return "\n".join(
            f"  {k}: {v['last']:.4g} ({v['change']:+.2f}%)" if v.get("last") and v.get("change") is not None
            else f"  {k}: N/A"
            for k, v in d.items()
        )

    mkt_lines = "\n".join(
        f"  {n}: {d['change']:+.2f}%  (r={d['corr']}, {d['region']})"
        for n, d in sorted(mkt.items(), key=lambda x: -x[1]["corr"])
    )

    tech_lines = []
    mv = ind.get("moving_averages", {})
    if mv:
        regime = "BULL MARKET" if mv.get("above_ma200") else "BEAR MARKET"
        tech_lines.append(f"Regime: {regime} | vs 200-MA: {mv.get('ma200_pct', 0):+.1f}% | vs 50-MA: {mv.get('ma50_pct', 0):+.1f}%")
        if mv.get("cross") in ("golden", "death"):
            tech_lines.append(f"*** {mv['cross'].upper()} CROSS DETECTED ***")
    rsi = ind.get("rsi", {})
    if rsi:
        tech_lines.append(f"RSI-14: {rsi['value']} ({rsi['signal']})")
    macd = ind.get("macd", {})
    if macd:
        cx = f" [{macd['crossover'].upper()} CROSSOVER]" if macd["crossover"] != "none" else ""
        tech_lines.append(f"MACD: {'above' if macd['above_signal'] else 'below'} signal{cx} | hist={macd['histogram']:+.3f}")
    adx = ind.get("adx", {})
    if adx:
        tech_lines.append(f"ADX: {adx['adx']:.1f} ({adx['trend_strength']}, {'bullish' if adx['bullish_trend'] else 'bearish'} DI bias)")
    bb = ind.get("bollinger", {})
    if bb:
        tech_lines.append(f"Bollinger: %B={bb['pct_b']:.2f} | width={bb['band_width']}% | {bb['position']}")
    stoch = ind.get("stochastic", {})
    if stoch:
        tech_lines.append(f"Stochastic K={stoch['k']:.1f} D={stoch['d']:.1f} ({stoch['zone']})")
    roc = ind.get("roc90", {})
    if roc:
        tech_lines.append(f"ROC-90: {roc['value']:+.1f}% ({roc['signal']})")
    w52 = ind.get("week52", {})
    if w52:
        tech_lines.append(f"52W: {w52['pct_of_range']:.0f}% of range | {w52['pct_from_high']:+.1f}% from high")

    news_text   = "\n".join(f"  [{h['source']}] {h['title']}" for h in news) or "  None fetched"
    sector_text = "\n".join(f"  {s}: {', '.join(stocks[:3])}" for s, stocks in SECTORS.items())
    other_rates = {k: v for k, v in other.items() if k in ["US 10Y Yield", "VIX"]}
    other_fx    = {k: v for k, v in other.items() if k in ["EUR/SEK", "USD/SEK", "EUR/USD", "DXY"]}
    other_comm  = {k: v for k, v in other.items() if k in ["Brent Oil", "Gold", "Copper"]}

    prompt = f"""Today is {day_label}. You are generating the OMX30 morning trading brief.

=== GLOBAL MARKET SIGNALS (prev session closes) ===
{mkt_lines}
Weighted correlation signal: {signal:+.3f}%

=== OMX30 TECHNICALS ===
{chr(10).join(tech_lines) if tech_lines else 'Insufficient data'}

=== RATES & VOLATILITY ===
{fmt(other_rates)}

=== FX ===
{fmt(other_fx)}

=== COMMODITIES ===
{fmt(other_comm)}

=== MARKET NEWS ===
{news_text}

=== OMX30 SECTORS ===
{sector_text}

=== SECTOR IMPACT RULES ===
- Yields up: banks POSITIVE (wider NIM), real estate NEGATIVE (refinancing costs), tech NEGATIVE (DCF compression)
- Oil up: industrials NEGATIVE (input costs), consumer NEGATIVE (spending pressure)
- Gold up: Boliden/Mining POSITIVE (direct revenue)
- Copper up: Boliden STRONGLY POSITIVE
- Strong USD/SEK (USD/SEK up): exporters POSITIVE (Volvo, Atlas Copco, Ericsson)
- Weak EUR/SEK: H&M NEGATIVE (sourcing costs)
- NASDAQ down: Ericsson/Hexagon NEGATIVE (sentiment)
- Risk-off: AstraZeneca/Essity POSITIVE (defensive rotation)
- ADX below 18: reduce confidence to Low and cut magnitude by 30%
- RSI above 70 or below 30: flag mean reversion risk

Generate the complete morning brief. Respond ONLY with valid JSON, no markdown, no backticks:
{{
  "recommendation": "BULLISH",
  "confidence": "Medium",
  "expectedMove": "+0.3%",
  "correlationBias": "BULLISH",
  "technicalBias": "NEUTRAL",
  "drivers": ["driver 1", "driver 2", "driver 3"],
  "narrative": "4-5 sentence synthesis referencing specific numbers, key technical levels, and main risk.",
  "morningBrief": "6-8 sentence trader-style briefing. Specific levels, sector calls, what to watch.",
  "sectorImpacts": [
    {{
      "sector": "Banks",
      "stocks": ["SEB A", "Handelsbanken A"],
      "direction": "POSITIVE",
      "magnitude": "Moderate",
      "reason": "US 10Y yield +3bp to 4.31% widens NIM expectations for Swedish banks.",
      "keyDriver": "yields_up"
    }}
  ],
  "watchList": [
    {{
      "stock": "Boliden",
      "action": "WATCH_LONG",
      "reason": "Gold +0.6% and copper firm — direct revenue drivers.",
      "catalyst": "Commodities"
    }}
  ],
  "keyLevels": {{
    "support": "3085 (lower Bollinger band)",
    "resistance": "3180 (50-MA)",
    "pivotWatch": "3123 (yesterday close)"
  }},
  "econCalendarAlert": "No major Swedish releases today. US Jobless Claims at 14:30 CET.",
  "topRisk": "Escalation in trade tensions could spike VIX and pressure all risk assets.",
  "technicalSummary": ["Above 200-MA (+9.8%)", "MACD above signal (bullish)", "RSI 58 neutral"]
}}"""

    client  = anthropic.Anthropic(api_key=API_KEY)
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2500,
        system="You are the head of research at a Swedish equity trading desk. Respond ONLY with valid JSON, nothing else.",
        messages=[{"role": "user", "content": prompt}],
    )

    text = message.content[0].text.strip()
    # Strip markdown fences if Claude wraps them
    if text.startswith("```"):
        lines = text.split("\n")
        text  = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])
    return json.loads(text)


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    today     = date.today()
    today_iso = today.strftime("%Y-%m-%d")
    today_lbl = today.strftime("%A %d %B %Y")

    print(f"\nOMX30 Morning Brief — {today_iso}")
    print("=" * 50)

    if today.weekday() >= 5:
        print("Weekend — nothing to do.")
        sys.exit(0)

    # Load existing scorecard (or start fresh)
    try:
        with open(SCORECARD) as f:
            scorecard = json.load(f)
    except Exception:
        scorecard = []

    if any(e["date"] == today_iso for e in scorecard):
        print("Brief already generated today — skipping.")
        sys.exit(0)

    # 1. Global markets
    print("\n[1/5] Global markets...")
    market_data = {}
    for name, info in MARKETS.items():
        pct, last = pct_and_last(info["symbol"])
        if pct is not None:
            market_data[name] = {**info, "change": pct, "last": last}
            print(f"  {name}: {pct:+.2f}%")
        time.sleep(0.4)

    if not market_data:
        print("ERROR: no market data fetched — aborting")
        sys.exit(1)

    total_corr = sum(v["corr"] for v in market_data.values())
    signal     = round(sum(v["change"] * v["corr"] / total_corr for v in market_data.values()), 3)
    print(f"  Weighted signal: {signal:+.3f}%")

    # 2. Rates / FX / Commodities
    print("\n[2/5] Rates, FX, commodities...")
    other_data = {}
    for name, symbol in OTHER.items():
        pct, last = pct_and_last(symbol)
        other_data[name] = {"change": pct, "last": last}
        if last:
            print(f"  {name}: {last:.4g}" + (f" ({pct:+.2f}%)" if pct else ""))
        time.sleep(0.35)

    # 3. OMX30 technicals
    print("\n[3/5] OMX30 technicals...")
    indicators = {}
    history    = omx_history()
    if history:
        closes, highs, lows = history
        indicators = compute_all(closes, highs, lows)
        print(f"  {len(closes)} days | " + " | ".join(indicators.get("summary", [])[:3]))
    else:
        print("  [warn] Could not fetch OMX30 history")

    # 4. News
    print("\n[4/5] News...")
    news = fetch_news()
    print(f"  {len(news)} headlines")

    # 5. Claude
    print("\n[5/5] Calling Claude...")
    analysis = call_claude(market_data, signal, indicators, other_data, news, today_lbl)
    print(f"  => {analysis['recommendation']} {analysis['expectedMove']} ({analysis['confidence']} confidence)")

    # Parse expected move to float
    try:
        predicted = float(analysis["expectedMove"].replace("%", "").replace("+", ""))
    except Exception:
        predicted = round(signal * 0.65, 2)

    # Build scorecard entry
    entry = {
        "date":             today_iso,
        "dateLabel":        today.strftime("%a %d %b"),
        "predicted":        predicted,
        "actual":           None,
        "result":           "pending",
        "confidence":       analysis.get("confidence", "Medium"),
        "recommendation":   analysis.get("recommendation", "NEUTRAL"),
        "technicalBias":    analysis.get("technicalBias", "NEUTRAL"),
        "correlationBias":  analysis.get("correlationBias", "NEUTRAL"),
        "drivers":          analysis.get("drivers", []),
        "narrative":        analysis.get("narrative", ""),
        "omxClose":         None,
        "magnitudeError":   None,
        "sectorImpacts":    analysis.get("sectorImpacts", []),
        "marketSnapshot":   {n: {"change": d["change"], "corr": d["corr"], "region": d["region"]}
                             for n, d in market_data.items()},
        "technicals":       {k: v for k, v in indicators.items() if k != "summary"},
        "technicalSummary": indicators.get("summary", []),
    }

    scorecard.insert(0, entry)
    scorecard = scorecard[:MAX_DAYS]

    os.makedirs(os.path.dirname(SCORECARD), exist_ok=True)
    with open(SCORECARD, "w") as f:
        json.dump(scorecard, f, indent=2, default=str)

    # Build full morning brief
    brief = {
        "date":              today_iso,
        "dateLabel":         today_lbl,
        "generatedAt":       datetime.utcnow().strftime("%H:%M UTC"),
        "recommendation":    analysis.get("recommendation", "NEUTRAL"),
        "confidence":        analysis.get("confidence", "Medium"),
        "expectedMove":      analysis.get("expectedMove", "0%"),
        "correlationBias":   analysis.get("correlationBias", "NEUTRAL"),
        "technicalBias":     analysis.get("technicalBias", "NEUTRAL"),
        "narrative":         analysis.get("narrative", ""),
        "morningBrief":      analysis.get("morningBrief", ""),
        "drivers":           analysis.get("drivers", []),
        "sectorImpacts":     analysis.get("sectorImpacts", []),
        "watchList":         analysis.get("watchList", []),
        "keyLevels":         analysis.get("keyLevels", {}),
        "econCalendarAlert": analysis.get("econCalendarAlert", ""),
        "topRisk":           analysis.get("topRisk", ""),
        "technicalSummary":  analysis.get("technicalSummary", []),
        "marketSnapshot":    {n: {"change": d["change"], "last": d.get("last"),
                                  "corr": d.get("corr"), "region": d.get("region")}
                              for n, d in market_data.items()},
        "otherData":         other_data,
        "newsHeadlines":     news,
        "technicals":        {k: v for k, v in indicators.items() if k != "summary"},
    }

    with open(BRIEF, "w") as f:
        json.dump(brief, f, indent=2, default=str)

    print(f"\nDone. Files written:")
    print(f"  {SCORECARD}")
    print(f"  {BRIEF}")


if __name__ == "__main__":
    main()
