CPYTHON_PATH               = ../cpython
PACKAGE_ABS_PATH = $(shell pwd)/$(shell find dist/python-docs-theme-*.tar.gz)


.PHONY: html
html: venv
	cd $(CPYTHON_PATH)/Doc && \
		make html


.PHONY: venv
venv:
	python3 -m build
	cd $(CPYTHON_PATH)/Doc \
		&& make venv \
		&& ./venv/bin/pip install $(PACKAGE_ABS_PATH)

.PHONY: help
help:
	@echo "html:		default rule; run the \`venv\` rule, and also rebuild the CPython docs"
	@echo "venv: 		build the package, and install it into the virtual environment"
	@echo "		at $(CPYTHON_PATH)/Doc/venv"
