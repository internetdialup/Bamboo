# Memory Entropy Metrics

This is the measurement architecture for Context Entropy. `behavior/ctx-entropy.md` defines what entropy *is* and the preservation discipline (PLTRF, LTIP, STIP) around it. This doc defines how to *measure* it so a system can act on the number instead of acting on a feeling.

Lives under `architecture/memory/` because it is systems-level architecture — embeddings, indices, similarity thresholds — not a behavior rule. A markdown file does not run a softmax. The indexing layer does. Keep the definition here and the computation there.

---

## Computing Entropy

Entropy has been a word up to this point. A direction, not a number. If it is going to trigger anything automatically, like a compression sweep, it has to be measured. The trap is measuring it the easy wrong way. Multiply volume by duplication by age and you get a number that grows with the size of the repo and means nothing. A real entropy measure does not grow just because the repo got bigger. It measures disorder in a distribution, normalized, so a fifty file repo and a two thousand file repo land on the same scale and can actually be compared. Size is volume. Entropy is how tangled the volume is.

There are two places worth measuring it, and they do different jobs.

### Retrieval Entropy

This is the one that improves retrieval directly, because it tells the agent when its own retrieval cannot be trusted, before it answers.

When the agent retrieves for a query it gets back a set of candidates with similarity scores. Turn those scores into a distribution, softmax over the top k, and take the entropy of that distribution. Normalize by the log of k so it lands between zero and one. A peaked distribution, one candidate far above the rest, is low entropy. The retriever found a clear answer. A flat distribution, ten candidates all scoring about the same, is high entropy. The retriever cannot tell the documents apart, and that is the exact moment retrieval turns into noise.

Low retrieval entropy, proceed. High retrieval entropy is the signal to widen the net, dedupe the region, or warn the user before the agent blends a muddy retrieval into a confident answer. This is the same alarm as the conflict detection in `memory-compression.md` (planned), coming from a different angle. Conflict detection asks whether the retrieved docs disagree. Retrieval entropy asks whether the retriever could even pick between them. When both fire on the same query you are looking at a topic that has rotted.

### Corpus Entropy

This is the health number. The one that crosses a threshold and triggers a sweep.

Embed the chunks of the repo and measure how much of the corpus is a near duplicate of itself. For each chunk find its nearest neighbor. If that neighbor sits above a high similarity threshold, the chunk is redundant. The fraction of the corpus that is redundant, weighted by how tightly it clusters, is the corpus entropy. A repo where every concept has one clean home scores low. A repo where auth is described four slightly different ways across four files scores high, because the retrieval probability mass for any auth query gets split across near copies, and the conflicting versions all surface together.

That is the disorder this framework has been describing, finally as a number. When it crosses the project threshold, the compression pass fires, scores the docs, dedupes the redundant cluster, and re-tiers. Garbage collection, triggered by a measurement instead of a feeling. The threshold is a project level dial. A small SaaS tolerates more tangle before a sweep earns its cost than a large monolith does.

---

## Where the Number Lives

Both of these need embeddings and a retrieval index to compute. This doc defines what they measure and why. It does not compute them. A markdown file does not run a softmax. The indexing layer does, and the implementation belongs with the algorithm work, not the behavior doc. Keep the definition here and the computation there — same split this framework keeps everywhere else.

One honest note on why this earns its place. The degradation this framework calls Context Decay is the same thing the long context research measures as context rot, where retrieval quality falls as the corpus grows and the right chunk competes against more and more noise. Corpus entropy is a lightweight proxy for that. Something you can compute on your own repo without running a full benchmark. It is not the whole story. It is a cheap early warning, and a cheap early warning is the entire point of measuring entropy before it collapses into decay.

---

## Cross-references

- `behavior/ctx-entropy.md` — the preservation view this doc serves. Entropy as direction.
- `architecture/memory/memory-watchdog.md` — what consumes the entropy number and acts on it.
- `architecture/memory/memory-rag.md` — the retrieval layer the metrics observe.
- `behavior/ctx-lexicon.md` — Entropy + Decay glossary entries.
