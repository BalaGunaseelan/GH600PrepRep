# Human Escalation Process

## Why this file exists
This file explains how an agent hands work back to a human when confidence or authority is insufficient. It demonstrates a core GH-600 safety pattern.

## Escalation flow
1. Stop automated changes.
2. Summarize the blocked task and the reason for escalation.
3. Cite the relevant guardrail, security, or compliance concern.
4. Request a human decision before continuing.

## Example escalation cases
- A user asks for a live GitHub token in sample configuration.
- A workflow needs deployment credentials that are not available.
- Evaluation results suggest unsafe behavior that needs policy interpretation.

## Real-project usage
Real escalation playbooks usually define response times, owners, incident channels, and audit requirements.
