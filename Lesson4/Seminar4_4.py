# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

numbers_list = [0, 2, 1, 5, 22, 64, 2, 1, 5]


def bubble_sort(arr: list[int]) -> None:
    """
    Bubble sort.

    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        # Флаг, который показывает, были ли перестановки в этом проходе
        swapped = False
        # Проходимся по массиву, сравнивая пары элементов
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если перестановок не было, массив уже отсортирован
        if not swapped:
            break


print(numbers_list)
bubble_sort(numbers_list)
print(numbers_list)
