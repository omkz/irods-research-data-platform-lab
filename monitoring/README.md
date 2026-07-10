# Monitoring

This project includes a simple Prometheus metrics exporter for the research data management workflow.

## Metrics Exporter

Run the exporter:

    make metrics

The exporter exposes metrics at:

    http://localhost:8000/metrics

## Available Metrics

    irods_healthcheck_status

Shows whether iRODS is reachable.

Value:

- 1 = healthy
- 0 = unhealthy

    metadata_validation_status

Shows whether the metadata YAML validation passes.

Value:

- 1 = valid
- 0 = invalid

    irods_healthcheck_total

Counts how many healthchecks have been performed.

## Prometheus

Run Prometheus:

    make prometheus

Open Prometheus UI:

    http://localhost:9090

Example queries:

    irods_healthcheck_status
    metadata_validation_status
    irods_healthcheck_total

## Notes

The exporter checks the local iRODS connection using:

    ils

If the iRODS healthcheck returns 0, run:

    iinit

Then restart the exporter.
