from abc import ABC, abstractmethod
from typing import Set, Tuple, Union


class BaseToken(ABC):
    """base class for all MagicRegex tokens"""

    @abstractmethod
    def expression(self) -> str:
        ...

    def __add__(self, other: 'BaseToken'):
        return ConcatToken(self, other)

    @property
    def right_most_token(self) -> 'BaseToken':
        return self

    def AND(self, other: 'BaseToken'):
        return self + other


class EmptyToken(BaseToken):
    def expression(self):
        return ''

    def __add__(self, other: 'BaseToken'):
        return other


class ConcatToken(BaseToken):
    def __init__(self, a: BaseToken, b: BaseToken):
        self._a = a
        self._b = b

    @property
    def right_most_token(self) -> 'BaseToken':
        return self._b.right_most_token

    def expression(self):
        return self._a.expression() + self._b.expression()


class ExpressionToken(BaseToken):
    def __init__(self, expr: str):
        self._expr = expr

    def expression(self):
        return self._expr


class OrToken(BaseToken):
    """`r'(expr1|expr2)'`"""

    def __init__(self, a: BaseToken, b: BaseToken):
        self._a = a
        self._b = b

    @property
    def right_most_token(self) -> 'BaseToken':
        return self._b.right_most_token

    def expression(self):
        return rf'({self._a.expression()}|{self._b.expression()})'


class CaptureGroupToken(BaseToken):
    """`r'(expr)'`"""

    def __init__(self, pattern: BaseToken):
        self._pattern = pattern

    def expression(self):
        return rf'({self._pattern.expression()})'


class NamedCaptureGroupToken(BaseToken):
    """`r'(?P<name>expr)'`"""

    def __init__(self, name: str, expr: BaseToken):
        self._name = name
        self._expr = expr

    def expression(self):
        return rf'(?P<{self._name}>{self._expr.expression()})'


class AnyCharactersToken(BaseToken):
    """`[characters]`"""

    def __init__(self, characters: Set[str]):
        self._characters = characters

    def expression(self):
        return f'[{"".join(self._characters)}]'


class NotCharactersToken(BaseToken):
    """`[^characters]`"""

    def __init__(self, characters: Set[str]):
        self._characters = characters

    def expression(self):
        return f'[^{"".join(self._characters)}]'


class TimesToken(BaseToken):
    """`{n}` or `{n,m}`"""

    def __init__(self, times: Union[int, Tuple[int, int]], expr: BaseToken):
        self._times = times
        self._expr = expr

    def expression(self):
        if isinstance(self._times, tuple):
            return f'{self._expr.expression()}{{{self._times[0]},{self._times[1]}}}'
        return f'{self._expr.expression()}{{{self._times}}}'
