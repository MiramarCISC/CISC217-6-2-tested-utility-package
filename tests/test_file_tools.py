from pathlib import Path

import pytest

from cisc217_week6 import read_lines, write_lines


def test_write_lines_creates_parent_directory(tmp_path):
    path = tmp_path / "output" / "names.txt"

    result = write_lines(path, ["Ada", "Grace"])

    assert isinstance(result, Path)
    assert result == path
    assert path.exists()


def test_write_lines_and_read_lines_round_trip(tmp_path):
    path = tmp_path / "names.txt"

    write_lines(path, ["Ada", "Grace", "李雷"])

    assert read_lines(path) == ["Ada", "Grace", "李雷"]


def test_read_lines_strips_and_skips_blank_lines(tmp_path):
    path = tmp_path / "names.txt"
    path.write_text("  Ada  \n\nGrace\n   \nLinus  \n", encoding="utf-8")

    assert read_lines(path) == ["Ada", "Grace", "Linus"]


def test_read_lines_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        read_lines(tmp_path / "missing.txt")
