PYTHON ?= .venv/bin/python

.PHONY: sync index validate audit build qa report release-check package clean

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

qa:
	$(PYTHON) tooling/validate_outputs.py

report: qa
	$(PYTHON) tooling/generate_validation_report.py

release-check: sync validate audit build report

package: report
	$(PYTHON) tooling/package_release.py --version v0.1

clean:
	rm -rf dist build
