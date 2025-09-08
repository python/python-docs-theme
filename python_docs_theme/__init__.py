from __future__ import annotations

from pathlib import Path

from sphinx.locale import get_translation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "2025.9"

THEME_PATH = Path(__file__).resolve().parent
LOCALE_DIR = THEME_PATH / "locale"
MESSAGE_CATALOG_NAME = "python-docs-theme"


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")

    app.add_html_theme("python_docs_theme", str(THEME_PATH))
    app.add_message_catalog(MESSAGE_CATALOG_NAME, LOCALE_DIR)

    def add_translation_to_context(app, pagename, templatename, context, doctree):
        _ = get_translation(MESSAGE_CATALOG_NAME)
        context["_"] = context["gettext"] = context["ngettext"] = _

    app.connect("html-page-context", add_translation_to_context)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
