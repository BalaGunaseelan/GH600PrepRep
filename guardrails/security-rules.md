# Security Guardrails

## Why this file exists
This file shows how security expectations can be written down for humans and agents. It supports GH-600 topics around safe automation and human escalation.

## Allowed actions
- Use placeholder values like `${GITHUB_TOKEN_PLACEHOLDER}` in examples.
- Keep permissions in workflows explicit and minimal.
- Run local validation that does not require private infrastructure.

## Denied actions
- Commit secrets or realistic access tokens.
- Request broader workflow permissions without a documented need.
- Call external systems that would leak repository content.

## Approval-required actions
- Storing new credentials in a secret manager
- Granting write access to production environments
- Using third-party services to process private repository data

## Real-project usage
Real repositories often pair these rules with secret scanning, dependency review, and incident response playbooks.
