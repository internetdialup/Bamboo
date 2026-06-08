# Bamboo

Your Multi-Agent Orchestrator for AI Governance in AI-assisted repos, and projects.

## Fork in 5 Minutes

If you want to use this in your own project, the easy path is the **Use this template** button at the top of the repo. Gives you a fresh repo with the structure already in place; no upstream commit history to clean up. Then trim what you don't need using the skip list below. If you'd rather slot Bamboo into an existing project, copy the files in manually instead.

**Whichever path you take, you'll want these into your project root:**

- `AGENT.md` — the cold-start router. Every agent that lands in your project reads this first.
- `Bamboo.md` — the policy layer. Recommended if you want the full contract; safe to skip if your project is small and you'd rather keep it lean.
- The behavior stack: `behavior/ctx-rules.md`, `ctx-lexicon.md`, `ctx-entropy.md`, `ctx-window.md`, `ctx-token-limits.md`, `ctx-utility.md`. These are the rules and the decoder ring. The set is small — copy them together as a unit.
- `docs/ctx-orientation.md` — your Knob log. This is the one file your agents (and future-you) will live in. Seed it with one entry: what the project is, when you forked, why.

**Skip these unless you actually need them:**

- `architecture/` and `agent-architecture/` are advanced add-ons. If your project doesn't have an ADM/RAG memory layer or a multi-agent setup, leave them alone. Most projects don't need either.
- `design/` is for projects that own UI or UX standards.
- `skills/` is for vendor-portable capability docs. Pick the ones you'll actually use; leave the rest.
- `CLAUDE.md`, `CODEX.md`, `GEMINI.md` are vendor overlays — only copy the one for the agent you're running. If you're running more than one, copy more than one. Easy.

**Then make two edits:**

1. Open `AGENT.md` and rewrite the top to describe your project. Keep it short — 2 or 3 lines is plenty.
2. Open `docs/ctx-orientation.md` and write your first Knob: the date, what you're building, why. That entry is the seed for everything that comes next.

**The one rule that survives every fork:**

Every Bump (a commit, a version push, a meaningful state change) earns a dated entry in `ctx-orientation.md`. Pick a shape from the five variants in `ctx-rules.md` — Knob block, semver release, agent handoff, dated priority block, or guardrail/runbook entry. Stay consistent within your project; mixing shapes inside one log creates drift.

That's the whole thing. The discipline is the log. Everything else is scaffolding that supports it.

## What This Repo Is

**Bamboo** is the source repo for a reusable documentation and agent-governance system. It is meant to be forked or copied into project repos so agents and humans inherit the same operating rules, shared vocabulary, and handoff patterns across vendors.

The policy source lives in `Bamboo.md`.
Agents start in `AGENT.md`.
Recent state for this repo lives in `docs/memory-ctx/ctx-orientation.md`.

## What It Includes

- `behavior/` for context, memory, and reasoning rules
- `workflows/` for repeatable setup and delivery procedures
- `skills/` for portable capabilities and overlays
- `architecture/` for memory-system and workflow architecture
- `agent-architecture/` for multi-agent roles, topology, and coordination patterns
- `design/` for UI and visual guidance when a repo needs it
- `docs/` for this repo's own map and change log

These modules are reusable, but downstream repos should only copy the parts they actively need.

This repo keeps its own operational log under `docs/memory-ctx/`, but the default downstream contract stays `docs/ctx-orientation.md` unless a project explicitly chooses the same layout.

## Who It Is For

- teams running multiple agent vendors
- repos that need durable handoff and context discipline
- projects that benefit from reusable Skills and workflow docs
- maintainers who want consistent repo initialization without rebuilding the docs system each time

## Intellectual Grounding

Bamboo is a synthesis, not an invention. The discipline draws from established work across information theory, cognitive science, software engineering, and AI:

- **Information entropy** — Shannon (1948)¹. Entropy as a measure of disorder gives the vocabulary for *context entropy*: retrieval probability mass spreading thin across near-duplicate chunks as a repo accumulates.
- **Working memory limits** — Miller (1956)². The "magical number seven" established working memory as bounded and dependent on chunking. A Knob is a chunk; the orientation file is a working-memory buffer.
- **Cognitive load theory** — Sweller (1988)³. PLTRF discipline is a sustained attack on *extraneous* cognitive load applied to the repo itself.
- **Tacit/explicit knowledge transfer** — Nonaka & Takeuchi (1995)⁴. The Knob log and handoff conventions are externalization surfaces in the SECI sense.
- **Retrieval-Augmented Generation (RAG)** — Lewis et al. (2020)⁵. Bamboo is a *structural* RAG complement: it shapes the corpus so retrieval is more likely to succeed.
- **Long-context degradation** — Liu et al. (2023)⁶, "Lost in the Middle." Empirical evidence that LLM retrieval is non-uniform across long contexts — validation for the "newest at the top" Knob log rule.
- **Documentation decay** — Lethbridge, Singer, Forward (2003)⁷. Voluntary documentation rots; mandatory documentation persists. PLTRF CI enforcement is the structural answer.

For the deep treatment — foundational concepts, the mapping table from prior work to Bamboo discipline, open research questions, methodological notes — see [`Documentation.md`](Documentation.md). The framework is engineering-pragmatic, not academic-formal. The grounding here exists so adopters know the operator has done their homework, not so Bamboo can be cited as a scientific work.

¹ Shannon, C. E. (1948). *A Mathematical Theory of Communication.* Bell System Technical Journal, 27(3), 379–423.
² Miller, G. A. (1956). *The Magical Number Seven, Plus or Minus Two.* Psychological Review, 63(2), 81–97.
³ Sweller, J. (1988). *Cognitive Load During Problem Solving.* Cognitive Science, 12(2), 257–285.
⁴ Nonaka, I., & Takeuchi, H. (1995). *The Knowledge-Creating Company.* Oxford University Press.
⁵ Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS 2020.
⁶ Liu, N. F., et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172.
⁷ Lethbridge, T. C., Singer, J., & Forward, A. (2003). *How Software Engineers Use Documentation.* IEEE Software, 20(6), 35–39.

## About

Created and maintained by Matt Stenquist.

Map hygiene is enforced in CI — every push runs `.github/workflows/pltrf-check.yml`, which scans the cold-start cascade and fails the build if any referenced file is missing from disk. PLTRF discipline plus a safety net.

## Recent Milestones

- 2026-06-03: Introduced a literal root `Bamboo.md` and separated policy from README and cold-start routing.
- 2026-05-30: Added PRD and TDD workflow documents.
- 2026-05-28: Added Watchdog and Drift to the memory architecture layer.
- 2026-05-16: Reworked context documents, updated the Skills folder, and added `AGENT.md`.
- 2026-05-11: Initial release.
