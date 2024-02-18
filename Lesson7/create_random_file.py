# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import os.path
import pathlib
import random
import string

VOWELS = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
CONSONANTS = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


def create_random_file(strings_amount: int, filename_: str) -> None:
    directory = './data'
    filepath = f'{directory}/{filename_}.txt'
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_exists = os.path.isfile(filepath)
    mode = 'a' if file_exists else 'w'

    with open(filepath, mode, encoding='utf-8') as f:
        for _ in range(strings_amount):
            f.write(generate_content())


def generate_content() -> str:
    return f'{random.randint(-1000, 1000)}|{random.uniform(-1000.00, 1000.00):.2f}\n'


# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл
def create_file_with_random_names(amount_of_names: int, file_name: str) -> None:
    save_names_in_file(generate_names_list(amount_of_names), file_name)


def save_names_in_file(names: list[str], file_name: str) -> None:
    filepath = f'data/{file_name}.txt'
    file_exists = os.path.isfile(filepath)
    mode = 'a' if file_exists else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        for i in names:
            f.write(i + '\n')


def generate_names_list(amount_of_names: int) -> list[str]:
    result_list = []
    for _ in range(amount_of_names):
        result_list.append(_generate_random_name())
    return result_list


def _generate_random_name() -> str:
    result = ''

    for i in range(random.randint(4, 7)):
        if i % 2 == 0:
            result += random.choice(VOWELS)
        else:
            result += random.choice(CONSONANTS)

    return result.capitalize()


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
def read_files():
    with (open('./data/Test1.txt', 'r+', encoding='utf-8') as numbers_file,
          open('./data/names.txt', 'r+', encoding='utf-8') as names_file,
          open('./data/results.txt', 'a', encoding='utf-8') as results_file):

        max_length = max(len(names_file.read().split('\n')[:-1]), len(numbers_file.read().split('\n')[:-1]))

        for line in range(max_length):
            read_name = my_readline(names_file).replace('\n', '')
            read_number = my_readline(numbers_file)
            new_int = int(read_number.split('|')[0])
            new_float = float(read_number.split('|')[1])
            new_num = new_int * new_float
            if new_num < 0:
                results_file.write(f'{read_name.lower()} {abs(new_num)}\n')
            else:
                results_file.write(f'{read_name.upper()} {round(new_num)}\n')


def my_readline(file):
    line = file.readline()
    if line == '':
        file.seek(0)
        return file.readline()
    return line


# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

def generate_file(extension: str,
                  min_name_length: int = 6,
                  max_name_length: int = 30,
                  min_bytes: int = 256,
                  max_bytes: int = 4096,
                  files_qty: int = 42) -> None:
    """
    Генерирует файлы с произвольным содержимым.

    :param extension: Расширение генерируемых файлов.
    :param min_name_length: Минимальная длина имени файла.
    :param max_name_length: Максимальная длина имени файла.
    :param min_bytes: Минимальный размер файла в байтах.
    :param max_bytes: Максимальный размер файла в байтах.
    :param files_qty: Количество генерируемых файлов.
    """
    for i in range(files_qty):
        with open(f'./data/files_output/{generate_file_name(min_name_length, max_name_length)}.{extension}',
                  'w') as file:
            file.write(f'{generate_bytes(min_bytes, max_bytes)}')


def generate_file_name(min_name_length: int, max_name_length: int) -> str:
    """
    Генерирует имя файла заданной длины.

    :param min_name_length: Минимальная длина имени файла.
    :param max_name_length: Максимальная длина имени файла.
    :return: Строка с именем файла.
    """
    result_name = ''
    for i in range(random.randint(min_name_length, max_name_length)):
        result_name += random.choice(string.ascii_letters)
    return result_name


def generate_bytes(min_bytes: int, max_bytes: int) -> bytes:
    """
    Генерирует случайный набор байтов заданного размера.

    :param min_bytes: Минимальный размер набора байтов.
    :param max_bytes: Максимальный размер набора байтов.
    :return: Байтовый объект заданного размера.
    """
    return bytes(list(random.randint(0, 255) for i in range(random.randint(min_bytes, max_bytes))))

def sort_files():
    curr_path = pathlib.Path('./data/files_output')
    for file in curr_path.iterdir():
        try:
            file.replace(f'{file.suffix}/{file.name}')
        except FileNotFoundError:
            os.mkdir(f'{file.suffix}')
            file.replace(f'{file.suffix}/{file.name}')


if __name__ == '__main__':
    # create_random_file(50, 'Test1')
    # create_file_with_random_names(75, 'names')
    # read_files()
    # generate_file('avi')
    sort_files()
