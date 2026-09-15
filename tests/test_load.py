from pathlib import Path

import pytest

from awesome_cl.load import load_yaml_list


def test_loads_list(tmp_path: Path):
    source = tmp_path / "items.yaml"
    source.write_text("- id: one\n", encoding="utf-8")
    assert load_yaml_list(source) == [{"id": "one"}]


def test_rejects_mapping_root(tmp_path: Path):
    source = tmp_path / "items.yaml"
    source.write_text("id: one\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_yaml_list(source)
