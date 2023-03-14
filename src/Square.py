from src.Figure import Figure


class Square(Figure):
    def __init__(self, side: int):
        super().__init__()
        if side <= 0:
            raise ValueError('Cannot create square with such side')
        self.name = 'Square'
        self.side = side
        self.area = pow(side, 2)
        self.perimeter = 4 * side
