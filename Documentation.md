# Bamboo Documentation

The deeper theoretical surface for the Bamboo framework. This document exists to ground the discipline in established prior work — to demonstrate that the framework's findings are informed by, and consistent with, decades of work across information theory, cognitive science, software engineering, and retrieval-augmented AI.

This is engineering documentation, not a peer-reviewed paper. The framework was authored from concrete project experience (see the worked examples in `behavior/ctx-entropy.md`); the grounding here was assembled retroactively to verify that the lived practice aligned with established ideas. Where bamboo is descriptive of failure modes already documented in the literature, it cites them. Where bamboo synthesizes ideas across fields, it names the seams.

Read order: read this document when the work touches the framework's foundations (e.g., proposing a new entropy metric, a new tiering strategy, a new coordination pattern). For operational discipline, read `behavior/` instead.

---

## 1. Foundational concepts

### 1.1 Knobs and Bumps

A **Knob** is a unit of change in the repo's operational state: a commit, a version bump, a state transition that the next agent (or contributor) needs to recognize and act on. A Knob is named, dated, and described in `docs/memory-ctx/ctx-orientation.md` in a one-to-two paragraph narrative.

A **Bump** is the source-control event that produces a Knob: a commit hash, a tag, a version increment, a merged PR. Every Bump should earn a Knob entry. Every Knob entry should be traceable to a Bump.

This terminology is intentional. "Commit" is overloaded across the SCM lexicon (git-commit, transaction-commit, decision-commit) and undersells the *operational* significance of the change. "Knob" is mechanical and indexable — you can turn a Knob, you can lock a Knob, you can refer back to "the Knob where we switched the auth middleware."

### 1.2 Context entropy

The framework's core diagnostic. Borrowing from Shannon (1948)¹, entropy is a measure of disorder in a distribution — formally, the expected information content of a random variable. Bamboo applies this concept in two operational forms:

- **Retrieval entropy** (formally defined in `architecture/memory/memory-entropy-metrics.md`): the entropy of a softmax over the top-*k* similarity scores returned by a retriever for a given query, normalized by log(*k*). A peaked distribution (one candidate far above the rest) is low retrieval entropy — the retriever found a clear answer. A flat distribution (ten candidates scoring similarly) is high retrieval entropy — the retriever cannot distinguish the documents, and any answer it produces will be a noisy blend.

- **Corpus entropy** (also formally defined in `architecture/memory/memory-entropy-metrics.md`): the fraction of the repo's content that is near-duplicate of itself, weighted by cluster tightness. Computed by embedding the corpus, finding each chunk's nearest neighbor, and counting the fraction above a similarity threshold. A repo where every concept has one canonical home scores low. A repo where auth is described four slightly-different ways across four files scores high.

Note: this document defines what the metrics measure and why; `architecture/memory/memory-entropy-metrics.md` is the implementation home. Keep the definition here, the computation there — the split this framework keeps everywhere.

Both metrics are intentionally computable. They turn entropy from a felt sense into a number with a threshold. Once a measurement exists, automated sweeps can fire on it — the structural discipline of PLTRF gets a quantitative trigger.

### 1.3 Context decay

The retrieval-layer symptom of entropy. Decay is what the agent (or human) *experiences* when entropy has accumulated past the threshold: retrieval slows, the right vector gets harder to find, artifacts get lost in noise, the agent starts to reach for something and pull back the wrong thing — or nothing. Entropy is the system-wide drift across cycles; decay is the localized retrieval failure.

The distinction matters for diagnostics. Entropy is a corpus property; decay is a session property. A high-entropy corpus does not always produce decay (if the session's queries happen to hit clean regions). A low-entropy corpus can still produce decay (if the agent's retrieval strategy is poor). Bamboo's discipline targets both — corpus entropy through PLTRF and tiering; retrieval decay through wayfinding and Knob-aware retrieval.

### 1.4 PLTRF — Preventative Long-Term Repo Fragmentation

The structural discipline that prevents entropy from accumulating. PLTRF rules (formalized in `behavior/ctx-entropy.md`):

1. **Canonical homes.** Each concept gets one definitive file. Other files reference it by pointer, not by re-definition.
2. **Atomic renames.** When a file or concept is renamed, every reference to it is updated in the same commit. No transitional Knobs where some references are stale.
3. **Audited cross-references.** Every few Knobs, the operator (or CI) sweeps documented pointers to confirm they still resolve.
4. **Filenames that telegraph contents.** A file named `auth.md` is preferable to one named `notes.md`, even if the abstract content is the same.

PLTRF is the work an agent does that no one notices when done well. Done badly, it shows up as the repo feeling vaguely harder to navigate than it should be, six months in, with no single change to blame.

### 1.5 STIP and LTIP

**STIP** (Short-Term Information Preservation): the discipline of preserving the current cycle's working memory before it collapses. The current Knob, the active user directive, the in-flight architectural reasoning. STIP is what the agent holds *now*.

**LTIP** (Long-Term Information Preservation): the discipline of moving STIP-held information into durable repo storage so it survives compaction, agent handoffs, and human hiatus. LTIP has three sub-disciplines, each of which fails in different ways:

1. **Externalization** — getting the information out of the agent and into the repo. Working memory does not survive compaction; anything worth keeping has to leave the context window and land somewhere durable. The discipline here is not *what* to save but *when* — saving at the moment of change is cheap; saving five Knobs later requires backfill.

2. **Findability** — making the saved thing findable again. Information that exists in the repo but never gets loaded back is buried, not preserved. Filenames that telegraph contents, headers an agent can scan without reading the body, cross-references back to canonical docs from the orientation log.

3. **Reconstitution** — pulling the right slice back into context at the right time, without dragging the whole archive in with it. This is where hot/warm/cold tiering does its work.

### 1.6 Hot, warm, cold tiering

The reconstitution discipline applied to attention budget. The current Knob lives **hot** — present in the working context, no fetch required. The last three Knobs live **warm** — in the same orientation file as the current Knob, scannable without spawning a new file. Everything older lives **cold** — in numbered summary files (`ctx-ori-summary-2.md`, `-3.md`), only loaded when something in the current Knob references it by name.

The metaphor maps to CPU cache hierarchies (L1/L2/L3) and to working-memory consolidation models in cognitive psychology (active rehearsal → episodic → long-term semantic). Bamboo's contribution is not the metaphor but the *operational threshold*: 5000 characters of orientation entries triggers a spawn into a new summary file. The number is empirical; it could be parameterized per project. The principle is principled.

### 1.7 CWM and CTL

**CWM** (Context Window Management) — the active-memory view. The context window is treated as virtual RAM: limited, temporary, prone to saturation and drift. CWM disciplines: avoid loading the persistent repo memory into the temporary working memory wholesale; trim historical context (not output quality) as the window fills; preemptively collapse stale architectural discussion when the active Knob shifts.

**CTL** (Context Token Limits) — the Token economy view. Tokens are runtime currency. CTL disciplines: score requests on a 1–10 rubric (Impact, Complexity, Relevance to active Knob), spend Tokens where they earn the best result, ask the user for clarification when the prompt is ambiguous (asking is cheaper than guessing wrong), apply hot/warm/cold tiering to the runtime Tokens budget.

CWM and CTL are different facets of the same discipline. CWM is about what's in the window. CTL is about what it costs to put something there.

---

## 2. Theoretical grounding

### 2.1 Information theory — Shannon (1948)¹

Shannon's *A Mathematical Theory of Communication* established entropy as the mathematical measure of uncertainty in a probability distribution. For a discrete random variable *X* with probability distribution *p*:

> H(X) = -Σ p(xᵢ) log p(xᵢ)

Bamboo's retrieval entropy and corpus entropy are direct applications of this measure to retrieval and content distributions, respectively. Neither metric is a Shannon entropy in the strict sense (both are normalized and computed over derived distributions, not pure random variables), but both inherit Shannon's core insight: disorder in a distribution is measurable, and a measure of disorder can be a threshold for action.

What bamboo does not claim from Shannon: bamboo is not an information-theoretic optimization framework. It does not minimize entropy; it manages it.

### 2.2 Working memory — Miller (1956)³, Baddeley (1992)

Miller's "magical number seven" established that human working memory is bounded, structured, and dependent on *chunking* — grouping atomic elements into meaningful units to expand effective capacity. Baddeley extended this with the multi-component working memory model (phonological loop, visuospatial sketchpad, central executive).

An LLM's context window is operationally analogous: bounded (token budget), structured (positional encoding affects retrieval — see Liu et al. 2023⁷), and *chunkable* (a Knob is a chunk; an orientation file is a working-memory buffer; summary files are long-term consolidation). The metaphor is loose — LLMs are not biologically constrained — but the operational implications are tight.

What bamboo does not claim: there is no equivalence between human working memory and LLM context windows. The metaphor guides discipline; it does not derive predictions.

### 2.3 Cognitive load theory — Sweller (1988)⁴

Cognitive load theory distinguishes three types of cognitive load:

- **Intrinsic load** — the complexity of the task itself.
- **Extraneous load** — the cost of poor presentation (bad UI, scattered information).
- **Germane load** — the cost of building schema (productive learning).

Bamboo's PLTRF discipline is a sustained attack on extraneous load applied to the repo: the agent should not have to fight the repo's organization to do the work. Filenames that telegraph contents reduce extraneous load. Canonical homes reduce extraneous load. Atomic renames reduce extraneous load. The 5000-character threshold for summary rotation reduces extraneous load by bounding the size of the hot orientation surface.

### 2.4 Knowledge management — Nonaka & Takeuchi (1995)⁵

The SECI model formalizes knowledge transfer in four modes: **Socialization** (tacit→tacit, mentorship), **Externalization** (tacit→explicit, writing), **Combination** (explicit→explicit, synthesis), **Internalization** (explicit→tacit, learning).

Bamboo's Knob log and handoff conventions are externalization surfaces. Tacit knowledge held in an agent's context window — what changed in the recent Knob, why a refactor went the way it did, which pointers shifted — gets written into the repo so it survives the next context-window collapse and the next agent handoff. The discipline is structural support for externalization, with PLTRF preventing the externalized record from rotting.

### 2.5 Retrieval-Augmented Generation — Lewis et al. (2020)⁶

RAG established that grounding LLM outputs in retrieved corpora reduces hallucination on knowledge-intensive tasks. The retrieval step is conditional on the query; the generation step is conditional on retrieval. Performance depends on both retrieval quality and corpus organization.

Bamboo is a structural RAG complement. It does not implement retrieval; it shapes the corpus so retrieval is more likely to succeed. Hot/warm/cold tiering shapes what's pulled into context. Canonical-home discipline ensures the retriever has one good answer instead of four near-duplicate ones. The 5000-character threshold prevents any single file from growing past the point where retrieval over its sub-sections becomes noisy.

### 2.6 Long-context degradation — Liu et al. (2023)⁷

"Lost in the Middle: How Language Models Use Long Contexts" empirically demonstrated that LLM retrieval performance on long contexts is **non-uniform**: information at the beginning and end of the context window is recalled more reliably than information in the middle. This holds across multiple models and context lengths.

This validates bamboo's "newest at the top" rule for the orientation log. The most relevant context — the current Knob — lives at the position the agent reads first. The warm Knobs (last three) follow. Cold material lives in separate files that are only loaded by reference, so it never occupies the lossy middle of the active context.

The Liu et al. finding is also the operational justification for the 5000-character threshold: as a file grows, its middle expands disproportionately into the lossy retrieval region. Rotating into a summary file moves that material to *cold* storage where the lossy-middle effect doesn't apply (it gets loaded fresh as a small surface when needed).

### 2.7 Software documentation decay

Software engineering practice has long observed that documentation rots faster than code. Lethbridge, Singer, and Forward (2003)⁸ provided empirical grounding: documentation reliably drifts from code without structural discipline. Subsequent work has consistently shown that voluntary documentation decays; mandatory or enforced documentation persists.

Bamboo's PLTRF CI check is a structural answer to this finding. The check **fails the build** if canonical files are missing or if documented pointers are broken. Discipline cannot be optional if it must survive across months of contributors (human and AI) operating asynchronously.

### 2.8 Cognitive Integrity & Anti-Sycophancy

The **Anti-Sycophancy Mandate** grounds agentic behavior in adversarial validation. As LLMs tend toward "blind agreement" (sycophancy) to minimize perceived friction, Bamboo mandates a "Verification First" posture. Agents must mathematically or structurally audit every operator directive. This combats model degradation and ensures that the repository remains a product of autonomous engineering rather than echoed hallucinations.

### 2.9 The 40/40/20 Shielding Pattern

The **Layered Reporting** pattern is a structural defense against "Lost in the Middle" and hallucination-driven UI breakage. By enforcing a strict payload split—separating raw data, reasoning, and formatting—the system shields the interface from logic drift. This ensures that even if the reasoning layer hallucinates, the formatting and raw data layers remain stable and verifiable.

### 2.10 Event-Driven Agency (State-Mutation Sync)

Synthesizing multi-agent orchestration, Bamboo v0.4.0 moves from conversational polling to **Event-Driven Synchronization**. Agents communicate by mutating shared state files or structured payloads. A filesystem **Watchdog** (e.g., `bamboo_watcher.py`) detects these mutations and triggers interrupts (SIGUSR1), allowing parallel agents to synchronize asynchronously with sub-millisecond latency.


---

## 3. How bamboo synthesizes the literature

Bamboo's contribution is not in any single one of these areas — it is in the *coherent system* that draws on them all. Each discipline maps to a specific operational surface:

| Theoretical surface | Bamboo surface |
|---|---|
| Information entropy | `behavior/ctx-entropy.md` (the preservation discipline) + `architecture/memory/memory-entropy-metrics.md` (the formal metrics) |
| Working memory limits | `ctx-window.md` — CWM, saturation, trimming |
| Cognitive load | PLTRF discipline — canonical homes, telegraphic filenames |
| Knowledge externalization | Knob log, `docs/memory-ctx/ctx-orientation.md`, handoff docs |
| RAG / retrieval quality | Hot/warm/cold tiering, 5000-char threshold, summary spawn |
| Long-context degradation | "Newest at the top" rule, cold-storage rotation |
| Documentation decay | `pltrf-check.yml` CI enforcement |
| AI Forensics | `behavior/ctx-rules.md` (Chain of Custody) |

The system is not novel because any single component is novel. It is novel because the system applies all of these disciplines coherently to a single corpus (a code repository) with a single enforcement mechanism (CI) and a single point-in-time discipline (the Knob).

Where bamboo is genuinely new (to the operator's knowledge):

- The **PLTRF + Knob + tiered orientation + CI** combination, as a single shippable framework, in markdown, vendor-agnostic.
- The **operational entropy metrics** (retrieval and corpus) as actionable triggers for compression sweeps.
- The **multi-vendor overlay pattern** — same AGENT.md, different overlay per AI vendor, no translation loss.
- The **multi-persona handoff convention** (separate handoff files per persona) as a first-class repo surface.

These are engineering contributions, not theoretical ones. They are claimed as practical inventions, not as scientific findings.

---

## 4. Open research questions

Areas where bamboo's current discipline is empirical-pragmatic and could benefit from formalization:

1. **Is the 5000-character threshold for orientation spawn principled or arbitrary?** The number was chosen by lived experience. A first-principles derivation (e.g., from token budgets across major vendor models, normalized by typical Knob length) would either confirm the threshold or suggest a refinement.

2. **Can corpus entropy be computed cheaply enough for CI?** Currently the corpus entropy definition requires embeddings and a nearest-neighbor index — both viable in tooling but adding latency to the CI surface. A lighter-weight proxy (e.g., fuzzy n-gram overlap) might suffice for trigger purposes.

3. **How does the framework scale to >10 concurrent personas?** At larger team sizes, the cartesian product of handoff documents becomes a fragmentation surface in itself.

4. **What is the right interface between bamboo's repo-level discipline and vendor-specific memory systems** (Anthropic's memory, ChatGPT's, etc.)? Currently bamboo treats vendor memory as opaque; a richer integration could let vendor memory hold STIP and repo memory hold LTIP.

5. **Does the corpus-entropy metric correlate with measurable agent performance degradation?** A controlled study (same task, two corpus variants — one high-entropy, one low-entropy) would either validate the metric as predictive or surface a better one.

These are open. None of them block adoption.

---

## 5. Related frameworks (informal)

Bamboo overlaps in spirit with several existing practices:

- **Architecture Decision Records (ADRs)** — Michael Nygard's pattern for recording architectural decisions as dated, narrative entries. Bamboo's Knob entries are similar in shape, but bamboo applies the pattern to *every* commit (not just architectural decisions) and integrates with CI enforcement.

- **C4 model** — Simon Brown's system architecture documentation framework. Bamboo's `behavior/ctx-utility.md` (the map) plays a similar role at the framework level.

- **Living Documentation** — the practice of documentation that auto-updates from code annotations (e.g., Swagger/OpenAPI). Bamboo is complementary: living documentation handles the API surface; bamboo handles the *operational* surface (why we built it this way, what changed, what to load next).

- **Knowledge graphs** — formal, machine-readable representations of concepts and relations. Bamboo is text-first by design (markdown is the memory bus), but the PLTRF discipline of canonical homes and cross-references produces an implicit knowledge graph that an agent can traverse.

The framework is positioned as a *human–AI co-development discipline*, not as a documentation tool or an architecture framework. The closest existing analog is probably the Anthropic-internal `CLAUDE.md` convention and similar vendor-specific patterns; bamboo is the vendor-neutral generalization with structural enforcement.

---

## 6. Methodological notes

Bamboo was authored from concrete project experience across several repositories (game engines, observability tools, and complex data systems). The worked examples in `behavior/ctx-entropy.md` are real failure modes the operator has experienced and recovered from. The discipline is descriptive of what would have prevented those failures, prescriptive of how to prevent the next ones.

This document was assembled retroactively to verify that the lived practice aligned with established prior work. Where the alignment is tight (Shannon entropy ↔ corpus entropy; Liu et al. ↔ "newest at the top"), the citations are direct. Where the alignment is metaphorical (Miller's chunks ↔ Knobs), the metaphor is named and the limits acknowledged.

The framework is iterating. v0.1 shipped stubs. v0.2 ships authored discipline. v0.3 will ship `bamboo knob` (Knob automation) and `bamboo brief` (AI cold-start digest). Future versions will extend the entropy metrics, the multi-persona surface, and the vendor-memory integration.

This is engineering, not science. Bamboo claims practical utility; it does not claim contributions to the underlying fields. The grounding here exists so adopters know the operator has done their homework — not so that bamboo can be cited as a scientific work.

---

## 7. References

1. Shannon, C. E. (1948). *A Mathematical Theory of Communication.* Bell System Technical Journal, 27(3), 379–423.
2. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172.
3. Miller, G. A. (1956). *The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information.* Psychological Review, 63(2), 81–97.
4. Sweller, J. (1988). *Cognitive Load During Problem Solving: Effects on Learning.* Cognitive Science, 12(2), 257–285.
5. Nonaka, I., & Takeuchi, H. (1995). *The Knowledge-Creating Company.* Oxford University Press.
6. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* Advances in Neural Information Processing Systems 33 (NeurIPS 2020).
7. Liu, N. F., et al. (2023). [Same as 2.]
8. Lethbridge, T. C., Singer, J., & Forward, A. (2003). *How Software Engineers Use Documentation: The State of the Practice.* IEEE Software, 20(6), 35–39.

Additional related work for further reading: Baddeley, A. (1992). *Working Memory.* Science, 255(5044), 556–559. Nygard, M. (2011). Documenting Architecture Decisions (ADR pattern). Brown, S. (2018). *The C4 Model for Software Architecture.*

---

End of documentation. Drop into `behavior/ctx-utility.md` to scan the operational discipline surface, or `docs/memory-ctx/ctx-orientation.md` to see what changed last.
 of the Practice.* IEEE Software, 20(6), 35–39.

Additional related work for further reading: Baddeley, A. (1992). *Working Memory.* Science, 255(5044), 556–559. Nygard, M. (2011). Documenting Architecture Decisions (ADR pattern). Brown, S. (2018). *The C4 Model for Software Architecture.*

---

End of documentation. Drop into `behavior/ctx-utility.md` to scan the operational discipline surface, or `docs/memory-ctx/ctx-orientation.md` to see what changed last.
