# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

mydict = {}


def txt_to_json(source='results.txt', result='new_json.json') -> None:
    with (open('results.txt', 'r', encoding='utf-8') as read_file,
          open('new_json.json', 'w', encoding='utf-8') as write_file):
        results_list = read_file.readlines()
        for line in range(len(results_list)):
            mydict[results_list[line].split(' ')[0].capitalize()] = float(
                results_list[line].split(' ')[1].replace('\n', ''))

        print(mydict)

        json.dump(mydict, write_file, indent=4, ensure_ascii=False)

txt_to_json()
