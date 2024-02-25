# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math


class Circle:

    __pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return 2 * self.__pi * self.radius

    def circle_area(self):
        return self.__pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5)

    print(f'{circle.circle_area() = }\n'
          f'{circle.circle_length() = }')
