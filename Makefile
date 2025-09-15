# You can set these variables from the command line.
CPYTHON_PATH = ../cpython
PYTHON       = python3
PACKAGE_ABS_PATH = $(shell pwd)/$(shell find dist/python-docs-theme-*.tar.gz)
SPHINXOPTS   =


.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to create a venv with necessary tools at $(CPYTHON_PATH)/Doc/venv"
	@echo "  html       to make standalone CPython HTML files"
	@echo "  htmlview   to open the index page built by the html target in your browser"

.PHONY: venv
venv:
	$(PYTHON) -m pip install build
	$(PYTHON) -m build
	cd $(CPYTHON_PATH)/Doc \
		&& make venv \
		&& ./venv/bin/pip install $(PACKAGE_ABS_PATH)

.PHONY: html
html: venv
	cd $(CPYTHON_PATH)/Doc && \
		make SPHINXOPTS="$(SPHINXOPTS)" html

.PHONY: htmlview
htmlview: html
	$(PYTHON) -c "import os, webbrowser; webbrowser.open('file://' + os.path.realpath('$(CPYTHON_PATH)/Doc/build/html/index.html'))"
