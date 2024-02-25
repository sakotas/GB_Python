# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
import os
from functools import wraps
from random import randint
from typing import Callable
import Task03
import Task04


def value_checker(func):
    @wraps(func)
    def wrapper(question_number: int, qty_number: int):
        print(f'Выполняем проверки функции {func.__name__}')
        if not 1 <= question_number <= 100:
            question_number = randint(1, 100)
        if not 1 <= qty_number <= 10:
            qty_number = randint(1, 10)
        return func(question_number, qty_number)

    return wrapper


@Task04.count_deco(3)
@Task03.json_cache
@value_checker
def Task05_func(question_number: int, qty_number: int):
    for _ in range(qty_number):
        answer = int(input('Введите ответ: '))
        if question_number == answer:
            print('Победа!')
            return True
    print('Лох, проиграл')
    return False


if __name__ == '__main__':
    Task05_func(2, 5)
    Task05_func(7, 1)
    Task05_func(3, 7)
