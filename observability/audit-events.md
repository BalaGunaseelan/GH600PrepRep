# Audit Events Demonstration

## Why this file exists
This file demonstrates the type of audit trail humans often need when agents can modify repository content. GH-600 learners should see auditability as a first-class concern.

## Example audit events
- Agent started with task scope and timestamp
- Files modified during execution
- Validation commands executed
- Human approval requested or granted

## Real-project usage
A real audit trail would include immutable identifiers, actor identities, policy decisions, and retention expectations.
