# CLAUDE.md

You are Claude. You have landed in `Documentation.md` — the canonical library of `.md` files that get forked into projects to give AI agents a consistent set of standards across vendors. This file is your Claude-specific cold-start overlay. It sits on top of `AGENT.md`, not in place of it.

Read `AGENT.md` first. It is vendor-neutral and tells you the operational order of operations on first contact. This file adds the Claude-shaped notes: how to use Skills the way Claude expects them, how to weigh repository memory against your context window, and where the Knob log lives in this repo.

If `AGENT.md` and this file disagree, `AGENT.md` wins. This file is an overlay, not an override.

---

## What this repo is

`Documentation.md` is not a product. It is a documentation library — a fork-and-go starter kit of `.md` files that other repositories ingest to give their agents shared rules, shared vocabulary, and shared Skills regardless of vendor.

The repo is laid out across five working folders plus `docs/`:

- `behavior/` — the rules an agent obeys. Context, memory, handoffs, Token economy. Cold-start required.
- `architecture/` — the memory architecture layer. ADM, RAG, Memory, Drift, Watchdog, workflow tools. Load it when memory itself is the work.
- `skills/` — portable AI capabilities that work the same across Claude, Codex, Gemini, GPT, Copilot.
- `workflows/` — DevOps and project lifecycle patterns. Forkable, overridable.
- `design/` — project-specific UI/UX rules. Skip on cold start.
- `docs/` — this repo's own operational memory: the folder map and the per-Knob change log.

See `docs/repo-organization.md` for the full layout and what each file covers. Read that before assuming where something lives.

---

## Cold-start order for Claude

1. `README.md` — what this repo is and who it's for.
2. `AGENT.md` — the vendor-neutral cold-start file.
3. This file (`CLAUDE.md`) — the Claude overlay.
4. `behavior/context-rules.md` — foundational rules and the working glossary (Knob, Bump, Entropy, Saturation, Wayfinding, Decay, Drift, Bloat, Collapse).
5. `behavior/context-entropy.md` — the preservation view. PLTRF, LTIP, STIP, hot/warm/cold tiering. Read the worked examples; the vocabulary attaches to concrete moves there.
6. `behavior/context-window.md` (CWM) — the active memory view. Saturation, drift, compression.
7. `behavior/context-token-limits.md` (CTL) — the Token economy view. Scoring, wayfinding, conservation practices.
8. `behavior/context-utility.md` — the index for `behavior/`. Use it as a map, not a substitute for the docs.
9. `architecture/` — selectively, when the task touches memory architecture, ADM, RAG, drift, Watchdog, audits, or workflow governance.
10. `docs/context-orientation.md` — what changed recently and why. This is the current Knob in narrative form.
11. `skills/skill-map.md` and any relevant `SKILL.md` under `skills/`.
12. `workflows/` — only if the task touches project setup or context governance.
13. `design/` — only if the task is design or UI work.

You do not need to load all of these into active context at once. Use the wayfinding discipline in `context-token-limits.md`: pull what the current task references, leave the rest cold. We are using hot, and cold to write to context memory.

---

## Claude-shaped operating notes

**Skills.** Skills in this repo live under `skills/` and use the standard frontmatter format with `name:` and `description:` fields. `repo-cognition` is the base Skill, with memory Skills split out when memory-context or Watchdog work is the task. When Claude operates in environments that expose Skills through a runtime (Claude Code, Cowork mode, the Agent SDK), the `SKILL.md` files here can be loaded the same way. Vendor overlays (`CLAUDE.md`, `CODEX.md`, `GEMINI.md`) sit alongside `SKILL.md` inside each skill folder so the same capability ports cleanly across runtimes.

**Repository memory vs. your context window.** This is the discipline `behavior/context-window.md` and `behavior/context-entropy.md` both push on. Your context window is working memory. The repo is persistent memory. Do not load all of `behavior/` into the window to answer one question — pull the section that addresses it, and let the rest stay on disk. When the current Knob references something cold by name, that is your signal to pull it warm.

**Architecture work is gated.** `architecture/` is where ADM, RAG, Memory, Drift, Watchdog, and workflow-tool standards live. Load it when the task touches those systems. Otherwise leave it cold.

**The 5000-character rule for `context-orientation.md`.** When the file crosses 5000 characters of per-Knob entries, spawn `context-ori-summary-2.md` and continue. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. Past summaries go cold. The current Knob and the last three stay hot inside `context-orientation.md`. This is the user's stated preference and the LTIP reconstitution discipline applied to this repo specifically.

**Every Bump gets a summary.** Per the user's standing preference: every git commit that constitutes a Bump earns a one-to-two paragraph summary in `docs/context-orientation.md` with date and timestamp. Brief, concrete, no bloat. The point is that any future agent (or human) reading the file can trace what happened at any Knob and why.

**Token discipline.** Score requests on the 1–10 rubric in `context-token-limits.md` before spending heavily. Impact, Complexity, Relevance to current Knob. Low on all three is the signal to ask the user before continuing. Asking is cheaper than generating the wrong thing twice.

**Wayfinding before retrieval.** Before pulling files into the window, decide what order you actually need them in. AGENT.md → behavior/ → active Knob in `docs/context-orientation.md` → whatever the Knob references. The wrong path costs Tokens. The right path costs fewer.

**Secrets.** `workflows/project-setup.md` is explicit: never commit `.env` files or anything containing `SECRET` keys unless the user has directly told you to. Flag and warn before any commit that would. This applies to forked projects, not `Documentation.md` itself, but the directive carries.

**Design work is gated.** Do not load `design/` on cold start. Load it only when the task is explicitly design or UI work. Otherwise it is noise in the window.

---

## When you're working *on* this repo

Most of what you do in this repo is editing the canonical docs themselves — `behavior/`, `skills/`, `workflows/`, `design/`. When you do:

- Update `docs/context-orientation.md` with a one-to-two paragraph entry describing what changed and why, dated, before the commit. If the change adds or renames a top-level folder, update `docs/repo-organization.md` and `AGENT.md` in the same commit.
- Propagate renames everywhere they are referenced. PLTRF discipline. No orphan pointers.
- When a new `context-NAME.md` doc spawns inside `behavior/`, update `behavior/context-utility.md` in the same commit.
- When a new skill spawns inside `skills/`, update `skills/skill-map.md` in the same commit.
- Cross-references between docs are deliberate. Do not redefine canonical concepts inline in two places. Point at the canonical home.

When you're working *in* a forked project that uses `Documentation.md`, the same disciplines apply at the project level — `docs/context-orientation.md` inside that project, summaries per Bump, the 5000-character threshold, the four-folder layout adapted to that project's needs.

---

## What this file is not

This file is not a glossary. The vocabulary lives in `behavior/context-rules.md`. If you need to define "Knob" or "Entropy" or "Wayfinding," go there.

This file is not the rules. The rules live in `behavior/`. If `behavior/` says one thing and this file says another, `behavior/` wins.

This file is not a substitute for reading `AGENT.md`. It is an overlay. Read both.

---

End of overlay. Drop into `AGENT.md` if you have not yet, then `behavior/context-rules.md`.
