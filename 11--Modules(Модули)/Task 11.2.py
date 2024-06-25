import itertools


def f(list1, list2):
    return list(itertools.chain(list1, list2))


print(list(f([1, 2], [3, 4, 5])))
