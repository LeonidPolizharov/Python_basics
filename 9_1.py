import time


class TrafficLight:
    __color = ('красный', 'желтый', 'зеленый')

    def running(self):
        while 1 == 1:
            for i, j in enumerate(TrafficLight.__color):
                if i == 0:
                    print(f'\033[31m{j}')
                    time.sleep(7)
                elif i == 1:
                    print(f'\033[33m{j}')
                    time.sleep(2)
                else:
                    print(f'\033[32m{j}')
                    time.sleep(7)


a = TrafficLight()
a.running()
