# Задание №6.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

account_balance = 0
operations_counter = 0

while True:
    if operations_counter == 3:
        print(f'Вам начислен кэшбэк: {account_balance * 0.03}!')
        account_balance *= 1.03
        print(f'Новый баланс: {account_balance}')
        operations_counter = 0

    if account_balance >= 5000000:
        print(f'Вы слишком богаты. Государство забирает у вас: {account_balance * 0.1}')
        account_balance *= 0.9
        print(f'Новый баланс: {account_balance}')

    print(f'Баланс: {account_balance}')
    print('Введите (1-3): \n'
          '1 - пополнить\n'
          '2 - снять\n'
          '3 - выйти')

    case = int(input('>>> '))


    if case == 1:
        while True:
            s = int(input('Введите сумму пополнения: '))
            if s % 50 == 0:
                account_balance += s
                print(f'Баланс пополнен. Сумма на счете: {account_balance}')
                operations_counter += 1
                break
            else:
                print('Сумма должна быть кратна 50!')
                continue

    elif case == 2:
        while True:
            withdraw_amount = int(input('Введите сумму снятия: '))
            commission = max(min(withdraw_amount * 0.015, 600), 30)
            if account_balance >= withdraw_amount + commission:
                account_balance -= withdraw_amount + commission
                print(f'Успешное снятие! Новый баланс: {account_balance}')
                operations_counter += 1
                break
            else:
                print('Недостаточно средств')
                continue

    elif case == 3:
        print('Спасибо. До свидания!')
        break

    else:
        print('Неверный ввод')
        continue
