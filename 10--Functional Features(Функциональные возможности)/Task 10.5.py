def f(n):
    for x in range(n + 1):
        if x == 0:
            yield -10
        elif x % 3 == 0:
            yield 45
        elif x % 5 == 0:
            yield x / 5 + 93
        else:
            yield x / 2


n = 3
print(list(f(n)))

n = 7
print(list(f(n)))
