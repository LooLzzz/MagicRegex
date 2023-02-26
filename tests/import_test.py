import re

from ..src.magic_regex import MagicRegex


assert MagicRegex().digit().raw == r'\d'
assert MagicRegex().digit().named_capture_group('digit').raw == r'(?P<digit>\d)'
