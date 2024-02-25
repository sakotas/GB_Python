# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from datetime import datetime


class MyString(str):
    def __new__(cls, my_string: str, *args, **kwargs):
        return super().__new__(cls, my_string)

    def __init__(self, *args):
        _, name, *_ = args
        self.name = name
        self.time = datetime.now()


class NewMyString(str):
    """ Класс NewMyString где на вход поступают:
    value - со всеми возможностями str;
    name = имя автора строки.

    Дополнительно:
    time = время создания (time.time) """

    def __new__(cls, value: str, name: str = None):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = datetime.now()
        return instance


if __name__ == '__main__':
    s1 = MyString('string1', 'Author1')
    print(type(s1))
    print(f'{s1.name=}\n'
          f'{s1.time=}\n'
          f'{s1=}\n'
          f'{s1.capitalize()=}')
    print(s1.__dict__)
    print()

    s2 = NewMyString('string2', 'Author2')
    print(type(s2))
    print(f'{s2.name=}\n'
          f'{s2.time=}\n'
          f'{s2=}\n'
          f'{s2.capitalize()=}')
    print(s2.__dict__)
