from magicregex import MagicRegex, tokens

# TODO


def test_import():
    assert MagicRegex().digit().raw == r'\d'
    assert MagicRegex().digit().named_capture_group('digit').raw == r'(?P<digit>\d)'


def test_tokens():
    print(tokens.ExpressionToken(r'^').expression())
