#!/usr/bin/env python3

import subprocess
import time
from prometheus_client import Gauge, Counter, start_http_server


IRODS_HEALTH = Gauge(
    "irods_healthcheck_status",
    "iRODS healthcheck status. 1 means healthy, 0 means unhealthy.",
)

METADATA_VALIDATION_STATUS = Gauge(
    "metadata_validation_status",
    "Metadata validation status. 1 means valid, 0 means invalid.",
)

HEALTHCHECK_TOTAL = Counter(
    "irods_healthcheck_total",
    "Total number of iRODS healthchecks performed.",
)


def run_command(command: list[str]) -> bool:
    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

    return result.returncode == 0


def update_metrics() -> None:
    HEALTHCHECK_TOTAL.inc()

    metadata_ok = run_command(["python", "python/validate_metadata.py"])
    METADATA_VALIDATION_STATUS.set(1 if metadata_ok else 0)

    irods_ok = run_command(["ils"])
    IRODS_HEALTH.set(1 if irods_ok else 0)


def main() -> None:
    start_http_server(8000)
    print("Metrics exporter running on http://localhost:8000/metrics")

    while True:
        update_metrics()
        time.sleep(15)


if __name__ == "__main__":
    main()
