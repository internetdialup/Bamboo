# Memory Compression

Compression already has a home in this repo. context-window.md defines what it is. Compression is not deletion, it is prioritization, and the hot and cold tiering rules live there. This document does not redefine any of that. This document is the scoring layer that sits underneath it. The part that answers the harder question. When the agent decides to compress, archive, promote, or delete a document, what is that decision actually based on.

Right now the answer is judgment. The active Knob stays hot, the last few Knobs stay warm, everything older goes cold. That works while a project is small and the agent can hold the whole shape in its head. It stops working when the repo grows past the point where any one agent can eyeball what matters. At that scale the tiering needs a number behind it, not a feel.

So this doc is about giving each document a value the agent can compute, and a set of triggers that fire when the corpus as a whole starts to rot. It is closer to cache eviction and garbage collection than to anything novel. That is on purpose. The proven idea is the safe idea.

## What This Doc Is Not

It is not the request scoring rubric. context-token-limits.md scores a users request 1 to 10 on Impact, Complexity, and Relevance. That is about whether a request is worth the Tokens right now. The scores here are about documents, not requests. How much a file is worth keeping hot, how much the corpus is drifting, how much the agent should trust what it just retrieved. Different axis, different job. Do not collapse the two into one pile of numbers.

## The Memory Value Score

Every document in the repo can carry a value that decides which tier it belongs in. The first instinct is to multiply the things that make a doc important and divide by how old it is. That instinct is close but it breaks in two specific ways, and both of them delete the wrong files.

The first break is age. Age in the denominator punishes old docs. But the oldest docs in this repo are the foundational ones. context-rules.md is old and it is the first thing every agent reads. A formula that divides by age wants to archive the constitution. What matters is not age, it is recency. Time since the doc was last touched or retrieved. A doc read yesterday is hot no matter when it was written. A doc untouched for fifty Knobs is cold even if it is new.

The second break is multiplication. Multiply relevance by access count by dependency count and any single zero zeros the whole score. A license file gets retrieved almost never and cannot be deleted. A spec that nothing references yet but the user just wrote is not worthless. Raw multiplication also lets the biggest number win. Access count in the thousands swamps a relevance score that lives between zero and one.

So the shape that holds up is a weighted sum of normalized parts, decayed by recency, with a floor for anything pinned.

Memory Value = ( wR · Relevance + wA · log(1 + AccessCount) + wD · log(1 + DependencyCount) ) × RecencyWeight

Relevance is normalized zero to one against the current Knob. The log on the counts keeps a doc referenced forty times from drowning a doc referenced four. RecencyWeight is an exponential decay on time since last access, so a doc that has gone quiet sinks on its own without anyone having to mark it stale. The weights wR, wA, wD are yours to tune per project, and they should sum to one so the score stays in a readable range.

Pinning overrides the math. A foundational doc carries a pin and its value is floored so no eviction pass can touch it. The formula is allowed to recommend. It is not allowed to delete the foundation.

So now all files and memories are not treated equally. The AI now can score and decide how to:

- Promote. High value. Pull it hot, keep it in the active window.
- Compress. Middle value. Summarize it, keep the summary hot and the full text cold.
- Archive. Low value. Move it to cold storage. Recoverable, out of the working set.
- Delete. Lowest value, and only when it is also unpinned, referenced by nothing, and superseded by a newer doc. Deletion is the one action that asks the user first. context-window.md already says we do not discard without understanding the project state. The score does not get to override that.

## Scoring Table

The Memory Value score above runs on a handful of inputs. The theory starts to take shape in the form of an algo that the AI can use to balance and score for compression. Here is what each input means, and how it actually feeds into the score.

| Input            | Meaning                              | Range                          | Role                              |
| ---------------- | ------------------------------------ | ------------------------------ | --------------------------------- |
| Relevance        | Importance to the current Knob       | 0 to 1                         | Weighted term                     |
| Access Count     | Times the doc has been retrieved     | Log dampened                   | Weighted term                     |
| Dependency Count | Files that reference it              | Log dampened                   | Weighted term                     |
| Recency          | Time since last touched or retrieved | Decays to a 0 to 1 multiplier  | Scales the whole score            |
| Pinned           | Foundational flag                    | Boolean                        | Floors the score, immune to evict |

Recency sits where age used to. Age punishes the oldest docs, and the oldest docs are usually the foundational ones. Recency flips that and rewards what is still getting used. Compression Ratio is worth tracking but it does not score anything. It is the number you read after a compress, not the reason you ran one. Keep it on the dashboard and out of the formula.

## Retrieval Confidence and Conflict Detection

This is the part worth building first. It prevents a hallucination instead of just tidying the shelves.

When an agent answers a question it retrieves a handful of documents. Ask how auth works and it might pull auth-v1.md, auth-v2.md, an oauth spec, and the supabase notes. The agent blends those into an answer. The danger is not that it retrieved too little. The danger is that it retrieved four docs that disagree, and blended the disagreement into something confident and wrong.

So before the agent answers, measure how much the retrieved set agrees with itself. If every doc points the same way the confidence is high. If auth-v1 and auth-v2 contradict each other on where the session token lives, the confidence is low, and that low number is the signal. The repo surfaces it.

CONTEXT CONFLICT DETECTED. Retrieved auth-v1.md and auth-v2.md disagree on session handling. Resolve before relying on this answer.

That warning fires before the bad answer, not after. Version drift is exactly where these conflicts hide, because the old doc rarely gets deleted when the new one lands, and both stay retrievable. An agreement check turns a silent trap into a loud one. The mechanism is a contradiction check across the retrieved set, pairwise, and it does not need to be heavy to earn its place. Even a coarse agree or disagree per pair beats blending the conflict blind.

## When Compression Triggers

The Memory Value score sorts individual docs. It does not tell you when to run a pass over the whole repo. That trigger belongs to entropy, and entropy is defined in context-entropy.md, not here. This doc does not get its own competing entropy number.

What this doc adds is the garbage collection framing. A reorganization pass is expensive, so you do not run it every Knob. You run it when the corpus crosses a threshold. Too much volume, too much duplication, retrieval accuracy starting to slide. This is where the theory of context entropy falls into place. Trigger Context Reorganization once entropy crosses a threshold, and the compression pass fires, scores every doc, and re-tiers the repo. Same idea as a runtime pausing to collect garbage. Let it accumulate, sweep, keep going.

The threshold is a project level dial, not a universal constant. A small SaaS tolerates more mess before a sweep earns its cost than an enterprise monolith does. This is where PLTRF is crucial. It is the discipline that keeps the repo from fragmenting in the stretches between sweeps, so each pass has less to clean up than the last.

## Research Surface

A few ideas belong here as exploration, not as core behavior. They are flagged so no agent treats them as shipped.

Context survivability borrows the ablation idea from chaos engineering. Randomly remove documents, randomly summarize them, randomly perturb what the agent retrieves, then ask whether the agent can still answer a fixed set of questions correctly. Run it enough times and you get a survivability number. Ninety two percent of perturbations still answerable is a robust corpus. The catch is cost. It needs a fixed question set with known answers and a lot of runs, which makes it a benchmark you run occasionally, not a thing the agent does inline. Treat it as a research feature.

Signal over noise at retrieval is the open one, and it needs a definition before it needs an algorithm. Name the signal and name the noise first. If signal is the doc that answers the query and noise is the stale or duplicate chunks retrieved alongside it, then the methods that fit are reranking the retrieved set, deduplicating by embedding similarity, and the conflict check above. Those are the levers that move retrieval signal over noise. A convolution over a grid is a tool for data that has real spatial locality, like an image, and a pile of documents does not have that shape by default. If a grid earns its place it is as a way to see the repo, a density map of where topics cluster and where they thin, not as a way to rank a retrieval. A Gaussian belongs to that picture as a smoothing kernel over a density estimate, not as a noise filter on a ranking. Decide what the grid is for before deciding it is a grid.

## End of Documentation

This doc is the scoring layer. context-window.md owns the compression principle and the hot and cold tiering it scores against. context-entropy.md owns entropy and the decay this pass fights, and it holds the threshold that triggers a sweep. memory.md owns the broad memory standard these scores operate inside. memory-tal.md, when it is written, owns the temporal side, and the recency decay in the Memory Value score is the first place the two will meet. Update this doc when the scoring changes shape, not when a weight gets tuned.
