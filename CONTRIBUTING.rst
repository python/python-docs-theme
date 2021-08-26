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
