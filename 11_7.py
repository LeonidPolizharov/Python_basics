class ComplexOperation:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'Сложение z1 и z2: z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Умножение z1 и z2: z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexOperation(6, 7)
z_2 = ComplexOperation(-4, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)