from pathlib import Path

from python.validate_metadata import load_yaml, validate_required_fields


def test_valid_metadata_file_has_no_errors():
    data = load_yaml(Path("metadata/wheat-research-sample.yaml"))

    errors = validate_required_fields(data)

    assert errors == []


def test_metadata_contains_dataset_id():
    data = load_yaml(Path("metadata/wheat-research-sample.yaml"))

    assert data["dataset"]["id"] == "wheat-research-sample"


def test_referenced_dataset_file_exists():
    data = load_yaml(Path("metadata/wheat-research-sample.yaml"))
    file_path = Path(data["files"][0]["path"])

    assert file_path.exists()
