'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
 желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
'''

#не совсем понял, что здесь требуется и выполнил следующим образом. Надеюсь это правильно :)

class TrafficLight:
    __color = None

    def running(self):
        self.__color = 'Red'
        print(f'{self.__color} горит 7 секунд')
        self.__color = 'Yellow'
        print(f'{self.__color} горит 2 секунды')
        self.__color = 'Green'
        print(f'{self.__color} горит 10 секунд')


traffic_light = TrafficLight()
traffic_light.running()

