from .duplicate_encoder import duplicate_encode


def test_01():
    assert duplicate_encode("din") == "((("


def test_02():
    assert duplicate_encode("recede") == "()()()"


def test_03():
    assert duplicate_encode("Success") == ")())())"


def test_04():
    assert duplicate_encode("(( @") == "))(("
