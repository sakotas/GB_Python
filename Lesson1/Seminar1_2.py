MAIN_CONDITION = 4
ADD_CONDITION_1 = 100
EXCEPTION_YEAR = 400

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = int(input('Enter Year: '))

if (year % MAIN_CONDITION == 0
        and year % ADD_CONDITION_1 != 0
        or year % EXCEPTION_YEAR == 0):
    res = 'Visokos'
else:
    res = 'Ne visokos'

print(res)
