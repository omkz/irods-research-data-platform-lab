.PHONY: validate manifest check healthcheck collection

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
