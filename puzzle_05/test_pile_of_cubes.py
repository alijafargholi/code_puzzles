from .pile_of_cubes import find_nd


def test_00():
    assert find_nd(1071225) == 45


def test_01():
    assert find_nd(4183059834009) == 2022


def test_02():
    assert find_nd(24723578342962) == -1


def test_03():
    assert find_nd(135440716410000) == 4824


def test_04():
        assert find_nd(40539911473216) == 3568


def test_05():
    assert find_nd(26825883955641) == 3218
