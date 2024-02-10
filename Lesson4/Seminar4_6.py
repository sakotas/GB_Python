# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

list_of_numbers = [0, 1, 2, 3, 4, 5, 6]


def sum_between_indexes(numbers: list[int], index_one: int, index_two: int) -> int:
    if index_one > index_two:
        temp = index_one
        index_one = index_two
        index_two = temp

    if index_one < 0:
        index_one = 0
    if index_two > len(numbers):
        index_two = len(numbers)

    return sum(numbers[index_one + 1:index_two])


print(sum_between_indexes(list_of_numbers, 1, 4))
print(sum_between_indexes(list_of_numbers, 1, 7))
print(sum_between_indexes(list_of_numbers, -1, 4))
