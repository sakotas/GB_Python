# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ результат.
# ○ аргументы вызова,


import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. В функцию {funcName} - {message}'
logging.basicConfig(format=FORMAT, filename='Task3.log', encoding='utf-8', style='{', level=logging.DEBUG)


def log_decorator(func):
    # Получаем логгер с именем оригинальной функции
    logger = logging.getLogger(func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # Формируем сообщение лога с явным указанием имени функции
        message = f'{func.__name__} - {args} {kwargs} {res}'
        # Записываем лог с сообщением
        logger.debug(message)
        return res

    return wrapper


@log_decorator
def division(x: int | float, y: int | float):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        return float('inf')


if __name__ == '__main__':
    division(2, 5)
    division(2, 0)
