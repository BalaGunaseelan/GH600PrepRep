# Evaluation Success Criteria

## Why this file exists
This file states what success looks like for the educational repository. It demonstrates that agents and humans need the same clear acceptance targets.

## Pass criteria
- The Python app prints `Hello GH-600`.
- At least one automated unit test validates the app.
- Every required educational folder exists.
- Example workflows include triggers, permissions, jobs, steps, and artifact uploads.
- Example configs use placeholders instead of real secrets.

## Fail criteria
- Missing required artifacts
- Broken imports or failing tests
- Workflows without explicit permissions
- Any committed credential or realistic token

## Real-project usage
In a production system, these criteria would be tighter and often mapped to release gates or service-level objectives.
