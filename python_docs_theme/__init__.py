import os


def setup(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme(
        'python_docs_theme', current_dir)
