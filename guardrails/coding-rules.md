# Coding Guardrails

## Why this file exists
This file demonstrates repository-level guardrails that constrain coding agents. GH-600 learners should see that guardrails are explicit artifacts, not hidden assumptions.

## Allowed actions
- Update the tiny Python application when requirements change.
- Add or revise repository documentation that improves the learning experience.
- Create or adjust sample workflows, prompts, and templates.

## Denied actions
- Add real credentials, tokens, or private URLs.
- Introduce production-only complexity that hides the core lesson.
- Modify unrelated files without a clear educational reason.

## Approval-required actions
- Adding external dependencies
- Changing ownership or approval rules
- Replacing placeholder examples with organization-specific policy

## Real-project usage
Production coding guardrails usually include architectural boundaries, dependency policies, and release-safety requirements.
