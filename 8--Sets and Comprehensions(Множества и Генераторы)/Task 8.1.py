elements_list = list(map(int, input("Введите элементы списка через пробел: \n").split()))

not_unic_elements = [
    x for x in elements_list
    if elements_list.count(x) > 1
]

print(not_unic_elements)

input()
