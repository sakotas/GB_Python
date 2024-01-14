# Проверка работы
print('Hello World')

# Блок 1
# a = 5
# print(id(a))
# a = 'Hello World'
# print(id(a))
# a = 5 / 2
# print(id(a))

# Блок 2 - Ветвление
# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     print('Но будьте осторожны')
# print('Работа завершена')

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     print('Но будьте осторожны')
# else:
#     print('Доступ запрещён')
# print('Работа завершена')

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     my_math = int(input('2 + 2 = '))
#     if 2 + 2 == my_math:
#         print('Вы в нормальном мире')
#     else:
#         print('Но будьте осторожны')
# else:
#     print('Доступ запрещён')
# print('Работа завершена')

# color = input('Твой любимый цвет: ')
# if color == 'красный':
#     print('Любитель яркого')
# elif color == 'зелёный':
#     print('Ты не охотник?')
# elif color == 'синий':
#     print('Ха, классика!')
# else:
#     print('Тебя не понять')

# color = input('Твой любимый цвет: ')
# match color:
#     case 'красный' | 'оранжевый':
#         print('Любитель яркого')
#     case 'зелёный':
#         print('Ты не охотник?')
#     case 'синий' | 'голубой':
#         print('Ха, классика!')
#     case _:
#         print('Тебя не понять')

# year = int(input('Введите год в формате yyyy: '))

# Option 1
# if year % 4 != 0:
#     print("Обычный")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("Високосный")
#     else:
#         print("Обычный")
# else:
#     print("Високосный")

# Option 2 - smaller
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Обычный")
# else:
#     print("Високосный")

# Check is in array
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Введи число: '))
# if num in data:
#     print('Леонардо передаёт привет!')
#
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Введи число: '))
# if num not in data:
#     print('Леонардо грустит :-(')

# Turn operator
# my_math = int(input('2 + 2 = '))
# print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')


## Loops Python
# num = float(input('Введите число: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2

## continue
# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)

## break
# min_limit = 0
# max_limit = 10
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ' + str(num))

## quit()
# min_limit = 0
# max_limit = 10
# count = 3
#
# while count > 0:
#     print('Попытка ' + str(count))
#     count -= 1
#     num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
#
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
#
# else:
#     print('Исчерпаны все попытки. Сожалею.')
#     quit()
#
# print('Было введено число ' + str(num))

## Loops for in
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

# num = int(input('Введите число: '))
# for i in range(0, num, 2):
#     print(i)

## Enumerate
# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i, animal)


