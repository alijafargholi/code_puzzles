"""
Source
^^^^^^

https://www.codewars.com/kata/the-observed-pin/train/python

"""
import itertools

PAD_LOCK = """
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
"""


def get_pins(observed):
    """

    :param observed:
    :return:
    """

    combination_keys = {'0': ['0', '8'],
                        '1': ['1', '2', '4'],
                        '2': ['2', '1', '3', '5'],
                        '3': ['3', '2', '6'],
                        '4': ['4', '1', '5', '7'],
                        '5': ['5', '2', '4', '6', '8'],
                        '6': ['6', '3', '5', '9'],
                        '7': ['7', '4', '8'],
                        '8': ['8', '5', '7', '9', '0'],
                        '9': ['9', '6', '8']}

    combination_possibilities = [combination_keys.get(_) for _ in observed]
    result = [''.join(i) for i in itertools.product(*combination_possibilities)]

    return result


if __name__ == '__main__':
    get_pins('369')
