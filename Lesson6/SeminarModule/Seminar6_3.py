# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию.

from datetime import date

__all__ = ['parse_data']

_LEAP_YEAR_MAIN_CONDITION = 4
_LEAP_YEAR_ADD_CONDITION_1 = 100
_LEAP_YEAR_EXCEPTION_YEAR = 400


def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return is_valid_day(d, m, y) and is_valid_month(m) and is_valid_year(y)


def is_valid_day(day: int, month: int, year: int) -> bool:
    if day in range(29 + 1) and _is_leap_year(year) and month == 2:
        return True
    elif day in range(28 + 1) and month == 2:
        return True
    elif day in range(31 + 1) and month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif day in range(30 + 1) and month in [4, 6, 9, 11]:
        return True
    else:
        return False


def is_valid_month(month: int) -> bool:
    return month in range(12 + 1)


def is_valid_year(year: int) -> bool:
    return year in range(1, 9999 + 1)


def _is_leap_year(year: int) -> bool:
    return (year % _LEAP_YEAR_MAIN_CONDITION == 0
            and year % _LEAP_YEAR_ADD_CONDITION_1 != 0
            or year % _LEAP_YEAR_EXCEPTION_YEAR == 0)


if __name__ == '__main__':
    print(parse_data('29.02.2024'))
