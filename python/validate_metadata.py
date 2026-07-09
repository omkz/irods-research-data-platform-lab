#!/usr/bin/env python3

from pathlib import Path
import sys
import yaml


REQUIRED_DATASET_FIELDS = [
    "id",
    "title",
    "description",
    "project",
    "owner",
    "created_at",
    "license",
]

REQUIRED_METADATA_FIELDS = [
    "discipline",
    "organism",
    "data_type",
    "location",
    "retention",
]


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Metadata file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("Metadata file must contain a YAML object")

    return data


def validate_required_fields(data: dict) -> list[str]:
    errors = []

    dataset = data.get("dataset")
    if not isinstance(dataset, dict):
        errors.append("Missing or invalid 'dataset' section")
    else:
        for field in REQUIRED_DATASET_FIELDS:
            if field not in dataset or dataset[field] in (None, ""):
                errors.append(f"Missing dataset field: {field}")

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("Missing or invalid 'metadata' section")
    else:
        for field in REQUIRED_METADATA_FIELDS:
            if field not in metadata or metadata[field] in (None, ""):
                errors.append(f"Missing metadata field: {field}")

    files = data.get("files")
    if not isinstance(files, list) or not files:
        errors.append("Missing or invalid 'files' section")
    else:
        for index, item in enumerate(files, start=1):
            if not isinstance(item, dict):
                errors.append(f"File entry #{index} must be an object")
                continue

            path = item.get("path")
            if not path:
                errors.append(f"File entry #{index} is missing path")
                continue

            if not Path(path).exists():
                errors.append(f"Referenced file does not exist: {path}")

    return errors


def main() -> int:
    metadata_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("metadata/wheat-research-sample.yaml")

    try:
        data = load_yaml(metadata_path)
        errors = validate_required_fields(data)
    except Exception as error:
        print(f"ERROR: {error}")
        return 1

    if errors:
        print("Metadata validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: metadata valid: {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
