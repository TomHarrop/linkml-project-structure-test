"""Data model package for linkml-project-structure-test."""

from pathlib import Path
from .linkml_project_structure_test import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "linkml_project_structure_test.yaml"
