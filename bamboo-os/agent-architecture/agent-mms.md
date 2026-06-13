# Agent Memory Management System (MMS)

`agent-mms.md` defines how each agent in the squad scores, tiers, isolates, and summarizes its own working memory while running. Where `agent-identity.md` says *who the agent is* and `agent-topology.md` says *how the squad coordinates*, this doc says *how each individual agent keeps its own memory from rotting mid-session*.

This file pairs with the Watchdog (`architecture/memory/memory-watchdog.md`). MMS is what each agent runs internally on its own context. The Watchdog is what audits across agents through the repo memory layer. Different layers, one shared discipline.

---

## Memory Value Scores (MVS)

Every artifact an agent holds in working memory gets a Memory Value Score from 0.0 to 1.0. The score answers one question: *if I have to free up context window space, would losing this hurt the active Knob?*

- **1.0** — active Knob, current user directive, current task. Never compress.
- **0.7–0.9** — last three Knobs, current architectural state, active handoff context. Compress only at the hard limit.
- **0.4–0.6** — operational context (last 1–4 weeks of decisions). Summarize on compaction, archive the source to the repo.
- **0.1–0.3** — historical context, completed Knobs, finished features. Trim freely.
- **0.0** — duplicate retrieval, stale architectural debate, off-Knob noise. Drop on next sweep.

MVS is not stored as a separate value. It is a running judgment the agent makes against the current Knob. The score updates whenever the agent retrieves, generates, or summarizes. Scoring stays cheap so the discipline survives sustained development cycles.

---

## Hot / Cold Agent Memory Tiering

MVS feeds the same hot / warm / cold tiering described in `ctx-entropy.md` (LTIP reconstitution discipline) and `ctx-window.md` (CWM compression rules), applied at the per-agent level instead of the repo level.

- **Hot** — MVS ≥ 0.7. Stays in active context. Never compressed without an explicit flag from the user or Watchdog.
- **Warm** — MVS 0.4–0.6. Compressed into summary form inside the working memory. Pullable on reference.
- **Cold** — MVS < 0.4. Archived to repo memory (Knob log, summary files). Reloaded only when the active Knob names it.

When the agent compresses — whether by auto-compaction or because it noticed saturation per the `ctx-window.md` rules — the tiering decides what survives. Per the narrate-compression rule in `AGENT.md`, the agent announces what it is doing, including which Knob it will reconstitute from and what tier of cold material it intends to pull back into context.

---

## Watchdog Interaction

Each agent's MMS runs inside the agent. The Watchdog runs across agents. They communicate via the repo memory layer, not directly with each other.

- The agent posts its current Knob, active MVS scores, and any summarization or compaction event to its handoff log.
- The Watchdog reads handoff logs, audits cross-agent memory for duplicate work, conflicting summaries, stale references, and drift.
- If the Watchdog flags rot, the affected agent re-tiers, re-summarizes, or escalates to the user.
- The Watchdog never directly mutates an agent's working memory. It mutates the repo, and the agent reloads from the repo on the next pass.

This keeps the Watchdog's aggression float (0.0–1.0, defined in the Watchdog persona doc) operating on persistent memory only. Agents stay sovereign over their own working memory until handoff. That sovereignty is what prevents the Watchdog from becoming a bottleneck or a corrupting influence.

---

## Parallel-Agent Memory Isolation

When multiple agents run concurrently (per `agent-topology.md`'s ownership boundaries), each maintains its own MMS state. No agent reads another agent's working memory directly.

- Each agent gets its own Knob log section or handoff file inside the repo.
- Agents read the *repo* version of another agent's state, not the live working memory.
- When two agents touch a shared surface, the primary owner publishes the interface change to the repo before the secondary agent continues.
- This is the same anti-conflict rule from `agent-topology.md`, applied at the memory layer.

Isolation prevents one agent's drift from contaminating another's working set. The Watchdog catches cross-agent inconsistencies via the repo layer; agents do not directly cross-check each other mid-session. Cross-checking through persistent memory is slower but cleaner — and it scales to N agents without N² coordination overhead.

---

## Summarization Triggers

The agent runs summarization on three signals:

1. **Knob transition** — a Bump landed. Summarize the closing Knob into the orientation log before opening the next one.
2. **Compaction event** — context window approaching the limit. Per `AGENT.md` section 8, narrate the event, summarize warm material into cold storage, reload the active Knob from the orientation log.
3. **Handoff** — work passes to another agent (or back to the user). Summarize the active Knob, post the handoff log, identify open questions and what the next owner is expected to do.

Summarization always preserves the current Knob's narrative and cross-references. It compresses warm material, not hot material. If the summarization is going to drop information the agent thinks the next owner needs, the agent escalates to the user before publishing. Asking is cheaper than losing the wrong thing.

---

## Conclusion

MMS gives each agent its own memory discipline. The Watchdog gives the squad cross-agent auditing. ADM, RAG, and CRUD (`architecture/memory/`) give the repo the systems-level memory model that MMS posts into. Identity (`agent-identity.md`) shapes how the agent behaves inside a lane. Topology (`agent-topology.md`) shapes how lanes coordinate. MMS shapes how each agent keeps its own memory honest while doing the work.

All four files share vocabulary on purpose. Read them in the order: identity, topology, MMS, watchdog. That sequence walks an agent from *who am I* to *how do I coordinate* to *how do I think* to *what watches over me*.
