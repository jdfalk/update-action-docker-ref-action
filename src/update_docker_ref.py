#!/usr/bin/env python3
# file: src/update_docker_ref.py
# version: 1.0.0
# guid: 4a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d

"""Update action.yml with new Docker image digest and version."""

import os
import re
import sys
from pathlib import Path


def update_docker_ref() -> int:
    """Update action.yml with Docker image references.

    Returns:
        0 on success, 1 on error.
    """
    action_file = Path(os.environ["ACTION_FILE"])
    image_name = os.environ["IMAGE_NAME"]
    image_tag = os.environ["IMAGE_TAG"]
    image_digest = os.environ["IMAGE_DIGEST"]
    version = os.environ["VERSION"]
    action_name = os.environ["ACTION_NAME"]

    if not action_file.exists():
        print(f"Error: {action_file} not found", file=sys.stderr)
        return 1

    content = action_file.read_text()

    # Build the full image reference with digest
    image_ref = f"{image_name}:{image_tag}@{image_digest}"

    # Update version comment (first occurrence only)
    content = re.sub(
        r"# version: [0-9]+\.[0-9]+\.[0-9]+",
        f"# version: {version}",
        content,
        count=1,
    )

    # Update docker-image default value
    # Pattern: default: "ghcr.io/jdfalk/{action-name}:..."
    content = re.sub(
        rf'default:\s*"ghcr\.io/jdfalk/{re.escape(action_name)}:[^"]+"',
        f'default: "{image_ref}"',
        content,
        count=1,
    )

    # Write updated content
    action_file.write_text(content)

    # Output for GitHub Actions
    print("::set-output name=updated::true")
    print(f"Updated {action_file} with {image_ref}")

    return 0


if __name__ == "__main__":
    sys.exit(update_docker_ref())
