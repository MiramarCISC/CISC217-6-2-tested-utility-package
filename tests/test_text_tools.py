import pytest

from cisc217_week6 import clean_name, slugify


def test_clean_name_strips_and_collapses_whitespace():
    assert clean_name("  Ada    Lovelace  ") == "Ada Lovelace"


def test_clean_name_converts_non_string_value():
    assert clean_name(12345) == "12345"


@pytest.mark.parametrize("value", ["", "   ", "\t\n"])
def test_clean_name_rejects_empty_result(value):
    with pytest.raises(ValueError):
        clean_name(value)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Ada Lovelace", "ada-lovelace"),
        ("  Grace   Hopper  ", "grace-hopper"),
        ("CISC 217!", "cisc-217"),
        ("Python_Utilities", "python-utilities"),
        ("Room #42", "room-42"),
    ],
)
def test_slugify(value, expected):
    assert slugify(value) == expected


@pytest.mark.parametrize("value", ["!!!", "---", "   "])
def test_slugify_rejects_unusable_text(value):
    with pytest.raises(ValueError):
        slugify(value)
