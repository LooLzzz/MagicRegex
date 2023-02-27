import re

import pytest

from magicregex import MagicRegex


def test_add__raises():
    match = 'Cannot add two MagicRegex objects with different flags'
    with pytest.raises(ValueError, match=match):
        _ = MagicRegex() + MagicRegex(flags=re.IGNORECASE)

    with pytest.raises(ValueError, match=match):
        _ = MagicRegex(flags=re.IGNORECASE) + MagicRegex()

    with pytest.raises(ValueError, match=match):
        _ = MagicRegex(flags=re.MULTILINE) + MagicRegex(flags=re.IGNORECASE)


def test_add__passes():
    _ = MagicRegex() + MagicRegex()
    _ = MagicRegex(flags=re.IGNORECASE) + MagicRegex(flags=re.IGNORECASE)
    _ = MagicRegex(flags=re.MULTILINE) + MagicRegex(flags=re.MULTILINE)


def test_regex_output():
    assert r'(abc){3}' == (MagicRegex().expr('abc')
                                       .times(3)
                                       .raw)

    assert r'(abc){3}' == (MagicRegex(flags=re.IGNORECASE).expr('abc')
                                                          .times(3)
                                                          .raw)
