# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

inputs_list = ["Привет, мир!", "Hello World!", "Мороз и солнце, день чудесный!"]

def task1(test_input:str) -> str:
    """ Parse.

    
    """
    input_words_list = test_input.split()
    input_words_list.sort()

    max_length = 0
    for item in input_words_list:
        if len(item) > max_length: max_length = len(item)

    res = ''
    for i, elem in enumerate(input_words_list, 1):
        res += f'{i}. {elem:>{max_length}}\n'
    return res


for item in inputs_list:
    print(task1(item))

custom_input = input(">>> ")
print(task1(custom_input))
