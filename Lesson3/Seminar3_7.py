# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

test_input = ("Мороз и солнце, день чудесный!"
              "Беги, беги, беги"
              "Беги на край земли")
my_dict = {}
my_dict_2 = {}

for item in test_input:
    my_dict.setdefault(item, 0)
    my_dict[item] += 1

for k, v in my_dict.items():
    print(f'Key: {k}\n'
          f'Count: {v}\n')

for item in test_input:
    my_dict_2[item] = test_input.count(item)

for k, v in my_dict_2.items():
    print(f'Key: {k}\n'
          f'Count: {v}\n')

print(my_dict)
print(my_dict_2)