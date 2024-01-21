import string

text = 'Hello world. Hello Python. Hello again.'

# Удаляем знаки препинания и приводим текст к нижнему регистру
text = text.translate(str.maketrans('', '', string.punctuation)).lower()

# Разделяем текст на слова
words = text.split()

# Создаем словарь для подсчета слов
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Сортируем слова по частоте встречаемости и берем топ-10
top_10 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_10)