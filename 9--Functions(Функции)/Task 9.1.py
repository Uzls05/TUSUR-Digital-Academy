def reverse_digits(n):
    """
    Возвращает список всех цифр этого числа в обратном порядке
    """
    return [int(d) for d in str(n)[::-1]]

print(reverse_digits(123))