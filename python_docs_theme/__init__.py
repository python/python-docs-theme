from __future__ import annotations

import hashlib
from functools import cache
from pathlib import Path

import sphinx.application
from sphinx.builders.html import StandaloneHTMLBuilder

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "2025.2"

THEME_PATH = Path(__file__).resolve().parent


@cache
def _asset_hash(path: str) -> str:
    """Append a `?digest=` to an url based on the file content."""
    full_path = THEME_PATH / path.replace("_static/", "static/")
    digest = hashlib.sha1(full_path.read_bytes()).hexdigest()

    return f"{path}?digest={digest}"


def _add_asset_hashes(static: list[str], add_digest_to: list[str]) -> None:
    for asset in add_digest_to:
        index = static.index(asset)
        static[index].filename = _asset_hash(asset)  # type: ignore[attr-defined]


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    if app.config.html_theme != "python_docs_theme":
        return

    assert isinstance(app.builder, StandaloneHTMLBuilder)

    if (4,) <= sphinx.version_info < (7, 1) and "css_files" in context:
        if "_static/pydoctheme.css" not in context["css_files"]:
            raise ValueError(
                "This documentation is not using `pydoctheme.css` as the stylesheet. "
                "If you have set `html_style` in your conf.py file, remove it."
            )

        _add_asset_hashes(
            context["css_files"],
            ["_static/pydoctheme.css"],
        )


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("3.4")

    app.add_html_theme("python_docs_theme", str(THEME_PATH))

    app.connect("html-page-context", _html_page_context)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
