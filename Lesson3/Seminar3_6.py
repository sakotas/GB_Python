# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

inputs_list = ["Привет, мир!", "Hello World!", "Мороз и солнце, день чудесный!"]


# test_input = "Привет, мир, Арбуз!"

def task6(test_input):
    input_words_list = test_input.split()
    input_words_list.sort()

    max_length = 0
    for item in input_words_list:
        if len(item) > max_length: max_length = len(item)

    for i, elem in enumerate(input_words_list, 1):
        print(f'{i}. {elem:>{max_length}}')
    print()


for item in inputs_list:
    task6(item)
