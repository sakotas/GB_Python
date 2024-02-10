# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

my_listcomp = [int(i) for i in range(2, 100, 2) if (i % 10) + (i // 10) != 8]

print(my_listcomp)

# i = 26
#
#
# def calculate(x):
#     x = int(i % 10)
#     j = int(i // 10)
#     k = x + j
#     return k
#
#
# print(calculate(i))
