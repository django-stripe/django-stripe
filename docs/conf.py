"""Sphinx configuration."""

project = "django-stripe"
author = "Abe Hanoka"
copyright = "2024, Abe Hanoka"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
