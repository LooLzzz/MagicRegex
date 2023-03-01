import re
from typing import Set, Union

from . import tokens


class MagicRegex:
    def __init__(self, flags: re.RegexFlag = 0):
        self._base_token: tokens.BaseToken = tokens.EmptyToken()
        self._flags = flags

    def __repr__(self):
        return f'<MagicRegex({self.pattern!r}, flags={self._flags!r})>'

    def __eq__(self, other: Union['MagicRegex', str]):
        if isinstance(other, MagicRegex):
            return self.pattern == other.pattern
        elif isinstance(other, str):
            return self.pattern == other
        else:
            raise TypeError(f'Unsupported operand type(s) for ==: {type(self)} and {type(other)}')

    def __add__(self, other: Union['MagicRegex', tokens.BaseToken]):
        if isinstance(other, MagicRegex):
            if other._flags != self._flags:
                raise ValueError('Cannot add two MagicRegex objects with different flags')
            self._base_token += other._base_token
        elif isinstance(other, tokens.BaseToken):
            self._base_token += other
        else:
            raise TypeError(f'Unsupported operand type(s) for +: {type(self)} and {type(other)}')
        return self

    @property
    def pattern(self):
        return self._base_token.expression()

    @property
    def _right_most_token(self):
        return self._base_token.right_most_token

    def compile(self):
        return re.compile(
            pattern=self.pattern,
            flags=self._flags
        )

    def expr(self, other: Union[str, tokens.BaseToken]):
        self._base_token += (tokens.ExpressionToken(other)
                             if isinstance(other, str)
                             else other)
        return self

    def OR(self, other: Union[str, tokens.BaseToken]):
        self._base_token += tokens.OrToken(other)
        return self

    def capture_group(self):
        self._base_token = tokens.CaptureGroupToken(self._base_token)
        return self

    def named_capture_group(self, name: str):
        self._base_token = tokens.NamedCaptureGroupToken(name, self._base_token)
        return self

    def start_of_line(self):
        self._base_token += tokens.ExpressionToken(r'^')
        return self

    def end_of_line(self):
        self._base_token += tokens.ExpressionToken(r'$')
        return self

    def any_character(self):
        self._base_token += tokens.ExpressionToken(r'.')
        return self

    def digit(self):
        self._base_token += tokens.ExpressionToken(r'\d')
        return self

    def whitespace(self):
        self._base_token += tokens.ExpressionToken(r'\s')

    def at_least_zero_times(self):
        self._base_token = (tokens.CaptureGroupToken(self._right_most_token)
                            + tokens.ExpressionToken(r'*'))
        return self

    def at_least_once(self):
        self._base_token = (tokens.CaptureGroupToken(self._right_most_token)
                            + tokens.ExpressionToken(r'+'))
        return self

    def any_characters(self, characters: Set[str]):
        self._base_token += tokens.AnyCharactersToken(characters)
        return self

    def not_characters(self, characters: Set[str]):
        self._base_token += tokens.NotCharactersToken(characters)
        return self

    def times(self, times: Union[int, range, tuple[int, int]]):
        if isinstance(times, range):
            times = (times.start, times.stop)

        self._base_token = tokens.TimesToken(times, tokens.CaptureGroupToken(self._right_most_token))
        return self
