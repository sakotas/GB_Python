# Создание класса-фабрики для животных
# Создайте базовый класс Animal, который имеет атрибут name,
# представляющий имя животного.
#
# Создайте классы Bird, Fish и Mammal, которые наследуются
# от базового класса Animal и добавляют дополнительные атрибуты и методы:
# - Bird имеет атрибут wingspan (размах крыльев) и
# метод wing_length, который возвращает длину крыла птицы.
# - Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth,
# который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная)
# в зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10,
# то она относится к категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100,
# то она относится к категории "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
# - Mammal имеет атрибут weight (вес) и метод category,
# который возвращает категорию млекопитающего (Малявка, Обычный, Гигант)
# в зависимости от веса.
# Если вес объекта меньше 1, то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".
#
# Создайте класс-фабрику AnimalFactory,
# который будет создавать экземпляры животных разных типов
# на основе переданного типа и параметров.
# Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# - animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# - *args - переменное количество аргументов, представляющих параметры для конкретного типа животного.
# Количество и типы аргументов могут различаться в зависимости от типа животного.
# - Метод create_animal должен создавать и возвращать экземпляр животного
# заданного типа с переданными параметрами.
# Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal',
# функция вызовет ValueError с сообщением 'Недопустимый тип животного'.

class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: int | float):
        self.wingspan = wingspan
        super().__init__(name)

    def wing_length(self) -> float:
        return float(self.wingspan) / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: int | float):
        self.max_depth = max_depth
        super().__init__(name)

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name: str, weight: int | float):
        self.weight = weight
        super().__init__(name)

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        return "Обычный"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')


if __name__ == '__main__':
    # b1 = Bird('Bird1', 10.0)
    # b2 = Bird('Bird2', 15)
    # f1 = Fish('Fish1', 50)
    # f2 = Fish('Fish2', 5)
    # f3 = Fish('Fish2', 500)
    # m1 = Mammal('Mammal1', 0.5)
    # m2 = Mammal('Mammal2', 3)
    # m3 = Mammal('Mammal3', 300)
    # print(f'{b1.wing_length()=}\t{b2.wing_length()=}')
    # print(f'{f1.depth()=}\t{f2.depth()=}\t{f3.depth()=}')
    # print(f'{m1.category()=}\t{m2.category()=}\t{m3.category()=}')
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
    print(f'---\n{animal1.wingspan=}\n{animal1.name=}\n{animal1.wing_length()=}')
    print(f'---\n{animal2.name=}\n{animal2.max_depth=}\n{animal2.depth()=}')
    print(f'---\n{animal3.name=}\n{animal3.weight=}\n{animal3.category()=}')
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())
