from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_internal_markdown_links_exist(self):
        missing = []
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in __import__("re").findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                clean = target.split("#", 1)[0]
                if clean and not (path.parent / clean).resolve().exists():
                    missing.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual(missing, [])

    def test_issue_forms_are_valid_yaml(self):
        for path in (ROOT / ".github/ISSUE_TEMPLATE").glob("*.yml"):
            form = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIn("name", form)
            self.assertIsInstance(form.get("body"), list)
            self.assertTrue(form["body"])

    def test_expected_data_volume(self):
        papers = yaml.safe_load((ROOT / "data/papers.yaml").read_text(encoding="utf-8"))
        industry = yaml.safe_load((ROOT / "data/industry.yaml").read_text(encoding="utf-8"))
        self.assertEqual(len(papers), 28)
        self.assertGreaterEqual(len(industry), 7)
