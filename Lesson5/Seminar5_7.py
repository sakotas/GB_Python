# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_simple(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def task7(number: int):
    i = 2
    yield i
    i += 1
    while i <= number:
        if is_simple(i):
            yield i
        i += 2
    #
    # for i in range(2, n + 1):
    #     if is_simple(i):
    #         yield i


generator_value = task7(27)

for _ in range(27):
    print(next(generator_value))
