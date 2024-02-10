# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def generate_list_unicode(text: str) -> list[int]:
    list_unicode = set()
    for char in text:
        list_unicode.add(ord(char))
    return sorted(list_unicode, reverse=True)


text = "Сформируйте список с уникальными кодами Unicode каждого"

for i, value in enumerate(generate_list_unicode(text), 1):
    print(f'{i}. {value}')
