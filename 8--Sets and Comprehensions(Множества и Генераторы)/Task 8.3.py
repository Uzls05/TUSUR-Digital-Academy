N = int(input("Введите N: "))

result = [
    x*2
    for x in range(1, N)
    if x % 2 != 0
]
print(result)

input()