# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def json_to_csv(filepath: str, result_file: str) -> None:
    write_csv(open_json_to_dic(filepath), result_file)


def open_json_to_dic(filepath: str) -> dict:
    with open(filepath, 'r+', newline='', encoding='utf8') as json_file:
        result_dict = json.load(json_file)
    return result_dict


def write_csv(input_data: dict, result_file: str) -> None:
    with open(result_file, 'w', newline='', encoding='utf-8') as write_file:
        csv_write = csv.DictWriter(write_file,
                                   fieldnames=['id', 'name', 'access_level'],
                                   delimiter=',',
                                   quoting=csv.QUOTE_MINIMAL)

        csv_write.writeheader()
        for access_level, users in input_data.items():
            for user_id, user_name in users.items():
                row = {'id': user_id, 'name': user_name, 'access_level': access_level}
                csv_write.writerow(row)


if __name__ == '__main__':
    json_to_csv('Task02.json', 'Task03.csv')
