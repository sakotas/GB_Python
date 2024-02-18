# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import hashlib
import json


def read_csv(csv_filepath: str) -> list:
    result = []
    with open(csv_filepath, 'r', newline='', encoding='utf-8') as csv_file:
        csv_dict = csv.reader(csv_file)
        for i, row in enumerate(csv_dict):
            if i != 0:
                result.append(row)
    return result


def extend_ids(data: list) -> None:
    for item in data:
        if len(item) > 0:
            item[0] = item[0].zfill(10)


def capitalize_first_letter(data: dict) -> None:
    for item in data:
        if len(item) > 1:
            item[1] = item[1].capitalize()


def generate_hash(data: list) -> None:
    for item in data:
        if len(item) > 1:
            string_to_hash = item[0] + item[1]
            hash_string = hashlib.sha256(string_to_hash.encode()).hexdigest()
            item.append(hash_string)


def list_to_dict(list_: list) -> dict:
    result_dict = {}
    for i, list_ in enumerate(list_):
        result_dict[i] = list_
    return result_dict


def save_to_json(data: dict, json_output_filepath: str) -> None:
    data_to_save = []
    for item in data:
        if len(item) >= 3:
            data_dict = {"id": item[0], "name": item[1], "access_level": item[2], "hash": item[3]}
            data_to_save.append(data_dict)

    with open(json_output_filepath, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, indent=2, ensure_ascii=False)


def Task04(csv_filepath: str, json_output_filepath: str) -> None:
    data_dict = read_csv(csv_filepath)
    extend_ids(data_dict)
    capitalize_first_letter(data_dict)
    generate_hash(data_dict)
    save_to_json(data_dict, json_output_filepath)


if __name__ == '__main__':
    Task04('Task03.csv', 'Task04.json')
