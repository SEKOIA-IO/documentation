"""Usage: python3 update_gitbook_asset_connectors.py /path/to/automation-library /path/to/documentation [--section-root docs]"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SECTION_ROOT = "docs"
INCLUDES_SUBDIR = Path(".gitbook") / "includes" / "asset_connectors"

CAPABILITY_TO_ASSET_TYPE = {
    "host_detection": "device",
    "account_detection": "user",
    "software_enrichment": "software",
    "vulnerability_enrichment": "vulnerability",
}

LEGACY_INCLUDE_PATTERN = re.compile(r"\{!(?:[^!\n]*/)?generated\\?_assets\\?_documentation/(?P<name>[^!/\n]+\.md)!\}")


def find_asset_connectors_folder(module_path: Path) -> Path | None:
    excluded_dirs = {".venv", "venv", "tests", "__pycache__", ".git", "node_modules", ".mypy_cache", ".github"}

    for folder_name in ["asset_connector", "asset_connectors"]:
        for path in module_path.rglob(folder_name):
            if path.is_dir():
                parts = path.relative_to(module_path).parts
                if not any(part in excluded_dirs for part in parts):
                    return path
    return None


def get_asset_type(connector_config: Dict) -> str | None:
    return CAPABILITY_TO_ASSET_TYPE.get(connector_config.get("capability"))


def load_asset_connectors(automation_module_repository: str) -> List[Dict]:
    asset_connectors: List[Dict] = []
    seen_output_names = set()

    for module_path in sorted(Path(automation_module_repository).iterdir()):
        if not module_path.is_dir() or module_path.name.startswith((".", "_")):
            continue

        manifest_path = module_path / "manifest.json"
        if not manifest_path.exists():
            continue

        with open(manifest_path, "r", encoding="utf-8") as fd:
            module_manifest = json.load(fd)

        module_slug = module_manifest.get("slug", module_path.name.lower())

        asset_connector_path = find_asset_connectors_folder(module_path)
        if not asset_connector_path:
            continue

        print(f"Module {module_slug}: found asset_connectors at {asset_connector_path.relative_to(module_path)}")

        for config_file in sorted(module_path.glob("*_assets.json")):
            with open(config_file, "r", encoding="utf-8") as fd:
                connector_config = json.load(fd)

            asset_type = get_asset_type(connector_config)
            if not asset_type:
                print(f"  - Skipping config {config_file.name}: unknown capability {connector_config.get('capability')!r}")
                continue

            mapping_file = asset_connector_path / f"{asset_type}_mapping.yml"
            if not mapping_file.exists():
                print(f"  - Skipping {module_slug}/{asset_type}: no mapping file")
                continue

            with open(mapping_file, "r", encoding="utf-8") as fd:
                mapping = (yaml.safe_load(fd) or {}).get("mapping") or {}

            output_name = f"{module_slug}_{asset_type}.md"
            if output_name in seen_output_names:
                raise ValueError(f"Duplicate asset connector documentation: {output_name} ({config_file})")
            seen_output_names.add(output_name)

            asset_connectors.append(
                {
                    "module_slug": module_slug,
                    "asset_type": asset_type,
                    "config": connector_config,
                    "mapping": mapping,
                    "output_name": output_name,
                }
            )
            print(f"  - Found: {module_slug} ({asset_type})")

    return asset_connectors


def escape_table_cell(value) -> str:
    return str(value).strip().replace("|", "\\|").replace("\n", "<br/>")


def escape_markdown_text(value) -> str:
    return str(value).replace("<", "\\<")


def generate_connector_doc(connector: Dict) -> str:
    config = connector["config"]
    module_slug = connector["module_slug"]

    env = Environment(loader=FileSystemLoader(SCRIPT_DIR / "templates"), trim_blocks=True, lstrip_blocks=True)
    env.filters["table_cell"] = escape_table_cell
    env.filters["markdown_text"] = escape_markdown_text
    body = env.get_template("asset_connector_gitbook.md.jinja").render(
        config=config,
        mapping=connector["mapping"],
        module_slug=module_slug,
        asset_type=connector["asset_type"],
    )

    front_matter = yaml.safe_dump(
        {"title": f"{config.get('name', module_slug)} OCSF mapping"}, sort_keys=False, allow_unicode=True, width=1000
    )
    return "---\n" + front_matter + "---\n\n" + body


def write_includes(connectors: List[Dict], includes_path: Path) -> Tuple[List[str], List[str]]:
    includes_path.mkdir(parents=True, exist_ok=True)

    written: List[str] = []
    for connector in connectors:
        (includes_path / connector["output_name"]).write_text(generate_connector_doc(connector), encoding="utf-8")
        written.append(connector["output_name"])
        print(f"Generated {connector['output_name']}")

    removed: List[str] = []
    for stale_file in sorted(includes_path.glob("*.md")):
        if stale_file.name not in written:
            stale_file.unlink()
            removed.append(stale_file.name)
            print(f"Removed stale {stale_file.name}")

    return written, removed


def rewrite_page_includes(section_path: Path, includes_path: Path) -> Tuple[List[Path], List[str]]:
    rewritten: List[Path] = []
    missing = set()

    for page in sorted(section_path.rglob("*.md")):
        if page.is_symlink():
            continue
        if ".gitbook" in page.relative_to(section_path).parts:
            continue

        def replace_include(match: re.Match) -> str:
            name = match["name"].replace("\\_", "_")
            if not (includes_path / name).exists():
                missing.add(name)
            path = Path(os.path.relpath(includes_path / name, page.parent)).as_posix()
            return f'{{% include "{path}" %}}'

        content = page.read_text(encoding="utf-8")
        new_content = LEGACY_INCLUDE_PATTERN.sub(replace_include, content)
        if new_content != content:
            page.write_text(new_content, encoding="utf-8")
            rewritten.append(page)
            print(f"Rewrote includes in {page.relative_to(section_path).as_posix()}")

    return rewritten, sorted(missing)


def update_asset_doc(
    connectors_repository: str, documentation_repository: str, section_root: str = DEFAULT_SECTION_ROOT
) -> None:
    section_path = Path(documentation_repository) / section_root
    if not section_path.is_dir():
        raise FileNotFoundError(f"GitBook section root not found: {section_path}")

    connectors = load_asset_connectors(connectors_repository)
    if not connectors:
        raise ValueError(f"No asset connectors found in {connectors_repository}")

    includes_path = section_path / INCLUDES_SUBDIR
    written, removed = write_includes(connectors, includes_path)
    pages, missing = rewrite_page_includes(section_path, includes_path)

    location = includes_path.relative_to(documentation_repository)
    print(f"Generated {len(written)} includes in {location} ({len(removed)} stale removed)")
    print(f"Rewrote includes in {len(pages)} pages")
    if missing:
        print(f"Warning: pages reference missing includes: {', '.join(missing)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update GitBook reusable content for asset connectors")
    parser.add_argument("connectors_repository", help="Path to the automation-library repository")
    parser.add_argument("documentation_repository", help="Path to the documentation repository")
    parser.add_argument(
        "--section-root",
        default=DEFAULT_SECTION_ROOT,
        help="GitBook space root relative to the documentation repository",
    )

    args = parser.parse_args()
    update_asset_doc(
        connectors_repository=args.connectors_repository,
        documentation_repository=args.documentation_repository,
        section_root=args.section_root,
    )
