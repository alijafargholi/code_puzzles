from .rectangle_rotation import rectangle_rotation


def test_01():
    assert rectangle_rotation(6, 4) == 23


def test_02():
    assert rectangle_rotation(30, 2) == 65


def test_03():
    assert rectangle_rotation(8, 6) == 49


def test_04():
    assert rectangle_rotation(16, 20) == 333
