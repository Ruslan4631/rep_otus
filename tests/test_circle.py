from src.Circle import Circle
from src.Square import Square
import pytest


def test_circle_positive_1():
    circle = Circle(3)
    assert circle.area == 28, 'Incorrect area'
    assert circle.perimeter == 18, 'Incorrect perimetr'


def test_circle_positive_2():
    Circle(5)


def test_circle_area():
    circle = Circle(7)
    square = Square(5)
    assert circle.add_area(square) == 178, 'Wrong result'


def test_circle_negative_2():
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_negative_3():
    with pytest.raises(ValueError):
        Circle(-7)
