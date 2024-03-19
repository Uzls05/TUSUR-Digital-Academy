# Task 1(Последний с четными)
elements = list(map(int, input('Введите целочисленный список через пробел  \n').split()))
if elements:
    elements_sum = sum(elements[::2])  # Sum of all even elements by index
    elements_last = elements[-1]  # Last element in list
    result = elements_sum * elements_last
    print(f'Список = {elements} , Результат = {result}')
else:
    print(f'Список = {elements} , Результат = {0}')

input()