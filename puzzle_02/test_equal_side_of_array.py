from .equal_side_of_array import find_even_index


def test_01():
    assert find_even_index([1,2,3,4,3,2,1]) == 3


def test_02():
    assert find_even_index([1,100,50,-51,1,1]) == 1


def test_03():
    assert find_even_index([1,2,3,4,5,6]) == -1


def test_04():
    assert find_even_index([20,10,30,10,10,15,35]) == 3


def test_05():
    assert find_even_index([20,10,-80,10,10,15,35]) == 0


def test_06():
    assert find_even_index([10,-80,10,10,15,35,20]) == 6


def test_07():
    assert find_even_index(range(1,100)) == -1


def test_08():
    assert find_even_index([0,0,0,0,0]) == 0


def test_09():
    assert find_even_index([-1,-2,-3,-4,-3,-2,-1]) == 3


def test_10():
    assert find_even_index(range(-100,-1)) == -1
