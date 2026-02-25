It’s completely valid to question whether merchant‑level recommendation actually moves card revenue. The honest answer is: it can, but only when framed correctly. The value does not come from “recommending random merchants.” It comes from influencing category‑level spend behavior, share‑of‑wallet, and activation, all of which are revenue drivers even when interchange is MCC‑based.
The key is to design the system so it is compliance‑safe, commercially meaningful, and aligned with how interchange and card economics actually work.

1) Whether a bank can recommend merchants without partnerships
Banks do this already in multiple forms, but the framing matters.
Normal and compliant when:
- The recommendation is customer‑centric (“places you might like based on your spend pattern”).
- There is no financial incentive tied to a specific merchant.
- The bank is not implying endorsement or commercial relationship.
- The logic is algorithmic, not paid placement.
This is the same category as:
- “People like you also shop at…”
- “Popular merchants near you…”
- “Your top categories this month…”
These are considered content personalization, not advertising.
Requires caution when:
- The bank receives compensation from the merchant.
- The recommendation could be interpreted as an advertisement.
- The merchant is sensitive (e.g., gambling, political, medical).
In those cases, you need:
- Clear disclosure
- Opt‑in or preference controls
- Internal marketing compliance review
But recommending merchants based on customer behavior is widely accepted and used by:
- Revolut
- Monzo
- Capital One
- Chase
- DBS
All without merchant partnerships.

2) Whether granular merchant categories matter if interchange is MCC‑based
You’re right that interchange is determined at the MCC level, not merchant level.
But merchant‑level semantics still drive revenue through three other levers that matter more than MCC granularity.
Lever 1 — Increasing share of wallet within a category
Even if two merchants share the same MCC, the customer’s spend distribution is not fixed.
Example:
A customer spends HKD 2,000/month on “Restaurants (MCC 5812)”.
If your card captures HKD 800 today, and you shift it to HKD 1,200, you gain 50% more interchange even though the MCC is unchanged.
LLM‑based merchant embeddings help by:
- identifying the customer’s preferred sub‑segments (ramen vs. dim sum vs. fast casual)
- recommending merchants aligned with their taste
- nudging spend toward your card
This is incremental revenue, not MCC‑dependent.
Lever 2 — Increasing activation and frequency
Merchant recommendations can:
- remind customers of merchants they like
- surface new merchants similar to their favorites
- increase card usage frequency
Interchange revenue is proportional to number of transactions × average ticket size.
Even if MCC is unchanged, more transactions = more revenue.
Lever 3 — Increasing cross‑category expansion
LLM embeddings reveal customer affinities across categories.
Example:
A customer who shops at Nike (sportswear) may also like Decathlon (sports equipment).
Different MCCs, but same semantic cluster.
This expands spend into:
- sporting goods
- outdoor
- athleisure
All of which have different interchange rates and higher ticket sizes.
Lever 4 — Improving campaign targeting
Even if you don’t recommend merchants directly, embeddings help you:
- target cashback campaigns more precisely
- reduce leakage
- increase ROI of category promotions
This is one of the highest‑impact uses of merchant embeddings.

3) Where merchant embeddings create real business value
The value is not in “recommend merchant X.”
It’s in the semantic understanding that powers multiple revenue levers.
High‑impact use cases
- Better customer segmentation (taste‑based, not MCC‑based)
- Personalized category offers (e.g., “Japanese dining” instead of “MCC 5812”)
- Spend‑back campaigns with lower leakage
- Cross‑sell of lifestyle products (travel card, dining card, sports card)
- Merchant deduplication and canonicalization (cleaner analytics → better decisions)
- Fraud detection (semantic similarity helps detect anomalies)
- Customer churn prediction (loss of spend in key merchant clusters)
These are all revenue‑relevant and regulator‑friendly.

4) Why granular merchant categories still matter even if MCC doesn’t change
MCC is too coarse for modern personalization.
Example:
MCC 5812 = all restaurants.
But customer behavior is driven by:
- cuisine
- price level
- dining style
- location
- brand affinity
LLM embeddings capture these dimensions automatically.
This allows:
- more relevant recommendations
- more effective offers
- better customer experience
- higher engagement
Even if interchange is MCC‑based, behavioral uplift is not.

5) A bank‑ready framing that avoids compliance issues
The safest and most effective framing is:
“Personalized insights based on your spending patterns.”
Not:
- “Go to this merchant.”
- “We recommend this shop.”
- “This is a sponsored merchant.”
Instead:
- “You seem to enjoy Japanese dining. Here are similar places people like you visit.”
- “You’ve been shopping at sportswear stores. Here are related categories you might enjoy.”
- “Your top merchants this month are… Here are similar ones.”
This is content personalization, not advertising.

6) A practical, defensible strategy for your bank
- Use LLM embeddings to understand merchant semantics.
- Use them to build taste clusters and customer affinity vectors.
- Use these clusters to power category‑level recommendations, not merchant‑level endorsements.
- Use the insights to improve campaign targeting, activation, cross‑sell, and share‑of‑wallet.
- Keep the UI phrasing customer‑centric and non‑commercial.
This is fully compliant, commercially meaningful, and technically feasible.

If you want, I can map this into a concrete end‑to‑end architecture for Mox Bank specifically, including how to integrate with your segmentation engine and how to keep it audit‑friendly.
