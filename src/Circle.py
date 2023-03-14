import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        super().__init__()
        if radius <= 0:
            raise ValueError('Cannot create with such radius')
        self.name = 'Circle'
        self.radius = radius
        self.area = int(math.pi * pow(radius, 2))
        self.perimeter = int(2 * math.pi * radius)
