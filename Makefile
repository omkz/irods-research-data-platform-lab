.PHONY: validate manifest

validate:
	python python/validate_metadata.py

manifest:
	python python/generate_manifest.py
