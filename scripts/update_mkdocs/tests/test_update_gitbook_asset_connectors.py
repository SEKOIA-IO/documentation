import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import update_gitbook_asset_connectors as generator  # noqa: E402

MAPPING = {
    "mapping": {
        "ocsf_class": "User Inventory Info",
        "class_uid": 5003,
        "ocsf_version": "1.6.0",
        "samples": [{"name": "Active user", "description": "A user", "data": '{\n  "id": "1"\n}\n'}],
        "fields": [
            {"source": "id", "target": "user.uid", "description": "Identifier", "type": "string", "logic": "Direct"}
        ],
        "ocsf_samples": [{"name": "OCSF user", "description": "Mapped user", "data": '{"uid": "1"}'}],
    }
}


def connector_config(name: str, capability: str) -> dict:
    return {"name": name, "type": "asset", "capability": capability}


def write_module(
    repository: Path, folder: str, slug: str, configs: dict, mappings: dict, asset_dir: str = "asset_connector"
) -> Path:
    """Create <repository>/<folder> with a manifest, the given configs and <type>_mapping.yml files."""
    module = repository / folder
    asset_path = module / slug.replace("-", "_") / asset_dir
    asset_path.mkdir(parents=True)
    (module / "manifest.json").write_text(json.dumps({"slug": slug, "name": folder}))
    for file_name, config in configs.items():
        (module / file_name).write_text(json.dumps(config))
    for asset_type, mapping in mappings.items():
        (asset_path / f"{asset_type}_mapping.yml").write_text(yaml.safe_dump(mapping))
    return module


class LoadAssetConnectorsTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.repository = Path(directory.name)

    def load(self) -> list:
        with redirect_stdout(io.StringIO()):
            return generator.load_asset_connectors(str(self.repository))

    def test_capabilities_map_to_asset_types(self):
        self.assertEqual(
            generator.CAPABILITY_TO_ASSET_TYPE,
            {
                "host_detection": "device",
                "account_detection": "user",
                "software_enrichment": "software",
                "vulnerability_enrichment": "vulnerability",
            },
        )

    def test_asset_type_comes_from_capability(self):
        write_module(
            self.repository,
            "HarfangLab",
            "harfanglab",
            {
                "connector_harfanglab_assets.json": connector_config("Harfanglab Devices", "host_detection"),
                "connector_harfanglab_software_assets.json": connector_config("Harfanglab Software", "software_enrichment"),
            },
            {"device": MAPPING, "software": MAPPING},
        )
        connectors = self.load()
        self.assertEqual([c["output_name"] for c in connectors], ["harfanglab_device.md", "harfanglab_software.md"])
        self.assertEqual([c["asset_type"] for c in connectors], ["device", "software"])

    def test_connector_fields(self):
        write_module(
            self.repository,
            "Okta",
            "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")},
            {"user": MAPPING},
            asset_dir="asset_connectors",
        )
        [connector] = self.load()
        self.assertEqual(
            connector,
            {
                "module_slug": "okta",
                "asset_type": "user",
                "config": connector_config("Okta Users", "account_detection"),
                "mapping": MAPPING["mapping"],
                "output_name": "okta_user.md",
            },
        )

    def test_unknown_capability_is_skipped(self):
        write_module(
            self.repository, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "unknown")}, {"user": MAPPING},
        )
        self.assertEqual(self.load(), [])

    def test_missing_mapping_is_skipped(self):
        write_module(
            self.repository, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")}, {"device": MAPPING},
        )
        self.assertEqual(self.load(), [])

    def test_duplicate_output_name_raises(self):
        write_module(
            self.repository, "Okta", "okta",
            {
                "connector_okta_device_assets.json": connector_config("Okta Devices", "host_detection"),
                "connector_okta_hosts_assets.json": connector_config("Okta Hosts", "host_detection"),
            },
            {"device": MAPPING},
        )
        with self.assertRaisesRegex(ValueError, "okta_device.md"):
            self.load()

    def test_empty_mapping_file_gives_empty_mapping(self):
        module = write_module(
            self.repository, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")}, {"user": MAPPING},
        )
        (module / "okta" / "asset_connector" / "user_mapping.yml").write_text("")
        [connector] = self.load()
        self.assertEqual(connector["mapping"], {})


def make_connector(mapping: dict, name: str = "Okta Users") -> dict:
    return {
        "module_slug": "okta",
        "asset_type": "user",
        "config": {"name": name},
        "mapping": mapping,
        "output_name": "okta_user.md",
    }


def front_matter(content: str) -> dict:
    _, header, _ = content.split("---\n", 2)
    return yaml.safe_load(header)


def table_rows(content: str) -> list:
    return [line for line in content.splitlines() if line.startswith("| `")]


class GenerateConnectorDocTests(unittest.TestCase):
    def render(self, mapping: dict = MAPPING["mapping"], name: str = "Okta Users") -> str:
        return generator.generate_connector_doc(make_connector(mapping, name))

    def test_escape_table_cell(self):
        self.assertEqual(generator.escape_table_cell(" a|b\nc \n"), "a\\|b<br/>c")
        self.assertEqual(generator.escape_table_cell(5003), "5003")

    def test_front_matter_has_title(self):
        content = self.render()
        self.assertTrue(content.startswith("---\n"))
        self.assertEqual(front_matter(content), {"title": "Okta Users OCSF mapping"})
        self.assertIn("---\n\n## OCSF Mapping for Okta Users\n", content)

    def test_title_with_yaml_special_characters(self):
        content = self.render(name='Foo: "Bar" #1')
        self.assertEqual(front_matter(content)["title"], 'Foo: "Bar" #1 OCSF mapping')

    def test_ocsf_header(self):
        content = self.render()
        self.assertIn("**OCSF Class:** `User Inventory Info`", content)
        self.assertIn("**Class UID:** `5003`", content)
        self.assertIn("**OCSF Version:** `1.6.0`", content)

    def test_ocsf_version_falls_back_to_version(self):
        mapping = {key: value for key, value in MAPPING["mapping"].items() if key != "ocsf_version"}
        self.assertIn("**OCSF Version:** `1.5.0`", self.render({**mapping, "version": "1.5.0"}))

    def test_table_cells_are_escaped(self):
        fields = [
            {
                "source": "a|b",
                "target": "x.type || x.type_id",
                "description": "line one\nline two\n",
                "type": "string",
                "logic": "Direct",
            }
        ]
        content = self.render({**MAPPING["mapping"], "fields": fields})
        self.assertIn("| `a\\|b` | `x.type \\|\\| x.type_id` | line one<br/>line two | `string` | Direct |", content)
        for row in table_rows(content):
            self.assertEqual(len(re.split(r"(?<!\\)\|", row)[1:-1]), 5, row)

    def test_missing_cell_values_render_as_dash(self):
        fields = [{"source": "id", "target": "user.uid", "type": None, "logic": None}]
        self.assertIn("| `id` | `user.uid` | - | `-` | - |", self.render({**MAPPING["mapping"], "fields": fields}))

    def test_samples_are_trimmed_code_blocks(self):
        self.assertIn('#### Active user\nA user\n\n```json\n{\n  "id": "1"\n}\n```\n', self.render())

    def test_sample_without_description_has_no_blank_line_run(self):
        mapping = {
            **MAPPING["mapping"],
            "samples": [{"name": "Bare", "data": "{}"}],
            "ocsf_samples": [{"name": "Bare OCSF", "description": "", "data": "{}"}],
        }
        content = self.render(mapping)
        self.assertIn("#### Bare\n\n```json\n{}\n```\n", content)
        self.assertIn("#### Bare OCSF\n\n```json\n{}\n```\n", content)
        self.assertNotIn("\n\n\n", content)

    def test_no_mkdocs_syntax_and_no_blank_line_runs(self):
        content = self.render()
        for marker in ("{!", "!!!", '=== "'):
            self.assertNotIn(marker, content)
        self.assertNotIn("\n\n\n", content)

    def test_empty_mapping_renders_headings_only(self):
        content = self.render({})
        self.assertIn("## OCSF Mapping for Okta Users\n\n## Information Collected\n", content)
        self.assertNotIn("###", content)
        self.assertNotIn("\n\n\n", content)


class WriteIncludesTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.includes = Path(directory.name) / "docs" / ".gitbook" / "includes" / "asset_connectors"

    def write(self, connectors: list) -> tuple:
        with redirect_stdout(io.StringIO()):
            return generator.write_includes(connectors, self.includes)

    def test_writes_blocks_and_prunes_stale_ones(self):
        self.includes.mkdir(parents=True)
        (self.includes / "old_device.md").write_text("stale")
        foreign = self.includes.parent / "restart-the-endpoint-agent.md"
        foreign.write_text("keep")
        connector = make_connector(MAPPING["mapping"])

        written, removed = self.write([connector])

        self.assertEqual((written, removed), (["okta_user.md"], ["old_device.md"]))
        self.assertEqual(sorted(path.name for path in self.includes.iterdir()), ["okta_user.md"])
        self.assertEqual(
            (self.includes / "okta_user.md").read_text(encoding="utf-8"), generator.generate_connector_doc(connector)
        )
        self.assertEqual(foreign.read_text(), "keep")

    def test_creates_missing_includes_folder(self):
        self.write([make_connector(MAPPING["mapping"])])
        self.assertTrue((self.includes / "okta_user.md").is_file())

    def test_non_markdown_files_are_not_pruned(self):
        self.includes.mkdir(parents=True)
        (self.includes / ".DS_Store").write_text("finder")
        _, removed = self.write([make_connector(MAPPING["mapping"])])
        self.assertEqual(removed, [])
        self.assertTrue((self.includes / ".DS_Store").is_file())


if __name__ == "__main__":
    unittest.main()
