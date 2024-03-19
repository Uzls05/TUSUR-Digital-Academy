# Task 2 (Max-min)
elements = list(map(float, input('Введите численный список(Через пробел) \n').split()))
if elements:
    elements_max = max(elements) # Min element in list
    elements_min = min(elements) # Max element in list
    elements_difference = elements_max - elements_min
    print(f'Список = {elements} , Результат = {elements_difference:.1f}')
else:
    print(f'Список = {elements} , Результат = {0}')

input()