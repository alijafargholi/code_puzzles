"""
Build a Pile of Cubes
=====================

Your task is to construct a building which will be a pile of n cubes. The cube
at the bottom will have a volume of n^3, the cube above will have volume of
(n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find
the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an
integer m and you have to return the integer n such as
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Source
^^^^^^

https://www.codewars.com/kata/build-a-pile-of-cubes/train/python

"""


def find_nb(m: int) -> int:
    """Find the number n of cubes we will have to build"""
    n = 2
    result = 0

    # Clue --> 1^3 + 2^3 + 3^3 + 4^3 + ... n^3 = (1 + 2 + 3 +...n)^2
    while result < m:
        result = pow(sum(range(n)), 2)
        if result == m:
            return n-1
        n += 1

    return -1
