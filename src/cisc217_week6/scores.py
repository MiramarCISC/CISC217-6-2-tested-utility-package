"""Score-related utilities."""


def _to_float(value):
    """Convert a value to float.

    Internal helper.
    """
    raise NotImplementedError


def _validate_score(score):
    """Return score if it is between 0 and 100 inclusive.

    Raise ValueError when the score is outside the valid range.
    Internal helper.
    """
    raise NotImplementedError


def normalize_scores(values):
    """Return valid scores converted to floats.

    Raise ValueError when any item is invalid.
    """
    raise NotImplementedError


def average_score(values):
    """Return the average score rounded to two decimals.

    Return 0.0 for an empty collection.
    Raise ValueError when a non-empty input contains an invalid score.
    """
    raise NotImplementedError
