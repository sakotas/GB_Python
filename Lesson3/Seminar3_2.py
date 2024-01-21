# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

user_input = input(">>> ")


def task3(test_input):
    if (test_input.isdigit() or test_input
            .replace('-', '')
            .isdigit()):
        return int(test_input)

    elif ('.' in test_input and test_input
            .replace('.', '', 1)
            .replace('-', '', 1)
            .isdigit()):
        return float(test_input)

    elif test_input.lower() != test_input:
        return test_input.lower()

    else:
        return test_input.lower()


print(task3(user_input), type(task3(user_input)))
