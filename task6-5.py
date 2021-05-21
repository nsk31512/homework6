'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
 (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
 Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
 выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
 экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет чернилами')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует. Его можно стереть')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует и закрашивает. Им можно выделить текст')


brush = Stationery('Кисть')
brush.draw()
print('-' * 10)

grey_pencil = Pencil('Простой карандаш')
grey_pencil.draw()
print('-' * 10)

gel_pen = Pen('Гелевая ручка')
gel_pen.draw()
print('-' * 10)

highlighter = Handle('Выделитель текста')
highlighter.draw()
print('-' * 10)
