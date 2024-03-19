x = 1
y = 2
z = 4
n = 2

# Создание Всех Перестановок По Заданным Значениям
permutations = [[i, j, k]
                for i in [x, y, z]
                for j in [x, y, z]
                for k in [x, y, z]
                if len({i, j, k}) == 3]
# Создание Перестановок Которые Подходят По Условию (x + y - z) > n
filtered_permutations = [perm
                         for perm in permutations
                         if perm[0] + perm[1] - perm[2] > n]

print(filtered_permutations)