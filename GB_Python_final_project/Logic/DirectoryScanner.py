from collections import namedtuple
import os
from typing import List

# Определение namedtuple для хранения информации о файлах и каталогах.
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def scan_directory(directory_path: str) -> List[FileInfo]:
    """
    Сканирует указанную директорию и возвращает информацию о ее содержимом в виде списка объектов FileInfo.

    :param directory_path: Путь к директории, которую нужно сканировать.
    :return: Список объектов FileInfo с информацией о содержимом директории.
    """
    directory_contents = []
    for root, dirs, files in os.walk(directory_path):
        for d in dirs:
            directory_contents.append(
                FileInfo(name=d, extension=None, is_directory=True, parent_directory=os.path.basename(root)))
        for f in files:
            filename, file_extension = os.path.splitext(f)
            directory_contents.append(FileInfo(name=filename, extension=file_extension, is_directory=False,
                                               parent_directory=os.path.basename(root)))
    return directory_contents
