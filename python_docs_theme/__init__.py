from __future__ import annotations

import os
from pathlib import Path

THEME_PATH = Path(__file__).parent.resolve()


def setup(app):
    app.require_sphinx("7.2")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("python_docs_theme", current_dir)

    return {
        "version": "2024.12",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
