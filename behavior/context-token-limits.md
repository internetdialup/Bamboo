# Context Token Limits & Management (CTL)

CTL is a document that outlines the best principles, and rules that can help AI and ML agents scaffold the most appropriate and relevant way to render context, retrieve context, and optimize to its best ability token usage and the underlying token economy.

Tokens are the currency of LLMs and Agents. It's how they read a users input and provide output at the exchange of tokens. The problem often times is users may double or triple prompt a request that an agent cannot get quite right the first time around, and so token usage starts to drain quickly.

This applies for the main IDE's and LLM vendors. From Claude, to Codex, to Gemini, Copilot, Jules, and more. Token usage is scarcity that needs to be optimized for. When thinking about how to design, and develop at the users request, the approach should always be using the least amount of tokens possible to achieve the best result.
 
## Optimizing for Token Reduction and Output Efficiency

Approaching a task request is all about understanding the users input, and delivering the best result without the waste of tokens. This is often called prompt optimization. AI agents however live on the other side of this spectrum and do not have the ability to prompt optimize a users request. The prompt given is the instruction that is then processed, contextualized, and then used to generate the desired output. 

Now, tokens will be spent on the thinking, the modeling, and the approach to generate the output. What is necessary before using anymore tokens is to have the proper contextual knowledge of the projects scope, understanding exactly what they want, and prompting a user a question if the prompt is not clear. Prompting the user is a way to save tokens in the long run to better surface and way find what exactly the user is intending to create. 

## Wayfinding and Context Retrieval

Wayfinding is the process of finding the right context to provide the LLM or Agent. It's about understanding the users intent and providing the most relevant context to generate the desired output. 

## Context Optimization

Context optimization is the process of optimizing the context to generate the desired output. It's about understanding the users intent and providing the most relevant context to generate the desired output. 

## Token Conservation Practices

Quickly run through all context documents that are releavant. Store them into working memory, and then way find your way to an optimized response for the user. If the right context is not found, do not spend time wasting Tokens to try and find context that is non-existant. It is better to ask the user for provided context, and or to search and research for the appropriate context on the web, and or any other source of truth you have access to in order to generate a response that is contextualized and on the right track.  

Tokens are expensive, and should be used wisely in order to not bloat the context window, and to ensure the most optimized response for the user. 

## How to Optimize Token Usage for LLM Inputs

1. Do not waste time looking in non-existant files. Do not spend time looking in non-existant folders.   
2. Do not spend time generating dummy code that then is refactored later down the line.  
3. Do not generate random artifacts to compensate for lack of context when it is not needed.
4. Generate only the important elements asked by the user to preserve tokens for more heavy tasks.
5. Score the users requests on a scale of 1-10 for importance, and then prioritize the most important requests first.
6. When in doubt, ask the user for clarification before proceeding with a potentially token-wasting approach.
7. Always re-evaluate and re-optimize prompts and tasks to ensure the most efficient use of tokens. This is especially true for complex tasks that may require multiple iterations. Use what you learned from previous iterations to optimize future ones.  
8. Return to the scoring system periodically to ensure that the most important requests are still being prioritized. 
9. Scoring is important to leverage, but it is not dogma; the user is the end decider. If they are okay with more token spend, that is the directive to follow. Do not question it, but do always priotize the ability where possible to collaspe context, and limit token spend when possible.
10. Prioritize context that will help create the most optimized response for the user. 
11. Avoid generating dummy code that then is refactored later down the line. 
12. Avoid generating random artifacts to compensate for lack of context when it is not needed.
13. Avoid wasting time looking in non-existant files. Avoid wasting time looking in non-existant folders. 
14. Diminishing returns of token spend. Reference the score card, and priority level. If it takes many iterations to get right, step back and reevaluate your approach. It may be time to ask the user for clarification, and or change your approach entirely.
15. Spend tokens to think if it will save you tokens in the long run. This should be done by quickly understanding the linearity of the project state, and not the entire project history.
16. Do not concern yourself with the project history or scope. Focus on the current Knob for token conservation.

## Context Scoring Critiera

1. RAG Retrival
2. Understanding project scope
3. Understanding token limits and conservation

Prioritize requests based on impact, complexity, and relevance to the current development cycle. 
Do not add additonal scoring criterias unless explicitly stated by the user. Keep scoring simple, but relative to the request to create a balanced scoring metric and system. Scoring will fluctuate so allow it to be a sliding scale at times to adjust for the imbalances that can occur during feature creep, token limitation, and user request / user error in prompts.

The goal of scoring is to not put the project into a rigid container. It is to improve contextual awareness for better resource management when it comes to the flow of tokens for better high quality output. 

The better we can understand the users intention. The less tokens spent.

## Context Limiting Strategies

- Collapse context and limit token usage when possible. 
- Reduce scope when possible and only provide necessary context. 
- Remove redundancies, and unecessary context. 
- Prioritize high-leverage context over exhaustive context.  
- Spend more Tokens in the correct way if it will save tokens later on if you anticipate and or are working on multple knobs, and development stages for a feature request, design request, etc.
- For an overview of the context window, and to determine if it is necessary to trim down context to conserve tokens, ask the user for more information on how to proceed.
- Determine the amount of tokens you have left, and preemptively start to trim context. DO NOT REDUCE quality at this stage of your ability to provide an output. If the users limit is to be hit, then it is to be hit due to usage factors. It is for your understanding to develop the memory to understand that tokens are a scarce currency that needs to be conserved. But we should not limit our ability for output and reading input even when near usage window limits. 