import cisc217_week6


def test_expected_public_names_are_available():
    expected = {
        "average_score",
        "normalize_scores",
        "clean_name",
        "slugify",
        "read_lines",
        "write_lines",
    }

    assert expected.issubset(set(dir(cisc217_week6)))


def test_private_helpers_are_not_exported_through_all():
    assert "_to_float" not in cisc217_week6.__all__
    assert "_validate_score" not in cisc217_week6.__all__
    assert "_collapse_spaces" not in cisc217_week6.__all__
