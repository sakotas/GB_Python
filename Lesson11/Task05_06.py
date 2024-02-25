# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, length: int | float, width: int | float = None):
        self.length = length
        self.width = width if width else length

    def rectangle_area(self):
        return self.width * self.length

    def rectangle_perimeter(self):
        return (self.width + self.length) * 2

    def __add__(self, other: 'Rectangle'):
        new_perimeter = self.rectangle_perimeter() + other.rectangle_perimeter()
        new_length = self.length + other.length
        new_width = (new_perimeter - new_length * 2) / 2
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimeter = abs(self.rectangle_perimeter() - other.rectangle_perimeter())
        new_length = abs(self.length - other.length)
        new_width = (new_perimeter - new_length * 2) / 2
        if new_width < 0:
            raise ValueError('Вычитание данных невозможно')
        return Rectangle(new_length, new_width)

    def __eq__(self, other: 'Rectangle'):
        return self.rectangle_area() == other.rectangle_area()

    def __gt__(self, other: 'Rectangle'):
        return self.rectangle_area() > other.rectangle_area()

    def __ge__(self, other: 'Rectangle'):
        return self.rectangle_area() > other.rectangle_area()

    def __str__(self):
        return f'Rectangle({self.width=}, {self.length=})'


if __name__ == '__main__':
    rectangle = Rectangle(5, 5)
    square = Rectangle(5)

    print(f'{rectangle.rectangle_area()=}\n'
          f'{rectangle.rectangle_perimeter()=}\n'
          f'{square.rectangle_perimeter()=}\n'
          f'{square.rectangle_area()=}')

    add_rectangle = rectangle + square
    print(add_rectangle)
    sub_rectangle = rectangle - square
    print(sub_rectangle)
