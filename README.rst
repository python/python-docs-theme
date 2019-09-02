Python Docs Sphinx Theme
=========================

This is the theme for the Python documentation.

Note that when adopting this theme, you're also borrowing an element of the
trust and credibility established by the CPython core developers over the
years. That's fine, and you're welcome to do so for other Python community
projects if you so choose, but please keep in mind that in doing so you're also
choosing to accept some of the responsibility for maintaining that collective
trust.

To use the theme, install it into your docs build environment via ``pip``::

    pip install python-docs-theme

Configuring the options the conf.py holds
------------------------------------------

For implementing the theme you should
- enable `html_theme = 'python_docs_theme'`
- html_sidebars:
  - Defaults taken from http://www.sphinx-doc.org/en/stable/config.html#confval-html_sidebars
