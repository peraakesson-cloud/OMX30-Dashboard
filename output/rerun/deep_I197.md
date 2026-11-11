# I197 - Window Maintenance Spare Kit: deep analysis (re-run, 2026-11-11)

**Verdict: PARK. Do not order stock. At most run a zero-capital B2B pilot (section 10); proceed only if installers/merchants pre-commit.** The stated moat (installer/BRF channel plus fit guide) is real as a *route to market* but is not a moat against copying, and the incumbent (VELUX) already sells a care kit through DIY chains.

## Evidence limits (read first)
- This session: WebSearch budget exhausted, Firecrawl out of credits, and WebFetch could not resolve velux.com, euronews.com, amazon.de or hornbach.de (hosts not allowed in session network). **I saw no new web pages in this run.**
- Facts with URLs below come from the earlier pass record `/home/user/OMX30-Dashboard/output/phase3/I197.md` (pages seen then, not re-opened now): Medium confidence for prices, Low for everything else. Everything else is labelled ASSUMPTION. No competitor, price or supplier has been invented. Not verified: Amazon.de/.se listings and reviews, VELUX spare-part pricing on velux sites, number of Nordic roof windows, installer purchasing behaviour, any supplier quote.

## Product
Fit-guided kit for roof/standard windows: replacement seal profile cut to type, hinge grease, groove gauge, how-to. Price EUR 29-39; landed EUR 7-11 (record estimate, unquoted); no tooling if stock EPDM profile is used.

## 1. Market size (Low confidence throughout)
No sourced bottom-up exists for Nordic window maintenance spend. Sourced anchors only:
- Europe roof-window market about USD 1.03bn in 2024 (aggregator, all windows not parts): https://www.credenceresearch.com/report/europe-roof-windows-market
- 51.7% of EU population lived in a house in 2023: https://ec.europa.eu/eurostat/web/interactive-publications/housing-2024
- SCB housing statistics exist for dwelling counts (not opened): https://scb.se/bo0104-en

| Level | Figure | Method | Confidence |
|---|---|---|---|
| TAM EU | EUR 100-200M/yr | ASSUMPTION: EU houses with 20+ yr windows x low single-digit % buying a seal/maintenance product x ~EUR 30 | Low |
| SAM Nordics (SE+DK online-reachable, incl. NO/FI later) | EUR 2-5M/yr | ASSUMPTION: ~2.5M older detached houses with roof windows; 3% buy a kit/year = ~75k kits x EUR 30 | Low |
| SOM year 1 | EUR 6-20k revenue (200-600 kits) | ASSUMPTION: two part-timers, ~450 h/yr; B2B pilot of 5-10 installers/merchants plus organic search | Low |

Skeptic note: seals last 10-20 years, so annual purchase rate is probably below 3%; real SAM may be half the above.

## 2. Personas
1. **DIY homeowner (40-65), detached house with roof windows**: draught/condensation, wants a cheap fix before winter.
2. **Installer/roofer/handyman (ex-VELUX network)**: buys seals by the metre at trade, wants correct-fit in the van; kit price is irrelevant to him, hassle is.
3. **BRF/housing-association caretaker/property manager**: many units, wants standard spares plus documentation; buys through frame contracts, rarely from a EUR 29 kit.
4. **Building merchant/DIY chain buyer**: gatekeeper; wants a SKU with margin and a compatibility chart.

## 3. Jobs to be done
- Identify the right seal for my window (brand/model/year) without climbing a ladder twice.
- Replace the seal/lubricate hinges correctly and verify the draught is gone.
- (Installer) Stock a short list of correct-fit parts, avoid callbacks.
- (BRF) Do planned maintenance across units with predictable cost.

## 4. Competitor map (REAL, from earlier pass; not re-opened)
| Competitor | Price | Note | URL |
|---|---|---|---|
| VELUX Kombi-Pflege-Set ZZZ 220 (grease, filter, foam seal for vent flap, strips, sandpaper) | EUR 25.99 at OBI (UVP 34.99, +4.95 ship); EUR 31.90 Hornbach.at | Brand-owner care kit in DIY chains; direct substitute; does not include main glazing seal | https://www.obi.de/p/1302561/velux-kombi-pflege-set-zzz-220 ; https://www.hornbach.at/p/velux-kombi-pflege-set-zzz-220-fuer-kunststoff-und-holzfenster/8422852/ |
| Graf Dichtungen roof-window profiles (Velux/Braas/Roto) | ~EUR 5-6/m | Model-specific by the metre | https://www.graf-dichtungen.de/pdfdatasheet/9da0254bae71432ca53a5724a3f73ddc |
| Hornbach Roto-compatible seal, 10 m | EUR 51.53 | Brand-specific roll | https://www.hornbach.de/p/dachfensterdichtung-fuer-roto-dachflaechenfenster-grau-10-meter-19-mm-hoehe-dichtung-fuer-dachfenster-zuverlaessig-gegen-zugluft-und-feuchtigkeit/12845447/ |
| Bauhaus DK universal self-adhesive strip 6 m | DKK 199.95 (~EUR 27) | Generic draught strip | https://www.bauhaus.dk/primo-taetningsliste-selvklaebende-universal-gra |
| Jem & Fix universal strip 6 m (DK) | not captured | Generic | https://www.jemogfix.dk/taetningsliste-universal-evo-hvid-6-m/4212/9044334 |
| Used OEM seals, finn.no | 1,500 kr for 4 (private listing) | Shows OEM profile scarcity/value | https://www.finn.no/439508335 |
Amazon.de/.se tapes: not verified; ASSUMPTION that many sub-EUR 15 generic tapes exist.

## 5. Review gaps (hypotheses, no review data seen)
Likely complaints (ASSUMPTION, test in interviews): wrong profile or size; instructions unclear; adhesive fails in cold; kit omits the main seal. Fiddliness of fitting is documented by Teknologisk Institut (size the groove with modelling wax): https://www.teknologisk.dk/_/media/72509%5FKlimask%E6rm%20%2D%20Faktaark%20%2D%20T%E6tningslister%20p%E5%20vinduer.pdf . Gap the founders could own: a verified brand/model/year to profile lookup, which is a data asset, not a product feature.

## 6. Channels and CAC
- Benchmarks (vendor blogs, conflicting): Meta CPM DE ~EUR 9.05; DTC Meta CPA USD 38-58; home category conversion ~0.9%: https://eightx.co/blog/eu-ecommerce-cac-benchmark , https://eightx.co/blog/germany-ecommerce-cac-benchmark
- **Paid D2C CAC ASSUMPTION EUR 25-50** for a EUR 30 low-intent item: unprofitable.
- **B2B/installer channel CAC ASSUMPTION EUR 3-8 per kit-equivalent** (founder time only: ~2 h per installer account, 8-10 accounts, spread over repeat orders). This is the only economic route, but it depends on installers wanting a branded kit; I expect them to prefer metre-priced trade profiles (Graf at EUR 5-6/m shows the reference price).
- Organic: how-to SEO ("tætning vindue", "byta tätningslist takfönster") and YouTube; slow (6-12 months).
- Amazon EU: referral ~15% (ASSUMPTION), price-pressured by generics.

## 7. Regulatory checklist (applicable only)
- **GPSR (EU 2023/988)**: EU responsible person, traceability, safety info and labelling.
- **Trademark**: no VELUX name/logo/part numbers as branding; nominative "fits..." statements only after legal check. Check founders' ex-employer non-compete/confidentiality on customer lists and technical data (important for the channel moat).
- **CLP/SDS**: hinge grease is a mixture; buy a finished, non-classified grease with supplier SDS.
- **REACH**: supplier declaration for EPDM profiles (ASSUMPTION).
- **Packaging EPR**: SE and DK registrations before selling (not researched here).
- CE marking: not expected for a seal kit (ASSUMPTION, confirm). No medical/battery kill triggers.

## 8. The specific moat: what it is, cost, time, circumvention
| Element | How to obtain | Cost / time | How circumvented |
|---|---|---|---|
| **B2B channel** (installers, BRFs, merchants) | Personal outreach through ex-VELUX contacts; frame agreement or pilot pack | EUR 0-500 for samples; 2-4 months to first 5-10 accounts (ASSUMPTION) | A competitor with its own relationships or a merchant's private label; VELUX itself. Relationships are personal and non-transferable, which is the only hurdle. |
| **Fit-guide / compatibility database** | Measure and photograph profiles per brand/model/year | 40-80 founder hours (ASSUMPTION) | Copyable by anyone with the same windows in weeks; protected only weakly (database right is thin) |
| **Exclusive seal-profile supplier** | Negotiate exclusivity in a chosen market with an extruder | Unsecured (ASSUMPTION); needs volume commitments the budget cannot back | Any other extruder can produce a profile to the same geometry; exclusivity only helps if the profile is a proprietary design (not the case for stock EPDM) |
| Registered Community design / utility model for a *new* seal clip or gauge | Develop a genuinely new part | EUR 350-1,000 filing (ASSUMPTION), tooling EUR 3-5k | Design around; most seals are standard geometry, so no protectable novelty |
Net: **moat = relationships plus data, no IP.** A copyist can replicate the product in weeks; the relationship channel buys head start, not exclusion. Defensibility 2.

## 9. Unit economics (ASSUMPTION unless cited)
Retail EUR 35 incl. 25% VAT = EUR 28 net; landed EUR 9 (record 7-11); gross margin ~68% (61% at EUR 29).

| Line (per kit, EUR) | D2C paid | B2B via installer/merchant |
|---|---|---|
| Net price | 28.0 | 19-21 (trade, 25-30% off retail) |
| Landed cost | 9.0 | 9.0 |
| Shipping/pick-pack | 4-6 | 1-2 (bulk) |
| Payment fees/returns (wrong fit) | 1.5-2.5 | 0.3 |
| **Contribution before CAC** | **~10-13** | **~8-10** |
| CAC | 25-50 | 3-8 |
| **Contribution after CAC** | **-12 to -40** | **~0 to +7** |
B2B is the only path that does not lose money per unit, and the margin is thin; it works only if installers reorder (ASSUMPTION: seal changes are a once-per-window-lifetime event, so repeat is low; grease is a small top-up). First order ~EUR 3.5k for 400-500 units (screen estimate, unquoted), inside the capital limit.

## 10. Cheapest validation test (EUR 0-300, 4 weeks, ~15 founder hours)
1. Ask 10 ex-VELUX installers/merchants/BRF caretakers (calls or LinkedIn): "How many roof-window seal/care jobs per year, what do you buy, from whom, at what price, would you stock a model-matched kit at EUR 19-21 trade?"
2. Pre-sell: mock one kit page plus a one-page fit chart; ask for a non-binding order of 20 kits from 3 accounts (or a merchant listing commitment).
3. In parallel: Google Keyword Planner/Trends volumes for SE/DK seal queries (free).
**Go threshold:** at least 3 accounts commit to 20+ kits each, or 1 merchant agrees to list. Otherwise stop; no capital spent.

## 11. Re-score (1-5, honest)
| Criterion | Re-run record | My score | Reasoning |
|---|---|---|---|
| Trend | 2 | **2** | Repair-over-replace direction is real but the only linked article concerns appliances; energy-saving demand for window seals unverified. |
| Defensibility | 2 | **2** | Channel plus guide, no IP; stock EPDM commodity; exclusivity unsecured. |
| Margin | 4 | **3** | 61-68% gross on net price, but contribution before CAC only EUR 8-13 after shipping, fees and returns. |
| Repeat | 3 | **2** | Seals last years; grease is trivial; B2B reorders only if installers adopt it. |
| EU | 4 | **4** | Same housing stock and products across SE/DK/NO/FI/DE; GPSR only; EPR per country. |
| Fit | 5 | **4** | Strong founder knowledge, but trademark/non-compete limits using the very edge. |
| Channel economics | 4 | **3** | B2B low CAC is plausible but unproven; D2C paid is negative. |

## Biggest risk
VELUX (or a merchant private label) already occupies the kit niche at EUR 26-32, and installers may buy the seal by the metre at trade price (EUR 5-6/m) rather than a branded kit, so the B2B channel may not pay a kit margin.

## Confidence
Low-Medium. Prices of competitors are Medium (seen earlier); all market sizing, CAC, trade price and installer demand are ASSUMPTION.
