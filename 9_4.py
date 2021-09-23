import random


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print(f'Машина {Car.name} поехала')

    def stop(self):
        print(f'Машина {Car.name} остановилась')

    def turn(self):
        direction = ('влево', 'вправо', 'назад')
        d = random.choice(direction)
        print(f'Машина {Car.name} повернула {d}')

    def show_speed(self):
        print(f'Скорость  {Car.name} - {Car.speed} км/ч')


class TownCar(Car):
    def __init__(self, name, color, speed):
        Car.name = name
        Car.color = color
        Car.speed = int(speed)
        Car.is_police = False

    def show_speed(self):
        if Car.speed > 60:
            print(f'Скорость {Car.name} - {Car.speed} км/ч. Превышение!')
        else:
            print(f'Скорость {Car.name} - {Car.speed} км/ч')


class SportCar(Car):
    def __init__(self, name, color, speed):
        Car.name = name
        Car.color = color
        Car.speed = speed
        Car.is_police = False


class WorkCar(Car):
    def __init__(self, name, color, speed):
        Car.name = name
        Car.color = color
        Car.speed = int(speed)
        Car.is_police = False

    def show_speed(self):
        if Car.speed > 40:
            print(f'Скорость {Car.name} - {Car.speed} км/ч. Превышение!')
        else:
            print(f'Скорость {Car.name} - {Car.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        Car.name = name
        Car.color = color
        Car.speed = speed
        Car.is_police = True


a = TownCar('Volkswagen', 'зеленый', '80')
a.go()
a.show_speed()
a.turn()
a.stop()


b = SportCar('Lamborghini', 'красный', '160')
b.go()
b.show_speed()
b.turn()
b.stop()

c = WorkCar('Lada', 'черный', '60')
c.go()
c.show_speed()
c.turn()
c.stop()

d = PoliceCar('Ford', 'синий', '80')
d.go()
d.show_speed()
d.turn()
d.stop()

