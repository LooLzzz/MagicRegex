from magicregex import MagicRegex, tokens

# TODO


def test_import():
    assert MagicRegex().digit().pattern == r'\d'
    assert MagicRegex().digit().named_capture_group('digit').pattern == r'(?P<digit>\d)'


def test_tokens():
    print(tokens.ExpressionToken(r'^').expression())
