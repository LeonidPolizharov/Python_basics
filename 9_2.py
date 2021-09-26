class Road:
    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def calculate(self):
        try:
            calc = (float(self._length) * float(self._width) * 25 * 5) / 1000
            print(f'{calc} тонн')

        except ValueError:
            msg = 'Некорректный ввод!'
            raise ValueError(msg)


a = Road(20, 5000)
a.calculate()
