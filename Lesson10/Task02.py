# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def rectangle_area(self):
        return self.width * self.length

    def rectangle_perimeter(self):
        return (self.width + self.length) * 2


if __name__ == '__main__':
    rectangle = Rectangle(5, 7)
    square = Rectangle(3)

    print(f'{rectangle.rectangle_area()=}\n'
          f'{rectangle.rectangle_perimeter()=}\n'
          f'{square.rectangle_perimeter()=}\n'
          f'{square.rectangle_area()=}')
