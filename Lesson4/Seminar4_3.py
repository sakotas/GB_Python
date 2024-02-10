# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

import json
import os

global_dictionary = dict()


def task3(input_str: str) -> dict[int, str]:
    """
    Make dictionary from console input.

    :param input_str:
    :return:
    """
    result_dictionary = dict()
    global global_dictionary

    input_string_list = input_str.split()
    result_dictionary[ord(input_string_list[0])] = input_string_list[1]
    global_dictionary[ord(input_string_list[0])] = input_string_list[1]

    return result_dictionary


def append_to_json_file(dictionary, file_path='./dictionary.json'):
    data = {}

    # Проверяем, существует ли файл и не пустой ли он
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Загружаем существующие данные

    # Обновляем данные новыми значениями из словаря
    data.update(dictionary)

    # Перезаписываем файл с обновленными данными
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def save_dict_to_file(dictionary: dict, file_path='./dictionary.json'):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)


while True:
    user_input = input('>>> ')

    if user_input == '0':
        append_to_json_file(global_dictionary)
        print(global_dictionary)
        break
    else:
        task3(user_input)
        print(global_dictionary)
        continue
