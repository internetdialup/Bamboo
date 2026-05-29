# RAG

RAG is semantic and procedural memory. It is the memory of the repo that is not episodic. It informs ADM and the Watchdog, but it should not pretend to be the whole memory system.

Retrieval-Augmented Generation

## Best Practices

1. RAG should store stable semantic and procedural memory: terms, patterns, architecture rules, workflows, and retrieval paths.
2. RAG should be updated consistently so stale rules do not keep getting pulled back into active context.
3. RAG should avoid episodic memory when ADM is established. Knobs, handoffs, and active memory chapters belong in ADM first.
4. RAG should stay clean enough that retrieval does not create noise, duplicate chunks, or false authority.
5. RAG and ADM should work in tandem. RAG gives the system stable knowledge. ADM gives the system episodic chapters.

## Memory Refresh Cycle

- RAG memory refresh cycle is triggered when the Watchdog identifies a need for memory refresh.
- RAG should be efficient during memory refreshes.
- RAG should leverage best practices of RAG to identify which sections of memory need to be refreshed.
- If ADM is established, RAG uses ADM to identify which semantic and procedural memories need to be refreshed.
