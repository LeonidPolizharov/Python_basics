class NumCheck(Exception):
    def __init__(self):
        self.num_list = []

    def my_input(self):
        while True:
            try:
                num = input('Введите число или "stop" для выхода: ')
                if '.' in num:
                    val = float(num)
                elif num == 'stop':
                    print(f'Cписок: {self.num_list} \n ')
                    break
                else:
                    val = int(num)
                self.num_list.append(val)

            except:
                print(f"Недопустимое значение!")


test = NumCheck()
test.my_input()
