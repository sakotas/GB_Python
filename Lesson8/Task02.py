# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os.path

my_dict = {}

if os.path.isfile('Task02.json') and os.path.getsize('Task02.json') > 0:
    with open('Task02.json', 'r+' if os.path.isfile('Task02.json') else 'w', encoding='utf8') as json_file:
        my_dict = json.load(json_file)
        print(my_dict, '\n', type(my_dict))

while True:
    user_input = input('>>> ')

    if user_input == 'quit':
        break

    user_name = user_input.split(' ')[0]
    user_id = user_input.split(' ')[1]
    access_level = user_input.split(' ')[2]

    try:
        if len(user_input.split(' ')) != 3 or int(access_level) > 7 or int(access_level) < 1:
            print('Введите в верном формате')
            continue
    except ValueError:
        print('Введите в верном формате')
        continue

    user_id_exists = False

    for outer_key, list_of_inner_dics in my_dict.items():
        for inner_key in list_of_inner_dics:
            if user_id in inner_key:
                print('Пользователь с таким user_id уже есть')
                break
        if user_id_exists:
            break

    if not user_id_exists:
        # my_dict.setdefault(access_level, []).append({user_id: user_name})
        my_dict.setdefault(access_level, {})
        my_dict[access_level].setdefault(user_id, user_name)
        with open('Task02.json', 'w', encoding='utf8') as json_file:
            json.dump(my_dict, json_file, indent=2, ensure_ascii=False)
