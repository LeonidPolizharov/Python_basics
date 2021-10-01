from abc import ABC, abstractmethod


class Clothes:
    all_clothes = 0

    def __init__(self, setting):
        self.setting = setting

    @abstractmethod
    def calculate(self):
        calc = 'abstract calc'
        return calc

    def __add__(self, other):
        Clothes.all_clothes += self.calculate + other.calculate


class Coat(Clothes):
    @property
    def calculate(self):
        calc = (self.setting / 6.5 + 0.5)
        return calc


class Suit(Clothes):
    @property
    def calculate(self):
        calc = (2 * self.setting + 0.3)
        return calc


a = Coat(52)
print(a.calculate)

b = Suit(24)
print(b.calculate)

c = a.calculate + b.calculate
print(c)


