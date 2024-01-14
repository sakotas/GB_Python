# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math

diameter = float(input('>>> '))
decimal.getcontext().prec = 48

radius = decimal.Decimal(diameter / 2)
PI = decimal.Decimal(3.14158265358979348846264335202950289372841939375)
area = PI * radius * radius
length = 2 * PI * radius

print(f"Площадь круга: {area} \n"
      f"Длина окружности: {length}")
