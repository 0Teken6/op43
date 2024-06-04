
# принципы ООП
# 4 наследование полиморфизм
# инкапсуляция абстракция

class BigO:
    def __init__(self): ...

    def res(self):
        print('метод класса 1')


class BigO2(BigO):

    def res(self):
        print('метод класса 2 ')
        super().res()


a = BigO()
b = BigO2()


# уровни доступа 3
# 1 публичный  2 защищенный _  3 скрытый __


class Bank:
    def __init__(self, name, balance, pin, svv):
        self.name = name
        self.__balance = balance
        self._pin = pin
        self.svv = svv

    def result(self):
        print(self._pin, self.svv)

    def __str__(self):
        return f'{self.name} {self.__balance}'


beka = Bank('beka', 1000, 2525, 644)
beka1 = Bank('beka', 1000, 2525, 644)

print(beka._pin)
print(dir(beka))
beka._pin = 10
print(beka._pin)

