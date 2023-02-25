import re
from typing import List, Set, Union


class MagicRegexExpression:
    ...


class MagicRegex:
    def __init__(self, flags: re.RegexFlag = 0):
        self._expression = ''
        self._flags = flags

    def _compile(self):
        return re.compile(self._expression, self._flags)

    def AND(self, expr: Union[str, MagicRegexExpression]):
        """`rf'({expr1}{expr2})'`"""
        return self

    def OR(self, expr: Union[str, MagicRegexExpression]):
        """`rf'({expr1}|{expr2})'`"""
        return self

    def named_group(self, name: str, expr: Union[str, MagicRegexExpression]):
        """`rf'(?P<{name}>{expr})'`"""
        return self

    def start_of_line(self):
        """`r'^...'`"""
        return self

    def end_of_line(self):
        """`r'...$'`"""
        return self

    def any_character(self):
        """`r'.'`"""
        return self

    def any_characters(self, characters: Set[str]):
        """`rf'[{characters}]'`"""
        return self

    def not_characters(self, characters: Set[str]):
        """`rf'[^{characters}]'`"""
        return self

    def digit(self):
        """`r'\d'`"""
        return self

    def whitespace(self):
        """`r'\s'`"""
        return self

    def at_least_zero_times(self, expr: Union[str, MagicRegexExpression]):
        """`rf'({expr})*'`"""
        return self

    def at_least_once(self, expr: Union[str, MagicRegexExpression]):
        """`rf'({expr})+'`"""
        return self

    def times(self, n: int):
        """`rf'{{{n}}}'`"""
        return self
