class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        try:
            calc = (float(_length) * float(_width) * 25 * 5) / 1000
            print(f'{calc} тонн')

        except:
            msg = 'Некорректный ввод!'
            raise ValueError(msg)


a = Road(20, 5000)
