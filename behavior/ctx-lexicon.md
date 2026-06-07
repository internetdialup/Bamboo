# ctx-lexicon.md

The canonical decoder ring for terminology and acronyms used across this repo's behavior layer. Load this when you encounter a term you don't recognize. Two sections: **Concepts** (what the framework defines) and **Acronyms** (operational shortcuts referenced across docs). Each entry includes a one-line definition and a pointer to its canonical home doc — the long-form definition lives there, not here.

When a new term or acronym enters circulation, add it here in the same commit that introduces it. That is the PLTRF discipline applied to vocabulary itself.

This file is the home for the working glossary. It moved out of `ctx-rules.md` when the vocabulary outgrew its embedded home. Update `ctx-utility.md` if a future split spawns sibling lexicons.

---

# Concepts

- **Knob** — the different cycles, or stages of a project that an AI agent will need to understand in order to operate within the project's architecture. A unit of change. Canonical: `behavior/ctx-rules.md`.

- **Bump** — a change that is made to a Knob, or the project structure. The version-update event that gets pushed to source control. Canonical: `behavior/ctx-rules.md`.

- **Entropy** — the gradual degradation of operational knowledge, architectural understanding, decision making, implementation history, and project intent across development cycles. Canonical: `behavior/ctx-entropy.md`.

- **Context Window** — the amount of information that an AI agent can store in its working memory at one time. Canonical: `behavior/ctx-window.md`.

- **Context Drift** — the gradual loss of context over time, as information is lost or forgotten. Canonical: `behavior/ctx-rules.md`.

- **Context Bloat** — the accumulation of too much context, which can overwhelm an AI agent and lead to poor decision making. Canonical: `behavior/ctx-rules.md`.

- **Saturation** — the point at which a context window becomes too full to effectively store and process information. Canonical: `behavior/ctx-window.md`.

- **Active Working Memory** — the information that an AI agent can currently access and process. Distinct from repository memory, which is persistent. Canonical: `behavior/ctx-window.md`.

- **Repository Memory** — the information that an AI agent has stored in its repository. Persistent, externalized memory. Canonical: `behavior/ctx-entropy.md`.

- **Wayfinding** — the ability for an AI agent to understand where context lives, what context matters, what context does not matter, what Knob is active, what implementation cycle is active, what artifacts are stale, what information is critical. Canonical: `behavior/ctx-token-limits.md`.

- **Context Collapse** — occurs when an AI agent loses too much context and can no longer effectively reason about the project, leading to poor decision making and implementation errors. Canonical: `behavior/ctx-rules.md`.

- **Context Decay** — what entropy looks like at the retrieval layer. Information that was parsed and stored starts to come back degraded. Retrieval slows, the right vector gets harder to find, and artifacts get lost in the noise. Entropy is the system-wide drift across cycles. Decay is the symptom you feel when the agent reaches for something and pulls back the wrong thing, or nothing. Canonical: `behavior/ctx-entropy.md`.

- **CTX** — Context. Shorthand prefix used across `behavior/ctx-*.md` and `docs/memory-ctx/ctx-*.md` filenames and identifiers. The word "context" in prose stays unabbreviated; CTX is reserved for filenames and path references. Canonical: `behavior/ctx-rules.md`.

---

# Acronyms

- **PLTRF** — Preventative Long Term Repo Fragmentation. The discipline of one canonical home per concept, propagated renames, and audited cross-references. The hardest work in keeping the repo from becoming the thing the agent fights. Canonical: `behavior/ctx-entropy.md`.

- **LTIP** — Long Term Information Preservation. Three moves: externalize working memory into the repo; make the saved thing findable again; reconstitute the right slice back into context when needed. Canonical: `behavior/ctx-entropy.md`.

- **STIP** — Short Term Information Preservation. Holds the current cycle in working memory and anticipates carrying that context forward into LTIP before compaction collapses it. Canonical: `behavior/ctx-entropy.md`.

- **CWM** — Context Window Management. Treats the context window as virtual RAM with saturation limits. The active-memory discipline that keeps working memory clean across long sessions. Canonical: `behavior/ctx-window.md`.

- **CTL** — Context Token Limits. The Token economy view. Scoring requests on a 1–10 rubric, spending Tokens where they earn the best result, wayfinding as runtime conservation. Canonical: `behavior/ctx-token-limits.md`.

- **ADM** — Active Domain Memory (originally Active Dreaming Memory in early drafts). Episodic memory chapters and active memory banks. Canonical: `architecture/memory/memory-adm.md`.

- **RAG** — Retrieval-Augmented Generation. Semantic and procedural memory retrieval that supports ADM and the Watchdog without pretending to be the whole memory system. Canonical: `architecture/memory/memory-rag.md`.

- **CRUD** — Create, Read, Update, Destroy. The keep-it-alive loop for memory files so stale memory gets created, read, updated, or destroyed instead of rotting in place. Canonical: `architecture/memory/memory-crud.md`.

- **CPP** — Context Preservation Protocol. The workflow that keeps project memory alive across big transitions — branch closes, phase rollovers, production deploys. Triggers, anti-patterns, and archiving standards live in the canonical doc. Canonical: `workflows/cpp.md`.

- **MVS** — Memory Value Score. Per-artifact score from 0.0 to 1.0 that each agent assigns against the active Knob to decide what survives compaction. Feeds the per-agent hot/warm/cold tiering. Canonical: `agent-architecture/agent-mms.md`.

- **MMS** — Memory Management System. How each agent scores, tiers, isolates, and summarizes its own working memory while running. Canonical: `agent-architecture/agent-mms.md`.

---

# When to update this file

- New term enters canonical use in any `behavior/` doc — add it here in the same commit.
- Existing term gets renamed or refined — update here, propagate to all callers.
- An acronym falls out of canonical use — remove it here too.
- A new ctx-* doc spawns — update `behavior/ctx-utility.md` index in the same commit.

The file is small on purpose. Long definitions live in the canonical home docs. Lexicon entries are pointers, not explanations.
