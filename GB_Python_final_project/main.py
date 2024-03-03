import sys
from Logic.DirectoryScanner import scan_directory


def main() -> None:
    """
    Главная функция, обрабатывающая ввод пользователя из командной строки и выводящая информацию о файлах
    и каталогах в указанной директории.
    """
    if len(sys.argv) != 2:
        print("Usage: main.py <directory_path>")
        return
    directory_path = sys.argv[1]
    contents = scan_directory(directory_path)
    for item in contents:
        print(item)


if __name__ == "__main__":
    main()
