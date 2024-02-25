# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint
from typing import Callable


def game(func):
    def wrapper(question_number: int, qty_number: int):
        print('Выполняем проверки')
        if not 1 <= question_number <= 100:
            question_number = randint(1, 100)
        if not 1 <= qty_number <= 10:
            qty_number = randint(1, 10)
        return func(question_number, qty_number)

    return wrapper


@game
def run(question_number: int, qty_number: int):
    for _ in range(qty_number):
        answer = int(input('Введите ответ: '))
        if question_number == answer:
            print('Победа!')
            return True
    print('Лох, проиграл')
    return False


if __name__ == '__main__':
    run(7, 6)
