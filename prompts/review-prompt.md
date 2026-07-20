# Review Prompt Template

## Why this file exists
This prompt shows how a repository can standardize review requests for humans or agents. GH-600 learners should see prompt libraries as first-class artifacts.

## Template
```text
Review the proposed changes for correctness, safety, and alignment with repository documentation.
Focus areas:
- Functional regressions
- Security or secret exposure
- Mismatches between docs and implementation
Ignore:
- Pure style preferences unless they hide a defect
Return:
- Findings ordered by severity
- File references
- Any required human escalation
```

## Best practices
- Ask for prioritized findings.
- Limit the review scope to the actual change.
- Define what the reviewer should ignore to reduce noise.
- Require evidence for every concern.

## Real-project usage
Real teams often customize review prompts for security, performance, or compliance-sensitive components.
