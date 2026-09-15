"""YAML loading helpers."""

from pathlib import Path
from typing import Any

import yaml


def load_yaml_list(path: str | Path) -> list[dict[str, Any]]:
    """Load a YAML document whose root must be a list of mappings."""
    source = Path(path)
    with source.open(encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{source}: expected a list of mappings")
    return value
