# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

new_list = [1, 1, 2, 2, 1, 3, 4, 4, 5, 12, 13]

my_dict = {}
uniq_list = []
counter = 1

for i, item in enumerate(new_list, 1):
    if item % 2 != 0:
        my_dict[counter] = item
        counter += 1

for k, v in my_dict.items():
    print(f'Ключ: {k}\n'
          f'Значение: {v}\n')

print()

for i, item in enumerate(new_list, 1):
    if item % 2 != 0:
        uniq_list.append(i)

for i in uniq_list:
    print(i)
