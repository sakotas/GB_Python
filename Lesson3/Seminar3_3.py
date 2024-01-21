# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data_tuple = (2.8, 10, 15, 8.53, 'Hello World!', 'Привет, Мир!', [1, 2], [65, 18])

my_dict = {}

for item in data_tuple:
    my_dict.setdefault(type(item), [])
    my_dict[type(item)].append(item)

for k, v in my_dict.items():
    print(k, '\n', v)
