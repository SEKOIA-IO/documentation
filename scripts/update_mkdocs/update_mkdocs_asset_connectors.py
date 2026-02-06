import argparse
import json
from pathlib import Path
from typing import Dict, List

import yaml
from jinja2 import Environment, FileSystemLoader

ASSET_TYPES = ["device", "user", "vulnerability"]


def load_asset_connectors(automation_module_repository: str) -> List[Dict]:
    asset_connectors: List[Dict] = []

    for module_path in Path(automation_module_repository).iterdir():
        if not module_path.is_dir() or module_path.name.startswith((".", "_")):
            continue

        manifest_path = module_path / "manifest.json"
        if not manifest_path.exists():
            continue

        with open(manifest_path, "r") as fd:
            module_manifest = json.load(fd)

        module_slug = module_manifest.get("slug", module_path.name.lower())

        sub_module_path = module_path / module_slug
        if not sub_module_path.exists():
            continue

        asset_connector_path = sub_module_path / "asset_connectors"
        if not asset_connector_path.exists():
            continue

        for config_file in module_path.glob("*_asset_connector.json"):
            config_name = config_file.stem
            asset_type = None
            for type in ASSET_TYPES:
                if f"_{type}_asset_connector" in config_name:
                    asset_type = type
                    break

            if not asset_type:
                print(f"Skipping config {config_file.name}: unknown asset type")
                continue

            with open(config_file, "r") as fd:
                connector_config = json.load(fd)

            mapping_file = asset_connector_path / f"{asset_type}_mapping.yml"
            if not mapping_file.exists():
                print(f"Skipping {module_slug}/{asset_type}: no mapping file")
                continue

            with open(mapping_file, "r") as fd:
                mapping = yaml.safe_load(fd) or {}

            connector = {
                "module_name": module_path.name,
                "module_slug": module_slug,
                "module_manifest": module_manifest,
                "asset_type": asset_type,
                "config": connector_config,
                "mapping": mapping,
            }

            asset_connectors.append(connector)
            print(f"Found: {module_slug} ({asset_type})")

    return asset_connectors


def generate_connector_doc(connector: Dict) -> str:
    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    template = env.get_template("asset_connector.md.jinja")
    return template.render(
        module_manifest=connector["module_manifest"],
        asset_type=connector["asset_type"],
        config=connector["config"],
        mapping=connector["mapping"],
        module_slug=connector["module_slug"],
    )


def update_asset_doc(connectors_repository: str, documentation_repository: str):
    doc_path = Path(documentation_repository)

    output_dir = (
        doc_path
        / "_shared_content"
        / "operations_center"
        / "integrations"
        / "generated_assets_documentation"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    connectors = load_asset_connectors(connectors_repository)

    print(f"\nFound {len(connectors)} asset connectors")

    for connector in connectors:
        content = generate_connector_doc(connector)

        output_file = output_dir / f"{connector['module_slug']}_{connector['asset_type']}.md"

        with open(output_file, "w") as fd:
            fd.write(content)

        print(f"Generated: {output_file.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update documentation for asset connectors"
    )
    parser.add_argument(
        "connectors_repository", help="Path to the automation-module repository"
    )
    parser.add_argument(
        "documentation_repository", help="Path to the documentation repository"
    )

    args = parser.parse_args()
    update_asset_doc(
        connectors_repository=args.connectors_repository,
        documentation_repository=args.documentation_repository,
    )
