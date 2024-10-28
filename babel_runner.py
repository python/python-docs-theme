#!/usr/bin/venv python3
"""Script for handling translations with Babel"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError as ie:
        raise ImportError(
            "tomli or tomllib is required to parse pyproject.toml"
        ) from ie

PROJECT_DIR = Path(__file__).resolve().parent

# Global variables used by pybabel below (paths relative to PROJECT_DIR)
DOMAIN = "messages"
COPYRIGHT_HOLDER = "Python Software Foundation"
LOCALES_DIR = "locales"
POT_FILE = Path(LOCALES_DIR, f"{DOMAIN}.pot")
SOURCE_DIR = "python_docs_theme"
MAPPING_FILE = ".babel.cfg"


def get_project_info() -> dict:
    """Retrieve project's info to populate the message catalog template"""
    with open(Path(PROJECT_DIR / "pyproject.toml"), "rb") as f:
        data = tomllib.load(f)
    return data["project"]


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
    cmd = ["pybabel", "init", "-i", POT_FILE, "-d", LOCALES_DIR, "-l", locale]
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)


def update_catalogs(locale: str) -> None:
    """Update translations from existing message catalogs"""
    cmd = ["pybabel", "update", "-i", POT_FILE, "-d", LOCALES_DIR]
    if locale:
        cmd.extend(["-l", locale])
    subprocess.run(cmd, cwd=PROJECT_DIR, check=True)


def compile_catalogs(locale: str) -> None:
    """Compile existing message catalogs"""
    cmd = ["pybabel", "compile", "-d", LOCALES_DIR]
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
