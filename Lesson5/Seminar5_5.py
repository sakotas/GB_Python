# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# def task5():
#     for i in range(1, 100):
#         if i % 15 == 0:
#             print('FizzBuzz')
#             yield i
#         elif i % 3 == 0:
#             print('Fizz')
#             yield i
#         elif i % 5 == 0:
#             print('Buzz')
#             yield i
#         else:
#             print(i)
#             yield i


# for i in range(1, 101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     else:
#         if i % 3 == 0:
#             print('Fizz')
#         else:
#             if i % 5 == 0:
#                 print('Buzz')
#             else:
#                 print(i)

# list_0 = ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(101)]

print(*['FizzBuzz' if i % 15 == 0
        else 'Fizz' if i % 3 == 0
        else 'Buzz' if i % 5 == 0
        else i for i in range(101)], sep='\n')

# for i in range(1, 100):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 and i % 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)

# gen = task5()
# for _ in range(101):
#     print(next(gen))
# print(list(task5()))
#
# for _ in task5():
#     pass
