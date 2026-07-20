# MCP Demonstration

## Why this folder exists
This folder shows where Model Context Protocol assets might live in a repository. It exists so GH-600 learners can see a concrete configuration example without exposing real infrastructure credentials.

## GH-600 concept demonstrated
- MCP server registration
- Filesystem server usage for local repository access
- GitHub server usage for repository metadata and automation context
- Safe use of placeholders instead of real secrets

## Files in this folder
- `mcp-config.json`: sample MCP client configuration with placeholder environment variables.

## How it would be used in a real project
A real project would load secrets from a secure environment, scope repository access tightly, and document which agents are allowed to call each server.
