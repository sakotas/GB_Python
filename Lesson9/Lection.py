from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'{func = }')
        return func(*args, **kwargs)

    return wrapper


def sum(a, b):
    return a + b


new_sum = decorator(sum)
print(new_sum(1, 2))
# first = add_one_str('Hello')
# print(first)
# print(first('Friends!'))
# print(add_one_str('Hello')('world!'))
