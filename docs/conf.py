"""Sphinx configuration."""

import os
import sys

import django


sys.path.insert(0, os.path.abspath(".."))  # Adjust the path to the Django project.
os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"  # Replace with your settings module.
django.setup()


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
