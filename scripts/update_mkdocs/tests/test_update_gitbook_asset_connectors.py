import io
import json
import re
import shutil
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

    def load(self) -> tuple:
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
        connectors, duplicates = self.load()
        self.assertEqual(duplicates, [])
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
        [connector], _ = self.load()
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
        self.assertEqual(self.load(), ([], []))

    def test_missing_mapping_is_skipped(self):
        write_module(
            self.repository, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")}, {"device": MAPPING},
        )
        self.assertEqual(self.load(), ([], []))

    def test_duplicate_output_name_is_skipped_and_reported(self):
        write_module(
            self.repository, "Okta", "okta",
            {
                "connector_okta_device_assets.json": connector_config("Okta Devices", "host_detection"),
                "connector_okta_hosts_assets.json": connector_config("Okta Hosts", "host_detection"),
            },
            {"device": MAPPING},
        )
        connectors, duplicates = self.load()
        self.assertEqual([c["config"]["name"] for c in connectors], ["Okta Devices"])
        self.assertEqual(duplicates, ["okta_device.md (connector_okta_hosts_assets.json)"])

    def test_empty_mapping_file_gives_empty_mapping(self):
        module = write_module(
            self.repository, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")}, {"user": MAPPING},
        )
        (module / "okta" / "asset_connector" / "user_mapping.yml").write_text("")
        [connector], _ = self.load()
        self.assertEqual(connector["mapping"], {})

    def test_null_slug_falls_back_to_the_folder_name(self):
        for slug in (None, ""):
            with self.subTest(slug=slug):
                directory = tempfile.TemporaryDirectory()
                self.addCleanup(directory.cleanup)
                self.repository = Path(directory.name)
                module = write_module(
                    self.repository, "Okta", "okta",
                    {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")},
                    {"user": MAPPING},
                )
                (module / "manifest.json").write_text(json.dumps({"slug": slug, "name": "Okta"}))
                [connector], _ = self.load()
                self.assertEqual((connector["module_slug"], connector["output_name"]), ("okta", "okta_user.md"))


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

    def test_names_are_escaped(self):
        mapping = {
            **MAPPING["mapping"],
            "samples": [{"name": "Sample {% x %} <b>", "data": "{}"}],
            "ocsf_samples": [{"name": "OCSF {{ y }}", "data": "{}"}],
        }
        content = self.render(mapping, name="A {{x}} <b>")
        self.assertIn("## OCSF Mapping for A \\{\\{x}} \\<b>\n", content)
        self.assertIn("The A \\{\\{x}} \\<b> fetches", content)
        self.assertIn("#### Sample \\{% x %} \\<b>\n", content)
        self.assertIn("#### OCSF \\{\\{ y }}\n", content)

    def test_missing_connector_name_falls_back_to_the_slug(self):
        for config in ({"name": None}, {"name": ""}, {}):
            with self.subTest(config=config):
                content = generator.generate_connector_doc({**make_connector(MAPPING["mapping"]), "config": config})
                self.assertEqual(front_matter(content), {"title": "okta OCSF mapping"})
                self.assertIn("## OCSF Mapping for okta\n", content)
                self.assertIn("The okta fetches", content)
                self.assertNotIn("None", content)

    def test_ocsf_header(self):
        content = self.render()
        self.assertIn("**OCSF Class:** `User Inventory Info`", content)
        self.assertIn("**Class UID:** `5003`", content)
        self.assertIn("**OCSF Version:** `1.6.0`", content)
        self.assertIn("### API Response Examples", content)
        self.assertIn("### Data Mapping Table", content)
        self.assertIn("### OCSF Model Structure", content)
        self.assertIn('#### OCSF user\nMapped user\n\n```json\n{"uid": "1"}\n```\n', content)

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

    def test_angle_brackets_in_text_cells_are_escaped(self):
        fields = [
            {
                "source": "tags<0>",
                "target": "device.name",
                "description": "Port <port>\nsecond",
                "type": "string",
                "logic": "Format as 'AWS Account <OwnerId>'",
            }
        ]
        content = self.render({**MAPPING["mapping"], "fields": fields})
        self.assertIn(
            "| `tags<0>` | `device.name` | Port \\<port><br/>second | `string` | Format as 'AWS Account \\<OwnerId>' |",
            content,
        )

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

    def test_sample_description_is_trimmed_and_escaped(self):
        mapping = {
            **MAPPING["mapping"],
            "samples": [{"name": "Padded", "description": "Agent <agent_uid>\n", "data": "{}"}],
            "ocsf_samples": [{"name": "Blank", "description": "   ", "data": "{}"}],
        }
        content = self.render(mapping)
        self.assertIn("#### Padded\nAgent \\<agent_uid>\n\n```json\n{}\n```\n", content)
        self.assertIn("#### Blank\n\n```json\n{}\n```\n", content)
        self.assertNotIn("\n\n\n", content)

    def test_empty_sample_name_and_description_do_not_render_none(self):
        mapping = {
            **MAPPING["mapping"],
            "samples": [{"name": None, "description": None, "data": "{}"}],
            "ocsf_samples": [{"description": None, "data": "{}"}],
        }
        content = self.render(mapping)
        self.assertEqual(content.count("#### -\n\n```json\n{}\n```\n"), 2)
        self.assertNotIn("None", content)

    def test_non_string_sample_data_is_rendered_as_json(self):
        mapping = {**MAPPING["mapping"], "samples": [{"name": "Object", "data": {"a": 1, "b": "é"}}]}
        self.assertIn('#### Object\n\n```json\n{\n  "a": 1,\n  "b": "é"\n}\n```\n', self.render(mapping))

    def test_backticks_in_sample_data_get_a_longer_fence(self):
        mapping = {**MAPPING["mapping"], "samples": [{"name": "Fence", "data": '{"text": "a ``` b"}'}]}
        self.assertIn('#### Fence\n\n````json\n{"text": "a ``` b"}\n````\n', self.render(mapping))

    def test_backticks_in_inline_code_values_get_a_longer_delimiter(self):
        fields = [{"source": "a`b", "target": "`x`", "description": "-", "type": "string", "logic": "-"}]
        content = self.render({**MAPPING["mapping"], "ocsf_class": "A``B", "fields": fields})
        self.assertIn("| ``a`b`` | `` `x` `` | - | `string` | - |", content)
        self.assertIn("**OCSF Class:** ```A``B```", content)

    def test_gitbook_tags_in_text_are_escaped(self):
        fields = [
            {"source": "id", "target": "user.uid", "description": "Use {% hint %}", "type": "string", "logic": "{{ var }}"}
        ]
        mapping = {
            **MAPPING["mapping"],
            "samples": [{"name": "Tags", "description": "See {{ x }} and {% y %}", "data": "{}"}],
            "fields": fields,
        }
        content = self.render(mapping)
        self.assertIn("| `id` | `user.uid` | Use \\{% hint %} | `string` | \\{\\{ var }} |", content)
        self.assertIn("#### Tags\nSee \\{\\{ x }} and \\{% y %}\n", content)

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


PLAIN = "{!_shared_content/operations_center/integrations/generated_assets_documentation/okta_user.md!}"
ESCAPED = (
    "{!\\_shared\\_content/operations\\_center/integrations/generated\\_assets\\_documentation/okta\\_user.md!}"
)
OKTA_PAGE = "integration/assets_categories/user/okta_user.md"
OKTA_INCLUDE = '{% include "../../../.gitbook/includes/asset_connectors/okta_user.md" %}'
BROKEN = "broken asset connector includes, nothing written:"
OKTA_TARGET = "../../../.gitbook/includes/asset_connectors/okta_user.md"
GHOST_TARGET = "../../../.gitbook/includes/asset_connectors/ghost_device.md"


class RewritePageIncludesTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.section = Path(directory.name) / "docs"
        self.includes = self.section / ".gitbook" / "includes" / "asset_connectors"
        self.includes.mkdir(parents=True)
        (self.includes / "okta_user.md").write_text("block")

    def write_page(self, relative: str, content: str) -> Path:
        page = self.section / relative
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(content)
        return page

    def rewrite(self) -> tuple:
        blocks = {path.name for path in self.includes.glob("*.md")}
        changes, broken = generator.plan_page_includes(self.section, self.includes, blocks)
        for page, content in changes.items():
            page.write_text(content, encoding="utf-8")
        return list(changes), broken

    def test_plain_include_is_rewritten(self):
        page = self.write_page(OKTA_PAGE, f"# Okta\n\nIntro\n\n{PLAIN}\n\n## Further Reading\n")
        self.assertEqual(self.rewrite(), ([page], []))
        self.assertEqual(page.read_text(), f"# Okta\n\nIntro\n\n{OKTA_INCLUDE}\n\n## Further Reading\n")

    def test_escaped_include_is_rewritten(self):
        page = self.write_page(OKTA_PAGE, f"{ESCAPED}\n")
        self.rewrite()
        self.assertEqual(page.read_text(), f"{OKTA_INCLUDE}\n")

    def test_relative_path_follows_page_depth(self):
        top = self.write_page("okta.md", PLAIN)
        deep = self.write_page("a/b/c/okta.md", PLAIN)
        self.rewrite()
        self.assertEqual(top.read_text(), '{% include ".gitbook/includes/asset_connectors/okta_user.md" %}')
        self.assertEqual(deep.read_text(), '{% include "../../../.gitbook/includes/asset_connectors/okta_user.md" %}')

    def test_two_includes_in_one_page(self):
        (self.includes / "okta_device.md").write_text("block")
        page = self.write_page("integration/okta.md", f"{PLAIN}\n\ntext\n\n{PLAIN.replace('okta_user', 'okta_device')}\n")
        self.rewrite()
        self.assertEqual(
            page.read_text(),
            '{% include "../.gitbook/includes/asset_connectors/okta_user.md" %}\n\ntext\n\n'
            '{% include "../.gitbook/includes/asset_connectors/okta_device.md" %}\n',
        )

    def test_page_without_legacy_include_is_untouched(self):
        page = self.write_page("intro.md", "# Intro\n")
        self.assertEqual(self.rewrite(), ([], []))
        self.assertEqual(page.read_text(), "# Intro\n")

    def test_gitbook_folder_is_skipped(self):
        inside = self.section / ".gitbook" / "includes" / "other.md"
        inside.write_text(PLAIN)
        self.assertEqual(self.rewrite(), ([], []))
        self.assertEqual(inside.read_text(), PLAIN)

    def test_symlinked_page_is_skipped(self):
        target = self.section.parent / "shared.md"
        target.write_text(PLAIN)
        link = self.section / "integration" / "shared.md"
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target)
        self.assertEqual(self.rewrite(), ([], []))
        self.assertEqual(target.read_text(), PLAIN)

    def test_other_includes_are_untouched(self):
        other = "{!_shared_content/operations_center/integrations/generated/0a1b2c.md!}"
        page = self.write_page(OKTA_PAGE, f"{other}\n\n{PLAIN}\n")
        self.rewrite()
        self.assertEqual(page.read_text(), f"{other}\n\n{OKTA_INCLUDE}\n")

    def test_missing_block_is_reported(self):
        page = self.write_page("ghost.md", PLAIN.replace("okta_user", "ghost_device"))
        self.assertEqual(self.rewrite(), ([page], ["ghost.md -> .gitbook/includes/asset_connectors/ghost_device.md"]))
        self.assertEqual(page.read_text(), '{% include ".gitbook/includes/asset_connectors/ghost_device.md" %}')

    def test_dangling_gitbook_include_is_reported(self):
        self.write_page(OKTA_PAGE, OKTA_INCLUDE.replace("okta_user", "ghost_device"))
        self.assertEqual(self.rewrite(), ([], [f"{OKTA_PAGE} -> {GHOST_TARGET}"]))

    def test_moved_page_with_a_stale_path_is_reported(self):
        moved = "integration/assets_categories/user/archive/okta_user.md"
        self.write_page(moved, OKTA_INCLUDE)
        self.assertEqual(self.rewrite(), ([], [f"{moved} -> {OKTA_TARGET}"]))

    def test_include_without_inner_spaces_is_checked(self):
        self.write_page(OKTA_PAGE, f'{{%include "{GHOST_TARGET}"%}}')
        self.assertEqual(self.rewrite(), ([], [f"{OKTA_PAGE} -> {GHOST_TARGET}"]))

    def test_other_gitbook_includes_are_not_checked(self):
        self.write_page(OKTA_PAGE, '{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}')
        self.assertEqual(self.rewrite(), ([], []))

    def test_dangling_tag_next_to_a_legacy_include_is_reported(self):
        page = self.write_page(OKTA_PAGE, f"{OKTA_INCLUDE.replace('okta_user', 'ghost_device')}\n\n{PLAIN}\n")
        self.assertEqual(self.rewrite(), ([page], [f"{OKTA_PAGE} -> {GHOST_TARGET}"]))

    def test_second_run_changes_nothing(self):
        self.write_page(OKTA_PAGE, ESCAPED)
        self.rewrite()
        self.assertEqual(self.rewrite(), ([], []))


SCRIPT = Path(__file__).resolve().parents[1] / "update_gitbook_asset_connectors.py"


def snapshot(root: Path) -> dict:
    return {str(path.relative_to(root)): path.read_bytes() for path in sorted(root.rglob("*")) if path.is_file()}


class UpdateAssetDocTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.library = self.root / "automation-library"
        self.documentation = self.root / "documentation"
        write_module(
            self.library, "Okta", "okta",
            {"connector_okta_user_assets.json": connector_config("Okta Users", "account_detection")}, {"user": MAPPING},
        )
        self.page = self.documentation / "docs" / OKTA_PAGE
        self.page.parent.mkdir(parents=True)
        self.page.write_text(f"# Okta\n\n{PLAIN}\n")

    def run_generator(self, *args: str) -> tuple:
        output = io.StringIO()
        with redirect_stdout(output):
            problems = generator.update_asset_doc(str(self.library), str(self.documentation), *args)
        return output.getvalue(), problems

    def test_default_section_root_is_docs(self):
        self.assertEqual(generator.DEFAULT_SECTION_ROOT, "docs")
        output, problems = self.run_generator()
        self.assertEqual(problems, [])
        self.assertTrue((self.documentation / "docs" / generator.INCLUDES_SUBDIR / "okta_user.md").is_file())
        self.assertEqual(self.page.read_text(), f"# Okta\n\n{OKTA_INCLUDE}\n")
        self.assertIn("Generated 1 includes in docs/.gitbook/includes/asset_connectors (0 stale removed)", output)
        self.assertIn("Rewrote includes in 1 pages", output)
        self.assertNotIn("Error", output)

    def test_custom_section_root(self):
        poc_page = self.documentation / "docs" / "integration" / "assets_categories" / "device" / "okta_device.md"
        poc_page.parent.mkdir(parents=True)
        poc_page.write_text(ESCAPED)
        _, problems = self.run_generator("docs/integration")
        self.assertEqual(problems, [])
        includes = self.documentation / "docs" / "integration" / generator.INCLUDES_SUBDIR
        self.assertTrue((includes / "okta_user.md").is_file())
        self.assertEqual(poc_page.read_text(), '{% include "../../.gitbook/includes/asset_connectors/okta_user.md" %}')

    def test_documentation_path_with_dot_dot_is_accepted(self):
        (self.root / "x").mkdir()
        output = io.StringIO()
        with redirect_stdout(output):
            problems = generator.update_asset_doc(str(self.library), str(self.root / "x" / ".." / "documentation"))
        self.assertEqual(problems, [])
        self.assertEqual(self.page.read_text(), f"# Okta\n\n{OKTA_INCLUDE}\n")

    def test_missing_section_root_raises(self):
        with self.assertRaises(FileNotFoundError):
            self.run_generator("missing")
        self.assertFalse((self.documentation / "missing").exists())

    def test_no_connectors_raises_without_touching_anything(self):
        includes = self.documentation / "docs" / generator.INCLUDES_SUBDIR
        includes.mkdir(parents=True)
        (includes / "okta_user.md").write_text("existing")
        (self.root / "empty").mkdir()
        before = snapshot(self.documentation)
        with self.assertRaises(ValueError), redirect_stdout(io.StringIO()):
            generator.update_asset_doc(str(self.root / "empty"), str(self.documentation))
        self.assertEqual(snapshot(self.documentation), before)

    def test_second_run_is_a_no_op(self):
        self.run_generator()
        first = snapshot(self.documentation)
        output, _ = self.run_generator()
        self.assertEqual(snapshot(self.documentation), first)
        self.assertIn("Rewrote includes in 0 pages", output)

    def add_aws(self) -> Path:
        write_module(
            self.library, "AWS", "aws",
            {"connector_aws_device_assets.json": connector_config("AWS Devices", "host_detection")}, {"device": MAPPING},
        )
        page = self.documentation / "docs" / "integration" / "assets_categories" / "device" / "aws_device.md"
        page.parent.mkdir(parents=True)
        page.write_text(f"# AWS\n\n{PLAIN.replace('okta_user', 'aws_device')}\n")
        return page

    def test_missing_block_is_reported_as_a_problem(self):
        self.page.write_text(PLAIN.replace("okta_user", "ghost_device"))
        before = snapshot(self.documentation)
        output, problems = self.run_generator()
        self.assertEqual(problems, [f"{BROKEN} {OKTA_PAGE} -> {GHOST_TARGET}"])
        self.assertIn(f"Error: {BROKEN} {OKTA_PAGE} -> {GHOST_TARGET}", output)
        self.assertEqual(snapshot(self.documentation), before)

    def test_block_removed_after_the_rewrite_fails_and_changes_nothing(self):
        self.add_aws()
        self.assertEqual(self.run_generator()[1], [])
        shutil.rmtree(self.library / "Okta")
        before = snapshot(self.documentation)
        result = self.run_cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(f"Error: {BROKEN} {OKTA_PAGE} -> {OKTA_TARGET}", result.stdout)
        self.assertEqual(snapshot(self.documentation), before)

    def test_partial_checkout_on_the_first_run_writes_nothing(self):
        aws_page = self.add_aws()
        shutil.rmtree(self.library / "Okta")
        before = snapshot(self.documentation)
        _, problems = self.run_generator()
        self.assertEqual(problems, [f"{BROKEN} {OKTA_PAGE} -> {OKTA_TARGET}"])
        self.assertEqual(snapshot(self.documentation), before)
        self.assertIn(PLAIN.replace("okta_user", "aws_device"), aws_page.read_text())

    def test_duplicate_and_broken_include_are_both_reported_and_nothing_is_written(self):
        duplicate = connector_config("Okta Users bis", "account_detection")
        (self.library / "Okta" / "connector_okta_users_bis_assets.json").write_text(json.dumps(duplicate))
        self.page.write_text(PLAIN.replace("okta_user", "ghost_device"))
        before = snapshot(self.documentation)
        _, problems = self.run_generator()
        self.assertEqual(
            problems,
            [
                "duplicate asset connectors skipped: okta_user.md (connector_okta_users_bis_assets.json)",
                f"{BROKEN} {OKTA_PAGE} -> {GHOST_TARGET}",
            ],
        )
        self.assertEqual(snapshot(self.documentation), before)

    def test_duplicate_is_reported_and_the_other_connectors_are_written(self):
        duplicate = connector_config("Okta Users bis", "account_detection")
        (self.library / "Okta" / "connector_okta_users_bis_assets.json").write_text(json.dumps(duplicate))
        output, problems = self.run_generator()
        self.assertEqual(
            problems, ["duplicate asset connectors skipped: okta_user.md (connector_okta_users_bis_assets.json)"]
        )
        self.assertIn("Error: duplicate asset connectors skipped: okta_user.md", output)
        self.assertTrue(output.rstrip().splitlines()[-1].startswith("Error: duplicate asset connectors skipped:"))
        block = (self.documentation / "docs" / generator.INCLUDES_SUBDIR / "okta_user.md").read_text(encoding="utf-8")
        self.assertIn("## OCSF Mapping for Okta Users\n", block)
        self.assertEqual(self.page.read_text(), f"# Okta\n\n{OKTA_INCLUDE}\n")

    def run_cli(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.library), str(self.documentation)],
            cwd=self.root, capture_output=True, text=True,
        )

    def test_cli_runs_from_any_working_directory(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Rewrote includes in 1 pages", result.stdout)

    def test_cli_exits_non_zero_on_problems(self):
        self.page.write_text(PLAIN.replace("okta_user", "ghost_device"))
        result = self.run_cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(f"Error: {BROKEN} {OKTA_PAGE} -> {GHOST_TARGET}", result.stdout)


if __name__ == "__main__":
    unittest.main()
