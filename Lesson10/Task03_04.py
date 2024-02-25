# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст


class DataPerson:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.__age = age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"---\n{self.name=} \n{self.surname=} \n{self.__age=}"


# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Employee(DataPerson):

    def __init__(self, id: int, *args, **kwargs):
        if len(str(id)) != 6:
            raise ValueError('Значение должно быть шестизначным')
        else:
            self.id = id
        self.level = sum(map(int, str(id))) % 7
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__() + f' \n{self.id=} \n{self.level=}'


if __name__ == '__main__':
    human_1 = DataPerson('Petr', 'Petrov', 27)
    human_2 = DataPerson('Sergey', 'Serov', 30)
    print(human_1)
    print(human_2)
    employee_1 = Employee(123321, 'Ivan', 'Jovanovich', 40)
    print(employee_1)
