#!/usr/bin/env python3

from pathlib import Path
import subprocess
import yaml

import streamlit as st


METADATA_PATH = Path("metadata/wheat-research-sample.yaml")
DATASET_DIR = Path("datasets/wheat-research-sample")
MANIFEST_PATH = DATASET_DIR / "manifest.csv"


st.set_page_config(
    page_title="Research Data Platform Lab",
    layout="wide",
)


def run_command(command: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )

    return result.returncode, result.stdout, result.stderr


def load_metadata() -> dict:
    with METADATA_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


st.title("Research Data Platform Lab")

st.write(
    "A small dashboard for exploring metadata validation, dataset manifest generation, "
    "and iRODS metadata discovery."
)

tab_overview, tab_metadata, tab_validation, tab_irods, tab_monitoring = st.tabs(
    [
        "Overview",
        "Metadata",
        "Validation",
        "iRODS Query",
        "Monitoring",
    ]
)

with tab_overview:
    st.header("Dataset Overview")

    metadata = load_metadata()
    dataset = metadata.get("dataset", {})

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Dataset ID", dataset.get("id", "unknown"))
        st.metric("Project", dataset.get("project", "unknown"))
        st.metric("Owner", dataset.get("owner", "unknown"))

    with col2:
        st.metric("Discipline", metadata.get("metadata", {}).get("discipline", "unknown"))
        st.metric("Organism", metadata.get("metadata", {}).get("organism", "unknown"))
        st.metric("Data Type", metadata.get("metadata", {}).get("data_type", "unknown"))

    st.subheader("Dataset Files")

    if DATASET_DIR.exists():
        files = sorted(path for path in DATASET_DIR.iterdir() if path.is_file())
        for path in files:
            st.write(f"- `{path}` ({path.stat().st_size} bytes)")
    else:
        st.warning(f"Dataset directory not found: {DATASET_DIR}")

with tab_metadata:
    st.header("Metadata YAML")

    if METADATA_PATH.exists():
        st.code(METADATA_PATH.read_text(encoding="utf-8"), language="yaml")
    else:
        st.error(f"Metadata file not found: {METADATA_PATH}")

with tab_validation:
    st.header("Validation and Manifest")

    if st.button("Run metadata validation"):
        code, stdout, stderr = run_command(["python", "python/validate_metadata.py"])

        if code == 0:
            st.success("Metadata validation passed")
        else:
            st.error("Metadata validation failed")

        st.code(stdout + stderr)

    if st.button("Generate manifest"):
        code, stdout, stderr = run_command(["python", "python/generate_manifest.py"])

        if code == 0:
            st.success("Manifest generated")
        else:
            st.error("Manifest generation failed")

        st.code(stdout + stderr)

    st.subheader("Manifest")

    if MANIFEST_PATH.exists():
        st.dataframe(
            MANIFEST_PATH.read_text(encoding="utf-8").splitlines(),
            use_container_width=True,
        )
        st.code(MANIFEST_PATH.read_text(encoding="utf-8"), language="csv")
    else:
        st.info("Manifest has not been generated yet.")

with tab_irods:
    st.header("iRODS Metadata Query")

    attr = st.text_input("Attribute", value="project")
    value = st.text_input("Value", value="wheat-growth-2026")

    if st.button("Query iRODS metadata"):
        code, stdout, stderr = run_command(
            ["bash", "-lc", f"ATTR={attr} VALUE={value} ./scripts/query_metadata.sh"]
        )

        if code == 0 and stdout.strip():
            st.success("Query completed")
        elif code == 0:
            st.warning("Query completed but returned no result")
        else:
            st.error("Query failed")

        st.code(stdout + stderr)

with tab_monitoring:
    st.header("Monitoring")

    st.write("Metrics exporter endpoint:")

    st.code("http://localhost:8000/metrics")

    st.write("Prometheus:")

    st.code("http://localhost:9090")

    st.write("Grafana:")

    st.code("http://localhost:3000")

    st.info("Run `make metrics` and `docker compose up prometheus grafana` before opening monitoring dashboards.")
