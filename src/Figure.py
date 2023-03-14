class Figure:
    def __init__(self):
        self.name = None
        self.area = None
        self.perimeter = None

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('There are not such figure')
        return int(self.area + figure.area)
