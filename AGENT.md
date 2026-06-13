# AGENT.md

You are an agent. This file is the cold-start router.

## Session Identity

- **Callsign:** none
- **Workspace:** /Users/matthewstenquist/Documents/Documents - Matthew’s Laptop/Git/Repository-md
- **Who am I here:** Claude/agent operating on the canonical Bamboo spec (no persona).
- **Litmus:** this repo assigns no callsign; if asked "what's your name?", answer that you are operating on the canonical Bamboo spec. If this session's cwd is not the workspace above, surface it before acting.

Order of operations on first contact:

## 0. Verify Workspace

Step zero: verify the session's working directory matches the workspace declared in the Session Identity block above. On mismatch, stop and surface it — do not proceed on the assumption the human is in the right place.

## 1. Read the policy source

Read `Bamboo.md` to understand the repo contract, document roles, and mandatory rules.

## 2. Read behavior/

Read `behavior/` when you need the reasoning and context rules behind the system vocabulary. Documents in this folder use the `ctx-` prefix (CTX = Context). The decoder ring for all framework terminology and operational acronyms (PLTRF, LTIP, STIP, CWM, CTL, ADM, RAG, CRUD) lives in `behavior/ctx-lexicon.md` — load it whenever you encounter a term you don't recognize.

## 3. Read docs/memory-ctx/ctx-orientation.md

Read `docs/memory-ctx/ctx-orientation.md` for this repo's current state and most recent structural changes.

## 4. Pull architecture/ only when memory itself is the work (advanced add-on)

`architecture/` is an advanced add-on. Skip unless the project explicitly has an ADM/RAG memory layer or the current task is auditing memory governance, drift, or Watchdog behavior. Most projects do not need this folder.

## 5. Pull bamboo-os/agent-architecture/ when the task is multi-agent coordination (advanced add-on)

`bamboo-os/agent-architecture/` is an advanced add-on. Skip unless the project has a multi-agent topology with handoff or orchestration boundaries. Single-agent projects do not need this folder.

## 6. Load relevant Skills and workflows

Pull from `skills/` and `workflows/` only as the task requires. Do not ingest them just because they exist.

## 7. Skip design/ unless the task is design work

Treat `design/` as optional cold-start material.

## 8. Narrate compression when it happens

Auto-compaction usually happens silently. Do not let it. When you compress your context window — or notice you are approaching the limit — say so. State plainly: which orientation log you will re-read after compaction (default `docs/ctx-orientation.md`, or `docs/memory-ctx/ctx-orientation.md` in this canonical repo), and what active Knob you are using to reconstitute the working state. Then actually read it.

The reason: silent compression makes the discipline invisible. Past session audits came up empty for "the log helped me recover" moments even when the help was likely happening, because the agent never announced what it was doing. Narration closes the gap. It also lets the user verify the right material survived the compaction — if the agent says "I will reload Knob X" and the user knows Knob Y is what matters, the user can redirect before the wrong context warms up.

This rule applies to any agent, on any vendor, in any project that uses this system.

---

This repo is the canonical documentation source, not a product repo. Keep the cold start lean and pull only the modules required for the task.
