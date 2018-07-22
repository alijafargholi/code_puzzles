from .balance_brackets import main


def test_balanced_brackets_pass():

    assert main("{[()]}") is True
    assert main("{[(])}") is False

    assert main("[]{}()") is True

    assert main("{()[][{}]}") is True
    assert main("({}{[]})({)}") is False
    assert main("()[]") is True
    assert main("[()][{}]{[({})[]]}") is True
    assert main("((){)}") is False
    assert main("{'foo': 'bar', 1: [1, 2, 3], 'bar': ('s')}") is True