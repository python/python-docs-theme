from __future__ import annotations

from pathlib import Path

TYPE_CHECKING = False
if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "2025.4"

THEME_PATH = Path(__file__).resolve().parent


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")

    app.add_html_theme("python_docs_theme", str(THEME_PATH))

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
