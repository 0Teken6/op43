class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def describe_car(self):
        print(f'color: {self.color}')

    def __str__(self):
        return (f'model: {self.model}\n'
                f'color: {self.color}\n')


class Car2(Car):
    def __init__(self, model, color, year):
        super().__init__(model, color)
        self.year = year

    def describe_car(self):
        super().describe_car()
        print(f'year: {self.year}')

    def __str__(self):
        return super().__str__() + f'year: {self.year}\n'


c1 = Car2('BMW', "black", 2022)
print(c1)
c1.describe_car()