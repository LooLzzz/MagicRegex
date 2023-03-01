import re
from functools import reduce
from typing import List, Tuple

import pytest
from pytest_subtests import SubTests

from magicregex import MagicRegex


def test_add__raises(subtests: SubTests,
                     bad_additions: List[Tuple[MagicRegex]]):
    match = 'Cannot add two MagicRegex objects with different flags'
    for test_case in bad_additions:
        with subtests.test():
            with pytest.raises(ValueError, match=match):
                _ = reduce(lambda a, b: a + b, test_case)


def test_add__raises(subtests: SubTests,
                     good_additions: List[Tuple[MagicRegex]]):
    for test_case in good_additions:
        with subtests.test():
            _ = reduce(lambda a, b: a + b, test_case)


def test_regex_output(subtests: SubTests,
                      regex_outputs: List[Tuple[re.Pattern, MagicRegex]]):
    for expected_result, test_case in regex_outputs:
        with subtests.test():
            assert expected_result.pattern == test_case.pattern
            assert expected_result == test_case.compile()
