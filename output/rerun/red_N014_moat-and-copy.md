# Red-team N014 Nordic FTX Filter Club - moat and copy angle (2026-11-11)

## Research limits (state plainly)
WebSearch budget exhausted, Firecrawl out of credits (resets 21:36 UTC), WebFetch cannot resolve bauhaus.se, ri.se, filterbutiken.se (outside allowed network domains).
NO new URL was seen this run. Everything below is domain reasoning, labelled ASSUMPTION / Low-Medium confidence. Nothing here is a verified finding.

## Strongest attacks
1. FATAL-ish: the moat is a document, not an exclusion right. ISO 16890 report = anyone can buy it (the prior record admits this). A test report proves a class for ONE media+construction; it does not stop a copier. Moat score should be 1-2.
2. Registered design on the frame is near worthless: EU design protection excludes features solely dictated by technical function (Reg. 6/2002 Art. 8(1), domain knowledge, not re-fetched) and the frame must match OEM housings; a copier changes a rib/corner radius or uses a different frame (or frameless pad) and routes around in weeks. Also no utility model in EU-wide form; Swedish/Danish utility models do not cover a plain pre-cut pad. Patentability: none (obvious).
3. The actual product is commodity: cut synthetic/glass media in a cardboard or plastic frame. Media is bought from the same few converters (Camfil, Freudenberg, Lydall/Hollingsworth, Chinese converters). Sourcing edge is replicable by anyone with an Alibaba account; a Chinese converter can quote F7 pocket/panel sets at USD 2-5 per piece (ASSUMPTION, Low).
4. Compatible filters almost certainly already exist (unverified): Nordic filter e-shops and VVS wholesalers (Ahlsell, Dahl, Solar, Lemvigh-Müller are the big installer distributors; names known, filter lines not verified) sell own-brand/compatible sets to the same installers. The installer's trade price from OEM is already discounted; a 2-person startup offering EUR 24 net is unlikely to beat distributor own-label at scale or the installer's convenience of one-stop wholesale account.
5. Installers are the channel AND the threat: installer margin on OEM filters is real, but they also hold service contracts and fear warranty/liability blame when a third-party filter underperforms. A founder network (ex-VELUX, ex-Nilfisk) does NOT reach ventilation service firms - prior record concedes this. 8-15 active installers in year 1 is optimistic; 3-5 is more likely.
6. OEM response is trivial: Genvex/Flexit/Nilan can (a) cut trade price, (b) key warranty to original filters (already stated by Genvex), (c) change frame geometry on a new unit generation. Also OEMs sell subscription/reminder services themselves (assumption). Pollen-season reminder is an email flow, copyable in a day.
7. Subscription lock-in is weak: unit is a replaceable standard-size consumable; cancel at will under EU consumer law; D2C retention 65% is ASSUMPTION with no source. Consumables "lock-in" only works with a proprietary format, which here is the reverse (you must fit OEM format).
8. Unit economics: EUR 39 incl VAT = EUR 31.2 net; after Shopify/payment, pick-pack, SE/DK freight for a light parcel (~EUR 6 assumed, DK/SE postal for 0.5-1 kg often higher, ASSUMPTION), returns for wrong-fit (the core risk of a fit-critical product: wrong size => return + warranty argument), and 25% Amazon-style fee if marketplace used, contribution ~EUR 12-15 vs CAC 12-25 => D2C first order roughly break-even to negative, as the prior record says. Lab cost EUR 2-5k per family is a multiple (3 SKUs = up to 3 families?) -> could be EUR 6-15k, breaching the EUR 5k moat ceiling. Prior note "per media/construction family" means several tests if you want sets for multiple media.
9. Revenue ceiling: contestable SAM EUR 3-5m, year-1 contribution EUR 5-12k on EUR 7-10k up-front, i.e. no payback in year 1 and a 2-founder business capped near a side job unless OEM-brand-adjacent volume is won. Fit for an "owned brand" ambition is weak: it is a parts-compatible reseller, not a brand.

## Likely copiers and speed
- Nordic VVS wholesalers/online filter shops (own-label): weeks to add a line; already have installer accounts. (names of wholesalers: domain knowledge, filter lines unverified)
- Amazon.de/.se and AliExpress/Temu sellers of generic F7/G4 pads cut to size: 2-6 weeks; they ignore ISO reports but sell "F7" claims; price pressure from below.
- Camfil, Freudenberg-type incumbents/Eurovent-certified brands already hold ISO 16890 reports; could sell sets via distributors at any time.
- OEMs themselves (Flexit, Genvex, Nilan, Systemair): price/warranty response.
- IKEA/Jula/Biltema/Clas Ohlson/Bauhaus/Hornbach: Hornbach/Bauhaus already sell vent filters (Hornbach.se 3-pack ~SEK 109 per prior record; Bauhaus Flexit set SEK 635, URLs from prior record, not re-opened). Biltema/Jula private-label is a real threat if the category shows volume (retailer private label is a hard-kill category type).
- Design houses (Hay, Normann): irrelevant.

## Revised scores (1-5)
trend 3, defensibility 1, margin 3, repeat 3, eu 2, fit 3, channel_econ 2 (total ~2.4)

## Verdict
Only if fixed. Defensibility 1: certification report and registered design give no exclusivity. Revealed demand and compatible-filter prior art are unchecked.

## What would fix it
- Move the moat to an exclusivity: a signed exclusive/preferred-supplier or co-branded agreement with ONE OEM or one housing-association portfolio/service chain (multi-year filter service contract for X units). Contract = real moat; test report is not.
- Or a proprietary quick-change cartridge format for retrofit housings (utility model/design, pleated frame with colour-coded model key) that installers prefer, but then fit with OEM units breaks.
- Pre-sell: written LOIs from 5+ installers plus a lab quote under EUR 5k before spending; and verify the existence/price of compatible filters on Nordic e-shops (not done this run).
- Re-run with network access: search EUIPO/Espacenet for ventilation filter frame designs, Hornbach/Bauhaus/Jula/Biltema filter ranges, filter e-shops, lab quotes.
