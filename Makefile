CPYTHON_PATH               = ../cpython
PACKAGE_ABS_PATH = $(shell pwd)/$(shell find dist/python-docs-theme-*.tar.gz)


.PHONY: all
all: install
	cd $(CPYTHON_PATH)/Doc && \
		make html


.PHONY: install
install:
	python3 -m build
	cd $(CPYTHON_PATH)/Doc && \
		./venv/bin/pip install $(PACKAGE_ABS_PATH)

.PHONY: help
help:
	@echo "all:		default rule; run the \`install\` rule, and also rebuild the cpython docs"
	@echo "install: 	build the package, and install it into the virtual environment"
	@echo "		at $(CPYTHON_PATH)/Doc/venv"
