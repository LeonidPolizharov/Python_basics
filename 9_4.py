import random


class Car:
    def __init__(self, name='', color='', speed=0, is_police=None):
        self.name = name
        self.color = color
        self.speed = int(speed)
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        direction = ('влево', 'вправо', 'назад')
        direct = random.choice(direction)
        print(f'Машина {self.name} повернула {direct}')

    def show_speed(self):
        print(f'Скорость  {self.name} - {self.speed} км/ч')


class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} - {self.speed} км/ч. Превышение!')
        else:
            print(f'Скорость {self.name} - {self.speed} км/ч')


class SportCar(Car):
    is_police = False


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} - {self.speed} км/ч. Превышение!')
        else:
            print(f'Скорость {self.name} - {self.speed} км/ч')


class PoliceCar(Car):
    Car.is_police = True


a = TownCar('Volkswagen', 'зеленый', 80, False)
a.go()
a.show_speed()
a.turn()
a.stop()


b = SportCar('Lamborghini', 'красный', 160, False)
b.go()
b.show_speed()
b.turn()
b.stop()

c = WorkCar('Lada', 'черный', 60, False)
c.go()
c.show_speed()
c.turn()
c.stop()

d = PoliceCar('Ford', 'синий', 80, True)
d.go()
d.show_speed()
d.turn()
d.stop()
