def power_list(x, y):
    return [x**y for x, y in zip(X, Y)]


X = [2, 3, 4]
Y = [10, 11, 12]
result = power_list(X, Y)
print(result)