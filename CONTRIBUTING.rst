# How to release

- Update CHANGELOG.rst
- bump version (YYYY.MM) in setup.py and python_docs_theme/theme.conf
- commit
- push to check one last time if the tests pass github side.
- tag it (YYYY.MM).
- build (``python -m build``)
- Test it (in :file:`cpython/Doc` run
  ``./venv/bin/pip install ../../python-docs-theme/dist/python-docs-theme-2021.8.tar.gz``
  then build the doc using ``make html``).
- upload it: ``twine upload dist/*``.
- bump version (YYYY.MM.dev) in setup.py and python_docs_theme/theme.conf
- Commit this last bump.
- push and push the tag (``git push && git push --tags``)

# Makefile Usage

This project includes a simple Makefile for syncing changes to the theme with
the main cpython repository. Run ``make help`` for details on available rules.

There is one configurable variable, ``CPYTHON_PATH``, which should be the path
to the cpython repository on your machine. By default, it points to
``../cpython``.
