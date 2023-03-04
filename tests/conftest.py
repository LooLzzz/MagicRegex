import re

import pytest

from magicregex import MagicRegex, tokens

from .types import TestCaseTuple


@pytest.fixture
def bad_additions():
    return [
        (MagicRegex(), MagicRegex(flags=re.IGNORECASE)),
        (MagicRegex(flags=re.IGNORECASE), MagicRegex()),
        (MagicRegex(flags=re.MULTILINE), MagicRegex(flags=re.IGNORECASE)),
    ]


@pytest.fixture
def good_additions():
    return [
        (MagicRegex() for _ in range(2)),
        (MagicRegex() for _ in range(3)),
        (MagicRegex() for _ in range(10)),
        (MagicRegex(flags=re.IGNORECASE) for _ in range(2)),
        (MagicRegex(flags=re.MULTILINE) for _ in range(2)),
        (MagicRegex(flags=re.MULTILINE), tokens.ExpressionToken('abc')),
    ]


@pytest.fixture
def regex_outputs():
    return map(TestCaseTuple, [
        (
            re.compile(r'\d'),
            MagicRegex().digit()
        ),
        (
            re.compile(r'.'),
            MagicRegex().any_character()
        ),
        (
            re.compile(r'^'),
            MagicRegex().start_of_line()
        ),
        (
            re.compile(r'$'),
            MagicRegex().end_of_line()
        ),
        (
            re.compile(r'(abc){3}'),
            MagicRegex().expr('abc')
                        .times(3)
        ),
        (
            re.compile(r'(abc){3}', flags=re.IGNORECASE),
            MagicRegex(flags=re.IGNORECASE).expr('abc')
                                           .times(3)
        )
    ])
