#!/usr/bin/env python3
"""Validate all structured data files."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from awesome_cl.validate import validate_all  # noqa: E402

errors = validate_all(ROOT)
if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    raise SystemExit(1)
print("Data validation passed.")
