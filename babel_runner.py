"""Script for handling translations with Babel"""

from __future__ import annotations

import argparse
import ast
import subprocess
import tomllib
from pathlib import Path

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
    cmd = ["pybabel", "compile", "-d", LOCALES_DIR, "-D", DOMAIN, "--use-fuzzy"]
    if locale:
        cmd.extend(["-l", locale])
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)


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
