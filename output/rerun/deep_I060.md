# I060 Trickle-vent refresh kit - deep analysis (re-run, 2026-11-11)

**Verdict: PARK / B2B validation test only (EUR 300-500).** The pain is plausible and the founders' installer/housing-association access is a real asset, but (a) the Nordic trickle-vent installed base is unproven, (b) the moat is a copyable compatibility library plus a weak registered design, (c) window OEMs probably sell their own spare filters, and (d) D2C paid economics are negative. It only works as a B2B/refill business and that is a hypothesis nobody has tested.

## 0. Evidence limits (read first)
- This session's WebSearch budget was exhausted, Firecrawl credits were exhausted, and WebFetch could not resolve idealhome.co.uk (outside allowed network). **No new web evidence was gathered.** amazon.de was not checked.
- The only URLs below are the three evidence links carried in the idea record (`all_ideas.json`, I060). I did not re-open them this session; they are forum/advice pages, i.e. anecdotes, not market data.
- Competitor names come from my background knowledge, are NOT verified, and have no URLs or prices. Anything numeric is labelled ASSUMPTION. Treat the whole file as a hypothesis map with Low confidence, not a validated analysis.

## 1. Product and real pain
Brush, die-cut dust/pollen filter inserts and clip-in baffles for common window trickle vents (kit EUR 19-25, refill EUR 12-15, landed cost EUR 3-5 per the record).
Pain evidence (record links, anecdotal): vents are often painted shut, clogged or closed in winter ([Ideal Home](https://www.idealhome.co.uk/house-manual/air-quality/should-you-close-window-vents-in-winter), [Mumsnet thread](https://www.mumsnet.com/talk/property/4490143-Ineffective-trickle-vents)); Swedish condensation/ventilation threads ([Byggahus](https://www.byggahus.se/forum/threads/obefintlig-ventilation-kondensproblem.128747/)).
Skeptic's note: two of three sources are UK. Trickle vents are a UK/Ireland-style item; Nordic dwellings mostly rely on mechanical exhaust or balanced ventilation with wall/frame supply-air valves (ASSUMPTION from general knowledge, unverified). Denmark has window-frame slot vents in many windows (ASSUMPTION). The Swedish thread is about condensation, not about trickle vents. So "Nordic trickle-vent owner" may be a much smaller group than the idea assumes.

## 2. Market sizing (Low confidence, all ASSUMPTION - no installed-base source found)
Dwellings: DK ~2.9m, SE ~5.2m (carried from the I075 analysis, unsourced here).
- Share with window-integrated vents that accept an insert: DK 25%, SE 15% => ~0.73m + ~0.78m = ~1.5m dwellings.
- Share actively bothered (dust, noise, pollen, blocked) and reachable: 20% => ~300k dwellings.
- **SAM Nordics (DK+SE):** one-off starter pool 300k x EUR 30 net = ~EUR 9m; recurring refill pool if 25% keep refilling x EUR 11 net = ~EUR 0.8m/yr. Say **EUR 9-10m one-off + ~EUR 1m/yr recurring.**
- **TAM EU:** ~200m EU dwellings (ASSUMPTION) x 10% with filterable vents x 20% bothered x EUR 30 = ~EUR 120-200m, dominated by UK-style/Benelux/DE markets with different profiles. Low confidence.
- **SOM year 1 (two part-timers, 10 h/wk):** 600-1,500 kits/inserts-sets, mostly B2B at ~EUR 9-11 wholesale => **EUR 6-15k revenue ex-VAT**, contribution EUR 3-8k. Side income, not a company.
Method: funnel multiplication with invented ratios; every ratio is the first thing to test.

## 3. Personas and JTBD
Personas:
1. Condensation-annoyed homeowner (DK/SE, 1990-2015 build or window-replaced home) - wants the window vent to work without a draught or dust.
2. Window installer / glazier / renovation contractor - wants an upsell and a way to close "my vent is blocked/noisy" callbacks.
3. Property manager / housing association maintenance (allmannytta, boligselskab, bostadsrattsforening) - wants cheap, repeatable annual service of supply-air points across many apartments (ASSUMPTION; likely bundled into existing maintenance contractors).
4. Allergy/pollen-sensitive household - buys on filter claim; **cannot be served with health claims** (see section 6).
JTBD: (1) keep the vent open without dust/insects/pollen coming in; (2) know my exact window profile and get the matching part without measuring; (3) replace the filter on a calendar, cheaply, with no tools; (4) for B2B: stop callbacks and prove maintenance was done.

## 4. Competitor / substitute map (UNVERIFIED - no URLs, no prices; to be checked)
| Type | Examples (from background knowledge) | Note |
|---|---|---|
| Window OEMs (spare parts) | VELUX (roof-window ventilation flap/filter), Nordic window makers (e.g. VELFAC, Rationel, Outline) | Most likely hold OEM spare filters; the aftermarket insert competes with free-to-the-installer OEM parts. Verify catalog existence and price. |
| Vent component brands | Titon, Greenwood Airvac, Renson, Siegenia, Aereco | Sell retrofit vents and canopies; the retrofit-vent substitute makes an insert unnecessary. |
| Generic filter media | Cut-to-size G3/G4 or pollen filter foam/fleece (hardware stores, Amazon, Biltema/Jula-type retail) | EUR 3-10 DIY substitute; this is the real price anchor. |
| Do nothing / close the vent | - | Dominant behaviour per the record links. |
Review-based gaps: not verifiable this session (no review data retrieved). Forum content suggests (anecdote) people do not know vents need cleaning and paint them shut; the "gap" may be awareness, which is expensive to buy with paid social.

## 5. Channels and CAC (ASSUMPTION benchmarks, no source)
- Shopify + Meta/TikTok: low-ticket EUR 22 kit, CAC EUR 18-35 => negative on first order. Search intent ("kondens fonster", "vinduesventil") is the only plausible D2C route; volume unknown.
- Amazon EU: no sourcing of listing data; expected dominated by generic filter media and private label (a kill criterion if confirmed).
- B2B installers/merchants (founders' network): cash CAC ~EUR 0-50 per account (samples + visit); time cost 3-5 h per account. Realistic: 15-25 installer accounts in year 1, 40 kits each.
- Housing associations: long cycles (6-18 months), framework purchasing, usually via maintenance contractors. Treat as upside, not plan.

## 6. EU/Nordic regulatory checklist (only what applies)
- GPSR (Reg. 2023/988): manufacturer/EU-importer name and address, batch/type number, safety information on product/pack.
- Flammability/material: filter media should have a stated fire class (e.g. EN 13501 or supplier datasheet) - ASSUMPTION it is wise, not confirmed mandatory for a passive insert.
- No CE marking expected for a passive insert; CE only if sold as part of a ventilation product (verify with a test house).
- **Claims:** no air-quality, allergy, asthma or mould-prevention claims (medical-claim kill and UCPD/Marketing law). Claim only "dust/insect filter insert, replace every X months".
- **Ventilation performance liability:** the insert adds pressure drop; Swedish BBR and Danish BR set air-change requirements. Selling to installers/housing requires a pressure-drop/airflow test and a clear "may reduce airflow" label. Confirm with a lab (EUR 500-1,500, ASSUMPTION).
- Packaging: EU PPWR/EPR registration (SE/DK) when volumes start; WEEE/batteries not applicable.
- VAT/OSS: 25% VAT in both SE and DK.

## 7. The moat, honestly
Stated: window-profile compatibility library + consumable filter inserts + B2B relationships.
- **Compatibility library:** obtain by measuring/photographing 20-40 profiles via installers; cost ~EUR 300-800 (samples, travel, die-cut tooling EUR 200-800 per steel-rule die, ASSUMPTION), time 3-6 months part-time. Copyist can reproduce it in weeks with a few window samples; installers will tell them the profiles. **Moat strength: low.**
- **Registered Community design** for insert/baffle shape: ~EUR 350 per design at EUIPO (ASSUMPTION from memory, verify); protects appearance only, easily designed around by changing a cut.
- **Consumable lock-in:** no genuine lock-in if the insert is a die-cut fleece; it is a commodity unless the retention clip/frame is proprietary and patentable (utility model in DE/DK costs ~EUR 500-1,500 + attorney, not budgeted). A proprietary snap-in frame with refill cartridges could create lock-in, but adds tooling toward the ~EUR 3-5k ceiling (injection mould) and is unproven.
- **B2B relationships:** the only real asset; but relationships do not stop an OEM adding a spare-part SKU. Circumvention paths: OEM spare filters, cheap Amazon/Biltema cut-to-size media, installers cutting their own.
Net: defensibility 2, not 3. The prior audit's 3 relied on "installer trust", which is unproven for a EUR 10 item.

## 8. Unit economics (ASSUMPTION; EUR; ex-VAT where stated)
D2C starter kit: price EUR 22 incl 25% VAT = 17.60 ex-VAT; payment 0.65; parcel shipping ~4.00; landed 4.00 => **contribution ~8.95**. Paid CAC 18-35 => **after CAC -9 to -26 per customer**. Refill EUR 13 incl VAT = 10.40; fees 0.40; letter-post 2.00; landed 1.50 => contribution ~6.50; payback of CAC needs 2-4 refills, but refill attach in year 1 is likely 20-30%. D2C paid does not work.
B2B installer: wholesale EUR 10/kit; landed 4.0; bulk freight/handling 0.5 => **contribution ~5.50 per kit, cash CAC ~EUR 0-50 per account**. At 25 accounts x 40 kits = 1,000 kits => ~EUR 5.5k contribution minus ~EUR 1.0k acquisition cash/samples => **~EUR 4.5k after CAC in year 1**, ~EUR 1-2k/yr per 10 accounts thereafter from refills. Capital: first order of 1,500 sets ~EUR 4.5-7.5k + tooling EUR 0.3-0.8k + airflow test EUR 0.5-1.5k = ~EUR 5.5-9.5k - at the edge of the soft ceiling for a product with ~EUR 5k year-1 contribution. Payback >1 year.

## 9. Re-score (1-5, skeptical)
| Criterion | Prior | Now | Why |
|---|---|---|---|
| Trend | 2 | 2 | Evidence anecdotal; "not verified as rising". |
| Defensibility | 3 | 2 | Library copyable in weeks; design right weak; OEM spare filters. |
| Margin | 4 | 4 | Gross margin >60% even at wholesale, but absolute EUR per unit small. |
| Repeat | 4 | 3 | Consumable is real, but annual replacement behaviour unproven and DIY substitute cheap. |
| EU scalability | 5 | 3 | Profile library is per-market; UK/BE/NL have vents, Nordics unproven. |
| Fit | 5 | 4 | Strong building-industry/installer edge; weak on filter media/airflow engineering. |
| Channel econ | 3 | 2 | D2C negative; B2B plausible but willingness-to-resell is unverified. |

## 10. Biggest risk
The Nordic addressable base (dwellings with trickle/slot vents that anyone wants a filter for) may be far smaller than modelled and installers may not resell a EUR 10 item; OEMs/DIY substitutes cap price.

## 11. Cheapest validation (EUR 300-500, 4-6 weeks, ~25 founder-hours)
1. 15-20 structured calls with installers, glaziers, window-service companies and 3-5 housing-association/property-maintenance managers: do they get blocked-vent callbacks, which windows, who supplies spare filters today, would they buy 40 sets at EUR 9-11? Target: >=6 say yes with a named volume and 3 sign a letter of intent.
2. Order OEM spare filters/vents for the 3 most common window brands to confirm price and availability (EUR 50-100); check if OEM kills the idea.
3. Landing page + simple "send a photo of your vent" form (EUR 100-200 incl. small search ads in SE/DK): target >=40 qualified submissions at EUR <5 each before any die is cut.
4. Prototype 20 hand-cut inserts for 2 profiles (EUR 50-100) and field-test with 5 installers.
Kill if: <3 installer LOIs, OEM spare price <= EUR 6, or fewer than 15 landing-page submissions.
