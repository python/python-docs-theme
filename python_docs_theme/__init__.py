from __future__ import annotations

import gettext
from pathlib import Path

TYPE_CHECKING = False
if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "2025.5"

THEME_PATH = Path(__file__).resolve().parent


def setup_translations(app):
    translation = gettext.translation(
        domain="messages",
        localedir=str(THEME_PATH / "locales"),
        languages=[app.config.language],
        fallback=True,
    )
    app.builder.templates.environment.install_gettext_translations(
        translation, newstyle=True
    )


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")

    app.connect("builder-inited", setup_translations)
    app.add_html_theme("python_docs_theme", str(THEME_PATH))

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
