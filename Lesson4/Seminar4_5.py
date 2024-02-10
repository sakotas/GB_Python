# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

names_list = ["Alex", "Misha", "Lesha"]
salary_list = [100, 200, 300]
award_list = ['10.00%', '5.00%', '10.00%']


def calculate_salary(names: list[str],
                     salary: list[int],
                     award: list[str]) -> dict[str, float]:
    result_dict = dict()

    for name, base_salary, percent in zip(names, salary, award):
        result_dict[name] = round(base_salary * (float(percent.replace("%", "")) / 100), 2)

    return result_dict


def convert_percent_to_float(percent_str):
    return float(percent_str.strip('%'))


award_dict = calculate_salary(names_list, salary_list, award_list)
print(award_dict)
