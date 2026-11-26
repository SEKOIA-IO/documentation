#!/usr/bin/env python3
"""
Usage: python3 update_gitbook.py /path/to/repository/intake-formats /path/to/repository/documentation
"""

import argparse
import re
from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader

from intake_common import load_intakes

SCRIPT_DIR = Path(__file__).resolve().parent


def _escape_markdown_table_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br/>")


def _escape_tab_title(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def _build_code_block(content: str, language: str) -> str:
    longest_run = max((len(run) for run in re.findall(r"`+", content)), default=0)
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}{language}\n{content}\n{fence}"


def _prepare_intake(intake: dict) -> dict:
    prepared = dict(intake)
    data_sources = intake["manifest"].get("data_sources", {})
    if not isinstance(data_sources, dict):
        data_sources = {}
    prepared["data_sources"] = [
        {
            "name": _escape_markdown_table_cell(name),
            "description": _escape_markdown_table_cell(description),
        }
        for name, description in data_sources.items()
    ]
    prepared["parser"] = {
        **intake["parser"],
        "fields": [
            {
                **field,
                "name": _escape_markdown_table_cell(field["name"]),
                "type": _escape_markdown_table_cell(field["type"]),
                "short": _escape_markdown_table_cell(field["short"]),
            }
            for field in intake["parser"].get("fields", [])
        ],
    }
    prepared["tests"] = [
        {
            **test,
            "tab_title": _escape_tab_title(test["name"]),
            "rendered_content": _build_code_block(test["content"], "json"),
        }
        for test in intake["tests"]
    ]
    prepared["samples"] = [
        {
            **sample,
            "tab_title": _escape_tab_title(sample["name"]),
            "rendered_content": _build_code_block(
                sample["content"], "json" if sample["is_json"] else "text"
            ),
        }
        for sample in intake["samples"]
    ]
    return prepared


def generate_intake_doc(intake: dict) -> str:
    file_loader = FileSystemLoader(SCRIPT_DIR / "templates")
    env = Environment(loader=file_loader)

    template = env.get_template("intake_gitbook.md.jinja")
    return template.render(
        manifest=intake["manifest"],
        fields=intake["fields"],
        parser=intake["parser"],
        tests=intake["tests"],
        data_sources=intake["data_sources"],
        repo_path=intake["repo_path"],
    )

# Samples doc generation

def generate_sample_intake_doc(intake: dict) -> str:
    file_loader = FileSystemLoader(SCRIPT_DIR / "templates")
    env = Environment(loader=file_loader)

    template = env.get_template("sample_gitbook.md.jinja")
    return template.render(
        samples=intake["samples"],
    )


def _resolve_section_root(
    documentation_repository: str, section_root: Optional[str]
) -> str:
    if section_root:
        return section_root

    config_path = Path(documentation_repository) / ".gitbook.yaml"
    if not config_path.exists():
        return "docs"

    with open(config_path, "r", encoding="utf-8") as fd:
        config = yaml.safe_load(fd) or {}

    root = config.get("root")
    if not isinstance(root, str) or not root.strip():
        raise ValueError(f"Missing or invalid 'root' in {config_path}")
    return root


def update_doc(
    intake_repository: str, documentation_repository: str, section_root: Optional[str] = None
):
    resolved_section_root = _resolve_section_root(documentation_repository, section_root)
    doc_path = Path(documentation_repository) / resolved_section_root
    output_path = doc_path / ".gitbook" / "includes" / "intakes"

    # load intakes
    intakes = load_intakes(intake_repository, SCRIPT_DIR, ensure_ascii=False)
    output_path.mkdir(parents=True, exist_ok=True)
    for stale_file in output_path.glob("*.md"):
        stale_file.unlink()

    # produce intake documentation
    for intake in intakes:
        prepared_intake = _prepare_intake(intake)
        intake_content = generate_intake_doc(prepared_intake)
        sample_content = generate_sample_intake_doc(prepared_intake)

        generated_intake_file_path = (
            output_path
            / f"{intake['manifest']['uuid']}.md"
        )
        
        generated_samples_file_path = (
            output_path
            / f"{intake['manifest']['uuid']}_sample.md"
        )
        
        with open(generated_intake_file_path, "w", encoding="utf-8") as fd:
            fd.write(intake_content)
        with open(generated_samples_file_path, "w", encoding="utf-8") as fd:
            fd.write(sample_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update GitBook intake includes"
    )
    parser.add_argument(
        "intake_repository", help="Path to the intake format repository"
    )
    parser.add_argument(
        "documentation_repository", help="Path to the documentation repository"
    )
    parser.add_argument(
        "--section-root",
        default=None,
        help="GitBook section root relative to the documentation repository",
    )

    args = parser.parse_args()
    update_doc(
        intake_repository=args.intake_repository,
        documentation_repository=args.documentation_repository,
        section_root=args.section_root,
    )
