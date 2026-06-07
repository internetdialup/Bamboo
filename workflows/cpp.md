# CPP — Context Preservation Protocol

CPP is the workflow that keeps a project's memory alive across the big transitions — branch switches, scope changes, production deployments, phase rollovers, and any time work moves from one cycle to the next. It is the DevOps-shaped sibling of the preservation discipline in `behavior/ctx-entropy.md` (LTIP), applied to the moments when context is most likely to drop on the floor.

This doc used to live as a section inside `architecture/workflow-tools.md`. It moved here because CPP is workflow-level — about how the project transitions across phases — not memory-architecture-level. The Watchdog enforces it; CPP defines what enforcement looks like.

---

## Why CPP Earns its Own Doc

The big transitions are where memory leaks happen. A user closes out a feature branch and the Knob log entry never gets written. Production deploys land and the architectural decisions that drove them stay only in the deploy notes. A user comes back after a hiatus and the LLM has no orientation. CPP names the protocol for catching those leak points before they cost the project.

It evolves as the project evolves. DevOps and forward-deployment standards will influence it heavily. The principle stays the same: treat everything as potentially needing to be archived and preserved. Do not harm the memory.

---

## Memory Archiving Standards

When a user decides to move on from a specific phase of development, a specific branch, or a specific feature, you must decide if that work needs to be preserved in memory.

- The Watchdog must be aware of all memory standards and acts as the gatekeeper of memory archiving. See `architecture/memory/memory-watchdog.md` for the Watchdog's role and the persona doc (planned) for the voice.
- Workflows should create standards around the Watchdog, and context handoff and retrieval systems.
- Developing an internal awareness for the AI (through Watchdog memory standards and context preservation) creates a concrete understanding of user behavior, project evolution, and workflow optimizations.

---

## Triggers

CPP runs on three triggers:

1. **Branch close** — a feature branch is about to merge or be abandoned. Before the close, summarize the Knobs that lived on the branch into the canonical orientation log. Anything the branch learned that main needs gets a dedicated Knob entry, not just a commit message.
2. **Phase rollover** — a release ships, a sprint ends, a development phase transitions. Compress the active Knob log if it has crossed its threshold (5000 chars by default in this framework). Older Knobs migrate to summary-N files. The hot log stays lean.
3. **Production deploy** — work moves into the real world. The architectural decisions that drove the deploy get a deliberate Knob entry. The Watchdog audits the orientation log post-deploy to confirm nothing critical was left only in commit messages.

---

## Anti-Patterns

- Treating commit messages as the orientation log. Commit messages are git history, not project memory. Knobs are project memory.
- Letting the orientation log overflow past its threshold without spawning a summary-N file. The hot log gets cluttered, the cold archive never gets created, retrieval degrades.
- Closing a branch without a Knob entry summarizing what it learned. The branch dies, the work survives, the *reasoning* does not.
- Skipping CPP because the transition feels small. The leaks are cumulative. Five small skips equal one big rewrite later.

---

## Cross-references

- `behavior/ctx-entropy.md` — LTIP, PLTRF, STIP. The preservation principles CPP implements.
- `architecture/workflow-tools.md` — where CPP used to live; pointer remains.
- `architecture/memory/memory-watchdog.md` — the Watchdog enforces CPP at the gate.
- `workflows/project-context.md` — ongoing project-level context governance.
- `behavior/ctx-lexicon.md` — CPP glossary entry.
