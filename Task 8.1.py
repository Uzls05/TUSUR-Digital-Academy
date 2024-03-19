elements_list = list(input("Введите элементы списка без пробела: \n"))

not_unic_elements = [
    x for x in elements_list
    if elements_list.count(x) > 1
]

print(not_unic_elements)

input()
