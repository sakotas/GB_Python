# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
#
# Напишите класс LotteryGame, который будет иметь метод compare_lists,
# который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2
#
# Если совпадающих чисел нет, то выведите на экран:
# Совпадающих чисел нет.
from collections import Counter

list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class LotteryGame:
    def __init__(self, list_a: list, list_b: list):
        self.list_a = list_a
        self.list_b = list_b

    def compare_lists(self):
        count_a = Counter(self.list_a)
        count_b = Counter(self.list_b)
        common_elements = count_a & count_b
        result_list = list(common_elements.elements())
        if len(result_list) == 0:
            print('Совпадающих чисел нет.')
        else:
            print(f'Совпадающие числа: {result_list}')
            print(f'Количество совпадающих чисел: {len(result_list)}')


if __name__ == '__main__':
    game1 = LotteryGame(list1, list2)
    matching_numbers = game1.compare_lists()
