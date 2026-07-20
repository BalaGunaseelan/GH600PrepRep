# Coding Prompt Template

## Why this file exists
This prompt template demonstrates how repositories can keep reusable prompt assets under version control. It supports GH-600 topics around prompt quality, repeatability, and context packaging.

## Template
```text
You are the coding agent for this repository.
Task: <describe the smallest safe change>
Context:
- Application area: <file or module>
- Guardrails to respect: <relevant rules>
- Tests to run: <commands>
Expected output:
- Summary of change
- Files modified
- Validation performed
```

## Best practices
- State the task in a single sentence first.
- Include relevant files, not the entire repository.
- Tell the agent which guardrails are mandatory.
- Ask for validation evidence, not just a completion claim.

## Real-project usage
In a production repository, this template would be tailored with architecture links, service ownership, and deployment constraints.
