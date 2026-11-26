#!/usr/bin/env python3
"""
Usage: python3 update_mkdocs.py /path/to/repository/intake-formats /path/to/repository/documentation
"""

import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from intake_common import load_intakes

SCRIPT_DIR = Path(__file__).resolve().parent


def generate_intake_doc(intake: dict) -> str:
    file_loader = FileSystemLoader(SCRIPT_DIR / "templates")
    env = Environment(loader=file_loader)

    template = env.get_template("intake.md.jinja")
    return template.render(
        manifest=intake["manifest"],
        fields=intake["fields"],
        parser=intake["parser"],
        tests=intake["tests"],
        repo_path=intake["repo_path"],
    )

# Samples doc generation

def generate_sample_intake_doc(intake: dict) -> str:
    file_loader = FileSystemLoader(SCRIPT_DIR / "templates")
    env = Environment(loader=file_loader)

    template = env.get_template("sample.md.jinja")
    return template.render(
        manifest=intake["manifest"],
        fields=intake["fields"],
        parser=intake["parser"],
        samples=intake["samples"],
        repo_path=intake["repo_path"],
    )

def update_doc(intake_repository: str, documentation_repository: str):

    doc_path = Path(documentation_repository)

    # load intakes
    intakes = load_intakes(intake_repository, SCRIPT_DIR)

    # produce intake documentation
    for intake in intakes:
        intake_content = generate_intake_doc(intake)
        sample_content = generate_sample_intake_doc(intake)

        generated_intake_file_path = (
            doc_path
            / "_shared_content"
            / "operations_center"
            / "integrations"
            / "generated"
            / f"{intake['manifest']['uuid']}.md"
        )
        
        generated_samples_file_path = (
            doc_path
            / "_shared_content"
            / "operations_center"
            / "integrations"
            / "generated"
            / f"{intake['manifest']['uuid']}_sample.md"
        )
        
        with open(generated_intake_file_path, "w", encoding="utf-8") as fd:
            fd.write(intake_content)
        with open(generated_samples_file_path, "w", encoding="utf-8") as fd:
            fd.write(sample_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update the documentation with intake formats"
    )
    parser.add_argument(
        "intake_repository", help="Path to the intake format repository"
    )
    parser.add_argument(
        "documentation_repository", help="Path to the documentation repository"
    )

    args = parser.parse_args()
    update_doc(
        intake_repository=args.intake_repository,
        documentation_repository=args.documentation_repository,
    )
