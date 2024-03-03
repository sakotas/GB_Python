import unittest
from Logic.DirectoryScanner import scan_directory, FileInfo
from typing import List


class TestDirectoryScanner(unittest.TestCase):
    def test_scan_directory(self) -> None:
        """
        Тестирование функции scan_directory на наличие возвращаемых данных.
        """
        test_directory = 'temp_test_directory'  # Путь к тестовой директории.
        contents = scan_directory(test_directory)
        self.assertTrue(len(contents) > 0)

    def test_file_info(self) -> None:
        """
        Тестирование, что каждый элемент, возвращаемый scan_directory, является экземпляром FileInfo.
        """
        test_directory = 'temp_test_directory'
        contents = scan_directory(test_directory)
        for item in contents:
            self.assertIsInstance(item, FileInfo)

    def test_file_extensions(self) -> None:
        """
        Тестирование, что расширения файлов в тестовой директории соответствуют ожидаемым.
        """
        test_directory = 'temp_test_directory'
        contents = scan_directory(test_directory)
        extensions = sorted([item.extension for item in contents if item.extension])
        expected_extensions = sorted(['.py', '.txt'])
        self.assertEqual(extensions, expected_extensions)


if __name__ == '__main__':
    unittest.main()
