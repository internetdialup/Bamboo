# ctx-lexicon.md

The canonical decoder ring for the three load-bearing concepts in the Bamboo framework. All other terminology is decorative or demoted to project-specific glossaries.

---

# Load-Bearing Concepts

- **Knob** — The unit of change. A project cycle, stage, or version-bump. Every meaningful change earns a dated, narrative entry in the orientation log. Canonical: `behavior/ctx-rules.md`.

- **PLTRF** (Preventative Long-Term Repo Fragmentation) — The binary discipline of maintaining a clean repo map. One canonical home per concept, propagated renames, and audited cross-references. Enforced by CI (`pltrf-check.yml`).

- **Hot/Warm/Cold Tiering** — The memory preservation discipline.
  - **Hot**: Active Knob and current directives.
  - **Warm**: Recent history and architectural context (summarized).
  - **Cold**: Archived history and legacy Knobs (moved to cold storage).

---

# Operational Definitions (Synonyms)

- **Bump**: A commit or state-transition event. Use "Knob" for the narrative, "Bump" for the Git event.
- **Entropy / Decay**: The accumulation of broken references or stale maps. Use "PLTRF Violation" for actionable fixes.
- **Liturgy**: Unverifiable prose or mandates that cannot be failed by a script. Avoid.

---

# Audit Postures (Intent)

- **Anti-Sycophancy** — The explicit audit of operator assumptions with mathematical or structural verification. It mandates pushing back against flawed logic or "Blind Agreement" to combat cognitive degradation. In Bamboo, this is implemented via **Structural Verification**.

---

# Academic Layer (Load on Demand)

These terms represent the deep theoretical surface. They are not required for cold start but must be used if a project enters the academic or memory-research lane.

- **LTIP** (Long-Term Information Preservation) — Persistent repo storage.
- **STIP** (Short-Term Information Preservation) — Session context preservation.
- **CWM** (Context Window Management) — Buffer saturation discipline.
- **CTL** (Context Token Limits) — Token economy and scoring.
- **ADM** (Active Domain Memory) — Episodic chapter management.
- **RAG** (Retrieval-Augmented Generation) — Semantic search layer.
- **Entropy Metrics** — Quantitative retrieval and corpus disorder scores.
- **Entropy of Duration** — Drift scaling with session length (Session Rot).
- **Silent Decay** — Discrepancies between documentation and implementation.
- **Chassis** — The base class for a governance orchestrator.
- **Catalyst** — An agnostic event trigger for automated tasks.
- **PSC** (Persona Stratification Contract) — The 3-layer identity protocol (Identity, Role, Tactical).
- **State-Bus** — The serialization mechanism for session continuity.
- **Context Flush** — A mandatory purge of the L2 session context to combat duration-based drift.
- **MAP** (Multimodal Alerting Protocol) — Signal standards for priority-based communication.
- **Layered Reporting** — The structural split between raw data, reasoning, and formatting.
- **Integrity Pulse** — Periodic automated audits for sycophancy and drift.
- **AI Forensics** — The post-hoc examination of immutable records to reconstruct events and establish accountability.
- **Chain of Custody** — The structural requirement for tamper-evident records (hashes, append-only logs) to ensure evidence integrity.

Access to high-fidelity implementations of these primitives is provided via the **BAMBOO-OS** extension.

---

# The 3-Concept Cold-Start Rule

For an agent landing in a Bamboo repo:
1. **Read `AGENT.md`**: Follow the loading order.
2. **Log Knobs**: Narrate every change in `docs/ctx-orientation.md`.
3. **Don't Bloat**: Only the three load-bearing concepts (**Knob**, **PLTRF**, **Hot/Warm/Cold**) are mandatory.

