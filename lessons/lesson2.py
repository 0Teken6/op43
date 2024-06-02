class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return (f'model: {self.model}\n'
                f'color: {self.color}\n')


class Car2(Car):
    def __init__(self, model, color, year):
        super().__init__(model, color)
        self.year = year

    def __str__(self):
        return (f'{super().__str__()}'
                f'year: {self.year}\n')


c1 = Car2('BMW', "black", 2022)
print(c1)