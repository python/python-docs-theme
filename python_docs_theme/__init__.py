from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

THEME_PATH = Path(__file__).resolve().parent


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")
    app.add_html_theme("python_docs_theme", THEME_PATH)

    return {
        "version": "2024.12",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
