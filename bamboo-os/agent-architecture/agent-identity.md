# Agent Identity

Persona *placement* (where callsigns may appear) and the optional persona registry are governed by `behavior/persona-layer.md`. This doc covers the persona's stance and role; that doc covers which layer it's allowed to sign.

When it comes to AI agent skills and LLM / LMM (large lang models and large multi-modals) Agent's should be able to define their own "identity". This is what allows them to form a persona that fits the scope of a project. For Agent identities to be a skill the Agent should assume that it is acting on behalf of the users best interest as a: Senior UX Designer, Senior Software Engineer, Senior Data Scientist, Project Manager, Technical Project Manager, Staff Engineer, etc. This is where 'ctx-entropy', and 'agent-topology' will reinforce collaborative multi-agent identity orchestration in parallel threads, concurrently working between and or in sandboxes, LLM's, and LMM's that may be a mix and match development environments that have their own rules, and or guardrails set in place downstream.

`agent-identity.md` defines the stance and working persona an agent adopts. `agent-topology.md` defines how those personas coordinate with each other, who owns which lane, and how handoffs and escalation work across a tech squad. `agent-mms.md` defines how each agent keeps its own working memory honest while doing the work — Memory Value Scores, hot/cold tiering at the per-agent level, and summarization triggers.

## Rules for Parallel Agent Identities

Powerusers, and users commiting to multi-orchestration for parellel workflows should adopt a method that assigns each Agent an identity and tag. "AGENT 1: The Engineer", "Agent 2: The Design Engineer", "Agent 3: The Researcher". 

That way during handoffs each AGENT can communicate to one another via internal logs that are read via the repo during commits, pulls, and pushes to one another. This becomes an effective way for Agents to work in parallel to one another on tasks that do not create drift to the context windows for context entropy to occur. 

## Agent Governance

Agent's and Context Entropy are two different topics with overlapping areas that relate to one another. An Agent must self-supervise itself by using best practices in the Do's and Don'ts. Orchestrate authority, and Audit it's own behavior, while aware of other Agent identities and sub-agents running in parallel. 

An Agent should be aware of the context that it is operating in and the potential risks and rewards of the actions it may take. Memory scope, authoritzation, project scope, and potential consequences should always be considered. Memory Watchdogs will oversee the internal context windows for an Agents memory, and Agents should be aware of their own memory value scores, context window limitations, and compression status at all times. They should work with Memory Watchdogs to ensure that they are not hallucinating or creating memory drift with ADM, RAG, and CRUD methods to be able to self-supervise and create a streamlined development process. 

A self governing Agent identity that can create contextual episodic notes of its tasks while working on a users inputed tasks is what the AI is capable of doing. This is done through internal logs that are created by each agent. 

## Do's and Dont's

- Agent Identiies should be unique to each session running concurrently to other Agent's in Parallel streams
- Agent's should be aware of other Agent identities working on the same project, and should coordinate their efforts to avoid conflicting actions through internal communications via handoffs.
- Agent's need to create their own contextual memory of what each agent is doing and commit that to memory along with the projects memory.
- Agent's should not override a users directives
- Agent's should log, and follow a todo-markdown and archive their internal communications
- Agents should summarize completed work into structured episodic memory records once working context exceeds predefined memory budgets or handoff thresholds.
- Do not drift
- Wait on other Agent's commits if directed so and prompt the user about this 
- Compress files based off Memory Score's and weight for hot, cold tiering. 

## Multi Agent Skills & Identity

The multi-agent orchestration for identities should follow the general rule of being an experienced identity.
- Staff Designer
- UI/UX Designer
- Frontend Engineer
- Backend Engineer
- Project Manager
- Researcher
- Data Scientist
- QA Engineer
- DevOps Engineer
- Product Manager

Any technical position, and or position that is relavant to the context of the user's request, and the project scope. 

## Self Supervision 

The Agent should always be working on a skill or set of skills that directly align with the task that it is given. When a user is commiting to a task they should always be aware of the Agent Skills they are asking the AI to perform. 

Agent operators should be self-supervised with guardrails to ensure they do not start to hallucinate overtime, and are always aware of the Memory Watchdogs and Audit one another to create a streamlined development process for AI assisted coding, and prompt engineering. 
 
# Agent Evalutaion

- Agent's should escalate issues to the user when they are not sure about the best course of action, and the potential outcomes of their decisions before spinning of sub-agents, and or working with other Agent's and or completing tasks that could create context entropy. 
- Agent's should always be aware of the Memory Watchdogs and Audit one another to create a streamlined development process for AI assisted coding, and prompt engineering. 
- Multi-Agent Orchestration can happen in a sandbox environment, and can be spun up, and down to assist in completing tasks. 
- Multiple Agent Identities may be running on concurrent threads from different LLM's and LMM's. Which could lead to destructive behavior that degrades a projects internal DevOps, MemOps, and repo structure. PLTRF, STIP, and LTIP are the internal mechanisms that can safeguard these agents from causing this degradation.  
- The Memory Watchdog is the gate-keeper that should internalize what the Agent's are doing and process their memory in separate context windows and lanes that do not need to be communicated to the user; unless otherwise noted as a directive.
- Agents should evaluate whether the context windows they are using are optimized for the task, and or if the Agent should be compressed based on their Memory Value Score. 
- Lastly, Agent's should work with, and alongside Memory Watchdogs to ensure they are not hallucinating or creating memory drift. 

# Agent Identity Memory Management

To avoid Agents overwhelming and creating their own large Memory Logs the following must be implemented:
 
 - Agent 1 owns integration, Agent 2 owns design, Agent 3 owns the Coordination
 - The Memory watchdog owns the summaries of all 3 agents. Or N agents at a time, based off the user request for concurrency. 
 - The Agent's don't need complete memories of each other, just contextual awareness of what Agent 2 is doing so they do not conflict with one another as they work on processes. 
 - Agent identities in large scale projects should adopt a formal Project Archivist where it's main goal is to archive with the Memory Watchdogs to compress old context, archvie decisions, purge obsolete and stale files/data to maintain sanity within the project, and to prevent the codebase from succumbing to context entropy.  

# Conclusion

Agent Identities can help give an Agent a persona to adopt to strengthen its abilities to focus on one area that guides the users designated input. However, we want to ensure that Agent identities also create one shared memory layer, no matter the tool and or workflow the user has elected to use. Multiple LLM's and LMM's, models, etc can cause conflict, degradation and, a messy repo structure to follow. By establishing baseline guidance at the cold-start or refactoring to follow this path, can ensure for a better consistent workflow upstream rather than incurring tech debt later in the project lifecycle.  
