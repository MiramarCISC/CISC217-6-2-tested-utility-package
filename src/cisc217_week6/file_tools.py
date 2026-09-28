"""UTF-8 text-file utilities."""

from pathlib import Path


def read_lines(path):
    """Return nonblank stripped lines from a UTF-8 text file.

    Raise FileNotFoundError when the file does not exist.
    """
    raise NotImplementedError


def write_lines(path, lines):
    """Write lines as UTF-8 text, one line per item.

    Create the parent directory if needed and return the Path written.
    """
    raise NotImplementedError
