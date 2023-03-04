from re import Pattern
from typing import NamedTuple

from magicregex import MagicRegex


class TestCaseTuple(NamedTuple):
    test_case: MagicRegex
    expected_result: Pattern
