# file: README.md
# version: 1.0.0
# guid: 5b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e

# Update Action Docker Reference Action

GitHub Action to update `action.yml` files with new Docker image digests and versions.

## Purpose

This action solves the problem of updating action.yml files with digest-pinned Docker images. It replaces inline HEREDOC Python scripts with a proper reusable composite action.

## Usage

```yaml
- name: Update action.yml with new Docker image
  uses: jdfalk/update-action-docker-ref-action@v1
  with:
    action-file: action.yml
    image-name: ghcr.io/jdfalk/my-action
    image-tag: v1.2.3
    image-digest: sha256:abc123...
    version: 1.2.3
    action-name: my-action
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|-------|
| `action-file` | Path to action.yml file | No | `action.yml` |
| `image-name` | Docker image name (e.g., ghcr.io/jdfalk/my-action) | Yes | |
| `image-tag` | Docker image tag (e.g., v1.2.3) | Yes | |
| `image-digest` | Docker image digest (e.g., sha256:abc123...) | Yes | |
| `version` | Version number to update (without v prefix) | Yes | |
| `action-name` | Action name for pattern matching | Yes | |

## Outputs

| Output | Description |
|--------|-------------|
| `updated` | Whether the file was updated |

## Example: publish-docker.yml

Replace HEREDOC Python with this action:

```yaml
- name: Update action.yml
  uses: jdfalk/update-action-docker-ref-action@v1
  with:
    image-name: ${{ env.IMAGE_NAME }}
    image-tag: ${{ env.IMAGE_TAG }}
    image-digest: ${{ steps.build.outputs.digest }}
    version: ${{ env.VERSION_NO_PREFIX }}
    action-name: my-action
```

## Development

This is a composite action that runs a Python script.

### Testing

Test locally with:

```bash
export ACTION_FILE="action.yml"
export IMAGE_NAME="ghcr.io/jdfalk/test-action"
export IMAGE_TAG="v1.0.0"
export IMAGE_DIGEST="sha256:abc123"
export VERSION="1.0.0"
export ACTION_NAME="test-action"
python3 src/update_docker_ref.py
```

## License

MIT
