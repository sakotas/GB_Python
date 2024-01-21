num = 255
hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

hex_result = ''
original_num = num

if num == 0:
    hex_result = '0'
else:
    while num > 0:
        remainder = num % 16
        hex_result = hex_dict[remainder] + hex_result
        num = num // 16

print(f"Шестнадцатеричное представление числа: {hex_result}")
print(f"Проверка результата: {hex(original_num)}\n")
