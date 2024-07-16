from __future__ import annotations

import hashlib
import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

import httpx
import sphinx.application
from sphinx.builders.html import StandaloneHTMLBuilder

if sys.version_info[:2] >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

THEME_PATH = Path(__file__).parent.resolve()


def _version_label(
    version_name: str,
    status: Literal["feature", "prerelease", "bugfix", "security", "end-of-life"],
) -> str:
    if status == "feature":
        return f"dev ({version_name})"
    if status == "prerelease":
        return f"pre ({version_name})"
    if status in {"end-of-life", "security", "bugfix"}:
        return version_name
    msg = f"Unknown status: {status}"
    raise ValueError(msg)


def _builder_inited(app):
    html_context = app.config.html_context
    language = app.config.language
    release = app.config.release
    if app.config.html_theme != "python_docs_theme":
        return

    # Get the current branch statuses
    releases = httpx.get(
        "https://raw.githubusercontent.com/python/devguide/main/include/release-cycle.json",
        timeout=30,
    ).json()
    # Get appropriate version labels
    release_labels = {
        name: _version_label(name, release["status"])
        for name, release in releases.items()
    }
    # Update the current version to be the full release string
    if (short_version := ".".join(release.split(".", 2)[:2])) in release_labels:
        release_labels[short_version] = release

    # Store the versions in the context as a sorted list of tuples
    html_context["switchers_versions"] = sorted(
        release_labels.items(),
        key=lambda release_label: tuple(map(int, release_label[0].split("."))),
        reverse=True,
    )

    # Get the languages from the docsbuild-scripts config
    docsbuild_config = httpx.get(
        "https://raw.githubusercontent.com/python/docsbuild-scripts/main/config.toml",
        timeout=30,
    ).text
    # Convert language tags and extract language names
    languages = [
        (iso639_tag.replace("_", "-").lower(), section["name"])
        for iso639_tag, section in tomllib.loads(docsbuild_config)["languages"].items()
        if section.get("in_prod", True)
    ]

    # If we are working on a language that is not in the list, add it
    if language and language not in dict(languages):
        languages.append((language, language))

    # Store the versions in the context as a sorted list of tuples
    html_context["switchers_languages"] = sorted(languages)


@lru_cache(maxsize=None)
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


def setup(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("python_docs_theme", current_dir)

    app.connect("builder-inited", _builder_inited)
    app.connect("html-page-context", _html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
