.PHONY: validate manifest check healthcheck collection ingest metadata query test local irods-demo metrics prometheus grafana monitoring-demo

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

gui:
	streamlit run app/main.py

local:
	$(MAKE) validate
	$(MAKE) manifest
	$(MAKE) test

irods-demo:
	$(MAKE) check
	$(MAKE) healthcheck
	$(MAKE) ingest
	$(MAKE) metadata
	$(MAKE) query

monitoring-demo:
	@echo "Terminal 1: make metrics"
	@echo "Terminal 2: docker compose up prometheus grafana"
	@echo "Prometheus: http://localhost:9090"
	@echo "Grafana: http://localhost:3000"
