Here’s where data science can actually move the needle — not just explain the drop, but shape the portfolio back toward healthy, regulator‑friendly revolving behaviour.

I’ll give you a structured, Mox‑ready framework that aligns with HKMA expectations and the realities of a digital‑first credit card.

---

🔵 1. Build a Revolver Behavioural Model (Core Engine)

You want a model that predicts:

P(\text{Customer Revolves Next Cycle})


Inputs typically include:

• Spend velocity
• Statement balance trajectory
• Payment behaviour (full / partial / minimum)
• Cashflow patterns (salary inflow, volatility)
• Instalment usage
• Credit line utilisation
• Seasonality (bonus months, tax months)
• App engagement signals


This model becomes the control tower for all downstream actions.

Why this matters

You can:

• Identify customers at risk of leaving the revolver segment
• Identify customers who are safe to revolve (no hardship risk)
• Quantify which levers (UX, comms, instalments) cannibalize revolvers


---

🔵 2. Decompose the Drop Using Attribution Models

You want to quantify how much each factor contributed.

Techniques:

• Cohort decomposition (vintage × revolver rate × avg balance)
• Counterfactual modelling• “What would revolver balance be if instalments stayed at last year’s level?”

• Shapley value attribution• Fairly allocates contribution of each driver (UX change, macro, risk actions)



This gives you a defensible, data‑driven narrative for management.

---

🔵 3. Build a Revolver Early‑Warning System

This is a real‑time classifier that flags customers who are about to:

• Pay full
• Reduce balance
• Convert to instalments
• Stop spending


Signals include:

• Drop in utilisation
• Increase in repayment ratio
• Change in salary inflow
• App behaviour (checking statement more often)
• Merchant category shifts


This lets you intervene before the revolver balance disappears.

---

🔵 4. Identify “Healthy Revolvers” vs “Distressed Revolvers”

HKMA cares deeply about fair treatment.
So you need segmentation that distinguishes:

Healthy revolvers

• Stable income
• Consistent partial payers
• No delinquency signals
• Low hardship risk


Distressed revolvers

• Rising utilisation
• Increasing minimum payments
• Irregular salary inflow
• High BNPL usage


Why this matters:
You can only target the healthy segment for retention strategies.

---

🔵 5. Build a “Revolver Retention” Propensity Model

This predicts:

P(\text{Customer Returns to Revolving After Full Pay})


Useful for:

• Customers who just paid full
• Customers who reduced balance
• Customers who shifted to instalments


You can then design non‑interest‑bearing nudges that encourage natural revolving behaviour (e.g., spend stimulation, category offers).

---

🔵 6. Detect Instalment Cannibalization with Causal Inference

Use:

• Difference‑in‑differences
• Propensity score matching
• Uplift modelling


Goal:

• Quantify how much instalment campaigns reduce revolver balance
• Identify which customer segments are most cannibalized
• Recommend guardrails (e.g., suppress instalment offers for certain cohorts)


This is one of the highest‑impact data science levers.

---

🔵 7. Build a Credit Line Elasticity Model

This estimates:

\Delta \text{Revolver Balance} \text{ per } \Delta \text{Credit Line}


You can simulate:

• What happens if you increase lines for safe revolvers
• What happens if you reduce lines for risky revolvers


This is a powerful lever because line increases often boost:

• Spend
• Utilisation
• Revolver balance


…without increasing delinquency if targeted correctly.

---

🔵 8. Seasonality Adjustment Models

Use:

• Time‑series decomposition
• Fourier seasonality
• Holiday/bonus dummy variables


This helps you:

• Remove seasonal noise
• Identify structural declines
• Forecast revolver balance more accurately


---

🔵 9. Build a “Revolver Recovery” Recommendation Engine

This is a rules‑plus‑ML hybrid that suggests the right action for each customer:

Customer Type	Recommended Action	
Healthy revolver trending to full pay	Spend stimulation, category offers	
High spend but full pay	Credit line increase, merchant‑based incentives	
Instalment cannibalized	Suppress instalment offers temporarily	
Distressed revolver	Hardship support, no retention nudges	


This ensures compliance while improving portfolio yield.

---

🔵 10. Portfolio‑Level Simulation Engine

Finally, build a simulator that answers:

• “If we increase line for 20k customers, what happens to revolver balance?”
• “If we reduce instalment push by 30%, what is the impact?”
• “If macro worsens, how much revolver balance is at risk?”


This becomes your strategic planning tool.

---

🟣 If you want, I can help you build:

• A full data science roadmap for revolver optimization
• A model architecture for each component
• A presentation‑ready deck for management
• A SQL/Python feature blueprint for all models
• A simulation framework for portfolio forecasting


Just tell me which direction you want to go next.