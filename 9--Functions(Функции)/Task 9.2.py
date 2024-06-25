def is_palindrome(word):
    """
     Возвращает True, если слово палиндромом, иначе False.
    """
    return word == word[::-1]


print(is_palindrome('hi'))

print(is_palindrome('lol'))

print(is_palindrome('peep'))
