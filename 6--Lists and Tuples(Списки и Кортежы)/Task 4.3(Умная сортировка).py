#Task 3(Умная сортировка)
elements = tuple(map(int, input('Введите численный кортеж через пробел  \n').split()))
elements_sorted = sorted(elements, key = abs)
print(f'Кортеж = {elements}, Результат = {elements_sorted}')

input()