#!/usr/bin/env python3
"""
Usage: python3 update_mkdocs.py /path/to/repository/intake-formats /path/to/repository/documentation
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import yaml
from jinja2 import Environment, FileSystemLoader

with open("ecs_flat.yml", "r") as fd:
    ECS = yaml.safe_load(fd)


def analyze_parser(parser, custom_fields) -> Dict:

    taxonomy = ECS.copy()
    taxonomy.update(custom_fields or {})
    # extract all the fields
    fields = defaultdict(set)
    kind_values = set()
    category_values = set()
    type_values = set()

    for stage_name, stage_definition in parser["stages"].items():

        for action in stage_definition.get("actions", []):
            for field in action.get("set", {}):

                if not isinstance(action["set"][field], list):
                    field_values = [action["set"][field]]
                else:
                    field_values = action["set"][field]

                fields[field].update(field_values)

                if field in ("event.type", "event.category", "event.kind"):
                    for field_value in field_values:
                        if "{" in field_value:
                            continue

                        if field == "event.type":
                            type_values.add(field_value)
                        elif field == "event.kind":
                            kind_values.add(field_value)
                        elif field == "event.category":
                            category_values.add(field_value)

    return {
        "fields": [
            {
                "name": field,
                "type": taxonomy[field]["type"],
                "short": taxonomy[field].get(
                    "short", taxonomy[field].get("description", "-")
                ),
            }
            for field in sorted(fields.keys())
            if field in taxonomy
        ],
        "category": sorted(category_values),
        "type": sorted(type_values),
        "kind": sorted(kind_values),
    }

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

def load_intakes(intake_repository: str) -> List[Dict]:

    intakes: List[Dict] = []

    for module_path in Path(intake_repository).iterdir():
        if not module_path.is_dir() or module_path.name.startswith("."):
            continue

        for intake_path in module_path.iterdir():
            if not module_path.is_dir() or module_path.name.startswith("_"):
                continue

            # load manifest
            intake_manifest = intake_path / "_meta" / "manifest.yml"
            if not intake_manifest.exists():
                continue

            intake = {"repo_path": f"{module_path.name}/{intake_path.name}"}
            with open(intake_manifest, "r") as fd:
                intake["manifest"] = yaml.safe_load(fd)

            # load fields
            intake_fields = intake_path / "_meta" / "fields.yml"
            if intake_fields.exists():
                with open(intake_fields, "r") as fd:
                    intake["fields"] = yaml.safe_load(fd) or {}
            else:
                intake["fields"] = {}

            # load parser
            intake_parser = intake_path / "ingest" / "parser.yml"
            if intake_parser.exists():
                with open(intake_parser, "r") as fd:
                    intake["parser"] = analyze_parser(
                        yaml.safe_load(fd), intake["fields"]
                    )
            else:
                intake["parser"] = {}

            # load tests
            intake_tests = intake_path / "tests"
            intake["tests"] = []
            intake["samples"] = []
            intake["samples_type"] = ""
            intake["is_sample_json"] = False
            if intake_tests.exists():
                for intake_test in sorted(intake_tests.iterdir()):

                    if not intake_test.name.endswith(".json"):
                        continue

                    with open(intake_test, "r") as fd:
                        test = json.load(fd)
                        intake["is_sample_json"] = is_valid_json(test["expected"]["message"])
                        content = json.dumps(json.loads(test["expected"]["message"]), indent="    ") if intake["is_sample_json"] else test["expected"]["message"]
                        intake["samples"].append(
                            {
                                "name": intake_test.name.split('.')[0],
                                "content": content
                            })
                        intake["tests"].append(
                            {
                                "name": intake_test.name,
                                "content": json.dumps(
                                    test["expected"], indent="    "
                                ),
                            }
                        )

            # load logo
            logo_path = intake_path / "_meta" / "logo.png"
            if logo_path.exists():
                with open(logo_path, "rb") as fd:
                    intake["logo"] = fd.read()

            intakes.append(intake)

    return intakes


def generate_intake_doc(intake: Dict) -> str:

    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    template = env.get_template("intake.md.jinja")
    return template.render(
        manifest=intake["manifest"],
        fields=intake["fields"],
        parser=intake["parser"],
        tests=intake["tests"],
        is_sample_json = intake["is_sample_json"],
        samples=intake["samples"],
        repo_path=intake["repo_path"],
    )


def update_doc(intake_repository: str, documentation_repository: str):

    doc_path = Path(documentation_repository)

    # load intakes
    intakes = load_intakes(intake_repository)

    # produce intake documentation
    for intake in intakes:

        intake_content = generate_intake_doc(intake)

        generated_file_path = (
            doc_path
            / "_shared_content"
            / "operations_center"
            / "integrations"
            / "generated"
            / f"{intake['manifest']['uuid']}.md"
        )

        with open(generated_file_path, "w") as fd:
            fd.write(intake_content)


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
