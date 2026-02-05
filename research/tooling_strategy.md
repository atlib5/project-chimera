# Tooling Strategy – Project Chimera

## Developer Tools (MCP)

These tools are used during development to support productivity,
traceability, and governance. They are not part of the runtime agent.

### Selected MCP Tools

#### Git MCP
Purpose:
- Track code changes
- Maintain clean commit history
- Support collaboration and rollback

#### Filesystem MCP
Purpose:
- Create and modify project files
- Ensure consistent file structure
- Enable traceability of changes

#### MCP Sense
Purpose:
- Capture development telemetry
- Provide traceability into agent and developer actions
- Act as a “black box” recorder for the project

## Rationale
Separating developer tools from runtime agent skills ensures
clear boundaries between human-driven development and
autonomous agent execution.
