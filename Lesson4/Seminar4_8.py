# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

name = "s"
names = ""
number = 1
numbers = [1, 2]
s = 's'


def print_attributes_end_with_s() -> list:
    return list(filter(lambda v: not v.startswith('__') and v.endswith('s') and len(v) != 1, globals()))
    print(list(filter(lambda v: not v.startswith('__') and v.endswith('s') and len(v) != 1, globals())))


print_attributes_end_with_s()
lol = print_attributes_end_with_s()
print(lol)