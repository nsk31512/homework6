'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
 сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
 вызов методов и также покажите результат.
'''


class Car:

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} тронулся')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name} {self.speed} км/ч. Превышение скорости! Снизьте скорость!')
        else:
            print(f'Текущая скорость {self.name} {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.speed} км/ч. Превышение скорости! Снизьте скорость!')
        else:
            print(f'Текущая скорость {self.speed} км/ч.')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police, power):
        Car.__init__(self, speed, color, name, is_police)
        self.power = power

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

    def show_power(self):
        print(f'Мощность автомобиля - {self.power} л.с.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police, is_radar):
        Car.__init__(self, speed, color, name, is_police)
        self.is_radad = is_radar

    def try_check_speed(self):
        if self.is_police:
            print('Контроль скорости доступен')
        else:
            print('Отсутствует радар для контроля скорости')


volvo = TownCar(55, 'Grey', 'Volvo', False)
bmw = TownCar(70, 'black', 'BMW', False)
truck = WorkCar(35, 'red', 'zil', False)
long_truck = WorkCar (60, 'white', 'MAN', False)
ferrari = SportCar(110, 'red', 'Ferrari 550', False, 350)
porsh = SportCar(200, 'black', 'Porsche 911', False, 400)
patrol = PoliceCar(60, 'black&white', 'Патрульный Ford', True, True)
detective_car = PoliceCar(60, 'blue', 'Служебный Chevrolet', True, False)

volvo.go()
volvo.show_speed()
volvo.turn('Left')
volvo.stop()
print('-' * 10)

bmw.go()
bmw.show_speed()
bmw.turn('right')
bmw.stop()
print('-' * 10)

truck.go()
truck.show_speed()
truck.turn('left')
truck.stop()
print('-' * 10)

long_truck.go()
long_truck.show_speed()
long_truck.turn('right')
long_truck.stop()
print('-' * 10)

ferrari.go()
ferrari.show_speed()
ferrari.show_power()
ferrari.turn('Left')
ferrari.stop()
print('-' * 10)

porsh.go()
porsh.show_speed()
porsh.show_power()
porsh.turn('right')
porsh.stop()
print('-' * 10)

patrol.go()
patrol.show_speed()
patrol.try_check_speed()
patrol.turn('right')
patrol.stop()
print('-' * 10)

detective_car.go()
detective_car.show_speed()
detective_car.try_check_speed()
detective_car.turn('right')
detective_car.stop()
print('-' * 10)
