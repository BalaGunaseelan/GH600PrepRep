# Debugging Prompt Template

## Why this file exists
This file demonstrates a debugging-oriented prompt asset. It highlights the GH-600 idea that prompt libraries can separate investigation behavior from coding behavior.

## Template
```text
Investigate the following failure without making assumptions.
Symptom: <paste the failing output>
Known context:
- Relevant files: <paths>
- Recent changes: <summary>
- Constraints: do not use secrets or external systems
Deliver:
- Likely root cause
- Minimal fix options
- Validation steps
- Escalation recommendation if confidence is low
```

## Best practices
- Provide the raw error text.
- Include the smallest set of relevant files.
- Ask for multiple fix options when the cause is uncertain.
- Request a confidence rating to support human review.

## Real-project usage
Production debugging prompts might add logs, traces, incident IDs, and rollback constraints.
