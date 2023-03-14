from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__()
        self.name = 'Triangle'
        if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a or  \
                side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('Cannot create triangle with such sides')
        self.sides = (side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        p = sum(self.sides) / 2
        self.area = int((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5)
        self.perimeter = sum(self.sides)
