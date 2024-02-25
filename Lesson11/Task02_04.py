# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра
# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    _instance = None

    def __new__(cls, text: str, name: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_text = []
            cls._instance.all_name = []
        else:
            cls._instance.all_text.append(cls._instance.text)
            cls._instance.all_name.append(cls._instance.name)
        return cls._instance

    def __init__(self, text: str, name: str):
        self.text = text
        self.name = name

    def __str__(self):
        return f'Экземпляр класса Archive. Текущий текст: {self.text}'

    def __repr__(self):
        return f'Archive({self.text=}, {self.name=}, {self.all_name=}, {self.all_text=})'


if __name__ == '__main__':
    archive1 = Archive('Hello', 'Jo')
    print(f'{archive1=}, {archive1.all_name=}, {archive1.all_text=}')
    archive2 = Archive('Good bye!', 'Stan')
    print(f'{archive2=}, {archive2.all_name=}, {archive2.all_text=}')
    archive3 = Archive('go away', 'Lolli')
    print(f'{archive3=}, {archive3.all_name=}, {archive3.all_text=}')
    print(f'\n{archive1.__dict__} \n{archive2.__dict__} \n{archive3.__dict__}')
    print()
    print(archive1)
    print(repr(archive1))
