# Human Approval Process

## Why this file exists
This file demonstrates how a repository can describe the moments when automation must pause for a person. GH-600 learners should expect human-in-the-loop design to be explicit.

## When agent must stop
- When a request needs real credentials or production access
- When workflow permissions need to expand beyond documented examples
- When legal, compliance, or security interpretation is required

## When human approval is required
- Before merging changes that alter guardrails
- Before enabling write actions against external systems
- Before accepting benchmark failures as known risk

## Real-project usage
Real approval processes often name approvers, service owners, and evidence required before work can proceed.
