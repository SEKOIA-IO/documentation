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


if __name__ == "__main__":
    unittest.main()
