# Configuration file for the Sphinx documentation builder.

import datetime

# Project values
project = "Sphinx mermaid"
author = "Antoine Mandin"
copyright = f"{datetime.date.today().strftime('%Y')}, Antoine Mandin"
release = "0.0.2"

extensions = [
    "sphinxmermaid", # Mermaid extension
    "sphinx_rtd_theme", # Read the docs them
]

# Use Read the docs theme
html_theme = "sphinx_rtd_theme"

# Link to Github repo
html_context = {
    "display_github": True,
    "github_user": "Doreapp",
    "github_repo": "sphinx-mermaid",
    "github_version": "main",
    "conf_py_path": "/doc/source/",
}
