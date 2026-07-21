PYTHON ?= .venv/bin/python

.PHONY: sync index validate audit build clean

sync:
	$(PYTHON) tooling/sync_research.py

index:
	$(PYTHON) tooling/index_claim_usage.py

validate:
	$(PYTHON) tooling/validate.py

audit: index
	$(PYTHON) tooling/audit_content.py

build:
	$(PYTHON) tooling/build.py

clean:
	rm -rf dist build
