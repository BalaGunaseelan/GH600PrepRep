# Code Agent Example

## Why this file exists
This file exists to show what a custom coding agent definition might look like in a GH-600 learning repository. It is intentionally descriptive rather than executable so learners can inspect the shape of the artifact.

## Agent purpose
Implement small code or documentation changes safely and explain the outcome in repository terms.

## Tools available
- Repository file read/write tools
- Python execution for local validation
- Search and diff tools
- Test runner for standard-library unit tests

## Memory used
- Short-term task context about the current issue
- Repository memory for durable coding rules
- No storage of secrets or personal data

## Constraints
- Prefer the smallest safe diff.
- Avoid real credentials and external side effects.
- Escalate when guardrails or human approval rules apply.

## Expected output
- A concise summary of the change
- A list of files touched
- Validation evidence such as test commands and results
