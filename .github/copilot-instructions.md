<!-- file: .github/copilot-instructions.md -->
<!-- version: 1.0.0 -->
<!-- guid: 9f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c -->

# AI Agent Instructions (Standard)

- Use VS Code tasks for non-git operations; prefer MCP GitHub tools for git operations.
- Commits must use conventional commits (type(scope): description).
- Include versioned headers in docs/configs and bump versions on changes.
- This is a composite GitHub Action with Python script in src/ directory.
- All changes to update logic should be made in src/update_docker_ref.py.
- Follow GitHub Actions composite action best practices.
- Provide concise plans and progress updates.

## Repository Context

This repository provides a composite GitHub Action that updates action.yml files with Docker image digests.

**Key Files:**

- [action.yml](action.yml) - Main composite action definition
- [src/update_docker_ref.py](src/update_docker_ref.py) - Python script for updating files
- [README.md](README.md) - Comprehensive documentation and examples
- [CHANGELOG.md](CHANGELOG.md) - Version history

**Update Logic:**

- Updates version comment in action.yml
- Updates docker-image default value with digest-pinned reference
- Uses regex patterns for precise replacements
- Outputs GitHub Actions output for workflow integration

**Design Pattern:**

- Composite action using shell to run Python script
- Python script in src/ directory (no HEREDOC)
- All environment variables passed as action inputs
- Outputs exposed via GitHub Actions output commands
