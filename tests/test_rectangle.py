from src.Rectangle import Rectangle
from src.Circle import Circle
import pytest


def test_rectangle_positive_1():
    rectangle = Rectangle(3, 9)
    assert rectangle.area == 27, 'Incorrect area'
    assert rectangle.perimeter == 24, 'Incorrect perimetr'


def test_rectangle_positive_2():
    Rectangle(8, 1)


def test_rectangle_area():
    rectangle = Rectangle(3, 9)
    circle = Circle(7)
    assert rectangle.add_area(circle) == 180, 'Wrong result'


def test_rectangle_negative_2():
    with pytest.raises(ValueError):
        Rectangle(-1, 9)


def test_rectangle_negative_3():
    with pytest.raises(ValueError):
        Rectangle(3, 0)
