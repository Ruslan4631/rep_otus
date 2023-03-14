from src.Triangle import Triangle
from src.Square import Square
import pytest


def test_triangle_positive_1():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == 6, 'Incorrect area'
    assert triangle.perimeter == 12, 'Incorrect perimetr'


def test_triangle_positive_2():
    Triangle(7, 7, 7)


def test_triangle_area():
    triangle = Triangle(7, 8, 9)
    square = Square(5)
    assert triangle.add_area(square) == 51, 'Wrong result'


def test_triangle_negative_2():
    with pytest.raises(ValueError):
        Triangle(0, 1, 2)


def test_triangle_negative_3():
    with pytest.raises(ValueError):
        Triangle(-1, 1, 7)
