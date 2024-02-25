# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
import random
from functools import wraps
from typing import Callable


def count_deco(qty: int):
    def decor(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(qty):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return decor


@count_deco(5)
def task04_func(*args, **kwargs):
    a, b, c, *_ = args
    return f'{a + b + c + sum(kwargs.values())}'


if __name__ == '__main__':
    print(task04_func(1, 2, 3, 4,
                      a=random.randint(10, 20),
                      b=random.randint(10, 20),
                      c=random.randint(10, 20)))
