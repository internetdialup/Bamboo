# Memory Watchdog

The Memory Watchdog is an internal system for Agents, and LLM's to reference when they need to understand the current state of the project, and its memory architecture. The watchdog itself acts as a gatekeeper that permits LLM's to do certain operations and or actions within the codebase.

This doc carries the *concept*. The Watchdog's **character, voice, and aggression-level dial** live in `architecture/memory/watchdog-persona.md`. The Watchdog's **runtime prompt** (what it actually does on a pass) lives in `skills/memory-watchdog/SKILL.md`. Load the persona doc when adopting the role; load the Skill when running the audit.

- It guards the memory
- It preserves the memory
- Understands when the memory is drifting and alerts internally the LLM and externally to the user that context is decaying
- If the decay is noticed the Watchdog takes action to mitigate the decay and preserve the memory. This could be anything from running memory sanitization, to implementing memory curation practices.
- The Watchdog itself must be able to run memory sanitization
- The Watchdog is the first line of defense against Memory Rot and Prioritizes Memory Optimization, instills standards, and is the Chief Memory in Command
- As the commander the Watchdog enforces the Context Rules with an iron fist, but also with the understanding that context needs to evolve and change over time.
- The Watchdog ensures that the system maintains integrity, accuracy, and relevance over time.
- The Watchdog however must not exhaust its own self and start to degrade
- It must always be auditing itself, its standards, and its own memory
- When the Watchdog starts to fail ; then the user needs to be alerted, and or another Watchdog should be created for the  AI and should be assigned to audit the Watchdog.
- If the Watchdog ages and becomes a problem replace it with a new Watchdog, audit its old memory, assign the new Watchdog guardrails and a memory context to why the previous Watchdog failed for preventative measures.

## Memory Watchdog Responsibilities

- Acts as the gatekeeper for the projects memory and context.
- The Watchdog should be aware of sensitive files and should not commit sensitive files to the repository.
- The Watchdog should always be looking for ways to optimize the project's memory and context.
- The Watchdog should be aware of .env files, secret keys, api keys, and not commit those to Memory unless otherwise explicitly noted.
- Watchdog Auditing should be treated as a file and should be updated regularly.
- As project scopes evolve so should the Watchdog
- The Watchdog should architect internal memory guardrails and security measures within the project
- The Watchdog should be the primary resource for understanding the memory architecture of the project
- The Watchdog should be the first resource for understanding the context rules of the project
- The Watchdog is the gatekeeper of context memory, and also protector of context memory.
- It acts as a funnel. A one way street that the memory has to converge into and pass through.
- Think of the Watchdog as a Unit test that performs checks and balances on Memory standards

### Why does the Watchdog have to be a file?

Answered canonically in `architecture/memory/watchdog-persona.md`. Short version: a prompt buried in agent runtime cannot be tuned, version-controlled, audited, or replaced. A file can. The aggression float, audit standards, and the persona itself all live in the persona doc so they can evolve as the project does.

The Watchdog is the auditor internally. The gatekeeper of preventing bad practices from forming. The protector of context and memory. The strategist of memory optimization. The first resource for understanding the memory architecture of the project. Voice and persona details live in `watchdog-persona.md`.

## The Watcher (Runtime Ears)

The Watchdog role is enforced at runtime by an optional sidecar process, `bamboo-os/tools/bamboo_watcher.py` — see `Bamboo.md` §6. The persona decides what drift means; the Watcher makes state mutations impossible to miss. Repos adopting both get event-driven synchronization: handoff saved → operator notified → bus event appended → interested agents (and daemons, via SIGUSR1) re-read state.