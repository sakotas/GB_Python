# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

new_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

for item in new_list:
    while new_list.count(item) > 3:
        new_list.remove(item)

print(new_list)
