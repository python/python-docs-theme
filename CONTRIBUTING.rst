How to release
--------------

- Update ``CHANGELOG.rst``
- Bump version (YYYY.MM) in ``python_docs_theme/__init__.py``
- Commit
- Push to check tests pass on
  `GitHub Actions <https://github.com/python/python-docs-theme/actions>`__
- Go to https://github.com/python/python-docs-theme/releases
- Click "Draft a new release"
- Click "Choose a tag"
- Type the next YYYY.MM version (no leading zero) and
  select "**Create new tag: YYYY.MM** on publish"
- Leave the "Release title" blank (it will be autofilled)
- Click "Generate release notes" and amend as required
- Click "Publish release"
- Check the tagged `GitHub Actions build <https://github.com/python/python-docs-theme/actions/workflows/pypi-package.yml>`__
  has deployed to `PyPI <https://pypi.org/project/python-docs-theme/#history>`__

Makefile usage
--------------

This project includes a simple Makefile for syncing changes to the theme with
the main CPython repository. Run ``make help`` for details on available rules.

There is one configurable variable, ``CPYTHON_PATH``, which should be the path
to the CPython repository on your machine. By default, it points to
``../cpython``.
