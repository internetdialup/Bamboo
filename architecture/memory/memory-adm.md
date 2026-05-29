# Active Dreaming Memories (ADM)

AI does not dream. It can create episodic references of past architecture, design decisions, user input, and anything between the input and output interaction. It can recall these from a cold state when the project is inactive. Keeping this context alive through an active dreaming protocol can help mitigate memory loss between project handoffs, and usage sessions.

ADM Protocols should align with CRUD and RAG practices inside the repo. Active Dreaming is the offline phase: when a project is cooling down, not actively being worked on by the user, and not being pushed forward by an external or internal force updating the codebase or architecture.

ADM helps reduce retrieval interference compared to standard RAG approaches. But ADM should not replace RAG. Combining RAG and ADM creates a sturdier context retrieval system and memory operating system. Memory context decay is real, and designing RAG and ADM methods that speak to the Memory Watchdog gives the repo a stronger memory toolchain.

ADM is useful for unlearning obsolete rules by consolidating and reinforcing new rules over stale ones. The system should not be stagnant. It should move with the project over time. ADM is stronger than plain RAG when the memory being retrieved is episodic: a Knob, a phase, a handoff, a branch, a session, or a chapter of work.

- ADM is more novel in design compared to RAG, and is a newer method of context retrieval.
- RAG is more established, and can be found in many places.
- Combining both RAG and ADM creates a sturdier system.
- We can use ADM to help mitigate memory context decay.
- Watchdog should understand if ADM and RAG protocols are established.
- Establishing a lite version of Active dreaming with the LLM (such as Gemma and Claude) will help mitigate memory loss between project handoffs, and usage sessions.

## Dual Storing Memory Architecture, and Triple Storing Memory Architecture

Defining the scope of dual stored memory architecture and triple stored memory architecture is for preventing context rot, memory loss, and weak retrieval. ADM groups memories and context into episodic, semantic, and procedural memories. Much like dreams in the human brain, we can recall episodic memories to help the project stabilize itself from drift and transition into a new Knob over time.

- ADM dreams can be considered episodic chapters. Knobs are the chapters memory retrieval uses.
- Semantic, and procedural memories will be stored in a RAG Database
- The Watchdog is informed of which episodic dream has it's attention and is prioritizing.
- Watchdog carries the ADM and references RAG to inform, audit, and double-audit authority and verisimilitude.
- Once audited, ADM can proceed down the Watchdog Funnel and be logged into the Manifest and or otherwise actioned upon for change or iterations.
- ADM and RAG must not cause friction but be aligned, and should be the standard for memory architecture, and memory retrieval.
- CRUD operations should be performed on ADM and RAG accordingly to maintain memory health, and to prevent context rot, memory loss, and to create a more robust system for memory retrieval and conversation context.

# Reference Files

Reference files internally if all exist, partial, or none. If none exist start with creating a memory overview, and move from there.
A `memory.md` should exist and allow for you to follow guardrails that allow ADM and RAG to work along side one another.

- Memory Overview - memory.md
- Memory RAG - memory-rag.md
- Memory CRUD - memory-crud.md
- Memory Watchdog - memory-watchdog.md
- Memory Context Preservation - memory-context-preservation.md
- Memory Manifest - memory-manifest.md

# ADM Conflict Memory Resolutions
- LLM can hallucinate. Active Dreaming, creates memories into episodic chapters over time.
- Conflict resolution system : Understand that the Watchdog may not have the most up to date information and should be updated accordingly.
- Conflicts with RAG and other systems may hinder ADM from working effectively.
- Read, Write, Update. No matter what these three operations should always happen in order to maintain memory integrity.

# Memory Refresh Cycle Protocol

## Trigger conditions:
- A new Knob is established.
- The repository context is reset.
- The LLM context window is cleared.
- The Watchdog identifies a need for memory refresh.

## Refresh Cycle:
1. ADM creates a fresh episodic chapter that the entire repo is aware of. We can call this the Active Memory Bank, or AMB, that the Watchdog pipeline is aware of.
2. ADM ensures that semantic and procedural memories are updated accordingly, and audits information across RAG and ADM to prevent memory corruption.
3. ADM creates a new entry within `memory.md` with a reference to the new episodic chapter, and assigns it the current date and time.
4. ADM marks the previous episodic chapter for cold storage, archival, and cleaning house.
5. ADM creates an anchor point against catastrophic memory collapse by making sure episodic memories can be retrieved, audited, and mapped to a simple memory protocol and log.


# Conlcusion 

Active Dreaming Memories act as episodic knobs that can reinforce RAG and other memory retrival methods. At the mathematical level ADM is more intensive than RAG but it provides a more logical step when you think about it in relation to a way a human dreams. Dreams act as episode we pull memory from in short term segments, along with long term referencing. ADM is the same principle. It provides a structured, and logical way to handle memory within an AI context that prevents the system from losing context over time and helps reinforce new rules and workflows.