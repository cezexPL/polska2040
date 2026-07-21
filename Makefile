PYTHON ?= .venv/bin/python

.PHONY: validate build clean

validate:
	$(PYTHON) tooling/validate.py

build:
	$(PYTHON) tooling/build.py

clean:
	rm -rf dist build

