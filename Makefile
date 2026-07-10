.PHONY: validate manifest check healthcheck collection ingest metadata query test

validate:
	python python/validate_metadata.py

manifest:
	python python/generate_manifest.py

check:
	./scripts/check_icommands.sh

healthcheck:
	./scripts/healthcheck.sh

collection:
	./scripts/create_collection.sh

ingest: manifest
	./scripts/ingest_dataset.sh

metadata:
	./scripts/attach_metadata.sh

query:
	./scripts/query_metadata.sh

test:
	python -m pytest

metrics:
	python python/metrics_exporter.py

prometheus:
	docker compose up prometheus
