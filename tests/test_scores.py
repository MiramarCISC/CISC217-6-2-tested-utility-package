import pytest

from cisc217_week6 import average_score, normalize_scores


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([0, 50, 100], [0.0, 50.0, 100.0]),
        (["88.5", "91"], [88.5, 91.0]),
        ((75, 80.25), [75.0, 80.25]),
    ],
)
def test_normalize_scores_accepts_valid_values(values, expected):
    assert normalize_scores(values) == expected


@pytest.mark.parametrize(
    "values",
    [
        [-1],
        [101],
        ["bad"],
        [None],
        [50, "oops", 70],
    ],
)
def test_normalize_scores_rejects_invalid_values(values):
    with pytest.raises(ValueError):
        normalize_scores(values)


def test_average_score_returns_zero_for_empty_input():
    assert average_score([]) == 0.0


def test_average_score_rounds_to_two_decimals():
    assert average_score([80, 90, 95]) == 88.33


def test_average_score_accepts_numeric_strings():
    assert average_score(["90", "95"]) == 92.5


def test_average_score_rejects_invalid_score():
    with pytest.raises(ValueError):
        average_score([90, 120])
