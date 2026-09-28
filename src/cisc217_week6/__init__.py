"""Public API for the CISC 217 Week 6 utility package."""

from .scores import average_score, normalize_scores
from .text_tools import clean_name, slugify
from .file_tools import read_lines, write_lines

__all__ = [
    "average_score",
    "normalize_scores",
    "clean_name",
    "slugify",
    "read_lines",
    "write_lines",
]
