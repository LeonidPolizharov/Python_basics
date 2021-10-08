class MyZeroDiv(Exception):
    def __init__(self, message):
        self.message = message


div1 = input('Введите делимое: ')
div2 = input('Введите делитель: ')

try:
    div1 = int(div1)
    div2 = int(div2)
    if div2 == 0:
        raise MyZeroDiv('Делить на ноль нельзя!')
except (ValueError, MyZeroDiv) as err:
    print(err)
else:
    print(f'{div1} / {div2} = {div1 / div2:.2f}')
