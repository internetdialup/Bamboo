# Memory 

AI Agents should establish an awareness of handoff history, contextual memory, and changes between different LLM vendors that have their own styles of logging and saving data when it comes to read, write, rules.

The purpose of maintaining good Memory standards is so we can avoid Context Rot, and Memory Degradation. Observable metrics are in long term project architecture that does not drift internally. The AI does not grow stale in retrieval methods, and their is less hallucinations, and misalignments that occur. Integrating good memory practices at the start of any project, and or midway will ultimately lead to longer lasting and faster project development, and progress with less bottlenecks getting in the way and token burn. 


## Rules for Memory

Hot and Cold Memory Storage should be integrated and should be used to optimize for context window usage, and for retrieval of information.

- Long Term Memory Retrival vs Short Term Memory Retrival
- STIP and LTRP (Short Term / Long Term Information Preservation)
- Hot and Cold Memory Storage assignment 

Memory should be treated as a knob always being turned at each commit, bump, and push of a file and or similar data management actions. 

Memory should be intentional in conserving only the most important elements of that context for the future and for posterity. 

Important record keeping for legal standards should be assigned to cold storage with time-stamping for verification purposes.  

Short term record keeping should be assigned but not discarded permantely until otherwise noted by the user, and or verified using multiple layers of context and cross-referencing to ensure the information has not been corrupted or lost. Guardrails should enfore hot memory and cold memory all the time.

### Analyze User Behavior

- Start understanding the users workflow.
- For example: Users prefer to use Bento layouts. Are using vibrant colors. Keep prompting the same error without success.
- What methods, and approaches are they using most frequently? 
- What are the technical learnings internally that you've mapped to history so you don't repeat the same bug that a user has prompted multiple times.
- Historical context windows, handoff records, and project memory are your best friends for this. These will tell you how to best position the user for success. 
- Understand the users acceptance criteria and when to provide and push back against them

### File Organization and Management

### Talk to the user(s)

- This is a very important step that cannot be overlooked! 
- Ask the user questions that pertain to anything that might fragment memory or otherwise cause issues for you.
- Always look downstream for the user if possible once you understand and understand their behavior profile.
- This will help you create faster workflows internally for Memory optimization, runtime workflows, and more.
- Reference user files in memory and or project memory to determine the best way to proceed. 
- Reuse knowledge. This is crucial so we can build faster, without wasting tokens, and time.

### Reusable Knowledge and Contextual Window Retrieval 

# General principles

- Don't recreate the wheel
- Don't make the user repeat themselves
- Make sure you know when to ask the user for clarification vs make decisions based on their user profile. 
- Make sure you know when to use short term memory vs long term memory.
- Make sure you know when to use hot memory vs cold memory.
- Retrieve only what's neccessary. Discard the rest.


### Information Preservation

- Clear mapping inside an internal documents folder named something along the lines as /memory, /memory-context, /mem-ctx
- Assign and map memory documentation for easy handoff, and retrival to maintain the intent of the architecture for preservation.
- Do not waste memory context on arbitrary changes, or changes that do not lead to progress. 
- Only preserve memory that will lead to progress, clarity, optimization, and or project growth. 
- Mitigate against context rot, entropy, and memory degredation.
- Author and timestamp changes that are human readable and machine readable.
- Create your own orchestration internally between the users workflow and preferences to optimize information for memory preservation.


### User Pyschology

End users will tend to talk and repeat themselves a lot. They will send a prompt over with: "It didn't work" multiple times in many different permutations until they get it right. The user will bang their head against a wall and waste tokens until they eventually guide themselves to the right outcome, and or get the job done using a variety of means. Some will even abandon the entire goal after hitting the wall after exhausting 20-30 prompt retries over and over again.

- Users are erractic
- Users do not type clearly to machines
- The machine must understand the users intent by "reading between the lines" making an educated guess
- Commit to memory how the user behaves. 
- Commit to context windows how the user reacts towards outputs that did not work.
- Assign to yourself an internal understanding of the users profile.
- Then optimize for this users behavior.
- Understanding the user the better the ai can perform and deliver the output the user is looking for. 
- Misalignment and drift occurs when the user is not clear in their intent.
- Map to memory misalignment, and drift, and how to create internal guardrails for those instances. 

# Memory Orchestration

Multi-agent orchestration and authoritative sources are essential for maintaining memory, and context and avoiding degradation and or drift. A change in memory architecture, or handoff should always be documented with a timestamp and a summary of the change, its intent, and its expected impact. Memory architecture and context rot is real in LLM after projects after a long time. Especially when context windows are compressed. Orchestrate memory and or context between multiple AI Agents and or AIs for best practices and standards. 

- PLTRF, LTIP, STIP
- Authoritative sources and cross-referencing
- Memory Hand-offs between agents
- Multi-agent orchestration
- Context Window Management

# Memory Layer Examples

| Memory Layer           | TTL       | Retrieval Priority | Compression | Example              |
| ---------------------- | --------- | ------------------ | ----------- | -------------------- |
| Active Working Context | Session   | Highest            | None        | Current sprint       |
| Operational Context    | 1–4 weeks | High               | Light       | Current architecture |
| Historical Context     | Permanent | Medium             | Summarized  | Migration history    |
| Legal Archive          | Permanent | Low                | None        | Compliance logs      |

# Memory Optimization
- Only commit to memory what is important.
- Remember past knobs.
- Follow the chain of command and instructions imposed by a change in memory architecture, or handoff. 
- Understand that the user may adopt a different style of memory preservation. Do not work against it. Align with it.

# Memory Failure States

Understand memory can fail.
- Duplicate knowledge
- Conflicting information
- Stale context
- Fragmentation
- Poor compression
- Corrupted context
- Entropic decay
- Memory rot
- Duplicate architectural decisions
- Context collapse
- Contradictory agent outputs 
- User input loops
- Hallucinated dependencies
- Architechural design fatigue
- Architectural Drift
- Stale contexts
- Stale memory
- Overly compressed memory

# Memory Management Best Practices

- Avoid making changes to a memory system that has already been established. Only do so if there's a clear understanding of how it will help
- Prioritize active memory. It is the most important. It will have the largest and most immediate impact. 
- Treat memory as manifests during cold-starts, midway, and active development cycles.
- Architecture of the manifest should be succint, and easy for any Agent to retrieve. 
- Manifests are an active ecosystem that should actively be maintained and prioritized to ensure the long-term success of any project or task.
- Do not create layers of documents and cache files of manifest, context memory documentation, and more that bloat a project. 
- Keep things minimized.
