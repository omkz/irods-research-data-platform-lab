.PHONY: validate manifest check healthcheck collection ingest metadata

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
