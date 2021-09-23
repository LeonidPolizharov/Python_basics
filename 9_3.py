class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        Worker.name = name
        Worker.surname = surname
        Worker._income['wage'] = wage
        Worker._income['bonus'] = bonus

    def get_full_name(self):
        print(f'Полное имя: {Worker.name} {Worker.surname}')

    def get_total_income(self):
        total_income = Worker._income['wage'] + Worker._income['bonus']
        print(f'Доход: {total_income}')


a = Position('Oleg', 'Petrov', 50000, 15000)
a.get_full_name()
a.get_total_income()

b = Position('Вячеслав', 'Добрынин', 70000, 18000)
b.get_full_name()
b.get_total_income()

