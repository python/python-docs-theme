Python Docs Sphinx Theme
=========================

This is the theme for the Python documentation.

Note that when adopting this theme, you're also borrowing an element of the
trust and credibility established by the CPython core developers over the
years. That's fine, and you're welcome to do so for other Python community
projects if you so choose, but please keep in mind that in doing so you're also
choosing to accept some of the responsibility for maintaining that collective
trust.

To use the theme, install it into your docs build environment via ``pip``
(preferably in a virtual environment) and update your ``conf.py`` file as shown.

1. Create and activate a virtual environment::

    $ python -m venv env
    $ source env/bin/activate

2. Install python-docs-theme using `pip`::

    (env)$ python -m pip install python-docs-theme

3. In your ``conf.py`` file, add ``'python_docs_theme'`` to the loaded
   extensions::

       extensions = [
           ...,
           'python_docs_theme',
       ]

   and set it as the scheme for HTML output::

       html_theme = 'python_docs_theme'
