"""Text utility functions."""


def _collapse_spaces(text):
    """Collapse repeated whitespace to single spaces.

    Internal helper.
    """
    raise NotImplementedError


def clean_name(value):
    """Return a cleaned display name.

    Convert value to string, strip surrounding whitespace, and collapse
    repeated internal whitespace. Raise ValueError if the cleaned result
    is empty.
    """
    raise NotImplementedError


def slugify(value):
    """Return a simple lowercase hyphen-separated slug.

    Example:
        "  Ada Lovelace  " -> "ada-lovelace"

    Only letters, digits, and single hyphens should remain.
    Raise ValueError when no usable characters remain.
    """
    raise NotImplementedError
