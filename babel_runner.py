#!/usr/bin/venv python3
"""Script for handling translations with Babel"""
from __future__ import annotations

import argparse
import os
import subprocess

import tomllib

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Global variables used by pybabel below
DOMAIN = "messages"
COPYRIGHT_HOLDER = "Python Software Foundation"
LOCALES_DIR = os.path.relpath(os.path.join(PROJECT_DIR, "locales"))
POT_FILE = os.path.relpath(os.path.join(LOCALES_DIR, f"{DOMAIN}.pot"), PROJECT_DIR)
SOURCE_DIR = os.path.relpath(
    os.path.join(PROJECT_DIR, "python_docs_theme"), PROJECT_DIR
)
MAPPING_FILE = os.path.relpath(os.path.join(PROJECT_DIR, ".babel.cfg"), PROJECT_DIR)


def get_project_info() -> dict:
    """Retrieve project's info to populate the message catalog template"""
    with open(os.path.join(PROJECT_DIR, "pyproject.toml"), "rb") as f:
        data = tomllib.load(f)
    return data["project"]


def extract_messages():
    """Extract messages from all source files into template file"""
    os.makedirs(LOCALES_DIR, exist_ok=True)
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
        check=True,
    )


def init_locale(locale: str):
    """Initialize a new locale based on existing"""
    cmd = ["pybabel", "init", "-i", POT_FILE, "-d", LOCALES_DIR, "-l", locale]
    subprocess.run(cmd, check=True)


def update_catalogs(locale: str):
    """Update translations from existing message catalogs"""
    cmd = ["pybabel", "update", "-i", POT_FILE, "-d", LOCALES_DIR]
    if locale != "":
        cmd.append(["-l", locale])
    subprocess.run(cmd, check=True)


def compile_catalogs(locale: str):
    """Compile existing message catalogs"""
    cmd = ["pybabel", "compile", "-d", LOCALES_DIR]
    if locale != "":
        cmd.append(["-l", locale])
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["init", "extract", "update", "compile"],
        help="command to be executed",
    )
    parser.add_argument(
        "-l",
        "--locale",
        help="language code (needed for init, optional for update and compile)",
    )

    args = parser.parse_args()
    locale = args.locale if args.locale else ""

    os.chdir(PROJECT_DIR)

    if args.command == "extract":
        extract_messages()
    elif args.command == "init":
        if locale == "":
            parser.error("init requires passing the --locale option")
        init_locale(locale)
    elif args.command == "update":
        update_catalogs(locale)
    elif args.command == "compile":
        compile_catalogs(locale)


if __name__ == "__main__":
    main()
