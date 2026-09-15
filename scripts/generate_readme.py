#!/usr/bin/env python3
"""Generate managed README sections from YAML data."""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from awesome_cl.load import load_yaml_list  # noqa: E402
from awesome_cl.render import render_readme  # noqa: E402
from awesome_cl.validate import validate_all  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated README files are stale")
    args = parser.parse_args()
    errors = validate_all(ROOT)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    taxonomy = load_yaml_list(ROOT / "data/taxonomy.yaml")
    papers = load_yaml_list(ROOT / "data/papers.yaml")
    industry = load_yaml_list(ROOT / "data/industry.yaml")
    stale: list[str] = []
    for filename, language in (("README.md", "en"), ("README.zh-CN.md", "zh")):
        path = ROOT / filename
        current = path.read_text(encoding="utf-8")
        generated = render_readme(current, papers, industry, taxonomy, language)
        if generated != current:
            stale.append(filename)
            if not args.check:
                path.write_text(generated, encoding="utf-8")
    if args.check and stale:
        print(f"Generated files are stale: {', '.join(stale)}")
        return 1
    print("README generation check passed." if args.check else "README files generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
