# Chimera Agent Skills

This directory defines the skills available to the Chimera agent.
A skill represents a reusable, well-defined capability that the agent
can invoke at runtime.

Skills are defined by clear input and output contracts.
Implementation details may evolve, but interfaces must remain stable.

## Core Skills

### Skill: Fetch Trends
Description:
- Retrieves trending topics from external platforms.

Input:
```json
{
  "platform": "string",
  "region": "string"
}
