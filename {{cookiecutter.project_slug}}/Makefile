PEX := pex
VIRTUALENV := python3 -m venv
PIP := venv/bin/pip
SCRIPT := {{ cookiecutter.script_name }}

all: bin/$(SCRIPT)

bin/$(SCRIPT): $(wildcard **/*.py)
	$(PEX) . -r requirements.txt --python=python3.6 -c $(SCRIPT) -o $@

.PHONY: requirements.txt
requirements.txt:
	@echo 'Installing into a clean virtualenv'
	$(eval TMPDIR := $(shell mktemp -d))
	$(VIRTUALENV) $(TMPDIR)
	$(TMPDIR)/bin/pip install --upgrade -e .
	@echo 'Writing out new requirements.txt based on setup.py'
	$(TMPDIR)/bin/pip freeze -r requirements.txt | grep -v '^-e' > requirements.txt
	@echo 'Wrote new requirements.txt'
	rm -rf $(TMPDIR)

.PHONY: venv
venv:
	$(VIRTUALENV) venv
	$(PIP) install -r requirements.txt
	$(PIP) install -e .
