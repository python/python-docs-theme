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


Features
========

Outdated redirection
--------------------

You can define the ``outdated_message`` and ``outdated_link_text``
variables to show a red banner on each page redirecting to the "latest"
version.

The ``outdated_message`` comes first, the ``outdated_link_text`` comes
afterwards and is the one user can click. When clicking on
``outdated_link_text``, they will be redirected to the same page
stripped from any prefix.

Meaning if they're on ``/2.7/``, they'll go to ``/``, if they're on
``/2.7/tutorial/`` they'll go to ``/tutorial/``.

Sadly it also mean that if you're on ``/fr/3.7/c-api/`` you'll be
redirected to ``/c-api/``, but as we don't know your URL patterns we
can't really do better.

You can personalize the URL by redefining the ``outdated_href`` block,
by default it contains::

    /{{ pagename }}{{ file_suffix }}
