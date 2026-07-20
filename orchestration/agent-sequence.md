# Agent Sequence Example

## Why this file exists
This file gives a narrative view of the multi-agent flow so learners can compare it with the diagram artifact. It connects GH-600 orchestration concepts to simple repository examples.

## Sequence
1. **Planner Agent** breaks the request into safe, minimal tasks.
2. **Developer Agent** updates the code or documentation.
3. **Test Agent** runs targeted automated checks.
4. **Reviewer Agent** inspects the diff for correctness and safety.
5. **Human Approval** decides whether the output is ready to merge.

## Real-project usage
Production systems often add logging, retries, task queues, and policy gates between these stages.
