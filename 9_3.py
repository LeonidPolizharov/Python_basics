class Worker:
    def __init__(self, name='', surname='', wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход: {total_income}')


a = Position('Oleg', 'Petrov', 50000, 15000)
a.get_full_name()
a.get_total_income()

b = Position('Вячеслав', 'Добрынин', 70000, 18000)
b.get_full_name()
b.get_total_income()
