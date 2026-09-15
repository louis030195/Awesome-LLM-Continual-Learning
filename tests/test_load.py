from pathlib import Path
import tempfile
import unittest

from awesome_cl.load import load_yaml_list


class LoadTests(unittest.TestCase):
    def test_loads_list(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "items.yaml"
            source.write_text("- id: one\n", encoding="utf-8")
            self.assertEqual(load_yaml_list(source), [{"id": "one"}])

    def test_rejects_mapping_root(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "items.yaml"
            source.write_text("id: one\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_yaml_list(source)
