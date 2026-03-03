You can extract concept vectors from an LLM in a systematic, numerical, non‑textual way — but you need to treat the LLM as a teacher model and convert its internal knowledge into dense vectors that you can reuse, store, and scale. The key is to avoid relying on textual JSON labels directly, and instead force the LLM to express its knowledge in a vectorizable form.
Below is a structured breakdown of the viable approaches, their tradeoffs, and how they fit into your merchant‑feature pipeline.

1. Why direct JSON labels are not enough
Direct LLM labels (e.g., {"is_restaurant": true}) are good for:
- leveraging world knowledge
- handling unseen merchants
- reasoning over ambiguous names
But they are not reusable vectors. They don’t give you:
- a continuous concept axis
- a direction in embedding space
- a projection score
- a scalable inference method
You need a way to numerically distill the LLM’s knowledge into a vector.

2. Three systematic ways to extract concept vectors from an LLM
These are the only practical, scalable, bank‑grade approaches.

🧱 Method 1 — LLM‑generated weak labels → train linear probe → concept vector
This is the most robust and widely used method in industry.
Process:
- Ask the LLM to label merchants for a concept (restaurant, sports, beauty, etc.).
- Use these labels as weak supervision.
- Train a linear classifier on top of your embedding model.
- The classifier’s weight vector becomes the concept direction.
Why this works:
- The LLM provides world knowledge.
- The embedding model provides geometric structure.
- The linear probe extracts a clean, reusable direction.
- You get a stable concept axis that generalizes to new merchants.
This is the closest thing to “extracting a concept vector from the LLM.”

🧭 Method 2 — LLM‑generated synthetic examples → embed → average → concept vector
This method uses the LLM to generate examples, not labels.
Process:
- Ask the LLM:
“Give me 20 examples of Hong Kong restaurants.”
- Embed all examples.
- Compute the mean embedding.
- Normalize → this is your restaurant concept vector.
Advantages:
- Uses LLM’s internal knowledge of brands, cuisines, categories.
- Produces a clean, interpretable direction.
- No need for labeled merchant data.
Limitations:
- Depends on LLM’s ability to generate good examples.
- May miss local HK‑specific merchants unless prompted carefully.

🧪 Method 3 — LLM‑generated pairwise comparisons → difference vectors → PCA
This is more advanced but very powerful.
Process:
- Ask the LLM to produce positive vs negative pairs:
- “Give me 10 restaurants and 10 non‑restaurants.”
- Embed all merchants.
- Compute difference vectors:
v_i=x_{\mathrm{positive}}-x_{\mathrm{negative}}- Run PCA or average the difference vectors.
- Normalize → concept direction.
Why this works:
- Difference vectors isolate the semantic dimension.
- PCA removes noise.
- You get a clean axis even for fuzzy concepts.

3. Why you cannot directly extract the LLM’s internal vector
LLMs do not expose their internal embedding space.
You cannot ask:
“Give me the internal vector for the concept ‘restaurant’.”

But you can force the LLM to express its knowledge through:
- labels
- examples
- comparisons
- synthetic data
Then you convert that into a vector using your embedding model.
This is the standard technique in knowledge distillation and representation learning.
