"""Script for handling translations with Babel"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import tomllib
from pathlib import Path

from babel.messages.mofile import read_mo
from babel.messages.pofile import read_po
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

# Global variables used by pybabel below (paths relative to PROJECT_DIR)
DOMAIN = "python-docs-theme"
COPYRIGHT_HOLDER = "Python Software Foundation"
SOURCE_DIR = "python_docs_theme"
MAPPING_FILE = ".babel.cfg"

PROJECT_DIR = Path(__file__).resolve().parent
PYPROJECT_TOML = Path(PROJECT_DIR, "pyproject.toml")
INIT_PY = PROJECT_DIR / SOURCE_DIR / "__init__.py"
LOCALES_DIR = Path(f"{SOURCE_DIR}", "locale")
POT_FILE = Path(LOCALES_DIR, f"{DOMAIN}.pot")


def get_project_info() -> dict:
    """Retrieve project's info to populate the message catalog template"""
    pyproject_text = PYPROJECT_TOML.read_text(encoding="utf-8")
    project_data = tomllib.loads(pyproject_text)["project"]

    # read __version__ from __init__.py
    for child in ast.parse(INIT_PY.read_bytes()).body:
        if not isinstance(child, ast.Assign):
            continue
        target = child.targets[0]
        if not isinstance(target, ast.Name) or target.id != "__version__":
            continue
        version_node = child.value
        if not isinstance(version_node, ast.Constant):
            continue
        project_data["version"] = version_node.value
        break

    return project_data


def extract_messages() -> None:
    """Extract messages from all source files into message catalog template"""
    Path(PROJECT_DIR, LOCALES_DIR).mkdir(parents=True, exist_ok=True)
    project_data = get_project_info()
    subprocess.run(
        [
            "pybabel",
            "extract",
            "-F",
            MAPPING_FILE,
            "--copyright-holder",
            COPYRIGHT_HOLDER,
            "--project",
            project_data["name"],
            "--version",
            project_data["version"],
            "--msgid-bugs-address",
            project_data["urls"]["Issue tracker"],
            "-o",
            POT_FILE,
            SOURCE_DIR,
        ],
        cwd=PROJECT_DIR,
        check=True,
    )


def init_locale(locale: str) -> None:
    """Initialize a new locale based on existing message catalog template"""
    pofile = PROJECT_DIR / LOCALES_DIR / locale / "LC_MESSAGES" / f"{DOMAIN}.po"
    if pofile.exists():
        print(f"There is already a message catalog for locale {locale}, skipping.")
        return
    cmd = [
        "pybabel",
        "init",
        "-i",
        POT_FILE,
        "-d",
        LOCALES_DIR,
        "-D",
        DOMAIN,
        "-l",
        locale,
    ]
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)


def update_catalogs(locale: str) -> None:
    """Update translations from existing message catalogs"""
    cmd = ["pybabel", "update", "-i", POT_FILE, "-d", LOCALES_DIR, "-D", DOMAIN]
    if locale:
        cmd.extend(["-l", locale])
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)


def compile_catalogs(locale: str) -> None:
    """Compile existing message catalogs"""
    cmd = ["pybabel", "compile", "-d", LOCALES_DIR, "-D", DOMAIN]
    if locale:
        cmd.extend(["-l", locale])
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)

    locale_dirs = PROJECT_DIR / LOCALES_DIR
    catalogs = (
        [locale_dirs / locale / "LC_MESSAGES" / f"{DOMAIN}.po"]
        if locale
        else sorted(locale_dirs.glob(f"*/LC_MESSAGES/{DOMAIN}.po"))
    )
    for pofile in catalogs:
        compile_js_catalog(pofile)


def compile_js_catalog(pofile: Path) -> None:
    """Export translated singular JavaScript messages from the compiled catalog."""
    mofile = pofile.with_suffix(".mo")
    jsfile = pofile.with_suffix(".js")
    if not mofile.exists():
        jsfile.unlink(missing_ok=True)
        return
    with pofile.open("rb") as f:
        source = read_po(f)
    with mofile.open("rb") as f:
        compiled = read_mo(f)
    messages = {}
    for message in source:
        if not isinstance(message.id, str):
            continue
        if not any(filename.endswith(".js") for filename, _ in message.locations):
            continue
        translation = compiled.get(message.id)
        if translation is not None and translation.string:
            messages[message.id] = translation.string
    jsfile.write_text(
        "Object.assign(Documentation.TRANSLATIONS, "
        + json.dumps(messages, ensure_ascii=True, sort_keys=True)
        + ");\n",
        encoding="utf-8",
    )


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, object]) -> None:
        compile_catalogs("")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["extract", "init", "update", "compile"],
        help="command to be executed",
    )
    parser.add_argument(
        "-l",
        "--locale",
        default="",
        help="language code (needed for init, optional for update and compile)",
    )

    args = parser.parse_args()
    locale = args.locale

    if args.command == "extract":
        extract_messages()
    elif args.command == "init":
        if not locale:
            parser.error("init requires passing the --locale option")
        init_locale(locale)
    elif args.command == "update":
        update_catalogs(locale)
    elif args.command == "compile":
        compile_catalogs(locale)


if __name__ == "__main__":
    main()
