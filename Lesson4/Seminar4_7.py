# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

test_dict1 = {"Газпром": [100.00, -100.00, 100.00],
              "Лукойл": [200.00, -200.00, 100.00],
              "Татнефть": [150.00, -150.00, 100.00]}
test_dict2 = {"Газпром": [100.00, -100.00, 100.00],
              "Лукойл": [200.00, -200.00, 100.00],
              "Татнефть": [150.00, -150.00, -100.00]}


# def is_all_profit(dictionary: dict[str, list[float]]) -> bool:
#     result_revenue_dict = dict()
#     surplus_flag = True
#
#     for name, revenue in dictionary.items():
#         result_revenue_dict[name] = sum(revenue)
#         if sum(revenue) < 0:
#             surplus_flag = False
#         print(f'Фирма: {name}, Прибыль/Убыток: {sum(revenue)}')
#     print(result_revenue_dict)
#
#     return surplus_flag

def is_all_profit(dictionary: dict[str, list[float]]) -> bool:
    return all(map(lambda v: sum(v) >= 0, dictionary.values()))


print(is_all_profit(test_dict1))
print(is_all_profit(test_dict2))
