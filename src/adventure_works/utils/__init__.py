"""
Utilities Module - Shared Utilities and Helpers

Provides common utilities for the ETL pipeline:
- Configuration management
- Global variables and Spark session management
- File operations
"""

from adventure_works.utils.file import load_config  # noqa: F401
from adventure_works.utils.globals import GlobalVariables  # noqa: F401

__all__ = ["load_config", "GlobalVariables"]

