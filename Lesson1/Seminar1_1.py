# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = 120
e = 3
res = 0

for i in range(0, n + 1, 2):
    if i % e != 0:
        res += i
print(res)
