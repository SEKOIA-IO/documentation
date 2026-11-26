import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import yaml


class IntakeLoadingError(ValueError):
    """Raised when an intake cannot be loaded or validated."""


def _load_ecs(script_dir: Path) -> Dict:
    with open(script_dir / "ecs_flat.yml", "r", encoding="utf-8") as fd:
        ecs = yaml.safe_load(fd)
    return ecs or {}


def is_valid_json(content: str) -> bool:
    if not isinstance(content, str):
        return False
    try:
        json.loads(content)
        return True
    except (TypeError, ValueError):
        return False


def _extract_event_value(field: str, field_value: object, values: Dict[str, set]) -> None:
    if not isinstance(field_value, str):
        return
    if "{" in field_value:
        return
    if field == "event.type":
        values["type"].add(field_value)
    elif field == "event.kind":
        values["kind"].add(field_value)
    elif field == "event.category":
        values["category"].add(field_value)


def analyze_parser(parser: Dict, custom_fields: Dict, intake_path: Path, ecs: Dict) -> Dict:
    if not isinstance(parser, dict):
        raise IntakeLoadingError(f"Invalid parser file format for intake {intake_path}")
    if not isinstance(parser.get("stages"), dict):
        raise IntakeLoadingError(f"Missing or invalid parser stages in intake {intake_path}")

    taxonomy = ecs.copy()
    taxonomy.update(custom_fields or {})

    fields = defaultdict(set)
    event_values = {"kind": set(), "category": set(), "type": set()}

    for stage_name, stage_definition in parser["stages"].items():
        if not isinstance(stage_definition, dict):
            raise IntakeLoadingError(
                f"Invalid stage definition '{stage_name}' in intake {intake_path}"
            )
        for action in stage_definition.get("actions", []):
            if not isinstance(action, dict):
                continue
            action_set = action.get("set", {})
            if not isinstance(action_set, dict):
                continue
            for field, raw_values in action_set.items():
                field_values = raw_values if isinstance(raw_values, list) else [raw_values]
                for field_value in field_values:
                    try:
                        fields[field].add(field_value)
                    except TypeError:
                        fields[field].add(str(field_value))
                    if field in ("event.type", "event.category", "event.kind"):
                        _extract_event_value(field, field_value, event_values)

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
        "category": sorted(event_values["category"]),
        "type": sorted(event_values["type"]),
        "kind": sorted(event_values["kind"]),
    }


def _ensure_manifest(manifest: object, intake_manifest: Path) -> Dict:
    if not isinstance(manifest, dict):
        raise IntakeLoadingError(f"Invalid manifest format in {intake_manifest}")
    uuid = manifest.get("uuid")
    if not isinstance(uuid, str) or not uuid.strip():
        raise IntakeLoadingError(f"Missing or invalid uuid in {intake_manifest}")
    return manifest


def _read_expected_message(test: Dict, intake_test: Path) -> object:
    expected = test.get("expected")
    if not isinstance(expected, dict):
        raise IntakeLoadingError(
            f"Missing or invalid 'expected' object in test file {intake_test}"
        )
    if "message" not in expected:
        raise IntakeLoadingError(f"Missing expected.message in test file {intake_test}")
    return expected["message"]


def _build_sample_name(base_name: str, existing_names: Dict[str, int]) -> str:
    if base_name not in existing_names:
        existing_names[base_name] = 1
        return base_name
    existing_names[base_name] += 1
    return f"{base_name} ({existing_names[base_name]})"


def _load_tests(intake_tests: Path) -> Dict[str, List[Dict]]:
    tests: List[Dict] = []
    samples: List[Dict] = []
    sample_names: Dict[str, int] = {}

    if not intake_tests.exists():
        return {"tests": tests, "samples": samples}

    for intake_test in sorted(intake_tests.iterdir()):
        if intake_test.suffix != ".json":
            continue
        with open(intake_test, "r", encoding="utf-8") as fd:
            test = json.load(fd)

        message = _read_expected_message(test, intake_test)
        is_json = is_valid_json(message)

        if is_json:
            content = json.dumps(
                json.loads(message),
                indent=4,
                ensure_ascii=False,
            )
        elif isinstance(message, str):
            content = message
        else:
            content = json.dumps(message, indent=4, ensure_ascii=False)

        sample_name = _build_sample_name(intake_test.stem, sample_names)

        samples.append({"name": sample_name, "content": content, "is_json": is_json})
        tests.append(
            {
                "name": intake_test.name,
                "content": json.dumps(test.get("expected"), indent=4, ensure_ascii=False),
            }
        )

    return {"tests": tests, "samples": samples}


def load_intakes(intake_repository: str, script_dir: Path) -> List[Dict]:
    intakes: List[Dict] = []
    ecs = _load_ecs(script_dir)

    for module_path in Path(intake_repository).iterdir():
        if not module_path.is_dir() or module_path.name.startswith("."):
            continue

        for intake_path in module_path.iterdir():
            if not intake_path.is_dir() or intake_path.name.startswith("_"):
                continue

            intake_manifest = intake_path / "_meta" / "manifest.yml"
            if not intake_manifest.exists():
                continue

            intake = {"repo_path": f"{module_path.name}/{intake_path.name}"}

            with open(intake_manifest, "r", encoding="utf-8") as fd:
                intake["manifest"] = _ensure_manifest(yaml.safe_load(fd), intake_manifest)

            intake_fields = intake_path / "_meta" / "fields.yml"
            if intake_fields.exists():
                with open(intake_fields, "r", encoding="utf-8") as fd:
                    loaded_fields = yaml.safe_load(fd) or {}
                if not isinstance(loaded_fields, dict):
                    raise IntakeLoadingError(
                        f"Invalid fields format in {intake_fields}, expected object"
                    )
                intake["fields"] = loaded_fields
            else:
                intake["fields"] = {}

            intake_parser = intake_path / "ingest" / "parser.yml"
            if intake_parser.exists():
                with open(intake_parser, "r", encoding="utf-8") as fd:
                    intake["parser"] = analyze_parser(
                        yaml.safe_load(fd), intake["fields"], intake_path, ecs
                    )
            else:
                intake["parser"] = {"fields": [], "kind": [], "category": [], "type": []}

            intake_tests = _load_tests(intake_path / "tests")
            intake["tests"] = intake_tests["tests"]
            intake["samples"] = intake_tests["samples"]

            logo_path = intake_path / "_meta" / "logo.png"
            if logo_path.exists():
                with open(logo_path, "rb") as fd:
                    intake["logo"] = fd.read()

            intakes.append(intake)

    return intakes
