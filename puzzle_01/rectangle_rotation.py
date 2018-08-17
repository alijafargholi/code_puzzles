"""
Source
^^^^^^
https://www.codewars.com/kata/simple-fun-number-27-rectangle-rotation/train/python

A rectangle with sides equal to even integers a and b is drawn on the Cartesian
plane. Its center (the intersection point of its diagonals) coincides with the
point (0, 0), but the sides of the rectangle are not parallel to the axes;
instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle?
"""
from math import cos, sin, radians, pow, sqrt
from itertools import product

ANGLE = radians(-45)


def rectangle_rotation(a, b):
    """How many points with integer coordinates are located inside
    the given rectangle

    :type a: int
    :param a: length of the rectangle
    :type b: int
    :param b: width of the rectangle
    :rtype: int
    :return: Number of points that are located inside the rectangle.
    """

    counter = []
    width = a//2
    height = b//2
    radius = int(sqrt(pow(a, 2) + pow(b, 2)))//2
    ranges = range(-radius, radius+1)

    for old_x, old_y in product(ranges, ranges):
        x, y = get_rotated_point(old_x, old_y)
        if -width < x < width and -height < y < height:
            counter.append((x, y))

    return len(set(counter))


def get_rotated_point(x, y):
    new_x = (x * cos(ANGLE)) - (y * sin(ANGLE))
    new_y = (x * sin(ANGLE)) + (y * cos(ANGLE))
    return new_x, new_y

