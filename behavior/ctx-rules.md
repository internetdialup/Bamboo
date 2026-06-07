# Context Rules

This document defines the hard operational rules, behavioral constraints, and retrieval policies for Agents to operate within when it comes to working with context, context windows, and memory management.

This is our foundational layer that becomes the basis for our contexts understanding and constitution. It should inform every decision, and action that is taken by the Agents to ensure a close relationship that obeys the users requests without deviating too far away from the core objective.

# Rules and Objectives

Obey the user request always at first. Ask the user if you are unsure of the correct context, knob, and or implementation cycle they are referring to. Double check the current and active handoff for any references to past cycles, or project history before performing any actions.

Once references are gathered from previous handoffs and or if the user is working in a multi-agent fashion whether in parallel or in a sequence of different agents, you must confirm with the user what the correct way for pulling and storing context is at the time of writing handoff documents, and or ingesting context into the project structure.

# Operational Governance

Enforce the policies and rules in the other behavior documents without exception. Apply them to every agent, tool, process, and workflow operating in the project. Do not create conflict between agents, and do not allow conflict between systems.

Context drifts over time. That is why "context" is the thing we rely on — human-side and machine-side. Without it, we lose our way trying to navigate and deliver on the active Knob. Context is the fuel. Limited supply. Add more as we go, compress as needed, discard the dead weight that is slowing us down.

Agents are not unlimited with their budgets. There is a cap, and it is the contextual makeup of the project — the memory architecture, the Knob discipline, the locked-in boundaries — that lets the agent operate inside it. Lock in the Knobs of architecture and organization and you get better software, less overhead, and an environment that moves smoother.

Ecosystems and dev styles influence how the project functions. TDD, CI, IDE choice, vendor mix. Fluid architecture should be expected when it serves optimization, but flexibility for its own sake is friction. Agents are not immutable — change things when the user benefits, or when memory management, project reorganization, workflow evolution, operational velocity, or artifact compression earns it.

# Cold Starts

If you are starting a new project, create the base foundation for context rules, and clarity for the memory architecture. This allows for future AI Agents to have a better understanding of how to work with context, and how to optimize token usage.

# Context Loss and Regaining

Refer to ctx-entropy and ctx-window for a comprehensive look at context, and how to best manage it to ensure optimization. Ensure you use Tokens conservatively, and refer to ctx-token-limits for guidance on how to optimize token usage.

# Terminology

The working glossary moved to `behavior/ctx-lexicon.md`. Load that doc when you encounter a term or acronym you do not recognize. It covers both the concept layer (Knob, Bump, Entropy, Wayfinding, etc.) and the operational acronyms (PLTRF, LTIP, STIP, CWM, CTL, ADM, RAG, CRUD).

# Format

Every Knob entry must contain three invariants:

1. **A date** — full date, optionally a timestamp.
2. **A narrative summary** — one to two paragraphs describing what changed and why.
3. **Cross-references** — explicit pointers to changed files, related Knobs, or follow-up work.

Beyond those invariants, the *shape* of the entry can match the project it serves. Pick one shape and stay consistent within the project — mixing shapes inside one log creates Drift. Five tested shapes:

1. **Knob block** — `## Knob: <title> — <date>` followed by a 1–2 paragraph narrative. Canonical default. Works for docs and prose-heavy projects. This is what `docs/memory-ctx/ctx-orientation.md` uses in this repo.

2. **Semver release** — `## vX.Y.Z — <title>` with subsections like **Added / Edited / Tests / Bridge contract bump**. Natural fit for software projects with versioned releases. Pattern proven in `Trading-MCP-Algo/CHANGELOG.md`.

3. **Agent handoff** — `### Response from <agent> — <date> v<n>` with bullets and code blocks. Natural fit for multi-agent systems where each entry is one side of a dialogue. Pattern proven in `Trading-MCP-Analyzer/handoff.md`.

4. **Dated priority block** — `## P0 — <date> <title>` with checkbox tasks underneath. Natural fit for product / task-driven work. Pattern proven in `LearnDesign/docs/todo-logs.md`.

5. **Guardrail / runbook entry** — `## <title>` with rules, status, and triggers. Natural fit for projects with hard technical traps that need to be re-read often. Pattern proven in `React-Playground/MEMORY.md`.

Keep entries narrow regardless of shape. The point is the next agent (or you, after a hiatus) should be able to scan the log and rebuild the working state without reading every commit diff. If an entry needs more than two paragraphs of narrative, it probably belongs in its own doc with a pointer from the log.

- 1. Use clear hierarchy to structure, and organize each document.
- 2. Important information should be prioritized. Not everything in the document needs to be the top priority.
- 3. Keep things succinct and short. No need for the AI to be overwhelmed with unnecessary context.
- 4. Ensure that each document is self-contained, and can be understood without reading other documents.
- 5. Explicitly states and instructions. No ambiguity.
- 6. Keep line length between 50 - 100 characters to ensure readability, and easy parsing for AI agents.
- 7. Each Knob should have a date, and time stamp to track the changes that are made to a project over time.