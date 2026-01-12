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

    # Update version comment
    content = re.sub(
        r"^# version: .*$",
        f"# version: {version}",
        content,
        flags=re.MULTILINE,
    )

    # Update docker-image default value
    # Pattern: default: "ghcr.io/jdfalk/{action-name}@sha256:..."
    new_image_ref = f"{image_name}@{image_digest}"
    content = re.sub(
        rf'(docker-image:.*?default:\s*")[^"]+(")'