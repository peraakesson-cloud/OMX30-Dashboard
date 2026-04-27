# OMX30 Morning Desk — Complete Setup Guide

A fully automated daily trading dashboard for the Stockholm Stock Exchange.
Every weekday at 07:55 CET, it fetches live market data, runs technical
analysis, and uses Claude AI to generate a complete morning brief with
sector-level impact analysis.

---

## What you get

- **Morning brief** — OMX30 directional call, expected move, narrative
- **Sector analysis** — which sectors and stocks are impacted and why
- **Watch list** — specific LONG/SHORT/MONITOR calls with catalysts
- **Market data** — global indices, rates, FX, commodities
- **Technical indicators** — RSI, MACD, MA50/200, ADX, Bollinger Bands
- **News feed** — Reuters and FT headlines
- **30-day scorecard** — tracks prediction accuracy over time

---

## Step 1 — Get an Anthropic API key

1. Go to **console.anthropic.com** and create an account
2. Click **API Keys → Create Key**
3. Copy the key (starts with `sk-ant-api03-...`)
4. Go to **Billing → Add payment method → Load $5 credits**
   - This is pay-as-you-go, NOT a subscription
   - Your script costs ~$0.03/day = ~$0.65/month
   - $5 will last roughly 7 months

---

## Step 2 — Create a GitHub account

Go to **github.com** and sign up if you don't have an account (it's free).

---

## Step 3 — Create a new repository

1. Click the **+** icon (top right) → **New repository**
2. Name it: `OMX30-Dashboard`
3. Set to **Public** (required for free GitHub Pages)
4. Leave everything else as default
5. Click **Create repository**

---

## Step 4 — Upload all files

In your new empty repository, click **uploading an existing file** or
**Add file → Upload files**. Upload ALL files maintaining this structure:

```
OMX30-Dashboard/
├── index.html
├── data/
│   ├── scorecard.json
│   └── morning_brief.json
├── scripts/
│   ├── morning.py
│   ├── evening.py
│   └── indicators.py
└── .github/
    └── workflows/
        ├── morning.yml
        ├── evening.yml
        └── deploy.yml
```

**Important:** The `.github` folder is hidden on Mac/Linux. Make sure
to include it — it contains the automation workflows.

Click **Commit changes** after uploading.

---

## Step 5 — Add your API key as a secret

1. In your repo, click **Settings** (top menu)
2. Left sidebar → **Secrets and variables → Actions**
3. Click **New repository secret**
4. Name: `ANTHROPIC_API_KEY` (exactly this, case-sensitive)
5. Value: paste your key from Step 1
6. Click **Add secret**

---

## Step 6 — Set workflow permissions

1. Still in **Settings**, click **Actions → General** in the left sidebar
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Click **Save**

---

## Step 7 — Enable GitHub Pages

1. Still in **Settings**, click **Pages** in the left sidebar
2. Under **Source**, select **GitHub Actions**
3. Click **Save**

---

## Step 8 — Test it manually

1. Click the **Actions** tab in your repo
2. You should see 3 workflows in the left sidebar:
   - Morning Brief
   - Evening Update
   - Deploy Site

3. Click **Deploy Site** → **Run workflow** → **Run workflow**
   - Wait ~30 seconds for green tick ✅
   - Your site is now live at: `https://YOUR-USERNAME.github.io/OMX30-Dashboard`

4. Click **Morning Brief** → **Run workflow** → **Run workflow**
   - This fetches live data and calls Claude (~60 seconds)
   - After it completes, **Deploy Site** fires automatically
   - Refresh your site — the brief should update with today's data

---

## Step 9 — Verify it works

Visit your site URL. You should see:
- The masthead with today's date
- The OMX30 signal (BULLISH/BEARISH/NEUTRAL)
- Market data panels
- Sector impact cards
- Watch list

If you see the seed data (Thu 24 Apr 2026) instead of today's data,
the Morning Brief workflow hasn't run yet — run it manually as in Step 8.

---

## Automatic schedule

Once set up, everything runs automatically:

| Time (CET) | Action |
|---|---|
| 07:55 Mon–Fri | Fetch markets + Claude analysis → update site |
| 18:30 Mon–Fri | Fetch OMX30 close → update scorecard result |
| On every push | Site redeploys automatically |

**Timezone note:**
- Summer (CEST, UTC+2): cron uses `55 5` = 07:55 CET ✅
- Winter (CET, UTC+1): change to `55 6` in morning.yml and `30 17` in evening.yml

---

## Troubleshooting

**Workflow fails with "exit code 1"**
→ Click into the failed run → click the red job → expand the Python step
→ Read the error message carefully

**401 Unauthorized**
→ API key is missing or wrong. Go to Settings → Secrets and re-add it.

**404 Not Found (from Anthropic)**
→ The script now uses the official Anthropic SDK which handles this correctly.
   Make sure you're using the latest morning.py from this package.

**Site shows old data**
→ Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
→ Or open in a private/incognito window

**Morning Brief says "skipping" on re-run**
→ It skips if today's entry already exists. This is intentional.
   To force a re-run, delete today's entry from data/scorecard.json.

**Pages shows 404**
→ Settings → Pages → Source must be "GitHub Actions" (not a branch)

---

## Cost summary

| Service | Cost |
|---|---|
| GitHub (repo + Actions + Pages) | Free |
| Anthropic API (~22 calls/month) | ~$0.65/month |
| **Total** | **~$0.65/month** |

---

## Correlation model

Correlations based on ~2,500 trading days (2015–2024):

| Market | r (same-day) | Timing |
|---|---|---|
| DAX 40 | 0.89 | Concurrent |
| CAC 40 | 0.85 | Concurrent |
| FTSE 100 | 0.78 | Concurrent |
| S&P 500 | 0.52 | Next-day lag |
| Dow Jones | 0.51 | Next-day lag |
| NASDAQ | 0.49 | Next-day lag |
| Nikkei 225 | 0.38 | Same-day open |
| Hang Seng | 0.31 | Same-day open |
| Shanghai | 0.22 | Same-day open |

Sources: Berben & Jansen (2005), Longin & Solnik (2001),
ECB working papers, Nasdaq Nordic annual reports 2015–2024.

---

**Not financial advice. For informational purposes only.**
