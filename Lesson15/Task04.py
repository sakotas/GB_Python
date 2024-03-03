# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import argparse
# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.


from datetime import datetime, date
from Task02 import log_decorator

MONTHS = [
    "января", "февраля", "марта",
    "апреля", "мая", "июня",
    "июля", "августа", "сентября",
    "октября", "ноября", "декабря"
]

DAYS = [
    "понедельник", "вторник", "среда",
    "четверг", "пятница", "суббота", "воскресенье"
]


@log_decorator
def string_to_date(s: str) -> datetime:
    weeks, weekday, month = s.split()

    weeks = int(weeks[0])
    y = datetime.now().year
    month_num = MONTHS.index(month) + 1
    weekday = DAYS.index(weekday) + 1
    first_day = date(day=1, month=month_num, year=y).isoweekday()
    day_by_date = (1 + 7 * weeks - (first_day - weekday)) \
        if weekday < first_day else (1 + 7 * (weeks - 1) - (first_day - weekday))

    return datetime(day=day_by_date, month=month_num, year=y)


def c1_parser():
    parser = argparse.ArgumentParser(description='String to Date')
    parser.add_argument('-w', '--weeks', default='1')
    parser.add_argument('-wd', '--weekdays', default='понедельник')
    parser.add_argument('-m', '--months', default='января')

    args = parser.parse_args()

    weekdays = args.weekdays if not args.weekdays.isdigit() else DAYS[int(args.weekdays) - 1]
    months = args.months if not args.months.isdigit() else MONTHS[int(args.months) - 1]

    return string_to_date(f'{args.weeks} {weekdays} {months}')


if __name__ == '__main__':
    print(c1_parser())
    # print(string_to_date('1-й четверг ноября'))
    # print(string_to_date('1-я суббота февраля'))
    # print(string_to_date('1-е воскресенье ноября'))
    # print(string_to_date('5-й четверг февраля'))
    # print(string_to_date('5-е воскресенье марта'))
    # print(string_to_date('5-я пятница мая'))
    # print(string_to_date('5-я пятница мая'))
