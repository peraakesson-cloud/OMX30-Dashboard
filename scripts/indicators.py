#!/usr/bin/env python3
"""
Technical Indicators for OMX30 Predictor
Computes: RSI-14, MACD(12/26/9), Bollinger Bands(20,2s),
MA50, MA200, ADX-14, Stochastic(14,3,3), ROC-90, 52-week range
"""
import numpy as np


def compute_rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    deltas = np.diff(closes[-(period + 1):])
    gains  = np.where(deltas > 0, deltas, 0.0)
    losses = np.where(deltas < 0, -deltas, 0.0)
    avg_gain = np.mean(gains)
    avg_loss = np.mean(losses)
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def ema(values, period):
    k = 2 / (period + 1)
    result = np.zeros(len(values))
    result[0] = values[0]
    for i in range(1, len(values)):
        result[i] = values[i] * k + result[i - 1] * (1 - k)
    return result


def compute_macd(closes):
    if len(closes) < 35:
        return None
    arr = np.array(closes, dtype=float)
    ema12 = ema(arr, 12)
    ema26 = ema(arr, 26)
    macd_line = ema12 - ema26
    signal    = ema(macd_line, 9)
    histogram = macd_line - signal
    crossover = "none"
    if macd_line[-1] > signal[-1] and macd_line[-2] <= signal[-2]:
        crossover = "bullish"
    elif macd_line[-1] < signal[-1] and macd_line[-2] >= signal[-2]:
        crossover = "bearish"
    return {
        "macd":         round(float(macd_line[-1]), 4),
        "signal":       round(float(signal[-1]), 4),
        "histogram":    round(float(histogram[-1]), 4),
        "crossover":    crossover,
        "above_signal": bool(macd_line[-1] > signal[-1]),
    }


def compute_bollinger(closes, period=20, num_std=2.0):
    if len(closes) < period:
        return None
    window = np.array(closes[-period:], dtype=float)
    mid    = np.mean(window)
    std    = np.std(window, ddof=1)
    upper  = mid + num_std * std
    lower  = mid - num_std * std
    price  = closes[-1]
    pct_b  = (price - lower) / (upper - lower) if upper != lower else 0.5
    bw     = round((upper - lower) / mid * 100, 2)
    if price > upper:   pos = "above_upper"
    elif price < lower: pos = "below_lower"
    elif price > mid:   pos = "upper_half"
    else:               pos = "lower_half"
    return {
        "upper":      round(upper, 2),
        "middle":     round(mid, 2),
        "lower":      round(lower, 2),
        "pct_b":      round(pct_b, 3),
        "band_width": bw,
        "position":   pos,
    }


def compute_moving_averages(closes):
    price  = closes[-1]
    result = {}
    if len(closes) >= 50:
        ma50 = round(float(np.mean(closes[-50:])), 2)
        result["ma50"]       = ma50
        result["ma50_pct"]   = round((price - ma50) / ma50 * 100, 2)
        result["above_ma50"] = bool(price > ma50)
    if len(closes) >= 200:
        ma200 = round(float(np.mean(closes[-200:])), 2)
        result["ma200"]       = ma200
        result["ma200_pct"]   = round((price - ma200) / ma200 * 100, 2)
        result["above_ma200"] = bool(price > ma200)
    if len(closes) >= 201 and "ma50" in result and "ma200" in result:
        prev_ma50  = float(np.mean(closes[-51:-1]))
        prev_ma200 = float(np.mean(closes[-201:-1]))
        if result["ma50"] > result["ma200"] and prev_ma50 <= prev_ma200:
            result["cross"] = "golden"
        elif result["ma50"] < result["ma200"] and prev_ma50 >= prev_ma200:
            result["cross"] = "death"
        else:
            result["cross"] = "none"
    return result


def compute_adx(highs, lows, closes, period=14):
    if len(closes) < period * 2:
        return None
    h = np.array(highs[-(period * 2):], dtype=float)
    l = np.array(lows[ -(period * 2):], dtype=float)
    c = np.array(closes[-(period * 2):], dtype=float)
    tr_list, plus_dm, minus_dm = [], [], []
    for i in range(1, len(c)):
        tr  = max(h[i] - l[i], abs(h[i] - c[i-1]), abs(l[i] - c[i-1]))
        pdm = max(h[i] - h[i-1], 0) if (h[i] - h[i-1]) > (l[i-1] - l[i]) else 0
        mdm = max(l[i-1] - l[i], 0) if (l[i-1] - l[i]) > (h[i] - h[i-1]) else 0
        tr_list.append(tr); plus_dm.append(pdm); minus_dm.append(mdm)
    atr  = np.mean(np.array(tr_list)[-period:])
    apdi = np.mean(np.array(plus_dm)[-period:])
    amdi = np.mean(np.array(minus_dm)[-period:])
    if atr == 0:
        return None
    pdi = 100 * apdi / atr
    mdi = 100 * amdi / atr
    dx  = 100 * abs(pdi - mdi) / (pdi + mdi) if (pdi + mdi) > 0 else 0
    strength = "strong" if dx > 25 else "moderate" if dx > 18 else "weak"
    return {
        "adx":            round(dx, 2),
        "plus_di":        round(pdi, 2),
        "minus_di":       round(mdi, 2),
        "trend_strength": strength,
        "bullish_trend":  bool(pdi > mdi),
    }


def compute_stochastic(highs, lows, closes, k_period=14, d_period=3):
    if len(closes) < k_period + d_period:
        return None
    k_values = []
    for i in range(d_period + 1):
        idx      = -(d_period - i) if (d_period - i) > 0 else None
        wh = highs[-(k_period + d_period - i): idx]
        wl = lows[ -(k_period + d_period - i): idx]
        cv = closes[idx - 1] if idx else closes[-1]
        hi = max(wh); lo = min(wl)
        k_values.append((cv - lo) / (hi - lo) * 100 if hi != lo else 50.0)
    k    = round(k_values[-1], 2)
    d    = round(float(np.mean(k_values[-d_period:])), 2)
    zone = "overbought" if k > 80 else "oversold" if k < 20 else "neutral"
    return {"k": k, "d": d, "zone": zone, "k_above_d": bool(k > d)}


def compute_roc(closes, period=90):
    if len(closes) < period + 1:
        return None
    return round((closes[-1] - closes[-period - 1]) / closes[-period - 1] * 100, 2)


def compute_52w(closes):
    if len(closes) < 252:
        return None
    window = closes[-252:]
    hi     = max(window); lo = min(window); price = closes[-1]
    pct_r  = (price - lo) / (hi - lo) * 100 if hi != lo else 50
    return {
        "high52":        round(hi, 2),
        "low52":         round(lo, 2),
        "pct_from_high": round((price - hi) / hi * 100, 2),
        "pct_from_low":  round((price - lo) / lo * 100, 2),
        "pct_of_range":  round(pct_r, 1),
    }


def compute_all(closes, highs, lows):
    ind = {}

    rsi = compute_rsi(closes)
    if rsi is not None:
        ind["rsi"] = {
            "value":  rsi,
            "signal": "overbought" if rsi > 70 else "oversold" if rsi < 30 else "neutral",
        }

    macd = compute_macd(closes)
    if macd:
        ind["macd"] = macd

    bb = compute_bollinger(closes)
    if bb:
        ind["bollinger"] = bb

    mv = compute_moving_averages(closes)
    if mv:
        ind["moving_averages"] = mv

    adx = compute_adx(highs, lows, closes)
    if adx:
        ind["adx"] = adx

    st = compute_stochastic(highs, lows, closes)
    if st:
        ind["stochastic"] = st

    roc = compute_roc(closes)
    if roc is not None:
        ind["roc90"] = {
            "value":  roc,
            "signal": "strong_momentum" if roc > 5 else "weak_momentum" if roc < -5 else "neutral",
        }

    w52 = compute_52w(closes)
    if w52:
        ind["week52"] = w52

    # Build human-readable summary for Claude
    summary = []
    if "rsi" in ind and ind["rsi"]["signal"] != "neutral":
        summary.append(f"RSI {ind['rsi']['signal']} ({rsi:.0f})")
    if "macd" in ind:
        m = ind["macd"]
        if m["crossover"] != "none":
            summary.append(f"MACD {m['crossover']} crossover")
        else:
            summary.append("MACD above signal" if m["above_signal"] else "MACD below signal")
    if "moving_averages" in ind:
        mv2 = ind["moving_averages"]
        if "above_ma200" in mv2:
            summary.append(f"{'Above' if mv2['above_ma200'] else 'Below'} 200-MA ({mv2.get('ma200_pct',0):+.1f}%)")
        if "above_ma50" in mv2:
            summary.append(f"{'Above' if mv2['above_ma50'] else 'Below'} 50-MA ({mv2.get('ma50_pct',0):+.1f}%)")
        if mv2.get("cross") in ("golden", "death"):
            summary.append(f"*** {mv2['cross'].upper()} CROSS ***")
    if "adx" in ind:
        a = ind["adx"]
        summary.append(f"ADX {a['adx']:.0f} ({a['trend_strength']} trend, {'bullish' if a['bullish_trend'] else 'bearish'} bias)")
    if "stochastic" in ind and ind["stochastic"]["zone"] != "neutral":
        summary.append(f"Stochastic {ind['stochastic']['zone']} (K={ind['stochastic']['k']:.0f})")
    if "roc90" in ind and ind["roc90"]["signal"] != "neutral":
        summary.append(f"3M momentum: {ind['roc90']['value']:+.1f}% ({ind['roc90']['signal']})")

    ind["summary"] = summary
    return ind
