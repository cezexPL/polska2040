PYTHON ?= .venv/bin/python

.PHONY: sync validate build clean

sync:
	$(PYTHON) tooling/sync_research.py

validate:
	$(PYTHON) tooling/validate.py

build:
	$(PYTHON) tooling/build.py

clean:
	rm -rf dist build
