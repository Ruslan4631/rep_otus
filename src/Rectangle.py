from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int, side_b: int):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError('Cannot create rectangle with such sides')
        self.name = 'Rectangle'
        self.side_a = side_a
        self.side_b = side_b
        self.area = side_a * side_b
        self.perimeter = 2 * (side_a + side_b)
