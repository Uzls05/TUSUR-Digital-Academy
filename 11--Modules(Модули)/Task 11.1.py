import random


def f(n):
    for i in range(n):
        yield random.uniform(0, n)


print(list(f(3)))
