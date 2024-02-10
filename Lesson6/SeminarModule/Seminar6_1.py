# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.
import random as rnd

__all__ = ['guessing_game']
def guessing_game(min_number=1, max_number=10, tries=5):
    guessing_number = rnd.randint(min_number, max_number)
    result = False

    for _ in range(tries):
        user_input = int(input('>>> '))
        if user_input == guessing_number:
            result = True
            break
        elif user_input < guessing_number:
            print('меньше')
        elif user_input > guessing_number:
            print('больше')
    return result


if __name__ == "Seminar6_1":
    print(f"Импортирован модуль {__name__}")

if __name__ == '__main__':
    # print(guessing_game(1, 10, 5))
    print(__name__)
