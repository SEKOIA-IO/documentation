import json
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from update_gitbook import update_doc


class GitBookGenerationTests(unittest.TestCase):
    def test_generate_includes_with_mixed_samples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "intakes"
            intake = source / "Example" / "example"
            metadata = intake / "_meta"
            metadata.mkdir(parents=True)
            (metadata / "manifest.yml").write_text(
                yaml.safe_dump({"uuid": "example", "name": "Example"})
            )
            tests = intake / "tests"
            tests.mkdir()
            for name, message in (("json", '{"value": 1}'), ("text", "raw log")):
                (tests / f"{name}.json").write_text(
                    json.dumps({"expected": {"message": message}})
                )

            destination = root / "documentation"
            update_doc(str(source), str(destination))
            includes = destination / "docs" / ".gitbook" / "includes" / "intakes"
            content = (includes / "example.md").read_text()
            samples = (includes / "example_sample.md").read_text()
            self.assertIn("#### `json.json`", content)
            self.assertIn("```json", samples)
            self.assertIn("```text\nraw log", samples)
            self.assertNotIn('=== "', content + samples)
            self.assertIn("intake-formats/tree/main/Example/example", content)

    def test_custom_section_without_parser_or_tests(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metadata = root / "intakes" / "Example" / "example" / "_meta"
            metadata.mkdir(parents=True)
            (metadata / "manifest.yml").write_text("uuid: example\n")
            update_doc(str(root / "intakes"), str(root / "output"), "section")
            includes = root / "output" / "section" / ".gitbook" / "includes" / "intakes"
            self.assertTrue((includes / "example.md").is_file())
            self.assertEqual((includes / "example_sample.md").read_text().strip(), "")


if __name__ == "__main__":
    unittest.main()