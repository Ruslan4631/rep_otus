from src.Square import Square
from src.Rectangle import Rectangle
import pytest


def test_square_positive_1():
    square = Square(7)
    assert square.area == 49, 'Incorrect area'
    assert square.perimeter == 28, 'Incorrect perimetr'


def test_square_positive_2():
    Square(7)


def test_square_area():
    square = Square(9)
    rectangle = Rectangle(7, 3)
    assert square.add_area(rectangle) == 102, 'Wrong result'


def test_square_negative_2():
    with pytest.raises(ValueError):
        Square(0)


def test_square_negative_3():
    with pytest.raises(ValueError):
        Square(-7)
