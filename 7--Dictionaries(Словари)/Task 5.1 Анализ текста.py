text = "hello, word of word"
chars_popularity = {}
words_popularity = {}

for char in text:
    if char.isalpha():  # Проверяем, является ли символ буквой
        char = char.lower()  # Приводим букву к нижнему регистру
        if char in chars_popularity:
            chars_popularity[char] += 1
        else:
            chars_popularity[char] = 1

words = text.split()
for word in words:
    word = word.lower()  # Приводим слово к нижнему регистру
    word = word.strip(",.")  # Удаляем знаки препинания
    if word in words_popularity:
        words_popularity[word] += 1
    else:
        words_popularity[word] = 1
print(f'text = {text}',end='\n\n')
print("chars_popularity:", chars_popularity,end='\n\n')
print("words_popularity:", words_popularity)

input()
